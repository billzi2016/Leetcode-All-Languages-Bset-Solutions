# 3218. Minimum Cost for Cutting Cake I

## Cpp

```cpp
class Solution {
public:
    int minimumCost(int m, int n, vector<int>& horizontalCut, vector<int>& verticalCut) {
        sort(horizontalCut.begin(), horizontalCut.end(), greater<int>());
        sort(verticalCut.begin(), verticalCut.end(), greater<int>());
        long long total = 0;
        int hPieces = 1, vPieces = 1;
        size_t i = 0, j = 0;
        while (i < horizontalCut.size() || j < verticalCut.size()) {
            if (j == verticalCut.size() || (i < horizontalCut.size() && horizontalCut[i] > verticalCut[j])) {
                total += (long long)horizontalCut[i] * vPieces;
                ++hPieces;
                ++i;
            } else {
                total += (long long)verticalCut[j] * hPieces;
                ++vPieces;
                ++j;
            }
        }
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    public int minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        java.util.Arrays.sort(horizontalCut);
        java.util.Arrays.sort(verticalCut);
        int i = horizontalCut.length - 1;
        int j = verticalCut.length - 1;
        long total = 0;
        long hSegments = 1; // number of pieces in vertical direction
        long vSegments = 1; // number of pieces in horizontal direction

        while (i >= 0 && j >= 0) {
            if (horizontalCut[i] >= verticalCut[j]) {
                total += (long) horizontalCut[i] * vSegments;
                hSegments++;
                i--;
            } else {
                total += (long) verticalCut[j] * hSegments;
                vSegments++;
                j--;
            }
        }

        while (i >= 0) {
            total += (long) horizontalCut[i] * vSegments;
            i--;
        }

        while (j >= 0) {
            total += (long) verticalCut[j] * hSegments;
            j--;
        }

        return (int) total;
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
        # Sort cuts in descending order to apply greedy algorithm
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        h_pieces = 1  # number of current horizontal segments
        v_pieces = 1  # number of current vertical segments

        i = j = 0
        total = 0

        while i < len(horizontalCut) and j < len(verticalCut):
            if horizontalCut[i] > verticalCut[j]:
                total += horizontalCut[i] * v_pieces
                h_pieces += 1
                i += 1
            else:
                total += verticalCut[j] * h_pieces
                v_pieces += 1
                j += 1

        # Remaining horizontal cuts
        while i < len(horizontalCut):
            total += horizontalCut[i] * v_pieces
            i += 1

        # Remaining vertical cuts
        while j < len(verticalCut):
            total += verticalCut[j] * h_pieces
            j += 1

        return total
```

## Python3

```python
from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Sort cuts in descending order to apply the most expensive cuts first
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        h_idx = v_idx = 0
        h_segments = v_segments = 1
        total_cost = 0

        while h_idx < len(horizontalCut) and v_idx < len(verticalCut):
            if horizontalCut[h_idx] > verticalCut[v_idx]:
                total_cost += horizontalCut[h_idx] * v_segments
                h_segments += 1
                h_idx += 1
            else:
                total_cost += verticalCut[v_idx] * h_segments
                v_segments += 1
                v_idx += 1

        while h_idx < len(horizontalCut):
            total_cost += horizontalCut[h_idx] * v_segments
            h_idx += 1

        while v_idx < len(verticalCut):
            total_cost += verticalCut[v_idx] * h_segments
            v_idx += 1

        return total_cost
```

## C

```c
int cmp_desc(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return ib - ia; // descending
}

int minimumCost(int m, int n, int* horizontalCut, int horizontalCutSize, int* verticalCut, int verticalCutSize){
    if (horizontalCutSize > 0)
        qsort(horizontalCut, horizontalCutSize, sizeof(int), cmp_desc);
    if (verticalCutSize > 0)
        qsort(verticalCut, verticalCutSize, sizeof(int), cmp_desc);
    
    int i = 0, j = 0;
    long long total = 0; // use long long to avoid overflow during computation
    int horizPieces = 1, vertPieces = 1;
    
    while (i < horizontalCutSize && j < verticalCutSize) {
        if (horizontalCut[i] >= verticalCut[j]) {
            total += (long long)horizontalCut[i] * vertPieces;
            horizPieces++;
            i++;
        } else {
            total += (long long)verticalCut[j] * horizPieces;
            vertPieces++;
            j++;
        }
    }
    
    while (i < horizontalCutSize) {
        total += (long long)horizontalCut[i] * vertPieces;
        i++;
    }
    while (j < verticalCutSize) {
        total += (long long)verticalCut[j] * horizPieces;
        j++;
    }
    
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        System.Array.Sort(horizontalCut);
        System.Array.Sort(verticalCut);
        // sort descending by reversing iteration
        int i = horizontalCut.Length - 1;
        int j = verticalCut.Length - 1;
        long total = 0;
        long hSegments = 1; // number of current horizontal pieces
        long vSegments = 1; // number of current vertical pieces

        while (i >= 0 && j >= 0) {
            if (horizontalCut[i] > verticalCut[j]) {
                total += (long)horizontalCut[i] * vSegments;
                hSegments++;
                i--;
            } else {
                total += (long)verticalCut[j] * hSegments;
                vSegments++;
                j--;
            }
        }

        while (i >= 0) {
            total += (long)horizontalCut[i] * vSegments;
            hSegments++;
            i--;
        }

        while (j >= 0) {
            total += (long)verticalCut[j] * hSegments;
            vSegments++;
            j--;
        }

        return (int)total;
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
    // Sort cuts in descending order to apply the most expensive cuts first
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);
    
    let hIdx = 0, vIdx = 0;
    let hSegments = 1, vSegments = 1; // current number of pieces in each direction
    let total = 0;
    
    while (hIdx < horizontalCut.length || vIdx < verticalCut.length) {
        if (
            vIdx === verticalCut.length ||
            (hIdx < horizontalCut.length && horizontalCut[hIdx] >= verticalCut[vIdx])
        ) {
            // Take a horizontal cut
            total += horizontalCut[hIdx] * vSegments;
            hSegments++;
            hIdx++;
        } else {
            // Take a vertical cut
            total += verticalCut[vIdx] * hSegments;
            vSegments++;
            vIdx++;
        }
    }
    
    return total;
};
```

## Typescript

```typescript
function minimumCost(m: number, n: number, horizontalCut: number[], verticalCut: number[]): number {
    // Sort cuts in descending order to apply greedy strategy
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);

    let hSegments = 1; // current number of horizontal pieces
    let vSegments = 1; // current number of vertical pieces
    let i = 0, j = 0;
    let total = 0;

    while (i < horizontalCut.length && j < verticalCut.length) {
        if (horizontalCut[i] > verticalCut[j]) {
            total += horizontalCut[i] * vSegments;
            hSegments++;
            i++;
        } else {
            total += verticalCut[j] * hSegments;
            vSegments++;
            j++;
        }
    }

    while (i < horizontalCut.length) {
        total += horizontalCut[i] * vSegments;
        i++;
        hSegments++;
    }

    while (j < verticalCut.length) {
        total += verticalCut[j] * hSegments;
        j++;
        vSegments++;
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
        rsort($horizontalCut);
        rsort($verticalCut);

        $hIdx = 0;
        $vIdx = 0;
        $horSegments = 1; // number of horizontal pieces
        $verSegments = 1; // number of vertical pieces
        $total = 0;

        $hLen = count($horizontalCut);
        $vLen = count($verticalCut);

        while ($hIdx < $hLen && $vIdx < $vLen) {
            if ($horizontalCut[$hIdx] > $verticalCut[$vIdx]) {
                $total += $horizontalCut[$hIdx] * $verSegments;
                $horSegments++;
                $hIdx++;
            } else {
                $total += $verticalCut[$vIdx] * $horSegments;
                $verSegments++;
                $vIdx++;
            }
        }

        while ($hIdx < $hLen) {
            $total += $horizontalCut[$hIdx] * $verSegments;
            $hIdx++;
        }

        while ($vIdx < $vLen) {
            $total += $verticalCut[$vIdx] * $horSegments;
            $vIdx++;
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ m: Int, _ n: Int, _ horizontalCut: [Int], _ verticalCut: [Int]) -> Int {
        var hCuts = horizontalCut.sorted(by: >)
        var vCuts = verticalCut.sorted(by: >)
        
        var hSegments = 1
        var vSegments = 1
        var totalCost = 0
        
        var i = 0
        var j = 0
        
        while i < hCuts.count && j < vCuts.count {
            if hCuts[i] >= vCuts[j] {
                totalCost += hCuts[i] * vSegments
                hSegments += 1
                i += 1
            } else {
                totalCost += vCuts[j] * hSegments
                vSegments += 1
                j += 1
            }
        }
        
        while i < hCuts.count {
            totalCost += hCuts[i] * vSegments
            i += 1
        }
        
        while j < vCuts.count {
            totalCost += vCuts[j] * hSegments
            j += 1
        }
        
        return totalCost
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(m: Int, n: Int, horizontalCut: IntArray, verticalCut: IntArray): Int {
        val h = horizontalCut.sortedDescending()
        val v = verticalCut.sortedDescending()
        var i = 0
        var j = 0
        var hSegments = 1
        var vSegments = 1
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
            hSegments++
            i++
        }
        while (j < v.size) {
            total += v[j].toLong() * hSegments
            vSegments++
            j++
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(int m, int n, List<int> horizontalCut, List<int> verticalCut) {
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);

    int hSegments = 1;
    int vSegments = 1;
    int i = 0, j = 0;
    int total = 0;

    while (i < horizontalCut.length && j < verticalCut.length) {
      if (horizontalCut[i] >= verticalCut[j]) {
        total += horizontalCut[i] * vSegments;
        hSegments++;
        i++;
      } else {
        total += verticalCut[j] * hSegments;
        vSegments++;
        j++;
      }
    }

    while (i < horizontalCut.length) {
      total += horizontalCut[i] * vSegments;
      i++;
    }

    while (j < verticalCut.length) {
      total += verticalCut[j] * hSegments;
      j++;
    }

    return total;
  }
}
```

## Golang

```go
import "sort"

func minimumCost(m int, n int, horizontalCut []int, verticalCut []int) int {
    sort.Slice(horizontalCut, func(i, j int) bool { return horizontalCut[i] > horizontalCut[j] })
    sort.Slice(verticalCut, func(i, j int) bool { return verticalCut[i] > verticalCut[j] })

    hSeg, vSeg := 1, 1
    i, j := 0, 0
    total := 0

    for i < len(horizontalCut) && j < len(verticalCut) {
        if horizontalCut[i] > verticalCut[j] {
            total += horizontalCut[i] * vSeg
            hSeg++
            i++
        } else {
            total += verticalCut[j] * hSeg
            vSeg++
            j++
        }
    }

    for i < len(horizontalCut) {
        total += horizontalCut[i] * vSeg
        i++
    }

    for j < len(verticalCut) {
        total += verticalCut[j] * hSeg
        j++
    }

    return total
}
```

## Ruby

```ruby
def minimum_cost(m, n, horizontal_cut, vertical_cut)
  horizontal = horizontal_cut.sort.reverse
  vertical = vertical_cut.sort.reverse
  h_idx = 0
  v_idx = 0
  h_segments = 1
  v_segments = 1
  total = 0

  while h_idx < horizontal.length || v_idx < vertical.length
    if v_idx == vertical.length || (h_idx < horizontal.length && horizontal[h_idx] > vertical[v_idx])
      total += horizontal[h_idx] * v_segments
      h_segments += 1
      h_idx += 1
    else
      total += vertical[v_idx] * h_segments
      v_segments += 1
      v_idx += 1
    end
  end

  total
end
```

## Scala

```scala
object Solution {
    def minimumCost(m: Int, n: Int, horizontalCut: Array[Int], verticalCut: Array[Int]): Int = {
        val h = horizontalCut.sorted(Ordering[Int].reverse)
        val v = verticalCut.sorted(Ordering[Int].reverse)
        var i = 0
        var j = 0
        var hSeg = 1L
        var vSeg = 1L
        var total = 0L
        while (i < h.length || j < v.length) {
            if (j >= v.length || (i < h.length && h(i) > v(j))) {
                total += h(i).toLong * vSeg
                hSeg += 1
                i += 1
            } else {
                total += v(j).toLong * hSeg
                vSeg += 1
                j += 1
            }
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_cost(m: i32, n: i32, mut horizontal_cut: Vec<i32>, mut vertical_cut: Vec<i32>) -> i32 {
        // Sort cuts in descending order to apply the greedy strategy
        horizontal_cut.sort_by(|a, b| b.cmp(a));
        vertical_cut.sort_by(|a, b| b.cmp(a));

        let mut i = 0usize;
        let mut j = 0usize;
        let mut h_segments: i64 = 1; // number of pieces in vertical direction
        let mut v_segments: i64 = 1; // number of pieces in horizontal direction
        let mut total: i64 = 0;

        while i < horizontal_cut.len() && j < vertical_cut.len() {
            if horizontal_cut[i] > vertical_cut[j] {
                total += (horizontal_cut[i] as i64) * v_segments;
                h_segments += 1;
                i += 1;
            } else {
                total += (vertical_cut[j] as i64) * h_segments;
                v_segments += 1;
                j += 1;
            }
        }

        while i < horizontal_cut.len() {
            total += (horizontal_cut[i] as i64) * v_segments;
            i += 1;
        }

        while j < vertical_cut.len() {
            total += (vertical_cut[j] as i64) * h_segments;
            j += 1;
        }

        total as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-cost m n horizontalCut verticalCut)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((h (sort horizontalCut >))
         (v (sort verticalCut >)))
    (let loop ((i 0) (j 0) (hseg 1) (vseg 1) (total 0))
      (cond
        [(and (= i (length h)) (= j (length v))) total]
        [(= i (length h))
         (loop i (+ j 1) hseg (+ vseg 1)
               (+ total (* (list-ref v j) hseg)))]
        [(= j (length v))
         (loop (+ i 1) j (+ hseg 1) vseg
               (+ total (* (list-ref h i) vseg)))]
        [else
         (if (>= (list-ref h i) (list-ref v j))
             (loop (+ i 1) j (+ hseg 1) vseg
                   (+ total (* (list-ref h i) vseg)))
             (loop i (+ j 1) hseg (+ vseg 1)
                   (+ total (* (list-ref v j) hseg))))]))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_cost/4]).

-spec minimum_cost(M :: integer(), N :: integer(), HorizontalCut :: [integer()], VerticalCut :: [integer()]) -> integer().
minimum_cost(_M, _N, HorizontalCut, VerticalCut) ->
    HSorted = lists:sort(fun(A, B) -> A > B end, HorizontalCut),
    VSorted = lists:sort(fun(A, B) -> A > B end, VerticalCut),
    total_cost(HSorted, VSorted, 1, 1, 0).

total_cost([], [], _HPieces, _VPieces, Acc) ->
    Acc;
total_cost([H|Hs], [], HPieces, VPieces, Acc) ->
    total_cost(Hs, [], HPieces + 1, VPieces, Acc + H * VPieces);
total_cost([], [V|Vs], HPieces, VPieces, Acc) ->
    total_cost([], Vs, HPieces, VPieces + 1, Acc + V * HPieces);
total_cost([H|Hs] = HList, [V|Vs] = VList, HPieces, VPieces, Acc) ->
    if
        H >= V ->
            total_cost(Hs, VList, HPieces + 1, VPieces, Acc + H * VPieces);
        true ->
            total_cost(HList, Vs, HPieces, VPieces + 1, Acc + V * HPieces)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(m :: integer, n :: integer, horizontal_cut :: [integer], vertical_cut :: [integer]) :: integer
  def minimum_cost(_m, _n, horizontal_cut, vertical_cut) do
    h = Enum.sort(horizontal_cut, &>=/2)
    v = Enum.sort(vertical_cut, &>=/2)
    greedy(h, v, 1, 1, 0)
  end

  defp greedy([], [], _hseg, _vseg, total), do: total

  defp greedy([cost | rest_h], [], hseg, vseg, total) do
    greedy(rest_h, [], hseg + 1, vseg, total + cost * vseg)
  end

  defp greedy([], [cost | rest_v], hseg, vseg, total) do
    greedy([], rest_v, hseg, vseg + 1, total + cost * hseg)
  end

  defp greedy([h_cost | h_rest] = hlist, [v_cost | v_rest] = vlist, hseg, vseg, total) do
    if h_cost >= v_cost do
      greedy(h_rest, vlist, hseg + 1, vseg, total + h_cost * vseg)
    else
      greedy(hlist, v_rest, hseg, vseg + 1, total + v_cost * hseg)
    end
  end
end
```
