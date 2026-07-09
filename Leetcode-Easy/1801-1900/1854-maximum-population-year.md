# 1854. Maximum Population Year

## Cpp

```cpp
class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        const int MIN_YEAR = 1950;
        const int MAX_YEAR = 2050; // death can be up to 2050, we need index up to 2050 for diff
        vector<int> diff(MAX_YEAR + 2, 0);
        for (const auto& log : logs) {
            int birth = log[0];
            int death = log[1]; // exclusive
            diff[birth] += 1;
            diff[death] -= 1;
        }
        int bestYear = MIN_YEAR;
        int cur = 0, maxPop = 0;
        for (int year = MIN_YEAR; year <= MAX_YEAR; ++year) {
            cur += diff[year];
            if (cur > maxPop) {
                maxPop = cur;
                bestYear = year;
            }
        }
        return bestYear;
    }
};
```

## Java

```java
class Solution {
    public int maximumPopulation(int[][] logs) {
        // The years are in the range [1950, 2050]
        // Use a difference array to count births and deaths.
        int[] diff = new int[2052]; // extra space for death year index
        
        for (int[] log : logs) {
            int birth = log[0];
            int death = log[1];
            diff[birth]++;   // person becomes alive at birth year
            diff[death]--;   // person stops being counted at death year
        }
        
        int maxPopulation = 0;
        int yearWithMax = 1950;
        int current = 0;
        for (int year = 1950; year <= 2050; year++) {
            current += diff[year];
            if (current > maxPopulation) {
                maxPopulation = current;
                yearWithMax = year;
            }
        }
        return yearWithMax;
    }
}
```

## Python

```python
class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        OFFSET = 1950
        MAX_YEAR = 2050
        diff = [0] * (MAX_YEAR - OFFSET + 2)  # extra space for safety
        for b, d in logs:
            diff[b - OFFSET] += 1
            diff[d - OFFSET] -= 1

        cur = 0
        best = -1
        ans = OFFSET
        for i in range(0, MAX_YEAR - OFFSET):
            cur += diff[i]
            year = OFFSET + i
            if cur > best:
                best = cur
                ans = year
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # years are within [1950, 2050]
        OFFSET = 1950
        MAX_YEAR = 2051  # need up to death year for decrement
        diff = [0] * (MAX_YEAR + 1)  # index by actual year

        for birth, death in logs:
            diff[birth] += 1
            diff[death] -= 1

        cur = 0
        max_pop = -1
        answer = OFFSET
        for year in range(OFFSET, MAX_YEAR):
            cur += diff[year]
            if cur > max_pop:
                max_pop = cur
                answer = year
        return answer
```

## C

```c
int maximumPopulation(int** logs, int logsSize, int* logsColSize) {
    // Year range is from 1950 to 2050 inclusive.
    // Use a difference array to count births and deaths.
    int diff[2102] = {0};  // enough size for indices up to 2051
    for (int i = 0; i < logsSize; ++i) {
        int birth = logs[i][0];
        int death = logs[i][1];   // exclusive
        diff[birth] += 1;
        diff[death] -= 1;
    }
    
    int maxPop = -1;
    int answerYear = 1950;
    int cur = 0;
    for (int year = 1950; year <= 2050; ++year) {
        cur += diff[year];
        if (cur > maxPop) {
            maxPop = cur;
            answerYear = year;
        }
    }
    return answerYear;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumPopulation(int[][] logs) {
        const int startYear = 1950;
        const int endYear = 2050; // death can be up to 2050 (exclusive)
        int[] diff = new int[endYear + 2]; // extra space for safety
        
        foreach (var log in logs) {
            int birth = log[0];
            int death = log[1];
            diff[birth] += 1;
            diff[death] -= 1; // death year is exclusive
        }
        
        int maxPop = 0;
        int curPop = 0;
        int answerYear = startYear;
        for (int year = startYear; year <= endYear; year++) {
            curPop += diff[year];
            if (curPop > maxPop) {
                maxPop = curPop;
                answerYear = year;
            }
        }
        return answerYear;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} logs
 * @return {number}
 */
var maximumPopulation = function(logs) {
    const diff = new Array(2052).fill(0);
    for (const [birth, death] of logs) {
        diff[birth] += 1;
        diff[death] -= 1;
    }
    let maxPop = 0, cur = 0, answer = 1950;
    for (let year = 1950; year <= 2050; ++year) {
        cur += diff[year];
        if (cur > maxPop) {
            maxPop = cur;
            answer = year;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function maximumPopulation(logs: number[][]): number {
    const OFFSET = 1950;
    const MAX_YEAR = 2050;
    const size = MAX_YEAR - OFFSET + 2; // extra slot for death decrement
    const diff = new Array(size).fill(0);
    
    for (const [birth, death] of logs) {
        diff[birth - OFFSET] += 1;
        diff[death - OFFSET] -= 1; // death year is exclusive
    }
    
    let cur = 0;
    let maxPop = 0;
    let answerYear = OFFSET;
    
    for (let i = 0; i < size - 1; i++) { // last slot only holds trailing decrement
        cur += diff[i];
        const year = OFFSET + i;
        if (cur > maxPop) {
            maxPop = cur;
            answerYear = year;
        }
    }
    
    return answerYear;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $logs
     * @return Integer
     */
    function maximumPopulation($logs) {
        // Difference array for years 0..2051 (enough for given constraints)
        $diff = array_fill(0, 2052, 0);
        foreach ($logs as $log) {
            $birth = $log[0];
            $death = $log[1];
            $diff[$birth] += 1;
            $diff[$death] -= 1; // death year not counted
        }

        $maxPop = 0;
        $yearWithMax = 1950;
        $curr = 0;

        for ($y = 1950; $y <= 2050; $y++) {
            $curr += $diff[$y];
            if ($curr > $maxPop) {
                $maxPop = $curr;
                $yearWithMax = $y;
            }
        }

        return $yearWithMax;
    }
}
```

## Swift

```swift
class Solution {
    func maximumPopulation(_ logs: [[Int]]) -> Int {
        var diff = [Int](repeating: 0, count: 2052)
        for log in logs {
            let birth = log[0]
            let death = log[1]
            diff[birth] += 1
            diff[death] -= 1
        }
        var maxPop = 0
        var cur = 0
        var answer = 1950
        for year in 1950...2050 {
            cur += diff[year]
            if cur > maxPop {
                maxPop = cur
                answer = year
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumPopulation(logs: Array<IntArray>): Int {
        val diff = IntArray(2052)
        for (log in logs) {
            diff[log[0]] += 1
            diff[log[1]] -= 1
        }
        var maxPop = 0
        var ansYear = 1950
        var cur = 0
        for (year in 1950..2050) {
            cur += diff[year]
            if (cur > maxPop) {
                maxPop = cur
                ansYear = year
            }
        }
        return ansYear
    }
}
```

## Dart

```dart
class Solution {
  int maximumPopulation(List<List<int>> logs) {
    const int MIN_YEAR = 1950;
    const int MAX_YEAR = 2050;
    List<int> diff = List.filled(MAX_YEAR + 2, 0);
    for (var log in logs) {
      int birth = log[0];
      int death = log[1];
      diff[birth] += 1;
      diff[death] -= 1;
    }
    int current = 0;
    int maxPop = 0;
    int bestYear = MIN_YEAR;
    for (int year = MIN_YEAR; year <= MAX_YEAR; ++year) {
      current += diff[year];
      if (current > maxPop) {
        maxPop = current;
        bestYear = year;
      }
    }
    return bestYear;
  }
}
```

## Golang

```go
func maximumPopulation(logs [][]int) int {
	const start = 1950
	const end = 2050
	// extra slot to handle death at year 2050
	diff := make([]int, end-start+2)

	for _, log := range logs {
		birth, death := log[0], log[1]
		diff[birth-start]++
		diff[death-start]--
	}

	maxPop, curPop, ansYear := 0, 0, start
	for i := 0; i <= end-start; i++ {
		curPop += diff[i]
		if curPop > maxPop {
			maxPop = curPop
			ansYear = start + i
		}
	}
	return ansYear
}
```

## Ruby

```ruby
def maximum_population(logs)
  diff = Array.new(2052, 0)
  logs.each do |b, d|
    diff[b] += 1
    diff[d] -= 1
  end

  max_pop = 0
  year = 0
  cur = 0
  (1950..2050).each do |y|
    cur += diff[y]
    if cur > max_pop
      max_pop = cur
      year = y
    end
  end
  year
end
```

## Scala

```scala
object Solution {
    def maximumPopulation(logs: Array[Array[Int]]): Int = {
        val diff = new Array[Int](2052)
        for (log <- logs) {
            val b = log(0)
            val d = log(1)
            diff(b) += 1
            diff(d) -= 1
        }
        var maxPop = 0
        var year = 1950
        var cur = 0
        for (y <- 1950 until 2051) {
            cur += diff(y)
            if (cur > maxPop) {
                maxPop = cur
                year = y
            }
        }
        year
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        const START_YEAR: usize = 1950;
        const END_YEAR: usize = 2050;
        let mut diff = vec![0i32; END_YEAR + 2]; // extra slot for safety

        for log in logs.iter() {
            let b = log[0] as usize;
            let d = log[1] as usize;
            diff[b] += 1;
            diff[d] -= 1;
        }

        let mut max_pop = 0i32;
        let mut best_year = START_YEAR as i32;
        let mut cur = 0i32;

        for year in START_YEAR..=END_YEAR {
            cur += diff[year];
            if cur > max_pop {
                max_pop = cur;
                best_year = year as i32;
            }
        }

        best_year
    }
}
```

## Racket

```racket
(define/contract (maximum-population logs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((births (map first logs))
         (deaths (map second logs))
         (min-year (apply min births))
         (max-year (apply max deaths))
         (size (+ (- max-year min-year) 2))
         (diff (make-vector size 0)))
    (for ([log logs])
      (define b (first log))
      (define d (second log))
      (vector-set! diff (- b min-year)
                   (+ (vector-ref diff (- b min-year)) 1))
      (vector-set! diff (- d min-year)
                   (+ (vector-ref diff (- d min-year)) -1)))
    (let* ((range (- max-year min-year))) ; years to evaluate
      (let loop ((i 0) (cur 0) (best -1) (ans min-year))
        (if (= i range)
            ans
            (let* ((new-cur (+ cur (vector-ref diff i)))
                   (year (+ i min-year)))
              (if (> new-cur best)
                  (loop (+ i 1) new-cur new-cur year)
                  (loop (+ i 1) new-cur best ans))))))))
```

## Erlang

```erlang
-spec maximum_population(Logs :: [[integer()]]) -> integer().
maximum_population(Logs) ->
    Changes = lists:foldl(
        fun([B, D], Acc) ->
            Acc1 = maps:update_with(B, fun(V) -> V + 1 end, 1, Acc),
            maps:update_with(D, fun(V) -> V - 1 end, -1, Acc1)
        end,
        #{},
        Logs
    ),
    Years = lists:seq(1950, 2050),
    {_, _, Answer} = lists:foldl(
        fun(Y, {Curr, MaxPop, Ans}) ->
            Delta = maps:get(Y, Changes, 0),
            NewCurr = Curr + Delta,
            if
                NewCurr > MaxPop -> {NewCurr, NewCurr, Y};
                true -> {NewCurr, MaxPop, Ans}
            end
        end,
        {0, -1, 1950},
        Years
    ),
    Answer.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_population(logs :: [[integer]]) :: integer
  def maximum_population(logs) do
    diffs =
      Enum.reduce(logs, %{}, fn [b, d], acc ->
        acc
        |> Map.update(b, 1, &(&1 + 1))
        |> Map.update(d, -1, &(&1 - 1))
      end)

    {_, _, answer} =
      diffs
      |> Map.keys()
      |> Enum.sort()
      |> Enum.reduce({0, -1, nil}, fn year, {cur_pop, max_pop, ans_year} ->
        cur_pop = cur_pop + Map.get(diffs, year)

        if cur_pop > max_pop do
          {cur_pop, cur_pop, year}
        else
          {cur_pop, max_pop, ans_year}
        end
      end)

    answer
  end
end
```
