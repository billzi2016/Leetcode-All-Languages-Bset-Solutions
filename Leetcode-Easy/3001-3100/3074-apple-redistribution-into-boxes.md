# 3074. Apple Redistribution into Boxes

## Cpp

```cpp
class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        long long total = 0;
        for (int a : apple) total += a;
        sort(capacity.begin(), capacity.end(), greater<int>());
        long long cur = 0;
        int cnt = 0;
        for (int cap : capacity) {
            cur += cap;
            ++cnt;
            if (cur >= total) break;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        int total = 0;
        for (int a : apple) total += a;
        java.util.Arrays.sort(capacity);
        int sum = 0;
        int count = 0;
        for (int i = capacity.length - 1; i >= 0 && sum < total; i--) {
            sum += capacity[i];
            count++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total = sum(apple)
        capacity.sort(reverse=True)
        cur = 0
        for i, cap in enumerate(capacity, 1):
            cur += cap
            if cur >= total:
                return i
        return len(capacity)
```

## Python3

```python
from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        used = 0
        cur = 0
        for cap in capacity:
            cur += cap
            used += 1
            if cur >= total_apples:
                return used
        return used
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    return *(const int *)b - *(const int *)a;
}

int minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize) {
    int total = 0;
    for (int i = 0; i < appleSize; ++i) {
        total += apple[i];
    }
    
    qsort(capacity, capacitySize, sizeof(int), cmp_desc);
    
    int sum = 0;
    for (int i = 0; i < capacitySize; ++i) {
        sum += capacity[i];
        if (sum >= total) {
            return i + 1;
        }
    }
    return capacitySize;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumBoxes(int[] apple, int[] capacity) {
        int totalApples = 0;
        foreach (int a in apple) totalApples += a;

        Array.Sort(capacity);
        int sum = 0, boxesUsed = 0;
        for (int i = capacity.Length - 1; i >= 0 && sum < totalApples; i--) {
            sum += capacity[i];
            boxesUsed++;
        }
        return boxesUsed;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function(apple, capacity) {
    const totalApples = apple.reduce((a, b) => a + b, 0);
    capacity.sort((a, b) => b - a); // descending
    let sum = 0;
    for (let i = 0; i < capacity.length; ++i) {
        sum += capacity[i];
        if (sum >= totalApples) return i + 1;
    }
    return capacity.length; // fallback, though problem guarantees feasibility
};
```

## Typescript

```typescript
function minimumBoxes(apple: number[], capacity: number[]): number {
    const totalApples = apple.reduce((sum, val) => sum + val, 0);
    capacity.sort((a, b) => b - a);
    let accumulated = 0;
    for (let i = 0; i < capacity.length; i++) {
        accumulated += capacity[i];
        if (accumulated >= totalApples) return i + 1;
    }
    return capacity.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $apple
     * @param Integer[] $capacity
     * @return Integer
     */
    function minimumBoxes($apple, $capacity) {
        $totalApples = array_sum($apple);
        rsort($capacity); // sort capacities in descending order
        
        $sum = 0;
        $boxesUsed = 0;
        foreach ($capacity as $cap) {
            $sum += $cap;
            $boxesUsed++;
            if ($sum >= $totalApples) {
                break;
            }
        }
        return $boxesUsed;
    }
}
```

## Swift

```swift
class Solution {
    func minimumBoxes(_ apple: [Int], _ capacity: [Int]) -> Int {
        let totalApples = apple.reduce(0, +)
        let sortedCapacities = capacity.sorted(by: >)
        var accumulated = 0
        var boxesUsed = 0
        for cap in sortedCapacities {
            if accumulated >= totalApples { break }
            accumulated += cap
            boxesUsed += 1
        }
        return boxesUsed
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumBoxes(apple: IntArray, capacity: IntArray): Int {
        val totalApples = apple.sum()
        var sumCapacity = 0
        var boxesUsed = 0
        for (c in capacity.sortedDescending()) {
            sumCapacity += c
            boxesUsed++
            if (sumCapacity >= totalApples) return boxesUsed
        }
        return boxesUsed
    }
}
```

## Dart

```dart
class Solution {
  int minimumBoxes(List<int> apple, List<int> capacity) {
    int total = apple.reduce((a, b) => a + b);
    capacity.sort();
    int sum = 0;
    int count = 0;
    for (int i = capacity.length - 1; i >= 0; i--) {
      sum += capacity[i];
      count++;
      if (sum >= total) break;
    }
    return count;
  }
}
```

## Golang

```go
import "sort"

func minimumBoxes(apple []int, capacity []int) int {
    total := 0
    for _, a := range apple {
        total += a
    }
    sort.Sort(sort.Reverse(sort.IntSlice(capacity)))
    sum, cnt := 0, 0
    for _, c := range capacity {
        sum += c
        cnt++
        if sum >= total {
            return cnt
        }
    }
    return cnt
}
```

## Ruby

```ruby
def minimum_boxes(apple, capacity)
  required = apple.sum
  sorted = capacity.sort.reverse
  used = 0
  accumulated = 0
  sorted.each do |c|
    break if accumulated >= required
    accumulated += c
    used += 1
  end
  used
end
```

## Scala

```scala
object Solution {
    def minimumBoxes(apple: Array[Int], capacity: Array[Int]): Int = {
        val totalApples = apple.sum
        val sortedCapacities = capacity.sorted(Ordering.Int.reverse)
        var sum = 0
        var count = 0
        for (c <- sortedCapacities) {
            if (sum >= totalApples) return count
            sum += c
            count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>) -> i32 {
        let total_apples: i32 = apple.iter().sum();
        let mut caps = capacity;
        caps.sort_by(|a, b| b.cmp(a)); // descending
        let mut sum = 0;
        for (i, c) in caps.iter().enumerate() {
            sum += *c;
            if sum >= total_apples {
                return (i + 1) as i32;
            }
        }
        caps.len() as i32 // should never reach here due to problem guarantee
    }
}
```

## Racket

```racket
(define/contract (minimum-boxes apple capacity)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((total (apply + apple))
         (sorted (sort capacity >)))
    (let loop ((remaining total) (cnt 0) (caps sorted))
      (if (<= remaining 0)
          cnt
          (loop (- remaining (car caps)) (+ cnt 1) (cdr caps))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_boxes/2]).

-spec minimum_boxes(Apple :: [integer()], Capacity :: [integer()]) -> integer().
minimum_boxes(Apple, Capacity) ->
    Total = lists:sum(Apple),
    SortedDesc = lists:reverse(lists:sort(Capacity)),
    select_boxes(SortedDesc, Total, 0).

select_boxes(_, Remaining, Count) when Remaining =< 0 ->
    Count;
select_boxes([Cap|Rest], Remaining, Count) ->
    select_boxes(Rest, Remaining - Cap, Count + 1);
select_boxes([], _, Count) ->
    Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_boxes(apple :: [integer], capacity :: [integer]) :: integer
  def minimum_boxes(apple, capacity) do
    required = Enum.sum(apple)

    if required == 0 do
      0
    else
      capacity
      |> Enum.sort(:desc)
      |> Enum.reduce_while({0, 0}, fn cap, {cnt, sum} ->
        new_sum = sum + cap
        new_cnt = cnt + 1

        if new_sum >= required do
          {:halt, new_cnt}
        else
          {:cont, {new_cnt, new_sum}}
        end
      end)
    end
  end
end
```
