# 1144. Decrease Elements To Make Array Zigzag

## Cpp

```cpp
class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        long long even = 0, odd = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int left = (i > 0) ? nums[i - 1] : INT_MAX;
            int right = (i + 1 < n) ? nums[i + 1] : INT_MAX;
            int minNeighbor = min(left, right);
            int need = max(0, nums[i] - (minNeighbor - 1));
            if (i % 2 == 0) even += need;
            else odd += need;
        }
        return (int)min(even, odd);
    }
};
```

## Java

```java
class Solution {
    public int movesToMakeZigzag(int[] nums) {
        int n = nums.length;
        long movesOddValley = 0;   // odd indices should be valleys
        long movesEvenValley = 0;  // even indices should be valleys

        for (int i = 1; i < n - 1; i++) {
            int left = nums[i - 1];
            int right = nums[i + 1];
            int minNeighbor = Math.min(left, right);
            int needed = Math.max(0, nums[i] - (minNeighbor - 1));

            if ((i & 1) == 0) { // even index
                movesEvenValley += needed;
            } else {
                movesOddValley += needed;
            }
        }

        return (int)Math.min(movesOddValley, movesEvenValley);
    }
}
```

## Python

```python
class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # pattern 0: even indices are valleys
        moves_even_valley = 0
        for i in range(0, n, 2):
            left = nums[i - 1] if i - 1 >= 0 else float('inf')
            right = nums[i + 1] if i + 1 < n else float('inf')
            target = min(left, right) - 1
            if nums[i] > target:
                moves_even_valley += nums[i] - target

        # pattern 1: odd indices are valleys
        moves_odd_valley = 0
        for i in range(1, n, 2):
            left = nums[i - 1]
            right = nums[i + 1] if i + 1 < n else float('inf')
            target = min(left, right) - 1
            if nums[i] > target:
                moves_odd_valley += nums[i] - target

        return min(moves_even_valley, moves_odd_valley)
```

## Python3

```python
from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)

        def calc(start_peak: bool) -> int:
            moves = 0
            for i in range(n):
                # Determine if this index should be a valley under the current pattern
                need_valley = (i % 2 == 0) ^ start_peak
                if not need_valley:
                    continue
                left = nums[i - 1] if i - 1 >= 0 else float('inf')
                right = nums[i + 1] if i + 1 < n else float('inf')
                min_neighbor = left if left < right else right
                target = min_neighbor - 1
                if nums[i] > target:
                    moves += nums[i] - target
            return moves

        return min(calc(True), calc(False))
```

## C

```c
#include <limits.h>

int movesToMakeZigzag(int* nums, int numsSize) {
    long long movesOddValley = 0;   // make odd indices valleys (even indices peaks)
    long long movesEvenValley = 0;  // make even indices valleys (odd indices peaks)

    for (int i = 0; i < numsSize; ++i) {
        int left  = (i > 0) ? nums[i - 1] : INT_MAX;
        int right = (i + 1 < numsSize) ? nums[i + 1] : INT_MAX;

        int minNeighbor = left < right ? left : right;
        if (minNeighbor == INT_MAX) continue; // single element, no moves needed

        int target = minNeighbor - 1;
        int need = nums[i] > target ? nums[i] - target : 0;

        if (i % 2 == 1)
            movesOddValley += need;   // odd index should be valley
        else
            movesEvenValley += need;  // even index should be valley
    }

    return (int)(movesOddValley < movesEvenValley ? movesOddValley : movesEvenValley);
}
```

## Csharp

```csharp
public class Solution {
    public int MovesToMakeZigzag(int[] nums) {
        long movesEvenValley = ComputeMoves(nums, true);
        long movesOddValley = ComputeMoves(nums, false);
        return (int)Math.Min(movesEvenValley, movesOddValley);
    }

    private long ComputeMoves(int[] nums, bool valleyAtEven) {
        int n = nums.Length;
        long moves = 0;
        for (int i = 0; i < n; i++) {
            bool isValley = ((i & 1) == 0) == valleyAtEven;
            if (!isValley) continue;

            int left = i > 0 ? nums[i - 1] : int.MaxValue;
            int right = i + 1 < n ? nums[i + 1] : int.MaxValue;
            int minNeighbor = Math.Min(left, right);
            int target = minNeighbor - 1; // must be strictly less
            if (nums[i] > target) {
                moves += nums[i] - target;
            }
        }
        return moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var movesToMakeZigzag = function(nums) {
    const n = nums.length;
    let movesEvenPeak = 0; // odd indices are valleys
    let movesOddPeak = 0;  // even indices are valleys

    // Pattern: even indices are peaks, so process odd positions as valleys
    for (let i = 1; i < n; i += 2) {
        const left = nums[i - 1];
        const right = i + 1 < n ? nums[i + 1] : Infinity;
        const minNeighbor = Math.min(left, right);
        if (nums[i] >= minNeighbor) {
            movesEvenPeak += nums[i] - minNeighbor + 1;
        }
    }

    // Pattern: odd indices are peaks, so process even positions as valleys
    for (let i = 0; i < n; i += 2) {
        const left = i > 0 ? nums[i - 1] : Infinity;
        const right = i + 1 < n ? nums[i + 1] : Infinity;
        const minNeighbor = Math.min(left, right);
        if (nums[i] >= minNeighbor) {
            movesOddPeak += nums[i] - minNeighbor + 1;
        }
    }

    return Math.min(movesEvenPeak, movesOddPeak);
};
```

## Typescript

```typescript
function movesToMakeZigzag(nums: number[]): number {
    const n = nums.length;
    let evenValleyMoves = 0; // make even indices valleys
    let oddValleyMoves = 0;  // make odd indices valleys

    for (let i = 0; i < n; ++i) {
        const left = i > 0 ? nums[i - 1] : Infinity;
        const right = i + 1 < n ? nums[i + 1] : Infinity;
        const minNeighbor = Math.min(left, right);
        const requiredMax = minNeighbor - 1;
        const dec = Math.max(0, nums[i] - requiredMax);

        if (i % 2 === 0) {
            evenValleyMoves += dec;
        } else {
            oddValleyMoves += dec;
        }
    }

    return Math.min(evenValleyMoves, oddValleyMoves);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function movesToMakeZigzag($nums) {
        $n = count($nums);
        $movesEvenPeak = 0; // even indices are peaks, odd are valleys
        $movesOddPeak = 0;  // odd indices are peaks, even are valleys

        for ($i = 0; $i < $n; $i++) {
            $left = $i > 0 ? $nums[$i - 1] : PHP_INT_MAX;
            $right = $i + 1 < $n ? $nums[$i + 1] : PHP_INT_MAX;
            $minNeighbor = min($left, $right);
            $required = $minNeighbor - 1; // max value allowed for a valley at i

            if ($i % 2 == 0) {
                // even index should be peak in movesOddPeak scenario,
                // so it must become a valley in movesEvenPeak scenario.
                $need = max(0, $nums[$i] - $required);
                $movesEvenPeak += $need;
            } else {
                // odd index should be peak in movesEvenPeak scenario,
                // so it must become a valley in movesOddPeak scenario.
                $need = max(0, $nums[$i] - $required);
                $movesOddPeak += $need;
            }
        }

        return min($movesEvenPeak, $movesOddPeak);
    }
}
```

## Swift

```swift
class Solution {
    func movesToMakeZigzag(_ nums: [Int]) -> Int {
        let n = nums.count
        var movesEvenValley = 0
        var movesOddValley = 0

        for i in 0..<n {
            var minNeighbor = Int.max
            if i > 0 { minNeighbor = min(minNeighbor, nums[i - 1]) }
            if i + 1 < n { minNeighbor = min(minNeighbor, nums[i + 1]) }

            if minNeighbor == Int.max { continue } // no neighbors

            let need = max(0, nums[i] - minNeighbor + 1)
            if i % 2 == 0 {
                movesEvenValley += need
            } else {
                movesOddValley += need
            }
        }

        return min(movesEvenValley, movesOddValley)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun movesToMakeZigzag(nums: IntArray): Int {
        val n = nums.size
        var movesEvenValley = 0L
        var movesOddValley = 0L

        for (i in 0 until n) {
            val left = if (i > 0) nums[i - 1] else Int.MAX_VALUE
            val right = if (i + 1 < n) nums[i + 1] else Int.MAX_VALUE
            val minNeighbor = kotlin.math.min(left, right)

            // Pattern: even indices are valleys
            if (i % 2 == 0 && nums[i] >= minNeighbor) {
                movesEvenValley += (nums[i] - (minNeighbor - 1)).toLong()
            }

            // Pattern: odd indices are valleys
            if (i % 2 == 1 && nums[i] >= minNeighbor) {
                movesOddValley += (nums[i] - (minNeighbor - 1)).toLong()
            }
        }

        return kotlin.math.min(movesEvenValley, movesOddValley).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int movesToMakeZigzag(List<int> nums) {
    int n = nums.length;
    int calc(int startParity) {
      int moves = 0;
      for (int i = startParity; i < n; i += 2) {
        int left = i > 0 ? nums[i - 1] : 1000000;
        int right = i + 1 < n ? nums[i + 1] : 1000000;
        int minNeighbor = left < right ? left : right;
        if (nums[i] >= minNeighbor) {
          moves += nums[i] - minNeighbor + 1;
        }
      }
      return moves;
    }

    int movesEvenValley = calc(0);
    int movesOddValley = calc(1);
    return movesEvenValley < movesOddValley ? movesEvenValley : movesOddValley;
  }
}
```

## Golang

```go
func movesToMakeZigzag(nums []int) int {
    n := len(nums)
    calc := func(start int) int {
        moves := 0
        for i := start; i < n; i += 2 {
            left, right := 2000, 2000
            if i > 0 {
                left = nums[i-1]
            }
            if i+1 < n {
                right = nums[i+1]
            }
            minNeighbor := left
            if right < minNeighbor {
                minNeighbor = right
            }
            target := minNeighbor - 1
            if nums[i] > target {
                moves += nums[i] - target
            }
        }
        return moves
    }

    evenValley := calc(0)
    oddValley := calc(1)

    if evenValley < oddValley {
        return evenValley
    }
    return oddValley
}
```

## Ruby

```ruby
def moves_to_make_zigzag(nums)
  n = nums.length
  moves_odd_valley = 0   # pattern: even indices are peaks, odd indices valleys
  moves_even_valley = 0  # pattern: odd indices are peaks, even indices valleys

  (0...n).each do |i|
    left = i > 0 ? nums[i - 1] : nil
    right = i + 1 < n ? nums[i + 1] : nil
    min_neighbor = [left, right].compact.min

    if i.even?
      # even index should be valley for the second pattern
      target = min_neighbor ? min_neighbor - 1 : nums[i]
      need = nums[i] - target
      moves_even_valley += need if need > 0
    else
      # odd index should be valley for the first pattern
      target = min_neighbor ? min_neighbor - 1 : nums[i]
      need = nums[i] - target
      moves_odd_valley += need if need > 0
    end
  end

  [moves_odd_valley, moves_even_valley].min
end
```

## Scala

```scala
object Solution {
    def movesToMakeZigzag(nums: Array[Int]): Int = {
        val n = nums.length
        var movesOddValley = 0   // make odd indices valleys (even peaks)
        var movesEvenValley = 0  // make even indices valleys (odd peaks)

        for (i <- 0 until n) {
            val left  = if (i > 0) nums(i - 1) else Int.MaxValue
            val right = if (i < n - 1) nums(i + 1) else Int.MaxValue
            val minNeighbor = Math.min(left, right)
            // moves needed to make nums[i] strictly less than its neighbors
            val need = Math.max(0, nums(i) - (minNeighbor - 1))
            if (i % 2 == 0) {
                movesEvenValley += need
            } else {
                movesOddValley += need
            }
        }

        Math.min(movesOddValley, movesEvenValley)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn moves_to_make_zigzag(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut moves_even_peak = 0i32; // odd indices need to be lowered
        let mut moves_odd_peak = 0i32;  // even indices need to be lowered

        for i in 0..n {
            let left = if i > 0 { nums[i - 1] } else { i32::MAX };
            let right = if i + 1 < n { nums[i + 1] } else { i32::MAX };
            let min_neighbor = left.min(right);
            // maximum allowed value for a valley position
            let target = min_neighbor - 1;

            if i % 2 == 0 {
                // even index: valley in the odd‑peak pattern
                if nums[i] > target {
                    moves_odd_peak += nums[i] - target;
                }
            } else {
                // odd index: valley in the even‑peak pattern
                if nums[i] > target {
                    moves_even_peak += nums[i] - target;
                }
            }
        }

        moves_even_peak.min(moves_odd_peak)
    }
}
```

## Racket

```racket
(define/contract (moves-to-make-zigzag nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((len (length nums))
         (INF 1000000000)
         (calc
          (lambda (p)
            (let loop ((i 0) (total 0))
              (if (>= i len)
                  total
                  (if (= (remainder i 2) p)
                      (let* ((left (if (> i 0) (list-ref nums (- i 1)) INF))
                             (right (if (< i (- len 1)) (list-ref nums (+ i 1)) INF))
                             (min-nei (if (< left right) left right))
                             (allowed (- min-nei 1))
                             (cur (list-ref nums i))
                             (need (if (> cur allowed) (- cur allowed) 0)))
                        (loop (+ i 1) (+ total need)))
                      (loop (+ i 1) total)))))))
    (min (calc 0) (calc 1))))
```

## Erlang

```erlang
-module(solution).
-export([moves_to_make_zigzag/1]).

-spec moves_to_make_zigzag(Nums :: [integer()]) -> integer().
moves_to_make_zigzag(Nums) ->
    MovesEvenPeak = calc_moves(Nums, 0),
    MovesOddPeak = calc_moves(Nums, 1),
    erlang:min(MovesEvenPeak, MovesOddPeak).

-spec calc_moves([integer()], integer()) -> integer().
calc_moves(Nums, PeakParity) ->
    Len = length(Nums),
    calc_loop(Nums, Len, PeakParity, 0, 0).

-spec calc_loop([integer()], integer(), integer(), integer(), integer()) -> integer().
calc_loop(_Nums, Len, _PeakParity, Index, Acc) when Index >= Len ->
    Acc;
calc_loop(Nums, Len, PeakParity, Index, Acc) ->
    case (Index rem 2) of
        PeakParity ->
            calc_loop(Nums, Len, PeakParity, Index + 1, Acc);
        _ ->
            Curr = lists:nth(Index + 1, Nums),
            Neighbors = get_neighbors(Nums, Len, Index),
            Needed =
                case Neighbors of
                    [] -> 0;
                    _ ->
                        MinN = lists:min(Neighbors),
                        Decrease = Curr - (MinN - 1),
                        if Decrease > 0 -> Decrease; true -> 0 end
                end,
            calc_loop(Nums, Len, PeakParity, Index + 1, Acc + Needed)
    end.

-spec get_neighbors([integer()], integer(), integer()) -> [integer()].
get_neighbors(Nums, Len, Index) ->
    Left = if Index > 0 -> [lists:nth(Index, Nums)]; true -> [] end,
    Right = if Index < Len - 1 -> [lists:nth(Index + 2, Nums)]; true -> [] end,
    Left ++ Right.
```

## Elixir

```elixir
defmodule Solution do
  @spec moves_to_make_zigzag(nums :: [integer]) :: integer
  def moves_to_make_zigzag(nums) do
    t = List.to_tuple(nums)
    n = tuple_size(t)

    sum_even_peaks =
      Enum.reduce(0..(n - 1), 0, fn i, acc ->
        if rem(i, 2) == 1 do
          left = if i > 0, do: elem(t, i - 1), else: nil
          right = if i < n - 1, do: elem(t, i + 1), else: nil

          min_neighbor =
            cond do
              left == nil -> right
              right == nil -> left
              true -> min(left, right)
            end

          val = elem(t, i)
          needed = max(0, val - min_neighbor + 1)
          acc + needed
        else
          acc
        end
      end)

    sum_odd_peaks =
      Enum.reduce(0..(n - 1), 0, fn i, acc ->
        if rem(i, 2) == 0 do
          left = if i > 0, do: elem(t, i - 1), else: nil
          right = if i < n - 1, do: elem(t, i + 1), else: nil

          min_neighbor =
            cond do
              left == nil -> right
              right == nil -> left
              true -> min(left, right)
            end

          val = elem(t, i)
          needed = max(0, val - min_neighbor + 1)
          acc + needed
        else
          acc
        end
      end)

    min(sum_even_peaks, sum_odd_peaks)
  end
end
```
