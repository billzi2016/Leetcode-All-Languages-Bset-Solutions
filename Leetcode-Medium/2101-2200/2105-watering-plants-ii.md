# 2105. Watering Plants II

## Cpp

```cpp
class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        long long curA = capacityA;
        long long curB = capacityB;
        int i = 0, j = (int)plants.size() - 1;
        int refill = 0;
        while (i <= j) {
            if (i == j) {
                // Only one plant left, let the person with more water handle it
                if (curA >= curB) {
                    if (curA < plants[i]) ++refill, curA = capacityA;
                    curA -= plants[i];
                } else {
                    if (curB < plants[j]) ++refill, curB = capacityB;
                    curB -= plants[j];
                }
                break;
            }
            // Alice waters plant i
            if (curA < plants[i]) ++refill, curA = capacityA;
            curA -= plants[i];
            // Bob waters plant j
            if (curB < plants[j]) ++refill, curB = capacityB;
            curB -= plants[j];
            ++i;
            --j;
        }
        return refill;
    }
};
```

## Java

```java
class Solution {
    public int minimumRefill(int[] plants, int capacityA, int capacityB) {
        int n = plants.length;
        int left = 0, right = n - 1;
        long curA = capacityA;
        long curB = capacityB;
        int refills = 0;

        while (left <= right) {
            if (left == right) {
                // Only one plant remains; let the person with more water handle it
                if (curA >= curB) {
                    if (curA < plants[left]) {
                        refills++;
                        curA = capacityA;
                    }
                    curA -= plants[left];
                } else {
                    if (curB < plants[right]) {
                        refills++;
                        curB = capacityB;
                    }
                    curB -= plants[right];
                }
                break;
            }

            // Alice waters from the left
            if (curA < plants[left]) {
                refills++;
                curA = capacityA;
            }
            curA -= plants[left];
            left++;

            // Bob waters from the right
            if (curB < plants[right]) {
                refills++;
                curB = capacityB;
            }
            curB -= plants[right];
            right--;
        }

        return refills;
    }
}
```

## Python

```python
class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        waterA = capacityA
        waterB = capacityB
        i, j = 0, len(plants) - 1
        refills = 0

        while i < j:
            if waterA < plants[i]:
                refills += 1
                waterA = capacityA
            waterA -= plants[i]
            i += 1

            if waterB < plants[j]:
                refills += 1
                waterB = capacityB
            waterB -= plants[j]
            j -= 1

        if i == j:
            need = plants[i]
            if max(waterA, waterB) < need:
                refills += 1

        return refills
```

## Python3

```python
from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i, j = 0, len(plants) - 1
        waterA, waterB = capacityA, capacityB
        refills = 0

        while i <= j:
            if i == j:
                need = plants[i]
                # Choose the person with more water left (or Alice if equal)
                if waterA >= waterB:
                    if waterA < need:
                        refills += 1
                        waterA = capacityA
                    waterA -= need
                else:
                    if waterB < need:
                        refills += 1
                        waterB = capacityB
                    waterB -= need
                break

            # Alice waters plant i
            needA = plants[i]
            if waterA < needA:
                refills += 1
                waterA = capacityA
            waterA -= needA

            # Bob waters plant j
            needB = plants[j]
            if waterB < needB:
                refills += 1
                waterB = capacityB
            waterB -= needB

            i += 1
            j -= 1

        return refills
```

## C

```c
int minimumRefill(int* plants, int plantsSize, int capacityA, int capacityB) {
    long long curA = capacityA;
    long long curB = capacityB;
    int i = 0, j = plantsSize - 1;
    int refills = 0;

    while (i < j) {
        if (curA < plants[i]) {
            ++refills;
            curA = capacityA;
        }
        curA -= plants[i];
        ++i;

        if (curB < plants[j]) {
            ++refills;
            curB = capacityB;
        }
        curB -= plants[j];
        --j;
    }

    if (i == j) { // one plant left
        if (curA >= curB) {
            if (curA < plants[i]) ++refills;
        } else {
            if (curB < plants[i]) ++refills;
        }
    }

    return refills;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumRefill(int[] plants, int capacityA, int capacityB) {
        int i = 0;
        int j = plants.Length - 1;
        int waterA = capacityA;
        int waterB = capacityB;
        int refills = 0;

        while (i < j) {
            if (waterA < plants[i]) {
                refills++;
                waterA = capacityA;
            }
            waterA -= plants[i];
            i++;

            if (waterB < plants[j]) {
                refills++;
                waterB = capacityB;
            }
            waterB -= plants[j];
            j--;
        }

        if (i == j) {
            // middle plant
            if (waterA >= waterB) {
                if (waterA < plants[i]) {
                    refills++;
                }
            } else {
                if (waterB < plants[i]) {
                    refills++;
                }
            }
        }

        return refills;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} plants
 * @param {number} capacityA
 * @param {number} capacityB
 * @return {number}
 */
var minimumRefill = function(plants, capacityA, capacityB) {
    let i = 0, j = plants.length - 1;
    let waterA = capacityA, waterB = capacityB;
    let refills = 0;

    while (i < j) {
        // Alice waters plant i
        if (waterA < plants[i]) {
            refills++;
            waterA = capacityA;
        }
        waterA -= plants[i];
        i++;

        // Bob waters plant j
        if (waterB < plants[j]) {
            refills++;
            waterB = capacityB;
        }
        waterB -= plants[j];
        j--;
    }

    if (i === j) { // middle plant
        if (waterA >= waterB) {
            if (waterA < plants[i]) refills++;
        } else {
            if (waterB < plants[i]) refills++;
        }
    }

    return refills;
};
```

## Typescript

```typescript
function minimumRefill(plants: number[], capacityA: number, capacityB: number): number {
    let i = 0;
    let j = plants.length - 1;
    let curA = capacityA;
    let curB = capacityB;
    let refills = 0;

    while (i <= j) {
        if (i === j) {
            // decide who waters the middle plant
            if (curA >= curB) {
                if (curA < plants[i]) {
                    refills++;
                    curA = capacityA;
                }
                curA -= plants[i];
            } else {
                if (curB < plants[j]) {
                    refills++;
                    curB = capacityB;
                }
                curB -= plants[j];
            }
            break;
        }

        // Alice waters plant i
        if (curA < plants[i]) {
            refills++;
            curA = capacityA;
        }
        curA -= plants[i];
        i++;

        // Bob waters plant j
        if (curB < plants[j]) {
            refills++;
            curB = capacityB;
        }
        curB -= plants[j];
        j--;
    }

    return refills;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $plants
     * @param Integer $capacityA
     * @param Integer $capacityB
     * @return Integer
     */
    function minimumRefill($plants, $capacityA, $capacityB) {
        $n = count($plants);
        $left = 0;
        $right = $n - 1;
        $remA = $capacityA;
        $remB = $capacityB;
        $refills = 0;

        while ($left <= $right) {
            if ($left == $right) {
                $need = $plants[$left];
                // Choose the person with more water left
                if ($remA >= $remB) {
                    if ($remA < $need) {
                        $refills++;
                        $remA = $capacityA;
                    }
                    $remA -= $need;
                } else {
                    if ($remB < $need) {
                        $refills++;
                        $remB = $capacityB;
                    }
                    $remB -= $need;
                }
                break;
            }

            // Alice waters from the left
            $needA = $plants[$left];
            if ($remA < $needA) {
                $refills++;
                $remA = $capacityA;
            }
            $remA -= $needA;
            $left++;

            // Bob waters from the right
            $needB = $plants[$right];
            if ($remB < $needB) {
                $refills++;
                $remB = $capacityB;
            }
            $remB -= $needB;
            $right--;
        }

        return $refills;
    }
}
```

## Swift

```swift
class Solution {
    func minimumRefill(_ plants: [Int], _ capacityA: Int, _ capacityB: Int) -> Int {
        var left = 0
        var right = plants.count - 1
        var waterA = capacityA
        var waterB = capacityB
        var refills = 0

        while left <= right {
            if left == right {
                // Only one plant remains, decide who waters it
                if waterA >= waterB {
                    if waterA < plants[left] {
                        refills += 1
                        waterA = capacityA
                    }
                    waterA -= plants[left]
                } else {
                    if waterB < plants[right] {
                        refills += 1
                        waterB = capacityB
                    }
                    waterB -= plants[right]
                }
                break
            }

            // Alice waters the left plant
            if waterA < plants[left] {
                refills += 1
                waterA = capacityA
            }
            waterA -= plants[left]

            // Bob waters the right plant
            if waterB < plants[right] {
                refills += 1
                waterB = capacityB
            }
            waterB -= plants[right]

            left += 1
            right -= 1
        }

        return refills
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumRefill(plants: IntArray, capacityA: Int, capacityB: Int): Int {
        var waterA = capacityA
        var waterB = capacityB
        var refills = 0
        var left = 0
        var right = plants.size - 1

        while (left < right) {
            if (waterA < plants[left]) {
                refills++
                waterA = capacityA
            }
            waterA -= plants[left]
            left++

            if (waterB < plants[right]) {
                refills++
                waterB = capacityB
            }
            waterB -= plants[right]
            right--
        }

        if (left == right) {
            val need = plants[left]
            if (maxOf(waterA, waterB) < need) {
                refills++
            }
        }

        return refills
    }
}
```

## Dart

```dart
class Solution {
  int minimumRefill(List<int> plants, int capacityA, int capacityB) {
    int n = plants.length;
    int i = 0, j = n - 1;
    int waterA = capacityA;
    int waterB = capacityB;
    int refills = 0;

    while (i < j) {
      // Alice waters plant i
      if (waterA < plants[i]) {
        refills++;
        waterA = capacityA;
      }
      waterA -= plants[i];
      i++;

      // Bob waters plant j
      if (waterB < plants[j]) {
        refills++;
        waterB = capacityB;
      }
      waterB -= plants[j];
      j--;
    }

    if (i == j) {
      // One plant left, decide who waters it
      if (waterA >= waterB) {
        if (waterA < plants[i]) {
          refills++;
          waterA = capacityA;
        }
        waterA -= plants[i];
      } else {
        if (waterB < plants[i]) {
          refills++;
          waterB = capacityB;
        }
        waterB -= plants[i];
      }
    }

    return refills;
  }
}
```

## Golang

```go
func minimumRefill(plants []int, capacityA int, capacityB int) int {
    a, b := capacityA, capacityB
    refills := 0
    i, j := 0, len(plants)-1

    for i < j {
        if a < plants[i] {
            refills++
            a = capacityA
        }
        a -= plants[i]
        i++

        if b < plants[j] {
            refills++
            b = capacityB
        }
        b -= plants[j]
        j--
    }

    if i == j { // middle plant when n is odd
        need := plants[i]
        if a >= b {
            if a < need {
                refills++
            }
        } else {
            if b < need {
                refills++
            }
        }
    }

    return refills
}
```

## Ruby

```ruby
def minimum_refill(plants, capacity_a, capacity_b)
  i = 0
  j = plants.length - 1
  water_a = capacity_a
  water_b = capacity_b
  refills = 0

  while i < j
    need = plants[i]
    if water_a < need
      refills += 1
      water_a = capacity_a
    end
    water_a -= need
    i += 1

    need = plants[j]
    if water_b < need
      refills += 1
      water_b = capacity_b
    end
    water_b -= need
    j -= 1
  end

  if i == j
    need = plants[i]
    if water_a >= water_b
      if water_a < need
        refills += 1
        water_a = capacity_a
      end
      water_a -= need
    else
      if water_b < need
        refills += 1
        water_b = capacity_b
      end
      water_b -= need
    end
  end

  refills
end
```

## Scala

```scala
object Solution {
    def minimumRefill(plants: Array[Int], capacityA: Int, capacityB: Int): Int = {
        var i = 0
        var j = plants.length - 1
        var remA = capacityA
        var remB = capacityB
        var refills = 0

        while (i <= j) {
            if (i == j) {
                val need = plants(i)
                if (remA >= remB) {
                    if (remA < need) { refills += 1; remA = capacityA }
                    remA -= need
                } else {
                    if (remB < need) { refills += 1; remB = capacityB }
                    remB -= need
                }
                i = j + 1 // exit loop
            } else {
                val needA = plants(i)
                if (remA < needA) { refills += 1; remA = capacityA }
                remA -= needA
                i += 1

                val needB = plants(j)
                if (remB < needB) { refills += 1; remB = capacityB }
                remB -= needB
                j -= 1
            }
        }

        refills
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_refill(plants: Vec<i32>, capacity_a: i32, capacity_b: i32) -> i32 {
        let n = plants.len();
        if n == 0 {
            return 0;
        }
        let mut left = 0usize;
        let mut right = n - 1;
        let mut rem_a = capacity_a;
        let mut rem_b = capacity_b;
        let mut refills = 0i32;

        while left < right {
            // Alice waters plant at 'left'
            if rem_a < plants[left] {
                refills += 1;
                rem_a = capacity_a;
            }
            rem_a -= plants[left];

            // Bob waters plant at 'right'
            if rem_b < plants[right] {
                refills += 1;
                rem_b = capacity_b;
            }
            rem_b -= plants[right];

            left += 1;
            right -= 1;
        }

        if left == right {
            let need = plants[left];
            // Choose the person with more water remaining
            if rem_a >= rem_b {
                if rem_a < need {
                    refills += 1;
                }
            } else {
                if rem_b < need {
                    refills += 1;
                }
            }
        }

        refills
    }
}
```

## Racket

```racket
(define/contract (minimum-refill plants capacityA capacityB)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length plants))
         (left 0)
         (right (sub1 n))
         (a-rem capacityA)
         (b-rem capacityB)
         (refills 0))
    (define (plant-at idx) (list-ref plants idx))
    (let loop ()
      (cond
        [(> left right) refills]
        [(= left right)
         (let ((need (plant-at left)))
           (if (>= (max a-rem b-rem) need)
               refills
               (+ refills 1))))]
        [else
         ;; Alice waters from the left
         (let ((needA (plant-at left)))
           (when (< a-rem needA)
             (set! refills (+ refills 1))
             (set! a-rem capacityA))
           (set! a-rem (- a-rem needA))
           (set! left (+ left 1)))
         ;; Bob waters from the right
         (let ((needB (plant-at right)))
           (when (< b-rem needB)
             (set! refills (+ refills 1))
             (set! b-rem capacityB))
           (set! b-rem (- b-rem needB))
           (set! right (- right 1)))
         (loop)]))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_refill/3]).

-spec minimum_refill([integer()], integer(), integer()) -> integer().
minimum_refill(Plants, CapacityA, CapacityB) ->
    Tuple = list_to_tuple(Plants),
    N = tuple_size(Tuple),
    loop(0, N - 1, CapacityA, CapacityB, 0, Tuple, CapacityA, CapacityB).

-spec loop(integer(), integer(), integer(), integer(), integer(),
           tuple(), integer(), integer()) -> integer().
loop(I, J, _ARem, _BRem, Count, _Tuple, _CapA, _CapB) when I > J ->
    Count;
loop(I, J, ARem, BRem, Count, Tuple, CapA, CapB) when I == J ->
    Need = element(I + 1, Tuple),
    if
        ARem >= BRem ->
            case ARem < Need of
                true -> Count + 1;
                false -> Count
            end;
        true ->
            case BRem < Need of
                true -> Count + 1;
                false -> Count
            end
    end;
loop(I, J, ARem, BRem, Count, Tuple, CapA, CapB) ->
    NeedA = element(I + 1, Tuple),
    {NewARem, NewCount} =
        case ARem < NeedA of
            true -> {CapA - NeedA, Count + 1};
            false -> {ARem - NeedA, Count}
        end,
    NeedB = element(J + 1, Tuple),
    {NewBRem, FinalCount} =
        case BRem < NeedB of
            true -> {CapB - NeedB, NewCount + 1};
            false -> {BRem - NeedB, NewCount}
        end,
    loop(I + 1, J - 1, NewARem, NewBRem, FinalCount, Tuple, CapA, CapB).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_refill(plants :: [integer], capacity_a :: integer, capacity_b :: integer) :: integer
  def minimum_refill(plants, capacity_a, capacity_b) do
    go(plants, 0, length(plants) - 1, capacity_a, capacity_b, capacity_a, capacity_b, 0)
  end

  defp go(_plants, l, r, _water_a, _water_b, _cap_a, _cap_b, refills) when l > r do
    refills
  end

  defp go(plants, l, r, water_a, water_b, cap_a, cap_b, refills) when l == r do
    need = Enum.at(plants, l)

    cond do
      water_a >= water_b ->
        if water_a < need do
          # refill Alice
          refills + 1
        else
          refills
        end

      true ->
        if water_b < need do
          # refill Bob
          refills + 1
        else
          refills
        end
    end
  end

  defp go(plants, l, r, water_a, water_b, cap_a, cap_b, refills) do
    need_a = Enum.at(plants, l)
    {water_a2, refills1} =
      if water_a < need_a do
        {cap_a - need_a, refills + 1}
      else
        {water_a - need_a, refills}
      end

    need_b = Enum.at(plants, r)
    {water_b2, refills2} =
      if water_b < need_b do
        {cap_b - need_b, refills1 + 1}
      else
        {water_b - need_b, refills1}
      end

    go(plants, l + 1, r - 1, water_a2, water_b2, cap_a, cap_b, refills2)
  end
end
```
