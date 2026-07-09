# 2079. Watering Plants

## Cpp

```cpp
class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        long long steps = 0;
        int water = capacity;
        for (int i = 0; i < (int)plants.size(); ++i) {
            if (water < plants[i]) {
                // go back to river and return to plant i
                steps += 2LL * i + 1;
                water = capacity;
            } else {
                // move from previous position (or start) to this plant
                steps += 1;
            }
            water -= plants[i];
        }
        return (int)steps;
    }
};
```

## Java

```java
class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        int steps = 0;
        int water = capacity;
        int pos = -1; // start at the river
        for (int i = 0; i < plants.length; i++) {
            if (water < plants[i]) {
                // go back to river and refill
                steps += (pos + 1);   // move from current position to river (-1)
                steps += (i + 1);     // move from river to plant i
                pos = i;
                water = capacity;
            } else {
                // just move forward to the next plant
                steps += (i - pos);
                pos = i;
            }
            water -= plants[i];
        }
        return steps;
    }
}
```

## Python

```python
class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        pos = -1          # current position, start at river (-1)
        water = capacity  # current water in can

        for i, need in enumerate(plants):
            if water < need:
                # return to river to refill
                steps += (pos + 1)   # distance from current pos to river at -1
                pos = -1
                water = capacity
            # move from current position to plant i
            steps += (i - pos)
            pos = i
            water -= need

        return steps
```

## Python3

```python
class Solution:
    def wateringPlants(self, plants, capacity):
        steps = 0
        water = capacity
        pos = -1  # start at the river
        
        for i, need in enumerate(plants):
            if water < need:
                # go back to river to refill
                steps += pos + 1          # distance from current position to -1
                pos = -1
                water = capacity
            # move from current position to plant i
            steps += i - pos
            pos = i
            water -= need
        
        return steps
```

## C

```c
int wateringPlants(int* plants, int plantsSize, int capacity) {
    int steps = 0;
    int cur = capacity;
    for (int i = 0; i < plantsSize; ++i) {
        if (cur < plants[i]) {
            steps += 2 * i + 1; // go back to river and return
            cur = capacity;
        } else {
            steps += 1; // move from previous plant
        }
        cur -= plants[i];
    }
    return steps;
}
```

## Csharp

```csharp
public class Solution {
    public int WateringPlants(int[] plants, int capacity) {
        int steps = 0;
        int cur = capacity;
        for (int i = 0; i < plants.Length; i++) {
            if (cur < plants[i]) {
                // Return to river from previous position (i-1)
                steps += i;          // distance back
                cur = capacity;      // refill
                // Move from river to current plant i
                steps += i + 1;
            } else {
                // Move from previous plant (or river for i=0) to plant i
                steps += 1;
            }
            cur -= plants[i];
        }
        return steps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} plants
 * @param {number} capacity
 * @return {number}
 */
var wateringPlants = function(plants, capacity) {
    let steps = 0;
    let water = capacity;
    let pos = -1; // start at river
    
    for (let i = 0; i < plants.length; i++) {
        const need = plants[i];
        if (water >= need) {
            // move directly to plant i
            steps += i - pos;
            water -= need;
            pos = i;
        } else {
            // go back to river, refill, then come to plant i
            steps += pos + 1;          // return to river
            water = capacity;
            steps += i + 1;            // go from river to plant i
            water -= need;
            pos = i;
        }
    }
    
    return steps;
};
```

## Typescript

```typescript
function wateringPlants(plants: number[], capacity: number): number {
    let steps = 0;
    let water = capacity;
    let position = -1; // start at the river

    for (let i = 0; i < plants.length; i++) {
        const need = plants[i];
        if (water < need) {
            // go back to river to refill
            steps += position + 1; // distance from current position to -1
            water = capacity;
            position = -1;
        }
        // move from current position to plant i
        steps += i - position;
        position = i;
        water -= need;
    }

    return steps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $plants
     * @param Integer $capacity
     * @return Integer
     */
    function wateringPlants($plants, $capacity) {
        $steps = 0;
        $water = $capacity;
        $pos = -1; // start at the river

        foreach ($plants as $i => $need) {
            if ($water >= $need) {
                // move directly to this plant
                $steps += $i - $pos;
                $water -= $need;
                $pos = $i;
            } else {
                // go back to the river, refill, then come again
                $steps += $pos + 1;      // distance from current position to river (-1)
                $water = $capacity;     // refill
                $steps += $i + 1;        // distance from river to plant i
                $water -= $need;
                $pos = $i;
            }
        }

        return $steps;
    }
}
```

## Swift

```swift
class Solution {
    func wateringPlants(_ plants: [Int], _ capacity: Int) -> Int {
        var water = capacity
        var steps = 0
        var pos = -1
        
        for i in 0..<plants.count {
            if water < plants[i] {
                steps += (pos + 1)
                water = capacity
                pos = -1
            }
            steps += (i - pos)
            water -= plants[i]
            pos = i
        }
        
        return steps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wateringPlants(plants: IntArray, capacity: Int): Int {
        var pos = -1
        var water = capacity
        var steps = 0
        for (i in plants.indices) {
            if (water < plants[i]) {
                steps += (pos + 1)          // return to river
                pos = -1
                water = capacity
            }
            steps += (i - pos)              // move to current plant
            pos = i
            water -= plants[i]
        }
        return steps
    }
}
```

## Dart

```dart
class Solution {
  int wateringPlants(List<int> plants, int capacity) {
    int steps = 0;
    int water = capacity;
    for (int i = 0; i < plants.length; i++) {
      if (water < plants[i]) {
        steps += i * 2 + 1;
        water = capacity - plants[i];
      } else {
        steps += 1;
        water -= plants[i];
      }
    }
    return steps;
  }
}
```

## Golang

```go
func wateringPlants(plants []int, capacity int) int {
    steps := 0
    cur := capacity
    pos := -1
    for i, need := range plants {
        if cur < need {
            // Return to river and refill
            steps += pos + 1          // back to x = -1
            cur = capacity
            steps += i + 1           // walk from river to plant i
        } else {
            steps += i - pos         // move forward from previous position
        }
        cur -= need
        pos = i
    }
    return steps
}
```

## Ruby

```ruby
def watering_plants(plants, capacity)
  steps = 0
  pos = -1
  water = capacity
  plants.each_with_index do |need, i|
    if water < need
      steps += pos + 1          # return to river from current position
      water = capacity
      steps += i + 1            # go from river to plant i
    else
      steps += i - pos          # move directly to plant i
    end
    pos = i
    water -= need
  end
  steps
end
```

## Scala

```scala
object Solution {
    def wateringPlants(plants: Array[Int], capacity: Int): Int = {
        var steps = 0
        var cur = capacity
        for (i <- plants.indices) {
            if (cur < plants(i)) {
                steps += i * 2
                cur = capacity
            }
            steps += 1
            cur -= plants(i)
        }
        steps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn watering_plants(plants: Vec<i32>, capacity: i32) -> i32 {
        let mut water = capacity;
        let mut pos: i32 = -1; // current position, start at river (-1)
        let mut steps: i32 = 0;

        for (i, &need) in plants.iter().enumerate() {
            let idx = i as i32;
            if water < need {
                // Return to river and refill
                steps += pos + 1; // distance from current position to -1
                pos = -1;
                water = capacity;
            }
            // Move from current position to the plant at idx
            steps += idx - pos;
            pos = idx;
            water -= need;
        }

        steps
    }
}
```

## Racket

```racket
(define/contract (watering-plants plants capacity)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((lst plants) (idx -1) (water capacity) (pos -1) (steps 0))
    (if (null? lst)
        steps
        (let* ((need (car lst))
               (i (+ idx 1)))
          (if (< water need)
              (let* ((back (+ pos 1))           ; distance back to river
                     (forward (+ i 1))         ; distance from river to plant i
                     (new-steps (+ steps back forward))
                     (new-water (- capacity need))) ; after refill and watering
                (loop (cdr lst) i new-water i new-steps))
              (let* ((forward (- i pos))       ; move directly to next plant
                     (new-steps (+ steps forward))
                     (new-water (- water need)))
                (loop (cdr lst) i new-water i new-steps)))))))
```

## Erlang

```erlang
-spec watering_plants(Plants :: [integer()], Capacity :: integer()) -> integer().
watering_plants(Plants, Capacity) ->
    water_loop(Plants, Capacity, -1, Capacity, 0, 0).

water_loop([], _Cap, _Pos, _Water, _Idx, Steps) ->
    Steps;
water_loop([Need | Rest], Cap, Pos, Water, Idx, Steps) ->
    if
        Water >= Need ->
            NewSteps = Steps + (Idx - Pos),
            water_loop(Rest, Cap, Idx, Water - Need, Idx + 1, NewSteps);
        true ->
            BackSteps = Pos + 1,
            ForwardSteps = Idx + 1,
            TotalSteps = Steps + BackSteps + ForwardSteps,
            water_loop(Rest, Cap, Idx, Cap - Need, Idx + 1, TotalSteps)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec watering_plants(plants :: [integer], capacity :: integer) :: integer
  def watering_plants(plants, capacity) do
    {steps, _, _} =
      Enum.reduce(Enum.with_index(plants), {0, -1, capacity}, fn {need, i},
          {steps_acc, prev_pos, cur_water} ->
        if cur_water >= need do
          steps_new = steps_acc + (i - prev_pos)
          {steps_new, i, cur_water - need}
        else
          steps_new = steps_acc + (prev_pos + 1) + (i + 1)
          {steps_new, i, capacity - need}
        end
      end)

    steps
  end
end
```
