# 0801. Minimum Swaps To Make Sequences Increasing

## Cpp

```cpp
class Solution {
public:
    int minSwap(vector<int>& nums1, vector<int>& nums2) {
        const int n = nums1.size();
        const int INF = 1e9;
        int keep = 0;          // no swap at previous index
        int swap = 1;          // swapped at previous index
        
        for (int i = 1; i < n; ++i) {
            int newKeep = INF, newSwap = INF;
            
            bool cond1 = nums1[i] > nums1[i-1] && nums2[i] > nums2[i-1];
            bool cond2 = nums1[i] > nums2[i-1] && nums2[i] > nums1[i-1];
            
            if (cond1) {
                newKeep = min(newKeep, keep);          // no swap now, previous not swapped
                newSwap = min(newSwap, swap + 1);      // swap now, previous swapped
            }
            if (cond2) {
                newKeep = min(newKeep, swap);          // no swap now, previous swapped
                newSwap = min(newSwap, keep + 1);      // swap now, previous not swapped
            }
            
            keep = newKeep;
            swap = newSwap;
        }
        return min(keep, swap);
    }
};
```

## Java

```java
class Solution {
    public int minSwap(int[] nums1, int[] nums2) {
        int n = nums1.length;
        final int INF = 1_000_000_0; // sufficiently large
        int keepPrev = 0;   // no swap at i-1
        int swapPrev = 1;   // swapped at i-1

        for (int i = 1; i < n; i++) {
            int keepCurr = INF;
            int swapCurr = INF;

            boolean condKeep = nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1];
            boolean condSwap = nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1];

            if (condKeep) {
                // keep current without swap
                keepCurr = Math.min(keepCurr, keepPrev);
                // swap current if previous was swapped
                swapCurr = Math.min(swapCurr, swapPrev + 1);
            }
            if (condSwap) {
                // keep current without swap but previous was swapped
                keepCurr = Math.min(keepCurr, swapPrev);
                // swap current while previous not swapped
                swapCurr = Math.min(swapCurr, keepPrev + 1);
            }

            keepPrev = keepCurr;
            swapPrev = swapCurr;
        }
        return Math.min(keepPrev, swapPrev);
    }
}
```

## Python

```python
class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        # keep: no swap at i, swap: swapped at i
        keep = 0          # for i = -1 (virtual), zero swaps and not swapped
        swap = 1          # if we swap the first pair
        for i in range(1, n):
            new_keep = new_swap = float('inf')
            # Case 1: both sequences are increasing without swapping at i
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                new_keep = min(new_keep, keep)          # no swap now, previous also not swapped
                new_swap = min(new_swap, swap + 1)      # swap now, previous was swapped
            # Case 2: increasing if we cross swap between i and i-1
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                new_keep = min(new_keep, swap)          # no swap now, previous was swapped
                new_swap = min(new_swap, keep + 1)      # swap now, previous not swapped
            keep, swap = new_keep, new_swap
        return int(min(keep, swap))
```

## Python3

```python
from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        INF = 10**9
        keep = 0          # no swap at previous index
        swap = 1          # swapped at previous index
        
        for i in range(1, n):
            new_keep = INF
            new_swap = INF
            
            # Case 1: both sequences are increasing without swapping at i
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                new_keep = min(new_keep, keep)          # no swap now, previous also not swapped
                new_swap = min(new_swap, swap + 1)      # swap now, previous was swapped
            
            # Case 2: increasing if we cross swap at i
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                new_keep = min(new_keep, swap)          # no swap now, previous was swapped
                new_swap = min(new_swap, keep + 1)      # swap now, previous not swapped
            
            keep, swap = new_keep, new_swap
        
        return min(keep, swap)
```

## C

```c
int minSwap(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    const int INF = 1000000000;
    int keep = 0;          // no swap at index 0
    int swapped = 1;       // swap at index 0

    for (int i = 1; i < nums1Size; ++i) {
        int newKeep = INF, newSwap = INF;

        if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
            // both sequences stay increasing without swapping at i
            if (keep < newKeep) newKeep = keep;
            if (swapped + 1 < newSwap) newSwap = swapped + 1;
        }
        if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
            // swapping at i makes sequences increasing
            if (swapped < newKeep) newKeep = swapped;          // no swap now, previous was swapped
            if (keep + 1 < newSwap) newSwap = keep + 1;        // swap now, previous not swapped
        }

        keep = newKeep;
        swapped = newSwap;
    }
    return keep < swapped ? keep : swapped;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSwap(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        const int INF = int.MaxValue / 2;
        int keep = 0;   // no swap at previous index
        int swap = 1;   // swapped at previous index

        for (int i = 1; i < n; i++) {
            int newKeep = INF;
            int newSwap = INF;

            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                // keep current without swap
                newKeep = Math.Min(newKeep, keep);
                // swap current, previous also swapped
                newSwap = Math.Min(newSwap, swap + 1);
            }

            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                // keep current without swap, previous was swapped
                newKeep = Math.Min(newKeep, swap);
                // swap current, previous not swapped
                newSwap = Math.Min(newSwap, keep + 1);
            }

            keep = newKeep;
            swap = newSwap;
        }

        return Math.Min(keep, swap);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minSwap = function(nums1, nums2) {
    const n = nums1.length;
    let keep = 0;          // no swap at i-1
    let swap = 1;          // swapped at i-1

    for (let i = 1; i < n; ++i) {
        let newKeep = Number.MAX_SAFE_INTEGER;
        let newSwap = Number.MAX_SAFE_INTEGER;

        const aCurr = nums1[i], bCurr = nums2[i];
        const aPrev = nums1[i - 1], bPrev = nums2[i - 1];

        // Case 1: both sequences are increasing without swapping at i
        if (aCurr > aPrev && bCurr > bPrev) {
            newKeep = Math.min(newKeep, keep);
            newSwap = Math.min(newSwap, swap + 1);
        }

        // Case 2: increasing if we swap one of the pairs
        if (aCurr > bPrev && bCurr > aPrev) {
            newKeep = Math.min(newKeep, swap);
            newSwap = Math.min(newSwap, keep + 1);
        }

        keep = newKeep;
        swap = newSwap;
    }

    return Math.min(keep, swap);
};
```

## Typescript

```typescript
function minSwap(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    let keep = 0; // no swap at i
    let swap = 1; // swapped at i

    for (let i = 1; i < n; i++) {
        let newKeep = Number.MAX_SAFE_INTEGER;
        let newSwap = Number.MAX_SAFE_INTEGER;

        if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
            // keep both current and previous as is
            newKeep = Math.min(newKeep, keep);
            // swap both current and previous
            newSwap = Math.min(newSwap, swap + 1);
        }

        if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
            // keep current, but previous was swapped
            newKeep = Math.min(newKeep, swap);
            // swap current, previous not swapped
            newSwap = Math.min(newSwap, keep + 1);
        }

        keep = newKeep;
        swap = newSwap;
    }

    return Math.min(keep, swap);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minSwap($nums1, $nums2) {
        $n = count($nums1);
        $dp0 = 0; // no swap at previous index
        $dp1 = 1; // swap at previous index
        for ($i = 1; $i < $n; $i++) {
            $ndp0 = PHP_INT_MAX;
            $ndp1 = PHP_INT_MAX;
            if ($nums1[$i] > $nums1[$i - 1] && $nums2[$i] > $nums2[$i - 1]) {
                // keep current without swap, previous also not swapped
                $ndp0 = min($ndp0, $dp0);
                // swap current, previous was swapped
                $ndp1 = min($ndp1, $dp1 + 1);
            }
            if ($nums1[$i] > $nums2[$i - 1] && $nums2[$i] > $nums1[$i - 1]) {
                // keep current without swap, previous was swapped
                $ndp0 = min($ndp0, $dp1);
                // swap current, previous not swapped
                $ndp1 = min($ndp1, $dp0 + 1);
            }
            $dp0 = $ndp0;
            $dp1 = $ndp1;
        }
        return min($dp0, $dp1);
    }
}
```

## Swift

```swift
class Solution {
    func minSwap(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var keep = 0          // no swap at previous index
        var swap = 1          // swapped at previous index
        
        for i in 1..<n {
            var newKeep = Int.max
            var newSwap = Int.max
            
            if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1] {
                newKeep = min(newKeep, keep)
                newSwap = min(newSwap, swap + 1)
            }
            if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1] {
                newKeep = min(newKeep, swap)
                newSwap = min(newSwap, keep + 1)
            }
            
            keep = newKeep
            swap = newSwap
        }
        
        return min(keep, swap)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwap(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        var keep = 0          // no swap at previous index
        var swap = 1          // swapped at previous index
        for (i in 1 until n) {
            var newKeep = Int.MAX_VALUE
            var newSwap = Int.MAX_VALUE
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                newKeep = minOf(newKeep, keep)
                newSwap = minOf(newSwap, swap + 1)
            }
            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                newKeep = minOf(newKeep, swap)
                newSwap = minOf(newSwap, keep + 1)
            }
            keep = newKeep
            swap = newSwap
        }
        return minOf(keep, swap)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minSwap(List<int> nums1, List<int> nums2) {
    const int INF = 1 << 30;
    int n = nums1.length;
    int keep = 0;
    int swap = 1;
    for (int i = 1; i < n; ++i) {
      int curKeep = INF;
      int curSwap = INF;
      if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
        curKeep = keep;
        curSwap = swap + 1;
      }
      if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
        curKeep = min(curKeep, swap);
        curSwap = min(curSwap, keep + 1);
      }
      keep = curKeep;
      swap = curSwap;
    }
    return min(keep, swap);
  }
}
```

## Golang

```go
func minSwap(nums1 []int, nums2 []int) int {
    const inf = int(1 << 60)
    n := len(nums1)
    keepPrev, swapPrev := 0, 1

    for i := 1; i < n; i++ {
        curKeep, curSwap := inf, inf

        // No swap at i
        if nums1[i] > nums1[i-1] && nums2[i] > nums2[i-1] {
            if keepPrev < curKeep {
                curKeep = keepPrev
            }
            if swapPrev+1 < curSwap {
                curSwap = swapPrev + 1
            }
        }

        // Swap at i
        if nums1[i] > nums2[i-1] && nums2[i] > nums1[i-1] {
            if swapPrev < curKeep {
                curKeep = swapPrev
            }
            if keepPrev+1 < curSwap {
                curSwap = keepPrev + 1
            }
        }

        keepPrev, swapPrev = curKeep, curSwap
    }

    if keepPrev < swapPrev {
        return keepPrev
    }
    return swapPrev
}
```

## Ruby

```ruby
def min_swap(nums1, nums2)
  n = nums1.length
  dp0 = 0          # no swap at previous index
  dp1 = 1          # swap at previous index
  (1...n).each do |i|
    new_dp0 = Float::INFINITY
    new_dp1 = Float::INFINITY

    if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]
      new_dp0 = [new_dp0, dp0].min
      new_dp1 = [new_dp1, dp1 + 1].min
    end

    if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]
      new_dp0 = [new_dp0, dp1].min
      new_dp1 = [new_dp1, dp0 + 1].min
    end

    dp0, dp1 = new_dp0, new_dp1
  end
  [dp0, dp1].min
end
```

## Scala

```scala
object Solution {
    def minSwap(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        var keepPrev = 0          // no swap at previous index
        var swapPrev = 1          // swapped at previous index (swap first element)
        for (i <- 1 until n) {
            var keepCurr = Int.MaxValue
            var swapCurr = Int.MaxValue
            if (nums1(i) > nums1(i - 1) && nums2(i) > nums2(i - 1)) {
                keepCurr = math.min(keepCurr, keepPrev)
                swapCurr = math.min(swapCurr, swapPrev + 1)
            }
            if (nums1(i) > nums2(i - 1) && nums2(i) > nums1(i - 1)) {
                keepCurr = math.min(keepCurr, swapPrev)
                swapCurr = math.min(swapCurr, keepPrev + 1)
            }
            keepPrev = keepCurr
            swapPrev = swapCurr
        }
        math.min(keepPrev, swapPrev)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swap(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        const INF: i32 = i32::MAX / 2;
        let mut keep: i32 = 0; // no swap at previous index
        let mut swap: i32 = 1; // swapped at previous index

        for i in 1..n {
            let mut new_keep = INF;
            let mut new_swap = INF;

            if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1] {
                new_keep = new_keep.min(keep);
                new_swap = new_swap.min(swap + 1);
            }
            if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1] {
                new_keep = new_keep.min(swap);
                new_swap = new_swap.min(keep + 1);
            }

            keep = new_keep;
            swap = new_swap;
        }

        std::cmp::min(keep, swap)
    }
}
```

## Racket

```racket
(define/contract (min-swap nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length nums1))
         (v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (inf 1000000000) ; sufficiently large
         (dp0 0)          ; no swap at previous index
         (dp1 1))         ; swapped at previous index
    (for ([i (in-range 1 n)])
      (let ((cur0 inf)
            (cur1 inf))
        ;; case: keep order without swapping i
        (when (and (< (vector-ref v1 (- i 1)) (vector-ref v1 i))
                   (< (vector-ref v2 (- i 1)) (vector-ref v2 i)))
          (set! cur0 (min cur0 dp0))
          (set! cur1 (min cur1 (+ dp1 1))))
        ;; case: swap at i (or not) crossing previous state
        (when (and (< (vector-ref v1 (- i 1)) (vector-ref v2 i))
                   (< (vector-ref v2 (- i 1)) (vector-ref v1 i)))
          (set! cur0 (min cur0 dp1))
          (set! cur1 (min cur1 (+ dp0 1))))
        (set! dp0 cur0)
        (set! dp1 cur1)))
    (min dp0 dp1)))
```

## Erlang

```erlang
-module(solution).
-export([min_swap/2]).

-spec min_swap(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_swap(Nums1, Nums2) ->
    case lists:zip(Nums1, Nums2) of
        [] -> 0;
        [{A0,B0}|Rest] ->
            loop(Rest, A0, B0, 0, 1)
    end.

loop([], _PrevA, _PrevB, Keep, Swap) ->
    if Keep =< Swap -> Keep; true -> Swap end;
loop([{Ai,Bi}|Rest], PrevA, PrevB, KeepPrev, SwapPrev) ->
    Inf = 1 bsl 30,
    Cond1 = (Ai > PrevA) andalso (Bi > PrevB),
    Cond2 = (Ai > PrevB) andalso (Bi > PrevA),
    Cond3 = (Bi > PrevA) andalso (Ai > PrevB),
    Cond4 = (Bi > PrevB) andalso (Ai > PrevA),

    KeepNew0 = if Cond1 -> KeepPrev; true -> Inf end,
    KeepNew  = if Cond2 -> erlang:min(KeepNew0, SwapPrev); true -> KeepNew0 end,

    SwapNew0 = if Cond3 -> KeepPrev + 1; true -> Inf end,
    SwapNew  = if Cond4 -> erlang:min(SwapNew0, SwapPrev + 1); true -> SwapNew0 end,

    loop(Rest, Ai, Bi, KeepNew, SwapNew).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swap(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_swap([a0 | rest_a] = _nums1, [b0 | rest_b] = _nums2) do
    # initial states: no swap at first index -> 0 swaps, swap at first index -> 1 swap
    dp0 = 0
    dp1 = 1
    do_min_swap(rest_a, rest_b, a0, b0, dp0, dp1)
  end

  defp do_min_swap([], [], _prev_a, _prev_b, dp0, dp1) do
    min(dp0, dp1)
  end

  defp do_min_swap([a | as], [b | bs], prev_a, prev_b, dp0, dp1) do
    inf = 1_000_000_000
    ndp0 = inf
    ndp1 = inf

    if a > prev_a and b > prev_b do
      ndp0 = min(ndp0, dp0)
      ndp1 = min(ndp1, dp1 + 1)
    end

    if a > prev_b and b > prev_a do
      ndp0 = min(ndp0, dp1)
      ndp1 = min(ndp1, dp0 + 1)
    end

    do_min_swap(as, bs, a, b, ndp0, ndp1)
  end
end
```
