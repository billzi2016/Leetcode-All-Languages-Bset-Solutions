# 0517. Super Washing Machines

## Cpp

```cpp
class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int n = machines.size();
        long long total = 0;
        for (int v : machines) total += v;
        if (total % n != 0) return -1;
        long long avg = total / n;
        long long ans = 0, prefix = 0;
        for (int i = 0; i < n; ++i) {
            long long diff = (long long)machines[i] - avg;
            prefix += diff;
            long long moves = max(llabs(prefix), diff);
            ans = max(ans, moves);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int findMinMoves(int[] machines) {
        int n = machines.length;
        long sum = 0;
        for (int v : machines) sum += v;
        if (sum % n != 0) return -1;
        long avg = sum / n;
        long left = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            long diff = machines[i] - avg;
            left += diff;
            int cur = (int)Math.max(Math.abs(left), diff);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        avg = total // n
        max_moves = 0
        cum = 0
        for m in machines:
            diff = m - avg
            cum += diff
            max_moves = max(max_moves, abs(cum), diff)
        return max_moves
```

## Python3

```python
from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        avg = total // n
        ans = 0
        left_balance = 0
        for m in machines:
            cur = m - avg          # excess (+) or deficit (-) at current machine
            left_balance += cur    # net dresses that must cross the boundary to the right
            ans = max(ans, max(abs(left_balance), cur))
        return ans
```

## C

```c
#include <stdlib.h>

int findMinMoves(int* machines, int machinesSize) {
    long long sum = 0;
    for (int i = 0; i < machinesSize; ++i) {
        sum += machines[i];
    }
    if (sum % machinesSize != 0) return -1;

    long long avg = sum / machinesSize;
    long long max_moves = 0;
    long long balance = 0;

    for (int i = 0; i < machinesSize; ++i) {
        long long diff = (long long)machines[i] - avg;
        balance += diff;
        long long cur = llabs(balance);
        if (diff > cur) cur = diff;
        if (cur > max_moves) max_moves = cur;
    }
    return (int)max_moves;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMinMoves(int[] machines) {
        long total = 0;
        foreach (int m in machines) total += m;
        int n = machines.Length;
        if (total % n != 0) return -1;
        long avg = total / n;
        long maxMoves = 0;
        long prefix = 0;
        for (int i = 0; i < n; i++) {
            long curExcess = machines[i] - avg;
            long leftDiff = prefix - i * avg;
            long movesNeeded = Math.Max(Math.Abs(leftDiff), curExcess);
            if (movesNeeded > maxMoves) maxMoves = movesNeeded;
            prefix += machines[i];
        }
        return (int)maxMoves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} machines
 * @return {number}
 */
var findMinMoves = function(machines) {
    const n = machines.length;
    let total = 0;
    for (let v of machines) total += v;
    if (total % n !== 0) return -1;
    const avg = total / n;
    let maxMove = 0;
    let prefix = 0;
    for (let i = 0; i < n; ++i) {
        const diff = machines[i] - avg;
        prefix += diff;
        const cur = Math.max(Math.abs(prefix), diff);
        if (cur > maxMove) maxMove = cur;
    }
    return maxMove;
};
```

## Typescript

```typescript
function findMinMoves(machines: number[]): number {
    const n = machines.length;
    const total = machines.reduce((sum, v) => sum + v, 0);
    if (total % n !== 0) return -1;
    const avg = total / n;

    let maxMove = 0;
    let prefix = 0; // net dresses that need to pass the boundary to the right

    for (let i = 0; i < n; i++) {
        const diff = machines[i] - avg; // excess at current machine
        prefix += diff;
        const movesNeeded = Math.max(Math.abs(prefix), diff);
        if (movesNeeded > maxMove) maxMove = movesNeeded;
    }

    return maxMove;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $machines
     * @return Integer
     */
    function findMinMoves($machines) {
        $n = count($machines);
        $sum = array_sum($machines);
        if ($sum % $n !== 0) {
            return -1;
        }
        $avg = intdiv($sum, $n);
        $maxMove = 0;
        $leftSum = 0;
        foreach ($machines as $val) {
            $diff = $val - $avg;          // excess or deficit at current machine
            $left = $leftSum;             // net excess on the left side before this machine
            $maxMove = max($maxMove, max(abs($left), $diff));
            $leftSum += $diff;
        }
        return $maxMove;
    }
}
?>
```

## Swift

```swift
class Solution {
    func findMinMoves(_ machines: [Int]) -> Int {
        let n = machines.count
        var total = 0
        for m in machines { total += m }
        if total % n != 0 { return -1 }
        let avg = total / n
        var ans = 0
        var prefix = 0
        for m in machines {
            let diff = m - avg
            prefix += diff
            let cur = max(abs(prefix), diff)
            if cur > ans { ans = cur }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinMoves(machines: IntArray): Int {
        val n = machines.size
        var total = 0L
        for (v in machines) total += v.toLong()
        if (total % n != 0L) return -1
        val avg = (total / n).toInt()
        var maxMoves = 0
        var prefix = 0
        for (i in 0 until n) {
            val diff = machines[i] - avg
            prefix += diff
            val moves = kotlin.math.max(kotlin.math.abs(prefix), diff)
            if (moves > maxMoves) maxMoves = moves
        }
        return maxMoves
    }
}
```

## Dart

```dart
class Solution {
  int findMinMoves(List<int> machines) {
    int n = machines.length;
    int total = machines.fold(0, (a, b) => a + b);
    if (total % n != 0) return -1;
    int avg = total ~/ n;
    int moves = 0;
    int balance = 0; // cumulative imbalance
    for (int i = 0; i < n; i++) {
      int diff = machines[i] - avg;
      balance += diff;
      int cur = diff.abs() > balance.abs() ? diff.abs() : balance.abs();
      if (cur > moves) moves = cur;
    }
    return moves;
  }
}
```

## Golang

```go
func findMinMoves(machines []int) int {
    n := len(machines)
    sum := 0
    for _, v := range machines {
        sum += v
    }
    if sum%n != 0 {
        return -1
    }
    avg := sum / n
    ans, cum := 0, 0
    for _, v := range machines {
        diff := v - avg
        cum += diff
        cur := max(abs(cum), diff)
        if cur > ans {
            ans = cur
        }
    }
    return ans
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## Ruby

```ruby
def find_min_moves(machines)
  n = machines.length
  total = machines.sum
  return -1 if total % n != 0
  avg = total / n
  left_sum = 0
  ans = 0
  machines.each_with_index do |m, i|
    left_excess = left_sum - i * avg
    right_excess = (total - left_sum - m) - (n - i - 1) * avg
    cur = [left_excess.abs, right_excess.abs].max
    cur = [cur, m - avg].max
    ans = [ans, cur].max
    left_sum += m
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findMinMoves(machines: Array[Int]): Int = {
        val n = machines.length
        var total: Long = 0L
        for (v <- machines) total += v
        if (total % n != 0) return -1
        val avg = total / n
        var ans: Long = 0L
        var prefix: Long = 0L
        for (vInt <- machines) {
            val diff = vInt.toLong - avg
            prefix += diff
            val cur = math.max(math.abs(prefix), diff)
            if (cur > ans) ans = cur
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_min_moves(machines: Vec<i32>) -> i32 {
        let n = machines.len() as i64;
        let sum: i64 = machines.iter().map(|&x| x as i64).sum();
        if sum % n != 0 {
            return -1;
        }
        let avg = sum / n;
        let mut balance: i64 = 0;
        let mut ans: i64 = 0;
        for &m in machines.iter() {
            let net = m as i64 - avg;
            balance += net;
            ans = ans.max(balance.abs()).max(net);
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (find-min-moves machines)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length machines))
         (total (foldl + 0 machines)))
    (if (not (= (remainder total n) 0))
        -1
        (let ((avg (quotient total n)))
          (let loop ((lst machines) (left 0) (ans 0))
            (if (null? lst)
                ans
                (let* ((m (car lst))
                       (diff (- m avg))
                       (new-left (+ left diff))
                       (candidate (max (abs new-left) diff)))
                  (loop (cdr lst) new-left (max ans candidate)))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_min_moves/1]).

-spec find_min_moves(Machines :: [integer()]) -> integer().
find_min_moves(Machines) ->
    N = length(Machines),
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Machines),
    case Sum rem N of
        0 ->
            Avg = Sum div N,
            loop(Machines, Avg, 0, 0);
        _ ->
            -1
    end.

loop([], _Avg, _Cum, Ans) ->
    Ans;
loop([M|Rest], Avg, Cum, Ans) ->
    Diff = M - Avg,
    NewCum = Cum + Diff,
    MovesNeeded = erlang:max(erlang:abs(NewCum), Diff),
    NewAns = erlang:max(Ans, MovesNeeded),
    loop(Rest, Avg, NewCum, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min_moves(machines :: [integer]) :: integer
  def find_min_moves(machines) do
    total = Enum.sum(machines)
    n = length(machines)

    if rem(total, n) != 0 do
      -1
    else
      avg = div(total, n)

      {ans, _} =
        Enum.reduce(machines, {0, 0}, fn m, {ans, left} ->
          new_left = left + m - avg
          cur = max(abs(new_left), m - avg)
          {max(ans, cur), new_left}
        end)

      ans
    end
  end
end
```
