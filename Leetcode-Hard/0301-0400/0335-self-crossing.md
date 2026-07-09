# 0335. Self Crossing

## Cpp

```cpp
class Solution {
public:
    bool isSelfCrossing(vector<int>& distance) {
        int n = distance.size();
        for (int i = 3; i < n; ++i) {
            // Case 1: current line crosses the line three steps ahead of it
            if (distance[i] >= distance[i-2] && distance[i-1] <= distance[i-3])
                return true;
            // Case 2: current line meets the line four steps ahead of it
            if (i >= 4) {
                if (distance[i-1] == distance[i-3] &&
                    distance[i] + distance[i-4] >= distance[i-2])
                    return true;
            }
            // Case 3: complex crossing with five steps ahead
            if (i >= 5) {
                if (distance[i-2] > distance[i-4] &&
                    distance[i] >= distance[i-2] - distance[i-4] &&
                    distance[i-1] >= distance[i-3] - distance[i-5] &&
                    distance[i-1] <= distance[i-3] &&
                    distance[i-3] > distance[i-5])
                    return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isSelfCrossing(int[] distance) {
        int n = distance.length;
        for (int i = 3; i < n; i++) {
            // Case 1: current line crosses the line three steps ahead of it
            if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3]) {
                return true;
            }
            // Case 2: current line meets the line four steps ahead of it
            if (i >= 4) {
                if (distance[i - 1] == distance[i - 3] &&
                    distance[i] + distance[i - 4] >= distance[i - 2]) {
                    return true;
                }
            }
            // Case 3: current line crosses the line five steps ahead of it
            if (i >= 5) {
                if (distance[i - 2] > distance[i - 4] &&
                    distance[i] >= distance[i - 2] - distance[i - 4] &&
                    distance[i - 1] >= distance[i - 3] - distance[i - 5] &&
                    distance[i - 1] <= distance[i - 3]) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        n = len(distance)
        for i in range(n):
            # Case 1: current line crosses the line 3 steps ahead of it
            if i >= 3 and distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            # Case 2: current line meets the line 4 steps ahead of it (overlap)
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
            # Case 3: complex crossing with the line 5 steps ahead
            if i >= 5:
                if (distance[i-2] > distance[i-4] and
                    distance[i] >= distance[i-2] - distance[i-4] and
                    distance[i-1] >= distance[i-3] - distance[i-5] and
                    distance[i-1] <= distance[i-3] and
                    distance[i-3] > distance[i-5]):
                    return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        for i in range(3, n):
            # Case 1: current line crosses the line 2 steps ahead of it
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True

            # Case 2: current line meets the line 3 steps ahead of it (overlap)
            if i >= 4:
                if distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                    return True

            # Case 3: current line crosses the line 4 steps ahead of it
            if i >= 5:
                if (distance[i - 2] >= distance[i - 4] and
                    distance[i] >= distance[i - 2] - distance[i - 4] and
                    distance[i - 1] >= distance[i - 3] - distance[i - 5] and
                    distance[i - 1] <= distance[i - 3] and
                    distance[i - 3] > distance[i - 5]):
                    return True

        return False
```

## C

```c
#include <stdbool.h>

bool isSelfCrossing(int* distance, int distanceSize) {
    for (int i = 3; i < distanceSize; ++i) {
        // Case 1: current line crosses the line 3 steps ahead of it
        if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3])
            return true;

        // Case 2: current line meets the line 4 steps ahead of it
        if (i >= 4) {
            if (distance[i - 1] == distance[i - 3] &&
                distance[i] + distance[i - 4] >= distance[i - 2])
                return true;
        }

        // Case 3: current line crosses the line 5 steps ahead of it
        if (i >= 5) {
            if (distance[i - 2] >= distance[i - 4] &&
                distance[i] >= distance[i - 2] - distance[i - 4] &&
                distance[i - 1] >= distance[i - 3] - distance[i - 5] &&
                distance[i - 1] <= distance[i - 3] &&
                distance[i - 3] > distance[i - 5])
                return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsSelfCrossing(int[] distance) {
        int n = distance.Length;
        for (int i = 3; i < n; i++) {
            // Case 1: current line crosses the line three steps ahead of it
            if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3])
                return true;

            // Case 2: current line meets the line four steps ahead of it
            if (i >= 4) {
                if (distance[i - 1] == distance[i - 3] &&
                    distance[i] + distance[i - 4] >= distance[i - 2])
                    return true;
            }

            // Case 3: current line crosses the line five steps ahead of it
            if (i >= 5) {
                if (distance[i - 2] > distance[i - 4] &&
                    distance[i] >= distance[i - 2] - distance[i - 4] &&
                    distance[i - 1] >= distance[i - 3] - distance[i - 5] &&
                    distance[i - 1] <= distance[i - 3])
                    return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} distance
 * @return {boolean}
 */
var isSelfCrossing = function(distance) {
    const n = distance.length;
    for (let i = 3; i < n; i++) {
        // Case 1: current line crosses the line 3 steps ahead of it
        if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3]) {
            return true;
        }
        // Case 2: current line meets the line 4 steps ahead of it
        if (
            i >= 4 &&
            distance[i - 1] === distance[i - 3] &&
            distance[i] + distance[i - 4] >= distance[i - 2]
        ) {
            return true;
        }
        // Case 3: current line crosses the line 5 steps ahead of it
        if (
            i >= 5 &&
            distance[i - 2] >= distance[i - 4] &&
            distance[i] >= distance[i - 2] - distance[i - 4] &&
            distance[i - 1] >= distance[i - 3] - distance[i - 5] &&
            distance[i - 1] <= distance[i - 3] &&
            distance[i - 3] > distance[i - 5]
        ) {
            return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function isSelfCrossing(distance: number[]): boolean {
    const n = distance.length;
    for (let i = 3; i < n; i++) {
        // Case 1: current line crosses the line 3 steps ahead of it
        if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3]) {
            return true;
        }
        // Case 2: current line meets the line 4 steps ahead of it
        if (
            i >= 4 &&
            distance[i - 1] === distance[i - 3] &&
            distance[i] + distance[i - 4] >= distance[i - 2]
        ) {
            return true;
        }
        // Case 3: current line crosses the line 5 steps ahead of it
        if (
            i >= 5 &&
            distance[i - 2] > distance[i - 4] &&
            distance[i] >= distance[i - 2] - distance[i - 4] &&
            distance[i - 1] >= distance[i - 3] - distance[i - 5] &&
            distance[i - 1] <= distance[i - 3] &&
            distance[i - 3] > distance[i - 5]
        ) {
            return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $distance
     * @return Boolean
     */
    function isSelfCrossing($distance) {
        $n = count($distance);
        for ($i = 3; $i < $n; $i++) {
            // Case 1: current line crosses the line 2 steps ahead of it
            if ($distance[$i] >= $distance[$i - 2] && $distance[$i - 1] <= $distance[$i - 3]) {
                return true;
            }

            // Case 2: current line meets the line 4 steps ahead of it (special case when i == 4)
            if ($i == 4) {
                if ($distance[3] == $distance[1] && $distance[4] + $distance[0] >= $distance[2]) {
                    return true;
                }
            }

            // Case 3: current line crosses the line 5 steps ahead of it
            if ($i >= 5) {
                if (
                    $distance[$i - 2] > $distance[$i - 4] &&
                    $distance[$i] + $distance[$i - 4] >= $distance[$i - 2] &&
                    $distance[$i - 1] <= $distance[$i - 3] &&
                    $distance[$i - 1] + $distance[$i - 5] >= $distance[$i - 3]
                ) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isSelfCrossing(_ distance: [Int]) -> Bool {
        let n = distance.count
        if n < 4 { return false }
        for i in 3..<n {
            // Case 1: current line crosses the line 3 steps ahead of it
            if distance[i] >= distance[i-2] && distance[i-1] <= distance[i-3] {
                return true
            }
            // Case 2: current line meets the line 4 steps ahead of it
            if i >= 4 {
                if distance[i-1] == distance[i-3] && distance[i] + distance[i-4] >= distance[i-2] {
                    return true
                }
            }
            // Case 3: current line crosses the line 5 steps ahead of it
            if i >= 5 {
                if distance[i-2] > distance[i-4] &&
                    distance[i] >= distance[i-2] - distance[i-4] &&
                    distance[i-1] >= distance[i-3] - distance[i-5] &&
                    distance[i-1] <= distance[i-3] &&
                    distance[i-3] > distance[i-5] {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isSelfCrossing(distance: IntArray): Boolean {
        val n = distance.size
        for (i in 0 until n) {
            // Case 1: current line crosses the line 3 steps ahead of it
            if (i >= 3 &&
                distance[i] >= distance[i - 2] &&
                distance[i - 1] <= distance[i - 3]
            ) return true

            // Case 2: current line meets the line 4 steps ahead of it
            if (i >= 4 &&
                distance[i - 1] == distance[i - 3] &&
                distance[i] + distance[i - 4] >= distance[i - 2]
            ) return true

            // Case 3: current line crosses the line 5 steps ahead of it
            if (i >= 5 &&
                distance[i - 2] >= distance[i - 4] &&
                distance[i] >= distance[i - 2] - distance[i - 4] &&
                distance[i - 1] <= distance[i - 3] &&
                distance[i - 1] >= distance[i - 3] - distance[i - 5]
            ) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isSelfCrossing(List<int> distance) {
    int n = distance.length;
    for (int i = 3; i < n; i++) {
      // Case 1: current line crosses the line 3 steps ahead of it
      if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3]) {
        return true;
      }
      // Case 2: current line meets the line 4 steps ahead of it
      if (i >= 4) {
        if (distance[i - 1] == distance[i - 3] &&
            distance[i] + distance[i - 4] >= distance[i - 2]) {
          return true;
        }
      }
      // Case 3: current line crosses the line 5 steps ahead of it
      if (i >= 5) {
        if (distance[i - 2] >= distance[i - 4] &&
            distance[i] >= distance[i - 2] - distance[i - 4] &&
            distance[i - 1] >= distance[i - 3] - distance[i - 5] &&
            distance[i - 1] <= distance[i - 3] &&
            distance[i - 3] > distance[i - 5]) {
          return true;
        }
      }
    }
    return false;
  }
}
```

## Golang

```go
func isSelfCrossing(distance []int) bool {
	n := len(distance)
	if n < 4 {
		return false
	}
	for i := 3; i < n; i++ {
		// Case 1: current line crosses the line 3 steps ahead of it
		if distance[i] >= distance[i-2] && distance[i-1] <= distance[i-3] {
			return true
		}
		// Case 2: current line meets the line 4 steps ahead of it (special case)
		if i == 4 {
			if distance[3] == distance[1] && distance[4]+distance[0] >= distance[2] {
				return true
			}
		} else if i > 4 {
			// Generalized case for i >=5 where the current line crosses the line 5 steps ahead of it
			if distance[i-1] == distance[i-3] && distance[i]+distance[i-4] >= distance[i-2] {
				return true
			}
			// Case 3: complex crossing
			if distance[i-2] > distance[i-4] &&
				distance[i] >= distance[i-2]-distance[i-4] &&
				distance[i-1] >= distance[i-3]-distance[i-5] &&
				distance[i-1] <= distance[i-3] &&
				distance[i-3] > distance[i-5] {
				return true
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def is_self_crossing(distance)
  n = distance.length
  (3...n).each do |i|
    # Case 1: current line crosses the line 3 steps ahead of it
    if distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3]
      return true
    end

    # Case 2: current line meets the line 4 steps ahead of it
    if i >= 4
      if distance[i - 1] == distance[i - 3] && distance[i] + distance[i - 4] >= distance[i - 2]
        return true
      end
    end

    # Case 3: current line crosses the line 5 steps ahead of it
    if i >= 5
      if distance[i - 2] >= distance[i - 4] &&
         distance[i] >= distance[i - 2] - distance[i - 4] &&
         distance[i - 1] >= distance[i - 3] - distance[i - 5] &&
         distance[i - 1] <= distance[i - 3] &&
         distance[i - 3] > distance[i - 5]
        return true
      end
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def isSelfCrossing(distance: Array[Int]): Boolean = {
        val n = distance.length
        for (i <- 0 until n) {
            if (i >= 3 && distance(i) >= distance(i - 2) && distance(i - 1) <= distance(i - 3)) return true
            if (i >= 4 && distance(i - 1) == distance(i - 3) && distance(i) + distance(i - 4) >= distance(i - 2)) return true
            if (i >= 5 &&
                distance(i - 2) >= distance(i - 4) &&
                distance(i) >= distance(i - 2) - distance(i - 4) &&
                distance(i - 1) >= distance(i - 3) - distance(i - 5) &&
                distance(i - 1) <= distance(i - 3) &&
                distance(i - 3) > distance(i - 5)) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_self_crossing(distance: Vec<i32>) -> bool {
        let n = distance.len();
        for i in 3..n {
            // Case 1: current line crosses the line 3 steps ahead of it
            if distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3] {
                return true;
            }
            // Case 2: current line meets the line 4 steps ahead of it
            if i >= 4 {
                if distance[i - 1] == distance[i - 3]
                    && distance[i] + distance[i - 4] >= distance[i - 2]
                {
                    return true;
                }
            }
            // Case 3: current line crosses the line 5 steps ahead of it
            if i >= 5 {
                if distance[i - 2] > distance[i - 4]
                    && distance[i] >= distance[i - 2] - distance[i - 4]
                    && distance[i - 1] >= distance[i - 3] - distance[i - 5]
                    && distance[i - 1] <= distance[i - 3]
                    && distance[i - 3] > distance[i - 5]
                {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (is-self-crossing distance)
  (-> (listof exact-integer?) boolean?)
  (let* ((v (list->vector distance))
         (n (vector-length v)))
    (for/or ([i (in-range 3 n)])
      (let* ((xi  (vector-ref v i))
             (xi1 (vector-ref v (- i 1)))
             (xi2 (vector-ref v (- i 2)))
             (xi3 (vector-ref v (- i 3))))
        (or
         ;; case 1: simple crossing
         (and (>= xi xi2) (<= xi1 xi3))
         ;; case 2: overlapping with the line 4 steps back
         (and (>= i 4)
              (= xi1 (vector-ref v (- i 3)))
              (>= (+ xi (vector-ref v (- i 4))) xi2))
         ;; case 3: complex crossing involving the line 5 steps back
         (and (>= i 5)
              (let* ((xi4 (vector-ref v (- i 4)))
                     (xi5 (vector-ref v (- i 5))))
                (and (>= xi2 xi4)
                     (>= (+ xi xi4) xi2)
                     (<= xi1 xi3)
                     (>= (+ xi1 xi5) xi3)))))))))
```

## Erlang

```erlang
-spec is_self_crossing(Distance :: [integer()]) -> boolean().
is_self_crossing(Distance) ->
    loop(Distance, []).

loop([], _) ->
    false;
loop([D|Rest], Prev) ->
    case check(D, Prev) of
        true -> true;
        false -> loop(Rest, [D|Prev])
    end.

check(_D, []) ->
    false;
check(_D, [_]) ->
    false;
check(_D, [_ , _]) ->
    false;
check(D, [X1,X2,X3|_]) when D >= X2, X1 =< X3 ->
    true;
check(D, [X1,X2,X3,X4|_]) when X1 =:= X3, D + X4 >= X2 ->
    true;
check(D, [X1,X2,X3,X4,X5|_]) when
        X2 >= X4,
        D >= X2 - X4,
        X1 >= X3 - X5,
        X1 =< X3,
        X2 > X4 ->
    true;
check(_, _) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_self_crossing(distance :: [integer]) :: boolean
  def is_self_crossing(distance) do
    process(distance, -1, [])
  end

  defp process([], _idx, _recent), do: false

  defp process([d | rest], idx, recent) do
    new_idx = idx + 1
    new_recent = recent ++ [d]
    new_recent = if length(new_recent) > 6, do: tl(new_recent), else: new_recent

    cross =
      cond do
        new_idx >= 3 and case1?(new_recent) -> true
        new_idx >= 4 and case2?(new_recent) -> true
        new_idx >= 5 and case3?(new_recent) -> true
        true -> false
      end

    if cross, do: true, else: process(rest, new_idx, new_recent)
  end

  defp case1?(recent) do
    rev = Enum.reverse(recent)
    [d_i, d_i_1, d_i_2, d_i_3 | _] = rev
    d_i >= d_i_2 and d_i_1 <= d_i_3
  end

  defp case2?(recent) do
    rev = Enum.reverse(recent)
    [d_i, d_i_1, d_i_2, d_i_3, d_i_4 | _] = rev
    d_i_1 == d_i_3 and d_i + d_i_4 >= d_i_2
  end

  defp case3?(recent) do
    rev = Enum.reverse(recent)
    [d_i, d_i_1, d_i_2, d_i_3, d_i_4, d_i_5 | _] = rev
    d_i_2 >= d_i_4 and d_i + d_i_4 >= d_i_2 and d_i_1 <= d_i_3 and d_i_1 + d_i_5 >= d_i_3
  end
end
```
