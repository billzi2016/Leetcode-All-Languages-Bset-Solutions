# 2673. Make Costs of Paths Equal in a Binary Tree

## Cpp

```cpp
class Solution {
public:
    int minIncrements(int n, vector<int>& cost) {
        vector<long long> maxSum(n + 2, 0);
        long long ans = 0;
        for (int i = n; i >= 1; --i) {
            if (2 * i > n) { // leaf
                maxSum[i] = cost[i - 1];
            } else {
                long long left = maxSum[2 * i];
                long long right = maxSum[2 * i + 1];
                ans += llabs(left - right);
                maxSum[i] = (long long)cost[i - 1] + max(left, right);
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minIncrements(int n, int[] cost) {
        long[] result = dfs(1, n, cost);
        return (int) result[1];
    }

    private long[] dfs(int idx, int n, int[] cost) {
        // If node is a leaf
        if (idx * 2 > n) {
            return new long[]{cost[idx - 1], 0L};
        }
        long[] left = dfs(idx * 2, n, cost);
        long[] right = dfs(idx * 2 + 1, n, cost);

        long diff = Math.abs(left[0] - right[0]);
        long inc = left[1] + right[1] + diff;
        long maxChild = Math.max(left[0], right[0]);
        long maxSum = cost[idx - 1] + maxChild;

        return new long[]{maxSum, inc};
    }
}
```

## Python

```python
class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(1 << 20)

        def dfs(i):
            left = i * 2
            if left > n:  # leaf node
                return cost[i - 1], 0
            right = left + 1
            lmax, linc = dfs(left)
            rmax, rinc = dfs(right)
            diff = abs(lmax - rmax)
            total_inc = linc + rinc + diff
            max_sum = cost[i - 1] + max(lmax, rmax)
            return max_sum, total_inc

        _, ans = dfs(1)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        dp = [0] * (n + 1)      # max path sum from node to leaf after adjustments
        inc = [0] * (n + 1)     # total increments needed in subtree

        # leaves
        for i in range(n // 2 + 1, n + 1):
            dp[i] = cost[i - 1]

        # internal nodes bottom‑up
        for i in range(n // 2, 0, -1):
            left = 2 * i
            right = left + 1
            diff = abs(dp[left] - dp[right])
            inc[i] = inc[left] + inc[right] + diff
            dp[i] = cost[i - 1] + max(dp[left], dp[right])

        return inc[1]
```

## C

```c
#include <stdlib.h>
#include <math.h>

typedef struct {
    long long inc;
    long long maxSum;
} Pair;

static int N;
static int *COST;

static Pair dfs(int idx) {
    int left = idx << 1;
    if (left > N) { // leaf
        return (Pair){0, COST[idx - 1]};
    }
    Pair L = dfs(left);
    Pair R = dfs(left + 1);
    long long inc = L.inc + R.inc + llabs(L.maxSum - R.maxSum);
    long long maxSum = COST[idx - 1] + (L.maxSum > R.maxSum ? L.maxSum : R.maxSum);
    return (Pair){inc, maxSum};
}

int minIncrements(int n, int* cost, int costSize) {
    N = n;
    COST = cost;
    Pair res = dfs(1);
    return (int)res.inc;
}
```

## Csharp

```csharp
public class Solution {
    public int MinIncrements(int n, int[] cost) {
        long total = 0;
        long[] maxSum = new long[n + 2]; // 1-indexed array

        for (int i = n; i >= 1; --i) {
            if (2 * i > n) { // leaf node
                maxSum[i] = cost[i - 1];
            } else {
                long left = maxSum[2 * i];
                long right = maxSum[2 * i + 1];
                total += System.Math.Abs(left - right);
                maxSum[i] = cost[i - 1] + System.Math.Max(left, right);
            }
        }

        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} cost
 * @return {number}
 */
var minIncrements = function(n, cost) {
    const maxSum = new Array(n + 1);
    let increments = 0;
    for (let i = n; i >= 1; --i) {
        if (2 * i > n) { // leaf node
            maxSum[i] = cost[i - 1];
        } else {
            const left = 2 * i;
            const right = 2 * i + 1;
            const diff = Math.abs(maxSum[left] - maxSum[right]);
            increments += diff;
            maxSum[i] = cost[i - 1] + Math.max(maxSum[left], maxSum[right]);
        }
    }
    return increments;
};
```

## Typescript

```typescript
function minIncrements(n: number, cost: number[]): number {
    const dfs = (i: number): [number, number] => {
        const idx = i - 1;
        // leaf node
        if (i * 2 > n) {
            return [cost[idx], 0];
        }
        const [leftSum, leftInc] = dfs(i * 2);
        const [rightSum, rightInc] = dfs(i * 2 + 1);
        const diff = Math.abs(leftSum - rightSum);
        const totalInc = leftInc + rightInc + diff;
        const curSum = cost[idx] + Math.max(leftSum, rightSum);
        return [curSum, totalInc];
    };
    return dfs(1)[1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $cost
     * @return Integer
     */
    function minIncrements($n, $cost) {
        // cumulative cost from root to each node (1-indexed)
        $cum = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            if ($i == 1) {
                $cum[$i] = $cost[0];
            } else {
                $parent = intdiv($i, 2);
                $cum[$i] = $cost[$i - 1] + $cum[$parent];
            }
        }

        // leaves are nodes with index >= (n+1)/2
        $firstLeaf = intdiv($n + 1, 2);
        $maxSum = 0;
        for ($i = $firstLeaf; $i <= $n; $i++) {
            if ($cum[$i] > $maxSum) {
                $maxSum = $cum[$i];
            }
        }

        $increments = 0;
        for ($i = $firstLeaf; $i <= $n; $i++) {
            $increments += $maxSum - $cum[$i];
        }

        return $increments;
    }
}
```

## Swift

```swift
class Solution {
    func minIncrements(_ n: Int, _ cost: [Int]) -> Int {
        func dfs(_ idx: Int) -> (sum: Int, inc: Int64, leaves: Int) {
            if idx * 2 > n { // leaf node
                return (cost[idx - 1], 0, 1)
            }
            let left = dfs(idx * 2)
            let right = dfs(idx * 2 + 1)
            
            let maxChildSum = max(left.sum, right.sum)
            let deltaLeft = maxChildSum - left.sum
            let deltaRight = maxChildSum - right.sum
            
            let incBalance = Int64(deltaLeft) * Int64(left.leaves) +
                             Int64(deltaRight) * Int64(right.leaves)
            
            let totalInc = left.inc + right.inc + incBalance
            let uniformSum = cost[idx - 1] + maxChildSum
            let leafCount = left.leaves + right.leaves
            
            return (uniformSum, totalInc, leafCount)
        }
        
        let result = dfs(1).inc
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minIncrements(n: Int, cost: IntArray): Int {
        fun dfs(idx: Int): Pair<Long, Long> {
            if (idx * 2 > n) { // leaf node
                return Pair(cost[idx - 1].toLong(), 0L)
            }
            val left = dfs(idx * 2)
            val right = dfs(idx * 2 + 1)
            val maxChild = kotlin.math.max(left.first, right.first)
            val extra = (maxChild - left.first) + (maxChild - right.first)
            val totalInc = left.second + right.second + extra
            val curMaxPath = cost[idx - 1].toLong() + maxChild
            return Pair(curMaxPath, totalInc)
        }
        val result = dfs(1).second
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minIncrements(int n, List<int> cost) {
    List<int> dp = List.filled(n + 1, 0);
    int ans = 0;
    for (int i = n; i >= 1; --i) {
      if (2 * i > n) {
        // leaf node
        dp[i] = cost[i - 1];
      } else {
        int left = dp[2 * i];
        int right = dp[2 * i + 1];
        ans += (left - right).abs();
        dp[i] = cost[i - 1] + (left > right ? left : right);
      }
    }
    return ans;
  }
}
```

## Golang

```go
func minIncrements(n int, cost []int) int {
    maxPath := make([]int64, n+2)
    var ans int64
    for i := n; i >= 1; i-- {
        if 2*i > n { // leaf node
            maxPath[i] = int64(cost[i-1])
        } else {
            left := maxPath[2*i]
            right := maxPath[2*i+1]
            diff := left - right
            if diff < 0 {
                diff = -diff
            }
            ans += diff
            if left > right {
                maxPath[i] = int64(cost[i-1]) + left
            } else {
                maxPath[i] = int64(cost[i-1]) + right
            }
        }
    }
    return int(ans)
}
```

## Ruby

```ruby
def min_increments(n, cost)
  max_sum = Array.new(n + 2, 0)
  inc = Array.new(n + 2, 0)

  i = n
  while i >= 1
    left = i * 2
    if left > n
      max_sum[i] = cost[i - 1]
      inc[i] = 0
    else
      right = left + 1
      diff = (max_sum[left] - max_sum[right]).abs
      inc[i] = inc[left] + inc[right] + diff
      max_sum[i] = [max_sum[left], max_sum[right]].max + cost[i - 1]
    end
    i -= 1
  end

  inc[1]
end
```

## Scala

```scala
object Solution {
    def minIncrements(n: Int, cost: Array[Int]): Int = {
        val dp = new Array[Long](n + 2) // 1-indexed
        var ans: Long = 0L
        for (i <- n to 1 by -1) {
            val left = i * 2
            if (left > n) { // leaf node
                dp(i) = cost(i - 1).toLong
            } else {
                val right = left + 1
                val leftSum = dp(left)
                val rightSum = dp(right)
                ans += math.abs(leftSum - rightSum)
                dp(i) = cost(i - 1).toLong + math.max(leftSum, rightSum)
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_increments(n: i32, cost: Vec<i32>) -> i32 {
        fn dfs(idx: usize, n: usize, cost: &Vec<i32>) -> (i64, i64) {
            // leaf node
            if idx * 2 > n {
                return (cost[idx - 1] as i64, 0);
            }
            let (left_sum, left_inc) = dfs(idx * 2, n, cost);
            let (right_sum, right_inc) = dfs(idx * 2 + 1, n, cost);
            let mut inc = left_inc + right_inc;
            if left_sum > right_sum {
                inc += left_sum - right_sum;
            } else {
                inc += right_sum - left_sum;
            }
            let max_child = left_sum.max(right_sum);
            let total_sum = max_child + cost[idx - 1] as i64;
            (total_sum, inc)
        }

        let (_, ans) = dfs(1, n as usize, &cost);
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-increments n cost)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((cost-vec (list->vector cost)))
    (letrec ((dfs
               (lambda (i)
                 (if (> (* 2 i) n)                     ; leaf node
                     (values (vector-ref cost-vec (- i 1)) 0)
                     (call-with-values
                         (lambda () (dfs (* 2 i)))      ; left subtree
                       (lambda (lsum linc)
                         (call-with-values
                             (lambda () (dfs (+ (* 2 i) 1))) ; right subtree
                           (lambda (rsum rinc)
                             (let* ((inc (+ linc rinc (abs (- lsum rsum))))
                                    (node-sum (+ (vector-ref cost-vec (- i 1))
                                                 (max lsum rsum))))
                               (values node-sum inc))))))))))
      (call-with-values
          (lambda () (dfs 1))
        (lambda (_total-sum total-inc) total-inc)))))
```

## Erlang

```erlang
-module(solution).
-export([min_increments/2]).

-spec min_increments(N :: integer(), Cost :: [integer()]) -> integer().
min_increments(N, Cost) ->
    CostT = list_to_tuple(Cost),
    {_, Inc} = dfs(1, N, CostT),
    Inc.

dfs(Index, N, CostT) when Index > N ->
    {0, 0};
dfs(Index, N, CostT) ->
    LeftIdx = Index * 2,
    case LeftIdx > N of
        true -> % leaf node
            Max = element(Index, CostT),
            {Max, 0};
        false ->
            RightIdx = Index * 2 + 1,
            {MaxL, IncL} = dfs(LeftIdx, N, CostT),
            {MaxR, IncR} = dfs(RightIdx, N, CostT),
            Diff = abs(MaxL - MaxR),
            IncTotal = IncL + IncR + Diff,
            MaxSum = element(Index, CostT) + max(MaxL, MaxR),
            {MaxSum, IncTotal}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_increments(n :: integer, cost :: [integer]) :: integer
  def min_increments(n, cost) do
    arr = :array.from_list([0] ++ cost)
    {_sum, inc} = dfs(1, n, arr)
    inc
  end

  defp dfs(i, n, arr) do
    if 2 * i > n do
      {:array.get(i, arr), 0}
    else
      {left_sum, left_inc} = dfs(2 * i, n, arr)
      {right_sum, right_inc} = dfs(2 * i + 1, n, arr)

      diff = abs(left_sum - right_sum)
      total_inc = left_inc + right_inc + diff

      node_cost = :array.get(i, arr)
      sum = node_cost + max(left_sum, right_sum)

      {sum, total_inc}
    end
  end
end
```
