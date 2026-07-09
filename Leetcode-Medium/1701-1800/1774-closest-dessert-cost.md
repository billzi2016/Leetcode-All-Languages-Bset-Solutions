# 1774. Closest Dessert Cost

## Cpp

```cpp
class Solution {
public:
    void dfs(int idx, int cur, const vector<int>& toppingCosts, int target, int& best) {
        int diffCur = abs(cur - target);
        int diffBest = abs(best - target);
        if (diffCur < diffBest || (diffCur == diffBest && cur < best)) {
            best = cur;
        }
        if (idx == (int)toppingCosts.size()) return;
        dfs(idx + 1, cur, toppingCosts, target, best);                         // 0 of this topping
        dfs(idx + 1, cur + toppingCosts[idx], toppingCosts, target, best);     // 1 of this topping
        dfs(idx + 1, cur + 2 * toppingCosts[idx], toppingCosts, target, best); // 2 of this topping
    }
    
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        int best = baseCosts[0];
        for (int b : baseCosts) {
            dfs(0, b, toppingCosts, target, best);
        }
        return best;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int closestCost(int[] baseCosts, int[] toppingCosts, int target) {
        List<Integer> toppingSums = new ArrayList<>();
        dfs(0, 0, toppingCosts, toppingSums);
        int bestDiff = Integer.MAX_VALUE;
        int answer = 0;
        for (int base : baseCosts) {
            for (int tSum : toppingSums) {
                int total = base + tSum;
                int diff = Math.abs(total - target);
                if (diff < bestDiff || (diff == bestDiff && total < answer)) {
                    bestDiff = diff;
                    answer = total;
                }
            }
        }
        return answer;
    }

    private void dfs(int idx, int cur, int[] toppingCosts, List<Integer> list) {
        if (idx == toppingCosts.length) {
            list.add(cur);
            return;
        }
        // Use 0 of this topping
        dfs(idx + 1, cur, toppingCosts, list);
        // Use 1 of this topping
        dfs(idx + 1, cur + toppingCosts[idx], toppingCosts, list);
        // Use 2 of this topping
        dfs(idx + 1, cur + 2 * toppingCosts[idx], toppingCosts, list);
    }
}
```

## Python

```python
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        possible = set()
        m = len(toppingCosts)

        def dfs(i, cur):
            if i == m:
                possible.add(cur)
                return
            # use 0 of this topping
            dfs(i + 1, cur)
            # use 1 of this topping
            dfs(i + 1, cur + toppingCosts[i])
            # use 2 of this topping
            dfs(i + 1, cur + 2 * toppingCosts[i])

        dfs(0, 0)

        best = None
        minDiff = float('inf')
        for base in baseCosts:
            for add in possible:
                total = base + add
                diff = abs(total - target)
                if diff < minDiff or (diff == minDiff and total < best):
                    minDiff = diff
                    best = total
        return best
```

## Python3

```python
class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        from math import inf

        # Generate all possible sums of toppings (each can be used 0,1,2 times)
        topping_sums = []

        def dfs(idx, cur):
            if idx == len(toppingCosts):
                topping_sums.append(cur)
                return
            cost = toppingCosts[idx]
            dfs(idx + 1, cur)                     # 0 of this topping
            dfs(idx + 1, cur + cost)              # 1 of this topping
            dfs(idx + 1, cur + 2 * cost)          # 2 of this topping

        dfs(0, 0)

        best_cost = None
        best_diff = inf

        for base in baseCosts:
            for t_sum in topping_sums:
                total = base + t_sum
                diff = abs(total - target)
                if diff < best_diff or (diff == best_diff and total < best_cost):
                    best_diff = diff
                    best_cost = total

        return best_cost
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int g_target;
static int g_best;

static void updateBest(int sum) {
    int diff = abs(sum - g_target);
    int bestDiff = abs(g_best - g_target);
    if (diff < bestDiff || (diff == bestDiff && sum < g_best)) {
        g_best = sum;
    }
}

static void dfs(int idx, int cur, int *toppingCosts, int toppingSize) {
    if (idx == toppingSize) {
        updateBest(cur);
        return;
    }
    dfs(idx + 1, cur, toppingCosts, toppingSize);                                 // 0 of this topping
    dfs(idx + 1, cur + toppingCosts[idx], toppingCosts, toppingSize);             // 1 of this topping
    dfs(idx + 1, cur + 2 * toppingCosts[idx], toppingCosts, toppingSize);         // 2 of this topping
}

int closestCost(int* baseCosts, int baseCostsSize, int* toppingCosts, int toppingCostsSize, int target) {
    g_target = target;
    g_best = INT_MAX;
    for (int i = 0; i < baseCostsSize; ++i) {
        dfs(0, baseCosts[i], toppingCosts, toppingCostsSize);
    }
    return g_best;
}
```

## Csharp

```csharp
public class Solution
{
    public int ClosestCost(int[] baseCosts, int[] toppingCosts, int target)
    {
        var toppingSums = new HashSet<int>();
        void Dfs(int idx, int sum)
        {
            if (idx == toppingCosts.Length)
            {
                toppingSums.Add(sum);
                return;
            }
            Dfs(idx + 1, sum); // 0 of this topping
            Dfs(idx + 1, sum + toppingCosts[idx]); // 1 of this topping
            Dfs(idx + 1, sum + 2 * toppingCosts[idx]); // 2 of this topping
        }

        Dfs(0, 0);

        int best = int.MaxValue;
        int bestDiff = int.MaxValue;

        foreach (int baseCost in baseCosts)
        {
            foreach (int tSum in toppingSums)
            {
                int total = baseCost + tSum;
                int diff = Math.Abs(total - target);
                if (diff < bestDiff || (diff == bestDiff && total < best))
                {
                    bestDiff = diff;
                    best = total;
                }
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} baseCosts
 * @param {number[]} toppingCosts
 * @param {number} target
 * @return {number}
 */
var closestCost = function(baseCosts, toppingCosts, target) {
    const toppingSums = [];
    const m = toppingCosts.length;
    const dfs = (i, sum) => {
        if (i === m) {
            toppingSums.push(sum);
            return;
        }
        dfs(i + 1, sum);                                 // 0 of this topping
        dfs(i + 1, sum + toppingCosts[i]);               // 1 of this topping
        dfs(i + 1, sum + 2 * toppingCosts[i]);           // 2 of this topping
    };
    dfs(0, 0);
    
    let bestCost = Infinity;
    let bestDiff = Infinity;
    
    for (const base of baseCosts) {
        for (const add of toppingSums) {
            const total = base + add;
            const diff = Math.abs(total - target);
            if (diff < bestDiff || (diff === bestDiff && total < bestCost)) {
                bestDiff = diff;
                bestCost = total;
            }
        }
    }
    
    return bestCost;
};
```

## Typescript

```typescript
function closestCost(baseCosts: number[], toppingCosts: number[], target: number): number {
    const m = toppingCosts.length;
    const toppingSums: number[] = [];

    function dfs(idx: number, cur: number) {
        if (idx === m) {
            toppingSums.push(cur);
            return;
        }
        // use 0,1,2 of current topping
        for (let cnt = 0; cnt <= 2; cnt++) {
            dfs(idx + 1, cur + cnt * toppingCosts[idx]);
        }
    }

    dfs(0, 0);

    let bestDiff = Infinity;
    let answer = 0;

    for (const base of baseCosts) {
        for (const tSum of toppingSums) {
            const total = base + tSum;
            const diff = Math.abs(total - target);
            if (diff < bestDiff || (diff === bestDiff && total < answer)) {
                bestDiff = diff;
                answer = total;
            }
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $baseCosts
     * @param Integer[] $toppingCosts
     * @param Integer $target
     * @return Integer
     */
    function closestCost($baseCosts, $toppingCosts, $target) {
        $possible = [];
        $m = count($toppingCosts);
        $dfs = function($idx, $curr) use (&$dfs, &$possible, $toppingCosts, $m) {
            if ($idx == $m) {
                $possible[] = $curr;
                return;
            }
            // 0 of this topping
            $dfs($idx + 1, $curr);
            // 1 of this topping
            $dfs($idx + 1, $curr + $toppingCosts[$idx]);
            // 2 of this topping
            $dfs($idx + 1, $curr + 2 * $toppingCosts[$idx]);
        };
        $dfs(0, 0);
        sort($possible);

        $bestDiff = PHP_INT_MAX;
        $answer = null;

        foreach ($baseCosts as $base) {
            foreach ($possible as $tSum) {
                $total = $base + $tSum;
                $diff = abs($total - $target);
                if ($diff < $bestDiff || ($diff == $bestDiff && $total < $answer)) {
                    $bestDiff = $diff;
                    $answer = $total;
                }
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func closestCost(_ baseCosts: [Int], _ toppingCosts: [Int], _ target: Int) -> Int {
        var toppingSums = [Int]()
        let m = toppingCosts.count
        func dfs(_ idx: Int, _ current: Int) {
            if idx == m {
                toppingSums.append(current)
                return
            }
            dfs(idx + 1, current)                              // 0 of this topping
            dfs(idx + 1, current + toppingCosts[idx])          // 1 of this topping
            dfs(idx + 1, current + 2 * toppingCosts[idx])      // 2 of this topping
        }
        dfs(0, 0)

        var bestDiff = Int.max
        var answer = 0

        for base in baseCosts {
            for sum in toppingSums {
                let total = base + sum
                let diff = abs(total - target)
                if diff < bestDiff || (diff == bestDiff && total < answer) {
                    bestDiff = diff
                    answer = total
                    if bestDiff == 0 { return target }
                }
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closestCost(baseCosts: IntArray, toppingCosts: IntArray, target: Int): Int {
        val possibleToppings = mutableSetOf<Int>()
        fun dfs(idx: Int, cur: Int) {
            if (idx == toppingCosts.size) {
                possibleToppings.add(cur)
                return
            }
            // 0 times
            dfs(idx + 1, cur)
            // 1 time
            dfs(idx + 1, cur + toppingCosts[idx])
            // 2 times
            dfs(idx + 1, cur + 2 * toppingCosts[idx])
        }
        dfs(0, 0)

        var best = Int.MAX_VALUE
        var bestDiff = Int.MAX_VALUE

        for (base in baseCosts) {
            for (tSum in possibleToppings) {
                val total = base + tSum
                val diff = kotlin.math.abs(total - target)
                if (diff < bestDiff || (diff == bestDiff && total < best)) {
                    bestDiff = diff
                    best = total
                }
            }
        }

        return best
    }
}
```

## Dart

```dart
class Solution {
  int closestCost(List<int> baseCosts, List<int> toppingCosts, int target) {
    Set<int> toppingSums = {};

    void dfs(int idx, int cur) {
      if (idx == toppingCosts.length) {
        toppingSums.add(cur);
        return;
      }
      for (int cnt = 0; cnt <= 2; ++cnt) {
        dfs(idx + 1, cur + cnt * toppingCosts[idx]);
      }
    }

    dfs(0, 0);

    int bestDiff = 1 << 30;
    int answer = 0;

    for (int base in baseCosts) {
      for (int tSum in toppingSums) {
        int total = base + tSum;
        int diff = (total - target).abs();
        if (diff < bestDiff || (diff == bestDiff && total < answer)) {
          bestDiff = diff;
          answer = total;
        }
      }
    }

    return answer;
  }
}
```

## Golang

```go
func closestCost(baseCosts []int, toppingCosts []int, target int) int {
    var sums []int
    m := len(toppingCosts)
    var dfs func(int, int)
    dfs = func(idx, cur int) {
        if idx == m {
            sums = append(sums, cur)
            return
        }
        for cnt := 0; cnt <= 2; cnt++ {
            dfs(idx+1, cur+cnt*toppingCosts[idx])
        }
    }
    dfs(0, 0)

    bestDiff := int(^uint(0) >> 1)
    ans := 0

    for _, base := range baseCosts {
        for _, s := range sums {
            total := base + s
            diff := total - target
            if diff < 0 {
                diff = -diff
            }
            if diff < bestDiff || (diff == bestDiff && total < ans) {
                bestDiff = diff
                ans = total
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def closest_cost(base_costs, topping_costs, target)
  topping_sums = [0]
  topping_costs.each do |c|
    current_size = topping_sums.size
    (0...current_size).each do |i|
      sum = topping_sums[i]
      topping_sums << sum + c
      topping_sums << sum + 2 * c
    end
  end

  best = nil
  min_diff = Float::INFINITY

  base_costs.each do |base|
    topping_sums.each do |t_sum|
      total = base + t_sum
      diff = (total - target).abs
      if diff < min_diff || (diff == min_diff && total < best)
        min_diff = diff
        best = total
      end
    end
  end

  best
end
```

## Scala

```scala
object Solution {
    def closestCost(baseCosts: Array[Int], toppingCosts: Array[Int], target: Int): Int = {
        val toppingSums = scala.collection.mutable.ArrayBuffer[Int]()

        def dfs(idx: Int, cur: Int): Unit = {
            if (idx == toppingCosts.length) {
                toppingSums += cur
                return
            }
            // use 0 of this topping
            dfs(idx + 1, cur)
            // use 1 of this topping
            dfs(idx + 1, cur + toppingCosts(idx))
            // use 2 of this topping
            dfs(idx + 1, cur + 2 * toppingCosts(idx))
        }

        dfs(0, 0)

        var best = Int.MaxValue

        def update(cost: Int): Unit = {
            val diff = math.abs(cost - target)
            if (best == Int.MaxValue) {
                best = cost
            } else {
                val bestDiff = math.abs(best - target)
                if (diff < bestDiff || (diff == bestDiff && cost < best)) {
                    best = cost
                }
            }
        }

        for (b <- baseCosts) {
            for (t <- toppingSums) {
                update(b + t)
            }
        }

        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn closest_cost(base_costs: Vec<i32>, topping_costs: Vec<i32>, target: i32) -> i32 {
        fn dfs(idx: usize, cur: i32, toppings: &Vec<i32>, sums: &mut Vec<i32>) {
            if idx == toppings.len() {
                sums.push(cur);
                return;
            }
            let cost = toppings[idx];
            dfs(idx + 1, cur, toppings, sums);               // use 0
            dfs(idx + 1, cur + cost, toppings, sums);        // use 1
            dfs(idx + 1, cur + 2 * cost, toppings, sums);    // use 2
        }

        let mut topping_sums = Vec::new();
        dfs(0, 0, &topping_costs, &mut topping_sums);

        let mut best = i32::MAX;
        let mut best_diff = i32::MAX;

        for &base in base_costs.iter() {
            for &tsum in topping_sums.iter() {
                let total = base + tsum;
                let diff = (total - target).abs();
                if diff < best_diff || (diff == best_diff && total < best) {
                    best_diff = diff;
                    best = total;
                }
            }
        }

        best
    }
}
```

## Racket

```racket
(define/contract (closest-cost baseCosts toppingCosts target)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (define (gen-topping-sums lst)
    (if (null? lst)
        '(0)
        (let* ((t (car lst))
               (rest (gen-topping-sums (cdr lst))))
          (append rest
                  (map (lambda (s) (+ s t)) rest)
                  (map (lambda (s) (+ s (* 2 t))) rest)))))
  (let* ((topping-sums (gen-topping-sums toppingCosts))
         (init-total (+ (car baseCosts) (car topping-sums)))
         (init-diff (abs (- init-total target))))
    (let loop ((bases baseCosts) (best-diff init-diff) (best-cost init-total))
      (if (null? bases)
          best-cost
          (let ((base (car bases)))
            (let inner ((tss topping-sums) (bd best-diff) (bc best-cost))
              (if (null? tss)
                  (loop (cdr bases) bd bc)
                  (let* ((total (+ base (car tss)))
                         (diff (abs (- total target))))
                    (cond
                      [(< diff bd) (inner (cdr tss) diff total)]
                      [(and (= diff bd) (< total bc)) (inner (cdr tss) diff total)]
                      [else (inner (cdr tss) bd bc)])))))))))
```

## Erlang

```erlang
-export([closest_cost/3]).
-spec closest_cost(BaseCosts :: [integer()], ToppingCosts :: [integer()], Target :: integer()) -> integer().
closest_cost(BaseCosts, ToppingCosts, Target) ->
    ToppingSums = gen_topping_sums(ToppingCosts),
    AllTotals = [Base + TS || Base <- BaseCosts, TS <- ToppingSums],
    lists:foldl(fun(Total, Acc) ->
        DiffAcc = erlang:abs(Target - Acc),
        DiffTot = erlang:abs(Target - Total),
        if
            DiffTot < DiffAcc -> Total;
            DiffTot == DiffAcc, Total < Acc -> Total;
            true -> Acc
        end
    end, hd(AllTotals), tl(AllTotals)).

gen_topping_sums(ToppingCosts) ->
    lists:foldl(fun(Cost, Acc) ->
        New = [S + Cost || S <- Acc] ++ [S + 2*Cost || S <- Acc],
        Acc ++ New
    end, [0], ToppingCosts).
```

## Elixir

```elixir
defmodule Solution do
  @spec closest_cost(base_costs :: [integer], topping_costs :: [integer], target :: integer) :: integer
  def closest_cost(base_costs, topping_costs, target) do
    topping_sums = gen_topping_sums(topping_costs, 0, [])
    totals = for b <- base_costs, s <- topping_sums, do: b + s

    Enum.min_by(totals, fn total -> {abs(total - target), total} end)
  end

  defp gen_topping_sums([], current, acc) do
    [current | acc]
  end

  defp gen_topping_sums([cost | rest], current, acc) do
    # use topping 0 times
    acc0 = gen_topping_sums(rest, current, acc)
    # use topping 1 time
    acc1 = gen_topping_sums(rest, current + cost, acc0)
    # use topping 2 times
    gen_topping_sums(rest, current + 2 * cost, acc1)
  end
end
```
