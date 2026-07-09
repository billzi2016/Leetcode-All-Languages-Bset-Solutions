# 1599. Maximum Profit of Operating a Centennial Wheel

## Cpp

```cpp
class Solution {
public:
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost, int runningCost) {
        long long profit = 0;
        long long maxProfit = LLONG_MIN;
        int answer = -1;
        long long waiting = 0;
        int rotations = 0;
        
        for (int c : customers) {
            waiting += c;
            int board = (int)min<long long>(4, waiting);
            waiting -= board;
            profit += (long long)board * boardingCost - runningCost;
            ++rotations;
            if (profit > maxProfit) {
                maxProfit = profit;
                answer = rotations;
            }
        }
        
        while (waiting > 0) {
            int board = (int)min<long long>(4, waiting);
            waiting -= board;
            profit += (long long)board * boardingCost - runningCost;
            ++rotations;
            if (profit > maxProfit) {
                maxProfit = profit;
                answer = rotations;
            }
        }
        
        return maxProfit > 0 ? answer : -1;
    }
};
```

## Java

```java
class Solution {
    public int minOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        long profit = 0;
        long maxProfit = Long.MIN_VALUE;
        int answer = -1;
        int waiting = 0;
        int rotations = 0;
        int i = 0;
        int n = customers.length;

        while (i < n || waiting > 0) {
            if (i < n) {
                waiting += customers[i];
                i++;
            }
            int board = Math.min(waiting, 4);
            profit += (long) board * boardingCost - runningCost;
            waiting -= board;
            rotations++;

            if (profit > maxProfit) {
                maxProfit = profit;
                answer = rotations;
            }
        }

        return maxProfit <= 0 ? -1 : answer;
    }
}
```

## Python

```python
class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        waiting = 0          # people waiting to board
        total_boarded = 0    # cumulative boarded passengers
        rotations = 0        # number of wheel rotations performed
        max_profit = 0
        best_rotations = -1

        n = len(customers)
        i = 0
        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
                i += 1
            # board up to 4 passengers
            board = 4 if waiting >= 4 else waiting
            waiting -= board
            total_boarded += board
            rotations += 1

            profit = total_boarded * boardingCost - rotations * runningCost
            if profit > max_profit:
                max_profit = profit
                best_rotations = rotations

        return best_rotations if max_profit > 0 else -1
```

## Python3

```python
class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        wait = 0
        total_boarded = 0
        max_profit = -float('inf')
        ans = -1
        i = 0
        rotations = 0
        n = len(customers)
        while i < n or wait > 0:
            if i < n:
                wait += customers[i]
                i += 1
            board = min(4, wait)
            wait -= board
            total_boarded += board
            rotations += 1
            profit = total_boarded * boardingCost - rotations * runningCost
            if profit > max_profit:
                max_profit = profit
                ans = rotations
        return ans if max_profit > 0 else -1
```

## C

```c
int minOperationsMaxProfit(int* customers, int customersSize, int boardingCost, int runningCost) {
    long long waiting = 0;
    long long profit = 0;
    long long maxProfit = 0;
    int bestRotations = -1;
    int rotations = 0;
    
    while (rotations < customersSize || waiting > 0) {
        if (rotations < customersSize) {
            waiting += customers[rotations];
        }
        long long board = waiting >= 4 ? 4 : waiting;
        waiting -= board;
        profit += board * boardingCost - runningCost;
        rotations++;
        if (profit > maxProfit) {
            maxProfit = profit;
            bestRotations = rotations;
        }
    }
    
    return (maxProfit <= 0) ? -1 : bestRotations;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        long profit = 0;
        long maxProfit = 0;
        int bestRotations = -1;
        int rotations = 0;
        int waiting = 0;
        int idx = 0;
        int n = customers.Length;

        while (idx < n || waiting > 0) {
            if (idx < n) {
                waiting += customers[idx];
                idx++;
            }
            int board = Math.Min(4, waiting);
            waiting -= board;
            profit += (long)board * boardingCost - runningCost;
            rotations++;

            if (profit > maxProfit) {
                maxProfit = profit;
                bestRotations = rotations;
            }
        }

        return maxProfit > 0 ? bestRotations : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} customers
 * @param {number} boardingCost
 * @param {number} runningCost
 * @return {number}
 */
var minOperationsMaxProfit = function(customers, boardingCost, runningCost) {
    let waiting = 0;
    let profit = 0;
    let maxProfit = 0;
    let answer = -1;
    let rotations = 0;
    let i = 0;
    const n = customers.length;

    while (i < n || waiting > 0) {
        if (i < n) {
            waiting += customers[i];
            i++;
        }
        const board = Math.min(4, waiting);
        waiting -= board;
        profit += board * boardingCost - runningCost;
        rotations++;

        if (profit > maxProfit) {
            maxProfit = profit;
            answer = rotations;
        }
    }

    return maxProfit > 0 ? answer : -1;
};
```

## Typescript

```typescript
function minOperationsMaxProfit(customers: number[], boardingCost: number, runningCost: number): number {
    let wait = 0;
    let totalBoarded = 0;
    let rotations = 0;
    let maxProfit = Number.MIN_SAFE_INTEGER;
    let answer = -1;

    const n = customers.length;
    let i = 0;
    while (i < n || wait > 0) {
        if (i < n) {
            wait += customers[i];
            i++;
        }
        const board = Math.min(4, wait);
        wait -= board;
        totalBoarded += board;
        rotations++;

        const profit = totalBoarded * boardingCost - rotations * runningCost;
        if (profit > maxProfit) {
            maxProfit = profit;
            answer = rotations;
        }
    }

    return maxProfit > 0 ? answer : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $customers
     * @param Integer $boardingCost
     * @param Integer $runningCost
     * @return Integer
     */
    function minOperationsMaxProfit($customers, $boardingCost, $runningCost) {
        $waiting = 0;
        $profit = 0;
        $maxProfit = PHP_INT_MIN;
        $answer = -1;
        $rotations = 0;
        $n = count($customers);
        $i = 0;

        while ($i < $n || $waiting > 0) {
            if ($i < $n) {
                $waiting += $customers[$i];
                $i++;
            }
            $board = min($waiting, 4);
            $waiting -= $board;
            $profit += $board * $boardingCost - $runningCost;
            $rotations++;

            if ($profit > $maxProfit) {
                $maxProfit = $profit;
                $answer = $rotations;
            }
        }

        return $maxProfit > 0 ? $answer : -1;
    }
}
```

## Swift

```swift
class Solution {
    func minOperationsMaxProfit(_ customers: [Int], _ boardingCost: Int, _ runningCost: Int) -> Int {
        var waiting = 0
        var served = 0
        var rotations = 0
        var maxProfit = 0
        var answer = -1
        
        var i = 0
        let n = customers.count
        
        while i < n || waiting > 0 {
            if i < n {
                waiting += customers[i]
                i += 1
            }
            
            let board = min(4, waiting)
            waiting -= board
            served += board
            rotations += 1
            
            let profit = served * boardingCost - rotations * runningCost
            if profit > maxProfit {
                maxProfit = profit
                answer = rotations
            }
        }
        
        return maxProfit > 0 ? answer : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperationsMaxProfit(customers: IntArray, boardingCost: Int, runningCost: Int): Int {
        var waiting = 0
        var totalBoarded = 0L
        var rotations = 0
        var maxProfit = Long.MIN_VALUE
        var answer = -1

        for (c in customers) {
            waiting += c
            val board = if (waiting >= 4) 4 else waiting
            waiting -= board
            totalBoarded += board
            rotations++
            val profit = totalBoarded * boardingCost - rotations.toLong() * runningCost
            if (profit > maxProfit) {
                maxProfit = profit
                answer = rotations
            }
        }

        while (waiting > 0) {
            val board = if (waiting >= 4) 4 else waiting
            waiting -= board
            totalBoarded += board
            rotations++
            val profit = totalBoarded * boardingCost - rotations.toLong() * runningCost
            if (profit > maxProfit) {
                maxProfit = profit
                answer = rotations
            }
        }

        return if (maxProfit <= 0L) -1 else answer
    }
}
```

## Dart

```dart
class Solution {
  int minOperationsMaxProfit(List<int> customers, int boardingCost, int runningCost) {
    int waiting = 0;
    int totalProfit = 0;
    int maxProfit = 0;
    int answer = -1;
    int rotations = 0;

    for (int i = 0; i < customers.length; i++) {
      waiting += customers[i];
      int board = waiting >= 4 ? 4 : waiting;
      waiting -= board;
      totalProfit += board * boardingCost - runningCost;
      rotations++;
      if (totalProfit > maxProfit) {
        maxProfit = totalProfit;
        answer = rotations;
      }
    }

    while (waiting > 0) {
      int board = waiting >= 4 ? 4 : waiting;
      waiting -= board;
      totalProfit += board * boardingCost - runningCost;
      rotations++;
      if (totalProfit > maxProfit) {
        maxProfit = totalProfit;
        answer = rotations;
      }
    }

    return maxProfit > 0 ? answer : -1;
  }
}
```

## Golang

```go
func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
    waiting := 0
    profit := 0
    maxProfit := 0
    answer := -1
    rotations := 0
    idx := 0

    for idx < len(customers) || waiting > 0 {
        if idx < len(customers) {
            waiting += customers[idx]
            idx++
        }
        board := 4
        if waiting < 4 {
            board = waiting
        }
        waiting -= board
        profit += board*boardingCost - runningCost
        rotations++

        if profit > maxProfit {
            maxProfit = profit
            answer = rotations
        }
    }

    if maxProfit <= 0 {
        return -1
    }
    return answer
}
```

## Ruby

```ruby
def min_operations_max_profit(customers, boarding_cost, running_cost)
  waiting = 0
  total_profit = 0
  max_profit = 0
  best_rotations = -1
  rotations = 0
  i = 0
  n = customers.length

  while i < n || waiting > 0
    if i < n
      waiting += customers[i]
      i += 1
    end

    board = waiting >= 4 ? 4 : waiting
    waiting -= board
    total_profit += board * boarding_cost - running_cost
    rotations += 1

    if total_profit > max_profit
      max_profit = total_profit
      best_rotations = rotations
    end
  end

  max_profit > 0 ? best_rotations : -1
end
```

## Scala

```scala
object Solution {
    def minOperationsMaxProfit(customers: Array[Int], boardingCost: Int, runningCost: Int): Int = {
        var idx = 0
        val n = customers.length
        var waiting: Long = 0L
        var profit: Long = 0L
        var maxProfit: Long = 0L
        var answer = -1
        var rotations = 0

        while (idx < n || waiting > 0) {
            if (idx < n) {
                waiting += customers(idx)
                idx += 1
            }
            val board = Math.min(4, waiting).toInt
            waiting -= board
            profit += board * boardingCost - runningCost
            rotations += 1
            if (profit > maxProfit) {
                maxProfit = profit
                answer = rotations
            }
        }

        if (maxProfit <= 0) -1 else answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations_max_profit(customers: Vec<i32>, boarding_cost: i32, running_cost: i32) -> i32 {
        let mut waiting: i64 = 0;
        let mut profit: i64 = 0;
        let mut max_profit: i64 = 0;
        let mut best_rotations: i32 = -1;
        let mut rotations: i64 = 0;

        for &c in customers.iter() {
            waiting += c as i64;
            let board = if waiting >= 4 { 4 } else { waiting };
            waiting -= board;
            profit += board * boarding_cost as i64 - running_cost as i64;
            rotations += 1;
            if profit > max_profit {
                max_profit = profit;
                best_rotations = rotations as i32;
            }
        }

        while waiting > 0 {
            let board = if waiting >= 4 { 4 } else { waiting };
            waiting -= board;
            profit += board * boarding_cost as i64 - running_cost as i64;
            rotations += 1;
            if profit > max_profit {
                max_profit = profit;
                best_rotations = rotations as i32;
            }
        }

        if max_profit <= 0 { -1 } else { best_rotations }
    }
}
```

## Racket

```racket
(define/contract (min-operations-max-profit customers boardingCost runningCost)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let ((n (length customers)))
    (let loop ((idx 0) (waiting 0) (profit 0) (maxProfit 0) (ans -1) (rot 0))
      (if (and (= idx n) (= waiting 0))
          (if (> maxProfit 0) ans -1)
          (let* ((new-waiting (+ waiting (if (< idx n) (list-ref customers idx) 0)))
                 (board (min new-waiting 4))
                 (after-board (- new-waiting board))
                 (new-profit (+ profit (- (* board boardingCost) runningCost)))
                 (new-rot (+ rot 1))
                 (new-maxProfit (if (> new-profit maxProfit) new-profit maxProfit))
                 (new-ans (if (> new-profit maxProfit) new-rot ans)))
            (loop (if (< idx n) (+ idx 1) idx)
                  after-board
                  new-profit
                  new-maxProfit
                  new-ans
                  new-rot))))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations_max_profit/3]).

-spec min_operations_max_profit(Customers :: [integer()], BoardingCost :: integer(), RunningCost :: integer()) -> integer().
min_operations_max_profit(Customers, BoardingCost, RunningCost) ->
    process(Customers, 0, 0, 0, 0, -1, BoardingCost, RunningCost).

process([], Waiting, _Rotations, _Profit, MaxProfit, Answer, _BoardingCost, _RunningCost) when Waiting =:= 0 ->
    case MaxProfit > 0 of
        true -> Answer;
        false -> -1
    end;
process(Customers, Waiting, Rotations, Profit, MaxProfit, Answer, BoardingCost, RunningCost) ->
    {Arrival, RestCustomers} =
        case Customers of
            [] -> {0, []};
            [H|T] -> {H, T}
        end,
    NewWaiting = Waiting + Arrival,
    Board = erlang:min(NewWaiting, 4),
    NextWaiting = NewWaiting - Board,
    NextRotations = Rotations + 1,
    NextProfit = Profit + Board * BoardingCost - RunningCost,
    {NextMaxProfit, NextAnswer} =
        if
            NextProfit > MaxProfit ->
                {NextProfit, NextRotations};
            true ->
                {MaxProfit, Answer}
        end,
    process(RestCustomers, NextWaiting, NextRotations, NextProfit, NextMaxProfit, NextAnswer, BoardingCost, RunningCost).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations_max_profit(customers :: [integer], boarding_cost :: integer, running_cost :: integer) :: integer
  def min_operations_max_profit(customers, boarding_cost, running_cost) do
    {max_profit, answer, profit, waiting, rot} =
      Enum.reduce(customers, {0, -1, 0, 0, 0}, fn cust,
                                            {max_p, ans, prof, wait, r} ->
        wait = wait + cust
        board = min(wait, 4)
        wait = wait - board
        prof = prof + board * boarding_cost - running_cost
        r = r + 1

        if prof > max_p do
          {prof, r, prof, wait, r}
        else
          {max_p, ans, prof, wait, r}
        end
      end)

    {final_max, final_ans} =
      process_waiting(waiting, max_profit, answer, profit, boarding_cost,
        running_cost, rot)

    if final_max > 0 do
      final_ans
    else
      -1
    end
  end

  defp process_waiting(0, max_p, ans, _profit, _bc, _rc, _rot), do: {max_p, ans}

  defp process_waiting(waiting, max_p, ans, profit, boarding_cost,
        running_cost, rot) do
    board = min(waiting, 4)
    waiting = waiting - board
    profit = profit + board * boarding_cost - running_cost
    rot = rot + 1

    {max_p, ans} =
      if profit > max_p do
        {profit, rot}
      else
        {max_p, ans}
      end

    process_waiting(waiting, max_p, ans, profit, boarding_cost,
      running_cost, rot)
  end
end
```
