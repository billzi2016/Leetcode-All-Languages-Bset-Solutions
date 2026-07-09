# 1536. Minimum Swaps to Arrange a Binary Grid

## Cpp

```cpp
class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> rightmost(n);
        for (int i = 0; i < n; ++i) {
            int pos = -1;
            for (int j = n - 1; j >= 0; --j) {
                if (grid[i][j] == 1) {
                    pos = j;
                    break;
                }
            }
            rightmost[i] = pos;
        }
        int swaps = 0;
        for (int i = 0; i < n; ++i) {
            int j = i;
            while (j < n && rightmost[j] > i) {
                ++j;
            }
            if (j == n) return -1;
            for (int k = j; k > i; --k) {
                swap(rightmost[k], rightmost[k - 1]);
                ++swaps;
            }
        }
        return swaps;
    }
};
```

## Java

```java
class Solution {
    public int minSwaps(int[][] grid) {
        int n = grid.length;
        int[] rightmost = new int[n];
        for (int i = 0; i < n; i++) {
            int pos = -1;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    pos = j;
                    break;
                }
            }
            rightmost[i] = pos;
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            int k = i;
            while (k < n && rightmost[k] > i) {
                k++;
            }
            if (k == n) {
                return -1;
            }
            while (k > i) {
                int temp = rightmost[k];
                rightmost[k] = rightmost[k - 1];
                rightmost[k - 1] = temp;
                swaps++;
                k--;
            }
        }
        return swaps;
    }
}
```

## Python

```python
class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # rightmost 1 index for each row; -1 if no 1
        right = []
        for i in range(n):
            pos = -1
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    pos = j
                    break
            right.append(pos)

        swaps = 0
        for i in range(n):
            # find a row at or below i with rightmost_one <= i
            target = i
            while target < n and right[target] > i:
                target += 1
            if target == n:
                return -1
            # bring the found row up to position i using adjacent swaps
            while target > i:
                right[target], right[target - 1] = right[target - 1], right[target]
                swaps += 1
                target -= 1

        return swaps
```

## Python3

```python
from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # last[i] = rightmost column index containing 1 in row i, -1 if none
        last = []
        for row in grid:
            pos = -1
            for j in range(n - 1, -1, -1):
                if row[j] == 1:
                    pos = j
                    break
            last.append(pos)

        swaps = 0
        for i in range(n):
            # find a row at or below i whose rightmost 1 is within column i
            target = -1
            for j in range(i, n):
                if last[j] <= i:
                    target = j
                    break
            if target == -1:
                return -1
            # bubble the found row up to position i
            while target > i:
                last[target], last[target - 1] = last[target - 1], last[target]
                swaps += 1
                target -= 1
        return swaps
```

## C

```c
#include <stdlib.h>

int minSwaps(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int *rightmost = (int *)malloc(n * sizeof(int));
    if (!rightmost) return -1; // allocation failure safeguard

    for (int i = 0; i < n; ++i) {
        int pos = -1;
        for (int j = n - 1; j >= 0; --j) {
            if (grid[i][j] == 1) {
                pos = j;
                break;
            }
        }
        rightmost[i] = pos;
    }

    int swaps = 0;
    for (int i = 0; i < n; ++i) {
        int j = i;
        while (j < n && rightmost[j] > i) {
            ++j;
        }
        if (j == n) {
            free(rightmost);
            return -1;
        }
        for (int k = j; k > i; --k) {
            int tmp = rightmost[k];
            rightmost[k] = rightmost[k - 1];
            rightmost[k - 1] = tmp;
            ++swaps;
        }
    }

    free(rightmost);
    return swaps;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSwaps(int[][] grid) {
        int n = grid.Length;
        int[] rightmost = new int[n];
        for (int i = 0; i < n; i++) {
            int pos = -1;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    pos = j;
                    break;
                }
            }
            rightmost[i] = pos;
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n && rightmost[j] > i) {
                j++;
            }
            if (j == n) return -1;
            for (int k = j; k > i; k--) {
                int temp = rightmost[k];
                rightmost[k] = rightmost[k - 1];
                rightmost[k - 1] = temp;
                swaps++;
            }
        }

        return swaps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minSwaps = function(grid) {
    const n = grid.length;
    const maxRight = new Array(n);
    for (let i = 0; i < n; i++) {
        let pos = -1;
        for (let j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 1) {
                pos = j;
                break;
            }
        }
        maxRight[i] = pos;
    }

    let swaps = 0;
    for (let i = 0; i < n; i++) {
        let j = i;
        while (j < n && maxRight[j] > i) {
            j++;
        }
        if (j === n) return -1;
        while (j > i) {
            // swap adjacent rows in the maxRight array
            const temp = maxRight[j];
            maxRight[j] = maxRight[j - 1];
            maxRight[j - 1] = temp;
            swaps++;
            j--;
        }
    }

    return swaps;
};
```

## Typescript

```typescript
function minSwaps(grid: number[][]): number {
    const n = grid.length;
    const rightmost: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        let pos = -1;
        for (let j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 1) {
                pos = j;
                break;
            }
        }
        rightmost[i] = pos;
    }

    let swaps = 0;
    for (let i = 0; i < n; i++) {
        let j = i;
        while (j < n && rightmost[j] > i) {
            j++;
        }
        if (j === n) return -1;
        while (j > i) {
            [rightmost[j], rightmost[j - 1]] = [rightmost[j - 1], rightmost[j]];
            swaps++;
            j--;
        }
    }

    return swaps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minSwaps($grid) {
        $n = count($grid);
        $right = array_fill(0, $n, -1);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $n - 1; $j >= 0; $j--) {
                if ($grid[$i][$j] == 1) {
                    $right[$i] = $j;
                    break;
                }
            }
        }

        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $j = $i;
            while ($j < $n && $right[$j] > $i) {
                $j++;
            }
            if ($j == $n) {
                return -1;
            }
            while ($j > $i) {
                $temp = $right[$j];
                $right[$j] = $right[$j - 1];
                $right[$j - 1] = $temp;
                $j--;
                $ans++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minSwaps(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var lastOne = [Int]()
        for row in grid {
            var pos = -1
            for j in 0..<n {
                if row[j] == 1 {
                    pos = j
                }
            }
            lastOne.append(pos)
        }
        
        var swaps = 0
        for i in 0..<n {
            var j = i
            while j < n && lastOne[j] > i {
                j += 1
            }
            if j == n { return -1 }
            while j > i {
                lastOne.swapAt(j, j - 1)
                swaps += 1
                j -= 1
            }
        }
        return swaps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwaps(grid: Array<IntArray>): Int {
        val n = grid.size
        val rightmost = IntArray(n)
        for (i in 0 until n) {
            var pos = -1
            for (j in n - 1 downTo 0) {
                if (grid[i][j] == 1) {
                    pos = j
                    break
                }
            }
            rightmost[i] = pos
        }
        var swaps = 0
        for (i in 0 until n) {
            var j = i
            while (j < n && rightmost[j] > i) {
                j++
            }
            if (j == n) return -1
            while (j > i) {
                val temp = rightmost[j]
                rightmost[j] = rightmost[j - 1]
                rightmost[j - 1] = temp
                swaps++
                j--
            }
        }
        return swaps
    }
}
```

## Dart

```dart
class Solution {
  int minSwaps(List<List<int>> grid) {
    int n = grid.length;
    List<int> rightmost = List.filled(n, -1);
    for (int i = 0; i < n; ++i) {
      for (int j = n - 1; j >= 0; --j) {
        if (grid[i][j] == 1) {
          rightmost[i] = j;
          break;
        }
      }
    }

    int swaps = 0;
    for (int i = 0; i < n; ++i) {
      int k = i;
      while (k < n && rightmost[k] > i) {
        k++;
      }
      if (k == n) return -1;
      while (k > i) {
        int temp = rightmost[k];
        rightmost[k] = rightmost[k - 1];
        rightmost[k - 1] = temp;
        swaps++;
        k--;
      }
    }

    return swaps;
  }
}
```

## Golang

```go
func minSwaps(grid [][]int) int {
	n := len(grid)
	rightmost := make([]int, n)
	for i := 0; i < n; i++ {
		pos := -1
		for j := n - 1; j >= 0; j-- {
			if grid[i][j] == 1 {
				pos = j
				break
			}
		}
		rightmost[i] = pos
	}

	swaps := 0
	for i := 0; i < n; i++ {
		target := -1
		for j := i; j < n; j++ {
			if rightmost[j] <= i {
				target = j
				break
			}
		}
		if target == -1 {
			return -1
		}
		for k := target; k > i; k-- {
			rightmost[k], rightmost[k-1] = rightmost[k-1], rightmost[k]
			swaps++
		}
	}
	return swaps
}
```

## Ruby

```ruby
def min_swaps(grid)
  n = grid.size
  rightmost = Array.new(n, -1)

  n.times do |i|
    row = grid[i]
    idx = -1
    (n - 1).downto(0) do |j|
      if row[j] == 1
        idx = j
        break
      end
    end
    rightmost[i] = idx
  end

  swaps = 0
  i = 0
  while i < n
    j = i
    while j < n && rightmost[j] > i
      j += 1
    end
    return -1 if j == n

    while j > i
      rightmost[j], rightmost[j - 1] = rightmost[j - 1], rightmost[j]
      swaps += 1
      j -= 1
    end
    i += 1
  end

  swaps
end
```

## Scala

```scala
object Solution {
    def minSwaps(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        val rightmost = new Array[Int](n)
        for (i <- 0 until n) {
            var pos = -1
            for (j <- 0 until n) {
                if (grid(i)(j) == 1) pos = j
            }
            rightmost(i) = pos
        }

        var swaps = 0
        for (i <- 0 until n) {
            var j = i
            while (j < n && rightmost(j) > i) {
                j += 1
            }
            if (j == n) return -1
            while (j > i) {
                val tmp = rightmost(j)
                rightmost(j) = rightmost(j - 1)
                rightmost(j - 1) = tmp
                swaps += 1
                j -= 1
            }
        }
        swaps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        // rightmost[i] = index of the rightmost 1 in row i, or -1 if none
        let mut rightmost: Vec<i32> = vec![0; n];
        for i in 0..n {
            let mut last = -1;
            for j in (0..n).rev() {
                if grid[i][j] == 1 {
                    last = j as i32;
                    break;
                }
            }
            rightmost[i] = last;
        }

        let mut swaps: i32 = 0;
        for i in 0..n {
            // find a row at or below i that can be placed at position i
            let mut j = i;
            while j < n && rightmost[j] > i as i32 {
                j += 1;
            }
            if j == n {
                return -1;
            }
            // bring the found row up to index i by swapping adjacent rows
            while j > i {
                rightmost.swap(j, j - 1);
                swaps += 1;
                j -= 1;
            }
        }
        swaps
    }
}
```

## Racket

```racket
(define/contract (min-swaps grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (rightmost-list
          (map (lambda (row)
                 (let loop ((idx 0) (mx -1))
                   (if (= idx (length row))
                       mx
                       (loop (+ idx 1)
                             (if (= (list-ref row idx) 1) idx mx)))))
               grid))
         (v (list->vector rightmost-list)))
    (let recur ((i 0) (total 0))
      (if (= i n)
          total
          (let search ((j i))
            (cond
              [(>= j n) -1]                                   ; impossible
              [(<= (vector-ref v j) i)                        ; found suitable row
               (let swap-loop ((k j) (cnt total))
                 (if (= k i)
                     (recur (+ i 1) cnt)
                     (begin
                       (let ((tmp (vector-ref v (- k 1))))
                         (vector-set! v (- k 1) (vector-ref v k))
                         (vector-set! v k tmp))
                       (swap-loop (- k 1) (+ cnt 1)))))]
              [else (search (+ j 1))]))))))
```

## Erlang

```erlang
-module(solution).
-export([min_swaps/1]).

-spec min_swaps(Grid :: [[integer()]]) -> integer().
min_swaps(Grid) ->
    N = length(Grid),
    MaxRights = [rightmost_one(Row) || Row <- Grid],
    process(0, MaxRights, 0, N).

rightmost_one(Row) ->
    rightmost_one(Row, 0, -1).

rightmost_one([], _Idx, Max) -> Max;
rightmost_one([H|T], Idx, Max) ->
    NewMax = case H of
        1 -> Idx;
        _ -> Max
    end,
    rightmost_one(T, Idx + 1, NewMax).

find_pos(I, List, J) ->
    case List of
        [] -> error;
        [H|T] ->
            if H =< I -> {ok, J};
               true -> find_pos(I, T, J + 1)
            end
    end.

move_up(List, I, J) ->
    {Prefix, Rest} = lists:split(I, List),
    Diff = J - I,
    case Diff of
        0 -> {List, ok};
        _ ->
            {BeforeTarget, [Target|After]} = lists:split(Diff, Rest),
            NewList = Prefix ++ [Target] ++ BeforeTarget ++ After,
            {NewList, ok}
    end.

process(I, List, Acc, N) when I >= N -> Acc;
process(I, List, Acc, N) ->
    case find_pos(I, List, I) of
        {ok, J} ->
            Swaps = J - I,
            NewAcc = Acc + Swaps,
            {NewList,_} = move_up(List, I, J),
            process(I + 1, NewList, NewAcc, N);
        error -> -1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swaps(grid :: [[integer]]) :: integer
  def min_swaps(grid) do
    n = length(grid)
    max_rights = Enum.map(grid, &rightmost_one/1)
    do_swap(max_rights, 0, 0, n)
  end

  defp rightmost_one(row) do
    case Enum.with_index(row) |> Enum.reverse() |> Enum.find(fn {v, _idx} -> v == 1 end) do
      nil -> -1
      {_v, idx} -> idx
    end
  end

  defp do_swap(_rights, i, swaps, n) when i == n, do: swaps

  defp do_swap(rights, i, swaps, n) do
    case Enum.with_index(rights)
         |> Enum.drop_while(fn {_v, idx} -> idx < i end)
         |> Enum.find(fn {v, _idx} -> v <= i end) do
      nil ->
        -1

      {_, j} ->
        new_swaps = swaps + (j - i)
        {value, rest} = List.pop_at(rights, j)
        new_rights = List.insert_at(rest, i, value)
        do_swap(new_rights, i + 1, new_swaps, n)
    end
  end
end
```
