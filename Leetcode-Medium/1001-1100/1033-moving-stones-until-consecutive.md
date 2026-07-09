# 1033. Moving Stones Until Consecutive

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        vector<int> v = {a, b, c};
        sort(v.begin(), v.end());
        int x = v[0], y = v[1], z = v[2];
        
        int minMoves;
        if (y - x == 1 && z - y == 1) {
            minMoves = 0;
        } else if (y - x == 2 || z - y == 2) {
            minMoves = 1;
        } else {
            minMoves = 2;
        }
        
        int maxMoves = (z - x) - 2;
        return {minMoves, maxMoves};
    }
};
```

## Java

```java
class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        int[] pos = new int[]{a, b, c};
        java.util.Arrays.sort(pos);
        int x = pos[0], y = pos[1], z = pos[2];
        
        // minimum moves
        int min;
        if (y - x == 1 && z - y == 1) {
            min = 0;
        } else if (y - x == 2 || z - y == 2) {
            min = 1;
        } else {
            min = 2;
        }
        
        // maximum moves
        int max = (z - x) - 2;
        return new int[]{min, max};
    }
}
```

## Python

```python
class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x, y, z = sorted([a, b, c])
        # minimum moves
        if y - x == 1 and z - y == 1:
            min_moves = 0
        elif y - x == 2 or z - y == 2:
            min_moves = 1
        else:
            min_moves = 2
        # maximum moves
        max_moves = (z - x) - 2
        return [min_moves, max_moves]
```

## Python3

```python
from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        # Minimum moves
        if y - x == 1 and z - y == 1:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2
        # Maximum moves
        max_moves = max(z - y, y - x) - 1
        return [min_moves, max_moves]
```

## C

```c
#include <stdlib.h>

int* numMovesStones(int a, int b, int c, int* returnSize) {
    int pos[3] = {a, b, c};
    // Simple sort for three elements
    for (int i = 0; i < 2; ++i) {
        for (int j = i + 1; j < 3; ++j) {
            if (pos[i] > pos[j]) {
                int tmp = pos[i];
                pos[i] = pos[j];
                pos[j] = tmp;
            }
        }
    }
    int x = pos[0], y = pos[1], z = pos[2];

    int minMoves;
    if (y - x == 1 && z - y == 1) {
        minMoves = 0;
    } else if ((y - x <= 2) || (z - y <= 2)) {
        minMoves = 1;
    } else {
        minMoves = 2;
    }

    int maxMoves = (z - x) - 2;

    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = minMoves;
    result[1] = maxMoves;
    *returnSize = 2;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] NumMovesStones(int a, int b, int c) {
        int[] pos = new int[] { a, b, c };
        Array.Sort(pos);
        int x = pos[0], y = pos[1], z = pos[2];

        // If already consecutive
        if (y - x == 1 && z - y == 1) {
            return new int[] { 0, 0 };
        }

        int minMoves;
        // One move is enough when there is a gap of exactly two
        if (y - x == 2 || z - y == 2) {
            minMoves = 1;
        } else {
            minMoves = 2;
        }

        // Maximum moves: each move reduces the total span by at least 1
        int maxMoves = (z - x) - 2;

        return new int[] { minMoves, maxMoves };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number[]}
 */
var numMovesStones = function(a, b, c) {
    const arr = [a, b, c].sort((x, y) => x - y);
    const x = arr[0], y = arr[1], z = arr[2];
    
    // maximum moves
    const maxMoves = (z - x) - 2;
    
    // minimum moves
    let minMoves;
    if (y - x === 1 && z - y === 1) {
        minMoves = 0; // already consecutive
    } else if (y - x === 2 || z - y === 2) {
        minMoves = 1; // one gap of size 2 allows a single move
    } else {
        minMoves = 2;
    }
    
    return [minMoves, maxMoves];
};
```

## Typescript

```typescript
function numMovesStones(a: number, b: number, c: number): number[] {
    const pos = [a, b, c].sort((x, y) => x - y);
    const x = pos[0], y = pos[1], z = pos[2];
    
    let minMoves: number;
    if (y - x === 1 && z - y === 1) {
        minMoves = 0;
    } else if (y - x === 2 || z - y === 2) {
        minMoves = 1;
    } else {
        minMoves = 2;
    }
    
    const maxMoves = (z - x) - 2;
    return [minMoves, maxMoves];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer[]
     */
    function numMovesStones($a, $b, $c) {
        $stones = [$a, $b, $c];
        sort($stones);
        list($x, $y, $z) = $stones;

        // maximum moves: reduce the span to 2 (consecutive)
        $max = $z - $x - 2;

        // minimum moves
        if ($y - $x == 1 && $z - $y == 1) {
            $min = 0;
        } elseif ($y - $x == 2 || $z - $y == 2) {
            $min = 1;
        } else {
            $min = 2;
        }

        return [$min, $max];
    }
}
```

## Swift

```swift
class Solution {
    func numMovesStones(_ a: Int, _ b: Int, _ c: Int) -> [Int] {
        let stones = [a, b, c].sorted()
        let x = stones[0], y = stones[1], z = stones[2]
        
        // Maximum moves: reduce the span to 2 (consecutive)
        let maxMoves = (z - x) - 2
        
        // Minimum moves
        var minMoves: Int
        if y - x == 1 && z - y == 1 {
            minMoves = 0
        } else if y - x == 2 || z - y == 2 {
            minMoves = 1
        } else {
            minMoves = 2
        }
        
        return [minMoves, maxMoves]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numMovesStones(a: Int, b: Int, c: Int): IntArray {
        val stones = intArrayOf(a, b, c)
        stones.sort()
        val x = stones[0]
        val y = stones[1]
        val z = stones[2]

        val minMoves = when {
            y - x == 1 && z - y == 1 -> 0
            y - x == 2 || z - y == 2 -> 1
            else -> 2
        }

        val maxMoves = kotlin.math.max(z - y, y - x) - 1

        return intArrayOf(minMoves, maxMoves)
    }
}
```

## Dart

```dart
class Solution {
  List<int> numMovesStones(int a, int b, int c) {
    var positions = [a, b, c];
    positions.sort();
    int x = positions[0], y = positions[1], z = positions[2];

    int minMoves;
    if (y - x == 1 && z - y == 1) {
      minMoves = 0;
    } else if (y - x == 2 || z - y == 2) {
      minMoves = 1;
    } else {
      minMoves = 2;
    }

    int maxGap = (z - y) > (y - x) ? (z - y) : (y - x);
    int maxMoves = maxGap - 1;

    return [minMoves, maxMoves];
  }
}
```

## Golang

```go
func numMovesStones(a int, b int, c int) []int {
	// sort the positions
	x, y, z := a, b, c
	if x > y {
		x, y = y, x
	}
	if y > z {
		y, z = z, y
	}
	if x > y {
		x, y = y, x
	}

	minMoves := 2
	if y-x == 1 && z-y == 1 {
		minMoves = 0
	} else if y-x == 2 || z-y == 2 {
		minMoves = 1
	}

	maxGap := z - y
	if y-x > maxGap {
		maxGap = y - x
	}
	maxMoves := maxGap - 1

	return []int{minMoves, maxMoves}
}
```

## Ruby

```ruby
def num_moves_stones(a, b, c)
  x, y, z = [a, b, c].sort
  d1 = y - x
  d2 = z - y

  min_moves =
    if d1 == 1 && d2 == 1
      0
    elsif d1 <= 2 || d2 <= 2
      1
    else
      2
    end

  max_moves = (z - x) - 2
  [min_moves, max_moves]
end
```

## Scala

```scala
object Solution {
    def numMovesStones(a: Int, b: Int, c: Int): Array[Int] = {
        val stones = List(a, b, c).sorted
        val x = stones(0)
        val y = stones(1)
        val z = stones(2)

        val minMoves = if (y - x == 1 && z - y == 1) {
            0
        } else if (y - x == 2 || z - y == 2) {
            1
        } else {
            2
        }

        val maxMoves = math.max(z - y, y - x) - 1

        Array(minMoves, maxMoves)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_moves_stones(a: i32, b: i32, c: i32) -> Vec<i32> {
        let mut v = vec![a, b, c];
        v.sort();
        let left = v[1] - v[0];
        let right = v[2] - v[1];

        let min_moves = if left == 1 && right == 1 {
            0
        } else if left <= 2 || right <= 2 {
            1
        } else {
            2
        };

        let max_moves = std::cmp::max(left, right) - 1;
        vec![min_moves, max_moves]
    }
}
```

## Racket

```racket
(define/contract (num-moves-stones a b c)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  (let* ((sorted (sort (list a b c) <))
         (x (first sorted))
         (y (second sorted))
         (z (third sorted))
         (gap1 (- y x))
         (gap2 (- z y)))
    (define min-moves
      (cond [(and (= gap1 1) (= gap2 1)) 0]
            [(or (= gap1 2) (= gap2 2)) 1]
            [else 2]))
    (define max-moves (- (max gap1 gap2) 1))
    (list min-moves max-moves)))
```

## Erlang

```erlang
-spec num_moves_stones(A :: integer(), B :: integer(), C :: integer()) -> [integer()].
num_moves_stones(A, B, C) ->
    Sorted = lists:sort([A, B, C]),
    X = hd(Sorted),
    Y = hd(tl(Sorted)),
    Z = hd(tl(tl(Sorted))),
    Gap1 = Y - X,
    Gap2 = Z - Y,
    MinMoves =
        case {Gap1, Gap2} of
            {1, 1} -> 0;
            {2, _} -> 1;
            {_, 2} -> 1;
            {1, G} when G > 2 -> 1;
            {G, 1} when G > 2 -> 1;
            _ -> 2
        end,
    MaxMoves = (Z - X) - 2,
    [MinMoves, MaxMoves].
```

## Elixir

```elixir
defmodule Solution do
  @spec num_moves_stones(a :: integer, b :: integer, c :: integer) :: [integer]
  def num_moves_stones(a, b, c) do
    [x, y, z] = Enum.sort([a, b, c])
    gap1 = y - x
    gap2 = z - y

    min_moves =
      cond do
        gap1 == 1 and gap2 == 1 -> 0
        gap1 <= 2 or gap2 <= 2 -> 1
        true -> 2
      end

    max_moves = (z - x) - 2
    [min_moves, max_moves]
  end
end
```
