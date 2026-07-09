# 2279. Maximum Bags With Full Capacity of Rocks

## Cpp

```cpp
class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        int n = capacity.size();
        vector<int> need(n);
        for (int i = 0; i < n; ++i) {
            need[i] = capacity[i] - rocks[i];
        }
        sort(need.begin(), need.end());
        long long extra = additionalRocks;
        int full = 0;
        for (int x : need) {
            if (x <= extra) {
                extra -= x;
                ++full;
            } else {
                break;
            }
        }
        return full;
    }
};
```

## Java

```java
class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = capacity.length;
        int[] need = new int[n];
        for (int i = 0; i < n; i++) {
            need[i] = capacity[i] - rocks[i];
        }
        java.util.Arrays.sort(need);
        long remaining = additionalRocks;
        int fullBags = 0;
        for (int req : need) {
            if (remaining >= req) {
                remaining -= req;
                fullBags++;
            } else {
                break;
            }
        }
        return fullBags;
    }
}
```

## Python

```python
class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        needed = [c - r for c, r in zip(capacity, rocks)]
        needed.sort()
        full = 0
        for req in needed:
            if req <= additionalRocks:
                additionalRocks -= req
                full += 1
            else:
                break
        return full
```

## Python3

```python
from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need = [c - r for c, r in zip(capacity, rocks)]
        need.sort()
        count = 0
        for x in need:
            if additionalRocks >= x:
                additionalRocks -= x
                count += 1
            else:
                break
        return count
```

## C

```c
#include <stdlib.h>

static int compare_ints(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    if (ai < bi) return -1;
    if (ai > bi) return 1;
    return 0;
}

int maximumBags(int* capacity, int capacitySize, int* rocks, int rocksSize, int additionalRocks) {
    int n = capacitySize; // same as rocksSize
    int *need = (int *)malloc(n * sizeof(int));
    if (!need) return 0;

    for (int i = 0; i < n; ++i) {
        need[i] = capacity[i] - rocks[i];
    }

    qsort(need, n, sizeof(int), compare_ints);

    long long remaining = additionalRocks;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        if (remaining >= need[i]) {
            remaining -= need[i];
            ++count;
        } else {
            break;
        }
    }

    free(need);
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = capacity.Length;
        int[] need = new int[n];
        for (int i = 0; i < n; i++) {
            need[i] = capacity[i] - rocks[i];
        }
        Array.Sort(need);
        long remaining = additionalRocks;
        int fullBags = 0;
        foreach (int req in need) {
            if (remaining >= req) {
                remaining -= req;
                fullBags++;
            } else {
                break;
            }
        }
        return fullBags;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} capacity
 * @param {number[]} rocks
 * @param {number} additionalRocks
 * @return {number}
 */
var maximumBags = function(capacity, rocks, additionalRocks) {
    const n = capacity.length;
    const need = new Array(n);
    for (let i = 0; i < n; ++i) {
        need[i] = capacity[i] - rocks[i];
    }
    need.sort((a, b) => a - b);
    let full = 0;
    for (let i = 0; i < n; ++i) {
        if (need[i] === 0) {
            full++;
        } else if (additionalRocks >= need[i]) {
            additionalRocks -= need[i];
            full++;
        } else {
            break;
        }
    }
    return full;
};
```

## Typescript

```typescript
function maximumBags(capacity: number[], rocks: number[], additionalRocks: number): number {
    const needed: number[] = [];
    for (let i = 0; i < capacity.length; i++) {
        needed.push(capacity[i] - rocks[i]);
    }
    needed.sort((a, b) => a - b);
    let fullBags = 0;
    for (const req of needed) {
        if (additionalRocks >= req) {
            additionalRocks -= req;
            fullBags++;
        } else {
            break;
        }
    }
    return fullBags;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $capacity
     * @param Integer[] $rocks
     * @param Integer $additionalRocks
     * @return Integer
     */
    function maximumBags($capacity, $rocks, $additionalRocks) {
        $needs = [];
        $n = count($capacity);
        for ($i = 0; $i < $n; $i++) {
            $needs[] = $capacity[$i] - $rocks[$i];
        }
        sort($needs, SORT_NUMERIC);
        $full = 0;
        foreach ($needs as $need) {
            if ($additionalRocks >= $need) {
                $additionalRocks -= $need;
                $full++;
            } else {
                break;
            }
        }
        return $full;
    }
}
```

## Swift

```swift
class Solution {
    func maximumBags(_ capacity: [Int], _ rocks: [Int], _ additionalRocks: Int) -> Int {
        var needs = [Int]()
        for i in 0..<capacity.count {
            needs.append(capacity[i] - rocks[i])
        }
        needs.sort()
        var remaining = additionalRocks
        var count = 0
        for need in needs {
            if need <= remaining {
                remaining -= need
                count += 1
            } else {
                break
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumBags(capacity: IntArray, rocks: IntArray, additionalRocks: Int): Int {
        val n = capacity.size
        val need = IntArray(n)
        for (i in 0 until n) {
            need[i] = capacity[i] - rocks[i]
        }
        java.util.Arrays.sort(need)
        var remaining = additionalRocks
        var count = 0
        for (x in need) {
            if (remaining >= x) {
                remaining -= x
                count++
            } else {
                break
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int maximumBags(List<int> capacity, List<int> rocks, int additionalRocks) {
    int n = capacity.length;
    List<int> need = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      need[i] = capacity[i] - rocks[i];
    }
    need.sort();
    int count = 0;
    for (int v in need) {
      if (additionalRocks >= v) {
        additionalRocks -= v;
        count++;
      } else {
        break;
      }
    }
    return count;
  }
}
```

## Golang

```go
import "sort"

func maximumBags(capacity []int, rocks []int, additionalRocks int) int {
	n := len(capacity)
	needs := make([]int, n)
	for i := 0; i < n; i++ {
		needs[i] = capacity[i] - rocks[i]
	}
	sort.Ints(needs)

	count := 0
	for _, need := range needs {
		if additionalRocks >= need {
			additionalRocks -= need
			count++
		} else {
			break
		}
	}
	return count
}
```

## Ruby

```ruby
def maximum_bags(capacity, rocks, additional_rocks)
  need = capacity.each_index.map { |i| capacity[i] - rocks[i] }
  need.sort!
  count = 0
  need.each do |r|
    break if r > additional_rocks
    additional_rocks -= r
    count += 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def maximumBags(capacity: Array[Int], rocks: Array[Int], additionalRocks: Int): Int = {
        val needed = capacity.indices.map(i => capacity(i) - rocks(i)).sorted
        var remaining = additionalRocks.toLong
        var count = 0
        for (need <- needed) {
            if (remaining >= need) {
                remaining -= need
                count += 1
            } else {
                return count
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_bags(capacity: Vec<i32>, rocks: Vec<i32>, additional_rocks: i32) -> i32 {
        let mut needs: Vec<i32> = capacity.iter().zip(rocks.iter())
            .map(|(&c, &r)| c - r)
            .collect();
        needs.sort_unstable();
        let mut remaining = additional_rocks;
        let mut count = 0;
        for need in needs {
            if remaining >= need {
                remaining -= need;
                count += 1;
            } else {
                break;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (maximum-bags capacity rocks additionalRocks)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([needs (map - capacity rocks)]
         [sorted-needs (sort needs <)])
    (let loop ((remaining sorted-needs) (rocks-left additionalRocks) (count 0))
      (cond
        [(null? remaining) count]
        [(<= (car remaining) rocks-left)
         (loop (cdr remaining) (- rocks-left (car remaining)) (+ count 1))]
        [else count]))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_bags/3]).

-spec maximum_bags(Capacity :: [integer()], Rocks :: [integer()], AdditionalRocks :: integer()) -> integer().
maximum_bags(Capacity, Rocks, AdditionalRocks) ->
    Needs = [C - R || {C,R} <- lists:zip(Capacity, Rocks)],
    SortedNeeds = lists:sort(Needs),
    count_full(SortedNeeds, AdditionalRocks, 0).

count_full([], _Rem, Acc) -> Acc;
count_full([Need|Rest], Rem, Acc) when Need =< Rem ->
    count_full(Rest, Rem - Need, Acc + 1);
count_full(_,_Rem, Acc) -> Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_bags(capacity :: [integer], rocks :: [integer], additional_rocks :: integer) :: integer
  def maximum_bags(capacity, rocks, additional_rocks) do
    needs =
      Enum.zip(capacity, rocks)
      |> Enum.map(fn {c, r} -> c - r end)
      |> Enum.sort()

    {count, _} =
      Enum.reduce_while(needs, {0, additional_rocks}, fn need, {cnt, rem} ->
        if need <= rem do
          {:cont, {cnt + 1, rem - need}}
        else
          {:halt, {cnt, rem}}
        end
      end)

    count
  end
end
```
