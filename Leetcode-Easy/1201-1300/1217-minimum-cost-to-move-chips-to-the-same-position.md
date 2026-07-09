# 1217. Minimum Cost to Move Chips to The Same Position

## Cpp

```cpp
class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int even = 0, odd = 0;
        for (int p : position) {
            if (p % 2 == 0) ++even;
            else ++odd;
        }
        return min(even, odd);
    }
};
```

## Java

```java
class Solution {
    public int minCostToMoveChips(int[] position) {
        int even = 0, odd = 0;
        for (int p : position) {
            if ((p & 1) == 0) {
                even++;
            } else {
                odd++;
            }
        }
        return Math.min(even, odd);
    }
}
```

## Python

```python
class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        even = odd = 0
        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
```

## Python3

```python
from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(p % 2 for p in position)
        even = len(position) - odd
        return min(odd, even)
```

## C

```c
int minCostToMoveChips(int* position, int positionSize) {
    int odd = 0, even = 0;
    for (int i = 0; i < positionSize; ++i) {
        if (position[i] & 1)
            ++odd;
        else
            ++even;
    }
    return odd < even ? odd : even;
}
```

## Csharp

```csharp
public class Solution {
    public int MinCostToMoveChips(int[] position) {
        int odd = 0, even = 0;
        foreach (int p in position) {
            if ((p & 1) == 0) even++;
            else odd++;
        }
        return Math.Min(odd, even);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function(position) {
    let even = 0, odd = 0;
    for (const p of position) {
        if (p % 2 === 0) even++;
        else odd++;
    }
    return Math.min(even, odd);
};
```

## Typescript

```typescript
function minCostToMoveChips(position: number[]): number {
    let odd = 0, even = 0;
    for (const p of position) {
        if (p % 2 === 0) {
            even++;
        } else {
            odd++;
        }
    }
    return Math.min(odd, even);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $position
     * @return Integer
     */
    function minCostToMoveChips($position) {
        $odd = 0;
        $even = 0;
        foreach ($position as $p) {
            if ($p % 2 == 0) {
                $even++;
            } else {
                $odd++;
            }
        }
        return min($odd, $even);
    }
}
```

## Swift

```swift
class Solution {
    func minCostToMoveChips(_ position: [Int]) -> Int {
        var evenCount = 0
        var oddCount = 0
        for pos in position {
            if pos % 2 == 0 {
                evenCount += 1
            } else {
                oddCount += 1
            }
        }
        return min(evenCount, oddCount)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCostToMoveChips(position: IntArray): Int {
        var evenCount = 0
        var oddCount = 0
        for (p in position) {
            if ((p and 1) == 0) {
                evenCount++
            } else {
                oddCount++
            }
        }
        return minOf(evenCount, oddCount)
    }
}
```

## Dart

```dart
class Solution {
  int minCostToMoveChips(List<int> position) {
    int odd = 0, even = 0;
    for (var p in position) {
      if (p % 2 == 0) {
        even++;
      } else {
        odd++;
      }
    }
    return odd < even ? odd : even;
  }
}
```

## Golang

```go
func minCostToMoveChips(position []int) int {
    even, odd := 0, 0
    for _, p := range position {
        if p%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    if even < odd {
        return even
    }
    return odd
}
```

## Ruby

```ruby
def min_cost_to_move_chips(position)
  odds = 0
  evens = 0
  position.each do |p|
    if p.even?
      evens += 1
    else
      odds += 1
    end
  end
  [odds, evens].min
end
```

## Scala

```scala
object Solution {
    def minCostToMoveChips(position: Array[Int]): Int = {
        var even = 0
        var odd = 0
        for (p <- position) {
            if ((p & 1) == 0) even += 1 else odd += 1
        }
        Math.min(even, odd)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost_to_move_chips(position: Vec<i32>) -> i32 {
        let mut even = 0;
        let mut odd = 0;
        for p in position {
            if p % 2 == 0 {
                even += 1;
            } else {
                odd += 1;
            }
        }
        std::cmp::min(even, odd) as i32
    }
}
```

## Racket

```racket
(define/contract (min-cost-to-move-chips position)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((odd-count (for/sum ([p position]) (if (odd? p) 1 0)))
         (even-count (- (length position) odd-count)))
    (min odd-count even-count)))
```

## Erlang

```erlang
-module(solution).
-export([min_cost_to_move_chips/1]).

-spec min_cost_to_move_chips(Position :: [integer()]) -> integer().
min_cost_to_move_chips(Position) ->
    {Odd, Even} = lists:foldl(
        fun(X, {O, E}) ->
            case X rem 2 of
                0 -> {O, E + 1};
                _ -> {O + 1, E}
            end
        end,
        {0, 0},
        Position),
    if Odd < Even -> Odd; true -> Even end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost_to_move_chips(position :: [integer]) :: integer
  def min_cost_to_move_chips(position) do
    {odd, even} =
      Enum.reduce(position, {0, 0}, fn x, {o, e} ->
        if rem(x, 2) == 1, do: {o + 1, e}, else: {o, e + 1}
      end)

    min(odd, even)
  end
end
```
