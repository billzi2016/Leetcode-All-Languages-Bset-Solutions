# 1954. Minimum Garden Perimeter to Collect Enough Apples

## Cpp

```cpp
class Solution {
public:
    long long minimumPerimeter(long long neededApples) {
        auto apples = [&](long long s) -> __int128 {
            // total = 2 * (2*s + 1) * s * (s + 1)
            return (__int128)2 * (2 * s + 1) * s * (s + 1);
        };
        
        long long lo = 0, hi = 1;
        while (apples(hi) < neededApples) {
            hi <<= 1; // double until sufficient
        }
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (apples(mid) >= neededApples) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo * 8LL;
    }
};
```

## Java

```java
class Solution {
    public long minimumPerimeter(long neededApples) {
        long lo = 0, hi = 1;
        while (apples(hi) < neededApples) {
            hi <<= 1; // double hi
        }
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (apples(mid) >= neededApples) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return 8L * lo;
    }

    private long apples(long n) {
        // total apples inside square with half side length n
        // formula: 2 * n * (n + 1) * (2 * n + 1)
        return 2L * n * (n + 1) * (2L * n + 1);
    }
}
```

## Python

```python
class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        def apples(k):
            # total apples inside square with half side length k
            return 2 * (2 * k + 1) * k * (k + 1)

        low, high = 0, 10**6  # sufficient upper bound for neededApples <= 1e15
        while low < high:
            mid = (low + high) // 2
            if apples(mid) >= neededApples:
                high = mid
            else:
                low = mid + 1
        return 8 * low
```

## Python3

```python
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def apples(k: int) -> int:
            # total apples in square with half-side length k
            return 2 * (2 * k + 1) * k * (k + 1)

        lo, hi = 0, 1
        while apples(hi) < neededApples:
            hi <<= 1

        while lo < hi:
            mid = (lo + hi) // 2
            if apples(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1

        return 8 * lo
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static __int128 applesInSquare(long long k) {
    // S(k) = 2 * (2k + 1) * k * (k + 1)
    return (__int128)2 * (2LL * k + 1) * k * (k + 1);
}

long long minimumPerimeter(long long neededApples) {
    long long lo = 0, hi = 1;
    while (applesInSquare(hi) < neededApples) hi <<= 1; // expand upper bound
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (applesInSquare(mid) >= neededApples)
            hi = mid;
        else
            lo = mid + 1;
    }
    return 8LL * lo; // perimeter = 4 * side length = 8 * k
}
```

## Csharp

```csharp
public class Solution
{
    public long MinimumPerimeter(long neededApples)
    {
        long lo = 0;
        long hi = 1;
        while (AppleCount(hi) < neededApples)
            hi <<= 1;

        while (lo < hi)
        {
            long mid = lo + (hi - lo) / 2;
            if (AppleCount(mid) >= neededApples)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo * 8;
    }

    private long AppleCount(long L)
    {
        // total apples in square with half-side length L:
        // 2 * (2L + 1) * L * (L + 1)
        long a = 2 * L + 1;   // up to ~2e6 for needed range
        long b = L;
        long c = L + 1;

        long res = a * b;     // safe within long
        res = res * c;
        return res * 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} neededApples
 * @return {number}
 */
var minimumPerimeter = function(neededApples) {
    const need = BigInt(neededApples);
    const apples = (k) => 2n * k * (k + 1n) * (2n * k + 1n); // total apples for half-side k
    let low = 0n, high = 1n;
    while (apples(high) < need) {
        high <<= 1n; // double high
    }
    while (low < high) {
        const mid = (low + high) >> 1n;
        if (apples(mid) >= need) {
            high = mid;
        } else {
            low = mid + 1n;
        }
    }
    return Number(8n * low);
};
```

## Typescript

```typescript
function minimumPerimeter(neededApples: number): number {
    const target = BigInt(neededApples);
    const apples = (k: bigint) => 2n * k * (k + 1n) * (2n * k + 1n);

    let lo = 0n;
    let hi = 1n;
    while (apples(hi) < target) {
        hi <<= 1n; // multiply by 2
    }

    while (lo + 1n < hi) {
        const mid = (lo + hi) >> 1n;
        if (apples(mid) >= target) {
            hi = mid;
        } else {
            lo = mid;
        }
    }

    return Number(hi * 8n);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $neededApples
     * @return Integer
     */
    function minimumPerimeter($neededApples) {
        // Helper closure to compute total apples for a given k
        $apples = function(int $k): int {
            // 2 * (2k + 1) * k * (k + 1)
            return 2 * (2 * $k + 1) * $k * ($k + 1);
        };

        $low = 0;
        $high = 1;
        // Expand upper bound until it's sufficient
        while ($apples($high) < $neededApples) {
            $high <<= 1; // double the high value
        }

        // Binary search for minimal k
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($apples($mid) >= $neededApples) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        // Perimeter is 8 * k
        return $low * 8;
    }
}
```

## Swift

```swift
class Solution {
    func minimumPerimeter(_ neededApples: Int) -> Int {
        let target = Int64(neededApples)
        
        func apples(_ k: Int) -> Int64 {
            let kk = Int64(k)
            return 2 * (2 * kk + 1) * kk * (kk + 1)
        }
        
        var left = 0
        var right = 1
        while apples(right) < target {
            right <<= 1
        }
        while left + 1 < right {
            let mid = (left + right) >> 1
            if apples(mid) >= target {
                right = mid
            } else {
                left = mid
            }
        }
        return right * 8
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumPerimeter(neededApples: Long): Long {
        var low = 0L
        var high = 1L
        while (apples(high) < neededApples) {
            high *= 2
        }
        while (low + 1 < high) {
            val mid = (low + high) / 2
            if (apples(mid) >= neededApples) {
                high = mid
            } else {
                low = mid
            }
        }
        return 8L * high
    }

    private fun apples(k: Long): Long {
        // total apples inside/on a square with side length 2k
        // formula: 2 * (2k + 1) * k * (k + 1)
        val term = 2L * (2L * k + 1L)
        return term * k * (k + 1L)
    }
}
```

## Dart

```dart
class Solution {
  int minimumPerimeter(int neededApples) {
    int low = 0;
    int high = 1;
    while (_apples(high) < neededApples) {
      high <<= 1;
    }
    while (low < high) {
      int mid = low + ((high - low) >> 1);
      if (_apples(mid) >= neededApples) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low * 8;
  }

  int _apples(int L) {
    // Total apples in square with half-side length L
    return 2 * (2 * L + 1) * L * (L + 1);
  }
}
```

## Golang

```go
func minimumPerimeter(neededApples int64) int64 {
	// helper to compute total apples inside square with half-side length L
	apples := func(L int64) int64 {
		return 2 * L * (L + 1) * (2*L + 1)
	}

	low, high := int64(0), int64(1)
	for apples(high) < neededApples {
		high <<= 1
	}
	for low < high {
		mid := (low + high) >> 1
		if apples(mid) >= neededApples {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return 8 * low
}
```

## Ruby

```ruby
def minimum_perimeter(needed_apples)
  # helper to compute total apples inside square with half-side length L
  apples = ->(l) { 2 * l * (l + 1) * (2 * l + 1) }

  low = 0
  high = 1
  while apples.call(high) < needed_apples
    high <<= 1
  end

  while low < high
    mid = (low + high) / 2
    if apples.call(mid) >= needed_apples
      high = mid
    else
      low = mid + 1
    end
  end

  8 * low
end
```

## Scala

```scala
object Solution {
    def minimumPerimeter(neededApples: Long): Long = {
        import scala.math.BigInt

        def apples(k: Long): BigInt = {
            val kk = BigInt(k)
            BigInt(2) * kk * (kk + 1) * (BigInt(2) * kk + 1)
        }

        var lo = 0L
        var hi = 1L
        val target = BigInt(neededApples)

        while (apples(hi) < target) {
            hi <<= 1
        }

        while (lo + 1 < hi) {
            val mid = lo + (hi - lo) / 2
            if (apples(mid) >= target) hi = mid else lo = mid
        }

        8L * hi
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_perimeter(needed_apples: i64) -> i64 {
        let need = needed_apples as i128;
        // helper to compute apples for given s
        let apples = |s: i64| -> i128 {
            let s = s as i128;
            2 * (2 * s + 1) * s * (s + 1)
        };
        // find an upper bound
        let mut low: i64 = 0;
        let mut high: i64 = 1;
        while apples(high) < need {
            high <<= 1; // double
        }
        // binary search for minimal s
        while low < high {
            let mid = low + (high - low) / 2;
            if apples(mid) >= need {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        // perimeter is 8 * s
        low * 8
    }
}
```

## Racket

```racket
(define/contract (minimum-perimeter neededApples)
  (-> exact-integer? exact-integer?)
  (letrec ((apples (lambda (L)
                     (* 2 (+ (* 2 L) 1) L (+ L 1)))))
    (let loop ((low 0) (high 1))
      (if (>= (apples high) neededApples)
          (let bs ((l low) (r high))
            (if (= l r)
                (* 8 l)
                (let ((mid (quotient (+ l r) 2)))
                  (if (>= (apples mid) neededApples)
                      (bs l mid)
                      (bs (+ mid 1) r)))))
          (loop high (* high 2))))))
```

## Erlang

```erlang
-spec minimum_perimeter(NeededApples :: integer()) -> integer().
minimum_perimeter(N) ->
    High = find_high(N, 1),
    K = binary_search(N, 0, High),
    8 * K.

find_high(N, H) when apples(H) >= N -> H;
find_high(N, H) -> find_high(N, H * 2).

apples(K) ->
    2 * (2 * K + 1) * K * (K + 1).

binary_search(N, L, R) when L < R ->
    M = (L + R) div 2,
    if apples(M) >= N -> binary_search(N, L, M);
       true -> binary_search(N, M + 1, R)
    end;
binary_search(_, K, _) -> K.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_perimeter(needed_apples :: integer) :: integer
  def minimum_perimeter(needed_apples) do
    {low, high} = find_bounds(1, needed_apples)
    k = binary_search(low, high, needed_apples)
    k * 8
  end

  defp apples(k), do: 2 * k * (k + 1) * (2 * k + 1)

  defp find_bounds(high, needed) when apples(high) >= needed, do: {1, high}
  defp find_bounds(high, needed), do: find_bounds(high * 2, needed)

  defp binary_search(low, high, needed) when low < high do
    mid = div(low + high, 2)
    if apples(mid) >= needed do
      binary_search(low, mid, needed)
    else
      binary_search(mid + 1, high, needed)
    end
  end

  defp binary_search(low, _high, _needed), do: low
end
```
