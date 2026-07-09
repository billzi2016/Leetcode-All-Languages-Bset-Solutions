# 1011. Capacity To Ship Packages Within D Days

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int lo = *max_element(weights.begin(), weights.end());
        long long hi_ll = accumulate(weights.begin(), weights.end(), 0LL);
        int hi = static_cast<int>(hi_ll);
        
        auto canShip = [&](int cap)->bool{
            int used = 1;
            int cur = 0;
            for (int w : weights) {
                if (cur + w > cap) {
                    ++used;
                    cur = w;
                } else {
                    cur += w;
                }
            }
            return used <= days;
        };
        
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canShip(mid))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int low = 0;
        int high = 0;
        for (int w : weights) {
            low = Math.max(low, w);
            high += w;
        }
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (canShip(weights, days, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean canShip(int[] weights, int days, int capacity) {
        int usedDays = 1;
        int curLoad = 0;
        for (int w : weights) {
            if (curLoad + w > capacity) {
                usedDays++;
                curLoad = w;
                if (usedDays > days) return false;
            } else {
                curLoad += w;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        lo = max(weights)
        hi = sum(weights)

        def can_ship(capacity):
            required_days = 1
            current_load = 0
            for w in weights:
                if current_load + w <= capacity:
                    current_load += w
                else:
                    required_days += 1
                    if required_days > days:
                        return False
                    current_load = w
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        def can_ship(capacity: int) -> bool:
            required_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    required_days += 1
                    current_load = w
                    if required_days > days:
                        return False
                else:
                    current_load += w
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
int shipWithinDays(int* weights, int weightsSize, int days) {
    int lo = 0, hi = 0;
    for (int i = 0; i < weightsSize; ++i) {
        if (weights[i] > lo) lo = weights[i];
        hi += weights[i];
    }
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int requiredDays = 1;
        int currentLoad = 0;
        for (int i = 0; i < weightsSize; ++i) {
            if (currentLoad + weights[i] <= mid) {
                currentLoad += weights[i];
            } else {
                ++requiredDays;
                currentLoad = weights[i];
            }
        }
        if (requiredDays <= days)
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
}
```

## Csharp

```csharp
public class Solution {
    public int ShipWithinDays(int[] weights, int days) {
        int left = 0;
        long right = 0;
        foreach (int w in weights) {
            if (w > left) left = w;
            right += w;
        }
        while (left < right) {
            int mid = left + (int)((right - left) / 2);
            if (CanShip(weights, days, mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }

    private bool CanShip(int[] weights, int days, int capacity) {
        int usedDays = 1;
        int curLoad = 0;
        foreach (int w in weights) {
            if (curLoad + w <= capacity) {
                curLoad += w;
            } else {
                usedDays++;
                if (usedDays > days) return false;
                curLoad = w;
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function(weights, days) {
    let left = Math.max(...weights);
    let right = weights.reduce((a, b) => a + b, 0);
    
    const canShip = (capacity) => {
        let needed = 1;
        let cur = 0;
        for (const w of weights) {
            if (cur + w > capacity) {
                needed++;
                cur = w;
            } else {
                cur += w;
            }
        }
        return needed <= days;
    };
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canShip(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function shipWithinDays(weights: number[], days: number): number {
    const maxWeight = Math.max(...weights);
    let left = maxWeight;
    let right = weights.reduce((a, b) => a + b, 0);

    const canShip = (capacity: number): boolean => {
        let requiredDays = 1;
        let currentLoad = 0;
        for (const w of weights) {
            if (currentLoad + w > capacity) {
                requiredDays++;
                currentLoad = w;
                if (requiredDays > days) return false;
            } else {
                currentLoad += w;
            }
        }
        return true;
    };

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canShip(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $weights
     * @param Integer $days
     * @return Integer
     */
    function shipWithinDays($weights, $days) {
        $low = max($weights);
        $high = array_sum($weights);

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canShip($weights, $days, $mid)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }

    private function canShip($weights, $days, $capacity) {
        $requiredDays = 1;
        $currentLoad = 0;

        foreach ($weights as $w) {
            if ($currentLoad + $w > $capacity) {
                $requiredDays++;
                $currentLoad = $w;
                if ($requiredDays > $days) {
                    return false;
                }
            } else {
                $currentLoad += $w;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func shipWithinDays(_ weights: [Int], _ days: Int) -> Int {
        var low = weights.max()!
        var high = weights.reduce(0, +)
        
        func canShip(_ capacity: Int) -> Bool {
            var requiredDays = 1
            var currentLoad = 0
            for w in weights {
                if currentLoad + w <= capacity {
                    currentLoad += w
                } else {
                    requiredDays += 1
                    if requiredDays > days { return false }
                    currentLoad = w
                }
            }
            return true
        }
        
        while low < high {
            let mid = (low + high) / 2
            if canShip(mid) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shipWithinDays(weights: IntArray, days: Int): Int {
        var left = weights.maxOrNull() ?: 0
        var right = weights.sum()
        while (left < right) {
            val mid = left + (right - left) / 2
            if (canShip(weights, days, mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }

    private fun canShip(weights: IntArray, days: Int, capacity: Int): Boolean {
        var neededDays = 1
        var currentLoad = 0
        for (w in weights) {
            if (currentLoad + w > capacity) {
                neededDays++
                currentLoad = w
                if (neededDays > days) return false
            } else {
                currentLoad += w
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int shipWithinDays(List<int> weights, int days) {
    int left = weights.reduce((a, b) => a > b ? a : b);
    int right = weights.fold(0, (sum, w) => sum + w);

    bool canShip(int capacity) {
      int neededDays = 1;
      int currentLoad = 0;
      for (int w in weights) {
        if (currentLoad + w > capacity) {
          neededDays++;
          currentLoad = w;
        } else {
          currentLoad += w;
        }
      }
      return neededDays <= days;
    }

    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (canShip(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
func shipWithinDays(weights []int, days int) int {
    maxWeight := 0
    total := 0
    for _, w := range weights {
        if w > maxWeight {
            maxWeight = w
        }
        total += w
    }

    lo, hi := maxWeight, total
    for lo < hi {
        mid := (lo + hi) / 2
        if canShip(weights, days, mid) {
            hi = mid
        } else {
            lo = mid + 1
        }
    }
    return lo
}

func canShip(weights []int, days int, capacity int) bool {
    neededDays := 1
    currentLoad := 0
    for _, w := range weights {
        if currentLoad+w > capacity {
            neededDays++
            currentLoad = 0
        }
        currentLoad += w
    }
    return neededDays <= days
}
```

## Ruby

```ruby
def ship_within_days(weights, days)
  low = weights.max
  high = weights.sum
  while low < high
    mid = (low + high) / 2
    needed = 1
    cur = 0
    weights.each do |w|
      if cur + w <= mid
        cur += w
      else
        needed += 1
        cur = w
      end
    end
    if needed <= days
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
    def shipWithinDays(weights: Array[Int], days: Int): Int = {
        var left = weights.max
        var right = weights.sum

        def canShip(capacity: Int): Boolean = {
            var requiredDays = 1
            var currentLoad = 0
            for (w <- weights) {
                if (currentLoad + w <= capacity) {
                    currentLoad += w
                } else {
                    requiredDays += 1
                    if (requiredDays > days) return false
                    currentLoad = w
                }
            }
            true
        }

        while (left < right) {
            val mid = left + (right - left) / 2
            if (canShip(mid)) right = mid
            else left = mid + 1
        }
        left
    }
}
```

## Rust

```rust
impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        let mut left = *weights.iter().max().unwrap() as i64;
        let mut right: i64 = weights.iter().map(|&x| x as i64).sum();

        while left < right {
            let mid = (left + right) / 2;
            if Self::can_ship(&weights, mid, days as usize) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left as i32
    }

    fn can_ship(weights: &[i32], capacity: i64, days: usize) -> bool {
        let mut needed = 1usize;
        let mut cur = 0i64;

        for &w in weights.iter() {
            let w = w as i64;
            if cur + w > capacity {
                needed += 1;
                cur = w;
                if needed > days {
                    return false;
                }
            } else {
                cur += w;
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (ship-within-days weights days)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((low (apply max weights))
         (high (apply + weights)))
    (define (possible? cap)
      (let loop ((ws weights) (cur 0) (need 1))
        (cond
          [(null? ws) (<= need days)]
          [else
           (let ((w (car ws)))
             (if (> (+ cur w) cap)
                 (loop (cdr ws) w (+ need 1))
                 (loop (cdr ws) (+ cur w) need)))])))
    (let loop ((lo low) (hi high) (ans high))
      (if (> lo hi)
          ans
          (let ((mid (quotient (+ lo hi) 2)))
            (if (possible? mid)
                (loop lo (- mid 1) mid)
                (loop (+ mid 1) hi ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([ship_within_days/2]).

-spec ship_within_days(Weights :: [integer()], Days :: integer()) -> integer().
ship_within_days(Weights, Days) ->
    MaxWeight = lists:max(Weights),
    SumWeight = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Weights),
    binary_search(MaxWeight, SumWeight, Weights, Days).

binary_search(Low, High, Weights, Days) when Low < High ->
    Mid = (Low + High) div 2,
    case can_ship(Mid, Weights, Days) of
        true -> binary_search(Low, Mid, Weights, Days);
        false -> binary_search(Mid + 1, High, Weights, Days)
    end;
binary_search(Low, _High, _Weights, _Days) ->
    Low.

-spec can_ship(Capacity :: integer(), Weights :: [integer()], Days :: integer()) -> boolean().
can_ship(Capacity, Weights, Days) ->
    {NeededDays, _} = lists:foldl(
        fun(W, {Day, Load}) ->
            if
                Load + W =< Capacity -> {Day, Load + W};
                true -> {Day + 1, W}
            end
        end,
        {1, 0},
        Weights),
    NeededDays =< Days.
```

## Elixir

```elixir
defmodule Solution do
  @spec ship_within_days([integer()], integer()) :: integer()
  def ship_within_days(weights, days) do
    min_cap = Enum.max(weights)
    max_cap = Enum.sum(weights)

    binary_search(min_cap, max_cap, weights, days)
  end

  defp binary_search(low, high, weights, days) when low < high do
    mid = div(low + high, 2)

    if possible?(weights, days, mid) do
      binary_search(low, mid, weights, days)
    else
      binary_search(mid + 1, high, weights, days)
    end
  end

  defp binary_search(low, _high, _weights, _days), do: low

  defp possible?(weights, days, capacity) do
    {required_days, _current} =
      Enum.reduce(weights, {1, 0}, fn w, {d, cur} ->
        if cur + w <= capacity do
          {d, cur + w}
        else
          {d + 1, w}
        end
      end)

    required_days <= days
  end
end
```
