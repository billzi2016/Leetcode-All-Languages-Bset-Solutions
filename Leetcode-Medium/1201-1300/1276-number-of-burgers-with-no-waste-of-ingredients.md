# 1276. Number of Burgers with No Waste of Ingredients

## Cpp

```cpp
class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        // Total tomatoes must be even
        if (tomatoSlices % 2 != 0) return {};
        // Derive number of jumbo burgers X
        int x = (tomatoSlices - 2 * cheeseSlices);
        if (x < 0 || x % 2 != 0) return {};
        x /= 2; // X = (T - 2C)/2
        int y = cheeseSlices - x;
        if (y < 0) return {};
        // Verify (optional)
        if (4 * x + 2 * y != tomatoSlices) return {};
        return {x, y};
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        // The total number of tomato slices must be even.
        if (tomatoSlices % 2 != 0) {
            return new java.util.ArrayList<>();
        }
        // Feasibility bounds: 4 * cheeseSlices >= tomatoSlices and 2 * cheeseSlices <= tomatoSlices
        if ((long)4 * cheeseSlices < tomatoSlices || (long)2 * cheeseSlices > tomatoSlices) {
            return new java.util.ArrayList<>();
        }
        int jumbo = tomatoSlices / 2 - cheeseSlices;          // X = (T/2) - C
        int small = cheeseSlices - jumbo;                    // Y = C - X
        java.util.List<Integer> result = new java.util.ArrayList<>(2);
        result.add(jumbo);
        result.add(small);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        # Tomato slices must be even and within feasible range.
        if tomatoSlices % 2 != 0:
            return []
        if not (2 * cheeseSlices <= tomatoSlices <= 4 * cheeseSlices):
            return []
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo
        if jumbo < 0 or small < 0:
            return []
        return [jumbo, small]
```

## Python3

```python
from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0:
            return []
        jumbo = tomatoSlices // 2 - cheeseSlices
        small = cheeseSlices - jumbo
        if jumbo < 0 or small < 0:
            return []
        return [jumbo, small]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numOfBurgers(int tomatoSlices, int cheeseSlices, int* returnSize) {
    *returnSize = 0;
    if (tomatoSlices % 2 != 0) return NULL;                     // T must be even
    if (tomatoSlices < 2 * cheeseSlices) return NULL;           // not enough tomatoes
    if (tomatoSlices > 4 * cheeseSlices) return NULL;           // too many tomatoes

    int jumbo = (tomatoSlices - 2 * cheeseSlices) / 2;
    int small = cheeseSlices - jumbo;

    if (jumbo < 0 || small < 0) return NULL;                    // safety check

    int* ans = (int*)malloc(2 * sizeof(int));
    if (!ans) return NULL;                                      // allocation failure guard
    ans[0] = jumbo;
    ans[1] = small;
    *returnSize = 2;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> NumOfBurgers(int tomatoSlices, int cheeseSlices) {
        // The total number of tomato slices must be even.
        if (tomatoSlices % 2 != 0) return new List<int>();
        
        // Solve the system:
        // 4X + 2Y = tomatoSlices
        // X + Y   = cheeseSlices
        // => X = (tomatoSlices - 2 * cheeseSlices) / 2
        int x = (tomatoSlices - 2 * cheeseSlices) / 2;
        int y = cheeseSlices - x;
        
        if (x < 0 || y < 0) return new List<int>();
        // Additional check to ensure equations hold (protect against overflow issues)
        if (4 * x + 2 * y != tomatoSlices) return new List<int>();
        if (x + y != cheeseSlices) return new List<int>();
        
        return new List<int> { x, y };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} tomatoSlices
 * @param {number} cheeseSlices
 * @return {number[]}
 */
var numOfBurgers = function(tomatoSlices, cheeseSlices) {
    // Total tomato slices must be even (both burger types use an even number)
    if (tomatoSlices % 2 !== 0) return [];
    
    const jumbo = (tomatoSlices - 2 * cheeseSlices) / 2;
    const small = cheeseSlices - jumbo;
    
    if (jumbo < 0 || small < 0) return [];
    return [jumbo, small];
};
```

## Typescript

```typescript
function numOfBurgers(tomatoSlices: number, cheeseSlices: number): number[] {
    if (tomatoSlices % 2 !== 0) return [];
    const jumbo = (tomatoSlices - 2 * cheeseSlices) / 2;
    const small = cheeseSlices - jumbo;
    if (jumbo < 0 || small < 0) return [];
    return [jumbo, small];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $tomatoSlices
     * @param Integer $cheeseSlices
     * @return Integer[]
     */
    function numOfBurgers($tomatoSlices, $cheeseSlices) {
        // Tomato count must be even for any solution
        if ($tomatoSlices % 2 !== 0) {
            return [];
        }
        // Compute candidate jumbo burgers (X)
        $diff = $tomatoSlices - 2 * $cheeseSlices;
        // diff must be non‑negative and even
        if ($diff < 0 || $diff % 2 !== 0) {
            return [];
        }
        $jumbo = intdiv($diff, 2);
        $small = $cheeseSlices - $jumbo;
        // Both counts must be non‑negative
        if ($small < 0) {
            return [];
        }
        return [$jumbo, $small];
    }
}
```

## Swift

```swift
class Solution {
    func numOfBurgers(_ tomatoSlices: Int, _ cheeseSlices: Int) -> [Int] {
        // Tomato slices must be even for any solution
        if tomatoSlices % 2 != 0 { return [] }
        
        let xNumerator = tomatoSlices - 2 * cheeseSlices
        // X must be non‑negative and integer
        if xNumerator < 0 || xNumerator % 2 != 0 { return [] }
        
        let jumbo = xNumerator / 2
        let small = cheeseSlices - jumbo
        
        if jumbo < 0 || small < 0 { return [] }
        return [jumbo, small]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List<Int> {
        val diff = tomatoSlices - 2 * cheeseSlices
        if (diff < 0 || diff % 2 != 0) return emptyList()
        val jumbo = diff / 2
        val small = cheeseSlices - jumbo
        if (small < 0) return emptyList()
        return listOf(jumbo, small)
    }
}
```

## Dart

```dart
class Solution {
  List<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
    if (tomatoSlices % 2 != 0) return [];
    int jumbo = tomatoSlices ~/ 2 - cheeseSlices;
    int small = cheeseSlices - jumbo;
    if (jumbo < 0 || small < 0) return [];
    return [jumbo, small];
  }
}
```

## Golang

```go
func numOfBurgers(tomatoSlices int, cheeseSlices int) []int {
	if tomatoSlices%2 != 0 {
		return []int{}
	}
	x := (tomatoSlices - 2*cheeseSlices) / 2
	y := cheeseSlices - x
	if x < 0 || y < 0 {
		return []int{}
	}
	return []int{x, y}
}
```

## Ruby

```ruby
def num_of_burgers(tomato_slices, cheese_slices)
  return [] if tomato_slices.odd?
  x = (tomato_slices - 2 * cheese_slices) / 2
  y = cheese_slices - x
  return [] if x < 0 || y < 0
  [x, y]
end
```

## Scala

```scala
object Solution {
    def numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List[Int] = {
        if (tomatoSlices % 2 != 0) return Nil
        val minTomato = 2 * cheeseSlices
        val maxTomato = 4 * cheeseSlices
        if (tomatoSlices < minTomato || tomatoSlices > maxTomato) return Nil
        val jumbo = (tomatoSlices - 2 * cheeseSlices) / 2
        val small = cheeseSlices - jumbo
        if (jumbo >= 0 && small >= 0) List(jumbo, small) else Nil
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_burgers(tomato_slices: i32, cheese_slices: i32) -> Vec<i32> {
        // tomato must be even and within [2*cheese, 4*cheese]
        if tomato_slices % 2 != 0 {
            return vec![];
        }
        let min_t = 2 * cheese_slices;
        let max_t = 4 * cheese_slices;
        if tomato_slices < min_t || tomato_slices > max_t {
            return vec![];
        }
        // Solve for jumbo (X) and small (Y)
        let x = (tomato_slices - 2 * cheese_slices) / 2; // number of jumbo burgers
        let y = cheese_slices - x;                       // number of small burgers
        if x < 0 || y < 0 {
            return vec![];
        }
        vec![x, y]
    }
}
```

## Racket

```racket
(define/contract (num-of-burgers tomatoSlices cheeseSlices)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (if (and (even? tomatoSlices)
           (>= tomatoSlices (* 2 cheeseSlices))
           (<= tomatoSlices (* 4 cheeseSlices)))
      (let* ((x (/ (- tomatoSlices (* 2 cheeseSlices)) 2))
             (y (- cheeseSlices x)))
        (list x y))
      '()))
```

## Erlang

```erlang
-module(solution).
-export([num_of_burgers/2]).

-spec num_of_burgers(integer(), integer()) -> [integer()].
num_of_burgers(TomatoSlices, CheeseSlices) ->
    if
        TomatoSlices rem 2 =/= 0 ->
            [];
        true ->
            X = (TomatoSlices - 2 * CheeseSlices) div 2,
            Y = CheeseSlices - X,
            case X >= 0 andalso Y >= 0 of
                true -> [X, Y];
                false -> []
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_burgers(tomato_slices :: integer, cheese_slices :: integer) :: [integer]
  def num_of_burgers(tomato_slices, cheese_slices) do
    diff = tomato_slices - 2 * cheese_slices

    cond do
      diff < 0 -> []
      rem(diff, 2) != 0 -> []
      true ->
        jumbo = div(diff, 2)
        small = cheese_slices - jumbo

        if small < 0, do: [], else: [jumbo, small]
    end
  end
end
```
