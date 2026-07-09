# 2943. Maximize Area of Square Hole in Grid

## Cpp

```cpp
class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        auto maxConsecutive = [](vector<int> a) {
            sort(a.begin(), a.end());
            int best = 0, cur = 0, prev = -2;
            for (int x : a) {
                if (x == prev + 1) ++cur;
                else cur = 1;
                best = max(best, cur);
                prev = x;
            }
            return best; // number of consecutive removable bars
        };
        int maxH = maxConsecutive(hBars) + 1; // maximal vertical gap size
        int maxV = maxConsecutive(vBars) + 1; // maximal horizontal gap size
        int side = min(maxH, maxV);
        return side * side;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int maxH = maxDimension(hBars);
        int maxV = maxDimension(vBars);
        int side = Math.min(maxH, maxV);
        return (int)((long)side * side);
    }

    private int maxDimension(int[] bars) {
        Arrays.sort(bars);
        int maxDim = 1; // at least one cell without removing any bar
        int start = bars[0];
        for (int i = 1; i < bars.length; i++) {
            if (bars[i] != bars[i - 1] + 1) {
                int runLen = bars[i - 1] - start + 1;
                maxDim = Math.max(maxDim, runLen + 1);
                start = bars[i];
            }
        }
        // handle the last run
        int runLen = bars[bars.length - 1] - start + 1;
        maxDim = Math.max(maxDim, runLen + 1);
        return maxDim;
    }
}
```

## Python

```python
class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        def max_side(bars):
            bars.sort()
            max_len = 0
            cur_len = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    cur_len += 1
                else:
                    if cur_len > max_len:
                        max_len = cur_len
                    cur_len = 1
            if cur_len > max_len:
                max_len = cur_len
            # side length in cells is (number of consecutive removable bars) + 1
            return max_len + 1

        side_h = max_side(hBars)
        side_v = max_side(vBars)
        side = min(side_h, side_v)
        return side * side
```

## Python3

```python
from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_consecutive_plus_one(arr: List[int]) -> int:
            arr.sort()
            best = cur = 0
            prev = None
            for x in arr:
                if prev is not None and x == prev + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
                prev = x
            # at least one removable bar exists, so best >=1
            return best + 1

        max_rows = max_consecutive_plus_one(hBars)   # height in units
        max_cols = max_consecutive_plus_one(vBars)   # width in units
        side = min(max_rows, max_cols)
        return side * side
```

## C

```c
int compareInt(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int maximizeSquareHoleArea(int n, int m, int* hBars, int hBarsSize, int* vBars, int vBarsSize) {
    // Sort the arrays
    qsort(hBars, hBarsSize, sizeof(int), compareInt);
    qsort(vBars, vBarsSize, sizeof(int), compareInt);
    
    // Find longest consecutive segment in hBars
    int maxLenH = 0, curLen = 0;
    for (int i = 0; i < hBarsSize; ++i) {
        if (i == 0 || hBars[i] != hBars[i-1] + 1) {
            curLen = 1;
        } else {
            curLen += 1;
        }
        if (curLen > maxLenH) maxLenH = curLen;
    }
    // Height achievable
    int height = maxLenH + 1;   // at least one unit even without removal
    
    // Find longest consecutive segment in vBars
    int maxLenV = 0;
    curLen = 0;
    for (int i = 0; i < vBarsSize; ++i) {
        if (i == 0 || vBars[i] != vBars[i-1] + 1) {
            curLen = 1;
        } else {
            curLen += 1;
        }
        if (curLen > maxLenV) maxLenV = curLen;
    }
    // Width achievable
    int width = maxLenV + 1;
    
    // The largest square side length is limited by both dimensions
    int side = height < width ? height : width;
    
    return side * side;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int GetSide(int[] bars) {
            if (bars == null || bars.Length == 0) return 1;
            Array.Sort(bars);
            int maxLen = 1, curLen = 1;
            for (int i = 1; i < bars.Length; i++) {
                if (bars[i] == bars[i - 1] + 1) {
                    curLen++;
                } else {
                    curLen = 1;
                }
                if (curLen > maxLen) maxLen = curLen;
            }
            return maxLen + 1; // length of consecutive removable bars plus one
        }

        int sideH = GetSide(hBars);
        int sideV = GetSide(vBars);
        int side = Math.Min(sideH, sideV);
        return side * side;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} hBars
 * @param {number[]} vBars
 * @return {number}
 */
var maximizeSquareHoleArea = function(n, m, hBars, vBars) {
    const maxGap = (arr) => {
        arr.sort((a, b) => a - b);
        let maxLen = 0;
        let curLen = 0;
        let prev = -Infinity;
        for (const x of arr) {
            if (x === prev + 1) {
                curLen++;
            } else {
                curLen = 1;
            }
            if (curLen > maxLen) maxLen = curLen;
            prev = x;
        }
        // add the two fixed bars surrounding the removable segment
        return maxLen + 1;
    };
    
    const rowGap = maxGap(hBars);
    const colGap = maxGap(vBars);
    const side = Math.min(rowGap, colGap);
    return side * side;
};
```

## Typescript

```typescript
function maximizeSquareHoleArea(n: number, m: number, hBars: number[], vBars: number[]): number {
    const longestConsecutive = (arr: number[]): number => {
        if (arr.length === 0) return 0;
        arr.sort((a, b) => a - b);
        let maxLen = 1;
        let curLen = 1;
        for (let i = 1; i < arr.length; i++) {
            if (arr[i] === arr[i - 1] + 1) {
                curLen++;
            } else {
                if (curLen > maxLen) maxLen = curLen;
                curLen = 1;
            }
        }
        return Math.max(maxLen, curLen);
    };

    const maxHRun = longestConsecutive(hBars); // number of removable horizontal bars in best run
    const maxVRun = longestConsecutive(vBars); // number of removable vertical bars in best run

    const maxHeight = maxHRun + 1; // cells spanned vertically
    const maxWidth = maxVRun + 1;   // cells spanned horizontally

    const side = Math.min(maxHeight, maxWidth);
    return side * side;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[] $hBars
     * @param Integer[] $vBars
     * @return Integer
     */
    function maximizeSquareHoleArea($n, $m, $hBars, $vBars) {
        // longest consecutive run in hBars
        sort($hBars);
        $maxRunH = 0;
        $curStart = null;
        $prev = null;
        foreach ($hBars as $val) {
            if ($curStart === null) {
                $curStart = $val;
            } else {
                if ($val != $prev + 1) {
                    $len = $prev - $curStart + 1;
                    if ($len > $maxRunH) $maxRunH = $len;
                    $curStart = $val;
                }
            }
            $prev = $val;
        }
        if ($curStart !== null) {
            $len = $prev - $curStart + 1;
            if ($len > $maxRunH) $maxRunH = $len;
        }

        // longest consecutive run in vBars
        sort($vBars);
        $maxRunV = 0;
        $curStart = null;
        $prev = null;
        foreach ($vBars as $val) {
            if ($curStart === null) {
                $curStart = $val;
            } else {
                if ($val != $prev + 1) {
                    $len = $prev - $curStart + 1;
                    if ($len > $maxRunV) $maxRunV = $len;
                    $curStart = $val;
                }
            }
            $prev = $val;
        }
        if ($curStart !== null) {
            $len = $prev - $curStart + 1;
            if ($len > $maxRunV) $maxRunV = $len;
        }

        // side length achievable from each direction
        $sideH = $maxRunH + 1; // removed bars + 1
        $sideV = $maxRunV + 1;

        $side = min($sideH, $sideV);
        return $side * $side;
    }
}
```

## Swift

```swift
class Solution {
    func maximizeSquareHoleArea(_ n: Int, _ m: Int, _ hBars: [Int], _ vBars: [Int]) -> Int {
        func maxSideFromBars(_ bars: [Int]) -> Int {
            let sorted = bars.sorted()
            var maxRun = 1
            var curRun = 1
            for i in 1..<sorted.count {
                if sorted[i] == sorted[i - 1] + 1 {
                    curRun += 1
                } else {
                    maxRun = max(maxRun, curRun)
                    curRun = 1
                }
            }
            maxRun = max(maxRun, curRun)
            return maxRun + 1   // run length plus one extra cell
        }
        
        let height = maxSideFromBars(hBars)
        let width = maxSideFromBars(vBars)
        let side = min(height, width)
        return side * side
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeSquareHoleArea(n: Int, m: Int, hBars: IntArray, vBars: IntArray): Int {
        fun maxSide(arr: IntArray): Int {
            if (arr.isEmpty()) return 1
            arr.sort()
            var maxRun = 1
            var curStart = arr[0]
            var prev = arr[0]
            for (i in 1 until arr.size) {
                val v = arr[i]
                if (v != prev + 1) {
                    val runLen = prev - curStart + 1
                    if (runLen > maxRun) maxRun = runLen
                    curStart = v
                }
                prev = v
            }
            val runLen = prev - curStart + 1
            if (runLen > maxRun) maxRun = runLen
            return maxRun + 1   // side length achievable from this direction
        }

        val sideH = maxSide(hBars)
        val sideV = maxSide(vBars)
        val side = kotlin.math.min(sideH, sideV)
        return side * side
    }
}
```

## Dart

```dart
class Solution {
  int maximizeSquareHoleArea(int n, int m, List<int> hBars, List<int> vBars) {
    int maxH = _longestConsecutivePlusTwo(hBars);
    int maxV = _longestConsecutivePlusTwo(vBars);
    int side = maxH < maxV ? maxH : maxV;
    return side * side;
  }

  int _longestConsecutivePlusTwo(List<int> bars) {
    if (bars.isEmpty) return 2; // not expected per constraints
    bars.sort();
    int best = 0;
    int start = bars[0];
    int prev = bars[0];

    for (int i = 1; i < bars.length; i++) {
      int cur = bars[i];
      if (cur != prev + 1) {
        int len = prev - start + 2;
        if (len > best) best = len;
        start = cur;
      }
      prev = cur;
    }

    // handle the last run
    int len = prev - start + 2;
    if (len > best) best = len;

    return best;
  }
}
```

## Golang

```go
func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
	// Helper to compute maximum gap length from removable bars
	maxGap := func(bars []int) int {
		if len(bars) == 0 {
			return 2 // only outer bars remain, distance between them is 2 units
		}
		sort.Ints(bars)
		maxLen := 0
		start := bars[0]
		prev := bars[0]
		for i := 1; i < len(bars); i++ {
			if bars[i] == prev+1 {
				// continue consecutive run
				prev = bars[i]
				continue
			}
			// end of current run
			curLen := prev - start + 2 // include the two fixed bars at both ends
			if curLen > maxLen {
				maxLen = curLen
			}
			// start new run
			start = bars[i]
			prev = bars[i]
		}
		// last run
		curLen := prev - start + 2
		if curLen > maxLen {
			maxLen = curLen
		}
		return maxLen
	}

	hMax := maxGap(hBars)
	vMax := maxGap(vBars)

	side := hMax
	if vMax < side {
		side = vMax
	}
	return side * side
}
```

## Ruby

```ruby
def maximize_square_hole_area(n, m, h_bars, v_bars)
  h = h_bars.sort
  v = v_bars.sort

  max_h = 1
  cur = 1
  (1...h.length).each do |i|
    if h[i] == h[i - 1] + 1
      cur += 1
    else
      max_h = [max_h, cur].max
      cur = 1
    end
  end
  max_h = [max_h, cur].max

  max_v = 1
  cur = 1
  (1...v.length).each do |i|
    if v[i] == v[i - 1] + 1
      cur += 1
    else
      max_v = [max_v, cur].max
      cur = 1
    end
  end
  max_v = [max_v, cur].max

  side = [max_h + 1, max_v + 1].min
  side * side
end
```

## Scala

```scala
object Solution {
    def maximizeSquareHoleArea(n: Int, m: Int, hBars: Array[Int], vBars: Array[Int]): Int = {
        def maxSide(arr: Array[Int]): Int = {
            val sorted = arr.sorted
            var curStart = sorted(0)
            var prev = sorted(0)
            var best = 0
            for (i <- 1 until sorted.length) {
                val cur = sorted(i)
                if (cur != prev + 1) {
                    val side = prev - curStart + 2
                    if (side > best) best = side
                    curStart = cur
                }
                prev = cur
            }
            val side = prev - curStart + 2
            if (side > best) best = side
            best
        }

        val maxH = maxSide(hBars)
        val maxV = maxSide(vBars)
        val side = Math.min(maxH, maxV)
        (side.toLong * side).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_square_hole_area(n: i32, m: i32, h_bars: Vec<i32>, v_bars: Vec<i32>) -> i32 {
        let max_h_gap = Self::longest_consecutive(&h_bars) + 1;
        let max_v_gap = Self::longest_consecutive(&v_bars) + 1;
        let side = std::cmp::min(max_h_gap, max_v_gap);
        (side as i64 * side as i64) as i32
    }

    fn longest_consecutive(arr: &Vec<i32>) -> i32 {
        if arr.is_empty() {
            return 0;
        }
        let mut sorted = arr.clone();
        sorted.sort_unstable();
        let mut max_len = 1;
        let mut cur_len = 1;
        for i in 1..sorted.len() {
            if sorted[i] == sorted[i - 1] + 1 {
                cur_len += 1;
            } else {
                cur_len = 1;
            }
            if cur_len > max_len {
                max_len = cur_len;
            }
        }
        max_len
    }
}
```

## Racket

```racket
(define (longest-consecutive lst)
  (if (null? lst)
      0
      (let* ((sorted (sort lst <))
             (first (car sorted)))
        (let loop ((rest (cdr sorted)) (cur-start first) (prev first) (maxlen 1))
          (if (null? rest)
              maxlen
              (let ((x (car rest)))
                (if (= x (+ prev 1))
                    (let ((newlen (+ (- x cur-start) 1)))
                      (loop (cdr rest) cur-start x (if (> newlen maxlen) newlen maxlen)))
                    (loop (cdr rest) x x (if (> 1 maxlen) 1 maxlen)))))))))

(define/contract (maximize-square-hole-area n m hBars vBars)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((hmax (+ (longest-consecutive hBars) 1))
         (vmax (+ (longest-consecutive vBars) 1))
         (side (min hmax vmax)))
    (* side side)))
```

## Erlang

```erlang
-spec maximize_square_hole_area(N :: integer(), M :: integer(), HBars :: [integer()], VBars :: [integer()]) -> integer().
maximize_square_hole_area(_N, _M, HBars, VBars) ->
    SortedH = lists:sort(HBars),
    SortedV = lists:sort(VBars),
    GapH = longest_gap(SortedH),
    GapV = longest_gap(SortedV),
    SideH = GapH + 2,
    SideV = GapV + 2,
    Side = erlang:min(SideH, SideV),
    Side * Side.

longest_gap([]) -> 0;
longest_gap([First|Rest]) ->
    longest_gap(Rest, First, First, 0).

longest_gap([], Start, Prev, Max) ->
    Gap = Prev - Start,
    case Gap > Max of
        true -> Gap;
        false -> Max
    end;
longest_gap([X|Xs], Start, Prev, Max) ->
    if X =:= Prev + 1 ->
            longest_gap(Xs, Start, X, Max);
       true ->
            Gap = Prev - Start,
            NewMax = case Gap > Max of true -> Gap; false -> Max end,
            longest_gap(Xs, X, X, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximize_square_hole_area(n :: integer, m :: integer, h_bars :: [integer], v_bars :: [integer]) :: integer
  def maximize_square_hole_area(_n, _m, h_bars, v_bars) do
    max_consecutive = fn bars ->
      sorted = Enum.sort(bars)

      {max_len, cur_len, _prev} =
        Enum.reduce(sorted, {0, 0, nil}, fn x, {max_acc, cur_acc, prev_val} ->
          if prev_val != nil and x == prev_val + 1 do
            new_cur = cur_acc + 1
            {max(max_acc, new_cur), new_cur, x}
          else
            {max(max_acc, 1), 1, x}
          end
        end)

      max_len
    end

    h_max = max_consecutive.(h_bars)
    v_max = max_consecutive.(v_bars)

    side = min(h_max + 1, v_max + 1)
    side * side
  end
end
```
