# 2928. Distribute Candies Among Children I

## Cpp

```cpp
class Solution {
public:
    int distributeCandies(int n, int limit) {
        int ways = 0;
        for (int a = 0; a <= limit; ++a) {
            for (int b = 0; b <= limit; ++b) {
                int c = n - a - b;
                if (c >= 0 && c <= limit) {
                    ++ways;
                }
            }
        }
        return ways;
    }
};
```

## Java

```java
class Solution {
    public int distributeCandies(int n, int limit) {
        int count = 0;
        int maxA = Math.min(limit, n);
        for (int a = 0; a <= maxA; a++) {
            int remainingAfterA = n - a;
            int maxB = Math.min(limit, remainingAfterA);
            for (int b = 0; b <= maxB; b++) {
                int c = remainingAfterA - b;
                if (c >= 0 && c <= limit) {
                    count++;
                }
            }
        }
        return count;
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
        from math import comb

        def ways(rem):
            if rem < 0:
                return 0
            # number of non‑negative integer solutions to x + y + z = rem
            return comb(rem + 2, 2)

        total = ways(n)
        L = limit
        exceed_one = 3 * ways(n - (L + 1))
        exceed_two = 3 * ways(n - 2 * (L + 1))
        exceed_three = ways(n - 3 * (L + 1))

        return total - exceed_one + exceed_two - exceed_three
```

## Python3

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb2(x: int) -> int:
            return x * (x - 1) // 2 if x >= 2 else 0

        L = limit + 1
        total = comb2(n + 2)

        # single variable exceeds limit
        s1 = n - L
        single = comb2(s1 + 2) if s1 >= 0 else 0

        # two variables exceed limit
        s2 = n - 2 * L
        double = comb2(s2 + 2) if s2 >= 0 else 0

        # all three variables exceed limit
        s3 = n - 3 * L
        triple = comb2(s3 + 2) if s3 >= 0 else 0

        return total - 3 * single + 3 * double - triple
```

## C

```c
int distributeCandies(int n, int limit) {
    int count = 0;
    for (int a = 0; a <= limit; ++a) {
        for (int b = 0; b <= limit; ++b) {
            int c = n - a - b;
            if (c >= 0 && c <= limit) {
                ++count;
            }
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int DistributeCandies(int n, int limit) {
        int count = 0;
        for (int a = 0; a <= limit; a++) {
            for (int b = 0; b <= limit; b++) {
                int c = n - a - b;
                if (c >= 0 && c <= limit) {
                    count++;
                }
            }
        }
        return count;
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
    let count = 0;
    const maxA = Math.min(limit, n);
    for (let a = 0; a <= maxA; a++) {
        const maxB = Math.min(limit, n - a);
        for (let b = 0; b <= maxB; b++) {
            const c = n - a - b;
            if (c >= 0 && c <= limit) {
                count++;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function distributeCandies(n: number, limit: number): number {
    let count = 0;
    const maxA = Math.min(limit, n);
    for (let a = 0; a <= maxA; a++) {
        const maxB = Math.min(limit, n - a);
        for (let b = 0; b <= maxB; b++) {
            const c = n - a - b;
            if (c >= 0 && c <= limit) {
                count++;
            }
        }
    }
    return count;
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
        $count = 0;
        for ($a = 0; $a <= $limit; $a++) {
            for ($b = 0; $b <= $limit; $b++) {
                $c = $n - $a - $b;
                if ($c >= 0 && $c <= $limit) {
                    $count++;
                }
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func distributeCandies(_ n: Int, _ limit: Int) -> Int {
        var count = 0
        let maxA = min(limit, n)
        for a in 0...maxA {
            let remainingAfterA = n - a
            let maxB = min(limit, remainingAfterA)
            for b in 0...maxB {
                let c = remainingAfterA - b
                if c >= 0 && c <= limit {
                    count += 1
                }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distributeCandies(n: Int, limit: Int): Int {
        var count = 0
        for (i in 0..limit) {
            for (j in 0..limit) {
                val k = n - i - j
                if (k >= 0 && k <= limit) {
                    count++
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int distributeCandies(int n, int limit) {
    int count = 0;
    for (int a = 0; a <= limit; ++a) {
      for (int b = 0; b <= limit; ++b) {
        int c = n - a - b;
        if (c >= 0 && c <= limit) {
          count++;
        }
      }
    }
    return count;
  }
}
```

## Golang

```go
func distributeCandies(n int, limit int) int {
	count := 0
	for a := 0; a <= limit; a++ {
		for b := 0; b <= limit; b++ {
			c := n - a - b
			if c >= 0 && c <= limit {
				count++
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def distribute_candies(n, limit)
  count = 0
  max_a = [limit, n].min
  (0..max_a).each do |a|
    max_b = [limit, n - a].min
    (0..max_b).each do |b|
      c = n - a - b
      count += 1 if c >= 0 && c <= limit
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def distributeCandies(n: Int, limit: Int): Int = {
        var count = 0
        for (a <- 0 to limit) {
            for (b <- 0 to limit) {
                val c = n - a - b
                if (c >= 0 && c <= limit) {
                    count += 1
                }
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i32 {
        let mut count = 0;
        let max_a = std::cmp::min(limit, n);
        for a in 0..=max_a {
            let remaining1 = n - a;
            let max_b = std::cmp::min(limit, remaining1);
            for b in 0..=max_b {
                let c = remaining1 - b;
                if c >= 0 && c <= limit {
                    count += 1;
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (distribute-candies n limit)
  (-> exact-integer? exact-integer? exact-integer?)
  (for/sum ([a (in-range 0 (+ limit 1))]
            [b (in-range 0 (+ limit 1))])
    (let ([c (- n a b)])
      (if (and (>= c 0) (<= c limit))
          1
          0))))
```

## Erlang

```erlang
-spec distribute_candies(N :: integer(), Limit :: integer()) -> integer().
distribute_candies(N, Limit) ->
    lists:foldl(
      fun(I, AccI) ->
          lists:foldl(
            fun(J, AccJ) ->
                K = N - I - J,
                if
                    K >= 0, K =< Limit -> AccJ + 1;
                    true -> AccJ
                end
            end,
            AccI,
            lists:seq(0, Limit)
          )
      end,
      0,
      lists:seq(0, Limit)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec distribute_candies(n :: integer, limit :: integer) :: integer
  def distribute_candies(n, limit) do
    0..limit
    |> Enum.reduce(0, fn a, acc_a ->
      0..limit
      |> Enum.reduce(acc_a, fn b, acc_b ->
        c = n - a - b

        if c >= 0 and c <= limit do
          acc_b + 1
        else
          acc_b
        end
      end)
    end)
  end
end
```
