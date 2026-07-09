# 0134. Gas Station

## Cpp

```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        long long total = 0, tank = 0;
        int start = 0;
        for (int i = 0; i < (int)gas.size(); ++i) {
            long long diff = (long long)gas[i] - cost[i];
            total += diff;
            tank += diff;
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total >= 0 ? start % gas.size() : -1;
    }
};
```

## Java

```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, tank = 0, start = 0;
        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            total += diff;
            tank += diff;
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total >= 0 ? start % gas.length : -1;
    }
}
```

## Python

```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1
```

## Python3

```python
class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        return start if total_tank >= 0 else -1
```

## C

```c
int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
    long total = 0;
    long tank = 0;
    int start = 0;
    for (int i = 0; i < gasSize; ++i) {
        int diff = gas[i] - cost[i];
        total += diff;
        tank += diff;
        if (tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }
    return (total >= 0) ? start % gasSize : -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int CanCompleteCircuit(int[] gas, int[] cost)
    {
        int n = gas.Length;
        long totalTank = 0;
        long currTank = 0;
        int startStation = 0;

        for (int i = 0; i < n; i++)
        {
            long diff = (long)gas[i] - cost[i];
            totalTank += diff;
            currTank += diff;

            if (currTank < 0)
            {
                startStation = i + 1;
                currTank = 0;
            }
        }

        return totalTank >= 0 ? startStation % n : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    let total = 0;
    let tank = 0;
    let start = 0;
    for (let i = 0; i < gas.length; i++) {
        const diff = gas[i] - cost[i];
        total += diff;
        tank += diff;
        if (tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }
    return total >= 0 ? start % gas.length : -1;
};
```

## Typescript

```typescript
function canCompleteCircuit(gas: number[], cost: number[]): number {
    let total = 0;
    let tank = 0;
    let start = 0;
    const n = gas.length;
    for (let i = 0; i < n; i++) {
        const diff = gas[i] - cost[i];
        total += diff;
        tank += diff;
        if (tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }
    return total >= 0 ? start % n : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $gas
     * @param Integer[] $cost
     * @return Integer
     */
    function canCompleteCircuit($gas, $cost) {
        $total = 0;
        $tank = 0;
        $start = 0;
        $n = count($gas);
        for ($i = 0; $i < $n; $i++) {
            $diff = $gas[$i] - $cost[$i];
            $total += $diff;
            $tank += $diff;
            if ($tank < 0) {
                $start = $i + 1;
                $tank = 0;
            }
        }
        return $total >= 0 ? $start % $n : -1;
    }
}
```

## Swift

```swift
class Solution {
    func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {
        var total = 0
        var tank = 0
        var start = 0
        for i in 0..<gas.count {
            let diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0 {
                start = i + 1
                tank = 0
            }
        }
        return total >= 0 ? start % gas.count : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canCompleteCircuit(gas: IntArray, cost: IntArray): Int {
        var total = 0
        var tank = 0
        var start = 0
        for (i in gas.indices) {
            val diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if (tank < 0) {
                start = i + 1
                tank = 0
            }
        }
        return if (total >= 0) start % gas.size else -1
    }
}
```

## Dart

```dart
class Solution {
  int canCompleteCircuit(List<int> gas, List<int> cost) {
    int n = gas.length;
    int totalTank = 0;
    int currTank = 0;
    int start = 0;

    for (int i = 0; i < n; i++) {
      int diff = gas[i] - cost[i];
      totalTank += diff;
      currTank += diff;
      if (currTank < 0) {
        start = i + 1;
        currTank = 0;
      }
    }

    return totalTank >= 0 ? start % n : -1;
  }
}
```

## Golang

```go
func canCompleteCircuit(gas []int, cost []int) int {
    total, tank, start := 0, 0, 0
    for i := 0; i < len(gas); i++ {
        diff := gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0 {
            start = i + 1
            tank = 0
        }
    }
    if total < 0 {
        return -1
    }
    if start >= len(gas) {
        return -1
    }
    return start
}
```

## Ruby

```ruby
def can_complete_circuit(gas, cost)
  total = 0
  tank = 0
  start = 0
  gas.each_index do |i|
    diff = gas[i] - cost[i]
    total += diff
    tank += diff
    if tank < 0
      start = i + 1
      tank = 0
    end
  end
  total >= 0 ? start : -1
end
```

## Scala

```scala
object Solution {
    def canCompleteCircuit(gas: Array[Int], cost: Array[Int]): Int = {
        var total = 0L
        var tank = 0L
        var start = 0
        for (i <- gas.indices) {
            val diff = gas(i).toLong - cost(i).toLong
            total += diff
            tank += diff
            if (tank < 0) {
                start = i + 1
                tank = 0L
            }
        }
        if (total >= 0) {
            if (start == gas.length) -1 else start
        } else {
            -1
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n = gas.len();
        let mut total_tank: i64 = 0;
        let mut curr_tank: i64 = 0;
        let mut start: usize = 0;

        for i in 0..n {
            let diff = gas[i] as i64 - cost[i] as i64;
            total_tank += diff;
            curr_tank += diff;
            if curr_tank < 0 {
                start = i + 1;
                curr_tank = 0;
            }
        }

        if total_tank >= 0 && start < n {
            start as i32
        } else {
            -1
        }
    }
}
```

## Racket

```racket
(define/contract (can-complete-circuit gas cost)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([n (length gas)]
         [gvec (list->vector gas)]
         [cvec (list->vector cost)])
    (let loop ((i 0) (total 0) (curr 0) (start 0))
      (if (= i n)
          (if (>= total 0) start -1)
          (let* ([diff (- (vector-ref gvec i) (vector-ref cvec i))]
                 [new-total (+ total diff)]
                 [new-curr (+ curr diff)])
            (if (< new-curr 0)
                (loop (+ i 1) new-total 0 (+ i 1))
                (loop (+ i 1) new-total new-curr start)))))))
```

## Erlang

```erlang
-spec can_complete_circuit(Gas :: [integer()], Cost :: [integer()]) -> integer().
can_complete_circuit(Gas, Cost) ->
    Total = lists:foldl(fun({G, C}, Acc) -> Acc + G - C end,
                        0,
                        lists:zip(Gas, Cost)),
    if
        Total < 0 ->
            -1;
        true ->
            {Start, _} = find_start(lists:zip(Gas, Cost), 0, 0, 0),
            Start
    end.

find_start([], _Idx, _Tank, Start) ->
    {Start, ok};
find_start([{G, C} | Rest], Index, Tank, Start) ->
    NewTank = Tank + G - C,
    if
        NewTank < 0 ->
            find_start(Rest, Index + 1, 0, Index + 1);
        true ->
            find_start(Rest, Index + 1, NewTank, Start)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_complete_circuit(gas :: [integer], cost :: [integer]) :: integer
  def can_complete_circuit(gas, cost) do
    pairs = Enum.zip(gas, cost)

    {total, _curr, start} =
      Enum.reduce(Enum.with_index(pairs), {0, 0, 0}, fn {{g, c}, idx},
                                                      {tot, cur, start_idx} ->
        diff = g - c
        tot2 = tot + diff
        cur2 = cur + diff

        if cur2 < 0 do
          {tot2, 0, idx + 1}
        else
          {tot2, cur2, start_idx}
        end
      end)

    if total >= 0 and start < length(gas), do: start, else: -1
  end
end
```
