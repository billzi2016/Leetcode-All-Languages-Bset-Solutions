# 2739. Total Distance Traveled

## Cpp

```cpp
class Solution {
public:
    int distanceTraveled(int mainTank, int additionalTank) {
        int distance = 0;
        while (mainTank >= 5 && additionalTank > 0) {
            mainTank -= 5;          // consume 5 liters
            distance += 50;         // 10 km per liter * 5
            mainTank += 1;          // transfer from additional tank
            additionalTank -= 1;
        }
        distance += mainTank * 10;   // use remaining fuel in main tank
        return distance;
    }
};
```

## Java

```java
class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        long distance = 0;
        while (mainTank > 0) {
            if (mainTank >= 5) {
                // consume 5 liters
                distance += 50; // 5 * 10 km
                mainTank -= 5;
                // transfer from additional tank if possible
                if (additionalTank > 0) {
                    mainTank += 1;
                    additionalTank--;
                }
            } else {
                // consume the remaining fuel
                distance += (long) mainTank * 10;
                break;
            }
        }
        return (int) distance;
    }
}
```

## Python

```python
class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        distance = 0
        while mainTank > 0:
            if mainTank >= 5:
                distance += 5 * 10
                mainTank -= 5
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1
            else:
                distance += mainTank * 10
                break
        return distance
```

## Python3

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank > 0:
            if mainTank >= 5:
                # consume 5 liters
                distance += 50
                mainTank -= 5
                # transfer from additional tank if possible
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1
            else:
                # consume the remaining fuel
                distance += mainTank * 10
                break
        return distance
```

## C

```c
int distanceTraveled(int mainTank, int additionalTank) {
    int distance = 0;
    while (mainTank > 0) {
        if (mainTank >= 5) {
            // consume 5 liters
            distance += 50;          // 5 * 10 km
            mainTank -= 5;
            // transfer from additional tank if possible
            if (additionalTank > 0) {
                mainTank += 1;
                additionalTank--;
            }
        } else {
            // consume the remaining fuel
            distance += mainTank * 10;
            mainTank = 0;
        }
    }
    return distance;
}
```

## Csharp

```csharp
public class Solution {
    public int DistanceTraveled(int mainTank, int additionalTank) {
        int distance = 0;
        while (mainTank > 0) {
            if (mainTank >= 5) {
                // consume 5 liters
                distance += 50; // 5 * 10 km
                mainTank -= 5;
                // transfer from additional tank if possible
                if (additionalTank > 0) {
                    mainTank += 1;
                    additionalTank--;
                }
            } else {
                // consume the remaining fuel
                distance += mainTank * 10;
                mainTank = 0;
            }
        }
        return distance;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} mainTank
 * @param {number} additionalTank
 * @return {number}
 */
var distanceTraveled = function(mainTank, additionalTank) {
    let distance = 0;
    while (mainTank > 0) {
        if (mainTank >= 5 && additionalTank > 0) {
            // consume 5 liters from main tank
            mainTank -= 5;
            distance += 5 * 10;
            // transfer 1 liter from additional to main tank
            additionalTank--;
            mainTank += 1;
        } else {
            // consume whatever is left in the main tank
            distance += mainTank * 10;
            break;
        }
    }
    return distance;
};
```

## Typescript

```typescript
function distanceTraveled(mainTank: number, additionalTank: number): number {
    let distance = 0;
    while (mainTank > 0) {
        if (mainTank >= 5) {
            distance += 50; // 5 liters * 10 km per liter
            mainTank -= 5;
            if (additionalTank > 0) {
                mainTank += 1;
                additionalTank -= 1;
            }
        } else {
            distance += mainTank * 10;
            break;
        }
    }
    return distance;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $mainTank
     * @param Integer $additionalTank
     * @return Integer
     */
    function distanceTraveled($mainTank, $additionalTank) {
        $distance = 0;
        while ($mainTank > 0) {
            if ($mainTank >= 5) {
                $mainTank -= 5;
                $distance += 50; // 5 liters * 10 km per liter
                if ($additionalTank > 0) {
                    $mainTank += 1;
                    $additionalTank -= 1;
                }
            } else {
                $distance += $mainTank * 10;
                $mainTank = 0;
            }
        }
        return $distance;
    }
}
```

## Swift

```swift
class Solution {
    func distanceTraveled(_ mainTank: Int, _ additionalTank: Int) -> Int {
        var m = mainTank
        var a = additionalTank
        var totalLiters = 0

        while m >= 5 {
            m -= 5
            totalLiters += 5
            if a > 0 {
                m += 1
                a -= 1
            }
        }

        totalLiters += m
        return totalLiters * 10
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distanceTraveled(mainTank: Int, additionalTank: Int): Int {
        val possibleTransfers = (mainTank - 1) / 4
        val transfers = kotlin.math.min(additionalTank, possibleTransfers)
        return (mainTank + transfers) * 10
    }
}
```

## Dart

```dart
class Solution {
  int distanceTraveled(int mainTank, int additionalTank) {
    int distance = 0;
    while (mainTank >= 5 && additionalTank > 0) {
      // Travel 5 liters worth of distance
      distance += 50; // 5 * 10 km per liter
      // Consume 5 liters and receive 1 liter from the additional tank
      mainTank = mainTank - 4; // net decrease of 4 liters
      additionalTank--;
    }
    // Use any remaining fuel in the main tank
    distance += mainTank * 10;
    return distance;
  }
}
```

## Golang

```go
func distanceTraveled(mainTank int, additionalTank int) int {
    distance := 0
    for mainTank > 0 {
        if mainTank >= 5 {
            distance += 50
            mainTank -= 5
            if additionalTank > 0 {
                additionalTank--
                mainTank++
            }
        } else {
            distance += mainTank * 10
            mainTank = 0
        }
    }
    return distance
}
```

## Ruby

```ruby
def distance_traveled(main_tank, additional_tank)
  distance = 0
  while main_tank > 0
    if main_tank >= 5
      distance += 50
      main_tank -= 5
      if additional_tank > 0
        main_tank += 1
        additional_tank -= 1
      end
    else
      distance += main_tank * 10
      break
    end
  end
  distance
end
```

## Scala

```scala
object Solution {
    def distanceTraveled(mainTank: Int, additionalTank: Int): Int = {
        var main = mainTank
        var add = additionalTank
        var distance = 0
        while (main >= 5) {
            distance += 50          // travel 5 liters * 10 km/l
            main -= 5
            if (add > 0) {
                main += 1           // transfer from additional tank
                add -= 1
            }
        }
        distance + main * 10       // consume remaining fuel
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distance_traveled(main_tank: i32, additional_tank: i32) -> i32 {
        let mut main = main_tank;
        let mut add = additional_tank;
        let mut liters = 0;

        while main > 0 {
            if main >= 5 {
                main -= 5;
                liters += 5;
                if add > 0 {
                    main += 1;
                    add -= 1;
                }
            } else {
                liters += main;
                main = 0;
            }
        }

        liters * 10
    }
}
```

## Racket

```racket
(define/contract (distance-traveled mainTank additionalTank)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((mt mainTank) (at additionalTank) (dist 0))
    (cond
      [(zero? mt) dist]
      [(>= mt 5)
       (let* ([new-mt (- mt 5)]
              [new-dist (+ dist 50)])
         (if (> at 0)
             (loop (+ new-mt 1) (- at 1) new-dist)
             (loop new-mt at new-dist))))]
      [else
       (+ dist (* mt 10))])))
```

## Erlang

```erlang
-spec distance_traveled(MainTank :: integer(), AdditionalTank :: integer()) -> integer().
distance_traveled(MainTank, AdditionalTank) ->
    distance_traveled_loop(MainTank, AdditionalTank, 0).

distance_traveled_loop(Main, Add, Dist) when Main >= 5, Add > 0 ->
    distance_traveled_loop(Main - 4, Add - 1, Dist + 50);
distance_traveled_loop(Main, _Add, Dist) ->
    Dist + Main * 10.
```

## Elixir

```elixir
defmodule Solution do
  @spec distance_traveled(main_tank :: integer, additional_tank :: integer) :: integer
  def distance_traveled(main_tank, additional_tank) do
    travel(main_tank, additional_tank, 0)
  end

  defp travel(m, a, dist) when m >= 5 do
    m_after = m - 5
    dist_after = dist + 50

    if a > 0 do
      travel(m_after + 1, a - 1, dist_after)
    else
      travel(m_after, a, dist_after)
    end
  end

  defp travel(m, _a, dist) do
    dist + m * 10
  end
end
```
