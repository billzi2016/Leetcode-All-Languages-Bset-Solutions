# 0624. Maximum Distance in Arrays

## Cpp

```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int m = arrays.size();
        int ans = 0;
        int minSoFar = arrays[0][0];
        int maxSoFar = arrays[0].back();
        for (int i = 1; i < m; ++i) {
            int curMin = arrays[i][0];
            int curMax = arrays[i].back();
            ans = max(ans, abs(curMax - minSoFar));
            ans = max(ans, abs(maxSoFar - curMin));
            minSoFar = min(minSoFar, curMin);
            maxSoFar = max(maxSoFar, curMax);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        if (arrays == null || arrays.size() < 2) return 0;
        int globalMin = arrays.get(0).get(0);
        int globalMax = arrays.get(0).get(arrays.get(0).size() - 1);
        int maxDist = 0;
        for (int i = 1; i < arrays.size(); i++) {
            List<Integer> arr = arrays.get(i);
            int curMin = arr.get(0);
            int curMax = arr.get(arr.size() - 1);
            // distance between current max and previous global min
            maxDist = Math.max(maxDist, Math.abs(curMax - globalMin));
            // distance between current min and previous global max
            maxDist = Math.max(maxDist, Math.abs(globalMax - curMin));
            // update globals
            globalMin = Math.min(globalMin, curMin);
            globalMax = Math.max(globalMax, curMax);
        }
        return maxDist;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize with the first array's extremes
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):
            cur_min = arrays[i][0]
            cur_max = arrays[i][-1]

            # Distance using current max with previous global min
            ans = max(ans, abs(cur_max - global_min))
            # Distance using current min with previous global max
            ans = max(ans, abs(global_max - cur_min))

            # Update the global extremes for future comparisons
            global_min = min(global_min, cur_min)
            global_max = max(global_max, cur_max)

        return ans
```

## Python3

```python
class Solution:
    def maxDistance(self, arrays):
        ans = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for i in range(1, len(arrays)):
            cur_min = arrays[i][0]
            cur_max = arrays[i][-1]
            # distance between current min and previous global max
            ans = max(ans, abs(cur_min - max_val))
            # distance between current max and previous global min
            ans = max(ans, abs(cur_max - min_val))
            # update global extremes
            if cur_min < min_val:
                min_val = cur_min
            if cur_max > max_val:
                max_val = cur_max
        return ans
```

## C

```c
#include <stdlib.h>

int maxDistance(int** arrays, int arraysSize, int* arraysColSize) {
    int ans = 0;
    int global_min = arrays[0][0];
    int global_max = arrays[0][arraysColSize[0] - 1];

    for (int i = 1; i < arraysSize; ++i) {
        int cur_min = arrays[i][0];
        int cur_max = arrays[i][arraysColSize[i] - 1];

        int d1 = abs(cur_max - global_min);
        if (d1 > ans) ans = d1;

        int d2 = abs(global_max - cur_min);
        if (d2 > ans) ans = d2;

        if (cur_min < global_min) global_min = cur_min;
        if (cur_max > global_max) global_max = cur_max;
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDistance(IList<IList<int>> arrays) {
        if (arrays == null || arrays.Count < 2) return 0;
        int globalMin = arrays[0][0];
        int globalMax = arrays[0][arrays[0].Count - 1];
        int maxDist = 0;

        for (int i = 1; i < arrays.Count; i++) {
            var cur = arrays[i];
            int curMin = cur[0];
            int curMax = cur[cur.Count - 1];

            // distance using current max with previous global min
            maxDist = Math.Max(maxDist, Math.Abs(curMax - globalMin));
            // distance using current min with previous global max
            maxDist = Math.Max(maxDist, Math.Abs(globalMax - curMin));

            // update globals for next iterations
            if (curMin < globalMin) globalMin = curMin;
            if (curMax > globalMax) globalMax = curMax;
        }

        return maxDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} arrays
 * @return {number}
 */
var maxDistance = function(arrays) {
    let ans = 0;
    // Initialize global min and max with the first array's extremes
    let globalMin = arrays[0][0];
    let globalMax = arrays[0][arrays[0].length - 1];
    
    for (let i = 1; i < arrays.length; i++) {
        const curArr = arrays[i];
        const curMin = curArr[0];
        const curMax = curArr[curArr.length - 1];
        
        // Possible distances using current array with previous global extremes
        ans = Math.max(
            ans,
            Math.abs(curMax - globalMin),
            Math.abs(globalMax - curMin)
        );
        
        // Update global extremes for next iterations
        if (curMin < globalMin) globalMin = curMin;
        if (curMax > globalMax) globalMax = curMax;
    }
    
    return ans;
};
```

## Typescript

```typescript
function maxDistance(arrays: number[][]): number {
    let minSoFar = arrays[0][0];
    let maxSoFar = arrays[0][arrays[0].length - 1];
    let ans = 0;
    for (let i = 1; i < arrays.length; ++i) {
        const curMin = arrays[i][0];
        const curMax = arrays[i][arrays[i].length - 1];
        ans = Math.max(ans, Math.abs(curMax - minSoFar));
        ans = Math.max(ans, Math.abs(curMin - maxSoFar));
        if (curMin < minSoFar) minSoFar = curMin;
        if (curMax > maxSoFar) maxSoFar = curMax;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $arrays
     * @return Integer
     */
    function maxDistance($arrays) {
        $m = count($arrays);
        if ($m < 2) return 0;

        $globalMin = $arrays[0][0];
        $firstLen = count($arrays[0]);
        $globalMax = $arrays[0][$firstLen - 1];

        $ans = 0;
        for ($i = 1; $i < $m; $i++) {
            $cur = $arrays[$i];
            $curMin = $cur[0];
            $curLen = count($cur);
            $curMax = $cur[$curLen - 1];

            // distance using current max and previous global min
            $ans = max($ans, $curMax - $globalMin);
            // distance using current min and previous global max
            $ans = max($ans, $globalMax - $curMin);

            if ($curMin < $globalMin) {
                $globalMin = $curMin;
            }
            if ($curMax > $globalMax) {
                $globalMax = $curMax;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistance(_ arrays: [[Int]]) -> Int {
        guard !arrays.isEmpty else { return 0 }
        var answer = 0
        var globalMin = arrays[0][0]
        var globalMax = arrays[0].last!
        for i in 1..<arrays.count {
            let curMin = arrays[i][0]
            let curMax = arrays[i].last!
            answer = max(answer, abs(curMin - globalMax))
            answer = max(answer, abs(curMax - globalMin))
            if curMin < globalMin { globalMin = curMin }
            if curMax > globalMax { globalMax = curMax }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistance(arrays: List<List<Int>>): Int {
        var minVal = arrays[0][0]
        var maxVal = arrays[0][arrays[0].size - 1]
        var ans = 0
        for (i in 1 until arrays.size) {
            val arr = arrays[i]
            val curMin = arr[0]
            val curMax = arr[arr.size - 1]
            ans = kotlin.math.max(ans, kotlin.math.abs(curMax - minVal))
            ans = kotlin.math.max(ans, kotlin.math.abs(maxVal - curMin))
            if (curMin < minVal) minVal = curMin
            if (curMax > maxVal) maxVal = curMax
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxDistance(List<List<int>> arrays) {
    int globalMin = arrays[0][0];
    int globalMax = arrays[0].last;
    int ans = 0;

    for (int i = 1; i < arrays.length; ++i) {
      List<int> arr = arrays[i];
      int curMin = arr[0];
      int curMax = arr.last;

      ans = _max(ans, (curMax - globalMin).abs());
      ans = _max(ans, (globalMax - curMin).abs());

      if (curMin < globalMin) globalMin = curMin;
      if (curMax > globalMax) globalMax = curMax;
    }

    return ans;
  }

  int _max(int a, int b) => a > b ? a : b;
}
```

## Golang

```go
func maxDistance(arrays [][]int) int {
    if len(arrays) == 0 {
        return 0
    }
    globalMin := arrays[0][0]
    globalMax := arrays[0][len(arrays[0])-1]
    ans := 0
    for i := 1; i < len(arrays); i++ {
        curMin := arrays[i][0]
        curMax := arrays[i][len(arrays[i])-1]

        if d := curMax - globalMin; d > ans {
            ans = d
        }
        if d := globalMax - curMin; d > ans {
            ans = d
        }

        if curMin < globalMin {
            globalMin = curMin
        }
        if curMax > globalMax {
            globalMax = curMax
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_distance(arrays)
  ans = 0
  global_min = arrays[0][0]
  global_max = arrays[0][-1]

  (1...arrays.length).each do |i|
    cur = arrays[i]
    cur_min = cur[0]
    cur_max = cur[-1]

    ans = [ans, cur_max - global_min].max
    ans = [ans, global_max - cur_min].max

    global_min = [global_min, cur_min].min
    global_max = [global_max, cur_max].max
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxDistance(arrays: List[List[Int]]): Int = {
        if (arrays.isEmpty) return 0
        var ans = 0
        var minSoFar = arrays.head.head
        var maxSoFar = arrays.head.last

        for (i <- 1 until arrays.length) {
            val cur = arrays(i)
            val curMin = cur.head
            val curMax = cur.last

            ans = math.max(ans, math.abs(curMax - minSoFar))
            ans = math.max(ans, math.abs(maxSoFar - curMin))

            if (curMin < minSoFar) minSoFar = curMin
            if (curMax > maxSoFar) maxSoFar = curMax
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_distance(arrays: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        // Initialize global min and max with the first array's extremes
        let mut global_min = arrays[0][0];
        let mut global_max = *arrays[0].last().unwrap();

        for (idx, arr) in arrays.iter().enumerate() {
            if idx == 0 { continue; }
            let cur_min = arr[0];
            let cur_max = *arr.last().unwrap();

            // Compare current max with previous global min
            ans = ans.max(cur_max - global_min);
            // Compare current min with previous global max
            ans = ans.max(global_max - cur_min);

            if cur_min < global_min {
                global_min = cur_min;
            }
            if cur_max > global_max {
                global_max = cur_max;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-distance arrays)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ((INF 1000000000))
    (let loop ((lst arrays) (idx 0)
               (min1 INF) (min1-idx -1) (min2 INF) (min2-idx -1)
               (max1 (- INF)) (max1-idx -1) (max2 (- INF)) (max2-idx -1))
      (if (null? lst)
          (let* ((candidate1 (if (= max1-idx min2-idx) (- INF) (- max1 min2)))
                 (candidate2 (if (= max2-idx min1-idx) (- INF) (- max2 min1))))
            (max candidate1 candidate2))
          (let* ((arr (car lst))
                 (lo (first arr))
                 (hi (list-ref arr (- (length arr) 1)))
                 (new-mins
                  (if (< lo min1)
                      (values lo idx min1 min1-idx)
                      (if (< lo min2)
                          (values min1 min1-idx lo idx)
                          (values min1 min1-idx min2 min2-idx))))
                 (new-maxs
                  (if (> hi max1)
                      (values hi idx max1 max1-idx)
                      (if (> hi max2)
                          (values max1 max1-idx hi idx)
                          (values max1 max1-idx max2 max2-idx)))))
            (let-values ([(new-min1 new-min1-idx new-min2 new-min2-idx) new-mins]
                         [(new-max1 new-max1-idx new-max2 new-max2-idx) new-maxs])
              (loop (cdr lst) (+ idx 1)
                    new-min1 new-min1-idx new-min2 new-min2-idx
                    new-max1 new-max1-idx new-max2 new-max2-idx)))))))
```

## Erlang

```erlang
-export([max_distance/1]).

-spec max_distance(Arrays :: [[integer()]]) -> integer().
max_distance([]) ->
    0;
max_distance([First|Rest]) ->
    Min0 = hd(First),
    Max0 = lists:last(First),

    % Fold over the remaining arrays while tracking global min/max and per-array mins/maxs
    {GlobalMin, GlobalMinIdx, GlobalMax, GlobalMaxIdx, MinsAcc, MaxsAcc} =
        lists:foldl(
            fun({Arr, Idx},
                {CurMin, CurMinIdx, CurMax, CurMaxIdx, MinList, MaxList}) ->
                    Min = hd(Arr),
                    Max = lists:last(Arr),

                    NewCurMin = if Min < CurMin -> Min; true -> CurMin end,
                    NewCurMinIdx = if Min < CurMin -> Idx; true -> CurMinIdx end,

                    NewCurMax = if Max > CurMax -> Max; true -> CurMax end,
                    NewCurMaxIdx = if Max > CurMax -> Idx; true -> CurMaxIdx end,

                    {NewCurMin, NewCurMinIdx, NewCurMax, NewCurMaxIdx,
                     [Min | MinList], [Max | MaxList]}
                end,
            {Min0, 0, Max0, 0, [], []},
            lists:zip(Rest, lists:seq(1, length(Rest)))),

    % Complete per-array min/max lists (include the first array)
    AllMins = [Min0 | lists:reverse(MinsAcc)],
    AllMaxs = [Max0 | lists:reverse(MaxsAcc)],

    case GlobalMinIdx =/= GlobalMaxIdx of
        true ->
            GlobalMax - GlobalMin;
        false ->
            % Need to pair the global max with a min from another array,
            % and the global min with a max from another array.
            Ans1 = max_diff_global_max(GlobalMax, AllMins, GlobalMaxIdx),
            Ans2 = max_diff_global_min(GlobalMin, AllMaxs, GlobalMinIdx),
            max(Ans1, Ans2)
    end.

% Compute max(GlobalMax - Min_i) for all i != ExcludeIdx
max_diff_global_max(_GlobalMax, [], _ExcludeIdx, Acc) ->
    Acc;
max_diff_global_max(GlobalMax, [Min | Rest], ExcludeIdx, Acc) when is_integer(ExcludeIdx) ->
    NewAcc = case ExcludeIdx of
                 0 -> max(Acc, GlobalMax - Min);
                 _ -> max(Acc, GlobalMax - Min)
             end,
    max_diff_global_max(GlobalMax, Rest, ExcludeIdx - 1, NewAcc).

% Wrapper that starts with index 0
max_diff_global_max(GlobalMax, Mins, ExcludeIdx) ->
    max_diff_global_max(GlobalMax, Mins, ExcludeIdx, 0).

% Compute max(Max_i - GlobalMin) for all i != ExcludeIdx
max_diff_global_min(_GlobalMin, [], _ExcludeIdx, Acc) ->
    Acc;
max_diff_global_min(GlobalMin, [Max | Rest], ExcludeIdx, Acc) when is_integer(ExcludeIdx) ->
    NewAcc = case ExcludeIdx of
                 0 -> max(Acc, Max - GlobalMin);
                 _ -> max(Acc, Max - GlobalMin)
             end,
    max_diff_global_min(GlobalMin, Rest, ExcludeIdx - 1, NewAcc).

% Wrapper that starts with index 0
max_diff_global_min(GlobalMin, Maxs, ExcludeIdx) ->
    max_diff_global_min(GlobalMin, Maxs, ExcludeIdx, 0).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distance(arrays :: [[integer]]) :: integer
  def max_distance([first | rest]) do
    global_min = List.first(first)
    global_max = List.last(first)

    {ans, _gmin, _gmax} =
      Enum.reduce(rest, {0, global_min, global_max}, fn arr, {cur_ans, cur_gmin, cur_gmax} ->
        cur_min = List.first(arr)
        cur_max = List.last(arr)

        d1 = abs(cur_min - cur_gmax)
        d2 = abs(cur_max - cur_gmin)
        new_ans = max(cur_ans, max(d1, d2))

        new_gmin = if cur_min < cur_gmin, do: cur_min, else: cur_gmin
        new_gmax = if cur_max > cur_gmax, do: cur_max, else: cur_gmax

        {new_ans, new_gmin, new_gmax}
      end)

    ans
  end
end
```
