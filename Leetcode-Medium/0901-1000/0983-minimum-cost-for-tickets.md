# 0983. Minimum Cost For Tickets

## Cpp

```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int lastDay = days.back();
        vector<bool> need(lastDay + 1, false);
        for (int d : days) need[d] = true;
        vector<int> dp(lastDay + 1, 0);
        for (int i = 1; i <= lastDay; ++i) {
            if (!need[i]) {
                dp[i] = dp[i - 1];
            } else {
                int cost1 = dp[i - 1] + costs[0];
                int cost7 = dp[max(0, i - 7)] + costs[1];
                int cost30 = dp[max(0, i - 30)] + costs[2];
                dp[i] = min({cost1, cost7, cost30});
            }
        }
        return dp[lastDay];
    }
};
```

## Java

```java
class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        boolean[] travel = new boolean[366];
        for (int d : days) {
            travel[d] = true;
        }
        int lastDay = days[days.length - 1];
        int[] dp = new int[lastDay + 1];
        for (int day = 1; day <= lastDay; ++day) {
            if (!travel[day]) {
                dp[day] = dp[day - 1];
            } else {
                int cost1 = dp[day - 1] + costs[0];
                int cost7 = dp[Math.max(0, day - 7)] + costs[1];
                int cost30 = dp[Math.max(0, day - 30)] + costs[2];
                dp[day] = Math.min(cost1, Math.min(cost7, cost30));
            }
        }
        return dp[lastDay];
    }
}
```

## Python

```python
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        travel = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        for d in range(1, last_day + 1):
            if d not in travel:
                dp[d] = dp[d - 1]
            else:
                cost1 = dp[d - 1] + costs[0]
                cost7 = dp[max(0, d - 7)] + costs[1]
                cost30 = dp[max(0, d - 30)] + costs[2]
                dp[d] = min(cost1, cost7, cost30)
        return dp[last_day]
```

## Python3

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        for d in range(1, last_day + 1):
            if d not in travel:
                dp[d] = dp[d - 1]
            else:
                cost1 = dp[d - 1] + costs[0]
                cost7 = dp[max(0, d - 7)] + costs[1]
                cost30 = dp[max(0, d - 30)] + costs[2]
                dp[d] = min(cost1, cost7, cost30)
        return dp[last_day]
```

## C

```c
#include <stdbool.h>

int mincostTickets(int* days, int daysSize, int* costs, int costsSize) {
    int lastDay = days[daysSize - 1];
    bool travel[366] = { false };
    for (int i = 0; i < daysSize; ++i) {
        travel[days[i]] = true;
    }

    int dp[366] = { 0 };
    for (int d = 1; d <= lastDay; ++d) {
        if (!travel[d]) {
            dp[d] = dp[d - 1];
        } else {
            int cost1 = dp[d - 1] + costs[0];
            int cost7 = dp[(d >= 7) ? d - 7 : 0] + costs[1];
            int cost30 = dp[(d >= 30) ? d - 30 : 0] + costs[2];
            int minc = cost1;
            if (cost7 < minc) minc = cost7;
            if (cost30 < minc) minc = cost30;
            dp[d] = minc;
        }
    }
    return dp[lastDay];
}
```

## Csharp

```csharp
public class Solution
{
    public int MincostTickets(int[] days, int[] costs)
    {
        int lastDay = days[days.Length - 1];
        bool[] needTravel = new bool[lastDay + 1];
        foreach (int d in days) needTravel[d] = true;

        int[] dp = new int[lastDay + 1];
        for (int i = 1; i <= lastDay; i++)
        {
            if (!needTravel[i])
            {
                dp[i] = dp[i - 1];
            }
            else
            {
                int cost1 = dp[i - 1] + costs[0];
                int cost7 = dp[Math.Max(0, i - 7)] + costs[1];
                int cost30 = dp[Math.Max(0, i - 30)] + costs[2];
                dp[i] = Math.Min(cost1, Math.Min(cost7, cost30));
            }
        }
        return dp[lastDay];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    const n = days.length;
    const lastDay = days[n - 1];
    const dp = new Array(lastDay + 1).fill(0);
    let i = 0; // index in days array

    for (let d = 1; d <= lastDay; d++) {
        if (d < days[i]) {
            dp[d] = dp[d - 1];
        } else {
            const cost1 = dp[d - 1] + costs[0];
            const cost7 = dp[Math.max(0, d - 7)] + costs[1];
            const cost30 = dp[Math.max(0, d - 30)] + costs[2];
            dp[d] = Math.min(cost1, cost7, cost30);
            i++;
        }
    }

    return dp[lastDay];
};
```

## Typescript

```typescript
function mincostTickets(days: number[], costs: number[]): number {
    const lastDay = days[days.length - 1];
    const daySet = new Set<number>(days);
    const dp: number[] = new Array(lastDay + 1).fill(0);

    for (let d = 1; d <= lastDay; d++) {
        if (!daySet.has(d)) {
            dp[d] = dp[d - 1];
        } else {
            const cost1 = dp[d - 1] + costs[0];
            const cost7 = dp[Math.max(0, d - 7)] + costs[1];
            const cost30 = dp[Math.max(0, d - 30)] + costs[2];
            dp[d] = Math.min(cost1, cost7, cost30);
        }
    }

    return dp[lastDay];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $days
     * @param Integer[] $costs
     * @return Integer
     */
    function mincostTickets($days, $costs) {
        $lastDay = $days[count($days) - 1];
        $dp = array_fill(0, $lastDay + 1, 0);
        $daySet = array_flip($days);

        for ($i = 1; $i <= $lastDay; $i++) {
            if (!isset($daySet[$i])) {
                $dp[$i] = $dp[$i - 1];
            } else {
                $cost1 = $dp[$i - 1] + $costs[0];
                $cost7 = $dp[max(0, $i - 7)] + $costs[1];
                $cost30 = $dp[max(0, $i - 30)] + $costs[2];
                $dp[$i] = min($cost1, $cost7, $cost30);
            }
        }

        return $dp[$lastDay];
    }
}
```

## Swift

```swift
class Solution {
    func mincostTickets(_ days: [Int], _ costs: [Int]) -> Int {
        guard let lastDay = days.last else { return 0 }
        let travelDays = Set(days)
        var dp = Array(repeating: 0, count: lastDay + 1)
        
        for day in 1...lastDay {
            if !travelDays.contains(day) {
                dp[day] = dp[day - 1]
            } else {
                let cost1 = dp[day - 1] + costs[0]
                let cost7 = dp[max(0, day - 7)] + costs[1]
                let cost30 = dp[max(0, day - 30)] + costs[2]
                dp[day] = min(cost1, min(cost7, cost30))
            }
        }
        
        return dp[lastDay]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mincostTickets(days: IntArray, costs: IntArray): Int {
        val lastDay = days.last()
        val travel = BooleanArray(lastDay + 1)
        for (d in days) travel[d] = true
        val dp = IntArray(lastDay + 1)
        for (day in 1..lastDay) {
            if (!travel[day]) {
                dp[day] = dp[day - 1]
            } else {
                val cost1 = dp[day - 1] + costs[0]
                val cost7 = dp[maxOf(0, day - 7)] + costs[1]
                val cost30 = dp[maxOf(0, day - 30)] + costs[2]
                dp[day] = minOf(cost1, cost7, cost30)
            }
        }
        return dp[lastDay]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int mincostTickets(List<int> days, List<int> costs) {
    if (days.isEmpty) return 0;
    int lastDay = days.last;
    Set<int> travelDays = days.toSet();
    List<int> dp = List.filled(lastDay + 1, 0);
    for (int d = 1; d <= lastDay; d++) {
      if (!travelDays.contains(d)) {
        dp[d] = dp[d - 1];
      } else {
        int cost1 = dp[d - 1] + costs[0];
        int cost7 = dp[max(0, d - 7)] + costs[1];
        int cost30 = dp[max(0, d - 30)] + costs[2];
        dp[d] = min(cost1, min(cost7, cost30));
      }
    }
    return dp[lastDay];
  }
}
```

## Golang

```go
func mincostTickets(days []int, costs []int) int {
    last := days[len(days)-1]
    travel := make([]bool, last+1)
    for _, d := range days {
        travel[d] = true
    }
    dp := make([]int, last+1)
    for i := 1; i <= last; i++ {
        if !travel[i] {
            dp[i] = dp[i-1]
            continue
        }
        cost1 := dp[i-1] + costs[0]

        idx7 := i - 7
        if idx7 < 0 {
            idx7 = 0
        }
        cost7 := dp[idx7] + costs[1]

        idx30 := i - 30
        if idx30 < 0 {
            idx30 = 0
        }
        cost30 := dp[idx30] + costs[2]

        minCost := cost1
        if cost7 < minCost {
            minCost = cost7
        }
        if cost30 < minCost {
            minCost = cost30
        }
        dp[i] = minCost
    }
    return dp[last]
}
```

## Ruby

```ruby
def mincost_tickets(days, costs)
  last_day = days[-1]
  need_travel = Array.new(last_day + 1, false)
  days.each { |d| need_travel[d] = true }

  dp = Array.new(last_day + 1, 0)

  (1..last_day).each do |day|
    if !need_travel[day]
      dp[day] = dp[day - 1]
    else
      cost_one   = dp[day - 1] + costs[0]
      cost_seven = dp[[day - 7, 0].max] + costs[1]
      cost_thirty= dp[[day - 30, 0].max] + costs[2]
      dp[day] = [cost_one, cost_seven, cost_thirty].min
    end
  end

  dp[last_day]
end
```

## Scala

```scala
object Solution {
    def mincostTickets(days: Array[Int], costs: Array[Int]): Int = {
        val lastDay = days.last
        val travelDays = days.toSet
        val dp = new Array[Int](lastDay + 1)
        for (day <- 1 to lastDay) {
            if (!travelDays.contains(day)) {
                dp(day) = dp(day - 1)
            } else {
                val cost1 = dp(day - 1) + costs(0)
                val cost7 = dp(Math.max(0, day - 7)) + costs(1)
                val cost30 = dp(Math.max(0, day - 30)) + costs(2)
                dp(day) = Math.min(cost1, Math.min(cost7, cost30))
            }
        }
        dp(lastDay)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {
        let last_day = *days.last().unwrap() as usize;
        let mut travel = vec![false; last_day + 1];
        for &d in &days {
            travel[d as usize] = true;
        }
        let mut dp = vec![0i32; last_day + 1];
        for d in 1..=last_day {
            if !travel[d] {
                dp[d] = dp[d - 1];
            } else {
                let cost1 = dp[d - 1] + costs[0];
                let cost7 = dp[if d >= 7 { d - 7 } else { 0 }] + costs[1];
                let cost30 = dp[if d >= 30 { d - 30 } else { 0 }] + costs[2];
                dp[d] = *[cost1, cost7, cost30].iter().min().unwrap();
            }
        }
        dp[last_day]
    }
}
```

## Racket

```racket
(define/contract (mincost-tickets days costs)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((last-day (if (null? days) 0 (car (reverse days))))
         (need (make-vector (+ last-day 1) #f)))
    (for-each (lambda (d) (vector-set! need d #t)) days)
    (define dp (make-vector (+ last-day 1) 0))
    (let loop ((day 1))
      (when (<= day last-day)
        (if (vector-ref need day)
            (let* ((c1 (+ (vector-ref dp (- day 1)) (list-ref costs 0)))
                   (c2 (+ (vector-ref dp (max (- day 7) 0)) (list-ref costs 1)))
                   (c3 (+ (vector-ref dp (max (- day 30) 0)) (list-ref costs 2))))
              (vector-set! dp day (min c1 (min c2 c3))))
            (vector-set! dp day (vector-ref dp (- day 1))))
        (loop (+ day 1))))
    (vector-ref dp last-day)))
```

## Erlang

```erlang
-spec mincost_tickets([integer()], [integer()]) -> integer().
mincost_tickets(Days, Costs) ->
    TravelSet = maps:from_list([{D, true} || D <- Days]),
    Cost1 = lists:nth(1, Costs),
    Cost7 = lists:nth(2, Costs),
    Cost30 = lists:nth(3, Costs),
    LastDay = lists:last(Days),
    DP0 = #{0 => 0},
    DPFinal = loop(1, LastDay, TravelSet, Cost1, Cost7, Cost30, DP0),
    maps:get(LastDay, DPFinal).

loop(Day, LastDay, _TravelSet, _C1, _C7, _C30, DP) when Day > LastDay ->
    DP;
loop(Day, LastDay, TravelSet, C1, C7, C30, DP) ->
    Prev = maps:get(Day - 1, DP),
    NewCost =
        case maps:is_key(Day, TravelSet) of
            true ->
                Cost1 = Prev + C1,
                Cost7 = maps:get(erlang:max(Day - 7, 0), DP) + C7,
                Cost30 = maps:get(erlang:max(Day - 30, 0), DP) + C30,
                erlang:min(Cost1, erlang:min(Cost7, Cost30));
            false ->
                Prev
        end,
    DP2 = maps:put(Day, NewCost, DP),
    loop(Day + 1, LastDay, TravelSet, C1, C7, C30, DP2).
```

## Elixir

```elixir
defmodule Solution do
  @spec mincost_tickets(days :: [integer], costs :: [integer]) :: integer
  def mincost_tickets(days, costs) do
    last_day = List.last(days)
    travel_set = MapSet.new(days)

    c1 = Enum.at(costs, 0)
    c7 = Enum.at(costs, 1)
    c30 = Enum.at(costs, 2)

    dp =
      Enum.reduce((last_day)..1, %{}, fn day, acc ->
        if not MapSet.member?(travel_set, day) do
          Map.put(acc, day, Map.get(acc, day + 1, 0))
        else
          cost_one = c1 + Map.get(acc, day + 1, 0)
          cost_seven = c7 + Map.get(acc, day + 7, 0)
          cost_thirty = c30 + Map.get(acc, day + 30, 0)

          min_cost = Enum.min([cost_one, cost_seven, cost_thirty])
          Map.put(acc, day, min_cost)
        end
      end)

    Map.get(dp, 1, 0)
  end
end
```
