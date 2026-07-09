# 1739. Building Boxes

## Cpp

```cpp
class Solution {
public:
    int minimumBoxes(int n) {
        long long target = n;
        long long lo = 1, hi = 2000000; // sufficient upper bound
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            __int128 tetra = (__int128)mid * (mid + 1) * (mid + 2) / 6;
            if (tetra >= target)
                hi = mid;
            else
                lo = mid + 1;
        }
        long long s = lo;
        return (int)(s * (s + 1) / 2);
    }
};
```

## Java

```java
class Solution {
    public int minimumBoxes(int n) {
        long target = n;
        long lo = 1, hi = 2000000; // sufficient upper bound
        while (lo < hi) {
            long mid = (lo + hi) >>> 1;
            long tetra = mid * (mid + 1) * (mid + 2) / 6;
            if (tetra >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        long k = lo; // minimal k such that tetrahedral number >= n
        long floorBoxes = k * (k + 1) / 2;
        return (int) floorBoxes;
    }
}
```

## Python

```python
class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, 2000000  # sufficient upper bound for n up to 1e9
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * (mid + 1) * (mid + 2) // 6 >= n:
                hi = mid
            else:
                lo = mid + 1
        k = lo
        return k * (k + 1) // 2
```

## Python3

```python
class Solution:
    def minimumBoxes(self, n: int) -> int:
        lo, hi = 1, 2000000  # sufficient upper bound for n <= 1e9
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * (mid + 1) * (mid + 2) // 6 >= n:
                hi = mid
            else:
                lo = mid + 1
        m = lo
        return m * (m + 1) // 2
```

## C

```c
int minimumBoxes(int n) {
    long long low = 1, high = 2000000; // sufficient upper bound for n <= 1e9
    while (low < high) {
        long long mid = (low + high) / 2;
        long long tetra = mid * (mid + 1) * (mid + 2) / 6; // sum_{i=1}^{mid} i*(i+1)/2
        if (tetra >= n)
            high = mid;
        else
            low = mid + 1;
    }
    long long k = low;
    return (int)(k * (k + 1) / 2);
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumBoxes(int n) {
        double s = System.Math.Sqrt(n);
        long ans = (long)System.Math.Ceiling(2 * s) - 1;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minimumBoxes = function(n) {
    const tetra = (h) => h * (h + 1) * (h + 2) / 6;
    let left = 0, right = 200000; // sufficient upper bound for n <= 1e9
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (tetra(mid) >= n) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    const h = left;
    return h * (h + 1) / 2;
};
```

## Typescript

```typescript
function minimumBoxes(n: number): number {
    let left = 1;
    let right = 2000000; // sufficiently large upper bound
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        const tetra = (mid * (mid + 1) * (mid + 2)) / 6;
        if (tetra >= n) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    const k = left;
    return (k * (k + 1)) / 2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minimumBoxes($n) {
        $low = 1;
        $high = 2000000; // sufficient upper bound for n <= 1e9

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            // compute tetrahedral number T(mid) = mid*(mid+1)*(mid+2)/6
            $a = $mid;
            $b = $mid + 1;
            $c = $mid + 2;

            // divide by 2 and 3 to keep integer arithmetic exact
            if ($a % 2 == 0) {
                $a = intdiv($a, 2);
            } elseif ($b % 2 == 0) {
                $b = intdiv($b, 2);
            } else {
                $c = intdiv($c, 2);
            }

            if ($a % 3 == 0) {
                $a = intdiv($a, 3);
            } elseif ($b % 3 == 0) {
                $b = intdiv($b, 3);
            } else {
                $c = intdiv($c, 3);
            }

            $tetra = $a * $b * $c; // now exact tetrahedral number

            if ($tetra >= $n) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        $h = $low;
        return intdiv($h * ($h + 1), 2);
    }
}
```

## Swift

```swift
class Solution {
    func minimumBoxes(_ n: Int) -> Int {
        var left = 0
        var right = 200000   // sufficient upper bound for n up to 1e9
        let target = Int64(n)
        while left < right {
            let mid = (left + right) / 2
            let m = Int64(mid)
            let maxBoxes = m * (m + 1) * (m + 2) / 6
            if maxBoxes >= target {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumBoxes(n: Int): Int {
        if (n <= 1) return n
        return (n + 3) / 2
    }
}
```

## Dart

```dart
class Solution {
  int minimumBoxes(int n) {
    if (n == 1) return 1;
    return ((n + 1) ~/ 2) + 1;
  }
}
```

## Golang

```go
func minimumBoxes(n int) int {
    lo, hi := 1, 2000000
    target := int64(n)
    for lo < hi {
        mid := (lo + hi) / 2
        t := int64(mid) * int64(mid+1) * int64(mid+2) / 6
        if t >= target {
            hi = mid
        } else {
            lo = mid + 1
        }
    }
    k := lo
    floorBoxes := int64(k) * int64(k+1) / 2
    return int(floorBoxes)
}
```

## Ruby

```ruby
def minimum_boxes(n)
  low = 1
  high = 2_000_000
  while low < high
    mid = (low + high) / 2
    tetra = mid * (mid + 1) * (mid + 2) / 6
    if tetra >= n
      high = mid
    else
      low = mid + 1
    end
  end
  k = low
  k * (k + 1) / 2
end
```

## Scala

```scala
object Solution {
    def minimumBoxes(n: Int): Int = {
        var lo = 1L
        var hi = 2000000L // sufficient upper bound for n up to 1e9
        while (lo < hi) {
            val mid = (lo + hi) / 2
            val tetra = mid * (mid + 1) * (mid + 2) / 6
            if (tetra >= n) hi = mid else lo = mid + 1
        }
        val k = lo
        ((k * (k + 1)) / 2).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_boxes(_n: i32) -> i32 {
        // Placeholder implementation
        0
    }
}
```

## Racket

```racket
(define/contract (minimum-boxes n)
  (-> exact-integer? exact-integer?)
  (letrec ((max-boxes
            (lambda (m)
              (/ (* m (+ m 1) (+ m 2)) 6)))
           (binary-search
            (lambda (lo hi)
              (if (= lo hi)
                  lo
                  (let* ((mid (quotient (+ lo hi) 2))
                         (cap (max-boxes mid)))
                    (if (>= cap n)
                        (binary-search lo mid)
                        (binary-search (+ mid 1) hi)))))))
    (binary-search 0 n)))
```

## Erlang

```erlang
-spec minimum_boxes(N :: integer()) -> integer().
minimum_boxes(N) ->
    binary_search(N, 1, N).

binary_search(_N, L, R) when L >= R ->
    L;
binary_search(N, L, R) ->
    Mid = (L + R) div 2,
    MaxBoxes = Mid * (Mid + 1) div 2,
    if
        MaxBoxes >= N -> binary_search(N, L, Mid);
        true -> binary_search(N, Mid + 1, R)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_boxes(n :: integer) :: integer
  def minimum_boxes(n) do
    binary_search(1, n, n)
  end

  defp binary_search(l, h, n) when l < h do
    mid = div(l + h, 2)

    if max_boxes(mid, n) >= n do
      binary_search(l, mid, n)
    else
      binary_search(mid + 1, h, n)
    end
  end

  defp binary_search(l, _h, _n), do: l

  defp max_boxes(m, n) do
    div(m * (2 * n - m + 1), 2)
  end
end
```
