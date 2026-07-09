# 1029. Two City Scheduling

## Cpp

```cpp
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        sort(costs.begin(), costs.end(),
             [](const vector<int>& x, const vector<int>& y) {
                 return (x[0] - x[1]) < (y[0] - y[1]);
             });
        int n = costs.size() / 2;
        int total = 0;
        for (int i = 0; i < costs.size(); ++i) {
            total += (i < n) ? costs[i][0] : costs[i][1];
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int twoCitySchedCost(int[][] costs) {
        java.util.Arrays.sort(costs, (c1, c2) -> Integer.compare(c1[0] - c1[1], c2[0] - c2[1]));
        int n = costs.length / 2;
        int total = 0;
        for (int i = 0; i < n; i++) {
            total += costs[i][0];
        }
        for (int i = n; i < costs.length; i++) {
            total += costs[i][1];
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Sort by the difference between cost to city A and city B.
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0]
        for i in range(n, len(costs)):
            total += costs[i][1]
        return total
```

## Python3

```python
from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by the difference between cost to city A and city B
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0]   # send first n people to city A
        for i in range(n, 2 * n):
            total += costs[i][1]   # send remaining to city B
        return total
```

## C

```c
#include <stdlib.h>

static int cmpDiff(const void *p1, const void *p2) {
    const int *a = *(const int **)p1;
    const int *b = *(const int **)p2;
    return (a[0] - a[1]) - (b[0] - b[1]);
}

int twoCitySchedCost(int** costs, int costsSize, int* costsColSize) {
    qsort(costs, (size_t)costsSize, sizeof(int *), cmpDiff);
    int n = costsSize / 2;
    int total = 0;
    for (int i = 0; i < costsSize; ++i) {
        if (i < n)
            total += costs[i][0];
        else
            total += costs[i][1];
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int TwoCitySchedCost(int[][] costs) {
        System.Array.Sort(costs, (x, y) => (x[0] - x[1]) - (y[0] - y[1]));
        int n = costs.Length / 2;
        int total = 0;
        for (int i = 0; i < n; ++i)
            total += costs[i][0];
        for (int i = n; i < costs.Length; ++i)
            total += costs[i][1];
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function(costs) {
    costs.sort((c1, c2) => (c1[0] - c1[1]) - (c2[0] - c2[1]));
    const n = costs.length >> 1;
    let total = 0;
    for (let i = 0; i < costs.length; ++i) {
        total += i < n ? costs[i][0] : costs[i][1];
    }
    return total;
};
```

## Typescript

```typescript
function twoCitySchedCost(costs: number[][]): number {
    // Sort by the difference between cost to city A and city B
    costs.sort((c1, c2) => (c1[0] - c1[1]) - (c2[0] - c2[1]));
    const n = costs.length >> 1;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        total += costs[i][0]; // send first n people to city A
    }
    for (let i = n; i < costs.length; ++i) {
        total += costs[i][1]; // send remaining to city B
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $costs
     * @return Integer
     */
    function twoCitySchedCost($costs) {
        usort($costs, function($a, $b) {
            $diffA = $a[0] - $a[1];
            $diffB = $b[0] - $b[1];
            return $diffA <=> $diffB;
        });
        $n = intdiv(count($costs), 2);
        $total = 0;
        foreach ($costs as $idx => $c) {
            if ($idx < $n) {
                $total += $c[0];
            } else {
                $total += $c[1];
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func twoCitySchedCost(_ costs: [[Int]]) -> Int {
        let sorted = costs.sorted { (c1, c2) -> Bool in
            return (c1[0] - c1[1]) < (c2[0] - c2[1])
        }
        var total = 0
        let n = costs.count / 2
        for i in 0..<sorted.count {
            if i < n {
                total += sorted[i][0]
            } else {
                total += sorted[i][1]
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun twoCitySchedCost(costs: Array<IntArray>): Int {
        val sorted = costs.sortedBy { it[0] - it[1] }
        var total = 0
        val n = costs.size / 2
        for (i in 0 until n) {
            total += sorted[i][0]
        }
        for (i in n until costs.size) {
            total += sorted[i][1]
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int twoCitySchedCost(List<List<int>> costs) {
    costs.sort((a, b) => (a[0] - a[1]) - (b[0] - b[1]));
    int n = costs.length ~/ 2;
    int total = 0;
    for (int i = 0; i < costs.length; i++) {
      total += i < n ? costs[i][0] : costs[i][1];
    }
    return total;
  }
}
```

## Golang

```go
func twoCitySchedCost(costs [][]int) int {
	type pair struct {
		a, b int
	}
	n := len(costs)
	arr := make([]pair, n)
	for i, c := range costs {
		arr[i] = pair{a: c[0], b: c[1]}
	}
	sort.Slice(arr, func(i, j int) bool {
		return (arr[i].a - arr[i].b) < (arr[j].a - arr[j].b)
	})
	total := 0
	half := n / 2
	for i := 0; i < half; i++ {
		total += arr[i].a
	}
	for i := half; i < n; i++ {
		total += arr[i].b
	}
	return total
}
```

## Ruby

```ruby
def two_city_sched_cost(costs)
  n = costs.length / 2
  sorted = costs.sort_by { |a, b| a - b }
  total = 0
  sorted.each_with_index do |(a, b), i|
    total += i < n ? a : b
  end
  total
end
```

## Scala

```scala
object Solution {
    def twoCitySchedCost(costs: Array[Array[Int]]): Int = {
        val sorted = costs.sortBy(c => c(0) - c(1))
        val n = costs.length / 2
        var total = 0
        for (i <- 0 until n) {
            total += sorted(i)(0)
        }
        for (i <- n until costs.length) {
            total += sorted(i)(1)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn two_city_sched_cost(costs: Vec<Vec<i32>>) -> i32 {
        let mut costs = costs;
        costs.sort_by_key(|c| c[0] - c[1]);
        let n = costs.len() / 2;
        let mut total = 0i32;
        for i in 0..n {
            total += costs[i][0];
        }
        for i in n..costs.len() {
            total += costs[i][1];
        }
        total
    }
}
```

## Racket

```racket
(define/contract (two-city-sched-cost costs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted (sort costs
                       (lambda (c1 c2)
                         (< (- (first c1) (second c1))
                            (- (first c2) (second c2))))))
         (n (/ (length costs) 2)))
    (let loop ((lst sorted) (i 0) (total 0))
      (if (null? lst)
          total
          (let* ((c (car lst))
                 (cost (if (< i n) (first c) (second c))))
            (loop (cdr lst) (+ i 1) (+ total cost)))))))
```

## Erlang

```erlang
-module(solution).
-export([two_city_sched_cost/1]).

-spec two_city_sched_cost(Costs :: [[integer()]]) -> integer().
two_city_sched_cost(Costs) ->
    Sorted = lists:sort(fun([A1, B1], [A2, B2]) -> (A1 - B1) > (A2 - B2) end, Costs),
    N = length(Costs) div 2,
    {FirstN, Rest} = split_at(N, Sorted),
    SumA = sum_city(FirstN, a),
    SumB = sum_city(Rest, b),
    SumA + SumB.

split_at(0, List) -> {[], List};
split_at(N, List) when N > 0 ->
    split_at(N, List, []).

split_at(0, Rest, Acc) -> {lists:reverse(Acc), Rest};
split_at(N, [H|T], Acc) ->
    split_at(N - 1, T, [H | Acc]).

sum_city([], _) -> 0;
sum_city([[A,_]|T], a) -> A + sum_city(T, a);
sum_city([[_,B]|T], b) -> B + sum_city(T, b).
```

## Elixir

```elixir
defmodule Solution do
  @spec two_city_sched_cost(costs :: [[integer]]) :: integer
  def two_city_sched_cost(costs) do
    sorted = Enum.sort_by(costs, fn [a, b] -> a - b end)
    n = div(length(sorted), 2)

    {first_n, last_n} = Enum.split(sorted, n)

    sum_a = Enum.reduce(first_n, 0, fn [a, _b], acc -> acc + a end)
    sum_b = Enum.reduce(last_n, 0, fn [_a, b], acc -> acc + b end)

    sum_a + sum_b
  end
end
```
