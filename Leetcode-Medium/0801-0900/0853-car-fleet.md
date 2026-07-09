# 0853. Car Fleet

## Cpp

```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, double>> cars;
        cars.reserve(n);
        for (int i = 0; i < n; ++i) {
            double time = static_cast<double>(target - position[i]) / speed[i];
            cars.emplace_back(position[i], time);
        }
        sort(cars.begin(), cars.end(),
             [](const pair<int, double>& a, const pair<int, double>& b) {
                 return a.first > b.first; // descending by position
             });
        int fleets = 0;
        double curMaxTime = 0.0;
        for (const auto& car : cars) {
            if (car.second > curMaxTime) {
                ++fleets;
                curMaxTime = car.second;
            }
        }
        return fleets;
    }
};
```

## Java

```java
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        // Pair positions with times
        double[][] cars = new double[n][2];
        for (int i = 0; i < n; i++) {
            double time = (double)(target - position[i]) / speed[i];
            cars[i][0] = position[i];
            cars[i][1] = time;
        }
        // Sort by starting position descending
        java.util.Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0]));
        
        int fleets = 0;
        double maxTime = 0.0;
        for (int i = 0; i < n; i++) {
            double curTime = cars[i][1];
            if (curTime > maxTime) {
                fleets++;
                maxTime = curTime;
            }
        }
        return fleets;
    }
}
```

## Python

```python
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Pair each car's start position with its time to reach the target
        cars = sorted(zip(position, speed), key=lambda x: -x[0])  # descending by position
        fleets = 0
        max_time = 0.0
        for pos, spd in cars:
            time = (target - pos) / float(spd)
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets
```

## Python3

```python
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        fleets = 0
        max_time = 0.0
        for pos, sp in cars:
            time = (target - pos) / sp
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets
```

## C

```c
#include <stdlib.h>

typedef struct {
    int pos;
    int speed;
} Car;

static int cmpCarDesc(const void *a, const void *b) {
    int pa = ((const Car *)a)->pos;
    int pb = ((const Car *)b)->pos;
    return pb - pa; // descending order
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    if (positionSize == 0) return 0;

    Car *cars = (Car *)malloc(positionSize * sizeof(Car));
    for (int i = 0; i < positionSize; ++i) {
        cars[i].pos = position[i];
        cars[i].speed = speed[i];
    }

    qsort(cars, positionSize, sizeof(Car), cmpCarDesc);

    int fleets = 0;
    double maxTime = -1.0;

    for (int i = 0; i < positionSize; ++i) {
        double time = (double)(target - cars[i].pos) / cars[i].speed;
        if (time > maxTime) {
            ++fleets;
            maxTime = time;
        }
    }

    free(cars);
    return fleets;
}
```

## Csharp

```csharp
public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        int n = position.Length;
        var cars = new (int pos, double time)[n];
        for (int i = 0; i < n; i++) {
            double t = (double)(target - position[i]) / speed[i];
            cars[i] = (position[i], t);
        }
        System.Array.Sort(cars, (a, b) => b.pos.CompareTo(a.pos)); // descending by position

        int fleets = 0;
        double maxTime = 0.0;
        foreach (var car in cars) {
            if (car.time > maxTime) {
                fleets++;
                maxTime = car.time;
            }
        }
        return fleets;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    const n = position.length;
    const cars = new Array(n);
    for (let i = 0; i < n; i++) {
        cars[i] = [position[i], (target - position[i]) / speed[i]];
    }
    // Sort by starting position descending (closest to target first)
    cars.sort((a, b) => b[0] - a[0]);
    
    let fleets = 0;
    let curMaxTime = 0;
    for (let i = 0; i < n; i++) {
        const time = cars[i][1];
        if (time > curMaxTime) {
            fleets++;
            curMaxTime = time;
        }
        // else it joins the fleet ahead
    }
    return fleets;
};
```

## Typescript

```typescript
function carFleet(target: number, position: number[], speed: number[]): number {
    const n = position.length;
    if (n === 0) return 0;

    const cars: [number, number][] = new Array(n);
    for (let i = 0; i < n; i++) {
        const time = (target - position[i]) / speed[i];
        cars[i] = [position[i], time];
    }

    // Sort by starting position descending (closest to target first)
    cars.sort((a, b) => b[0] - a[0]);

    let fleets = 0;
    let maxTime = 0;

    for (let i = 0; i < n; i++) {
        const t = cars[i][1];
        if (t > maxTime) {
            fleets++;
            maxTime = t;
        }
    }

    return fleets;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer[] $position
     * @param Integer[] $speed
     * @return Integer
     */
    function carFleet($target, $position, $speed) {
        $n = count($position);
        $cars = [];
        for ($i = 0; $i < $n; $i++) {
            $time = ($target - $position[$i]) / $speed[$i];
            $cars[] = [$position[$i], $time];
        }
        usort($cars, function($a, $b) {
            return $b[0] <=> $a[0]; // descending by position
        });

        $fleets = 0;
        $maxTime = -1.0;
        foreach ($cars as $car) {
            $time = $car[1];
            if ($time > $maxTime) {
                $fleets++;
                $maxTime = $time;
            }
        }
        return $fleets;
    }
}
```

## Swift

```swift
class Solution {
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        let n = position.count
        var cars = [(pos: Int, time: Double)]()
        cars.reserveCapacity(n)
        for i in 0..<n {
            let dist = target - position[i]
            let t = Double(dist) / Double(speed[i])
            cars.append((position[i], t))
        }
        cars.sort { $0.pos > $1.pos } // descending by position
        
        var fleets = 0
        var maxTime: Double = 0.0
        for car in cars {
            if car.time > maxTime {
                fleets += 1
                maxTime = car.time
            }
        }
        return fleets
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun carFleet(target: Int, position: IntArray, speed: IntArray): Int {
        val n = position.size
        if (n == 0) return 0
        val cars = Array(n) { i ->
            Pair(position[i], (target - position[i]).toDouble() / speed[i])
        }
        cars.sortByDescending { it.first }
        var fleets = 0
        var maxTime = 0.0
        for ((_, time) in cars) {
            if (time > maxTime) {
                fleets++
                maxTime = time
            }
        }
        return fleets
    }
}
```

## Dart

```dart
class Solution {
  int carFleet(int target, List<int> position, List<int> speed) {
    int n = position.length;
    List<_Car> cars = List.generate(
      n,
      (i) => _Car(position[i], (target - position[i]) / speed[i]),
    );
    cars.sort((a, b) => b.pos.compareTo(a.pos)); // descending by position

    double lastTime = 0.0;
    int fleets = 0;

    for (var car in cars) {
      if (car.time > lastTime) {
        fleets++;
        lastTime = car.time;
      }
    }

    return fleets;
  }
}

class _Car {
  final int pos;
  final double time;
  _Car(this.pos, this.time);
}
```

## Golang

```go
func carFleet(target int, position []int, speed []int) int {
	type Car struct {
		pos  int
		time float64
	}
	n := len(position)
	cars := make([]Car, n)
	for i := 0; i < n; i++ {
		dist := target - position[i]
		t := float64(dist) / float64(speed[i])
		cars[i] = Car{pos: position[i], time: t}
	}
	sort.Slice(cars, func(i, j int) bool {
		return cars[i].pos > cars[j].pos
	})
	fleets := 0
	maxTime := -1.0
	for _, c := range cars {
		if c.time > maxTime {
			fleets++
			maxTime = c.time
		}
	}
	return fleets
}
```

## Ruby

```ruby
def car_fleet(target, position, speed)
  cars = position.zip(speed).map { |p, s| [p, (target - p).to_f / s] }
  cars.sort_by! { |p, _| -p }
  fleets = 0
  max_time = 0.0
  cars.each do |_pos, time|
    if time > max_time
      fleets += 1
      max_time = time
    end
  end
  fleets
end
```

## Scala

```scala
object Solution {
    def carFleet(target: Int, position: Array[Int], speed: Array[Int]): Int = {
        val n = position.length
        // Pair each car's position with its time to reach target
        val cars = new Array[(Int, Double)](n)
        var i = 0
        while (i < n) {
            val pos = position(i)
            val spd = speed(i).toDouble
            val time = (target - pos).toDouble / spd
            cars(i) = (pos, time)
            i += 1
        }
        // Sort by starting position descending (closest to target first)
        java.util.Arrays.sort(cars, new java.util.Comparator[(Int, Double)] {
            override def compare(a: (Int, Double), b: (Int, Double)): Int = 
                Integer.compare(b._1, a._1)
        })
        var fleets = 0
        var maxTime = 0.0
        i = 0
        while (i < n) {
            val time = cars(i)._2
            if (time > maxTime) {
                fleets += 1
                maxTime = time
            }
            i += 1
        }
        fleets
    }
}
```

## Rust

```rust
impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut cars: Vec<(i32, f64)> = position
            .into_iter()
            .zip(speed.into_iter())
            .map(|(p, s)| (p, (target - p) as f64 / s as f64))
            .collect();
        // Sort by starting position descending (closest to target first)
        cars.sort_by(|a, b| b.0.cmp(&a.0));
        let mut fleets = 0;
        let mut cur_time = 0.0_f64;
        for &(_, t) in cars.iter() {
            if t > cur_time {
                fleets += 1;
                cur_time = t;
            }
        }
        fleets
    }
}
```

## Racket

```racket
(define/contract (car-fleet target position speed)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((pairs (map (lambda (pos spd) (cons pos (/ (- target pos) spd))) position speed))
         (sorted (sort pairs (lambda (a b) (> (car a) (car b))))))
    (let loop ((lst sorted) (max-time -inf.0) (fleets 0))
      (if (null? lst)
          fleets
          (let* ((time (cdr (car lst)))
                 (new-fleets (if (> time max-time) (+ fleets 1) fleets))
                 (new-max (if (> time max-time) time max-time)))
            (loop (cdr lst) new-max new-fleets))))))
```

## Erlang

```erlang
-spec car_fleet(Target :: integer(), Position :: [integer()], Speed :: [integer()]) -> integer().
car_fleet(Target, Position, Speed) ->
    Cars = [{Pos, (Target - Pos) / Spd} || {Pos, Spd} <- lists:zip(Position, Speed)],
    Sorted = lists:keysort(1, Cars),
    RevSorted = lists:reverse(Sorted),
    {Count, _} = lists:foldl(
        fun({_, Time}, {Cnt, MaxTime}) ->
            case Time > MaxTime of
                true -> {Cnt + 1, Time};
                false -> {Cnt, MaxTime}
            end
        end,
        {0, -1.0},
        RevSorted),
    Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec car_fleet(target :: integer, position :: [integer], speed :: [integer]) :: integer
  def car_fleet(target, position, speed) do
    cars =
      Enum.zip(position, speed)
      |> Enum.map(fn {p, s} -> {p, (target - p) / s} end)
      |> Enum.sort_by(fn {p, _t} -> -p end)

    {count, _max_time} =
      Enum.reduce(cars, {0, 0.0}, fn {_pos, time}, {cnt, max_time} ->
        if time > max_time do
          {cnt + 1, time}
        else
          {cnt, max_time}
        end
      end)

    count
  end
end
```
