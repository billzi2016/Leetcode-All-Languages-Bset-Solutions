# 1024. Video Stitching

## Cpp

```cpp
class Solution {
public:
    int videoStitching(vector<vector<int>>& clips, int time) {
        sort(clips.begin(), clips.end(), [](const vector<int>& a, const vector<int>& b){
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] > b[1];
        });
        int n = clips.size();
        int ans = 0;
        int curEnd = 0;
        int i = 0;
        while (curEnd < time) {
            int furthest = curEnd;
            while (i < n && clips[i][0] <= curEnd) {
                furthest = max(furthest, clips[i][1]);
                ++i;
            }
            if (furthest == curEnd) return -1; // cannot extend further
            ++ans;
            curEnd = furthest;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int videoStitching(int[][] clips, int time) {
        java.util.Arrays.sort(clips, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return b[1] - a[1];
        });
        int n = clips.length;
        int ans = 0;
        int curEnd = 0;
        int i = 0;
        int maxReach = 0;
        while (curEnd < time) {
            while (i < n && clips[i][0] <= curEnd) {
                if (clips[i][1] > maxReach) {
                    maxReach = clips[i][1];
                }
                i++;
            }
            if (maxReach == curEnd) {
                return -1;
            }
            ans++;
            curEnd = maxReach;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        # Sort by start ascending; if same start, larger end first
        clips.sort(key=lambda x: (x[0], -x[1]))
        n = len(clips)
        i = 0
        cur_end = 0
        ans = 0
        while cur_end < time:
            farthest = cur_end
            # Extend as far as possible with clips starting at or before cur_end
            while i < n and clips[i][0] <= cur_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest == cur_end:  # cannot progress
                return -1
            ans += 1
            cur_end = farthest
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        n = len(clips)
        i = 0
        cnt = 0
        cur_end = 0
        while cur_end < time:
            furthest = cur_end
            while i < n and clips[i][0] <= cur_end:
                furthest = max(furthest, clips[i][1])
                i += 1
            if furthest == cur_end:
                return -1
            cnt += 1
            cur_end = furthest
        return cnt
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->start != ib->start)
        return ia->start - ib->start;
    return ib->end - ia->end; // larger end first when starts equal
}

int videoStitching(int** clips, int clipsSize, int* clipsColSize, int time) {
    if (time == 0) return 0;
    Interval *arr = (Interval *)malloc(sizeof(Interval) * clipsSize);
    for (int i = 0; i < clipsSize; ++i) {
        arr[i].start = clips[i][0];
        arr[i].end   = clips[i][1];
    }
    qsort(arr, clipsSize, sizeof(Interval), cmpInterval);

    int ans = 0;
    int curEnd = 0;
    int nextEnd = 0;
    int i = 0;

    while (curEnd < time) {
        while (i < clipsSize && arr[i].start <= curEnd) {
            if (arr[i].end > nextEnd)
                nextEnd = arr[i].end;
            ++i;
        }
        if (nextEnd == curEnd) { // cannot extend further
            free(arr);
            return -1;
        }
        ++ans;
        curEnd = nextEnd;
    }

    free(arr);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int VideoStitching(int[][] clips, int time) {
        Array.Sort(clips, (a, b) => a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        int n = clips.Length;
        int ans = 0;
        int curEnd = 0;
        int i = 0;
        while (curEnd < time) {
            int furthest = curEnd;
            while (i < n && clips[i][0] <= curEnd) {
                if (clips[i][1] > furthest) furthest = clips[i][1];
                i++;
            }
            if (furthest == curEnd) return -1;
            ans++;
            curEnd = furthest;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} clips
 * @param {number} time
 * @return {number}
 */
var videoStitching = function(clips, time) {
    // Sort by start ascending; if same start, end descending (helps greedy)
    clips.sort((a, b) => a[0] === b[0] ? b[1] - a[1] : a[0] - b[0]);
    
    let ans = 0;
    let curEnd = 0;
    let nextEnd = 0;
    let i = 0;
    const n = clips.length;
    
    while (curEnd < time) {
        // Extend coverage using all clips that start at or before current end
        while (i < n && clips[i][0] <= curEnd) {
            if (clips[i][1] > nextEnd) nextEnd = clips[i][1];
            i++;
        }
        // If we cannot extend further, impossible
        if (nextEnd === curEnd) return -1;
        ans++;
        curEnd = nextEnd;
    }
    
    return ans;
};
```

## Typescript

```typescript
function videoStitching(clips: number[][], time: number): number {
    // Sort clips by start ascending; if same start, end descending
    clips.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

    let ans = 0;
    let curEnd = 0;
    let farthest = 0;
    let i = 0;
    const n = clips.length;

    while (curEnd < time) {
        // Extend coverage using all clips that start at or before current end
        while (i < n && clips[i][0] <= curEnd) {
            if (clips[i][1] > farthest) farthest = clips[i][1];
            i++;
        }
        // If we cannot extend further, it's impossible
        if (farthest === curEnd) return -1;
        ans++;
        curEnd = farthest;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $clips
     * @param Integer $time
     * @return Integer
     */
    function videoStitching($clips, $time) {
        usort($clips, function ($a, $b) {
            if ($a[0] == $b[0]) {
                return $b[1] <=> $a[1];
            }
            return $a[0] <=> $b[0];
        });

        $n = count($clips);
        $i = 0;
        $ans = 0;
        $currEnd = 0;
        $nextEnd = 0;

        while ($currEnd < $time) {
            while ($i < $n && $clips[$i][0] <= $currEnd) {
                if ($clips[$i][1] > $nextEnd) {
                    $nextEnd = $clips[$i][1];
                }
                $i++;
            }

            if ($nextEnd == $currEnd) {
                return -1;
            }

            $ans++;
            $currEnd = $nextEnd;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func videoStitching(_ clips: [[Int]], _ time: Int) -> Int {
        let sorted = clips.sorted { a, b in
            if a[0] == b[0] {
                return a[1] > b[1]
            }
            return a[0] < b[0]
        }
        var ans = 0
        var i = 0
        var curEnd = 0
        var nextEnd = 0
        
        while curEnd < time {
            while i < sorted.count && sorted[i][0] <= curEnd {
                nextEnd = max(nextEnd, sorted[i][1])
                i += 1
            }
            if nextEnd == curEnd {
                return -1
            }
            ans += 1
            curEnd = nextEnd
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun videoStitching(clips: Array<IntArray>, time: Int): Int {
        if (time == 0) return 0
        clips.sortWith(compareBy<IntArray> { it[0] }.thenByDescending { it[1] })
        var ans = 0
        var curEnd = 0
        var i = 0
        val n = clips.size
        while (curEnd < time) {
            var furthest = curEnd
            while (i < n && clips[i][0] <= curEnd) {
                if (clips[i][1] > furthest) furthest = clips[i][1]
                i++
            }
            if (furthest == curEnd) return -1
            ans++
            curEnd = furthest
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int videoStitching(List<List<int>> clips, int time) {
    // Sort clips by start time; if equal, by end descending
    clips.sort((a, b) {
      if (a[0] == b[0]) return a[1] - b[1];
      return a[0] - b[0];
    });

    int ans = 0;
    int curEnd = 0;
    int i = 0;
    int n = clips.length;

    while (curEnd < time) {
      int furthest = curEnd;
      // Extend coverage using all clips that start at or before current end
      while (i < n && clips[i][0] <= curEnd) {
        if (clips[i][1] > furthest) furthest = clips[i][1];
        i++;
      }
      // No clip can extend the current coverage
      if (furthest == curEnd) return -1;
      ans++;
      curEnd = furthest;
    }

    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func videoStitching(clips [][]int, time int) int {
	sort.Slice(clips, func(i, j int) bool {
		if clips[i][0] == clips[j][0] {
			return clips[i][1] > clips[j][1]
		}
		return clips[i][0] < clips[j][0]
	})
	ans, curEnd, nextEnd := 0, 0, 0
	i, n := 0, len(clips)
	for curEnd < time {
		for i < n && clips[i][0] <= curEnd {
			if clips[i][1] > nextEnd {
				nextEnd = clips[i][1]
			}
			i++
		}
		if nextEnd == curEnd {
			return -1
		}
		ans++
		curEnd = nextEnd
	}
	return ans
}
```

## Ruby

```ruby
def video_stitching(clips, time)
  clips.sort_by! { |c| [c[0], -c[1]] }
  ans = 0
  cur_end = 0
  i = 0
  n = clips.length
  while cur_end < time
    furthest = cur_end
    while i < n && clips[i][0] <= cur_end
      furthest = [furthest, clips[i][1]].max
      i += 1
    end
    return -1 if furthest == cur_end
    ans += 1
    cur_end = furthest
  end
  ans
end
```

## Scala

```scala
object Solution {
    def videoStitching(clips: Array[Array[Int]], time: Int): Int = {
        val sorted = clips.sortBy(c => (c(0), -c(1)))
        var ans = 0
        var curEnd = 0
        var i = 0
        val n = sorted.length
        while (curEnd < time) {
            var furthest = curEnd
            while (i < n && sorted(i)(0) <= curEnd) {
                furthest = math.max(furthest, sorted(i)(1))
                i += 1
            }
            if (furthest == curEnd) return -1
            ans += 1
            curEnd = furthest
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn video_stitching(clips: Vec<Vec<i32>>, time: i32) -> i32 {
        let mut clips = clips;
        clips.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut ans = 0;
        let mut cur_end = 0;
        let mut next_end = 0;
        let mut i = 0usize;
        while cur_end < time {
            while i < clips.len() && clips[i][0] <= cur_end {
                if clips[i][1] > next_end {
                    next_end = clips[i][1];
                }
                i += 1;
            }
            if next_end == cur_end {
                return -1;
            }
            ans += 1;
            cur_end = next_end;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (video-stitching clips time)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((sorted
          (sort clips
                (lambda (a b)
                  (or (< (first a) (first b))
                      (and (= (first a) (first b))
                           (> (second a) (second b)))))))
         (vec (list->vector sorted))
         (n   (vector-length vec)))
    (let loop ((i 0) (cur-end 0) (ans 0))
      (if (>= cur-end time)
          ans
          (let inner ((next-end cur-end) (j i))
            (cond
              [(or (= j n)
                   (> (first (vector-ref vec j)) cur-end))
               (if (= next-end cur-end)
                   -1
                   (loop j next-end (+ ans 1)))]
              [else
               (inner (max next-end (second (vector-ref vec j))) (+ j 1))]))))))
```

## Erlang

```erlang
-module(solution).
-export([video_stitching/2]).

-spec video_stitching(Clips :: [[integer()]], Time :: integer()) -> integer().
video_stitching(Clips, Time) ->
    Sorted = lists:sort(fun compare/2, Clips),
    go(Sorted, Time, 0, 0, 0).

compare([S1,_], [S2,_]) -> S1 < S2.

go(_Sorted, Time, CurEnd, _NextEnd, Count) when CurEnd >= Time ->
    Count;
go([], _Time, _CurEnd, _NextEnd, _Count) ->
    -1;
go(Clips, Time, CurEnd, _NextEnd, Count) ->
    {NewEnd, Rest} = take_clips(Clips, CurEnd, CurEnd),
    case NewEnd > CurEnd of
        true -> go(Rest, Time, NewEnd, 0, Count + 1);
        false -> -1
    end.

take_clips([], _CurEnd, Max) ->
    {Max, []};
take_clips([[S,E]|Rest], CurEnd, Max) when S =< CurEnd ->
    NewMax = erlang:max(E, Max),
    take_clips(Rest, CurEnd, NewMax);
take_clips(List, _CurEnd, Max) ->
    {Max, List}.
```

## Elixir

```elixir
defmodule Solution do
  @spec video_stitching(clips :: [[integer]], time :: integer) :: integer
  def video_stitching(clips, time) do
    sorted = Enum.sort_by(clips, fn [s, _] -> s end)
    greedy(sorted, time, 0, 0)
  end

  defp greedy(_clips, time, cur_end, ans) when cur_end >= time, do: ans

  defp greedy(clips, time, cur_end, ans) do
    {max_reach, rest} = take_while_start_leq(clips, cur_end, cur_end)

    if max_reach == cur_end do
      -1
    else
      greedy(rest, time, max_reach, ans + 1)
    end
  end

  defp take_while_start_leq([], _cur_end, max), do: {max, []}

  defp take_while_start_leq([[s, e] | tail] = list, cur_end, max) when s <= cur_end do
    new_max = if e > max, do: e, else: max
    take_while_start_leq(tail, cur_end, new_max)
  end

  defp take_while_start_leq(list, _cur_end, max), do: {max, list}
end
```
