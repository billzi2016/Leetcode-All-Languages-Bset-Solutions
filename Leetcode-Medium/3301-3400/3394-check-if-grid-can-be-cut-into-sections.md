# 3394. Check if Grid can be Cut into Sections

## Cpp

```cpp
class Solution {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        auto canCut = [&](int dim)->bool{
            int m = rectangles.size();
            vector<pair<long long,long long>> seg;
            seg.reserve(m);
            for (auto &r : rectangles) {
                long long s = r[dim];
                long long e = r[dim + 2];
                seg.emplace_back(s, e);
            }
            sort(seg.begin(), seg.end(),
                 [](const auto& a, const auto& b){ return a.first < b.first; });
            long long furthest = seg[0].second;
            int gaps = 0;
            for (int i = 1; i < m; ++i) {
                if (seg[i].first >= furthest) {
                    ++gaps;
                    if (gaps >= 2) return true;
                }
                furthest = max(furthest, seg[i].second);
            }
            return false;
        };
        return canCut(0) || canCut(1);
    }
};
```

## Java

```java
class Solution {
    public boolean checkValidCuts(int n, int[][] rectangles) {
        if (canCut(rectangles, 0)) return true;
        if (canCut(rectangles, 1)) return true;
        return false;
    }

    private boolean canCut(int[][] rects, int dim) {
        java.util.Arrays.sort(rects, (a, b) -> Integer.compare(a[dim], b[dim]));
        int gaps = 0;
        int furthest = rects[0][dim + 2];
        for (int i = 1; i < rects.length; i++) {
            int start = rects[i][dim];
            if (start >= furthest) {
                gaps++;
                if (gaps >= 2) return true;
                furthest = rects[i][dim + 2];
            } else {
                furthest = Math.max(furthest, rects[i][dim + 2]);
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def can_cut(dim):
            # dim = 0 for vertical cuts (x), 1 for horizontal cuts (y)
            intervals = [(r[dim * 2], r[dim * 2 + 1]) for r in rectangles]
            intervals.sort(key=lambda x: x[0])
            max_end = intervals[0][1]
            gaps = 0
            for s, e in intervals[1:]:
                if s >= max_end:
                    gaps += 1
                    if gaps >= 2:
                        return True
                if e > max_end:
                    max_end = e
            return False

        return can_cut(0) or can_cut(1)
```

## Python3

```python
from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cut(dim: int) -> bool:
            segs = [(r[dim], r[dim + 2]) for r in rectangles]
            segs.sort(key=lambda x: x[0])
            max_end = segs[0][1]
            gaps = 0
            for start, end in segs[1:]:
                if start >= max_end:
                    gaps += 1
                    if gaps >= 2:
                        return True
                if end > max_end:
                    max_end = end
            return False

        return can_cut(0) or can_cut(1)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int s;
    int e;
} Interval;

static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->s != ib->s) return ia->s - ib->s;
    return ia->e - ib->e;
}

static bool canMakeTwoCuts(int rectCount, int **rects, int dim) {
    // dim == 0 -> vertical (use x coordinates), dim == 1 -> horizontal (use y)
    Interval *arr = (Interval *)malloc(sizeof(Interval) * rectCount);
    if (!arr) return false;
    for (int i = 0; i < rectCount; ++i) {
        if (dim == 0) {
            arr[i].s = rects[i][0];
            arr[i].e = rects[i][2];
        } else {
            arr[i].s = rects[i][1];
            arr[i].e = rects[i][3];
        }
    }

    qsort(arr, rectCount, sizeof(Interval), cmpInterval);

    int gaps = 0;
    int furthest = arr[0].e;
    for (int i = 1; i < rectCount && gaps < 2; ++i) {
        if (arr[i].s > furthest) {
            ++gaps;
            furthest = arr[i].e;
        } else if (arr[i].e > furthest) {
            furthest = arr[i].e;
        }
    }

    free(arr);
    return gaps >= 2;
}

bool checkValidCuts(int n, int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    (void)n; // n is not needed for the logic
    if (rectanglesSize < 3) return false;
    bool vertical = canMakeTwoCuts(rectanglesSize, rectangles, 0);
    bool horizontal = canMakeTwoCuts(rectanglesSize, rectangles, 1);
    return vertical || horizontal;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool CheckValidCuts(int n, int[][] rectangles) {
        return CanCut(rectangles, true) || CanCut(rectangles, false);
    }

    private bool CanCut(int[][] rects, bool vertical) {
        int m = rects.Length;
        var intervals = new List<(int start, int end)>(m);
        for (int i = 0; i < m; i++) {
            if (vertical)
                intervals.Add((rects[i][0], rects[i][2])); // x-direction
            else
                intervals.Add((rects[i][1], rects[i][3])); // y-direction
        }

        intervals.Sort((a, b) => a.start.CompareTo(b.start));

        long maxEnd = intervals[0].end;
        int gaps = 0;

        for (int i = 1; i < m; i++) {
            if (intervals[i].start > maxEnd) {
                gaps++;
                if (gaps >= 2) return true;
            }
            if (intervals[i].end > maxEnd) maxEnd = intervals[i].end;
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var checkValidCuts = function(n, rectangles) {
    const canCut = (dim) => {
        // dim: 0 for x, 1 for y
        const intervals = new Array(rectangles.length);
        for (let i = 0; i < rectangles.length; ++i) {
            intervals[i] = [rectangles[i][dim], rectangles[i][dim + 2]];
        }
        intervals.sort((a, b) => a[0] - b[0]);
        let furthest = intervals[0][1];
        let gaps = 0;
        for (let i = 1; i < intervals.length; ++i) {
            const [start, end] = intervals[i];
            if (start > furthest) { // a gap exists
                gaps++;
                if (gaps >= 2) return true;
            }
            if (end > furthest) furthest = end;
        }
        return false;
    };
    
    return canCut(0) || canCut(1);
};
```

## Typescript

```typescript
function checkValidCuts(n: number, rectangles: number[][]): boolean {
    const canCut = (startIdx: number, endIdx: number): boolean => {
        const segs: [number, number][] = rectangles.map(r => [r[startIdx], r[endIdx]]);
        segs.sort((a, b) => a[0] - b[0]);
        let maxEnd = segs[0][1];
        let gaps = 0;
        for (let i = 1; i < segs.length; i++) {
            const s = segs[i][0];
            const e = segs[i][1];
            if (s >= maxEnd) {
                gaps++;
                maxEnd = e;
                if (gaps >= 2) return true;
            } else if (e > maxEnd) {
                maxEnd = e;
            }
        }
        return false;
    };
    return canCut(0, 2) || canCut(1, 3);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $rectangles
     * @return Boolean
     */
    function checkValidCuts($n, $rectangles) {
        if ($this->canCut($rectangles, 0)) return true; // vertical cuts (x)
        if ($this->canCut($rectangles, 1)) return true; // horizontal cuts (y)
        return false;
    }

    private function canCut($rects, $dim) {
        usort($rects, function($a, $b) use ($dim) {
            $startA = $dim === 0 ? $a[0] : $a[1];
            $startB = $dim === 0 ? $b[0] : $b[1];
            if ($startA == $startB) {
                $endA = $dim === 0 ? $a[2] : $a[3];
                $endB = $dim === 0 ? $b[2] : $b[3];
                return $endA <=> $endB;
            }
            return $startA <=> $startB;
        });

        $gapCount = 0;
        $maxEnd = $dim === 0 ? $rects[0][2] : $rects[0][3];
        $len = count($rects);
        for ($i = 1; $i < $len; $i++) {
            $start = $dim === 0 ? $rects[$i][0] : $rects[$i][1];
            $end   = $dim === 0 ? $rects[$i][2] : $rects[$i][3];

            if ($start > $maxEnd) {
                $gapCount++;
                $maxEnd = $end;
                if ($gapCount >= 2) return true;
            } else {
                if ($end > $maxEnd) $maxEnd = $end;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func checkValidCuts(_ n: Int, _ rectangles: [[Int]]) -> Bool {
        // Helper to determine if we can make two cuts in one dimension
        func canMakeTwoCuts(_ intervals: [(Int, Int)]) -> Bool {
            let sorted = intervals.sorted { $0.0 < $1.0 }
            var furthestEnd = sorted[0].1
            var gapCount = 0
            for i in 1..<sorted.count {
                let (start, end) = sorted[i]
                if start > furthestEnd {
                    gapCount += 1
                    if gapCount >= 2 { return true }
                }
                if end > furthestEnd {
                    furthestEnd = end
                }
            }
            return false
        }
        
        var vertical: [(Int, Int)] = []
        var horizontal: [(Int, Int)] = []
        vertical.reserveCapacity(rectangles.count)
        horizontal.reserveCapacity(rectangles.count)
        
        for rect in rectangles {
            // rect format: [startx, starty, endx, endy]
            vertical.append((rect[0], rect[2]))
            horizontal.append((rect[1], rect[3]))
        }
        
        return canMakeTwoCuts(vertical) || canMakeTwoCuts(horizontal)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkValidCuts(n: Int, rectangles: Array<IntArray>): Boolean {
        fun canCut(startIdx: Int, endIdx: Int): Boolean {
            val intervals = rectangles.map { intArrayOf(it[startIdx], it[endIdx]) }
                .sortedBy { it[0] }
            var maxEnd = intervals[0][1]
            var gaps = 0
            for (i in 1 until intervals.size) {
                val s = intervals[i][0]
                val e = intervals[i][1]
                if (s > maxEnd) {
                    gaps++
                    if (gaps >= 2) return true
                }
                if (e > maxEnd) maxEnd = e
            }
            return false
        }
        return canCut(0, 2) || canCut(1, 3)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  bool checkValidCuts(int n, List<List<int>> rectangles) {
    return _canCut(rectangles, 0) || _canCut(rectangles, 1);
  }

  bool _canCut(List<List<int>> rects, int dim) {
    // dim = 0 for horizontal (y), 1 for vertical (x)
    List<List<int>> intervals = List.generate(
        rects.length,
        (i) => [rects[i][dim], rects[i][dim + 2]],
        growable: false);
    intervals.sort((a, b) => a[0].compareTo(b[0]));

    int furthest = intervals[0][1];
    int gaps = 0;

    for (int i = 1; i < intervals.length; i++) {
      if (intervals[i][0] >= furthest) {
        gaps++;
        if (gaps >= 2) return true;
        furthest = intervals[i][1];
      } else {
        furthest = max(furthest, intervals[i][1]);
      }
    }
    return false;
  }
}
```

## Golang

```go
func checkValidCuts(n int, rectangles [][]int) bool {
	type interval struct{ start, end int }
	// helper to check cuts along a given dimension (0 for x, 1 for y)
	canCut := func(dim int) bool {
		m := len(rectangles)
		if m < 3 {
			return false
		}
		ints := make([]interval, m)
		for i, r := range rectangles {
			if dim == 0 { // x dimension
				ints[i] = interval{r[0], r[2]}
			} else { // y dimension
				ints[i] = interval{r[1], r[3]}
			}
		}
		// sort by start coordinate
		sort.Slice(ints, func(i, j int) bool {
			if ints[i].start == ints[j].start {
				return ints[i].end < ints[j].end
			}
			return ints[i].start < ints[j].start
		})
		groups := 1
		maxEnd := ints[0].end
		for i := 1; i < m; i++ {
			if ints[i].start > maxEnd { // gap creates a new group
				groups++
				maxEnd = ints[i].end
			} else if ints[i].end > maxEnd {
				maxEnd = ints[i].end
			}
		}
		return groups >= 3
	}

	if canCut(0) || canCut(1) {
		return true
	}
	return false
}

// needed import
import "sort"
```

## Ruby

```ruby
def check_valid_cuts(n, rectangles)
  can_cut = lambda do |start_idx, end_idx|
    sorted = rectangles.sort_by { |r| r[start_idx] }
    gap = 0
    max_end = sorted[0][end_idx]
    (1...sorted.length).each do |i|
      if sorted[i][start_idx] > max_end
        gap += 1
        return true if gap >= 2
      end
      max_end = [max_end, sorted[i][end_idx]].max
    end
    false
  end

  can_cut.call(0, 2) || can_cut.call(1, 3)
end
```

## Scala

```scala
object Solution {
    def checkValidCuts(n: Int, rectangles: Array[Array[Int]]): Boolean = {
        def canCut(startIdx: Int, endIdx: Int): Boolean = {
            val sorted = rectangles.sortBy(_(startIdx))
            var maxEnd = sorted(0)(endIdx)
            var gaps = 0
            var i = 1
            while (i < sorted.length && gaps < 2) {
                val curStart = sorted(i)(startIdx)
                if (curStart >= maxEnd) {
                    gaps += 1
                }
                val curEnd = sorted(i)(endIdx)
                if (curEnd > maxEnd) maxEnd = curEnd
                i += 1
            }
            gaps >= 2
        }
        canCut(0, 2) || canCut(1, 3)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_valid_cuts(_n: i32, rectangles: Vec<Vec<i32>>) -> bool {
        fn can_cut(dim: usize, rects: &Vec<Vec<i32>>) -> bool {
            let mut intervals: Vec<(i32, i32)> = rects.iter().map(|r| (r[dim], r[dim + 2])).collect();
            intervals.sort_by_key(|&(s, _)| s);
            if intervals.is_empty() {
                return false;
            }
            let mut groups = 1;
            let mut cur_end = intervals[0].1;
            for &(s, e) in intervals.iter().skip(1) {
                if s < cur_end {
                    if e > cur_end {
                        cur_end = e;
                    }
                } else {
                    groups += 1;
                    cur_end = e;
                }
            }
            groups >= 3
        }

        can_cut(0, &rectangles) || can_cut(1, &rectangles)
    }
}
```

## Racket

```racket
(define (check-dim dim rects)
  (let* ((start-idx (if (= dim 0) 0 1))
         (end-idx   (if (= dim 0) 2 3))
         (sorted (sort rects
                       (lambda (a b)
                         (< (list-ref a start-idx) (list-ref b start-idx)))))
         (len (length sorted)))
    (if (< len 3)
        #f
        (let loop ((i 1)
                   (furthest (list-ref (first sorted) end-idx))
                   (gaps 0))
          (cond
            [(>= gaps 2) #t]
            [(= i len)   #f]
            [else
             (define cur (list-ref sorted i))
             (define cur-start (list-ref cur start-idx))
             (define cur-end   (list-ref cur end-idx))
             (if (>= cur-start furthest)
                 (loop (+ i 1) (max furthest cur-end) (+ gaps 1))
                 (loop (+ i 1) (max furthest cur-end) gaps))])))))

(define/contract (check-valid-cuts n rectangles)
  (-> exact-integer? (listof (listof exact-integer?)) boolean?)
  (or (check-dim 0 rectangles)   ; vertical cuts
      (check-dim 1 rectangles)))  ; horizontal cuts
```

## Erlang

```erlang
-export([check_valid_cuts/2]).

-spec check_valid_cuts(N :: integer(), Rectangles :: [[integer()]]) -> boolean().
check_valid_cuts(_N, Rectangles) ->
    can_cut(Rectangles, x) orelse can_cut(Rectangles, y).

%%--------------------------------------------------------------------
%% internal helpers
%%--------------------------------------------------------------------
can_cut([], _Dim) -> false;
can_cut([First|Rest], Dim) ->
    Sorted = lists:sort(fun(R1, R2) -> start_coord(R1, Dim) < start_coord(R2, Dim) end,
                        [First|Rest]),
    MaxEnd0 = end_coord(hd(Sorted), Dim),
    scan(tl(Sorted), Dim, MaxEnd0, 0).

scan([], _Dim, _MaxEnd, GapCount) ->
    GapCount >= 2;
scan([Rect|Rest], Dim, MaxEnd, GapCount) ->
    Start = start_coord(Rect, Dim),
    End   = end_coord(Rect, Dim),
    NewGapCount =
        if
            Start > MaxEnd -> GapCount + 1;
            true          -> GapCount
        end,
    case NewGapCount >= 2 of
        true -> true;
        false ->
            NewMaxEnd = erlang:max(MaxEnd, End),
            scan(Rest, Dim, NewMaxEnd, NewGapCount)
    end.

start_coord([Sx, _Sy, _Ex, _Ey], x) -> Sx;
start_coord([_Sx, Sy, _Ex, _Ey], y) -> Sy.

end_coord([_Sx, _Sy, Ex, _Ey], x) -> Ex;
end_coord([_Sx, _Sy, _Ex, Ey], y) -> Ey.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_valid_cuts(n :: integer, rectangles :: [[integer]]) :: boolean
  def check_valid_cuts(_n, rectangles) do
    vertical = can_cut?(rectangles, 0, 2)
    horizontal = can_cut?(rectangles, 1, 3)
    vertical or horizontal
  end

  defp can_cut?(rects, start_idx, end_idx) do
    sorted = Enum.sort_by(rects, fn r -> Enum.at(r, start_idx) end)

    case sorted do
      [] ->
        false

      [first | rest] ->
        {gap_cnt, _} =
          Enum.reduce(rest, {0, Enum.at(first, end_idx)}, fn rect,
                                                            {cnt, furthest_end} ->
            start = Enum.at(rect, start_idx)
            ending = Enum.at(rect, end_idx)

            cnt =
              if start > furthest_end do
                cnt + 1
              else
                cnt
              end

            new_furthest = max(furthest_end, ending)
            {cnt, new_furthest}
          end)

        gap_cnt >= 2
    end
  end
end
```
