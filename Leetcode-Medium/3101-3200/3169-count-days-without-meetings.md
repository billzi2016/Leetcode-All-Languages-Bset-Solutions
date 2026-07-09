# 3169. Count Days Without Meetings

## Cpp

```cpp
class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 if (a[0] != b[0]) return a[0] < b[0];
                 return a[1] < b[1];
             });
        long long freeDays = 0;
        int latestEnd = 0;
        for (const auto& m : meetings) {
            int start = m[0], end = m[1];
            if (start > latestEnd + 1) {
                freeDays += start - latestEnd - 1;
            }
            if (end > latestEnd) latestEnd = end;
        }
        if (days > latestEnd) freeDays += days - latestEnd;
        return static_cast<int>(freeDays);
    }
};
```

## Java

```java
class Solution {
    public int countDays(int days, int[][] meetings) {
        if (meetings == null || meetings.length == 0) {
            return days;
        }
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        long free = 0;
        int latestEnd = 0;
        for (int[] m : meetings) {
            int start = m[0];
            int end = m[1];
            if (start > latestEnd + 1) {
                free += (long) start - latestEnd - 1;
            }
            if (end > latestEnd) {
                latestEnd = end;
            }
        }
        free += (long) days - latestEnd;
        return (int) free;
    }
}
```

## Python

```python
class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # Sort meetings by start day
        meetings.sort(key=lambda x: x[0])
        free_days = 0
        latest_end = 0  # the farthest day covered by processed meetings
        
        for start, end in meetings:
            if start > latest_end + 1:
                # Gap between the last covered day and current meeting's start
                free_days += start - latest_end - 1
            # Extend the covered range
            if end > latest_end:
                latest_end = end
        
        # Days after the last meeting till 'days'
        if days > latest_end:
            free_days += days - latest_end
        
        return free_days
```

## Python3

```python
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free_days = 0
        latest_end = 0
        for start, end in meetings:
            if start > latest_end + 1:
                free_days += start - latest_end - 1
            if end > latest_end:
                latest_end = end
        if days > latest_end:
            free_days += days - latest_end
        return free_days
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

static int compareIntervals(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->start != ib->start)
        return ia->start - ib->start;
    return ia->end - ib->end;
}

int countDays(int days, int** meetings, int meetingsSize, int* meetingsColSize) {
    if (meetingsSize == 0) return days;

    Interval *arr = (Interval *)malloc(sizeof(Interval) * meetingsSize);
    for (int i = 0; i < meetingsSize; ++i) {
        arr[i].start = meetings[i][0];
        arr[i].end   = meetings[i][1];
    }

    qsort(arr, meetingsSize, sizeof(Interval), compareIntervals);

    long long freeDays = 0;
    int latestEnd = 0;

    for (int i = 0; i < meetingsSize; ++i) {
        if (arr[i].start > latestEnd + 1) {
            freeDays += (long long)arr[i].start - latestEnd - 1;
        }
        if (arr[i].end > latestEnd) {
            latestEnd = arr[i].end;
        }
    }

    if (days > latestEnd) {
        freeDays += (long long)days - latestEnd;
    }

    free(arr);
    return (int)freeDays;
}
```

## Csharp

```csharp
public class Solution {
    public int CountDays(int days, int[][] meetings) {
        if (meetings == null || meetings.Length == 0) return days;
        System.Array.Sort(meetings, (a, b) => a[0].CompareTo(b[0]));
        long free = 0;
        int latestEnd = 0;
        foreach (var m in meetings) {
            int start = m[0];
            int end = m[1];
            if (start > latestEnd + 1) {
                free += start - latestEnd - 1;
            }
            if (end > latestEnd) latestEnd = end;
        }
        if (days > latestEnd) {
            free += days - latestEnd;
        }
        return (int)free;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} days
 * @param {number[][]} meetings
 * @return {number}
 */
var countDays = function(days, meetings) {
    // Sort meetings by start day (and end day for tie-breaking)
    meetings.sort((a, b) => {
        if (a[0] === b[0]) return a[1] - b[1];
        return a[0] - b[0];
    });
    
    let freeDays = 0;
    let latestEnd = 0; // no meeting before day 1
    
    for (const [start, end] of meetings) {
        if (start > latestEnd + 1) {
            freeDays += start - latestEnd - 1;
        }
        if (end > latestEnd) {
            latestEnd = end;
        }
    }
    
    // Days after the last meeting
    if (days > latestEnd) {
        freeDays += days - latestEnd;
    }
    
    return freeDays;
};
```

## Typescript

```typescript
function countDays(days: number, meetings: number[][]): number {
    // Sort meetings by start day (and end day for tie-breaking)
    meetings.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1];
    });

    let freeDays = 0;
    let latestEnd = 0; // no meeting yet, so day 0 is the last occupied day

    for (const [start, end] of meetings) {
        if (start > latestEnd + 1) {
            freeDays += start - latestEnd - 1;
        }
        if (end > latestEnd) {
            latestEnd = end;
        }
    }

    // Add remaining days after the last meeting
    if (days > latestEnd) {
        freeDays += days - latestEnd;
    }

    return freeDays;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $days
     * @param Integer[][] $meetings
     * @return Integer
     */
    function countDays($days, $meetings) {
        usort($meetings, function ($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1];
            }
            return $a[0] <=> $b[0];
        });

        $free = 0;
        $latestEnd = 0;

        foreach ($meetings as $m) {
            $start = $m[0];
            $end   = $m[1];

            if ($start > $latestEnd + 1) {
                $free += $start - $latestEnd - 1;
            }

            if ($end > $latestEnd) {
                $latestEnd = $end;
            }
        }

        if ($days > $latestEnd) {
            $free += $days - $latestEnd;
        }

        return $free;
    }
}
```

## Swift

```swift
class Solution {
    func countDays(_ days: Int, _ meetings: [[Int]]) -> Int {
        var sortedMeetings = meetings.sorted { $0[0] < $1[0] }
        var freeDays = 0
        var latestEnd = 0
        
        for meeting in sortedMeetings {
            let start = meeting[0]
            let end = meeting[1]
            
            if start > latestEnd + 1 {
                freeDays += start - latestEnd - 1
            }
            if end > latestEnd {
                latestEnd = end
            }
        }
        
        if days > latestEnd {
            freeDays += days - latestEnd
        }
        return freeDays
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countDays(days: Int, meetings: Array<IntArray>): Int {
        if (meetings.isEmpty()) return days
        val sorted = meetings.sortedWith(compareBy<IntArray> { it[0] })
        var freeDays = 0L
        var latestEnd = 0
        for (m in sorted) {
            val start = m[0]
            val end = m[1]
            if (start > latestEnd + 1) {
                freeDays += (start - latestEnd - 1).toLong()
            }
            if (end > latestEnd) latestEnd = end
        }
        if (days > latestEnd) {
            freeDays += (days - latestEnd).toLong()
        }
        return freeDays.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countDays(int days, List<List<int>> meetings) {
    if (meetings.isEmpty) return days;
    meetings.sort((a, b) => a[0].compareTo(b[0]));
    int freeDays = 0;
    int latestEnd = 0;
    for (var m in meetings) {
      int start = m[0];
      int end = m[1];
      if (start > latestEnd + 1) {
        freeDays += start - latestEnd - 1;
      }
      if (end > latestEnd) {
        latestEnd = end;
      }
    }
    freeDays += days - latestEnd;
    return freeDays;
  }
}
```

## Golang

```go
import "sort"

func countDays(days int, meetings [][]int) int {
	if len(meetings) == 0 {
		return days
	}
	sort.Slice(meetings, func(i, j int) bool {
		if meetings[i][0] == meetings[j][0] {
			return meetings[i][1] < meetings[j][1]
		}
		return meetings[i][0] < meetings[j][0]
	})
	free := 0
	latestEnd := 0
	for _, m := range meetings {
		start, end := m[0], m[1]
		if start > latestEnd+1 {
			free += start - latestEnd - 1
		}
		if end > latestEnd {
			latestEnd = end
		}
	}
	if days > latestEnd {
		free += days - latestEnd
	}
	return free
}
```

## Ruby

```ruby
def count_days(days, meetings)
  meetings.sort_by! { |s, e| [s, e] }
  free = 0
  latest_end = 0
  meetings.each do |s, e|
    if s > latest_end + 1
      free += s - latest_end - 1
    end
    latest_end = e if e > latest_end
  end
  free + (days - latest_end)
end
```

## Scala

```scala
object Solution {
    def countDays(days: Int, meetings: Array[Array[Int]]): Int = {
        if (meetings.isEmpty) return days
        val sorted = meetings.sortBy(_(0))
        var latestEnd = 0
        var freeDays: Long = 0L
        for (m <- sorted) {
            val start = m(0)
            val end = m(1)
            if (start > latestEnd + 1) {
                freeDays += (start - latestEnd - 1).toLong
            }
            if (end > latestEnd) latestEnd = end
        }
        freeDays += (days - latestEnd).toLong
        freeDays.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_days(days: i32, mut meetings: Vec<Vec<i32>>) -> i32 {
        meetings.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut latest_end = 0i32;
        let mut free: i64 = 0;
        for m in meetings.iter() {
            let start = m[0];
            let end = m[1];
            if start > latest_end + 1 {
                free += (start - latest_end - 1) as i64;
            }
            if end > latest_end {
                latest_end = end;
            }
        }
        if days > latest_end {
            free += (days - latest_end) as i64;
        }
        free as i32
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (count-days days meetings)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted (sort meetings < #:key car)))
    (let loop ((lst sorted) (latest-end 0) (free 0))
      (if (null? lst)
          (+ free (- days latest-end))
          (let* ((m (car lst))
                 (s (car m))
                 (e (cadr m))
                 (gap (if (> s (+ latest-end 1))
                          (- s latest-end 1)
                          0))
                 (new-free (+ free gap))
                 (new-latest (max latest-end e)))
            (loop (cdr lst) new-latest new-free))))))
```

## Erlang

```erlang
-module(solution).
-export([count_days/2]).

-spec count_days(Days :: integer(), Meetings :: [[integer()]]) -> integer().
count_days(Days, Meetings) ->
    Sorted = lists:sort(fun([S1,_], [S2,_]) -> S1 < S2 end, Meetings),
    {LastEnd, Free} = lists:foldl(
        fun([Start, End], {CurEnd, Acc}) ->
            Gap = if
                Start > CurEnd + 1 -> Start - CurEnd - 1;
                true -> 0
            end,
            NewAcc = Acc + Gap,
            NewEnd = erlang:max(CurEnd, End),
            {NewEnd, NewAcc}
        end,
        {0, 0},
        Sorted),
    Free + (Days - LastEnd).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_days(days :: integer, meetings :: [[integer]]) :: integer
  def count_days(days, meetings) do
    sorted = Enum.sort_by(meetings, fn [s, _] -> s end)

    {free, latest_end} =
      Enum.reduce(sorted, {0, 0}, fn [s, e], {free_acc, latest_acc} ->
        free_acc =
          if s > latest_acc + 1 do
            free_acc + (s - latest_acc - 1)
          else
            free_acc
          end

        latest_acc = max(latest_acc, e)
        {free_acc, latest_acc}
      end)

    free + days - latest_end
  end
end
```
