# 0875. Koko Eating Bananas

## Cpp

```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());
        while (left < right) {
            int mid = left + (right - left) / 2;
            long long hours = 0;
            for (int p : piles) {
                hours += (p + mid - 1) / mid; // ceil division
                if (hours > h) break; // early exit
            }
            if (hours <= h) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = 0;
        for (int p : piles) {
            if (p > high) high = p;
        }
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (canFinish(piles, h, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean canFinish(int[] piles, int h, int speed) {
        long hoursNeeded = 0;
        for (int p : piles) {
            // ceil division without floating point
            hoursNeeded += (p + speed - 1L) / speed;
            if (hoursNeeded > h) {
                return false;
            }
        }
        return hoursNeeded <= h;
    }
}
```

## Python

```python
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                # ceil division without using math.ceil
                hours += (p + mid - 1) // mid
                if hours > h:  # early break to save time
                    break
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
```

## Python3

```python
class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum((p + mid - 1) // mid for p in piles)
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
```

## C

```c
int minEatingSpeed(int* piles, int pilesSize, int h) {
    int maxPile = 0;
    for (int i = 0; i < pilesSize; ++i) {
        if (piles[i] > maxPile) maxPile = piles[i];
    }
    int left = 1, right = maxPile;
    while (left < right) {
        int mid = left + (right - left) / 2;
        long long hours = 0;
        for (int i = 0; i < pilesSize; ++i) {
            hours += (piles[i] + (long long)mid - 1) / mid;
            if (hours > h) break; // early exit
        }
        if (hours <= h) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinEatingSpeed(int[] piles, int h)
    {
        int left = 1;
        int right = 0;
        foreach (int p in piles)
            if (p > right) right = p;

        while (left < right)
        {
            int mid = left + (right - left) / 2;
            long hoursNeeded = 0;
            foreach (int p in piles)
                hoursNeeded += (p + mid - 1) / mid; // ceiling division

            if (hoursNeeded <= h)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    const canFinish = (k) => {
        let hours = 0;
        for (let p of piles) {
            // ceil division without floating point
            hours += Math.floor((p + k - 1) / k);
            if (hours > h) return false; // early exit
        }
        return true;
    };
    
    let left = 1;
    let right = Math.max(...piles);
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canFinish(mid)) {
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
function minEatingSpeed(piles: number[], h: number): number {
    let left = 1;
    let right = Math.max(...piles);
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        let hours = 0;
        for (const p of piles) {
            hours += Math.floor((p + mid - 1) / mid);
            if (hours > h) break;
        }
        if (hours <= h) {
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
     * @param Integer[] $piles
     * @param Integer $h
     * @return Integer
     */
    function minEatingSpeed($piles, $h) {
        $low = 1;
        $high = max($piles);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $hours = 0;
            foreach ($piles as $pile) {
                $hours += intdiv($pile + $mid - 1, $mid);
                if ($hours > $h) {
                    break;
                }
            }
            if ($hours <= $h) {
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
class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        var left = 1
        var right = piles.max()!
        while left < right {
            let mid = (left + right) / 2
            var hours = 0
            for p in piles {
                hours += (p + mid - 1) / mid
                if hours > h { break }
            }
            if hours <= h {
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
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        var left = 1
        var right = piles.maxOrNull() ?: 0
        while (left < right) {
            val mid = left + (right - left) / 2
            var hoursNeeded = 0L
            for (p in piles) {
                hoursNeeded += ((p + mid - 1) / mid)
                if (hoursNeeded > h) break
            }
            if (hoursNeeded <= h) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int minEatingSpeed(List<int> piles, int h) {
    int left = 1;
    int right = piles.reduce((a, b) => a > b ? a : b);
    while (left < right) {
      int mid = (left + right) ~/ 2;
      int hours = 0;
      for (int p in piles) {
        hours += (p + mid - 1) ~/ mid;
        if (hours > h) break; // early exit
      }
      if (hours <= h) {
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
func minEatingSpeed(piles []int, h int) int {
    maxPile := 0
    for _, p := range piles {
        if p > maxPile {
            maxPile = p
        }
    }

    low, high := 1, maxPile
    for low < high {
        mid := (low + high) / 2
        hours := 0
        for _, p := range piles {
            hours += (p + mid - 1) / mid
            if hours > h {
                break
            }
        }
        if hours <= h {
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
def min_eating_speed(piles, h)
  left = 1
  right = piles.max
  while left < right
    mid = (left + right) / 2
    hours = 0
    piles.each do |p|
      hours += (p + mid - 1) / mid
      break if hours > h
    end
    if hours <= h
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
```

## Scala

```scala
object Solution {
    def minEatingSpeed(piles: Array[Int], h: Int): Int = {
        var left: Long = 1L
        var right: Long = piles.max.toLong

        while (left < right) {
            val mid = (left + right) / 2
            var hoursNeeded: Long = 0L
            for (p <- piles) {
                hoursNeeded += (p.toLong + mid - 1) / mid
            }
            if (hoursNeeded <= h) {
                right = mid
            } else {
                left = mid + 1
            }
        }

        left.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut left: i64 = 1;
        let mut right: i64 = *piles.iter().max().unwrap() as i64;

        while left < right {
            let mid = (left + right) / 2;
            let mut hours_needed: i64 = 0;
            for &pile in piles.iter() {
                hours_needed += (pile as i64 + mid - 1) / mid;
                if hours_needed > h as i64 {
                    break;
                }
            }
            if hours_needed <= h as i64 {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left as i32
    }
}
```

## Racket

```racket
#lang racket

(provide min-eating-speed)

(define/contract (min-eating-speed piles h)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((max-pile (apply max piles))
         (hours-needed
          (lambda (speed)
            (foldl (lambda (pile acc)
                     (define q (quotient pile speed))
                     (+ acc (if (= (* q speed) pile) q (+ q 1))))
                   0
                   piles))))
    (let loop ((low 1) (high max-pile))
      (if (= low high)
          low
          (let* ((mid (quotient (+ low high) 2))
                 (need (hours-needed mid)))
            (if (<= need h)
                (loop low mid)
                (loop (+ mid 1) high)))))))
```

## Erlang

```erlang
-spec min_eating_speed([integer()], integer()) -> integer().
min_eating_speed(Piles, H) ->
    Max = lists:max(Piles),
    binary_search(Piles, H, 1, Max).

binary_search(_Piles, _H, Low, High) when Low >= High ->
    Low;
binary_search(Piles, H, Low, High) ->
    Mid = (Low + High) div 2,
    Hours = needed_hours(Piles, Mid),
    if
        Hours =< H -> binary_search(Piles, H, Low, Mid);
        true       -> binary_search(Piles, H, Mid + 1, High)
    end.

needed_hours(Piles, K) ->
    lists:foldl(fun(Pile, Acc) ->
        Acc + ((Pile + K - 1) div K)
    end, 0, Piles).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_eating_speed(piles :: [integer], h :: integer) :: integer
  def min_eating_speed(piles, h) do
    max_pile = Enum.max(piles)
    bs(piles, h, 1, max_pile)
  end

  defp bs(_piles, _h, lo, hi) when lo >= hi, do: lo

  defp bs(piles, h, lo, hi) do
    mid = div(lo + hi, 2)

    required =
      Enum.reduce(piles, 0, fn pile, acc ->
        acc + div(pile + mid - 1, mid)
      end)

    if required <= h do
      bs(piles, h, lo, mid)
    else
      bs(piles, h, mid + 1, hi)
    end
  end
end
```
