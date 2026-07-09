# 1964. Find the Longest Valid Obstacle Course at Each Position

## Cpp

```cpp
class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        vector<int> dp;
        vector<int> ans;
        ans.reserve(obstacles.size());
        for (int h : obstacles) {
            int idx = upper_bound(dp.begin(), dp.end(), h) - dp.begin();
            if (idx == (int)dp.size()) dp.push_back(h);
            else dp[idx] = h;
            ans.push_back(idx + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        int n = obstacles.length;
        int[] ans = new int[n];
        int[] tails = new int[n];
        int size = 0;
        for (int i = 0; i < n; i++) {
            int x = obstacles[i];
            int l = 0, r = size;
            while (l < r) {
                int m = (l + r) >>> 1;
                if (tails[m] > x) {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
            int pos = l; // first index where tails[pos] > x
            ans[i] = pos + 1;
            tails[pos] = x;
            if (pos == size) {
                size++;
            }
        }
        return ans;
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        tails = []
        ans = []
        for x in obstacles:
            idx = bisect.bisect_right(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
            ans.append(idx + 1)
        return ans
```

## Python3

```python
from typing import List
from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tails = []
        ans = []
        for h in obstacles:
            idx = bisect_right(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
            ans.append(idx + 1)
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestObstacleCourseAtEachPosition(int* obstacles, int obstaclesSize, int* returnSize) {
    int *ans = (int*)malloc(obstaclesSize * sizeof(int));
    int *tails = (int*)malloc(obstaclesSize * sizeof(int));
    int len = 0;
    
    for (int i = 0; i < obstaclesSize; ++i) {
        int x = obstacles[i];
        int lo = 0, hi = len;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (tails[mid] <= x)
                lo = mid + 1;
            else
                hi = mid;
        }
        int pos = lo;               // first index with tails[pos] > x
        ans[i] = pos + 1;           // length of longest non‑decreasing subsequence ending at i
        
        if (pos == len) {
            tails[len++] = x;
        } else {
            tails[pos] = x;
        }
    }
    
    free(tails);
    *returnSize = obstaclesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] LongestObstacleCourseAtEachPosition(int[] obstacles)
    {
        int n = obstacles.Length;
        int[] ans = new int[n];
        int[] tails = new int[n];
        int size = 0;

        for (int i = 0; i < n; i++)
        {
            int x = obstacles[i];
            int l = 0, r = size;
            while (l < r)
            {
                int m = (l + r) >> 1;
                if (tails[m] <= x)
                    l = m + 1;
                else
                    r = m;
            }
            int pos = l;
            tails[pos] = x;
            if (pos == size) size++;
            ans[i] = pos + 1;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} obstacles
 * @return {number[]}
 */
var longestObstacleCourseAtEachPosition = function(obstacles) {
    const tails = [];
    const ans = new Array(obstacles.length);
    for (let i = 0; i < obstacles.length; i++) {
        const x = obstacles[i];
        // find first index where tails[idx] > x
        let l = 0, r = tails.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (tails[m] <= x) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        const pos = l; // length of longest non‑decreasing subsequence ending here minus 1
        ans[i] = pos + 1;
        if (pos === tails.length) {
            tails.push(x);
        } else {
            tails[pos] = x;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function longestObstacleCourseAtEachPosition(obstacles: number[]): number[] {
    const n = obstacles.length;
    const ans = new Array<number>(n);
    const tails: number[] = [];
    for (let i = 0; i < n; ++i) {
        const h = obstacles[i];
        // binary search for first element > h
        let l = 0, r = tails.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (tails[m] <= h) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        const idx = l;
        if (idx === tails.length) {
            tails.push(h);
        } else {
            tails[idx] = h;
        }
        ans[i] = idx + 1;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $obstacles
     * @return Integer[]
     */
    function longestObstacleCourseAtEachPosition($obstacles) {
        $n = count($obstacles);
        $ans = array_fill(0, $n, 0);
        $tails = [];
        foreach ($obstacles as $i => $h) {
            $l = 0;
            $r = count($tails) - 1;
            while ($l <= $r) {
                $mid = intdiv($l + $r, 2);
                if ($tails[$mid] <= $h) {
                    $l = $mid + 1;
                } else {
                    $r = $mid - 1;
                }
            }
            if ($l == count($tails)) {
                $tails[] = $h;
            } else {
                $tails[$l] = $h;
            }
            $ans[$i] = $l + 1;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestObstacleCourseAtEachPosition(_ obstacles: [Int]) -> [Int] {
        var tails = [Int]()
        var answer = [Int]()
        answer.reserveCapacity(obstacles.count)
        
        for h in obstacles {
            var left = 0
            var right = tails.count
            while left < right {
                let mid = (left + right) >> 1
                if tails[mid] <= h {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            // left is the first index with value > h (upper bound)
            if left == tails.count {
                tails.append(h)
            } else {
                tails[left] = h
            }
            answer.append(left + 1)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestObstacleCourseAtEachPosition(obstacles: IntArray): IntArray {
        val n = obstacles.size
        val ans = IntArray(n)
        val tails = IntArray(n)
        var size = 0
        for (i in 0 until n) {
            val x = obstacles[i]
            var l = 0
            var r = size
            while (l < r) {
                val m = (l + r) ushr 1
                if (tails[m] <= x) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            tails[l] = x
            if (l == size) size++
            ans[i] = l + 1
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> longestObstacleCourseAtEachPosition(List<int> obstacles) {
    List<int> tails = [];
    int n = obstacles.length;
    List<int> ans = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int val = obstacles[i];
      int l = 0, r = tails.length;
      while (l < r) {
        int m = (l + r) >> 1;
        if (tails[m] <= val) {
          l = m + 1;
        } else {
          r = m;
        }
      }
      int idx = l;
      if (idx == tails.length) {
        tails.add(val);
      } else {
        tails[idx] = val;
      }
      ans[i] = idx + 1;
    }
    return ans;
  }
}
```

## Golang

```go
func longestObstacleCourseAtEachPosition(obstacles []int) []int {
    n := len(obstacles)
    ans := make([]int, n)
    tails := make([]int, 0, n)
    for i, h := range obstacles {
        lo, hi := 0, len(tails)
        for lo < hi {
            mid := (lo + hi) >> 1
            if tails[mid] <= h {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        if lo == len(tails) {
            tails = append(tails, h)
        } else {
            tails[lo] = h
        }
        ans[i] = lo + 1
    }
    return ans
}
```

## Ruby

```ruby
def longest_obstacle_course_at_each_position(obstacles)
  tails = []
  ans = Array.new(obstacles.size)
  obstacles.each_with_index do |h, i|
    l = 0
    r = tails.length
    while l < r
      m = (l + r) / 2
      if tails[m] <= h
        l = m + 1
      else
        r = m
      end
    end
    pos = l
    if pos == tails.length
      tails << h
    else
      tails[pos] = h
    end
    ans[i] = pos + 1
  end
  ans
end
```

## Scala

```scala
object Solution {
  def longestObstacleCourseAtEachPosition(obstacles: Array[Int]): Array[Int] = {
    import scala.collection.mutable.ArrayBuffer
    val tails = new ArrayBuffer[Int]()
    val n = obstacles.length
    val ans = new Array[Int](n)
    for (i <- 0 until n) {
      val x = obstacles(i)
      var l = 0
      var r = tails.length
      while (l < r) {
        val m = (l + r) >>> 1
        if (tails(m) <= x) l = m + 1 else r = m
      }
      val idx = l
      if (idx == tails.length) tails += x else tails(idx) = x
      ans(i) = idx + 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_obstacle_course_at_each_position(obstacles: Vec<i32>) -> Vec<i32> {
        let n = obstacles.len();
        let mut ans = vec![0i32; n];
        let mut tails: Vec<i32> = Vec::new(); // tails[i] = min possible tail for length i+1

        for (i, &h) in obstacles.iter().enumerate() {
            // upper_bound: first index where tails[idx] > h
            let mut l = 0usize;
            let mut r = tails.len();
            while l < r {
                let m = (l + r) / 2;
                if tails[m] <= h {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            let idx = l;
            if idx == tails.len() {
                tails.push(h);
            } else {
                tails[idx] = h;
            }
            ans[i] = (idx + 1) as i32;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (longest-obstacle-course-at-each-position obstacles)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length obstacles))
         (obs-vec (list->vector obstacles))
         (tails (make-vector n 0))
         (ans   (make-vector n 0)))
    (let loop ((i 0) (len 0))
      (if (= i n)
          (vector->list ans)
          (let* ((x (vector-ref obs-vec i))
                 ;; upper bound: first index with value > x
                 (pos (let ub ((lo 0) (hi len))
                        (if (= lo hi)
                            lo
                            (let* ((mid (quotient (+ lo hi) 2))
                                   (mid-val (vector-ref tails mid)))
                              (if (> mid-val x)
                                  (ub lo mid)
                                  (ub (+ mid 1) hi)))))))
            (vector-set! ans i (+ pos 1))
            (vector-set! tails pos x)
            (loop (+ i 1) (if (= pos len) (+ len 1) len)))))))
```

## Erlang

```erlang
-define(INF, 20000001).
 
-export([longest_obstacle_course_at_each_position/1]).
 
-spec longest_obstacle_course_at_each_position(Obstacles :: [integer()]) -> [integer()].
longest_obstacle_course_at_each_position(Obstacles) ->
    process(Obstacles, array:new(), 0, []).
 
process([], _Tails, _Len, AccRev) ->
    lists:reverse(AccRev);
process([X|Rest], Tails, Len, AccRev) ->
    Pos = find_pos(Tails, Len, X),
    NewTails = array:set(Pos, X, Tails),
    NewLen = case Pos of
                 Len + 1 -> Len + 1;
                 _       -> Len
             end,
    process(Rest, NewTails, NewLen, [Pos|AccRev]).
 
find_pos(Tails, Len, X) ->
    find_pos(1, Len + 1, Tails, Len, X).
 
find_pos(Low, High, _Tails, _Len, _X) when Low >= High ->
    Low;
find_pos(Low, High, Tails, Len, X) ->
    Mid = (Low + High) div 2,
    Val = if
              Mid > Len -> ?INF;
              true      -> array:get(Mid, Tails)
          end,
    if
        Val > X ->
            find_pos(Low, Mid, Tails, Len, X);
        true ->
            find_pos(Mid + 1, High, Tails, Len, X)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_obstacle_course_at_each_position(obstacles :: [integer]) :: [integer]
  def longest_obstacle_course_at_each_position(obstacles) do
    {rev_ans, _tails, _size} =
      Enum.reduce(obstacles, {[], :array.new(), 0}, fn x, {ans_acc, tails, sz} ->
        pos = upper_bound(tails, sz, x)
        new_ans = [pos + 1 | ans_acc]
        new_tails = :array.set(pos, x, tails)
        new_sz = if pos == sz, do: sz + 1, else: sz
        {new_ans, new_tails, new_sz}
      end)

    Enum.reverse(rev_ans)
  end

  defp upper_bound(tails, size, target) do
    ub_search(tails, target, 0, size)
  end

  defp ub_search(_tails, _target, lo, hi) when lo >= hi, do: lo

  defp ub_search(tails, target, lo, hi) do
    mid = div(lo + hi, 2)
    val = :array.get(mid, tails)

    if val > target do
      ub_search(tails, target, lo, mid)
    else
      ub_search(tails, target, mid + 1, hi)
    end
  end
end
```
