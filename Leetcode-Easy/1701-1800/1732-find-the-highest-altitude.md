# 1732. Find the Highest Altitude

## Cpp

```cpp
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int cur = 0;
        int best = 0;
        for (int g : gain) {
            cur += g;
            if (cur > best) best = cur;
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int largestAltitude(int[] gain) {
        int current = 0;
        int highest = 0;
        for (int g : gain) {
            current += g;
            if (current > highest) {
                highest = current;
            }
        }
        return highest;
    }
}
```

## Python

```python
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current = 0
        max_altitude = 0
        for g in gain:
            current += g
            if current > max_altitude:
                max_altitude = current
        return max_altitude
```

## Python3

```python
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0
        for g in gain:
            current += g
            if current > highest:
                highest = current
        return highest
```

## C

```c
int largestAltitude(int* gain, int gainSize) {
    int current = 0;
    int highest = 0;
    for (int i = 0; i < gainSize; ++i) {
        current += gain[i];
        if (current > highest) {
            highest = current;
        }
    }
    return highest;
}
```

## Csharp

```csharp
public class Solution {
    public int LargestAltitude(int[] gain) {
        int current = 0;
        int highest = 0;
        foreach (int g in gain) {
            current += g;
            if (current > highest) highest = current;
        }
        return highest;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let curr = 0;
    let highest = 0;
    for (const g of gain) {
        curr += g;
        if (curr > highest) highest = curr;
    }
    return highest;
};
```

## Typescript

```typescript
function largestAltitude(gain: number[]): number {
    let current = 0;
    let highest = 0;
    for (const delta of gain) {
        current += delta;
        if (current > highest) highest = current;
    }
    return highest;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $gain
     * @return Integer
     */
    function largestAltitude($gain) {
        $current = 0;
        $max = 0;
        foreach ($gain as $g) {
            $current += $g;
            if ($current > $max) {
                $max = $current;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func largestAltitude(_ gain: [Int]) -> Int {
        var current = 0
        var highest = 0
        for g in gain {
            current += g
            if current > highest {
                highest = current
            }
        }
        return highest
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var current = 0
        var highest = 0
        for (g in gain) {
            current += g
            if (current > highest) highest = current
        }
        return highest
    }
}
```

## Dart

```dart
class Solution {
  int largestAltitude(List<int> gain) {
    int current = 0;
    int highest = 0;
    for (int g in gain) {
      current += g;
      if (current > highest) highest = current;
    }
    return highest;
  }
}
```

## Golang

```go
func largestAltitude(gain []int) int {
    current, highest := 0, 0
    for _, v := range gain {
        current += v
        if current > highest {
            highest = current
        }
    }
    return highest
}
```

## Ruby

```ruby
# @param {Integer[]} gain
# @return {Integer}
def largest_altitude(gain)
  current = 0
  highest = 0
  gain.each do |g|
    current += g
    highest = current if current > highest
  end
  highest
end
```

## Scala

```scala
object Solution {
    def largestAltitude(gain: Array[Int]): Int = {
        var current = 0
        var highest = 0
        for (g <- gain) {
            current += g
            if (current > highest) highest = current
        }
        highest
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut current = 0;
        let mut max_alt = 0;
        for g in gain {
            current += g;
            if current > max_alt {
                max_alt = current;
            }
        }
        max_alt
    }
}
```

## Racket

```racket
(define/contract (largest-altitude gain)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst gain) (cur 0) (mx 0))
    (if (null? lst)
        mx
        (let* ((new-cur (+ cur (car lst)))
               (new-mx (max mx new-cur)))
          (loop (cdr lst) new-cur new-mx)))))
```

## Erlang

```erlang
-spec largest_altitude(Gain :: [integer()]) -> integer().
largest_altitude(Gain) ->
    {_, MaxAltitude} = lists:foldl(
        fun(G, {Curr, Max}) ->
            NewCurr = Curr + G,
            NewMax = if NewCurr > Max -> NewCurr; true -> Max end,
            {NewCurr, NewMax}
        end,
        {0, 0},
        Gain
    ),
    MaxAltitude.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_altitude(gain :: [integer]) :: integer
  def largest_altitude(gain) do
    {_current, max_altitude} =
      Enum.reduce(gain, {0, 0}, fn g, {curr, max} ->
        new_curr = curr + g
        new_max = if new_curr > max, do: new_curr, else: max
        {new_curr, new_max}
      end)

    max_altitude
  end
end
```
