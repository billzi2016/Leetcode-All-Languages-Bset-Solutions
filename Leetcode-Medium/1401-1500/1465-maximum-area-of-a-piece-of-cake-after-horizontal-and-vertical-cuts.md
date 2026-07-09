# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

## Cpp

```cpp
class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        const long long MOD = 1000000007LL;
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());

        long long maxH = max((long long)horizontalCuts.front(), (long long)h - horizontalCuts.back());
        for (size_t i = 1; i < horizontalCuts.size(); ++i) {
            maxH = max(maxH, (long long)horizontalCuts[i] - horizontalCuts[i - 1]);
        }

        long long maxV = max((long long)verticalCuts.front(), (long long)w - verticalCuts.back());
        for (size_t i = 1; i < verticalCuts.size(); ++i) {
            maxV = max(maxV, (long long)verticalCuts[i] - verticalCuts[i - 1]);
        }

        long long result = (maxH % MOD) * (maxV % MOD) % MOD;
        return static_cast<int>(result);
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        final long MOD = 1_000_000_007L;
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);

        long maxH = Math.max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.length - 1]);
        for (int i = 1; i < horizontalCuts.length; i++) {
            maxH = Math.max(maxH, horizontalCuts[i] - horizontalCuts[i - 1]);
        }

        long maxV = Math.max(verticalCuts[0], w - verticalCuts[verticalCuts.length - 1]);
        for (int i = 1; i < verticalCuts.length; i++) {
            maxV = Math.max(maxV, verticalCuts[i] - verticalCuts[i - 1]);
        }

        return (int) ((maxH % MOD) * (maxV % MOD) % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        horizontalCuts.sort()
        verticalCuts.sort()

        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            gap = horizontalCuts[i] - horizontalCuts[i - 1]
            if gap > max_h:
                max_h = gap

        max_v = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            gap = verticalCuts[i] - verticalCuts[i - 1]
            if gap > max_v:
                max_v = gap

        return (max_h * max_v) % MOD
```

## Python3

```python
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            gap = horizontalCuts[i] - horizontalCuts[i-1]
            if gap > max_h:
                max_h = gap
        
        max_v = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            gap = verticalCuts[i] - verticalCuts[i-1]
            if gap > max_v:
                max_v = gap
        
        return (max_h * max_v) % MOD
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int maxArea(int h, int w, int* horizontalCuts, int horizontalCutsSize,
            int* verticalCuts, int verticalCutsSize) {
    qsort(horizontalCuts, (size_t)horizontalCutsSize, sizeof(int), cmp_int);
    qsort(verticalCuts, (size_t)verticalCutsSize, sizeof(int), cmp_int);

    long long max_h = 0;
    int prev = 0;
    for (int i = 0; i < horizontalCutsSize; ++i) {
        long long gap = (long long)horizontalCuts[i] - prev;
        if (gap > max_h) max_h = gap;
        prev = horizontalCuts[i];
    }
    long long gap = (long long)h - prev;
    if (gap > max_h) max_h = gap;

    long long max_v = 0;
    prev = 0;
    for (int i = 0; i < verticalCutsSize; ++i) {
        long long gapv = (long long)verticalCuts[i] - prev;
        if (gapv > max_v) max_v = gapv;
        prev = verticalCuts[i];
    }
    gap = (long long)w - prev;
    if (gap > max_v) max_v = gap;

    long long result = (max_h % MOD) * (max_v % MOD) % MOD;
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1_000_000_007;
    
    public int MaxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        Array.Sort(horizontalCuts);
        Array.Sort(verticalCuts);
        
        long maxH = GetMaxGap(horizontalCuts, h);
        long maxV = GetMaxGap(verticalCuts, w);
        
        long result = (maxH % MOD) * (maxV % MOD) % MOD;
        return (int)result;
    }
    
    private long GetMaxGap(int[] cuts, int totalLength) {
        long maxGap = 0;
        int prev = 0;
        foreach (int cut in cuts) {
            long gap = cut - prev;
            if (gap > maxGap) maxGap = gap;
            prev = cut;
        }
        long lastGap = totalLength - prev;
        if (lastGap > maxGap) maxGap = lastGap;
        return maxGap;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} horizontalCuts
 * @param {number[]} verticalCuts
 * @return {number}
 */
var maxArea = function(h, w, horizontalCuts, verticalCuts) {
    horizontalCuts.sort((a, b) => a - b);
    verticalCuts.sort((a, b) => a - b);
    
    let prev = 0;
    let maxH = 0;
    for (const cut of horizontalCuts) {
        const diff = cut - prev;
        if (diff > maxH) maxH = diff;
        prev = cut;
    }
    if (h - prev > maxH) maxH = h - prev;
    
    prev = 0;
    let maxV = 0;
    for (const cut of verticalCuts) {
        const diff = cut - prev;
        if (diff > maxV) maxV = diff;
        prev = cut;
    }
    if (w - prev > maxV) maxV = w - prev;
    
    const MOD = 1000000007n;
    const result = (BigInt(maxH) * BigInt(maxV)) % MOD;
    return Number(result);
};
```

## Typescript

```typescript
function maxArea(h: number, w: number, horizontalCuts: number[], verticalCuts: number[]): number {
    const MOD = 1000000007n;

    horizontalCuts.sort((a, b) => a - b);
    verticalCuts.sort((a, b) => a - b);

    let maxH = Math.max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.length - 1]);
    for (let i = 1; i < horizontalCuts.length; i++) {
        const diff = horizontalCuts[i] - horizontalCuts[i - 1];
        if (diff > maxH) maxH = diff;
    }

    let maxV = Math.max(verticalCuts[0], w - verticalCuts[verticalCuts.length - 1]);
    for (let i = 1; i < verticalCuts.length; i++) {
        const diff = verticalCuts[i] - verticalCuts[i - 1];
        if (diff > maxV) maxV = diff;
    }

    const area = (BigInt(maxH) * BigInt(maxV)) % MOD;
    return Number(area);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $h
     * @param Integer $w
     * @param Integer[] $horizontalCuts
     * @param Integer[] $verticalCuts
     * @return Integer
     */
    function maxArea($h, $w, $horizontalCuts, $verticalCuts) {
        sort($horizontalCuts);
        sort($verticalCuts);
        
        $prev = 0;
        $maxH = 0;
        foreach ($horizontalCuts as $cut) {
            $gap = $cut - $prev;
            if ($gap > $maxH) {
                $maxH = $gap;
            }
            $prev = $cut;
        }
        $gap = $h - $prev;
        if ($gap > $maxH) {
            $maxH = $gap;
        }
        
        $prev = 0;
        $maxV = 0;
        foreach ($verticalCuts as $cut) {
            $gap = $cut - $prev;
            if ($gap > $maxV) {
                $maxV = $gap;
            }
            $prev = $cut;
        }
        $gap = $w - $prev;
        if ($gap > $maxV) {
            $maxV = $gap;
        }
        
        $mod = 1000000007;
        return (int)((($maxH % $mod) * ($maxV % $mod)) % $mod);
    }
}
```

## Swift

```swift
class Solution {
    func maxArea(_ h: Int, _ w: Int, _ horizontalCuts: [Int], _ verticalCuts: [Int]) -> Int {
        let MOD = 1_000_000_007
        let sortedH = horizontalCuts.sorted()
        let sortedV = verticalCuts.sorted()
        
        var maxH = max(sortedH.first ?? h, h - (sortedH.last ?? 0))
        for i in 1..<sortedH.count {
            let diff = sortedH[i] - sortedH[i - 1]
            if diff > maxH { maxH = diff }
        }
        
        var maxV = max(sortedV.first ?? w, w - (sortedV.last ?? 0))
        for i in 1..<sortedV.count {
            let diff = sortedV[i] - sortedV[i - 1]
            if diff > maxV { maxV = diff }
        }
        
        let area = (Int64(maxH) * Int64(maxV)) % Int64(MOD)
        return Int(area)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxArea(h: Int, w: Int, horizontalCuts: IntArray, verticalCuts: IntArray): Int {
        val MOD = 1_000_000_007L
        horizontalCuts.sort()
        verticalCuts.sort()

        var maxH = 0L
        var prev = 0
        for (cut in horizontalCuts) {
            val diff = cut - prev
            if (diff > maxH) maxH = diff.toLong()
            prev = cut
        }
        val lastDiffH = h - prev
        if (lastDiffH > maxH) maxH = lastDiffH.toLong()

        var maxV = 0L
        prev = 0
        for (cut in verticalCuts) {
            val diff = cut - prev
            if (diff > maxV) maxV = diff.toLong()
            prev = cut
        }
        val lastDiffV = w - prev
        if (lastDiffV > maxV) maxV = lastDiffV.toLong()

        return ((maxH % MOD) * (maxV % MOD) % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int maxArea(int h, int w, List<int> horizontalCuts, List<int> verticalCuts) {
    horizontalCuts.sort();
    verticalCuts.sort();

    int maxH = horizontalCuts.first;
    for (int i = 1; i < horizontalCuts.length; ++i) {
      int diff = horizontalCuts[i] - horizontalCuts[i - 1];
      if (diff > maxH) maxH = diff;
    }
    int endDiffH = h - horizontalCuts.last;
    if (endDiffH > maxH) maxH = endDiffH;

    int maxW = verticalCuts.first;
    for (int i = 1; i < verticalCuts.length; ++i) {
      int diff = verticalCuts[i] - verticalCuts[i - 1];
      if (diff > maxW) maxW = diff;
    }
    int endDiffW = w - verticalCuts.last;
    if (endDiffW > maxW) maxW = endDiffW;

    return ((maxH % _mod) * (maxW % _mod)) % _mod;
  }
}
```

## Golang

```go
package main

import "sort"

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	sort.Ints(horizontalCuts)
	sort.Ints(verticalCuts)

	maxH := horizontalCuts[0]
	for i := 1; i < len(horizontalCuts); i++ {
		if diff := horizontalCuts[i] - horizontalCuts[i-1]; diff > maxH {
			maxH = diff
		}
	}
	if last := h - horizontalCuts[len(horizontalCuts)-1]; last > maxH {
		maxH = last
	}

	maxV := verticalCuts[0]
	for i := 1; i < len(verticalCuts); i++ {
		if diff := verticalCuts[i] - verticalCuts[i-1]; diff > maxV {
			maxV = diff
		}
	}
	if last := w - verticalCuts[len(verticalCuts)-1]; last > maxV {
		maxV = last
	}

	const mod int64 = 1000000007
	return int((int64(maxH) * int64(maxV)) % mod)
}
```

## Ruby

```ruby
def max_area(h, w, horizontal_cuts, vertical_cuts)
  mod = 1_000_000_007
  horizontal_cuts.sort!
  vertical_cuts.sort!

  max_h = [horizontal_cuts[0], h - horizontal_cuts[-1]].max
  (1...horizontal_cuts.length).each do |i|
    gap = horizontal_cuts[i] - horizontal_cuts[i - 1]
    max_h = gap if gap > max_h
  end

  max_v = [vertical_cuts[0], w - vertical_cuts[-1]].max
  (1...vertical_cuts.length).each do |i|
    gap = vertical_cuts[i] - vertical_cuts[i - 1]
    max_v = gap if gap > max_v
  end

  ((max_h % mod) * (max_v % mod)) % mod
end
```

## Scala

```scala
object Solution {
    def maxArea(h: Int, w: Int, horizontalCuts: Array[Int], verticalCuts: Array[Int]): Int = {
        val MOD = 1000000007L

        val sortedH = horizontalCuts.sorted
        var prev = 0
        var maxHGap = 0
        for (cut <- sortedH) {
            val gap = cut - prev
            if (gap > maxHGap) maxHGap = gap
            prev = cut
        }
        val lastHGap = h - prev
        if (lastHGap > maxHGap) maxHGap = lastHGap

        val sortedV = verticalCuts.sorted
        prev = 0
        var maxVGap = 0
        for (cut <- sortedV) {
            val gap = cut - prev
            if (gap > maxVGap) maxVGap = gap
            prev = cut
        }
        val lastVGap = w - prev
        if (lastVGap > maxVGap) maxVGap = lastVGap

        ((maxHGap.toLong * maxVGap.toLong) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_area(h: i32, w: i32, horizontal_cuts: Vec<i32>, vertical_cuts: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut hcuts = horizontal_cuts;
        let mut vcuts = vertical_cuts;
        hcuts.sort_unstable();
        vcuts.sort_unstable();

        let mut max_h_gap: i64 = 0;
        let mut prev: i64 = 0;
        for &cut in &hcuts {
            let cur = cut as i64;
            max_h_gap = max_h_gap.max(cur - prev);
            prev = cur;
        }
        max_h_gap = max_h_gap.max(h as i64 - prev);

        let mut max_v_gap: i64 = 0;
        let mut prev: i64 = 0;
        for &cut in &vcuts {
            let cur = cut as i64;
            max_v_gap = max_v_gap.max(cur - prev);
            prev = cur;
        }
        max_v_gap = max_v_gap.max(w as i64 - prev);

        ((max_h_gap % MOD) * (max_v_gap % MOD) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (max-gap size cuts)
  (let* ((sorted (sort cuts <))
         (first-gap (car sorted))
         (max-diff first-gap)
         (prev (car sorted)))
    (for ([c (in-list (cdr sorted))])
      (let ((gap (- c prev)))
        (when (> gap max-diff) (set! max-diff gap))
        (set! prev c)))
    (let ((last-gap (- size (last sorted))))
      (if (> last-gap max-diff) last-gap max-diff))))

(define/contract (max-area h w horizontalCuts verticalCuts)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((max-h (max-gap h horizontalCuts))
         (max-w (max-gap w verticalCuts))
         (area (* max-h max-w)))
    (modulo area MOD)))
```

## Erlang

```erlang
-module(solution).
-export([max_area/4]).

-spec max_area(integer(), integer(), [integer()], [integer()]) -> integer().
max_area(H, W, HorizontalCuts, VerticalCuts) ->
    MaxH = max_gap(HorizontalCuts, H),
    MaxV = max_gap(VerticalCuts, W),
    Mod = 1000000007,
    ((MaxH rem Mod) * (MaxV rem Mod)) rem Mod.

max_gap(Cuts, Total) ->
    Sorted = lists:sort(Cuts),
    FirstGap = hd(Sorted) - 0,
    LastGap = Total - lists:last(Sorted),
    MaxMid = max_mid_gap(Sorted, FirstGap),
    case MaxMid > LastGap of
        true -> MaxMid;
        false -> LastGap
    end.

max_mid_gap([_], Max) ->
    Max;
max_mid_gap([Prev, Curr | Rest], Max) ->
    Gap = Curr - Prev,
    NewMax = if Gap > Max -> Gap; true -> Max end,
    max_mid_gap([Curr | Rest], NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec max_area(h :: integer, w :: integer, horizontal_cuts :: [integer], vertical_cuts :: [integer]) :: integer
  def max_area(h, w, horizontal_cuts, vertical_cuts) do
    mod = 1_000_000_007

    max_h = max_gap(horizontal_cuts, h)
    max_v = max_gap(vertical_cuts, w)

    rem(max_h * max_v, mod)
  end

  defp max_gap(cuts, total) do
    sorted = Enum.sort(cuts)

    {max_gap, last_cut} =
      Enum.reduce(sorted, {0, 0}, fn cut, {mx, prev} ->
        gap = cut - prev
        mx = if gap > mx, do: gap, else: mx
        {mx, cut}
      end)

    final_gap = total - last_cut
    if final_gap > max_gap, do: final_gap, else: max_gap
  end
end
```
