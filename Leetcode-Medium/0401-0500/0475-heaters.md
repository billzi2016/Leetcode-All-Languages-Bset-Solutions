# 0475. Heaters

## Cpp

```cpp
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int result = 0;
        for (int house : houses) {
            auto it = lower_bound(heaters.begin(), heaters.end(), house);
            int curDist = INT_MAX;
            if (it != heaters.end()) curDist = min(curDist, abs(*it - house));
            if (it != heaters.begin()) {
                --it;
                curDist = min(curDist, abs(*it - house));
            }
            result = max(result, curDist);
        }
        return result;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(heaters);
        int radius = 0;
        for (int house : houses) {
            int idx = Arrays.binarySearch(heaters, house);
            if (idx < 0) {
                idx = -idx - 1; // insertion point
            }
            int dist = Integer.MAX_VALUE;
            if (idx < heaters.length) {
                dist = Math.min(dist, Math.abs(heaters[idx] - house));
            }
            if (idx > 0) {
                dist = Math.min(dist, Math.abs(house - heaters[idx - 1]));
            }
            radius = Math.max(radius, dist);
        }
        return radius;
    }
}
```

## Python

```python
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        import bisect
        radius = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            left = float('inf')
            right = float('inf')
            if idx < len(heaters):
                right = heaters[idx] - house
            if idx > 0:
                left = house - heaters[idx - 1]
            radius = max(radius, min(left, right))
        return radius
```

## Python3

```python
from bisect import bisect_left
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        for house in houses:
            idx = bisect_left(heaters, house)
            left = float('inf')
            right = float('inf')
            if idx < len(heaters):
                right = heaters[idx] - house
            if idx > 0:
                left = house - heaters[idx - 1]
            radius = max(radius, min(left, right))
        return radius
```

## C

```c
#include <stdlib.h>

static int cmpInt(const void *a, const void *b) {
    long x = *(const int *)a;
    long y = *(const int *)b;
    return (x > y) - (x < y);
}

int findRadius(int* houses, int housesSize, int* heaters, int heatersSize) {
    qsort(houses, housesSize, sizeof(int), cmpInt);
    qsort(heaters, heatersSize, sizeof(int), cmpInt);

    int answer = 0;
    for (int i = 0; i < housesSize; ++i) {
        int house = houses[i];
        int left = 0, right = heatersSize;
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (heaters[mid] < house)
                left = mid + 1;
            else
                right = mid;
        }

        int curDist = 2147483647; // INT_MAX
        if (left < heatersSize) {
            int d = heaters[left] - house;
            if (d < 0) d = -d;
            curDist = d;
        }
        if (left > 0) {
            int d = heaters[left - 1] - house;
            if (d < 0) d = -d;
            if (d < curDist) curDist = d;
        }

        if (curDist > answer) answer = curDist;
    }
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int FindRadius(int[] houses, int[] heaters) {
        Array.Sort(houses);
        Array.Sort(heaters);
        int result = 0;
        foreach (int house in houses) {
            int idx = Array.BinarySearch(heaters, house);
            if (idx < 0) idx = ~idx; // insertion point
            int minDist = int.MaxValue;
            if (idx < heaters.Length)
                minDist = Math.Min(minDist, Math.Abs(heaters[idx] - house));
            if (idx > 0)
                minDist = Math.Min(minDist, Math.Abs(house - heaters[idx - 1]));
            result = Math.Max(result, minDist);
        }
        return result;
    }
}
```

## Javascript

```javascript
var findRadius = function(houses, heaters) {
    houses.sort((a, b) => a - b);
    heaters.sort((a, b) => a - b);
    
    const lowerBound = (arr, target) => {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (arr[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    };
    
    let result = 0;
    for (const house of houses) {
        const idx = lowerBound(heaters, house);
        let dist = Infinity;
        if (idx < heaters.length) dist = Math.min(dist, Math.abs(heaters[idx] - house));
        if (idx > 0) dist = Math.min(dist, Math.abs(heaters[idx - 1] - house));
        result = Math.max(result, dist);
    }
    
    return result;
};
```

## Typescript

```typescript
function findRadius(houses: number[], heaters: number[]): number {
    houses.sort((a, b) => a - b);
    heaters.sort((a, b) => a - b);
    let result = 0;
    for (const house of houses) {
        let left = 0, right = heaters.length - 1;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (heaters[mid] < house) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        let dist = Math.abs(heaters[left] - house);
        if (left > 0) {
            dist = Math.min(dist, Math.abs(heaters[left - 1] - house));
        }
        result = Math.max(result, dist);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $houses
     * @param Integer[] $heaters
     * @return Integer
     */
    function findRadius($houses, $heaters) {
        sort($houses);
        sort($heaters);
        $ans = 0;
        $m = count($heaters);
        foreach ($houses as $house) {
            $left = 0;
            $right = $m - 1;
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($heaters[$mid] < $house) {
                    $left = $mid + 1;
                } else {
                    $right = $mid;
                }
            }
            $dist = abs($heaters[$left] - $house);
            if ($left > 0) {
                $dist = min($dist, abs($heaters[$left - 1] - $house));
            }
            $ans = max($ans, $dist);
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findRadius(_ houses: [Int], _ heaters: [Int]) -> Int {
        let sortedHouses = houses.sorted()
        let sortedHeaters = heaters.sorted()
        var result = 0
        
        for house in sortedHouses {
            var left = 0
            var right = sortedHeaters.count - 1
            
            while left <= right {
                let mid = (left + right) / 2
                if sortedHeaters[mid] < house {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
            
            var minDist = Int.max
            if left < sortedHeaters.count {
                minDist = min(minDist, abs(sortedHeaters[left] - house))
            }
            if right >= 0 {
                minDist = min(minDist, abs(sortedHeaters[right] - house))
            }
            
            result = max(result, minDist)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRadius(houses: IntArray, heaters: IntArray): Int {
        houses.sort()
        heaters.sort()
        var answer = 0
        for (house in houses) {
            var left = 0
            var right = heaters.size - 1
            while (left <= right) {
                val mid = left + (right - left) / 2
                if (heaters[mid] < house) {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
            var minDist = Int.MAX_VALUE
            if (left < heaters.size) {
                minDist = kotlin.math.abs(heaters[left] - house)
            }
            if (right >= 0) {
                minDist = kotlin.math.min(minDist, kotlin.math.abs(house - heaters[right]))
            }
            answer = kotlin.math.max(answer, minDist)
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int findRadius(List<int> houses, List<int> heaters) {
    houses.sort();
    heaters.sort();
    const int INF = 1 << 60;
    int result = 0;

    for (int house in houses) {
      int left = 0;
      int right = heaters.length - 1;
      while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (heaters[mid] < house) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }

      int dist = INF;
      if (left < heaters.length) {
        dist = heaters[left] - house;
      }
      if (right >= 0) {
        dist = min(dist, house - heaters[right]);
      }

      result = max(result, dist);
    }

    return result;
  }
}
```

## Golang

```go
import "sort"

func findRadius(houses []int, heaters []int) int {
	sort.Ints(houses)
	sort.Ints(heaters)

	maxDist := 0
	for _, house := range houses {
		idx := sort.Search(len(heaters), func(i int) bool { return heaters[i] >= house })
		var dist int
		if idx == 0 {
			dist = heaters[0] - house
		} else if idx == len(heaters) {
			dist = house - heaters[len(heaters)-1]
		} else {
			left := heaters[idx-1]
			right := heaters[idx]
			dLeft := house - left
			dRight := right - house
			if dLeft < dRight {
				dist = dLeft
			} else {
				dist = dRight
			}
		}
		if dist > maxDist {
			maxDist = dist
		}
	}
	return maxDist
}
```

## Ruby

```ruby
def find_radius(houses, heaters)
  houses.sort!
  heaters.sort!
  max_dist = 0
  h_len = heaters.length

  houses.each do |house|
    # binary search for first heater >= house
    left = 0
    right = h_len - 1
    while left <= right
      mid = (left + right) / 2
      if heaters[mid] < house
        left = mid + 1
      else
        right = mid - 1
      end
    end

    dist = Float::INFINITY
    if left < h_len
      dist = [dist, (heaters[left] - house).abs].min
    end
    if left > 0
      dist = [dist, (house - heaters[left - 1]).abs].min
    end

    max_dist = [max_dist, dist].max
  end

  max_dist
end
```

## Scala

```scala
object Solution {
    def findRadius(houses: Array[Int], heaters: Array[Int]): Int = {
        val hs = houses.sorted
        val he = heaters.sorted
        var result = 0

        for (h <- hs) {
            var left = 0
            var right = he.length - 1
            while (left <= right) {
                val mid = left + (right - left) / 2
                if (he(mid) < h) left = mid + 1
                else right = mid - 1
            }

            var minDist = Int.MaxValue
            if (left < he.length) minDist = math.min(minDist, math.abs(he(left) - h))
            if (right >= 0)      minDist = math.min(minDist, math.abs(h - he(right)))

            result = math.max(result, minDist)
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_radius(houses: Vec<i32>, heaters: Vec<i32>) -> i32 {
        let mut houses = houses;
        let mut heaters = heaters;
        houses.sort_unstable();
        heaters.sort_unstable();

        let mut ans = 0i32;

        for &h in houses.iter() {
            match heaters.binary_search(&h) {
                Ok(_) => continue,
                Err(idx) => {
                    let mut dist = i32::MAX;
                    if idx < heaters.len() {
                        dist = (heaters[idx] - h).abs();
                    }
                    if idx > 0 {
                        let d = (h - heaters[idx - 1]).abs();
                        if d < dist {
                            dist = d;
                        }
                    }
                    if dist > ans {
                        ans = dist;
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (find-radius houses heaters)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([sorted-houses (sort houses <)]
         [sorted-heaters (sort heaters <)]
         [hvec (list->vector sorted-houses)]
         [heaters-vec (list->vector sorted-heaters)])
    (define (closest-distance hv target)
      (let loop ([lo 0] [hi (- (vector-length hv) 1)])
        (if (> lo hi)
            (cond [(= lo 0)
                   (abs (- target (vector-ref hv 0)))]
                  [(= lo (vector-length hv))
                   (abs (- target (vector-ref hv (- lo 1))))]
                  [else
                   (let* ([left (vector-ref hv (- lo 1))]
                          [right (vector-ref hv lo)])
                     (min (abs (- target left))
                          (abs (- target right))))])
            (let* ([mid (quotient (+ lo hi) 2)]
                   [mid-val (vector-ref hv mid)])
              (cond [(= mid-val target) 0]
                    [(< mid-val target) (loop (+ mid 1) hi)]
                    [else (loop lo (- mid 1))])))))
    (let loop ([i 0] [max-dist 0])
      (if (= i (vector-length hvec))
          max-dist
          (let* ([house (vector-ref hvec i)]
                 [dist (closest-distance heaters-vec house)]
                 [new-max (if (> dist max-dist) dist max-dist)])
            (loop (+ i 1) new-max))))))
```

## Erlang

```erlang
-module(solution).
-export([find_radius/2]).

-spec find_radius(Houses :: [integer()], Heaters :: [integer()]) -> integer().
find_radius(Houses, Heaters) ->
    SortedH = lists:sort(Houses),
    SortedHe = lists:sort(Heaters),
    process(SortedH, SortedHe, undefined, 0).

process([], _Heaters, _Prev, Max) ->
    Max;
process([House|Rest], Heaters, Prev, Max) ->
    {NewHeaters, NewPrev} = advance_heaters(House, Heaters, Prev),
    DistRight = case NewHeaters of
        [] -> 1 bsl 60;
        [R|_] -> erlang:abs(R - House)
    end,
    DistLeft = case NewPrev of
        undefined -> 1 bsl 60;
        L -> erlang:abs(L - House)
    end,
    HouseDist = erlang:min(DistLeft, DistRight),
    NewMax = erlang:max(Max, HouseDist),
    process(Rest, NewHeaters, NewPrev, NewMax).

advance_heaters(_House, [], Prev) ->
    {[], Prev};
advance_heaters(House, [H|T], _Prev) when H < House ->
    advance_heaters(House, T, H);
advance_heaters(_House, Heaters, Prev) ->
    {Heaters, Prev}.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_radius(houses :: [integer], heaters :: [integer]) :: integer
  def find_radius(houses, heaters) do
    houses = Enum.sort(houses)
    heaters_sorted = Enum.sort(heaters)
    heaters_tuple = List.to_tuple(heaters_sorted)
    len = tuple_size(heaters_tuple)

    {_, answer} =
      Enum.reduce(houses, {0, 0}, fn house, {idx, cur_max} ->
        idx = move_pointer(heaters_tuple, len, idx, house)
        dist = abs(elem(heaters_tuple, idx) - house)
        {idx, max(cur_max, dist)}
      end)

    answer
  end

  defp move_pointer(heaters, len, i, house) do
    if i + 1 < len and
         abs(elem(heaters, i + 1) - house) <= abs(elem(heaters, i) - house) do
      move_pointer(heaters, len, i + 1, house)
    else
      i
    end
  end
end
```
