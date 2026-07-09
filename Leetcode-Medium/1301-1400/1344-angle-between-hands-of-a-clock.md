# 1344. Angle Between Hands of a Clock

## Cpp

```cpp
class Solution {
public:
    double angleClock(int hour, int minutes) {
        // Normalize hour to [0,11]
        hour %= 12;
        // Minute hand moves 6 degrees per minute
        double minuteAngle = minutes * 6.0;
        // Hour hand moves 30 degrees per hour + 0.5 degree per minute
        double hourAngle = hour * 30.0 + minutes * 0.5;
        double diff = fabs(hourAngle - minuteAngle);
        if (diff > 180.0) diff = 360.0 - diff;
        return diff;
    }
};
```

## Java

```java
class Solution {
    public double angleClock(int hour, int minutes) {
        // Normalize hour to 0-11 range
        hour = hour % 12;
        // Calculate angles of hour and minute hands
        double hourAngle = hour * 30.0 + minutes * 0.5; // 30 degrees per hour + 0.5 per minute
        double minuteAngle = minutes * 6.0; // 6 degrees per minute
        
        // Find absolute difference
        double diff = Math.abs(hourAngle - minuteAngle);
        // Return the smaller angle
        return Math.min(diff, 360.0 - diff);
    }
}
```

## Python

```python
class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # Normalize hour to 0-11 range
        hour %= 12
        # Minute hand moves 6 degrees per minute
        minute_angle = minutes * 6.0
        # Hour hand moves 30 degrees per hour plus 0.5 degree per minute
        hour_angle = hour * 30.0 + minutes * 0.5
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360.0 - diff)
```

## Python3

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Normalize hour to 0-11 range
        h = hour % 12
        # Calculate angles of hour and minute hands
        hour_angle = h * 30 + minutes * 0.5
        minute_angle = minutes * 6
        # Find the absolute difference
        diff = abs(hour_angle - minute_angle)
        # Return the smaller angle
        return min(diff, 360 - diff)
```

## C

```c
#include <math.h>

double angleClock(int hour, int minutes) {
    // Normalize hour to [0,11]
    hour %= 12;
    
    // Calculate angles of hour and minute hands
    double hourAngle = hour * 30.0 + minutes * 0.5;   // 30 degrees per hour + 0.5 per minute
    double minuteAngle = minutes * 6.0;              // 6 degrees per minute
    
    // Find absolute difference
    double diff = fabs(hourAngle - minuteAngle);
    
    // Return the smaller angle
    if (diff > 180.0) {
        diff = 360.0 - diff;
    }
    return diff;
}
```

## Csharp

```csharp
public class Solution {
    public double AngleClock(int hour, int minutes) {
        // Normalize hour to [0,11]
        hour = hour % 12;
        // Calculate angles
        double hourAngle = hour * 30.0 + minutes * 0.5; // each minute moves hour hand by 0.5 degrees
        double minuteAngle = minutes * 6.0; // each minute moves minute hand by 6 degrees
        
        double diff = Math.Abs(hourAngle - minuteAngle);
        return Math.Min(diff, 360.0 - diff);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} hour
 * @param {number} minutes
 * @return {number}
 */
var angleClock = function(hour, minutes) {
    const h = hour % 12;
    const hourAngle = h * 30 + minutes * 0.5;
    const minuteAngle = minutes * 6;
    let diff = Math.abs(hourAngle - minuteAngle);
    if (diff > 180) diff = 360 - diff;
    return diff;
};
```

## Typescript

```typescript
function angleClock(hour: number, minutes: number): number {
    const minuteAngle = minutes * 6;
    const hourAngle = (hour % 12) * 30 + minutes * 0.5;
    let diff = Math.abs(hourAngle - minuteAngle);
    if (diff > 180) diff = 360 - diff;
    return diff;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $hour
     * @param Integer $minutes
     * @return Float
     */
    function angleClock($hour, $minutes) {
        $hour = $hour % 12;
        $hourAngle = $hour * 30 + $minutes * 0.5;
        $minuteAngle = $minutes * 6;
        $diff = abs($hourAngle - $minuteAngle);
        if ($diff > 180) {
            $diff = 360 - $diff;
        }
        return $diff;
    }
}
```

## Swift

```swift
class Solution {
    func angleClock(_ hour: Int, _ minutes: Int) -> Double {
        let h = hour % 12
        let minuteAngle = Double(minutes) * 6.0
        let hourAngle = Double(h) * 30.0 + Double(minutes) * 0.5
        var diff = abs(hourAngle - minuteAngle)
        if diff > 180.0 {
            diff = 360.0 - diff
        }
        return diff
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun angleClock(hour: Int, minutes: Int): Double {
        val h = hour % 12
        val hourAngle = h * 30.0 + minutes * 0.5
        val minuteAngle = minutes * 6.0
        var diff = kotlin.math.abs(hourAngle - minuteAngle)
        if (diff > 180) diff = 360 - diff
        return diff
    }
}
```

## Dart

```dart
class Solution {
  double angleClock(int hour, int minutes) {
    double hourAngle = (hour % 12) * 30 + minutes * 0.5;
    double minuteAngle = minutes * 6.0;
    double diff = (hourAngle - minuteAngle).abs();
    if (diff > 180) diff = 360 - diff;
    return diff;
  }
}
```

## Golang

```go
func angleClock(hour int, minutes int) float64 {
    // Convert hour to 12-hour format
    h := hour % 12

    // Calculate angles of hour and minute hands
    minuteAngle := float64(minutes) * 6.0               // 360/60 = 6 degrees per minute
    hourAngle := float64(h)*30.0 + float64(minutes)*0.5 // 30 degrees per hour + 0.5 degree per minute

    // Find absolute difference
    diff := hourAngle - minuteAngle
    if diff < 0 {
        diff = -diff
    }

    // Return the smaller angle
    if diff > 180 {
        diff = 360 - diff
    }
    return diff
}
```

## Ruby

```ruby
def angle_clock(hour, minutes)
  hour %= 12
  minute_angle = minutes * 6.0
  hour_angle = hour * 30.0 + minutes * 0.5
  diff = (hour_angle - minute_angle).abs
  [diff, 360.0 - diff].min
end
```

## Scala

```scala
object Solution {
    def angleClock(hour: Int, minutes: Int): Double = {
        val h = (hour % 12) * 30.0 + minutes * 0.5
        val m = minutes * 6.0
        val diff = math.abs(h - m)
        math.min(diff, 360.0 - diff)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn angle_clock(hour: i32, minutes: i32) -> f64 {
        let h = (hour % 12) as f64;
        let m = minutes as f64;
        let minute_angle = m * 6.0;
        let hour_angle = h * 30.0 + m * 0.5;
        let mut diff = (hour_angle - minute_angle).abs();
        if diff > 180.0 {
            diff = 360.0 - diff;
        }
        diff
    }
}
```

## Racket

```racket
(define/contract (angle-clock hour minutes)
  (-> exact-integer? exact-integer? flonum?)
  (let* ([h (modulo hour 12)]
         [hour-angle (+ (* h 30) (* minutes 0.5))]
         [minute-angle (* minutes 6)]
         [diff (abs (- hour-angle minute-angle))])
    (if (> diff 180)
        (- 360 diff)
        diff)))
```

## Erlang

```erlang
-spec angle_clock(Hour :: integer(), Minutes :: integer()) -> float().
angle_clock(Hour, Minutes) ->
    HourMod = Hour rem 12,
    HourAngle = HourMod * 30 + Minutes * 0.5,
    MinuteAngle = Minutes * 6,
    Diff = abs(HourAngle - MinuteAngle),
    if
        Diff > 180 -> 360 - Diff;
        true -> Diff
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec angle_clock(hour :: integer, minutes :: integer) :: float
  def angle_clock(hour, minutes) do
    h = rem(hour, 12)
    hour_angle = h * 30 + minutes * 0.5
    minute_angle = minutes * 6
    diff = abs(hour_angle - minute_angle)

    if diff > 180 do
      360 - diff
    else
      diff
    end
  end
end
```
