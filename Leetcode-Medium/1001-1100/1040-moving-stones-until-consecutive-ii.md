# 1040. Moving Stones Until Consecutive II

## Cpp

```cpp
class Solution {
public:
    vector<int> numMovesStonesII(vector<int>& stones) {
        int n = stones.size();
        sort(stones.begin(), stones.end());
        
        // Maximum moves
        int maxMove = max(stones[n-2] - stones[0], stones[n-1] - stones[1]) - (n - 2);
        
        // Minimum moves using sliding window
        int minMove = n;
        int i = 0;
        for (int j = 0; j < n; ++j) {
            while (stones[j] - stones[i] >= n) ++i;
            int cnt = j - i + 1;
            if (cnt == n - 1 && stones[j] - stones[i] == n - 2) {
                // Special case where we need two moves
                minMove = min(minMove, 2);
            } else {
                minMove = min(minMove, n - cnt);
            }
        }
        return {minMove, maxMove};
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[] numMovesStonesII(int[] stones) {
        int n = stones.length;
        Arrays.sort(stones);
        
        // Maximum moves
        int maxMove = Math.max(stones[n - 2] - stones[0], stones[n - 1] - stones[1]) - (n - 2);
        
        // Minimum moves using sliding window
        int left = 0, best = 0;
        for (int right = 0; right < n; ++right) {
            while (stones[right] - stones[left] + 1 > n) {
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        
        int minMove;
        if (best == n - 1 && ((stones[n - 2] - stones[0] == n - 2) || (stones[n - 1] - stones[1] == n - 2))) {
            minMove = 2;
        } else {
            minMove = n - best;
        }
        
        return new int[]{minMove, maxMove};
    }
}
```

## Python

```python
class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        n = len(stones)

        # maximum moves
        max_moves = max(stones[-2] - stones[0], stones[-1] - stones[1]) - (n - 2)

        # minimum moves using sliding window
        i = 0
        best = 0
        for j in range(n):
            while stones[j] - stones[i] + 1 > n:
                i += 1
            best = max(best, j - i + 1)

        min_moves = n - best

        # special case where we need two moves instead of one
        if best == n - 1:
            if (stones[-2] - stones[0] == n - 2) or (stones[-1] - stones[1] == n - 2):
                min_moves = 2

        return [min_moves, max_moves]
```

## Python3

```python
from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)

        # maximum moves
        max_moves = max(
            stones[-1] - stones[1] - (n - 2),
            stones[-2] - stones[0] - (n - 2)
        )

        # minimum moves using sliding window
        best = n
        i = 0
        for j in range(n):
            while stones[j] - stones[i] >= n:
                i += 1
            cur = j - i + 1
            if cur == n - 1 and stones[j] - stones[i] == n - 2:
                best = min(best, 2)
            else:
                best = min(best, n - cur)

        return [best, max_moves]
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numMovesStonesII(int* stones, int stonesSize, int* returnSize){
    qsort(stones, stonesSize, sizeof(int), cmp_int);
    int n = stonesSize;

    // Maximum moves
    int maxMoveLeft  = stones[n-1] - stones[1]   - (n - 2);
    int maxMoveRight = stones[n-2] - stones[0]   - (n - 2);
    int maxMove = maxMoveLeft > maxMoveRight ? maxMoveLeft : maxMoveRight;

    // Minimum moves using sliding window
    int i = 0, maxInside = 0;
    for (int j = 0; j < n; ++j) {
        while (stones[j] - stones[i] + 1 > n) {
            ++i;
        }
        int cnt = j - i + 1;
        if (cnt > maxInside) maxInside = cnt;
    }

    int minMove = n - maxInside;

    // Special case where we need two moves instead of one
    if (minMove == 1) {
        int condition1 = (stones[n-2] - stones[0] == n - 2) && (stones[n-1] - stones[n-2] > 2);
        int condition2 = (stones[n-1] - stones[1] == n - 2) && (stones[1] - stones[0] > 2);
        if (condition1 || condition2) {
            minMove = 2;
        }
    }

    int *res = (int *)malloc(2 * sizeof(int));
    res[0] = minMove;
    res[1] = maxMove;
    *returnSize = 2;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] NumMovesStonesII(int[] stones) {
        int n = stones.Length;
        Array.Sort(stones);
        
        // Maximum moves
        int maxMove = Math.Max(stones[n - 2] - stones[0], stones[n - 1] - stones[1]) - (n - 2);
        
        // Minimum moves using sliding window
        int minMove = n;
        int left = 0;
        for (int right = 0; right < n; ++right) {
            while (stones[right] - stones[left] >= n) {
                left++;
            }
            int count = right - left + 1;
            if (count == n - 1 && stones[right] - stones[left] == n - 2) {
                // Special case: all but one stone are consecutive and the gap is exactly 2
                minMove = Math.Min(minMove, 2);
            } else {
                minMove = Math.Min(minMove, n - count);
            }
        }
        
        return new int[] { minMove, maxMove };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {number[]}
 */
var numMovesStonesII = function(stones) {
    const n = stones.length;
    stones.sort((a, b) => a - b);
    
    // maximum moves
    const maxMoveLeft = stones[n - 2] - stones[0];
    const maxMoveRight = stones[n - 1] - stones[1];
    const maxMoves = Math.max(maxMoveLeft, maxMoveRight) - (n - 2);
    
    // minimum moves using sliding window
    let best = 0;
    let j = 0;
    for (let i = 0; i < n; ++i) {
        while (j < n && stones[j] - stones[i] <= n - 1) {
            ++j;
        }
        best = Math.max(best, j - i);
    }
    
    let minMoves;
    if (
        best === n - 1 &&
        (stones[n - 2] - stones[0] === n - 2 ||
         stones[n - 1] - stones[1] === n - 2)
    ) {
        minMoves = 2;
    } else {
        minMoves = n - best;
    }
    
    return [minMoves, maxMoves];
};
```

## Typescript

```typescript
function numMovesStonesII(stones: number[]): number[] {
    const n = stones.length;
    stones.sort((a, b) => a - b);
    
    // maximum moves
    const maxMove = Math.max(
        stones[n - 1] - stones[1] - (n - 2),
        stones[n - 2] - stones[0] - (n - 2)
    );
    
    // minimum moves using sliding window
    let maxInWindow = 0;
    let left = 0;
    for (let right = 0; right < n; ++right) {
        while (stones[right] - stones[left] + 1 > n) {
            ++left;
        }
        const cnt = right - left + 1;
        if (cnt > maxInWindow) maxInWindow = cnt;
    }
    
    let minMove = n - maxInWindow;
    
    // handle the special case where we need exactly 2 moves
    if (maxInWindow === n - 1) {
        const leftConsecutive = stones[n - 2] - stones[0] === n - 2 && stones[n - 1] - stones[n - 2] > 2;
        const rightConsecutive = stones[n - 1] - stones[1] === n - 2 && stones[1] - stones[0] > 2;
        if (leftConsecutive || rightConsecutive) {
            minMove = 2;
        }
    }
    
    return [minMove, maxMove];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer[]
     */
    function numMovesStonesII($stones) {
        sort($stones);
        $n = count($stones);
        
        // Maximum moves
        $maxMove = max($stones[$n - 2] - $stones[0], $stones[$n - 1] - $stones[1]) - ($n - 2);
        
        // Minimum moves using sliding window
        $minMove = $n;
        $j = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($j < $i) {
                $j = $i;
            }
            while ($j + 1 < $n && $stones[$j + 1] - $stones[$i] < $n) {
                $j++;
            }
            $cnt = $j - $i + 1;
            if ($cnt == $n - 1 && $stones[$j] - $stones[$i] == $n - 2) {
                // Special case where we need two moves
                $minMove = min($minMove, 2);
            } else {
                $minMove = min($minMove, $n - $cnt);
            }
        }
        
        return [$minMove, $maxMove];
    }
}
```

## Swift

```swift
class Solution {
    func numMovesStonesII(_ stones: [Int]) -> [Int] {
        let a = stones.sorted()
        let n = a.count
        // Maximum moves
        let maxMove = max(a[n - 1] - a[1] - (n - 2), a[n - 2] - a[0] - (n - 2))
        
        // Minimum moves
        var minMove: Int
        if (a[n - 2] - a[0] == n - 2 && a[n - 1] - a[n - 2] > 2) ||
           (a[n - 1] - a[1] == n - 2 && a[1] - a[0] > 2) {
            minMove = 2
        } else {
            var best = 0
            var j = 0
            for i in 0..<n {
                while j < n && a[j] - a[i] < n {
                    j += 1
                }
                let cnt = j - i
                if cnt > best { best = cnt }
            }
            minMove = n - best
        }
        
        return [minMove, maxMove]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numMovesStonesII(stones: IntArray): IntArray {
        val n = stones.size
        stones.sort()
        // Maximum moves
        val maxMove = kotlin.math.max(
            stones[n - 1] - stones[1] - (n - 2),
            stones[n - 2] - stones[0] - (n - 2)
        )
        // Minimum moves using sliding window
        var best = 0
        var j = 0
        for (i in 0 until n) {
            while (j < n && stones[j] - stones[i] + 1 <= n) {
                j++
            }
            val cnt = j - i
            if (cnt > best) best = cnt
        }
        val minMove = if (best == n - 1) {
            if ((stones[n - 2] - stones[0] == n - 2) || (stones[n - 1] - stones[1] == n - 2)) 2 else 1
        } else {
            n - best
        }
        return intArrayOf(minMove, maxMove)
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  List<int> numMovesStonesII(List<int> stones) {
    stones.sort();
    int n = stones.length;

    // Maximum moves
    int maxMove1 = stones[n - 2] - stones[0] - (n - 2);
    int maxMove2 = stones[n - 1] - stones[1] - (n - 2);
    int maxMoves = math.max(maxMove1, maxMove2);

    // Minimum moves using sliding window
    int minMoves = n;
    int left = 0;
    for (int right = 0; right < n; ++right) {
      while (stones[right] - stones[left] + 1 > n) {
        left++;
      }
      int cnt = right - left + 1;
      if (cnt == n - 1 && stones[right] - stones[left] + 1 == n - 1) {
        minMoves = math.min(minMoves, 2);
      } else {
        minMoves = math.min(minMoves, n - cnt);
      }
    }

    return [minMoves, maxMoves];
  }
}
```

## Golang

```go
func numMovesStonesII(stones []int) []int {
    n := len(stones)
    sort.Ints(stones)

    // maximum moves
    maxMove1 := stones[n-1] - stones[1] - (n - 2)
    maxMove2 := stones[n-2] - stones[0] - (n - 2)
    if maxMove2 > maxMove1 {
        maxMove1 = maxMove2
    }

    // minimum moves using sliding window
    best := 0
    j := 0
    for i := 0; i < n; i++ {
        for j+1 < n && stones[j+1]-stones[i]+1 <= n {
            j++
        }
        cur := j - i + 1
        if cur > best {
            best = cur
        }
    }
    minMoves := n - best

    // special case where we need two moves instead of one
    if (stones[n-2]-stones[0] == n-2 && stones[n-1]-stones[n-2] > 2) ||
        (stones[n-1]-stones[1] == n-2 && stones[1]-stones[0] > 2) {
        minMoves = 2
    }

    return []int{minMoves, maxMove1}
}
```

## Ruby

```ruby
def num_moves_stones_ii(stones)
  stones.sort!
  n = stones.length

  # maximum moves
  max_move = [stones[-2] - stones[0], stones[-1] - stones[1]].max - (n - 2)

  # minimum moves using sliding window
  max_in_window = 0
  j = 0
  (0...n).each do |i|
    while j + 1 < n && stones[j + 1] - stones[i] < n
      j += 1
    end
    count = j - i + 1
    max_in_window = [max_in_window, count].max
  end

  min_move = n - max_in_window

  # special case where we need exactly two moves
  if (stones[n - 2] - stones[0] == n - 2 && stones[n - 1] - stones[n - 2] > 2) ||
     (stones[n - 1] - stones[1] == n - 2 && stones[1] - stones[0] > 2)
    min_move = 2
  end

  [min_move, max_move]
end
```

## Scala

```scala
object Solution {
    def numMovesStonesII(stones: Array[Int]): Array[Int] = {
        val a = stones.sorted
        val n = a.length

        var minMoves = n
        var j = 0
        for (i <- 0 until n) {
            while (j < n && a(j) - a(i) < n) {
                j += 1
            }
            val cnt = j - i
            if (cnt == n - 1 && a(j - 1) - a(i) == n - 2) {
                minMoves = math.min(minMoves, 2)
            } else {
                minMoves = math.min(minMoves, n - cnt)
            }
        }

        val maxMoves = math.max(a(n - 1) - a(1) - (n - 2), a(n - 2) - a(0) - (n - 2))
        Array(minMoves, maxMoves)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_moves_stones_ii(mut stones: Vec<i32>) -> Vec<i32> {
        stones.sort_unstable();
        let n = stones.len() as i32;

        // Maximum moves
        let max_move1 = stones[stones.len() - 1] - stones[1] - (n - 2);
        let max_move2 = stones[stones.len() - 2] - stones[0] - (n - 2);
        let max_moves = std::cmp::max(max_move1, max_move2);

        // Minimum moves using sliding window
        let mut max_in_window = 0usize;
        let mut j = 0usize;
        for i in 0..stones.len() {
            while j + 1 < stones.len()
                && stones[j + 1] - stones[i] <= n - 1
            {
                j += 1;
            }
            let cnt = j - i + 1;
            if cnt > max_in_window {
                max_in_window = cnt;
            }
        }

        // Special case where we need exactly two moves
        let mut min_moves = (stones.len() as i32) - max_in_window as i32;
        if (stones[stones.len() - 2] - stones[0] == n - 2 && stones[stones.len() - 1] - stones[stones.len() - 2] > 2)
            || (stones[stones.len() - 1] - stones[1] == n - 2 && stones[1] - stones[0] > 2)
        {
            min_moves = 2;
        }

        vec![min_moves, max_moves]
    }
}
```

## Racket

```racket
(define/contract (num-moves-stones-ii stones)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted (sort stones <))
         (arr    (list->vector sorted))
         (n      (vector-length arr)))
    ;; find maximal number of stones that can fit into a window of size n
    (let ([i   (box 0)]
          [best (box 0)])
      (for ([j (in-range n)])
        (while (> (+ (- (vector-ref arr j) (vector-ref arr (unbox i))) 1) n)
          (set-box! i (+ (unbox i) 1)))
        (let ((window (+ 1 (- j (unbox i)))))
          (when (> window (unbox best))
            (set-box! best window))))
      (define max-in-window (unbox best))
      ;; minimum moves
      (define min-moves
        (if (= max-in-window n)
            0
            (let ((candidate (- n max-in-window)))
              (if (and (= candidate 1)
                       (or (and (= (- (vector-ref arr (- n 2)) (vector-ref arr 0))
                                 (- n 2))
                                (> (- (vector-ref arr (- n 1)) (vector-ref arr (- n 2))) 2))
                           (and (= (- (vector-ref arr (- 1)) (vector-ref arr 1))
                                 (- n 2))
                                (> (- (vector-ref arr 1) (vector-ref arr 0)) 2))))
                  2
                  candidate)))))
      ;; maximum moves
      (define max-moves
        (max (- (vector-ref arr (- n 1)) (vector-ref arr 1) (- n 2))
             (- (vector-ref arr (- n 2)) (vector-ref arr 0) (- n 2))))
      (list min-moves max-moves))))
```

## Erlang

```erlang
-module(solution).
-export([num_moves_stones_ii/1]).

-spec num_moves_stones_ii(Stones :: [integer()]) -> [integer()].
num_moves_stones_ii(Stones) ->
    Sorted = lists:sort(Stones),
    Arr = list_to_tuple(Sorted),
    N = tuple_size(Arr),

    MaxCount = max_count(Arr, N),

    MinMoves =
        case (MaxCount == N - 1) andalso
             ((element(N - 1, Arr) - element(1, Arr) == N - 2) orelse
              (element(N, Arr) - element(2, Arr) == N - 2)) of
            true -> 2;
            false -> N - MaxCount
        end,

    MaxMoves = erlang:max(element(N, Arr) - element(2, Arr),
                         element(N - 1, Arr) - element(1, Arr)) - (N - 2),

    [MinMoves, MaxMoves].

max_count(Arr, N) ->
    max_count_loop(0, 0, 0, Arr, N).

max_count_loop(I, J, Max, _Arr, N) when I >= N ->
    Max;
max_count_loop(I, J, Max, Arr, N) ->
    J1 = if J < I -> I; true -> J end,
    {J2, _} = advance(J1, I, Arr, N),
    Count = J2 - I + 1,
    NewMax = if Count > Max -> Count; true -> Max end,
    max_count_loop(I + 1, J2, NewMax, Arr, N).

advance(J, I, Arr, N) ->
    case J + 1 < N of
        true ->
            Diff = element(J + 2, Arr) - element(I + 1, Arr),
            if Diff < N -> advance(J + 1, I, Arr, N);
               true -> {J, ok}
            end;
        false -> {J, ok}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_moves_stones_ii(stones :: [integer]) :: [integer]
  def num_moves_stones_ii(stones) do
    arr = Enum.sort(stones)
    n = length(arr)

    # maximum moves
    left_gap = Enum.at(arr, n - 1) - Enum.at(arr, 1) - (n - 2)
    right_gap = Enum.at(arr, n - 2) - Enum.at(arr, 0) - (n - 2)
    max_moves = if left_gap > right_gap, do: left_gap, else: right_gap

    # minimum moves using sliding window
    {max_in_window, _} =
      Enum.reduce(0..(n - 1), {0, 0}, fn j, {max_win, i} ->
        i = move_i(i, arr, j, n)
        cur = j - i + 1
        new_max = if cur > max_win, do: cur, else: max_win
        {new_max, i}
      end)

    min_moves =
      cond do
        max_in_window == n ->
          0

        max_in_window == n - 1 ->
          left_consecutive = Enum.at(arr, n - 2) - Enum.at(arr, 0) == n - 2
          right_gap_two = Enum.at(arr, n - 1) - Enum.at(arr, n - 2) == 2
          left_gap_two = Enum.at(arr, 1) - Enum.at(arr, 0) == 2
          right_consecutive = Enum.at(arr, n - 1) - Enum.at(arr, 1) == n - 2

          if (left_consecutive && right_gap_two) || (right_consecutive && left_gap_two) do
            2
          else
            1
          end

        true ->
          n - max_in_window
      end

    [min_moves, max_moves]
  end

  defp move_i(i, arr, j, n) do
    if Enum.at(arr, j) - Enum.at(arr, i) >= n do
      move_i(i + 1, arr, j, n)
    else
      i
    end
  end
end
```
