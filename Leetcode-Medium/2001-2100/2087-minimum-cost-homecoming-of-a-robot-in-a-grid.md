# 2087. Minimum Cost Homecoming of a Robot in a Grid

## Cpp

```cpp
class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        int sr = startPos[0], sc = startPos[1];
        int hr = homePos[0], hc = homePos[1];
        long long total = 0;
        if (sr < hr) {
            for (int r = sr + 1; r <= hr; ++r) total += rowCosts[r];
        } else if (sr > hr) {
            for (int r = hr; r < sr; ++r) total += rowCosts[r];
        }
        if (sc < hc) {
            for (int c = sc + 1; c <= hc; ++c) total += colCosts[c];
        } else if (sc > hc) {
            for (int c = hc; c < sc; ++c) total += colCosts[c];
        }
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    public int minCost(int[] startPos, int[] homePos, int[] rowCosts, int[] colCosts) {
        int sr = startPos[0];
        int sc = startPos[1];
        int hr = homePos[0];
        int hc = homePos[1];
        long total = 0;
        if (sr < hr) {
            for (int r = sr + 1; r <= hr; ++r) {
                total += rowCosts[r];
            }
        } else {
            for (int r = sr - 1; r >= hr; --r) {
                total += rowCosts[r];
            }
        }
        if (sc < hc) {
            for (int c = sc + 1; c <= hc; ++c) {
                total += colCosts[c];
            }
        } else {
            for (int c = sc - 1; c >= hc; --c) {
                total += colCosts[c];
            }
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        sr, sc = startPos
        hr, hc = homePos
        total = 0

        if sr < hr:
            for r in range(sr + 1, hr + 1):
                total += rowCosts[r]
        else:
            for r in range(hr, sr):
                total += rowCosts[r]

        if sc < hc:
            for c in range(sc + 1, hc + 1):
                total += colCosts[c]
        else:
            for c in range(hc, sc):
                total += colCosts[c]

        return total
```

## Python3

```python
class Solution:
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        sr, sc = startPos
        hr, hc = homePos
        total = 0

        if sr < hr:
            for r in range(sr + 1, hr + 1):
                total += rowCosts[r]
        else:
            for r in range(sr - 1, hr - 1, -1):
                total += rowCosts[r]

        if sc < hc:
            for c in range(sc + 1, hc + 1):
                total += colCosts[c]
        else:
            for c in range(sc - 1, hc - 1, -1):
                total += colCosts[c]

        return total
```

## C

```c
int minCost(int* startPos, int startPosSize, int* homePos, int homePosSize, int* rowCosts, int rowCostsSize, int* colCosts, int colCostsSize) {
    int sr = startPos[0];
    int sc = startPos[1];
    int hr = homePos[0];
    int hc = homePos[1];
    long long total = 0;
    
    if (sr < hr) {
        for (int r = sr + 1; r <= hr; ++r) {
            total += rowCosts[r];
        }
    } else if (sr > hr) {
        for (int r = hr; r < sr; ++r) {
            total += rowCosts[r];
        }
    }
    
    if (sc < hc) {
        for (int c = sc + 1; c <= hc; ++c) {
            total += colCosts[c];
        }
    } else if (sc > hc) {
        for (int c = hc; c < sc; ++c) {
            total += colCosts[c];
        }
    }
    
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int MinCost(int[] startPos, int[] homePos, int[] rowCosts, int[] colCosts) {
        long total = 0;
        int sr = startPos[0], sc = startPos[1];
        int hr = homePos[0], hc = homePos[1];

        if (sr < hr) {
            for (int r = sr + 1; r <= hr; ++r) {
                total += rowCosts[r];
            }
        } else {
            for (int r = sr - 1; r >= hr; --r) {
                total += rowCosts[r];
            }
        }

        if (sc < hc) {
            for (int c = sc + 1; c <= hc; ++c) {
                total += colCosts[c];
            }
        } else {
            for (int c = sc - 1; c >= hc; --c) {
                total += colCosts[c];
            }
        }

        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} startPos
 * @param {number[]} homePos
 * @param {number[]} rowCosts
 * @param {number[]} colCosts
 * @return {number}
 */
var minCost = function(startPos, homePos, rowCosts, colCosts) {
    let [sr, sc] = startPos;
    const [hr, hc] = homePos;
    let total = 0;

    if (sr < hr) {
        for (let r = sr + 1; r <= hr; ++r) {
            total += rowCosts[r];
        }
    } else if (sr > hr) {
        for (let r = sr - 1; r >= hr; --r) {
            total += rowCosts[r];
        }
    }

    if (sc < hc) {
        for (let c = sc + 1; c <= hc; ++c) {
            total += colCosts[c];
        }
    } else if (sc > hc) {
        for (let c = sc - 1; c >= hc; --c) {
            total += colCosts[c];
        }
    }

    return total;
};
```

## Typescript

```typescript
function minCost(startPos: number[], homePos: number[], rowCosts: number[], colCosts: number[]): number {
    let [sr, sc] = startPos;
    const [hr, hc] = homePos;
    let total = 0;

    if (sr < hr) {
        for (let r = sr + 1; r <= hr; ++r) {
            total += rowCosts[r];
        }
    } else {
        for (let r = sr - 1; r >= hr; --r) {
            total += rowCosts[r];
        }
    }

    if (sc < hc) {
        for (let c = sc + 1; c <= hc; ++c) {
            total += colCosts[c];
        }
    } else {
        for (let c = sc - 1; c >= hc; --c) {
            total += colCosts[c];
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $startPos
     * @param Integer[] $homePos
     * @param Integer[] $rowCosts
     * @param Integer[] $colCosts
     * @return Integer
     */
    function minCost($startPos, $homePos, $rowCosts, $colCosts) {
        $sr = $startPos[0];
        $sc = $startPos[1];
        $hr = $homePos[0];
        $hc = $homePos[1];
        $cost = 0;

        if ($sr < $hr) {
            for ($r = $sr + 1; $r <= $hr; $r++) {
                $cost += $rowCosts[$r];
            }
        } elseif ($sr > $hr) {
            for ($r = $sr - 1; $r >= $hr; $r--) {
                $cost += $rowCosts[$r];
            }
        }

        if ($sc < $hc) {
            for ($c = $sc + 1; $c <= $hc; $c++) {
                $cost += $colCosts[$c];
            }
        } elseif ($sc > $hc) {
            for ($c = $sc - 1; $c >= $hc; $c--) {
                $cost += $colCosts[$c];
            }
        }

        return $cost;
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ startPos: [Int], _ homePos: [Int], _ rowCosts: [Int], _ colCosts: [Int]) -> Int {
        var total = 0
        let sr = startPos[0]
        let sc = startPos[1]
        let hr = homePos[0]
        let hc = homePos[1]
        
        if sr < hr {
            for r in (sr + 1)...hr {
                total += rowCosts[r]
            }
        } else if sr > hr {
            for r in hr...sr - 1 {
                total += rowCosts[r]
            }
        }
        
        if sc < hc {
            for c in (sc + 1)...hc {
                total += colCosts[c]
            }
        } else if sc > hc {
            for c in hc...sc - 1 {
                total += colCosts[c]
            }
        }
        
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(startPos: IntArray, homePos: IntArray, rowCosts: IntArray, colCosts: IntArray): Int {
        var total = 0L
        val sr = startPos[0]
        val sc = startPos[1]
        val hr = homePos[0]
        val hc = homePos[1]

        if (sr < hr) {
            for (r in sr + 1..hr) {
                total += rowCosts[r].toLong()
            }
        } else if (sr > hr) {
            for (r in hr until sr) {
                total += rowCosts[r].toLong()
            }
        }

        if (sc < hc) {
            for (c in sc + 1..hc) {
                total += colCosts[c].toLong()
            }
        } else if (sc > hc) {
            for (c in hc until sc) {
                total += colCosts[c].toLong()
            }
        }

        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minCost(List<int> startPos, List<int> homePos, List<int> rowCosts, List<int> colCosts) {
    int total = 0;
    int sr = startPos[0];
    int sc = startPos[1];
    int hr = homePos[0];
    int hc = homePos[1];

    if (sr < hr) {
      for (int r = sr + 1; r <= hr; ++r) {
        total += rowCosts[r];
      }
    } else if (sr > hr) {
      for (int r = sr - 1; r >= hr; --r) {
        total += rowCosts[r];
      }
    }

    if (sc < hc) {
      for (int c = sc + 1; c <= hc; ++c) {
        total += colCosts[c];
      }
    } else if (sc > hc) {
      for (int c = sc - 1; c >= hc; --c) {
        total += colCosts[c];
      }
    }

    return total;
  }
}
```

## Golang

```go
func minCost(startPos []int, homePos []int, rowCosts []int, colCosts []int) int {
	startRow, startCol := startPos[0], startPos[1]
	homeRow, homeCol := homePos[0], homePos[1]

	total := 0

	if startRow < homeRow {
		for r := startRow + 1; r <= homeRow; r++ {
			total += rowCosts[r]
		}
	} else if startRow > homeRow {
		for r := startRow - 1; r >= homeRow; r-- {
			total += rowCosts[r]
		}
	}

	if startCol < homeCol {
		for c := startCol + 1; c <= homeCol; c++ {
			total += colCosts[c]
		}
	} else if startCol > homeCol {
		for c := startCol - 1; c >= homeCol; c-- {
			total += colCosts[c]
		}
	}

	return total
}
```

## Ruby

```ruby
def min_cost(start_pos, home_pos, row_costs, col_costs)
  sr, sc = start_pos
  hr, hc = home_pos
  total = 0

  if sr < hr
    (sr + 1..hr).each { |r| total += row_costs[r] }
  elsif sr > hr
    (hr...sr).each { |r| total += row_costs[r] }
  end

  if sc < hc
    (sc + 1..hc).each { |c| total += col_costs[c] }
  elsif sc > hc
    (hc...sc).each { |c| total += col_costs[c] }
  end

  total
end
```

## Scala

```scala
object Solution {
    def minCost(startPos: Array[Int], homePos: Array[Int], rowCosts: Array[Int], colCosts: Array[Int]): Int = {
        var cost: Long = 0L
        val (sr, sc) = (startPos(0), startPos(1))
        val (hr, hc) = (homePos(0), homePos(1))

        if (sr < hr) {
            for (r <- sr + 1 to hr) cost += rowCosts(r)
        } else if (sr > hr) {
            for (r <- sr - 1 until hr - 1 by -1) cost += rowCosts(r)
        }

        if (sc < hc) {
            for (c <- sc + 1 to hc) cost += colCosts(c)
        } else if (sc > hc) {
            for (c <- sc - 1 until hc - 1 by -1) cost += colCosts(c)
        }

        cost.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(start_pos: Vec<i32>, home_pos: Vec<i32>, row_costs: Vec<i32>, col_costs: Vec<i32>) -> i32 {
        let start_row = start_pos[0] as usize;
        let start_col = start_pos[1] as usize;
        let home_row = home_pos[0] as usize;
        let home_col = home_pos[1] as usize;

        let mut total: i64 = 0;

        if start_row < home_row {
            for r in (start_row + 1)..=home_row {
                total += row_costs[r] as i64;
            }
        } else {
            for r in (home_row..start_row).rev() {
                total += row_costs[r] as i64;
            }
        }

        if start_col < home_col {
            for c in (start_col + 1)..=home_col {
                total += col_costs[c] as i64;
            }
        } else {
            for c in (home_col..start_col).rev() {
                total += col_costs[c] as i64;
            }
        }

        total as i32
    }
}
```

## Racket

```racket
(define/contract (min-cost startPos homePos rowCosts colCosts)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((sr (first startPos))
         (sc (second startPos))
         (hr (first homePos))
         (hc (second homePos)))
    (define (sum-range a b vec)
      (if (= a b) 
          0
          (let ((step (if (< a b) 1 -1)))
            (for/sum ([i (in-range (+ a step) (+ b step) step)])
              (list-ref vec i)))))
    (+ (sum-range sr hr rowCosts)
       (sum-range sc hc colCosts))))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/4]).

-spec min_cost(StartPos :: [integer()], HomePos :: [integer()], RowCosts :: [integer()], ColCosts :: [integer()]) -> integer().
min_cost([StartRow, StartCol], [HomeRow, HomeCol], RowCosts, ColCosts) ->
    RowTuple = list_to_tuple(RowCosts),
    ColTuple = list_to_tuple(ColCosts),
    RowSum = sum_range(StartRow, HomeRow, RowTuple),
    ColSum = sum_range(StartCol, HomeCol, ColTuple),
    RowSum + ColSum.

sum_range(From, To, _Tuple) when From == To ->
    0;
sum_range(From, To, Tuple) ->
    Step = if From < To -> 1; true -> -1 end,
    sum_range_loop(From + Step, To, Step, Tuple, 0).

sum_range_loop(Cur, To, _Step, Tuple, Acc) when Cur == To ->
    Acc + element(Cur + 1, Tuple);
sum_range_loop(Cur, To, Step, Tuple, Acc) ->
    NewAcc = Acc + element(Cur + 1, Tuple),
    sum_range_loop(Cur + Step, To, Step, Tuple, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(start_pos :: [integer], home_pos :: [integer], row_costs :: [integer], col_costs :: [integer]) :: integer
  def min_cost(start_pos, home_pos, row_costs, col_costs) do
    sr = Enum.at(start_pos, 0)
    sc = Enum.at(start_pos, 1)
    hr = Enum.at(home_pos, 0)
    hc = Enum.at(home_pos, 1)

    row_total =
      cond do
        sr < hr ->
          Enum.reduce((sr + 1)..hr, 0, fn r, acc -> acc + Enum.at(row_costs, r) end)

        sr > hr ->
          Enum.reduce(hr..(sr - 1), 0, fn r, acc -> acc + Enum.at(row_costs, r) end)

        true ->
          0
      end

    col_total =
      cond do
        sc < hc ->
          Enum.reduce((sc + 1)..hc, 0, fn c, acc -> acc + Enum.at(col_costs, c) end)

        sc > hc ->
          Enum.reduce(hc..(sc - 1), 0, fn c, acc -> acc + Enum.at(col_costs, c) end)

        true ->
          0
      end

    row_total + col_total
  end
end
```
