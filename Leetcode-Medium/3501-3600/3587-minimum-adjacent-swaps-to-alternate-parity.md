# 3587. Minimum Adjacent Swaps to Alternate Parity

## Cpp

```cpp
class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        vector<int> evenIdx;
        for (int i = 0; i < n; ++i) {
            if ((nums[i] & 1) == 0) evenIdx.push_back(i);
        }
        int evenCnt = evenIdx.size();
        int oddCnt = n - evenCnt;
        if (abs(evenCnt - oddCnt) > 1) return -1;

        auto costForStart = [&](int startParity) -> long long {
            vector<int> targetEvenIdx;
            targetEvenIdx.reserve(evenCnt);
            for (int i = 0; i < n; ++i) {
                int expectedParity = (startParity + i) % 2; // 0 -> even, 1 -> odd
                if (expectedParity == 0) targetEvenIdx.push_back(i);
            }
            long long cost = 0;
            for (size_t k = 0; k < evenIdx.size(); ++k) {
                cost += llabs((long long)evenIdx[k] - targetEvenIdx[k]);
            }
            return cost;
        };

        long long ans = LLONG_MAX;
        if (n % 2 == 0) {
            ans = min(costForStart(0), costForStart(1));
        } else {
            if (evenCnt > oddCnt) ans = costForStart(0);
            else ans = costForStart(1);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        int evenCount = 0;
        for (int num : nums) {
            if ((num & 1) == 0) evenCount++;
        }
        int oddCount = n - evenCount;
        if (Math.abs(evenCount - oddCount) > 1) return -1;

        // collect positions of even numbers
        int[] evenPos = new int[evenCount];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if ((nums[i] & 1) == 0) {
                evenPos[idx++] = i;
            }
        }

        long answer = Long.MAX_VALUE;

        // pattern: even at index 0
        if (evenCount >= oddCount) { // feasible when evens occupy ceil(n/2) spots
            long cost = 0;
            int targetIdx = 0; // first even position
            for (int i = 0; i < evenCount; i++) {
                cost += Math.abs(evenPos[i] - targetIdx);
                targetIdx += 2;
            }
            answer = Math.min(answer, cost);
        }

        // pattern: odd at index 0 (even positions start from 1)
        if (oddCount >= evenCount) { // feasible when evens occupy floor(n/2) spots
            long cost = 0;
            int targetIdx = 1; // first even position in this pattern
            for (int i = 0; i < evenCount; i++) {
                cost += Math.abs(evenPos[i] - targetIdx);
                targetIdx += 2;
            }
            answer = Math.min(answer, cost);
        }

        return (int) answer;
    }
}
```

## Python

```python
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        even_indices = [i for i, x in enumerate(nums) if x % 2 == 0]
        odd_cnt = n - len(even_indices)
        even_cnt = len(even_indices)

        if abs(even_cnt - odd_cnt) > 1:
            return -1

        def cost(start_even):
            # positions where evens should be placed
            target = list(range(0, n, 2)) if start_even else list(range(1, n, 2))
            if len(target) != even_cnt:
                return float('inf')
            return sum(abs(c - t) for c, t in zip(even_indices, target))

        if n % 2 == 1:
            # majority parity must start first
            if even_cnt > odd_cnt:
                return cost(True)
            else:
                return cost(False)
        else:
            return int(min(cost(True), cost(False)))
```

## Python3

```python
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        even_idx = [i for i, x in enumerate(nums) if x % 2 == 0]
        even_cnt = len(even_idx)
        odd_cnt = n - even_cnt

        if abs(even_cnt - odd_cnt) > 1:
            return -1

        def cost(start_even: bool) -> int:
            # positions where an even number should be placed
            target = [i for i in range(n) if (i % 2 == 0) == start_even]
            total = 0
            for cur, tar in zip(even_idx, target):
                total += abs(cur - tar)
            return total

        if n % 2 == 0:
            return min(cost(True), cost(False))
        else:
            # the parity with more elements must start first
            if even_cnt > odd_cnt:
                return cost(True)
            else:
                return cost(False)
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minSwaps(int* nums, int numsSize) {
    int n = numsSize;
    int evenCnt = 0;
    for (int i = 0; i < n; ++i) {
        if ((nums[i] & 1) == 0) ++evenCnt;
    }
    int oddCnt = n - evenCnt;
    if (abs(evenCnt - oddCnt) > 1) return -1;

    int *evenPos = (int *)malloc(evenCnt * sizeof(int));
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        if ((nums[i] & 1) == 0) evenPos[idx++] = i;
    }

    long long best = LLONG_MAX;

    for (int startParity = 0; startParity <= 1; ++startParity) {
        int slotsEven = (n + (startParity == 0)) / 2;
        if (evenCnt != slotsEven) continue;

        long long cost = 0;
        for (int k = 0; k < evenCnt; ++k) {
            int targetIdx = startParity + 2 * k;
            cost += llabs((long long)evenPos[k] - targetIdx);
        }
        if (cost < best) best = cost;
    }

    free(evenPos);

    return (best == LLONG_MAX) ? -1 : (int)best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinSwaps(int[] nums) {
        int n = nums.Length;
        List<int> evenIdx = new List<int>();
        for (int i = 0; i < n; i++) {
            if ((nums[i] & 1) == 0) evenIdx.Add(i);
        }
        int evenCnt = evenIdx.Count;
        int oddCnt = n - evenCnt;

        if (Math.Abs(evenCnt - oddCnt) > 1) return -1;

        long answer = long.MaxValue;

        // Pattern starting with even at index 0
        if (evenCnt >= oddCnt) {
            long cost = ComputeCost(evenIdx, startEven: true);
            answer = Math.Min(answer, cost);
        }

        // Pattern starting with odd at index 0
        if (oddCnt >= evenCnt) {
            long cost = ComputeCost(evenIdx, startEven: false);
            answer = Math.Min(answer, cost);
        }

        return (int)answer;
    }

    private long ComputeCost(List<int> evenIndices, bool startEven) {
        long cost = 0;
        for (int k = 0; k < evenIndices.Count; k++) {
            int target = startEven ? 2 * k : 2 * k + 1;
            cost += Math.Abs(evenIndices[k] - target);
        }
        return cost;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minSwaps = function(nums) {
    const n = nums.length;
    const evIdx = [];
    let evenCnt = 0, oddCnt = 0;
    for (let i = 0; i < n; i++) {
        if ((nums[i] & 1) === 0) {
            evenCnt++;
            evIdx.push(i);
        } else {
            oddCnt++;
        }
    }
    if (Math.abs(evenCnt - oddCnt) > 1) return -1;

    const computeCost = (startParity) => {
        // startParity: 0 -> even at index 0, 1 -> odd at index 0
        const targetEvenIdx = [];
        for (let i = 0; i < n; i++) {
            const expectedParity = (i + startParity) % 2; // 0 for even, 1 for odd
            if (expectedParity === 0) targetEvenIdx.push(i);
        }
        let cost = 0;
        for (let k = 0; k < evIdx.length; k++) {
            cost += Math.abs(evIdx[k] - targetEvenIdx[k]);
        }
        return cost;
    };

    if (n % 2 === 1) {
        // majority parity must start first
        const startParity = evenCnt > oddCnt ? 0 : 1;
        return computeCost(startParity);
    } else {
        // both patterns possible, take min
        const costEvenStart = computeCost(0);
        const costOddStart = computeCost(1);
        return Math.min(costEvenStart, costOddStart);
    }
};
```

## Typescript

```typescript
function minSwaps(nums: number[]): number {
    const n = nums.length;
    const evenIdx: number[] = [];
    for (let i = 0; i < n; i++) {
        if (nums[i] % 2 === 0) evenIdx.push(i);
    }
    const eCnt = evenIdx.length;
    const oCnt = n - eCnt;

    if (Math.abs(eCnt - oCnt) > 1) return -1;

    const computeCost = (startEven: boolean): number => {
        const targets: number[] = [];
        for (let i = startEven ? 0 : 1; i < n; i += 2) {
            targets.push(i);
        }
        let cost = 0;
        for (let k = 0; k < targets.length; k++) {
            cost += Math.abs(evenIdx[k] - targets[k]);
        }
        return cost;
    };

    if (n % 2 === 1) {
        // Majority parity must start first
        if (eCnt > oCnt) return computeCost(true);
        else return computeCost(false);
    } else {
        const costEvenStart = computeCost(true);
        const costOddStart = computeCost(false);
        return Math.min(costEvenStart, costOddStart);
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minSwaps($nums) {
        $n = count($nums);
        $evenPos = [];
        foreach ($nums as $i => $val) {
            if (($val & 1) === 0) { // even
                $evenPos[] = $i;
            }
        }
        $evenCnt = count($evenPos);
        $oddCnt = $n - $evenCnt;

        if (abs($evenCnt - $oddCnt) > 1) {
            return -1;
        }

        $calcCost = function(array $positions, int $startParity) use ($n): int {
            $cost = 0;
            $targetIdx = $startParity; // first index where an even should be placed
            foreach ($positions as $pos) {
                $cost += abs($pos - $targetIdx);
                $targetIdx += 2;
            }
            return $cost;
        };

        if ($n % 2 === 0) {
            $costEvenStart = $calcCost($evenPos, 0); // even at index 0
            $costOddStart  = $calcCost($evenPos, 1); // odd at index 0 (evens at odd indices)
            return min($costEvenStart, $costOddStart);
        } else {
            if ($evenCnt > $oddCnt) {
                // must start with even
                return $calcCost($evenPos, 0);
            } else {
                // must start with odd
                return $calcCost($evenPos, 1);
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func minSwaps(_ nums: [Int]) -> Int {
        let n = nums.count
        var evenCount = 0
        for v in nums {
            if v % 2 == 0 { evenCount += 1 }
        }
        let oddCount = n - evenCount
        if abs(evenCount - oddCount) > 1 {
            return -1
        }
        
        func cost(startEven: Bool) -> Int? {
            var currentEvenIdx = [Int]()
            for (i, v) in nums.enumerated() {
                if v % 2 == 0 { currentEvenIdx.append(i) }
            }
            var targetEvenIdx = [Int]()
            for i in 0..<n {
                let needEven = startEven ? (i % 2 == 0) : (i % 2 == 1)
                if needEven { targetEvenIdx.append(i) }
            }
            if currentEvenIdx.count != targetEvenIdx.count { return nil }
            var total: Int64 = 0
            for i in 0..<currentEvenIdx.count {
                total += Int64(abs(currentEvenIdx[i] - targetEvenIdx[i]))
            }
            return Int(total)
        }
        
        if n % 2 == 1 {
            let startEven = evenCount > oddCount
            return cost(startEven: startEven) ?? -1
        } else {
            var answer = Int.max
            if let c1 = cost(startEven: true) { answer = min(answer, c1) }
            if let c2 = cost(startEven: false) { answer = min(answer, c2) }
            return answer == Int.max ? -1 : answer
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwaps(nums: IntArray): Int {
        val n = nums.size
        var evenCount = 0
        for (v in nums) if (v % 2 == 0) evenCount++
        val oddCount = n - evenCount
        if (kotlin.math.abs(evenCount - oddCount) > 1) return -1

        fun computeCost(startEven: Boolean): Long {
            // indices where an even number should be placed according to the pattern
            val target = ArrayList<Int>()
            for (i in 0 until n) {
                val expectEven = if (startEven) i % 2 == 0 else i % 2 == 1
                if (expectEven) target.add(i)
            }
            // current indices of even numbers
            val cur = ArrayList<Int>()
            for (i in 0 until n) {
                if (nums[i] % 2 == 0) cur.add(i)
            }
            var sum = 0L
            for (idx in cur.indices) {
                sum += kotlin.math.abs(cur[idx] - target[idx]).toLong()
            }
            return sum
        }

        val costs = mutableListOf<Long>()
        if (n % 2 == 0) {
            costs.add(computeCost(true))
            costs.add(computeCost(false))
        } else {
            // majority parity must start first
            if (evenCount > oddCount) costs.add(computeCost(true)) else costs.add(computeCost(false))
        }
        val minCost = costs.minOrNull() ?: 0L
        return minCost.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minSwaps(List<int> nums) {
    int n = nums.length;
    int evenCnt = 0, oddCnt = 0;
    List<int> evenPos = [];
    for (int i = 0; i < n; ++i) {
      if (nums[i] % 2 == 0) {
        evenCnt++;
        evenPos.add(i);
      } else {
        oddCnt++;
      }
    }

    if ((evenCnt - oddCnt).abs() > 1) return -1;

    int computeCost(int startParity) {
      int idx = 0;
      int cost = 0;
      for (int i = 0; i < n; ++i) {
        // positions where an even number should be placed
        if ((startParity + i) % 2 == 0) {
          cost += (evenPos[idx] - i).abs();
          idx++;
        }
      }
      return cost;
    }

    int ans = 1 << 60; // sufficiently large

    if (evenCnt >= oddCnt) {
      ans = computeCost(0); // even at index 0
    }
    if (oddCnt >= evenCnt) {
      int alt = computeCost(1); // odd at index 0, so evens at odd indices
      if (alt < ans) ans = alt;
    }

    return ans;
  }
}
```

## Golang

```go
func minSwaps(nums []int) int {
    n := len(nums)
    evenIdx := make([]int, 0)
    for i, v := range nums {
        if v%2 == 0 {
            evenIdx = append(evenIdx, i)
        }
    }
    evenCnt := len(evenIdx)
    oddCnt := n - evenCnt
    if abs(evenCnt-oddCnt) > 1 {
        return -1
    }

    const INF int64 = 1 << 60
    ans := INF

    compute := func(startEven bool) int64 {
        target := make([]int, 0)
        for i := 0; i < n; i++ {
            if (i%2 == 0 && startEven) || (i%2 == 1 && !startEven) {
                target = append(target, i)
            }
        }
        if len(target) != evenCnt {
            return INF
        }
        var cost int64 = 0
        for k := 0; k < evenCnt; k++ {
            diff := evenIdx[k] - target[k]
            if diff < 0 {
                diff = -diff
            }
            cost += int64(diff)
        }
        return cost
    }

    if n%2 == 0 || evenCnt > oddCnt {
        ans = minInt64(ans, compute(true))
    }
    if n%2 == 0 || oddCnt > evenCnt {
        ans = minInt64(ans, compute(false))
    }

    if ans == INF {
        return -1
    }
    return int(ans)
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}

func minInt64(a, b int64) int64 {
    if a < b {
        return a
    }
    return b
}
```

## Ruby

```ruby
def min_swaps(nums)
  n = nums.length
  evens = []
  odds = []
  nums.each_with_index do |v, i|
    if v.even?
      evens << i
    else
      odds << i
    end
  end

  even_cnt = evens.size
  odd_cnt = odds.size
  return -1 if (even_cnt - odd_cnt).abs > 1

  compute_cost = ->(target_even) do
    cost = 0
    evens.each_with_index do |pos, idx|
      cost += (pos - target_even[idx]).abs
    end
    cost
  end

  ans = Float::INFINITY

  if n.even?
    # both patterns possible when counts are equal (guaranteed here)
    target1 = (0...n).step(2).to_a
    target2 = (1...n).step(2).to_a
    ans = [compute_cost.call(target1), compute_cost.call(target2)].min
  else
    if even_cnt > odd_cnt
      target = (0...n).step(2).to_a
    else
      target = (1...n).step(2).to_a
    end
    ans = compute_cost.call(target)
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
    def minSwaps(nums: Array[Int]): Int = {
        val n = nums.length
        var evenCnt = 0
        for (v <- nums) if ((v & 1) == 0) evenCnt += 1
        val oddCnt = n - evenCnt
        if (math.abs(evenCnt - oddCnt) > 1) return -1

        // indices of even numbers in original array
        val evenIdx = new scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- nums.indices) {
            if ((nums(i) & 1) == 0) evenIdx += i
        }

        def cost(startEven: Boolean): Long = {
            var total: Long = 0L
            var k = 0
            while (k < evenIdx.length) {
                val targetPos = if (startEven) 2 * k else 2 * k + 1
                total += math.abs(evenIdx(k) - targetPos)
                k += 1
            }
            total
        }

        if (n % 2 == 1) {
            // the parity with more count must start first
            if (evenCnt > oddCnt) cost(true).toInt else cost(false).toInt
        } else {
            val c1 = cost(true)
            val c2 = cost(false)
            math.min(c1, c2).toInt
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut even_pos = Vec::new();
        let mut odd_pos = Vec::new();

        for (i, &v) in nums.iter().enumerate() {
            if v % 2 == 0 {
                even_pos.push(i);
            } else {
                odd_pos.push(i);
            }
        }

        let even_cnt = even_pos.len();
        let odd_cnt = odd_pos.len();

        if (even_cnt as i32 - odd_cnt as i32).abs() > 1 {
            return -1;
        }

        fn cost(pos: &Vec<usize>) -> i64 {
            let mut total: i64 = 0;
            for (i, &p) in pos.iter().enumerate() {
                let target = 2 * i;
                total += ((p as i64) - (target as i64)).abs();
            }
            total
        }

        let mut ans: i64 = i64::MAX;

        if n % 2 == 0 {
            // both starting patterns are possible
            ans = ans.min(cost(&even_pos));
            ans = ans.min(cost(&odd_pos));
        } else {
            if even_cnt > odd_cnt {
                ans = cost(&even_pos);
            } else {
                ans = cost(&odd_pos);
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-swaps nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (even-idx
          (for/list ([i (in-range n)] [v (in-list nums)]
                     #:when (even? v)) i))
         (odd-idx
          (for/list ([i (in-range n)] [v (in-list nums)]
                     #:when (odd? v)) i))
         (evenCnt (length even-idx))
         (oddCnt (length odd-idx)))
    (if (> (abs (- evenCnt oddCnt)) 1)
        -1
        (letrec ((cost
                  (lambda (start)
                    (let* ((target-even
                            (for/list ([i (in-range n)]
                                       #:when (= (modulo (+ start i) 2) 0))
                              i)))
                      (if (= (length target-even) evenCnt)
                          (apply + (map (lambda (a b) (abs (- a b))) even-idx target-even))
                          +inf.0)))))
          (let ((candidates
                 (filter (lambda (v) (not (= v +inf.0)))
                         (if (even? n)
                             (list (cost 0) (cost 1))
                             (let ((start (if (> evenCnt oddCnt) 0 1)))
                               (list (cost start)))))))
            (if (null? candidates)
                -1
                (apply min candidates)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_swaps/1]).

-spec min_swaps(Nums :: [integer()]) -> integer().
min_swaps(Nums) ->
    N = length(Nums),
    Indexed = lists:zip(Nums, lists:seq(0, N - 1)),
    EvenIdx = [Idx || {Num, Idx} <- Indexed, Num rem 2 == 0],
    EvenCnt = length(EvenIdx),
    OddCnt = N - EvenCnt,
    case erlang:abs(EvenCnt - OddCnt) > 1 of
        true -> -1;
        false ->
            Costs = compute_cost(N, EvenIdx, EvenCnt, 0) ++
                    compute_cost(N, EvenIdx, EvenCnt, 1),
            case Costs of
                [] -> -1;
                _  -> lists:min(Costs)
            end
    end.

-spec compute_cost(integer(), [integer()], integer(), integer()) -> [integer()].
compute_cost(N, EvenIdx, EvenCnt, StartParity) ->
    NeededEven = if StartParity == 0 -> (N + 1) div 2; true -> N div 2 end,
    case EvenCnt == NeededEven of
        true ->
            TargetIdx = lists:seq(StartParity, N - 1, 2),
            [lists:foldl(
                fun({Cur, Tgt}, Acc) -> Acc + erlang:abs(Cur - Tgt) end,
                0,
                lists:zip(EvenIdx, TargetIdx)
              )];
        false -> []
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swaps(nums :: [integer]) :: integer
  def min_swaps(nums) do
    n = length(nums)

    {even_cnt, odd_cnt} =
      Enum.reduce(nums, {0, 0}, fn x, {e, o} ->
        if rem(x, 2) == 0, do: {e + 1, o}, else: {e, o + 1}
      end)

    if abs(even_cnt - odd_cnt) > 1 do
      -1
    else
      even_positions =
        nums
        |> Enum.with_index()
        |> Enum.filter(fn {val, _idx} -> rem(val, 2) == 0 end)
        |> Enum.map(fn {_val, idx} -> idx end)

      cost = fn start_parity ->
        target_positions = for i <- 0..(even_cnt - 1), do: start_parity + i * 2

        Enum.zip(even_positions, target_positions)
        |> Enum.reduce(0, fn {cur, tgt}, acc -> acc + abs(cur - tgt) end)
      end

      if rem(n, 2) == 1 do
        if even_cnt > odd_cnt, do: cost.(0), else: cost.(1)
      else
        min(cost.(0), cost.(1))
      end
    end
  end
end
```
