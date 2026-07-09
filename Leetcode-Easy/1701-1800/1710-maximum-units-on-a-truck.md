# 1710. Maximum Units on a Truck

## Cpp

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[1] > b[1];
             });
        long long total = 0;
        for (const auto& type : boxTypes) {
            if (truckSize == 0) break;
            int take = min(truckSize, type[0]);
            total += static_cast<long long>(take) * type[1];
            truckSize -= take;
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        java.util.Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
        int total = 0;
        for (int[] type : boxTypes) {
            if (truckSize == 0) break;
            int take = Math.min(truckSize, type[0]);
            total += take * type[1];
            truckSize -= take;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # Sort by units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0
        remaining = truckSize

        for count, units in boxTypes:
            if remaining == 0:
                break
            take = min(count, remaining)
            total_units += take * units
            remaining -= take

        return total_units
```

## Python3

```python
from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0
        for count, units in boxTypes:
            if truckSize == 0:
                break
            take = min(count, truckSize)
            total += take * units
            truckSize -= take
        return total
```

## C

```c
#include <stdlib.h>

static int compare(const void *a, const void *b) {
    const int *rowA = *(const int **)a;
    const int *rowB = *(const int **)b;
    return rowB[1] - rowA[1];  // descending by units per box
}

int maximumUnits(int** boxTypes, int boxTypesSize, int* boxTypesColSize, int truckSize) {
    (void)boxTypesColSize; // unused parameter

    qsort(boxTypes, boxTypesSize, sizeof(int *), compare);

    int total = 0;
    for (int i = 0; i < boxTypesSize && truckSize > 0; ++i) {
        int boxes = boxTypes[i][0];
        int units = boxTypes[i][1];
        int take = boxes < truckSize ? boxes : truckSize;
        total += take * units;
        truckSize -= take;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumUnits(int[][] boxTypes, int truckSize) {
        System.Array.Sort(boxTypes, (a, b) => b[1].CompareTo(a[1]));
        long total = 0;
        foreach (var type in boxTypes) {
            if (truckSize == 0) break;
            int take = type[0] < truckSize ? type[0] : truckSize;
            total += (long)take * type[1];
            truckSize -= take;
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
var maximumUnits = function(boxTypes, truckSize) {
    boxTypes.sort((a, b) => b[1] - a[1]);
    let total = 0;
    for (const [count, units] of boxTypes) {
        if (truckSize === 0) break;
        const take = Math.min(count, truckSize);
        total += take * units;
        truckSize -= take;
    }
    return total;
};
```

## Typescript

```typescript
function maximumUnits(boxTypes: number[][], truckSize: number): number {
    boxTypes.sort((a, b) => b[1] - a[1]);
    let total = 0;
    for (const [count, units] of boxTypes) {
        if (truckSize === 0) break;
        const take = Math.min(count, truckSize);
        total += take * units;
        truckSize -= take;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $boxTypes
     * @param Integer $truckSize
     * @return Integer
     */
    function maximumUnits($boxTypes, $truckSize) {
        usort($boxTypes, function($a, $b) {
            return $b[1] <=> $a[1];
        });

        $totalUnits = 0;
        foreach ($boxTypes as $type) {
            if ($truckSize == 0) break;
            $boxesToTake = min($type[0], $truckSize);
            $totalUnits += $boxesToTake * $type[1];
            $truckSize -= $boxesToTake;
        }
        return $totalUnits;
    }
}
```

## Swift

```swift
class Solution {
    func maximumUnits(_ boxTypes: [[Int]], _ truckSize: Int) -> Int {
        let sorted = boxTypes.sorted { $0[1] > $1[1] }
        var remaining = truckSize
        var total = 0
        for type in sorted {
            if remaining == 0 { break }
            let take = min(remaining, type[0])
            total += take * type[1]
            remaining -= take
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumUnits(boxTypes: Array<IntArray>, truckSize: Int): Int {
        val sorted = boxTypes.sortedByDescending { it[1] }
        var remaining = truckSize
        var total = 0L
        for (type in sorted) {
            if (remaining == 0) break
            val take = minOf(type[0], remaining)
            total += take.toLong() * type[1]
            remaining -= take
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maximumUnits(List<List<int>> boxTypes, int truckSize) {
    // Sort box types by units per box in descending order
    boxTypes.sort((a, b) => b[1] - a[1]);
    int totalUnits = 0;
    for (var type in boxTypes) {
      if (truckSize == 0) break;
      int boxesToTake = truckSize < type[0] ? truckSize : type[0];
      totalUnits += boxesToTake * type[1];
      truckSize -= boxesToTake;
    }
    return totalUnits;
  }
}
```

## Golang

```go
import "sort"

func maximumUnits(boxTypes [][]int, truckSize int) int {
	sort.Slice(boxTypes, func(i, j int) bool {
		return boxTypes[i][1] > boxTypes[j][1]
	})
	total := 0
	for _, bt := range boxTypes {
		if truckSize == 0 {
			break
		}
		cnt, units := bt[0], bt[1]
		if cnt > truckSize {
			cnt = truckSize
		}
		total += cnt * units
		truckSize -= cnt
	}
	return total
}
```

## Ruby

```ruby
def maximum_units(box_types, truck_size)
  # Sort box types by units per box in descending order
  sorted = box_types.sort_by { |type| -type[1] }
  total_units = 0
  remaining = truck_size

  sorted.each do |count, units|
    break if remaining == 0
    take = [count, remaining].min
    total_units += take * units
    remaining -= take
  end

  total_units
end
```

## Scala

```scala
object Solution {
    def maximumUnits(boxTypes: Array[Array[Int]], truckSize: Int): Int = {
        val sorted = boxTypes.sortWith((a, b) => a(1) > b(1))
        var remaining = truckSize
        var total = 0
        for (box <- sorted if remaining > 0) {
            val take = math.min(box(0), remaining)
            total += take * box(1)
            remaining -= take
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_units(mut box_types: Vec<Vec<i32>>, truck_size: i32) -> i32 {
        // Sort by units per box in descending order
        box_types.sort_by(|a, b| b[1].cmp(&a[1]));
        let mut remaining = truck_size;
        let mut total: i64 = 0;
        for bt in box_types.iter() {
            if remaining == 0 {
                break;
            }
            let take = std::cmp::min(remaining, bt[0]);
            total += (take as i64) * (bt[1] as i64);
            remaining -= take;
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-units boxTypes truckSize)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((sorted (sort boxTypes (lambda (a b) (> (second a) (second b)))))
         (result
          (let loop ((remaining truckSize) (lst sorted) (total 0))
            (if (or (= remaining 0) (null? lst))
                total
                (let* ((cnt   (first (car lst)))
                       (units (second (car lst)))
                       (take  (min cnt remaining)))
                  (loop (- remaining take)
                        (cdr lst)
                        (+ total (* take units))))))))
    result))
```

## Erlang

```erlang
-module(solution).
-export([maximum_units/2]).

-spec maximum_units(BoxTypes :: [[integer()]], TruckSize :: integer()) -> integer().
maximum_units(BoxTypes, TruckSize) ->
    Sorted = lists:sort(fun([_,U1],[_,U2]) -> U1 > U2 end, BoxTypes),
    go(Sorted, TruckSize, 0).

go(_, 0, Acc) -> Acc;
go([], _Remain, Acc) -> Acc;
go([[Cnt, Units]|Rest], Remain, Acc) ->
    Take = erlang:min(Cnt, Remain),
    go(Rest, Remain - Take, Acc + Take * Units).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_units(box_types :: [[integer]], truck_size :: integer) :: integer
  def maximum_units(box_types, truck_size) do
    sorted = Enum.sort_by(box_types, fn [_cnt, units] -> -units end)

    {total, _} =
      Enum.reduce(sorted, {0, truck_size}, fn [cnt, units], {acc, remaining} ->
        if remaining == 0 do
          {acc, 0}
        else
          take = min(cnt, remaining)
          {acc + take * units, remaining - take}
        end
      end)

    total
  end
end
```
