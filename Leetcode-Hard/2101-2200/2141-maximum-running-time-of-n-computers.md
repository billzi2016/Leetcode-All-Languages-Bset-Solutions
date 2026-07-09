# 2141. Maximum Running Time of N Computers

## Cpp

```cpp
class Solution {
public:
    long long maxRunTime(int n, std::vector<int>& batteries) {
        long long total = 0;
        for (int b : batteries) total += b;
        long long left = 0, right = total / n;
        while (left < right) {
            long long mid = (left + right + 1) >> 1;
            __int128 can = 0;
            for (int b : batteries) {
                can += std::min<long long>(b, mid);
            }
            if (can >= (__int128)mid * n)
                left = mid;
            else
                right = mid - 1;
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public long maxRunTime(int n, int[] batteries) {
        long total = 0;
        for (int b : batteries) {
            total += b;
        }
        long left = 0;
        long right = total / n; // maximum possible time
        
        while (left < right) {
            long mid = left + (right - left + 1) / 2; // upper middle to avoid infinite loop
            long usable = 0;
            for (int b : batteries) {
                usable += Math.min(b, mid);
            }
            if (usable >= (long) n * mid) {
                left = mid; // feasible, try longer
            } else {
                right = mid - 1; // not feasible, reduce
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        total = sum(batteries)
        left, right = 0, total // n

        while left < right:
            mid = (left + right + 1) // 2
            usable = 0
            for b in batteries:
                usable += b if b < mid else mid
                # early exit if already enough
                if usable >= mid * n:
                    break
            if usable >= mid * n:
                left = mid
            else:
                right = mid - 1

        return left
```

## Python3

```python
from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        lo, hi = 0, total // n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            usable = 0
            for b in batteries:
                usable += b if b < mid else mid
            if usable >= mid * n:
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stddef.h>

long long maxRunTime(int n, int* batteries, int batteriesSize) {
    long long total = 0;
    for (int i = 0; i < batteriesSize; ++i) {
        total += (long long)batteries[i];
    }
    
    long long left = 0;
    long long right = total / n;
    
    while (left < right) {
        long long mid = (left + right + 1) >> 1; // upper middle
        long long usable = 0;
        for (int i = 0; i < batteriesSize; ++i) {
            usable += batteries[i] < mid ? (long long)batteries[i] : mid;
            if (usable >= (long long)n * mid) break; // enough power, stop early
        }
        if (usable >= (long long)n * mid)
            left = mid;
        else
            right = mid - 1;
    }
    
    return left;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        long sum = 0;
        foreach (int b in batteries) sum += b;
        long left = 0;
        long right = sum / n; // maximum possible runtime

        while (left < right) {
            long mid = (left + right + 1) >> 1; // upper middle
            long needed = (long)mid * n;
            long total = 0;
            foreach (int b in batteries) {
                total += Math.Min(b, mid);
                if (total >= needed) break; // early exit
            }
            if (total >= needed)
                left = mid;
            else
                right = mid - 1;
        }

        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} batteries
 * @return {number}
 */
var maxRunTime = function(n, batteries) {
    let total = 0;
    for (let b of batteries) total += b;
    let left = 0;
    let right = Math.floor(total / n);
    while (left < right) {
        const mid = Math.floor((left + right + 1) / 2);
        let usable = 0;
        for (let b of batteries) {
            usable += Math.min(b, mid);
        }
        if (usable >= mid * n) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function maxRunTime(n: number, batteries: number[]): number {
    const totalPower = batteries.reduce((sum, b) => sum + b, 0);
    let left = 0;
    let right = Math.floor(totalPower / n);

    while (left < right) {
        const mid = Math.floor((left + right + 1) / 2);
        let usable = 0;
        for (const b of batteries) {
            usable += b < mid ? b : mid;
            if (usable >= n * mid) break; // early exit
        }
        if (usable >= n * mid) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }

    return left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $batteries
     * @return Integer
     */
    function maxRunTime($n, $batteries) {
        $total = array_sum($batteries);
        $right = intdiv($total, $n);
        $left = 0;

        while ($left < $right) {
            $mid = intdiv($left + $right + 1, 2);
            $need = $n * $mid;
            $available = 0;
            foreach ($batteries as $b) {
                $available += min($b, $mid);
                if ($available >= $need) {
                    break;
                }
            }
            if ($available >= $need) {
                $left = $mid;
            } else {
                $right = $mid - 1;
            }
        }

        return $left;
    }
}
```

## Swift

```swift
class Solution {
    func maxRunTime(_ n: Int, _ batteries: [Int]) -> Int {
        var total: Int64 = 0
        for b in batteries {
            total += Int64(b)
        }
        var left: Int64 = 0
        var right: Int64 = total / Int64(n)
        while left < right {
            let mid = (left + right + 1) >> 1
            var usable: Int64 = 0
            for b in batteries {
                usable += min(Int64(b), mid)
            }
            if usable >= Int64(n) * mid {
                left = mid
            } else {
                right = mid - 1
            }
        }
        return Int(left)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxRunTime(n: Int, batteries: IntArray): Long {
        var totalSum = 0L
        for (b in batteries) {
            totalSum += b.toLong()
        }
        var left = 0L
        var right = totalSum / n
        while (left < right) {
            val mid = (left + right + 1) / 2
            var available = 0L
            for (b in batteries) {
                val power = b.toLong()
                available += if (power < mid) power else mid
            }
            if (available >= mid * n) {
                left = mid
            } else {
                right = mid - 1
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int maxRunTime(int n, List<int> batteries) {
    int total = 0;
    for (var b in batteries) {
      total += b;
    }
    int left = 0;
    int right = total ~/ n;

    while (left < right) {
      // upper mid to avoid infinite loop
      int mid = ((right - left) >> 1) + left + 1;
      int usable = 0;
      for (var b in batteries) {
        usable += b < mid ? b : mid;
      }
      if (usable >= mid * n) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }

    return left;
  }
}
```

## Golang

```go
func maxRunTime(n int, batteries []int) int64 {
    var sum int64
    for _, b := range batteries {
        sum += int64(b)
    }
    left, right := int64(0), sum/int64(n)
    for left < right {
        mid := (left + right + 1) / 2
        var can int64
        for _, b := range batteries {
            if int64(b) < mid {
                can += int64(b)
            } else {
                can += mid
            }
        }
        if can >= int64(n)*mid {
            left = mid
        } else {
            right = mid - 1
        }
    }
    return left
}
```

## Ruby

```ruby
def max_run_time(n, batteries)
  left = 1
  right = batteries.sum / n
  while left < right
    mid = (left + right + 1) / 2
    total = 0
    batteries.each do |b|
      total += b < mid ? b : mid
    end
    if total >= mid * n
      left = mid
    else
      right = mid - 1
    end
  end
  left
end
```

## Scala

```scala
object Solution {
  def maxRunTime(n: Int, batteries: Array[Int]): Long = {
    val total: Long = batteries.foldLeft(0L)(_ + _.toLong)
    var left: Long = 0L
    var right: Long = total / n

    while (left < right) {
      val mid: Long = (left + right + 1) >>> 1 // upper middle to avoid infinite loop
      var sum: Long = 0L
      var i = 0
      while (i < batteries.length && sum < n.toLong * mid) {
        sum += math.min(batteries(i).toLong, mid)
        i += 1
      }
      if (sum >= n.toLong * mid) left = mid
      else right = mid - 1
    }
    left
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_run_time(n: i32, batteries: Vec<i32>) -> i64 {
        let n_i64 = n as i64;
        let total: i64 = batteries.iter().map(|&x| x as i64).sum();
        let mut left: i64 = 0;
        let mut right: i64 = total / n_i64;

        while left < right {
            let mid = (left + right + 1) / 2;
            let mut sum: i64 = 0;
            for &b in batteries.iter() {
                sum += std::cmp::min(b as i64, mid);
            }
            if sum >= mid * n_i64 {
                left = mid;
            } else {
                right = mid - 1;
            }
        }

        left
    }
}
```

## Racket

```racket
(define/contract (max-run-time n batteries)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((total (foldl + 0 batteries))
         (right (quotient total n))
         (left 0))
    (define (feasible? mid)
      (let loop ((lst batteries) (acc 0))
        (if (null? lst)
            (>= acc (* n mid))
            (loop (cdr lst) (+ acc (min (car lst) mid))))))
    (let rec ((l left) (r right))
      (if (= l r)
          l
          (let* ((mid (+ l (quotient (+ (- r l) 1) 2)))
                 (ok (feasible? mid)))
            (if ok
                (rec mid r)
                (rec l (- mid 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_run_time/2]).

-spec max_run_time(N :: integer(), Batteries :: [integer()]) -> integer().
max_run_time(N, Batteries) ->
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Batteries),
    Right = Sum div N,
    binary_search(0, Right, N, Batteries).

binary_search(L, R, _N, _Batteries) when L >= R ->
    L;
binary_search(L, R, N, Batteries) ->
    Mid = (L + R + 1) div 2,
    case feasible(Mid, N, Batteries) of
        true -> binary_search(Mid, R, N, Batteries);
        false -> binary_search(L, Mid - 1, N, Batteries)
    end.

feasible(Target, N, Batteries) ->
    Needed = Target * N,
    Total = lists:foldl(fun(B, Acc) -> Acc + min(B, Target) end, 0, Batteries),
    Total >= Needed.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_run_time(n :: integer, batteries :: [integer]) :: integer
  def max_run_time(n, batteries) do
    total_power = Enum.reduce(batteries, 0, &+/2)
    right = div(total_power, n)
    binary_search(0, right, n, batteries)
  end

  defp binary_search(left, right, _n, _batteries) when left >= right, do: left

  defp binary_search(left, right, n, batteries) do
    mid = div(left + right + 1, 2)

    usable =
      Enum.reduce(batteries, 0, fn b, acc ->
        acc + min(b, mid)
      end)

    if usable >= n * mid do
      binary_search(mid, right, n, batteries)
    else
      binary_search(left, mid - 1, n, batteries)
    end
  end
end
```
