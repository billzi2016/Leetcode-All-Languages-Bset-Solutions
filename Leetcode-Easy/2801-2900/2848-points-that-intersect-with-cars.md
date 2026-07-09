# 2848. Points That Intersect With Cars

## Cpp

```cpp
class Solution {
public:
    int numberOfPoints(vector<vector<int>>& nums) {
        sort(nums.begin(), nums.end());
        int ans = 0;
        int curStart = -1, curEnd = -1;
        for (auto& seg : nums) {
            int l = seg[0], r = seg[1];
            if (curStart == -1) {
                curStart = l;
                curEnd = r;
            } else if (l <= curEnd) { // overlap
                curEnd = max(curEnd, r);
            } else {
                ans += curEnd - curStart + 1;
                curStart = l;
                curEnd = r;
            }
        }
        if (curStart != -1) ans += curEnd - curStart + 1;
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {
        boolean[] covered = new boolean[101]; // indices 0..100, we use 1..100
        for (List<Integer> interval : nums) {
            int start = interval.get(0);
            int end = interval.get(1);
            for (int i = start; i <= end; i++) {
                covered[i] = true;
            }
        }
        int count = 0;
        for (boolean b : covered) {
            if (b) count++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        covered = set()
        for start, end in nums:
            covered.update(range(start, end + 1))
        return len(covered)
```

## Python3

```python
from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for start, end in nums:
            points.update(range(start, end + 1))
        return len(points)
```

## C

```c
int numberOfPoints(int** nums, int numsSize, int* numsColSize){
    int visited[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int start = nums[i][0];
        int end = nums[i][1];
        for (int p = start; p <= end; ++p) {
            visited[p] = 1;
        }
    }
    int count = 0;
    for (int i = 0; i <= 100; ++i) {
        if (visited[i]) ++count;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfPoints(IList<IList<int>> nums) {
        var intervals = new List<(int start, int end)>();
        foreach (var p in nums) {
            intervals.Add((p[0], p[1]));
        }
        intervals.Sort((a, b) => a.start.CompareTo(b.start));
        
        int total = 0;
        int curStart = intervals[0].start;
        int curEnd = intervals[0].end;
        
        for (int i = 1; i < intervals.Count; i++) {
            var (s, e) = intervals[i];
            if (s <= curEnd + 1) {
                // Overlapping or contiguous
                if (e > curEnd) curEnd = e;
            } else {
                total += curEnd - curStart + 1;
                curStart = s;
                curEnd = e;
            }
        }
        total += curEnd - curStart + 1;
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} nums
 * @return {number}
 */
var numberOfPoints = function(nums) {
    if (nums.length === 0) return 0;
    // Sort intervals by start point
    nums.sort((a, b) => a[0] - b[0]);
    
    let total = 0;
    let curStart = nums[0][0];
    let curEnd = nums[0][1];
    
    for (let i = 1; i < nums.length; i++) {
        const [s, e] = nums[i];
        if (s > curEnd) { // no overlap
            total += curEnd - curStart + 1;
            curStart = s;
            curEnd = e;
        } else { // overlap, merge
            curEnd = Math.max(curEnd, e);
        }
    }
    
    total += curEnd - curStart + 1; // add last merged interval
    return total;
};
```

## Typescript

```typescript
function numberOfPoints(nums: number[][]): number {
    const covered = new Array(101).fill(false);
    for (const [start, end] of nums) {
        for (let i = start; i <= end; i++) {
            covered[i] = true;
        }
    }
    let count = 0;
    for (let i = 0; i < covered.length; i++) {
        if (covered[i]) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer
     */
    function numberOfPoints($nums) {
        $covered = [];
        foreach ($nums as $interval) {
            $start = $interval[0];
            $end   = $interval[1];
            for ($i = $start; $i <= $end; $i++) {
                $covered[$i] = true;
            }
        }
        return count($covered);
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPoints(_ nums: [[Int]]) -> Int {
        var points = Set<Int>()
        for interval in nums {
            let start = interval[0]
            let end = interval[1]
            if start <= end {
                for p in start...end {
                    points.insert(p)
                }
            }
        }
        return points.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPoints(nums: List<List<Int>>): Int {
        val covered = BooleanArray(101)
        for (interval in nums) {
            val start = interval[0]
            val end = interval[1]
            for (p in start..end) {
                covered[p] = true
            }
        }
        var count = 0
        for (c in covered) if (c) count++
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPoints(List<List<int>> nums) {
    const int maxCoord = 100;
    List<bool> covered = List.filled(maxCoord + 1, false);
    for (var interval in nums) {
      int start = interval[0];
      int end = interval[1];
      for (int i = start; i <= end; ++i) {
        covered[i] = true;
      }
    }
    int count = 0;
    for (bool isCovered in covered) {
      if (isCovered) count++;
    }
    return count;
  }
}
```

## Golang

```go
func numberOfPoints(nums [][]int) int {
	covered := make([]bool, 101)
	for _, interval := range nums {
		start, end := interval[0], interval[1]
		for i := start; i <= end; i++ {
			covered[i] = true
		}
	}
	count := 0
	for _, v := range covered {
		if v {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def number_of_points(nums)
  return 0 if nums.empty?
  intervals = nums.sort_by { |a| a[0] }
  cur_start, cur_end = intervals[0]
  total = 0
  intervals[1..-1].each do |s, e|
    if s <= cur_end
      cur_end = [cur_end, e].max
    else
      total += cur_end - cur_start + 1
      cur_start, cur_end = s, e
    end
  end
  total + (cur_end - cur_start + 1)
end
```

## Scala

```scala
object Solution {
    def numberOfPoints(nums: List[List[Int]]): Int = {
        val covered = scala.collection.mutable.HashSet[Int]()
        for (interval <- nums) {
            val start = interval(0)
            val end = interval(1)
            var i = start
            while (i <= end) {
                covered += i
                i += 1
            }
        }
        covered.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_points(nums: Vec<Vec<i32>>) -> i32 {
        let mut intervals = nums;
        intervals.sort_by_key(|v| v[0]);
        let mut total = 0i32;
        let mut cur_start = intervals[0][0];
        let mut cur_end = intervals[0][1];
        for iv in intervals.iter().skip(1) {
            let s = iv[0];
            let e = iv[1];
            if s <= cur_end + 1 {
                if e > cur_end {
                    cur_end = e;
                }
            } else {
                total += cur_end - cur_start + 1;
                cur_start = s;
                cur_end = e;
            }
        }
        total += cur_end - cur_start + 1;
        total
    }
}
```

## Racket

```racket
(define/contract (number-of-points nums)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ((present (make-vector 101 #f)))
    (for-each
     (lambda (interval)
       (let ((s (first interval))
             (e (second interval)))
         (for ([i (in-range s (+ e 1))])
           (vector-set! present i #t))))
     nums)
    (let loop ((i 0) (cnt 0))
      (if (> i 100)
          cnt
          (loop (+ i 1) (if (vector-ref present i) (+ cnt 1) cnt))))))
```

## Erlang

```erlang
-spec number_of_points(Nums :: [[integer()]]) -> integer().
number_of_points(Nums) ->
    Sorted = lists:sort(fun([A,_], [B,_]) -> A =< B end, Nums),
    case Sorted of
        [] -> 0;
        [[S,E]|Rest] ->
            merge_intervals(Rest, S, E, 0)
    end.

merge_intervals([], CurStart, CurEnd, Acc) ->
    Acc + (CurEnd - CurStart + 1);
merge_intervals([[S,E]|Tail], CurStart, CurEnd, Acc) ->
    if
        S =< CurEnd ->
            NewEnd = erlang:max(CurEnd, E),
            merge_intervals(Tail, CurStart, NewEnd, Acc);
        true ->
            NewAcc = Acc + (CurEnd - CurStart + 1),
            merge_intervals(Tail, S, E, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_points(nums :: [[integer]]) :: integer
  def number_of_points(nums) do
    {total, last_interval} =
      nums
      |> Enum.sort_by(fn [s, _] -> s end)
      |> Enum.reduce({0, nil}, fn [s, e], {acc, cur} ->
        case cur do
          nil ->
            {acc, {s, e}}

          {cs, ce} ->
            if s <= ce do
              # Overlapping intervals, merge them
              {acc, {cs, max(ce, e)}}
            else
              # Disjoint interval, add length of previous and start new
              {acc + (ce - cs + 1), {s, e}}
            end
        end
      end)

    case last_interval do
      nil -> total
      {cs, ce} -> total + (ce - cs + 1)
    end
  end
end
```
