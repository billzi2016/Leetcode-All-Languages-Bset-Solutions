# 3560. Find Minimum Log Transportation Cost

## Cpp

```cpp
class Solution {
public:
    long long minCuttingCost(int n, int m, int k) {
        long long L = max(n, m);
        if (L <= k) return 0;
        // The other log must be <= k (guaranteed by problem constraints)
        return (L - k) * 1LL * k;
    }
};
```

## Java

```java
class Solution {
    public long minCuttingCost(int n, int m, int k) {
        int longer = Math.max(n, m);
        if (longer <= k) {
            return 0L;
        }
        long excess = longer - k; // piece that must be cut off
        return excess * (long) k;
    }
}
```

## Python

```python
class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        if n <= k and m <= k:
            return 0
        big = max(n, m)
        # Since the problem guarantees feasibility, only one log can exceed k.
        # Split it into (big - k) and k to satisfy the capacity constraint.
        return k * (big - k)
```

## Python3

```python
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0
        longer = max(n, m)
        # Since input guarantees feasibility, the other log is <= k.
        return k * (longer - k)
```

## C

```c
long long minCuttingCost(int n, int m, int k) {
    if (n <= k && m <= k) return 0;
    if (n > k) return (long long)(n - k) * k;
    return (long long)(m - k) * k;
}
```

## Csharp

```csharp
public class Solution {
    public long MinCuttingCost(int n, int m, int k) {
        if (n <= k && m <= k) return 0;
        int longer = Math.Max(n, m);
        if (longer <= k) return 0;
        long diff = longer - k;
        return diff * (long)k;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var minCuttingCost = function(n, m, k) {
    if (n <= k && m <= k) return 0;
    const longer = Math.max(n, m);
    // The other log is guaranteed to be ≤k by problem constraints.
    return (longer - k) * k;
};
```

## Typescript

```typescript
function minCuttingCost(n: number, m: number, k: number): number {
    if (n <= k && m <= k) return 0;
    const L = Math.max(n, m);
    // The other log is guaranteed to fit into a truck.
    return (L - k) * k;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer $k
     * @return Integer
     */
    function minCuttingCost($n, $m, $k) {
        // If both logs already fit into trucks, no cost.
        if ($n <= $k && $m <= $k) {
            return 0;
        }

        // Ensure $a is the longer log.
        $a = $n;
        $b = $m;
        if ($a < $b) {
            $tmp = $a;
            $a = $b;
            $b = $tmp;
        }

        // At this point $a > $k (otherwise both <= k handled above).
        // Feasibility guarantees $b <= $k.
        if ($a <= $k + 1) {
            // Cut into lengths 1 and $a-1.
            return $a - 1;
        } else {
            // Cut into lengths ($a-$k) and $k.
            return ($a - $k) * $k;
        }
    }
}
```

## Swift

```swift
class Solution {
    func minCuttingCost(_ n: Int, _ m: Int, _ k: Int) -> Int {
        if n <= k && m <= k { return 0 }
        let longer = max(n, m)
        return (longer - k) * k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCuttingCost(n: Int, m: Int, k: Int): Long {
        val maxLen = maxOf(n, m)
        val minLen = minOf(n, m)
        if (maxLen <= k && minLen <= k) return 0L
        // Only one log can exceed k in feasible inputs
        if (maxLen > k) {
            val a = maxLen - k
            val b = k
            return a.toLong() * b.toLong()
        }
        return 0L
    }
}
```

## Dart

```dart
class Solution {
  int minCuttingCost(int n, int m, int k) {
    if (n <= k && m <= k) return 0;
    int big = n > m ? n : m;
    return (big - k) * k;
  }
}
```

## Golang

```go
func minCuttingCost(n int, m int, k int) int64 {
	if n <= k && m <= k {
		return 0
	}
	if n > k && m <= k {
		return int64(k) * int64(n-k)
	}
	if m > k && n <= k {
		return int64(k) * int64(m-k)
	}
	// Both exceed k: choose the cheaper single cut (problem guarantees this case won't occur,
	// but we handle it for completeness).
	cost1 := int64(k) * int64(n-k)
	cost2 := int64(k) * int64(m-k)
	if cost1 < cost2 {
		return cost1
	}
	return cost2
}
```

## Ruby

```ruby
def min_cutting_cost(n, m, k)
  return 0 if n <= k && m <= k
  big = n > k ? n : m
  k * (big - k)
end
```

## Scala

```scala
object Solution {
    def minCuttingCost(n: Int, m: Int, k: Int): Long = {
        if (n <= k && m <= k) return 0L
        val x = math.max(n, m)
        // the other log must be <= k due to problem guarantee
        val cost = (x - k).toLong * k.toLong
        cost
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cutting_cost(n: i32, m: i32, k: i32) -> i64 {
        if n <= k && m <= k {
            0
        } else {
            let l = std::cmp::max(n, m);
            (l - k) as i64 * k as i64
        }
    }
}
```

## Racket

```racket
(define/contract (min-cutting-cost n m k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (if (and (<= n k) (<= m k))
      0
      (let* ([longer (max n m)]
             [a (max 1 (- longer k))]
             [b (- longer a)])
        (* a b))))
```

## Erlang

```erlang
-spec min_cutting_cost(N :: integer(), M :: integer(), K :: integer()) -> integer().
min_cutting_cost(N, M, K) ->
    case {N =< K, M =< K} of
        {true, true} -> 0;
        _ ->
            L = if N > K -> N; true -> M end,
            (L - K) * K
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cutting_cost(n :: integer, m :: integer, k :: integer) :: integer
  def min_cutting_cost(n, m, k) do
    max_len = max(n, m)

    if max_len <= k do
      0
    else
      k * (max_len - k)
    end
  end
end
```
