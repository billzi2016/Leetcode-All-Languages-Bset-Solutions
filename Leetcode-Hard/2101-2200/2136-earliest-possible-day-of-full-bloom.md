# 2136. Earliest Possible Day of Full Bloom

## Cpp

```cpp
class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        int n = plantTime.size();
        vector<pair<int,int>> seeds;
        seeds.reserve(n);
        for (int i = 0; i < n; ++i) {
            seeds.emplace_back(growTime[i], plantTime[i]);
        }
        sort(seeds.begin(), seeds.end(),
             [](const pair<int,int>& a, const pair<int,int>& b){
                 return a.first > b.first; // descending growTime
             });
        long long curPlant = 0;
        long long answer = 0;
        for (auto& p : seeds) {
            int g = p.first;
            int pt = p.second;
            curPlant += pt;
            answer = max(answer, curPlant + (long long)g);
        }
        return (int)answer;
    }
};
```

## Java

```java
class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        java.util.Arrays.sort(idx, (a, b) -> Integer.compare(growTime[b], growTime[a]));
        long currentPlant = 0;
        long answer = 0;
        for (int i : idx) {
            currentPlant += plantTime[i];
            answer = Math.max(answer, currentPlant + growTime[i]);
        }
        return (int)answer;
    }
}
```

## Python

```python
class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        # Pair each seed's grow time with its planting time and sort by decreasing grow time
        seeds = sorted(zip(growTime, plantTime), key=lambda x: -x[0])
        current_day = 0
        answer = 0
        for g, p in seeds:
            current_day += p          # finish planting this seed
            answer = max(answer, current_day + g)  # day when this seed blooms
        return answer
```

## Python3

```python
from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Sort seeds by decreasing grow time
        seeds = sorted(zip(growTime, plantTime), key=lambda x: -x[0])
        current_day = 0
        result = 0
        for g, p in seeds:
            current_day += p          # days spent planting up to this seed
            result = max(result, current_day + g)  # bloom day of this seed
        return result
```

## C

```c
#include <stdlib.h>

typedef struct {
    int plant;
    int grow;
} Seed;

static int compareSeeds(const void *a, const void *b) {
    const Seed *sa = (const Seed *)a;
    const Seed *sb = (const Seed *)b;
    return sb->grow - sa->grow; // descending by grow time
}

int earliestFullBloom(int* plantTime, int plantTimeSize, int* growTime, int growTimeSize) {
    int n = plantTimeSize;
    Seed *seeds = (Seed *)malloc(n * sizeof(Seed));
    for (int i = 0; i < n; ++i) {
        seeds[i].plant = plantTime[i];
        seeds[i].grow = growTime[i];
    }

    qsort(seeds, n, sizeof(Seed), compareSeeds);

    long long currentPlant = 0;
    long long result = 0;
    for (int i = 0; i < n; ++i) {
        currentPlant += seeds[i].plant;
        long long bloomDay = currentPlant + seeds[i].grow;
        if (bloomDay > result) result = bloomDay;
    }

    free(seeds);
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int EarliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.Length;
        var seeds = new (int plant, int grow)[n];
        for (int i = 0; i < n; i++) {
            seeds[i] = (plantTime[i], growTime[i]);
        }
        Array.Sort(seeds, (a, b) => b.grow.CompareTo(a.grow));
        long currentPlant = 0;
        long result = 0;
        foreach (var s in seeds) {
            currentPlant += s.plant;
            long bloomDay = currentPlant + s.grow;
            if (bloomDay > result) result = bloomDay;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} plantTime
 * @param {number[]} growTime
 * @return {number}
 */
var earliestFullBloom = function(plantTime, growTime) {
    const n = plantTime.length;
    const seeds = new Array(n);
    for (let i = 0; i < n; ++i) {
        seeds[i] = [growTime[i], plantTime[i]];
    }
    // Sort by decreasing grow time
    seeds.sort((a, b) => b[0] - a[0]);
    
    let currentDay = 0;
    let answer = 0;
    for (let i = 0; i < n; ++i) {
        const [g, p] = seeds[i];
        currentDay += p;
        answer = Math.max(answer, currentDay + g);
    }
    return answer;
};
```

## Typescript

```typescript
function earliestFullBloom(plantTime: number[], growTime: number[]): number {
    const n = plantTime.length;
    const order = Array.from({ length: n }, (_, i) => i);
    order.sort((a, b) => growTime[b] - growTime[a]); // descending by growTime

    let currentDay = 0;
    let result = 0;

    for (const idx of order) {
        currentDay += plantTime[idx];
        result = Math.max(result, currentDay + growTime[idx]);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $plantTime
     * @param Integer[] $growTime
     * @return Integer
     */
    function earliestFullBloom($plantTime, $growTime) {
        $n = count($plantTime);
        $seeds = [];
        for ($i = 0; $i < $n; $i++) {
            // store as [growTime, plantTime] for easier sorting
            $seeds[] = [$growTime[$i], $plantTime[$i]];
        }
        usort($seeds, function($a, $b) {
            // descending by growTime
            return $b[0] <=> $a[0];
        });

        $currentDay = 0;
        $fullBloomDay = 0;
        foreach ($seeds as $seed) {
            $grow = $seed[0];
            $plant = $seed[1];
            $currentDay += $plant;               // days spent planting up to this seed
            $fullBloomDay = max($fullBloomDay, $currentDay + $grow);
        }

        return $fullBloomDay;
    }
}
```

## Swift

```swift
class Solution {
    func earliestFullBloom(_ plantTime: [Int], _ growTime: [Int]) -> Int {
        let n = plantTime.count
        var indices = Array(0..<n)
        indices.sort { growTime[$0] > growTime[$1] }
        
        var currentDay = 0
        var result = 0
        for i in indices {
            currentDay += plantTime[i]
            result = max(result, currentDay + growTime[i])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun earliestFullBloom(plantTime: IntArray, growTime: IntArray): Int {
        val n = plantTime.size
        val order = (0 until n).sortedWith(compareByDescending<Int> { growTime[it] })
        var currentPlant = 0L
        var result = 0L
        for (i in order) {
            currentPlant += plantTime[i]
            val bloomDay = currentPlant + growTime[i]
            if (bloomDay > result) result = bloomDay
        }
        return result.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int earliestFullBloom(List<int> plantTime, List<int> growTime) {
    int n = plantTime.length;
    List<int> indices = List.generate(n, (i) => i);
    indices.sort((a, b) => growTime[b].compareTo(growTime[a])); // descending by growTime

    int currentPlant = 0;
    int answer = 0;

    for (int idx in indices) {
      currentPlant += plantTime[idx];
      answer = max(answer, currentPlant + growTime[idx]);
    }

    return answer;
  }
}
```

## Golang

```go
import "sort"

func earliestFullBloom(plantTime []int, growTime []int) int {
	n := len(plantTime)
	type seed struct{ plant, grow int }
	seeds := make([]seed, n)
	for i := 0; i < n; i++ {
		seeds[i] = seed{plantTime[i], growTime[i]}
	}
	sort.Slice(seeds, func(i, j int) bool {
		return seeds[i].grow > seeds[j].grow
	})
	cur, ans := 0, 0
	for _, s := range seeds {
		cur += s.plant
		if cur+s.grow > ans {
			ans = cur + s.grow
		}
	}
	return ans
}
```

## Ruby

```ruby
def earliest_full_bloom(plant_time, grow_time)
  seeds = plant_time.zip(grow_time)
  seeds.sort_by! { |_, g| -g }
  current_day = 0
  result = 0
  seeds.each do |p, g|
    current_day += p
    result = [result, current_day + g].max
  end
  result
end
```

## Scala

```scala
object Solution {
  def earliestFullBloom(plantTime: Array[Int], growTime: Array[Int]): Int = {
    val n = plantTime.length
    val order = (0 until n).toArray.sortWith { (i, j) =>
      growTime(i) > growTime(j)
    }
    var currentPlant = 0L
    var result = 0L
    for (idx <- order) {
      currentPlant += plantTime(idx)
      val bloomDay = currentPlant + growTime(idx)
      if (bloomDay > result) result = bloomDay
    }
    result.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn earliest_full_bloom(plant_time: Vec<i32>, grow_time: Vec<i32>) -> i32 {
        let mut seeds: Vec<(i32, i32)> = plant_time
            .into_iter()
            .zip(grow_time.into_iter())
            .map(|(p, g)| (g, p))
            .collect();
        // Sort by decreasing grow time
        seeds.sort_by(|a, b| b.0.cmp(&a.0));
        let mut current_day = 0;
        let mut answer = 0;
        for (grow, plant) in seeds {
            current_day += plant;
            answer = answer.max(current_day + grow);
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (earliest-full-bloom plantTime growTime)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((pairs (map cons plantTime growTime))
         (sorted (sort pairs (lambda (a b) (> (cdr a) (cdr b))))))
    (let loop ((lst sorted) (current 0) (ans 0))
      (if (null? lst)
          ans
          (let* ((p (car lst))
                 (new-current (+ current (car p)))
                 (candidate (+ new-current (cdr p)))
                 (new-ans (max ans candidate)))
            (loop (cdr lst) new-current new-ans))))))
```

## Erlang

```erlang
-module(solution).
-export([earliest_full_bloom/2]).

-spec earliest_full_bloom(PlantTime :: [integer()], GrowTime :: [integer()]) -> integer().
earliest_full_bloom(PlantTime, GrowTime) ->
    Seeds = lists:zip(GrowTime, PlantTime),
    Sorted = lists:sort(fun({G1,_}, {G2,_}) -> G1 > G2 end, Seeds),
    {_, Result} = lists:foldl(
        fun({Grow, Plant}, {AccPlant, MaxDay}) ->
            NewAcc = AccPlant + Plant,
            BloomDay = NewAcc + Grow,
            NewMax = if BloomDay > MaxDay -> BloomDay; true -> MaxDay end,
            {NewAcc, NewMax}
        end,
        {0, 0},
        Sorted),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @spec earliest_full_bloom(plant_time :: [integer], grow_time :: [integer]) :: integer
  def earliest_full_bloom(plant_time, grow_time) do
    seeds = Enum.zip(plant_time, grow_time)

    sorted =
      Enum.sort_by(seeds, fn {_p, g} -> -g end)

    {result, _} =
      Enum.reduce(sorted, {0, 0}, fn {p, g}, {max_day, cur_plant} ->
        new_cur = cur_plant + p
        new_max = max(max_day, new_cur + g)
        {new_max, new_cur}
      end)

    result
  end
end
```
