# 1184. Distance Between Bus Stops

## Cpp

```cpp
class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        if (start == destination) return 0;
        if (start > destination) swap(start, destination);
        int clockwise = 0;
        for (int i = start; i < destination; ++i) {
            clockwise += distance[i];
        }
        int total = 0;
        for (int d : distance) total += d;
        return min(clockwise, total - clockwise);
    }
};
```

## Java

```java
class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start == destination) return 0;
        int n = distance.length;
        int clockwise = 0;
        int i = start;
        while (i != destination) {
            clockwise += distance[i];
            i = (i + 1) % n;
        }
        int total = 0;
        for (int d : distance) total += d;
        return Math.min(clockwise, total - clockwise);
    }
}
```

## Python

```python
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start == destination:
            return 0
        # Ensure start is less than destination for clockwise calculation
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        total = sum(distance)
        counter_clockwise = total - clockwise
        return min(clockwise, counter_clockwise)
```

## Python3

```python
from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        total = sum(distance)
        return min(clockwise, total - clockwise)
```

## C

```c
int distanceBetweenBusStops(int* distance, int distanceSize, int start, int destination){
    if (start == destination) return 0;
    // Ensure start is less than destination for easier loop, but we can compute directly.
    int total = 0;
    for (int i = 0; i < distanceSize; ++i) {
        total += distance[i];
    }
    int clockwise = 0;
    int i = start;
    while (i != destination) {
        clockwise += distance[i];
        i = (i + 1) % distanceSize;
    }
    int counterClockwise = total - clockwise;
    return clockwise < counterClockwise ? clockwise : counterClockwise;
}
```

## Csharp

```csharp
public class Solution {
    public int DistanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start > destination) {
            int temp = start;
            start = destination;
            destination = temp;
        }
        int clockwise = 0;
        for (int i = start; i < destination; i++) {
            clockwise += distance[i];
        }
        int total = 0;
        foreach (int d in distance) {
            total += d;
        }
        int counterClockwise = total - clockwise;
        return Math.Min(clockwise, counterClockwise);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
    if (start === destination) return 0;
    // Ensure start is the smaller index for clockwise traversal
    let s = Math.min(start, destination);
    let d = Math.max(start, destination);
    
    let clockwise = 0;
    for (let i = s; i < d; ++i) {
        clockwise += distance[i];
    }
    
    const total = distance.reduce((a, b) => a + b, 0);
    return Math.min(clockwise, total - clockwise);
};
```

## Typescript

```typescript
function distanceBetweenBusStops(distance: number[], start: number, destination: number): number {
    if (start === destination) return 0;
    const n = distance.length;
    // Ensure start is less than destination for easier iteration
    let s = start, d = destination;
    if (s > d) {
        [s, d] = [d, s];
    }
    let clockwise = 0;
    for (let i = s; i < d; i++) {
        clockwise += distance[i];
    }
    const total = distance.reduce((acc, val) => acc + val, 0);
    const counterClockwise = total - clockwise;
    return Math.min(clockwise, counterClockwise);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $distance
     * @param Integer $start
     * @param Integer $destination
     * @return Integer
     */
    function distanceBetweenBusStops($distance, $start, $destination) {
        if ($start == $destination) {
            return 0;
        }
        $low = min($start, $destination);
        $high = max($start, $destination);
        $direct = 0;
        for ($i = $low; $i < $high; $i++) {
            $direct += $distance[$i];
        }
        $total = array_sum($distance);
        return min($direct, $total - $direct);
    }
}
```

## Swift

```swift
class Solution {
    func distanceBetweenBusStops(_ distance: [Int], _ start: Int, _ destination: Int) -> Int {
        if start == destination { return 0 }
        let n = distance.count
        var clockwise = 0
        var i = start
        while i != destination {
            clockwise += distance[i]
            i = (i + 1) % n
        }
        let total = distance.reduce(0, +)
        return min(clockwise, total - clockwise)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distanceBetweenBusStops(distance: IntArray, start: Int, destination: Int): Int {
        if (start == destination) return 0
        val n = distance.size
        var clockwise = 0
        var i = start
        while (i != destination) {
            clockwise += distance[i]
            i = (i + 1) % n
        }
        val total = distance.sum()
        val counterClockwise = total - clockwise
        return kotlin.math.min(clockwise, counterClockwise)
    }
}
```

## Golang

```go
func distanceBetweenBusStops(distance []int, start int, destination int) int {
	if start == destination {
		return 0
	}
	total := 0
	for _, d := range distance {
		total += d
	}
	cw := 0
	i := start
	n := len(distance)
	for i != destination {
		cw += distance[i]
		i = (i + 1) % n
	}
	if cw > total-cw {
		return total - cw
	}
	return cw
}
```

## Ruby

```ruby
def distance_between_bus_stops(distance, start, destination)
  return 0 if start == destination
  s, e = [start, destination].minmax
  clockwise = distance[s...e].sum
  total = distance.sum
  counter = total - clockwise
  [clockwise, counter].min
end
```

## Scala

```scala
object Solution {
    def distanceBetweenBusStops(distance: Array[Int], start: Int, destination: Int): Int = {
        if (start == destination) return 0
        var s = start
        var d = destination
        if (s > d) { val tmp = s; s = d; d = tmp }
        var clockwise = 0
        var i = s
        while (i < d) {
            clockwise += distance(i)
            i += 1
        }
        val total = distance.sum
        math.min(clockwise, total - clockwise)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distance_between_bus_stops(distance: Vec<i32>, start: i32, destination: i32) -> i32 {
        let mut s = start as usize;
        let mut d = destination as usize;
        if s > d {
            std::mem::swap(&mut s, &mut d);
        }
        let total: i32 = distance.iter().sum();
        let mut forward = 0i32;
        for i in s..d {
            forward += distance[i];
        }
        std::cmp::min(forward, total - forward)
    }
}
```
