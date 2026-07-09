# 2144. Minimum Cost of Buying Candies With Discount

## Cpp

```cpp
class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(), cost.end(), greater<int>());
        int total = 0;
        for (int i = 0; i < (int)cost.size(); ++i) {
            if (i % 3 != 2) total += cost[i];
        }
        return total;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int total = 0;
        int cnt = 0;
        for (int i = cost.length - 1; i >= 0; i--) {
            if (cnt % 3 != 2) {
                total += cost[i];
            }
            cnt++;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        total = 0
        for i, c in enumerate(cost):
            if i % 3 != 2:  # pay for first two in each group of three
                total += c
        return total
```

## Python3

```python
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for i, c in enumerate(cost):
            if i % 3 != 2:  # every third candy (0-indexed) is free
                total += c
        return total
```

## C

```c
#include <stdlib.h>

static int compareDesc(const void *a, const void *b) {
    return *(int *)b - *(int *)a;
}

int minimumCost(int* cost, int costSize) {
    if (costSize == 0) return 0;
    qsort(cost, costSize, sizeof(int), compareDesc);
    int total = 0;
    for (int i = 0; i < costSize; ++i) {
        if (i % 3 != 2) {
            total += cost[i];
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumCost(int[] cost)
    {
        System.Array.Sort(cost);
        int total = 0;
        int n = cost.Length;
        // Iterate from most expensive to cheapest
        for (int i = n - 1, idx = 0; i >= 0; i--, idx++)
        {
            // Skip every third candy (free one)
            if (idx % 3 != 2)
                total += cost[i];
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(cost) {
    cost.sort((a, b) => b - a);
    let total = 0;
    for (let i = 0; i < cost.length; i++) {
        if (i % 3 !== 2) {
            total += cost[i];
        }
    }
    return total;
};
```

## Typescript

```typescript
function minimumCost(cost: number[]): number {
    // Sort costs in descending order
    cost.sort((a, b) => b - a);
    let total = 0;
    for (let i = 0; i < cost.length; i++) {
        // Every third candy (i % 3 === 2) is free
        if (i % 3 !== 2) {
            total += cost[i];
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($cost) {
        rsort($cost);
        $total = 0;
        foreach ($cost as $i => $c) {
            if ($i % 3 !== 2) {
                $total += $c;
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ cost: [Int]) -> Int {
        let sorted = cost.sorted(by: >)
        var total = 0
        for (i, c) in sorted.enumerated() {
            if i % 3 != 2 {
                total += c
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(cost: IntArray): Int {
        cost.sort()
        var total = 0
        val n = cost.size
        for (i in n - 1 downTo 0) {
            val idxFromEnd = n - 1 - i
            if (idxFromEnd % 3 == 2) continue
            total += cost[i]
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(List<int> cost) {
    cost.sort((a, b) => b - a);
    int total = 0;
    for (int i = 0; i < cost.length; i++) {
      if (i % 3 != 2) {
        total += cost[i];
      }
    }
    return total;
  }
}
```

## Golang

```go
import "sort"

func minimumCost(cost []int) int {
	sort.Slice(cost, func(i, j int) bool { return cost[i] > cost[j] })
	total := 0
	for i, c := range cost {
		if i%3 != 2 {
			total += c
		}
	}
	return total
}
```

## Ruby

```ruby
def minimum_cost(cost)
  sorted = cost.sort.reverse
  total = 0
  sorted.each_with_index do |c, i|
    total += c unless i % 3 == 2
  end
  total
end
```

## Scala

```scala
object Solution {
    def minimumCost(cost: Array[Int]): Int = {
        val sorted = cost.sorted(Ordering.Int.reverse)
        var total = 0
        for (i <- sorted.indices) {
            if (i % 3 != 2) total += sorted(i)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_cost(cost: Vec<i32>) -> i32 {
        let mut v = cost;
        v.sort_unstable_by(|a, b| b.cmp(a));
        let mut total = 0;
        for (i, &c) in v.iter().enumerate() {
            if i % 3 != 2 {
                total += c;
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (minimum-cost cost)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort cost >)])
    (let loop ((lst sorted) (idx 0) (total 0))
      (if (null? lst)
          total
          (let ((c (car lst)))
            (loop (cdr lst)
                  (+ idx 1)
                  (if (= (modulo idx 3) 2)
                      total
                      (+ total c))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_cost/1]).

-spec minimum_cost(Cost :: [integer()]) -> integer().
minimum_cost(Cost) ->
    SortedDesc = lists:reverse(lists:sort(Cost)),
    sum_pay(SortedDesc, 0, 1).

sum_pay([], Acc, _Idx) -> Acc;
sum_pay([H|T], Acc, Idx) ->
    NewAcc = case Idx rem 3 of
        0 -> Acc;          % free candy
        _ -> Acc + H       % pay for this candy
    end,
    sum_pay(T, NewAcc, Idx + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(cost :: [integer]) :: integer
  def minimum_cost(cost) do
    cost
    |> Enum.sort(&>=/2)
    |> Enum.with_index()
    |> Enum.reduce(0, fn {c, i}, acc ->
      if rem(i + 1, 3) == 0, do: acc, else: acc + c
    end)
  end
end
```
