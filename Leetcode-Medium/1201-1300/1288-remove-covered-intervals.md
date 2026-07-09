# 1288. Remove Covered Intervals

## Cpp

```cpp
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 if (a[0] != b[0]) return a[0] < b[0];
                 return a[1] > b[1]; // longer interval first when starts equal
             });
        int count = 0;
        int maxEnd = -1;
        for (const auto& iv : intervals) {
            if (iv[1] > maxEnd) {
                ++count;
                maxEnd = iv[1];
            }
        }
        return count;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]); // descending end when starts equal
        });
        int count = 0;
        int maxEnd = -1;
        for (int[] interval : intervals) {
            if (interval[1] > maxEnd) {
                count++;
                maxEnd = interval[1];
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by start ascending; for same start, larger end first
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_end = -1
        for _, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        return count
```

## Python3

```python
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_end = -1
        for _, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        return count
```

## C

```c
#include <stdlib.h>

static int cmp(const void *p1, const void *p2) {
    int *a = *(int **)p1;
    int *b = *(int **)p2;
    if (a[0] != b[0]) return a[0] - b[0];
    return b[1] - a[1];
}

int removeCoveredIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    qsort(intervals, intervalsSize, sizeof(int *), cmp);
    int count = 0;
    int max_end = -1;
    for (int i = 0; i < intervalsSize; ++i) {
        int end = intervals[i][1];
        if (end > max_end) {
            ++count;
            max_end = end;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int RemoveCoveredIntervals(int[][] intervals) {
        System.Array.Sort(intervals, (a, b) => {
            if (a[0] != b[0]) return a[0].CompareTo(b[0]);
            return b[1].CompareTo(a[1]); // descending end when starts equal
        });
        int count = 0;
        int maxEnd = -1;
        foreach (var interval in intervals) {
            if (interval[1] > maxEnd) {
                count++;
                maxEnd = interval[1];
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var removeCoveredIntervals = function(intervals) {
    intervals.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return b[1] - a[1];
    });
    let count = 0;
    let maxEnd = -Infinity;
    for (const [_, end] of intervals) {
        if (end > maxEnd) {
            count++;
            maxEnd = end;
        }
    }
    return count;
};
```

## Typescript

```typescript
function removeCoveredIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return b[1] - a[1];
    });
    let count = 0;
    let maxEnd = -1;
    for (const [, r] of intervals) {
        if (r > maxEnd) {
            count++;
            maxEnd = r;
        }
    }
    return count;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function removeCoveredIntervals($intervals) {
        usort($intervals, function($a, $b) {
            if ($a[0] == $b[0]) {
                return $b[1] <=> $a[1];
            }
            return $a[0] <=> $b[0];
        });
        $count = 0;
        $maxEnd = -1;
        foreach ($intervals as $int) {
            if ($int[1] > $maxEnd) {
                $count++;
                $maxEnd = $int[1];
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func removeCoveredIntervals(_ intervals: [[Int]]) -> Int {
        let sorted = intervals.sorted { (a, b) -> Bool in
            if a[0] == b[0] {
                return a[1] > b[1]
            }
            return a[0] < b[0]
        }
        var count = 0
        var maxEnd = -1
        for interval in sorted {
            let end = interval[1]
            if end > maxEnd {
                count += 1
                maxEnd = end
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeCoveredIntervals(intervals: Array<IntArray>): Int {
        intervals.sortWith(Comparator { a, b ->
            if (a[0] != b[0]) a[0] - b[0] else b[1] - a[1]
        })
        var count = 0
        var maxEnd = -1
        for (interval in intervals) {
            val end = interval[1]
            if (end > maxEnd) {
                count++
                maxEnd = end
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int removeCoveredIntervals(List<List<int>> intervals) {
    intervals.sort((a, b) {
      if (a[0] != b[0]) return a[0] - b[0];
      return b[1] - a[1];
    });
    int count = 0;
    int maxEnd = -1;
    for (var interval in intervals) {
      int end = interval[1];
      if (end > maxEnd) {
        count++;
        maxEnd = end;
      }
    }
    return count;
  }
}
```

## Golang

```go
import "sort"

func removeCoveredIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] > intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})
	count := 0
	maxEnd := -1
	for _, iv := range intervals {
		if iv[1] > maxEnd {
			count++
			maxEnd = iv[1]
		}
	}
	return count
}
```

## Ruby

```ruby
def remove_covered_intervals(intervals)
  intervals.sort_by! { |l, r| [l, -r] }
  count = 0
  max_end = -1
  intervals.each do |l, r|
    if r > max_end
      count += 1
      max_end = r
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def removeCoveredIntervals(intervals: Array[Array[Int]]): Int = {
        val sorted = intervals.sortWith { (a, b) =>
            if (a(0) != b(0)) a(0) < b(0)
            else a(1) > b(1)
        }
        var count = 0
        var maxEnd = -1
        for (intv <- sorted) {
            val end = intv(1)
            if (end > maxEnd) {
                count += 1
                maxEnd = end
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_covered_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        // Sort by start asc, and for equal starts sort by end desc
        intervals.sort_by(|a, b| {
            if a[0] != b[0] {
                a[0].cmp(&b[0])
            } else {
                b[1].cmp(&a[1])
            }
        });

        let mut count = 0;
        let mut max_end = -1i32;

        for intv in intervals.iter() {
            if intv[1] > max_end {
                count += 1;
                max_end = intv[1];
            }
        }

        count as i32
    }
}
```

## Racket

```racket
(define/contract (remove-covered-intervals intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted
          (sort intervals
                (lambda (a b)
                  (or (< (first a) (first b))
                      (and (= (first a) (first b))
                           (> (second a) (second b))))))))
    (let loop ((lst sorted) (max-end -1) (count 0))
      (if (null? lst)
          count
          (let* ((curr (car lst))
                 (end (second curr)))
            (if (<= end max-end)
                (loop (cdr lst) max-end count)
                (loop (cdr lst) end (+ count 1))))))))
```

## Erlang

```erlang
-spec remove_covered_intervals(Intervals :: [[integer()]]) -> integer().
remove_covered_intervals(Intervals) ->
    Sorted = lists:sort(fun compare/2, Intervals),
    {Count,_} = lists:foldl(
        fun([_,R], {Cnt,Max}) ->
            if R =< Max -> {Cnt,Max};
               true     -> {Cnt+1,R}
            end
        end,
        {0,-1},
        Sorted),
    Count.

compare([L1,_],[L2,_]) when L1 < L2 -> true;
compare([L1,_],[L2,_]) when L1 > L2 -> false;
compare([_,R1],[_,R2]) -> R1 > R2.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_covered_intervals(intervals :: [[integer]]) :: integer
  def remove_covered_intervals(intervals) do
    sorted = Enum.sort_by(intervals, fn [l, r] -> {l, -r} end)

    {count, _} =
      Enum.reduce(sorted, {0, -1}, fn [_l, r], {cnt, max_r} ->
        if r <= max_r do
          {cnt, max_r}
        else
          {cnt + 1, r}
        end
      end)

    count
  end
end
```
