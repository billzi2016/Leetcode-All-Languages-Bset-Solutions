# 3219. Minimum Cost for Cutting Cake II

## Cpp

```cpp
class Solution {
public:
    long long minimumCost(int m, int n, std::vector<int>& horizontalCut, std::vector<int>& verticalCut) {
        std::sort(horizontalCut.begin(), horizontalCut.end(), std::greater<int>());
        std::sort(verticalCut.begin(), verticalCut.end(), std::greater<int>());
        
        long long total = 0;
        long long hSegments = 1; // number of vertical pieces (affected by vertical cuts)
        long long vSegments = 1; // number of horizontal pieces (affected by horizontal cuts)
        size_t i = 0, j = 0;
        while (i < horizontalCut.size() && j < verticalCut.size()) {
            if (horizontalCut[i] > verticalCut[j]) {
                total += static_cast<long long>(horizontalCut[i]) * vSegments;
                ++hSegments;
                ++i;
            } else {
                total += static_cast<long long>(verticalCut[j]) * hSegments;
                ++vSegments;
                ++j;
            }
        }
        while (i < horizontalCut.size()) {
            total += static_cast<long long>(horizontalCut[i]) * vSegments;
            ++i;
        }
        while (j < verticalCut.size()) {
            total += static_cast<long long>(verticalCut[j]) * hSegments;
            ++j;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public long minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        // Sort cuts in descending order
        java.util.Arrays.sort(horizontalCut);
        java.util.Arrays.sort(verticalCut);
        int h = horizontalCut.length - 1;
        int v = verticalCut.length - 1;

        long total = 0L;
        long horizSegments = 1; // number of current vertical pieces
        long vertSegments = 1;  // number of current horizontal pieces

        while (h >= 0 && v >= 0) {
            if (horizontalCut[h] > verticalCut[v]) {
                total += (long) horizontalCut[h] * vertSegments;
                horizSegments++;
                h--;
            } else {
                total += (long) verticalCut[v] * horizSegments;
                vertSegments++;
                v--;
            }
        }

        while (h >= 0) {
            total += (long) horizontalCut[h] * vertSegments;
            h--;
        }

        while (v >= 0) {
            total += (long) verticalCut[v] * horizSegments;
            v--;
        }

        return total;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        # Sort cuts in descending order to apply greedy choice
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        h_parts, v_parts = 1, 1  # current number of pieces along each dimension
        i = j = 0
        total = 0

        while i < len(horizontalCut) and j < len(verticalCut):
            if horizontalCut[i] > verticalCut[j]:
                total = (total + horizontalCut[i] * v_parts) % MOD
                h_parts += 1
                i += 1
            else:
                total = (total + verticalCut[j] * h_parts) % MOD
                v_parts += 1
                j += 1

        while i < len(horizontalCut):
            total = (total + horizontalCut[i] * v_parts) % MOD
            i += 1

        while j < len(verticalCut):
            total = (total + verticalCut[j] * h_parts) % MOD
            j += 1

        return total % MOD
```

## Python3

```python
from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        MOD = 10**9 + 7
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        h_parts = 1  # number of horizontal pieces currently
        v_parts = 1  # number of vertical pieces currently
        i = j = 0
        total = 0

        while i < len(horizontalCut) and j < len(verticalCut):
            if horizontalCut[i] > verticalCut[j]:
                total = (total + horizontalCut[i] * v_parts) % MOD
                h_parts += 1
                i += 1
            else:
                total = (total + verticalCut[j] * h_parts) % MOD
                v_parts += 1
                j += 1

        while i < len(horizontalCut):
            total = (total + horizontalCut[i] * v_parts) % MOD
            i += 1

        while j < len(verticalCut):
            total = (total + verticalCut[j] * h_parts) % MOD
            j += 1

        return total % MOD
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return vb - va; // descending order
}

long long minimumCost(int m, int n, int* horizontalCut, int horizontalCutSize,
                      int* verticalCut, int verticalCutSize) {
    const long long MOD = 1000000007LL;

    qsort(horizontalCut, (size_t)horizontalCutSize, sizeof(int), cmp_desc);
    qsort(verticalCut, (size_t)verticalCutSize, sizeof(int), cmp_desc);

    long long result = 0;
    long long hPieces = 1; // number of vertical segments created by horizontal cuts
    long long vPieces = 1; // number of horizontal segments created by vertical cuts

    int i = 0, j = 0;
    while (i < horizontalCutSize && j < verticalCutSize) {
        if (horizontalCut[i] > verticalCut[j]) {
            result = (result + ((long long)horizontalCut[i] * vPieces) % MOD) % MOD;
            hPieces++;
            i++;
        } else {
            result = (result + ((long long)verticalCut[j] * hPieces) % MOD) % MOD;
            vPieces++;
            j++;
        }
    }

    while (i < horizontalCutSize) {
        result = (result + ((long long)horizontalCut[i] * vPieces) % MOD) % MOD;
        i++;
    }

    while (j < verticalCutSize) {
        result = (result + ((long long)verticalCut[j] * hPieces) % MOD) % MOD;
        j++;
    }

    return result % MOD;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    public long MinimumCost(int m, int n, int[] horizontalCut, int[] verticalCut)
    {
        Array.Sort(horizontalCut);
        Array.Reverse(horizontalCut);
        Array.Sort(verticalCut);
        Array.Reverse(verticalCut);

        long hSegments = 1, vSegments = 1;
        long result = 0;
        int i = 0, j = 0;

        while (i < horizontalCut.Length && j < verticalCut.Length)
        {
            if (horizontalCut[i] >= verticalCut[j])
            {
                result = (result + ((long)horizontalCut[i] * vSegments) % MOD) % MOD;
                hSegments++;
                i++;
            }
            else
            {
                result = (result + ((long)verticalCut[j] * hSegments) % MOD) % MOD;
                vSegments++;
                j++;
            }
        }

        while (i < horizontalCut.Length)
        {
            result = (result + ((long)horizontalCut[i] * vSegments) % MOD) % MOD;
            i++;
        }

        while (j < verticalCut.Length)
        {
            result = (result + ((long)verticalCut[j] * hSegments) % MOD) % MOD;
            j++;
        }

        return result % MOD;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[]} horizontalCut
 * @param {number[]} verticalCut
 * @return {number}
 */
var minimumCost = function(m, n, horizontalCut, verticalCut) {
    // Sort cuts in descending order to apply greedy highest-cost first
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);
    
    let hIdx = 0, vIdx = 0;
    let horizPieces = 1; // number of current horizontal segments
    let vertPieces = 1;  // number of current vertical segments
    let total = 0;
    
    while (hIdx < horizontalCut.length && vIdx < verticalCut.length) {
        if (horizontalCut[hIdx] >= verticalCut[vIdx]) {
            total += horizontalCut[hIdx] * vertPieces;
            horizPieces++;
            hIdx++;
        } else {
            total += verticalCut[vIdx] * horizPieces;
            vertPieces++;
            vIdx++;
        }
    }
    
    // Process any remaining horizontal cuts
    while (hIdx < horizontalCut.length) {
        total += horizontalCut[hIdx] * vertPieces;
        hIdx++;
    }
    
    // Process any remaining vertical cuts
    while (vIdx < verticalCut.length) {
        total += verticalCut[vIdx] * horizPieces;
        vIdx++;
    }
    
    return total;
};
```

## Typescript

```typescript
function minimumCost(m: number, n: number, horizontalCut: number[], verticalCut: number[]): number {
    const MOD = 1_000_000_007;
    // sort in descending order
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);
    
    let hIdx = 0, vIdx = 0;
    let hSegments = 1; // number of current horizontal pieces
    let vSegments = 1; // number of current vertical pieces
    let total = 0;
    
    while (hIdx < horizontalCut.length && vIdx < verticalCut.length) {
        if (horizontalCut[hIdx] > verticalCut[vIdx]) {
            total = (total + horizontalCut[hIdx] * vSegments) % MOD;
            hSegments++;
            hIdx++;
        } else {
            total = (total + verticalCut[vIdx] * hSegments) % MOD;
            vSegments++;
            vIdx++;
        }
    }
    
    while (hIdx < horizontalCut.length) {
        total = (total + horizontalCut[hIdx] * vSegments) % MOD;
        hIdx++;
    }
    
    while (vIdx < verticalCut.length) {
        total = (total + verticalCut[vIdx] * hSegments) % MOD;
        vIdx++;
    }
    
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[] $horizontalCut
     * @param Integer[] $verticalCut
     * @return Integer
     */
    function minimumCost($m, $n, $horizontalCut, $verticalCut) {
        // Sort cuts in descending order to apply greedy choice
        rsort($horizontalCut);
        rsort($verticalCut);

        $hIdx = 0; // index for horizontal cuts
        $vIdx = 0; // index for vertical cuts

        $horizontalPieces = 1; // number of current horizontal segments
        $verticalPieces   = 1; // number of current vertical segments

        $totalCost = 0;

        while ($hIdx < count($horizontalCut) && $vIdx < count($verticalCut)) {
            if ($horizontalCut[$hIdx] >= $verticalCut[$vIdx]) {
                // Perform horizontal cut
                $totalCost += $horizontalCut[$hIdx] * $verticalPieces;
                $horizontalPieces++;
                $hIdx++;
            } else {
                // Perform vertical cut
                $totalCost += $verticalCut[$vIdx] * $horizontalPieces;
                $verticalPieces++;
                $vIdx++;
            }
        }

        // Process any remaining horizontal cuts
        while ($hIdx < count($horizontalCut)) {
            $totalCost += $horizontalCut[$hIdx] * $verticalPieces;
            $hIdx++;
        }

        // Process any remaining vertical cuts
        while ($vIdx < count($verticalCut)) {
            $totalCost += $verticalCut[$vIdx] * $horizontalPieces;
            $vIdx++;
        }

        return $totalCost;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ m: Int, _ n: Int, _ horizontalCut: [Int], _ verticalCut: [Int]) -> Int {
        let MOD = 1_000_000_007
        var hCuts = horizontalCut.sorted(by: >)
        var vCuts = verticalCut.sorted(by: >)
        
        var i = 0, j = 0
        var hPieces = 1   // number of horizontal pieces currently
        var vPieces = 1   // number of vertical pieces currently
        var result: Int64 = 0
        
        while i < hCuts.count || j < vCuts.count {
            if j == vCuts.count || (i < hCuts.count && hCuts[i] >= vCuts[j]) {
                // perform a horizontal cut
                let cost = Int64(hCuts[i])
                result += cost * Int64(vPieces)
                result %= Int64(MOD)
                hPieces += 1
                i += 1
            } else {
                // perform a vertical cut
                let cost = Int64(vCuts[j])
                result += cost * Int64(hPieces)
                result %= Int64(MOD)
                vPieces += 1
                j += 1
            }
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(m: Int, n: Int, horizontalCut: IntArray, verticalCut: IntArray): Long {
        val h = horizontalCut.sortedArrayDescending()
        val v = verticalCut.sortedArrayDescending()
        var i = 0
        var j = 0
        var hSegments = 1L
        var vSegments = 1L
        var total = 0L
        while (i < h.size && j < v.size) {
            if (h[i] > v[j]) {
                total += h[i].toLong() * vSegments
                hSegments++
                i++
            } else {
                total += v[j].toLong() * hSegments
                vSegments++
                j++
            }
        }
        while (i < h.size) {
            total += h[i].toLong() * vSegments
            i++
        }
        while (j < v.size) {
            total += v[j].toLong() * hSegments
            j++
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(int m, int n, List<int> horizontalCut, List<int> verticalCut) {
    // Sort cuts in descending order to apply greedy approach
    horizontalCut.sort((a, b) => b.compareTo(a));
    verticalCut.sort((a, b) => b.compareTo(a));

    int hIdx = 0;
    int vIdx = 0;
    int hSegments = 1; // number of current horizontal pieces
    int vSegments = 1; // number of current vertical pieces

    int totalCost = 0;

    while (hIdx < horizontalCut.length && vIdx < verticalCut.length) {
      if (horizontalCut[hIdx] > verticalCut[vIdx]) {
        totalCost += horizontalCut[hIdx] * vSegments;
        hSegments++;
        hIdx++;
      } else {
        totalCost += verticalCut[vIdx] * hSegments;
        vSegments++;
        vIdx++;
      }
    }

    while (hIdx < horizontalCut.length) {
      totalCost += horizontalCut[hIdx] * vSegments;
      hSegments++;
      hIdx++;
    }

    while (vIdx < verticalCut.length) {
      totalCost += verticalCut[vIdx] * hSegments;
      vSegments++;
      vIdx++;
    }

    return totalCost;
  }
}
```

## Golang

```go
package main

import "sort"

func minimumCost(m int, n int, horizontalCut []int, verticalCut []int) int64 {
	sort.Slice(horizontalCut, func(i, j int) bool { return horizontalCut[i] > horizontalCut[j] })
	sort.Slice(verticalCut, func(i, j int) bool { return verticalCut[i] > verticalCut[j] })

	hIdx, vIdx := 0, 0
	hSegments, vSegments := 1, 1
	var total int64

	for hIdx < len(horizontalCut) && vIdx < len(verticalCut) {
		if horizontalCut[hIdx] > verticalCut[vIdx] {
			total += int64(horizontalCut[hIdx]) * int64(vSegments)
			hSegments++
			hIdx++
		} else {
			total += int64(verticalCut[vIdx]) * int64(hSegments)
			vSegments++
			vIdx++
		}
	}

	for hIdx < len(horizontalCut) {
		total += int64(horizontalCut[hIdx]) * int64(vSegments)
		hIdx++
	}

	for vIdx < len(verticalCut) {
		total += int64(verticalCut[vIdx]) * int64(hSegments)
		vIdx++
	}

	return total
}
```

## Ruby

```ruby
def minimum_cost(m, n, horizontal_cut, vertical_cut)
  horizontal_cut.sort!.reverse!
  vertical_cut.sort!.reverse!

  h_segments = 1
  v_segments = 1
  i = 0
  j = 0
  total = 0

  while i < horizontal_cut.length && j < vertical_cut.length
    if horizontal_cut[i] >= vertical_cut[j]
      total += horizontal_cut[i] * v_segments
      h_segments += 1
      i += 1
    else
      total += vertical_cut[j] * h_segments
      v_segments += 1
      j += 1
    end
  end

  while i < horizontal_cut.length
    total += horizontal_cut[i] * v_segments
    i += 1
  end

  while j < vertical_cut.length
    total += vertical_cut[j] * h_segments
    j += 1
  end

  total
end
```

## Scala

```scala
object Solution {
    def minimumCost(m: Int, n: Int, horizontalCut: Array[Int], verticalCut: Array[Int]): Long = {
        val h = horizontalCut.sorted(Ordering[Int].reverse)
        val v = verticalCut.sorted(Ordering[Int].reverse)

        var i = 0
        var j = 0
        var hSeg = 1L
        var vSeg = 1L
        var total = 0L

        while (i < h.length && j < v.length) {
            if (h(i) > v(j)) {
                total += h(i).toLong * vSeg
                hSeg += 1
                i += 1
            } else {
                total += v(j).toLong * hSeg
                vSeg += 1
                j += 1
            }
        }

        while (i < h.length) {
            total += h(i).toLong * vSeg
            i += 1
        }

        while (j < v.length) {
            total += v(j).toLong * hSeg
            j += 1
        }

        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_cost(m: i32, n: i32, horizontal_cut: Vec<i32>, vertical_cut: Vec<i32>) -> i64 {
        let mut h = horizontal_cut;
        let mut v = vertical_cut;
        h.sort_unstable_by(|a, b| b.cmp(a));
        v.sort_unstable_by(|a, b| b.cmp(a));

        let mut i = 0usize;
        let mut j = 0usize;
        let mut horiz_segments: i64 = 1;
        let mut vert_segments: i64 = 1;
        let mut total: i64 = 0;

        while i < h.len() && j < v.len() {
            if h[i] > v[j] {
                total += (h[i] as i64) * vert_segments;
                horiz_segments += 1;
                i += 1;
            } else {
                total += (v[j] as i64) * horiz_segments;
                vert_segments += 1;
                j += 1;
            }
        }

        while i < h.len() {
            total += (h[i] as i64) * vert_segments;
            i += 1;
        }

        while j < v.len() {
            total += (v[j] as i64) * horiz_segments;
            j += 1;
        }

        total
    }
}
```

## Racket

```racket
(define/contract (minimum-cost m n horizontalCut verticalCut)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((h-sorted (sort horizontalCut >))
         (v-sorted (sort verticalCut >))
         (hlen (length h-sorted))
         (vlen (length v-sorted)))
    (let loop ((i 0) (j 0)
               (h-pieces 1) (v-pieces 1)
               (total 0))
      (cond
        [(and (= i hlen) (= j vlen)) total]
        [(= i hlen)
         (let* ((cost (list-ref v-sorted j)))
           (loop i (+ j 1) h-pieces (+ v-pieces 1)
                 (+ total (* cost h-pieces))))]
        [(= j vlen)
         (let* ((cost (list-ref h-sorted i)))
           (loop (+ i 1) j (+ h-pieces 1) v-pieces
                 (+ total (* cost v-pieces))))]
        [else
         (let ((h-cost (list-ref h-sorted i))
               (v-cost (list-ref v-sorted j)))
           (if (> h-cost v-cost)
               (loop (+ i 1) j (+ h-pieces 1) v-pieces
                     (+ total (* h-cost v-pieces)))
               (loop i (+ j 1) h-pieces (+ v-pieces 1)
                     (+ total (* v-cost h-pieces)))))]))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_cost/4]).

-spec minimum_cost(M :: integer(), N :: integer(), HorizontalCut :: [integer()], VerticalCut :: [integer()]) -> integer().
minimum_cost(_M, _N, HorizontalCut, VerticalCut) ->
    HSorted = lists:sort(fun(A, B) -> A > B end, HorizontalCut),
    VSorted = lists:sort(fun(A, B) -> A > B end, VerticalCut),
    go(HSorted, VSorted, 1, 1, 0).

go([], [], _HSeg, _VSeg, Acc) ->
    Acc;
go([], [V | Vs], HSeg, VSeg, Acc) ->
    NewAcc = Acc + V * HSeg,
    go([], Vs, HSeg, VSeg + 1, NewAcc);
go([H | Hs], [], HSeg, VSeg, Acc) ->
    NewAcc = Acc + H * VSeg,
    go(Hs, [], HSeg + 1, VSeg, NewAcc);
go([H | Hs] = HList, [V | Vs] = VList, HSeg, VSeg, Acc) ->
    if
        H >= V ->
            NewAcc = Acc + H * VSeg,
            go(Hs, VList, HSeg + 1, VSeg, NewAcc);
        true ->
            NewAcc = Acc + V * HSeg,
            go(HList, Vs, HSeg, VSeg + 1, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(m :: integer, n :: integer, horizontal_cut :: [integer], vertical_cut :: [integer]) :: integer
  def minimum_cost(_m, _n, horizontal_cut, vertical_cut) do
    h = Enum.sort(horizontal_cut, &>=/2)
    v = Enum.sort(vertical_cut, &>=/2)

    hl = length(h)
    vl = length(v)

    rec = fn rec_fun, i, j, h_seg, v_seg, total ->
      cond do
        i < hl and j < vl ->
          hc = Enum.at(h, i)
          vc = Enum.at(v, j)

          if hc > vc do
            rec_fun.(rec_fun, i + 1, j, h_seg + 1, v_seg, total + hc * v_seg)
          else
            rec_fun.(rec_fun, i, j + 1, h_seg, v_seg + 1, total + vc * h_seg)
          end

        i < hl ->
          hc = Enum.at(h, i)
          rec_fun.(rec_fun, i + 1, j, h_seg + 1, v_seg, total + hc * v_seg)

        j < vl ->
          vc = Enum.at(v, j)
          rec_fun.(rec_fun, i, j + 1, h_seg, v_seg + 1, total + vc * h_seg)

        true ->
          total
      end
    end

    rec.(rec, 0, 0, 1, 1, 0)
  end
end
```
