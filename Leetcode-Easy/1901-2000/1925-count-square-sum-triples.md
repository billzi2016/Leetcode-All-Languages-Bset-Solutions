# 1925. Count Square Sum Triples

## Cpp

```cpp
class Solution {
public:
    int countTriples(int n) {
        int cnt = 0;
        for (int a = 1; a <= n; ++a) {
            int aa = a * a;
            for (int b = 1; b <= n; ++b) {
                int sum = aa + b * b;
                int c = (int)(sqrt((double)sum) + 0.5);
                if (c <= n && c * c == sum) {
                    ++cnt;
                }
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            int a2 = a * a;
            for (int b = 1; b <= n; b++) {
                int sum = a2 + b * b;
                int c = (int) Math.sqrt(sum);
                if (c * c == sum && c <= n) {
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
import math

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        for a in range(1, n + 1):
            a2 = a * a
            for b in range(1, n + 1):
                c2 = a2 + b * b
                c = math.isqrt(c2)
                if c * c == c2 and c <= n:
                    cnt += 1
        return cnt
```

## Python3

```python
import math

class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            aa = a * a
            for b in range(1, n + 1):
                s = aa + b * b
                c = math.isqrt(s)
                if c * c == s and c <= n:
                    cnt += 1
        return cnt
```

## C

```c
#include <math.h>

int countTriples(int n) {
    int cnt = 0;
    for (int a = 1; a <= n; ++a) {
        for (int b = 1; b <= n; ++b) {
            long sum = (long)a * a + (long)b * b;
            int c = (int)sqrt((double)sum);
            if (c > n) continue;
            if ((long)c * c == sum && c >= 1) {
                cnt++;
            }
        }
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int CountTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            long a2 = (long)a * a;
            for (int b = 1; b <= n; b++) {
                long sum = a2 + (long)b * b;
                double root = Math.Sqrt(sum);
                int c = (int)root;
                if (c * c == sum && c <= n) {
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
 * @return {number}
 */
var countTriples = function(n) {
    let count = 0;
    for (let a = 1; a <= n; ++a) {
        const a2 = a * a;
        for (let b = 1; b <= n; ++b) {
            const sum = a2 + b * b;
            const c = Math.floor(Math.sqrt(sum));
            if (c * c === sum && c <= n) {
                count++;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function countTriples(n: number): number {
    let count = 0;
    for (let a = 1; a <= n; a++) {
        const a2 = a * a;
        for (let b = 1; b <= n; b++) {
            const sum = a2 + b * b;
            const c = Math.sqrt(sum);
            if (c <= n && Number.isInteger(c)) {
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
     * @return Integer
     */
    function countTriples($n) {
        $count = 0;
        for ($a = 1; $a <= $n; $a++) {
            $a2 = $a * $a;
            for ($b = 1; $b <= $n; $b++) {
                $sum = $a2 + $b * $b;
                $c = (int)sqrt($sum);
                if ($c * $c == $sum && $c <= $n) {
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
    func countTriples(_ n: Int) -> Int {
        var count = 0
        for a in 1...n {
            let aa = a * a
            for b in 1...n {
                let sum = aa + b * b
                let c = Int(Double(sum).squareRoot())
                if c * c == sum && c <= n {
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
import kotlin.math.sqrt

class Solution {
    fun countTriples(n: Int): Int {
        var count = 0
        for (a in 1..n) {
            val a2 = a * a
            for (b in 1..n) {
                val c2 = a2 + b * b
                val c = sqrt(c2.toDouble()).toInt()
                if (c * c == c2 && c <= n) {
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
import 'dart:math';

class Solution {
  int countTriples(int n) {
    int cnt = 0;
    for (int a = 1; a <= n; ++a) {
      for (int b = 1; b <= n; ++b) {
        int c2 = a * a + b * b;
        int c = sqrt(c2).toInt();
        if (c * c == c2 && c <= n) cnt++;
      }
    }
    return cnt;
  }
}
```

## Golang

```go
import "math"

func countTriples(n int) int {
	cnt := 0
	for a := 1; a <= n; a++ {
		aa := a * a
		for b := 1; b <= n; b++ {
			sum := aa + b*b
			c := int(math.Sqrt(float64(sum)))
			if c*c == sum && c <= n {
				cnt++
			}
		}
	}
	return cnt
}
```

## Ruby

```ruby
def count_triples(n)
  cnt = 0
  (1..n).each do |a|
    a2 = a * a
    (1..n).each do |b|
      c2 = a2 + b * b
      c = Math.sqrt(c2).to_i
      cnt += 1 if c * c == c2 && c <= n
    end
  end
  cnt
end
```

## Scala

```scala
object Solution {
    def countTriples(n: Int): Int = {
        var cnt = 0
        for (a <- 1 to n) {
            val a2 = a * a
            for (b <- 1 to n) {
                val c2 = a2 + b * b
                val c = math.sqrt(c2).toInt
                if (c * c == c2 && c <= n) cnt += 1
            }
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut count = 0;
        for a in 1..=n {
            for b in 1..=n {
                let sum_sq = a * a + b * b;
                let c = (sum_sq as f64).sqrt() as i32;
                if c * c == sum_sq && c <= n {
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
(require racket/math)

(define/contract (count-triples n)
  (-> exact-integer? exact-integer?)
  (for/sum ([a (in-range 1 (add1 n))]
            [b (in-range 1 (add1 n))])
    (let* ((s (+ (* a a) (* b b)))
           (c (integer-sqrt s)))
      (if (and (= (* c c) s) (<= c n))
          1
          0))))
```

## Erlang

```erlang
-module(solution).
-export([count_triples/1]).

-spec count_triples(N :: integer()) -> integer().
count_triples(N) when N >= 1 ->
    count_a(1, N, 0).

count_a(A, N, Acc) when A =< N ->
    NewAcc = count_b(A, 1, N, Acc),
    count_a(A + 1, N, NewAcc);
count_a(_, _, Acc) -> 
    Acc.

count_b(_A, B, N, Acc) when B > N ->
    Acc;
count_b(A, B, N, Acc) ->
    S = A * A + B * B,
    C = trunc(math:sqrt(S)),
    UpdatedAcc = case (C * C == S) andalso (C =< N) of
        true -> Acc + 1;
        false -> Acc
    end,
    count_b(A, B + 1, N, UpdatedAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_triples(n :: integer) :: integer
  def count_triples(n) do
    1..n
    |> Enum.reduce(0, fn a, acc_a ->
      cnt =
        1..n
        |> Enum.reduce(0, fn b, acc_b ->
          c2 = a * a + b * b
          c = :math.sqrt(c2) |> trunc()
          if c * c == c2 and c <= n do
            acc_b + 1
          else
            acc_b
          end
        end)

      acc_a + cnt
    end)
  end
end
```
