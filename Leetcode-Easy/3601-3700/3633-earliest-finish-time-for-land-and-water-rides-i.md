# 3633. Earliest Finish Time for Land and Water Rides I

## Cpp

```cpp
class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration,
                           vector<int>& waterStartTime, vector<int>& waterDuration) {
        int n = landStartTime.size();
        int m = waterStartTime.size();
        int best = INT_MAX;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                // Land then Water
                int endLand = landStartTime[i] + landDuration[i];
                int startWater = max(waterStartTime[j], endLand);
                int finishLW = startWater + waterDuration[j];
                best = min(best, finishLW);
                
                // Water then Land
                int endWater = waterStartTime[j] + waterDuration[j];
                int startLand = max(landStartTime[i], endWater);
                int finishWL = startLand + landDuration[i];
                best = min(best, finishWL);
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int n = landStartTime.length;
        int m = waterStartTime.length;
        int best = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int landFinish = landStartTime[i] + landDuration[i];
            for (int j = 0; j < m; j++) {
                // Land then Water
                int startWater = Math.max(waterStartTime[j], landFinish);
                int finish1 = startWater + waterDuration[j];
                // Water then Land
                int waterFinish = waterStartTime[j] + waterDuration[j];
                int startLand = Math.max(landStartTime[i], waterFinish);
                int finish2 = startLand + landDuration[i];
                best = Math.min(best, Math.min(finish1, finish2));
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        INF = 10**9
        ans = INF
        n = len(landStartTime)
        m = len(waterStartTime)
        for i in range(n):
            land_end = landStartTime[i] + landDuration[i]
            for j in range(m):
                # Land then water
                finish1 = max(waterStartTime[j], land_end) + waterDuration[j]
                # Water then land
                water_end = waterStartTime[j] + waterDuration[j]
                finish2 = max(landStartTime[i], water_end) + landDuration[i]
                if finish1 < ans:
                    ans = finish1
                if finish2 < ans:
                    ans = finish2
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        best = float('inf')
        for i in range(n):
            ls, ld = landStartTime[i], landDuration[i]
            finish_land = ls + ld
            for j in range(m):
                ws, wd = waterStartTime[j], waterDuration[j]
                # Land then Water
                start_water = max(ws, finish_land)
                finish1 = start_water + wd
                best = min(best, finish1)

                # Water then Land
                finish_water = ws + wd
                start_land = max(ls, finish_water)
                finish2 = start_land + ld
                best = min(best, finish2)
        return best
```

## C

```c
#include <limits.h>

int earliestFinishTime(int* landStartTime, int landStartTimeSize, int* landDuration, int landDurationSize,
                       int* waterStartTime, int waterStartTimeSize, int* waterDuration, int waterDurationSize) {
    int n = landStartTimeSize;
    int m = waterStartTimeSize;
    int best = INT_MAX;

    for (int i = 0; i < n; ++i) {
        int lStart = landStartTime[i];
        int lDur   = landDuration[i];
        int lFinish = lStart + lDur;

        for (int j = 0; j < m; ++j) {
            int wStart = waterStartTime[j];
            int wDur   = waterDuration[j];
            int wFinish = wStart + wDur;

            // Land first, then water
            int startWaterAfterLand = lFinish > wStart ? lFinish : wStart;
            int finishWaterAfterLand = startWaterAfterLand + wDur;
            if (finishWaterAfterLand < best) best = finishWaterAfterLand;

            // Water first, then land
            int startLandAfterWater = wFinish > lStart ? wFinish : lStart;
            int finishLandAfterWater = startLandAfterWater + lDur;
            if (finishLandAfterWater < best) best = finishLandAfterWater;
        }
    }

    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int EarliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int n = landStartTime.Length;
        int m = waterStartTime.Length;
        int best = int.MaxValue;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // Land then Water
                int finishLand = landStartTime[i] + landDuration[i];
                int startWater = Math.Max(waterStartTime[j], finishLand);
                int finishWater = startWater + waterDuration[j];
                if (finishWater < best) best = finishWater;
                
                // Water then Land
                int finishWaterFirst = waterStartTime[j] + waterDuration[j];
                int startLand = Math.Max(landStartTime[i], finishWaterFirst);
                int finishLandSecond = startLand + landDuration[i];
                if (finishLandSecond < best) best = finishLandSecond;
            }
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} landStartTime
 * @param {number[]} landDuration
 * @param {number[]} waterStartTime
 * @param {number[]} waterDuration
 * @return {number}
 */
var earliestFinishTime = function(landStartTime, landDuration, waterStartTime, waterDuration) {
    let n = landStartTime.length;
    let m = waterStartTime.length;
    let best = Infinity;
    for (let i = 0; i < n; ++i) {
        const landFinish = landStartTime[i] + landDuration[i];
        for (let j = 0; j < m; ++j) {
            // Land then Water
            const finish1 = Math.max(waterStartTime[j], landFinish) + waterDuration[j];
            // Water then Land
            const waterFinish = waterStartTime[j] + waterDuration[j];
            const finish2 = Math.max(landStartTime[i], waterFinish) + landDuration[i];
            if (finish1 < best) best = finish1;
            if (finish2 < best) best = finish2;
        }
    }
    return best;
};
```

## Typescript

```typescript
function earliestFinishTime(landStartTime: number[], landDuration: number[], waterStartTime: number[], waterDuration: number[]): number {
    let best = Infinity;
    const n = landStartTime.length;
    const m = waterStartTime.length;
    for (let i = 0; i < n; ++i) {
        const landFinish = landStartTime[i] + landDuration[i];
        for (let j = 0; j < m; ++j) {
            // Land then Water
            const finishLandThenWater = Math.max(waterStartTime[j], landFinish) + waterDuration[j];
            if (finishLandThenWater < best) best = finishLandThenWater;
            // Water then Land
            const waterFinish = waterStartTime[j] + waterDuration[j];
            const finishWaterThenLand = Math.max(landStartTime[i], waterFinish) + landDuration[i];
            if (finishWaterThenLand < best) best = finishWaterThenLand;
        }
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $landStartTime
     * @param Integer[] $landDuration
     * @param Integer[] $waterStartTime
     * @param Integer[] $waterDuration
     * @return Integer
     */
    function earliestFinishTime($landStartTime, $landDuration, $waterStartTime, $waterDuration) {
        $ans = PHP_INT_MAX;
        $n = count($landStartTime);
        $m = count($waterStartTime);
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $m; ++$j) {
                // Land then water
                $finishLand = $landStartTime[$i] + $landDuration[$i];
                $startWater = max($waterStartTime[$j], $finishLand);
                $finishWater = $startWater + $waterDuration[$j];
                if ($finishWater < $ans) {
                    $ans = $finishWater;
                }
                // Water then land
                $finishWater2 = $waterStartTime[$j] + $waterDuration[$j];
                $startLand = max($landStartTime[$i], $finishWater2);
                $finishLand2 = $startLand + $landDuration[$i];
                if ($finishLand2 < $ans) {
                    $ans = $finishLand2;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func earliestFinishTime(_ landStartTime: [Int], _ landDuration: [Int], _ waterStartTime: [Int], _ waterDuration: [Int]) -> Int {
        var best = Int.max
        for i in 0..<landStartTime.count {
            let landStart = landStartTime[i]
            let landEnd = landStart + landDuration[i]
            for j in 0..<waterStartTime.count {
                // Land then water
                let finishLandThenWater = max(landEnd, waterStartTime[j]) + waterDuration[j]
                best = min(best, finishLandThenWater)
                
                // Water then land
                let waterEnd = waterStartTime[j] + waterDuration[j]
                let finishWaterThenLand = max(waterEnd, landStart) + landDuration[i]
                best = min(best, finishWaterThenLand)
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun earliestFinishTime(
        landStartTime: IntArray,
        landDuration: IntArray,
        waterStartTime: IntArray,
        waterDuration: IntArray
    ): Int {
        var best = Int.MAX_VALUE
        for (i in landStartTime.indices) {
            val landEnd = landStartTime[i] + landDuration[i]
            for (j in waterStartTime.indices) {
                // Land first, then water
                val startWater = maxOf(landEnd, waterStartTime[j])
                val finishLandThenWater = startWater + waterDuration[j]
                best = minOf(best, finishLandThenWater)

                // Water first, then land
                val waterEnd = waterStartTime[j] + waterDuration[j]
                val startLand = maxOf(waterEnd, landStartTime[i])
                val finishWaterThenLand = startLand + landDuration[i]
                best = minOf(best, finishWaterThenLand)
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int earliestFinishTime(List<int> landStartTime, List<int> landDuration,
      List<int> waterStartTime, List<int> waterDuration) {
    int ans = 1 << 30;
    for (int i = 0; i < landStartTime.length; i++) {
      int finishLand = landStartTime[i] + landDuration[i];
      for (int j = 0; j < waterStartTime.length; j++) {
        // Land first, then water
        int finish1 = (finishLand > waterStartTime[j] ? finishLand : waterStartTime[j]) +
            waterDuration[j];
        if (finish1 < ans) ans = finish1;

        // Water first, then land
        int finishWater = waterStartTime[j] + waterDuration[j];
        int finish2 = (finishWater > landStartTime[i] ? finishWater : landStartTime[i]) +
            landDuration[i];
        if (finish2 < ans) ans = finish2;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	minFinish := int(^uint(0) >> 1) // MaxInt
	for i := 0; i < len(landStartTime); i++ {
		landEnd := landStartTime[i] + landDuration[i]
		for j := 0; j < len(waterStartTime); j++ {
			// Land then water
			startWater := waterStartTime[j]
			if landEnd > startWater {
				startWater = landEnd
			}
			finish1 := startWater + waterDuration[j]

			// Water then land
			waterEnd := waterStartTime[j] + waterDuration[j]
			startLand := landStartTime[i]
			if waterEnd > startLand {
				startLand = waterEnd
			}
			finish2 := startLand + landDuration[i]

			if finish1 < minFinish {
				minFinish = finish1
			}
			if finish2 < minFinish {
				minFinish = finish2
			}
		}
	}
	return minFinish
}
```

## Ruby

```ruby
def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration)
  ans = Float::INFINITY
  n = land_start_time.length
  m = water_start_time.length

  (0...n).each do |i|
    (0...m).each do |j|
      # Land first, then water
      finish_land = land_start_time[i] + land_duration[i]
      start_water = [water_start_time[j], finish_land].max
      finish = start_water + water_duration[j]
      ans = [ans, finish].min

      # Water first, then land
      finish_water = water_start_time[j] + water_duration[j]
      start_land = [land_start_time[i], finish_water].max
      finish2 = start_land + land_duration[i]
      ans = [ans, finish2].min
    end
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
    def earliestFinishTime(landStartTime: Array[Int], landDuration: Array[Int],
                           waterStartTime: Array[Int], waterDuration: Array[Int]): Int = {
        var best = Int.MaxValue
        for (i <- landStartTime.indices) {
            val landEnd = landStartTime(i) + landDuration(i)
            for (j <- waterStartTime.indices) {
                // Land first, then water
                val finishLandFirst = Math.max(waterStartTime(j), landEnd) + waterDuration(j)
                if (finishLandFirst < best) best = finishLandFirst

                // Water first, then land
                val waterEnd = waterStartTime(j) + waterDuration(j)
                val finishWaterFirst = Math.max(landStartTime(i), waterEnd) + landDuration(i)
                if (finishWaterFirst < best) best = finishWaterFirst
            }
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn earliest_finish_time(
        land_start_time: Vec<i32>,
        land_duration: Vec<i32>,
        water_start_time: Vec<i32>,
        water_duration: Vec<i32>,
    ) -> i32 {
        let mut best = i32::MAX;
        for (ls, ld) in land_start_time.iter().zip(land_duration.iter()) {
            for (ws, wd) in water_start_time.iter().zip(water_duration.iter()) {
                // Land then Water
                let finish_land = *ls + *ld;
                let finish_water = std::cmp::max(*ws, finish_land) + *wd;
                best = best.min(finish_water);
                // Water then Land
                let finish_water_first = *ws + *wd;
                let finish_land_second = std::cmp::max(*ls, finish_water_first) + *ld;
                best = best.min(finish_land_second);
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (earliest-finish-time landStartTime landDuration waterStartTime waterDuration)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((pairs
          (for*/list ([i (in-range (length landStartTime))]
                      [j (in-range (length waterStartTime))])
            (let* ((ls (list-ref landStartTime i))
                   (ld (list-ref landDuration i))
                   (ws (list-ref waterStartTime j))
                   (wd (list-ref waterDuration j))
                   
                   ;; land then water
                   (finish-land (+ ls ld))
                   (start-water (max ws finish-land))
                   (finish1 (+ start-water wd))
                   
                   ;; water then land
                   (finish-water (+ ws wd))
                   (start-land (max ls finish-water))
                   (finish2 (+ start-land ld)))
              (min finish1 finish2)))))
    (apply min pairs)))
```

## Erlang

```erlang
-spec earliest_finish_time([integer()], [integer()], [integer()], [integer()]) -> integer().
earliest_finish_time(LandStartTime, LandDuration, WaterStartTime, WaterDuration) ->
    LandPairs = lists:zip(LandStartTime, LandDuration),
    WaterPairs = lists:zip(WaterStartTime, WaterDuration),
    Inf = 1 bsl 30,
    find_min(LandPairs, WaterPairs, Inf).

find_min([], _, Min) -> Min;
find_min([Land|RestLand], WaterPairs, CurrentMin) ->
    NewMin = find_min_water(Land, WaterPairs, CurrentMin),
    find_min(RestLand, WaterPairs, NewMin).

find_min_water(_, [], Min) -> Min;
find_min_water({LStart, LDur}, [{WStart, WDur}|RestWater], Min) ->
    LandFinish = LStart + LDur,
    StartWater1 = erlang:max(LandFinish, WStart),
    Finish1 = StartWater1 + WDur,
    WaterFinish = WStart + WDur,
    StartLand2 = erlang:max(WaterFinish, LStart),
    Finish2 = StartLand2 + LDur,
    PairMin = erlang:min(Finish1, Finish2),
    NewMin = if PairMin < Min -> PairMin; true -> Min end,
    find_min_water({LStart, LDur}, RestWater, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec earliest_finish_time(land_start_time :: [integer], land_duration :: [integer], water_start_time :: [integer], water_duration :: [integer]) :: integer
  def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration) do
    land = Enum.zip(land_start_time, land_duration)
    water = Enum.zip(water_start_time, water_duration)

    finishes =
      for {ls, ld} <- land,
          {ws, wd} <- water do
        # Land first then water
        finish_land = ls + ld
        start_water = max(ws, finish_land)
        time1 = start_water + wd

        # Water first then land
        finish_water = ws + wd
        start_land = max(ls, finish_water)
        time2 = start_land + ld

        [time1, time2]
      end

    finishes
    |> List.flatten()
    |> Enum.min()
  end
end
```
