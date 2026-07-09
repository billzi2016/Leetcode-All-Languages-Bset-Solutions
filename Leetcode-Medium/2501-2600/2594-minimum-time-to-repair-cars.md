# 2594. Minimum Time to Repair Cars

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long minRank = *min_element(ranks.begin(), ranks.end());
        long long low = 1;
        long long high = minRank * 1LL * cars * cars; // worst case time
        
        while (low < high) {
            long long mid = low + (high - low) / 2;
            long long total = 0;
            for (int r : ranks) {
                total += static_cast<long long>(sqrt((double)mid / r));
                if (total >= cars) break; // early exit
            }
            if (total >= cars)
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public long repairCars(int[] ranks, int cars) {
        int minRank = Integer.MAX_VALUE;
        for (int r : ranks) {
            if (r < minRank) minRank = r;
        }
        long low = 1L;
        long high = (long) minRank * cars * cars; // upper bound using fastest mechanic
        while (low < high) {
            long mid = low + (high - low) / 2;
            if (canRepair(ranks, cars, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean canRepair(int[] ranks, int cars, long time) {
        long total = 0L;
        for (int r : ranks) {
            long limit = time / r; // maximum n^2 allowed for this mechanic
            if (limit == 0) continue;
            long maxCars = (long) Math.sqrt(limit);
            // Adjust for possible floating point errors
            while ((maxCars + 1) * (maxCars + 1) <= limit) {
                maxCars++;
            }
            while (maxCars * maxCars > limit) {
                maxCars--;
            }
            total += maxCars;
            if (total >= cars) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        import math
        lo = 0
        hi = min(ranks) * cars * cars
        while lo < hi:
            mid = (lo + hi) // 2
            total = 0
            for r in ranks:
                total += math.isqrt(mid // r)
                if total >= cars:
                    break
            if total >= cars:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
import math
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_rank = min(ranks)
        low, high = 1, min_rank * cars * cars

        while low < high:
            mid = (low + high) // 2
            total = 0
            for r in ranks:
                total += math.isqrt(mid // r)
                if total >= cars:
                    break
            if total >= cars:
                high = mid
            else:
                low = mid + 1

        return low
```

## C

```c
#include <math.h>
#include <stddef.h>

static int canRepair(long long time, const int *ranks, int ranksSize, int cars) {
    long long total = 0;
    for (int i = 0; i < ranksSize; ++i) {
        double val = (double)time / (double)ranks[i];
        if (val <= 0.0) continue;
        long long cnt = (long long)sqrt(val);
        total += cnt;
        if (total >= cars) return 1;
    }
    return 0;
}

long long repairCars(int* ranks, int ranksSize, int cars) {
    int minRank = ranks[0];
    for (int i = 1; i < ranksSize; ++i) {
        if (ranks[i] < minRank) minRank = ranks[i];
    }
    long long low = 1;
    long long high = (long long)minRank * cars * cars;

    while (low < high) {
        long long mid = low + (high - low) / 2;
        if (canRepair(mid, ranks, ranksSize, cars))
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}
```

## Csharp

```csharp
public class Solution
{
    public long RepairCars(int[] ranks, int cars)
    {
        // Find the smallest rank to set an upper bound.
        int minRank = int.MaxValue;
        foreach (int r in ranks)
            if (r < minRank) minRank = r;

        long low = 1;
        long high = (long)minRank * cars * cars; // Upper bound where fastest mechanic does all work.

        while (low < high)
        {
            long mid = low + (high - low) / 2;
            long repaired = 0;

            foreach (int r in ranks)
            {
                // Maximum cars this mechanic can repair within 'mid' time.
                repaired += (long)Math.Floor(Math.Sqrt((double)mid / r));
                if (repaired >= cars) break; // Early exit if enough cars are already covered.
            }

            if (repaired >= cars)
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} ranks
 * @param {number} cars
 * @return {number}
 */
var repairCars = function(ranks, cars) {
    let minRank = Infinity;
    for (let r of ranks) {
        if (r < minRank) minRank = r;
    }
    let low = 1;
    let high = minRank * cars * cars; // worst case
    
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        let repaired = 0;
        for (let r of ranks) {
            repaired += Math.floor(Math.sqrt(mid / r));
            if (repaired >= cars) break; // early stop
        }
        if (repaired >= cars) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function repairCars(ranks: number[], cars: number): number {
    let minRank = Number.MAX_SAFE_INTEGER;
    for (const r of ranks) {
        if (r < minRank) minRank = r;
    }
    let low = 0;
    let high = minRank * cars * cars; // maximum possible time

    const canRepair = (time: number): boolean => {
        let total = 0;
        for (const r of ranks) {
            total += Math.floor(Math.sqrt(time / r));
            if (total >= cars) return true;
        }
        return false;
    };

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (canRepair(mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $ranks
     * @param Integer $cars
     * @return Integer
     */
    function repairCars($ranks, $cars) {
        // Find the minimum rank to set upper bound
        $minRank = PHP_INT_MAX;
        foreach ($ranks as $r) {
            if ($r < $minRank) $minRank = $r;
        }
        
        $low = 1;
        $high = $minRank * $cars * $cars; // worst case time
        
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $total = 0;
            foreach ($ranks as $r) {
                // maximum cars this mechanic can repair in 'mid' minutes
                $cnt = (int)sqrt($mid / $r);
                $total += $cnt;
                if ($total >= $cars) break; // early exit
            }
            if ($total >= $cars) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func repairCars(_ ranks: [Int], _ cars: Int) -> Int {
        var minRank = Int.max
        for r in ranks {
            if r < minRank { minRank = r }
        }
        var low: Int64 = 1
        var high: Int64 = Int64(minRank) * Int64(cars) * Int64(cars)
        let target = Int64(cars)
        
        while low < high {
            let mid = (low + high) / 2
            var total: Int64 = 0
            for r in ranks {
                let possible = Int64(sqrt(Double(mid) / Double(r)))
                total += possible
                if total >= target { break }
            }
            if total >= target {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return Int(low)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun repairCars(ranks: IntArray, cars: Int): Long {
        var minRank = Int.MAX_VALUE
        for (r in ranks) {
            if (r < minRank) minRank = r
        }
        var low = 1L
        var high = minRank.toLong() * cars.toLong() * cars.toLong()
        while (low < high) {
            val mid = (low + high) / 2
            var total = 0L
            for (r in ranks) {
                val cnt = kotlin.math.sqrt(mid.toDouble() / r).toLong()
                total += cnt
                if (total >= cars) break
            }
            if (total >= cars) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  int repairCars(List<int> ranks, int cars) {
    int minRank = ranks.reduce((a, b) => a < b ? a : b);
    int low = 1;
    int high = minRank * cars * cars; // worst case time

    bool canRepair(int time) {
      int total = 0;
      for (int r in ranks) {
        int possible = math.sqrt(time / r).floor();
        total += possible;
        if (total >= cars) return true;
      }
      return false;
    }

    while (low < high) {
      int mid = low + ((high - low) >> 1);
      if (canRepair(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func repairCars(ranks []int, cars int) int64 {
	if len(ranks) == 0 || cars == 0 {
		return 0
	}
	minRank := ranks[0]
	for _, r := range ranks {
		if r < minRank {
			minRank = r
		}
	}

	low := int64(1)
	high := int64(minRank) * int64(cars) * int64(cars)

	target := int64(cars)

	for low < high {
		mid := (low + high) / 2
		var total int64 = 0

		for _, r := range ranks {
			if mid < int64(r) {
				continue
			}
			div := mid / int64(r)
			n := int64(math.Sqrt(float64(div)))
			// adjust for possible floating point errors
			for (n+1)*(n+1) <= div {
				n++
			}
			for n*n > div {
				n--
			}
			total += n
			if total >= target {
				break
			}
		}

		if total >= target {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}
```

## Ruby

```ruby
def repair_cars(ranks, cars)
  min_rank = ranks.min
  low = 0
  high = min_rank * cars * cars

  while low < high
    mid = (low + high) / 2
    total = 0

    ranks.each do |r|
      next if mid < r
      n = Math.sqrt(mid / r.to_f).floor
      total += n
      break if total >= cars
    end

    if total >= cars
      high = mid
    else
      low = mid + 1
    end
  end

  low
end
```

## Scala

```scala
object Solution {
  def repairCars(ranks: Array[Int], cars: Int): Long = {
    val minRank = ranks.min
    var low = 1L
    var high = minRank.toLong * cars.toLong * cars.toLong

    while (low < high) {
      val mid = (low + high) / 2
      var total = 0L
      var i = 0
      while (i < ranks.length && total < cars) {
        val r = ranks(i).toLong
        val cnt = Math.sqrt(mid.toDouble / r).toLong
        total += cnt
        i += 1
      }
      if (total >= cars) high = mid
      else low = mid + 1
    }

    low
  }
}
```

## Rust

```rust
impl Solution {
    pub fn repair_cars(ranks: Vec<i32>, cars: i32) -> i64 {
        let cars_needed = cars as i64;
        let min_rank = *ranks.iter().min().unwrap() as i64;
        let mut low: i64 = 1;
        let mut high: i64 = min_rank * cars_needed * cars_needed;

        while low < high {
            let mid = low + (high - low) / 2;
            if Self::can_repair(mid, &ranks, cars_needed) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        low
    }

    fn can_repair(time: i64, ranks: &[i32], cars_needed: i64) -> bool {
        let mut total: i64 = 0;
        for &r_i in ranks.iter() {
            let r = r_i as i64;
            if time < r {
                continue;
            }
            // maximum n such that r * n^2 <= time
            let val = (time / r) as f64;
            let n = val.sqrt() as i64;
            total += n;
            if total >= cars_needed {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(require racket/math)

(define/contract (repair-cars ranks cars)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((min-rank (apply min ranks))
         (high (* min-rank (expt cars 2)))
         (low 1))
    (let loop ((l low) (h high))
      (if (= l h)
          l
          (let* ((mid (quotient (+ l h) 2))
                 (total
                  (let sum-loop ((rs ranks) (acc 0))
                    (if (null? rs)
                        acc
                        (let* ((r (car rs))
                               (cnt (exact-floor (sqrt (/ mid r)))))
                          (define new-acc (+ acc cnt))
                          (if (>= new-acc cars)
                              cars
                              (sum-loop (cdr rs) new-acc)))))))
            (if (>= total cars)
                (loop l mid)
                (loop (+ mid 1) h)))))))
```

## Erlang

```erlang
-module(solution).
-export([repair_cars/2]).

-spec repair_cars(Ranks :: [integer()], Cars :: integer()) -> integer().
repair_cars(Ranks, Cars) ->
    MinRank = lists:min(Ranks),
    Low = 1,
    High = MinRank * Cars * Cars,
    binary_search(Low, High, Ranks, Cars).

binary_search(Low, High, _Ranks, _Cars) when Low >= High ->
    Low;
binary_search(Low, High, Ranks, Cars) ->
    Mid = (Low + High) div 2,
    Total = total_cars(Mid, Ranks),
    if
        Total >= Cars -> binary_search(Low, Mid, Ranks, Cars);
        true -> binary_search(Mid + 1, High, Ranks, Cars)
    end.

total_cars(Time, Ranks) ->
    lists:foldl(fun(Rank, Acc) ->
        MaxN = trunc(math:sqrt(Time / Rank)),
        Acc + MaxN
    end, 0, Ranks).
```

## Elixir

```elixir
defmodule Solution do
  @spec repair_cars(ranks :: [integer], cars :: integer) :: integer
  def repair_cars(ranks, cars) do
    min_rank = Enum.min(ranks)
    low = 1
    high = min_rank * cars * cars
    binary_search(low, high, ranks, cars)
  end

  defp binary_search(low, high, _ranks, _cars) when low >= high, do: low

  defp binary_search(low, high, ranks, cars) do
    mid = div(low + high, 2)

    total =
      Enum.reduce(ranks, 0, fn r, acc ->
        n = :math.sqrt(mid / r) |> trunc()
        acc + n
      end)

    if total >= cars do
      binary_search(low, mid, ranks, cars)
    else
      binary_search(mid + 1, high, ranks, cars)
    end
  end
end
```
