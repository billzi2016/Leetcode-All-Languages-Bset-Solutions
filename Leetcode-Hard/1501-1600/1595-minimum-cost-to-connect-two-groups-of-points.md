# 1595. Minimum Cost to Connect Two Groups of Points

## Cpp

```cpp
class Solution {
public:
    int connectTwoGroups(vector<vector<int>>& cost) {
        int n = cost.size();
        int m = cost[0].size();
        const int INF = 1e9;
        // precompute sumCost[i][mask]
        vector<vector<int>> sumCost(n, vector<int>(1 << m, 0));
        for (int i = 0; i < n; ++i) {
            for (int mask = 1; mask < (1 << m); ++mask) {
                int lsb = mask & -mask;
                int bit = __builtin_ctz(lsb);
                sumCost[i][mask] = sumCost[i][mask ^ lsb] + cost[i][bit];
            }
        }
        // min cost for each right point across all left points
        vector<int> minRight(m, INF);
        for (int j = 0; j < m; ++j) {
            for (int i = 0; i < n; ++i)
                minRight[j] = min(minRight[j], cost[i][j]);
        }
        // memoization dp[i][mask]
        vector<vector<int>> memo(n + 1, vector<int>(1 << m, -1));
        function<int(int,int)> dfs = [&](int i, int mask) -> int {
            if (i == n) {
                int extra = 0;
                for (int j = 0; j < m; ++j)
                    if (!(mask >> j & 1)) extra += minRight[j];
                return extra;
            }
            int &res = memo[i][mask];
            if (res != -1) return res;
            int best = INF;
            // each left point must connect to at least one right point
            for (int sub = 1; sub < (1 << m); ++sub) {
                int newMask = mask | sub;
                int cur = sumCost[i][sub] + dfs(i + 1, newMask);
                if (cur < best) best = cur;
            }
            res = best;
            return res;
        };
        return dfs(0, 0);
    }
};
```

## Java

```java
class Solution {
    public int connectTwoGroups(java.util.List<java.util.List<Integer>> cost) {
        int m = cost.size();
        int n = cost.get(0).size();
        int fullMask = 1 << n;
        int INF = Integer.MAX_VALUE / 4;

        // Precompute sum of costs for each left point and every subset of right points
        int[][] sums = new int[m][fullMask];
        for (int i = 0; i < m; i++) {
            for (int sub = 1; sub < fullMask; sub++) {
                int lowbit = sub & -sub;
                int idx = Integer.numberOfTrailingZeros(lowbit);
                sums[i][sub] = sums[i][sub ^ lowbit] + cost.get(i).get(idx);
            }
        }

        int[] dp = new int[fullMask];
        java.util.Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int i = 0; i < m; i++) {
            int[] ndp = new int[fullMask];
            java.util.Arrays.fill(ndp, INF);
            for (int mask = 0; mask < fullMask; mask++) {
                if (dp[mask] == INF) continue;
                for (int sub = 1; sub < fullMask; sub++) {
                    int newMask = mask | sub;
                    int val = dp[mask] + sums[i][sub];
                    if (val < ndp[newMask]) ndp[newMask] = val;
                }
            }
            dp = ndp;
        }

        return dp[fullMask - 1];
    }
}
```

## Python

```python
class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        n = len(cost)
        m = len(cost[0])
        # minimum cost to connect each right point from any left point
        min_right = [min(cost[i][j] for i in range(n)) for j in range(m)]
        full_mask = (1 << m) - 1
        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0

        for i in range(n):
            ndp = [INF] * (1 << m)
            for mask in range(1 << m):
                cur = dp[mask]
                if cur == INF:
                    continue
                for j in range(m):
                    new_mask = mask | (1 << j)
                    val = cur + cost[i][j]
                    if val < ndp[new_mask]:
                        ndp[new_mask] = val
            dp = ndp

        ans = INF
        for mask in range(1 << m):
            if dp[mask] == INF:
                continue
            extra = 0
            missing = full_mask ^ mask
            # add cheapest connections for uncovered right points
            j = 0
            while missing:
                if missing & 1:
                    extra += min_right[j]
                missing >>= 1
                j += 1
            total = dp[mask] + extra
            if total < ans:
                ans = total
        return ans
```

## Python3

```python
class Solution:
    def connectTwoGroups(self, cost):
        from math import inf
        m, n = len(cost), len(cost[0])
        full_mask = (1 << n) - 1

        # precompute sum of costs for each left point and subset of right points
        sum_cost = [[0] * (1 << n) for _ in range(m)]
        for i in range(m):
            for mask in range(1, 1 << n):
                lowbit = mask & -mask
                j = (lowbit.bit_length() - 1)
                sum_cost[i][mask] = sum_cost[i][mask ^ lowbit] + cost[i][j]

        INF = 10 ** 9
        dp = [INF] * (1 << n)

        # first left point must connect to at least one right point
        for mask in range(1, 1 << n):
            dp[mask] = sum_cost[0][mask]

        # process remaining left points
        for i in range(1, m):
            newdp = [INF] * (1 << n)
            for mask in range(1 << n):
                sub = mask
                while sub:
                    prev_mask = mask ^ sub
                    val = dp[prev_mask] + sum_cost[i][sub]
                    if val < newdp[mask]:
                        newdp[mask] = val
                    sub = (sub - 1) & mask
            dp = newdp

        return dp[full_mask]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int connectTwoGroups(int** cost, int costSize, int* costColSize) {
    int n = costSize;
    int m = costColSize[0];
    int fullMask = (1 << m) - 1;
    const int INF = 1000000000;

    /* precompute sum of costs for each left point and subset of right points */
    int **sum = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        sum[i] = (int *)malloc((fullMask + 1) * sizeof(int));
        sum[i][0] = 0;
        for (int mask = 1; mask <= fullMask; ++mask) {
            int lsb = mask & -mask;
            int bit = __builtin_ctz(lsb);
            int prev = mask ^ lsb;
            sum[i][mask] = sum[i][prev] + cost[i][bit];
        }
    }

    int *dpPrev = (int *)malloc((fullMask + 1) * sizeof(int));
    int *dpCurr = (int *)malloc((fullMask + 1) * sizeof(int));

    for (int mask = 0; mask <= fullMask; ++mask) dpPrev[mask] = INF;
    dpPrev[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int mask = 0; mask <= fullMask; ++mask) dpCurr[mask] = INF;

        for (int mask = 0; mask <= fullMask; ++mask) {
            if (dpPrev[mask] == INF) continue;
            for (int sub = 1; sub <= fullMask; ++sub) {
                int newMask = mask | sub;
                int val = dpPrev[mask] + sum[i][sub];
                if (val < dpCurr[newMask]) dpCurr[newMask] = val;
            }
        }

        int *tmp = dpPrev;
        dpPrev = dpCurr;
        dpCurr = tmp;
    }

    int ans = dpPrev[fullMask];

    for (int i = 0; i < n; ++i) free(sum[i]);
    free(sum);
    free(dpPrev);
    free(dpCurr);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int ConnectTwoGroups(IList<IList<int>> cost) {
        int n = cost.Count;
        int m = cost[0].Count;
        int[,] c = new int[n, m];
        for (int i = 0; i < n; i++) {
            var row = cost[i];
            for (int j = 0; j < m; j++) {
                c[i, j] = row[j];
            }
        }

        // minimum cost to connect any left node to each right node
        int[] minRight = new int[m];
        for (int j = 0; j < m; j++) {
            int mn = int.MaxValue;
            for (int i = 0; i < n; i++) {
                if (c[i, j] < mn) mn = c[i, j];
            }
            minRight[j] = mn;
        }

        int maxMask = 1 << m;
        const int INF = 1_000_000_000;
        int[] dp = new int[maxMask];
        for (int mask = 0; mask < maxMask; mask++) dp[mask] = INF;
        dp[0] = 0;

        // DP over each left node
        for (int i = 0; i < n; i++) {
            // precompute cost of connecting this left node to any subset of right nodes
            int[] subCost = new int[maxMask];
            for (int sub = 1; sub < maxMask; sub++) {
                int sum = 0;
                for (int j = 0; j < m; j++) {
                    if ((sub & (1 << j)) != 0) sum += c[i, j];
                }
                subCost[sub] = sum;
            }

            int[] newDp = new int[maxMask];
            for (int mask = 0; mask < maxMask; mask++) newDp[mask] = INF;

            for (int prevMask = 0; prevMask < maxMask; prevMask++) {
                if (dp[prevMask] == INF) continue;
                // connect current left node to a non‑empty subset
                for (int sub = 1; sub < maxMask; sub++) {
                    int newMask = prevMask | sub;
                    int val = dp[prevMask] + subCost[sub];
                    if (val < newDp[newMask]) newDp[newMask] = val;
                }
            }

            dp = newDp;
        }

        int fullMask = maxMask - 1;
        int answer = INF;
        for (int mask = 0; mask < maxMask; mask++) {
            if (dp[mask] == INF) continue;
            int extra = 0;
            int missing = fullMask ^ mask;
            for (int j = 0; j < m; j++) {
                if ((missing & (1 << j)) != 0) extra += minRight[j];
            }
            int total = dp[mask] + extra;
            if (total < answer) answer = total;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} cost
 * @return {number}
 */
var connectTwoGroups = function(cost) {
    const n = cost.length;
    const m = cost[0].length;
    const fullMask = (1 << m) - 1;

    // precompute sum[i][mask] = total cost of connecting left i to all right points in mask
    const sum = Array.from({ length: n }, () => new Array(1 << m).fill(0));
    for (let i = 0; i < n; i++) {
        for (let mask = 1; mask <= fullMask; mask++) {
            const lsb = mask & -mask;
            const j = Math.round(Math.log2(lsb)); // index of least significant set bit
            sum[i][mask] = sum[i][mask ^ (1 << j)] + cost[i][j];
        }
    }

    let cur = new Array(1 << m).fill(Infinity);
    cur[0] = 0;

    for (let i = 0; i < n; i++) {
        const nxt = new Array(1 << m).fill(Infinity);
        for (let mask = 0; mask <= fullMask; mask++) {
            if (cur[mask] === Infinity) continue;
            // each left point must connect to at least one right point
            for (let sub = 1; sub <= fullMask; sub++) {
                const newMask = mask | sub;
                const val = cur[mask] + sum[i][sub];
                if (val < nxt[newMask]) nxt[newMask] = val;
            }
        }
        cur = nxt;
    }

    return cur[fullMask];
};
```

## Typescript

```typescript
function connectTwoGroups(cost: number[][]): number {
    const m = cost.length;
    const n = cost[0].length;
    const INF = Number.MAX_SAFE_INTEGER;
    const size = 1 << n;

    let dp = new Array<number>(size).fill(INF);
    dp[0] = 0;

    for (let i = 0; i < m; i++) {
        const ndp = new Array<number>(size).fill(INF);
        for (let mask = 0; mask < size; mask++) {
            const cur = dp[mask];
            if (cur === INF) continue;
            for (let j = 0; j < n; j++) {
                const nMask = mask | (1 << j);
                const val = cur + cost[i][j];
                if (val < ndp[nMask]) ndp[nMask] = val;
            }
        }
        dp = ndp;
    }

    const minRight = new Array<number>(n).fill(INF);
    for (let j = 0; j < n; j++) {
        let mn = INF;
        for (let i = 0; i < m; i++) {
            if (cost[i][j] < mn) mn = cost[i][j];
        }
        minRight[j] = mn;
    }

    let ans = INF;
    for (let mask = 0; mask < size; mask++) {
        let total = dp[mask];
        if (total === INF) continue;
        for (let j = 0; j < n; j++) {
            if ((mask & (1 << j)) === 0) total += minRight[j];
        }
        if (total < ans) ans = total;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $cost
     * @return Integer
     */
    function connectTwoGroups($cost) {
        $m = count($cost);
        $n = count($cost[0]);
        $fullMask = (1 << $n) - 1;
        $INF = PHP_INT_MAX;

        // precompute min cost for each right point
        $minRight = array_fill(0, $n, $INF);
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($cost[$i][$j] < $minRight[$j]) {
                    $minRight[$j] = $cost[$i][$j];
                }
            }
        }

        // map single bit to its index
        $bitIdx = [];
        for ($b = 0; $b < $n; ++$b) {
            $bitIdx[1 << $b] = $b;
        }

        // precompute subset costs for each left point
        $subsetCost = array_fill(0, $m, []);
        for ($i = 0; $i < $m; ++$i) {
            $subsetCost[$i] = array_fill(0, $fullMask + 1, 0);
            for ($mask = 1; $mask <= $fullMask; ++$mask) {
                $lsb = $mask & (-$mask);
                $prev = $mask ^ $lsb;
                $idx = $bitIdx[$lsb];
                $subsetCost[$i][$mask] = $subsetCost[$i][$prev] + $cost[$i][$idx];
            }
        }

        // DP over left points
        $dp = array_fill(0, $fullMask + 1, $INF);
        $dp[0] = 0;

        for ($i = 0; $i < $m; ++$i) {
            $newdp = array_fill(0, $fullMask + 1, $INF);
            for ($mask = 0; $mask <= $fullMask; ++$mask) {
                if ($dp[$mask] === $INF) continue;
                // connect current left point to any non‑empty subset of right points
                for ($sub = 1; $sub <= $fullMask; ++$sub) {
                    $newMask = $mask | $sub;
                    $val = $dp[$mask] + $subsetCost[$i][$sub];
                    if ($val < $newdp[$newMask]) {
                        $newdp[$newMask] = $val;
                    }
                }
            }
            $dp = $newdp;
        }

        // add cheapest connections for uncovered right points
        $answer = $INF;
        for ($mask = 0; $mask <= $fullMask; ++$mask) {
            if ($dp[$mask] === $INF) continue;
            $extra = 0;
            $missing = (~$mask) & $fullMask;
            for ($j = 0; $j < $n; ++$j) {
                if (($missing >> $j) & 1) {
                    $extra += $minRight[$j];
                }
            }
            $total = $dp[$mask] + $extra;
            if ($total < $answer) {
                $answer = $total;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func connectTwoGroups(_ cost: [[Int]]) -> Int {
        let n = cost.count
        let m = cost[0].count
        let totalMask = 1 << m
        let INF = Int.max / 4
        
        var dp = Array(repeating: INF, count: totalMask)
        dp[0] = 0
        
        // Minimum cost to connect each right point from any left point
        var minCostRight = Array(repeating: INF, count: m)
        for j in 0..<m {
            var mn = INF
            for i in 0..<n {
                mn = min(mn, cost[i][j])
            }
            minCostRight[j] = mn
        }
        
        for i in 0..<n {
            // Precompute cost of connecting left point i to any subset of right points
            var subCost = Array(repeating: 0, count: totalMask)
            if m > 0 {
                for sub in 1..<totalMask {
                    let lowbit = sub & -sub
                    let idx = lowbit.trailingZeroBitCount
                    let prev = sub ^ lowbit
                    subCost[sub] = subCost[prev] + cost[i][idx]
                }
            }
            
            var ndp = Array(repeating: INF, count: totalMask)
            for mask in 0..<totalMask {
                if dp[mask] == INF { continue }
                var sub = mask
                while true {
                    let newVal = dp[mask ^ sub] + subCost[sub]
                    if newVal < ndp[mask] {
                        ndp[mask] = newVal
                    }
                    if sub == 0 { break }
                    sub = (sub - 1) & mask
                }
            }
            dp = ndp
        }
        
        var answer = INF
        let fullMask = totalMask - 1
        for mask in 0..<totalMask {
            let cur = dp[mask]
            if cur == INF { continue }
            var extra = 0
            var missing = fullMask ^ mask
            while missing > 0 {
                let lowbit = missing & -missing
                let idx = lowbit.trailingZeroBitCount
                extra += minCostRight[idx]
                missing ^= lowbit
            }
            answer = min(answer, cur + extra)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun connectTwoGroups(cost: List<List<Int>>): Int {
        val m = cost.size
        val n = cost[0].size
        val fullMask = (1 shl n) - 1
        val INF = 1_000_000_000

        // Precompute sum of costs for each left point and every subset of right points
        val sumCost = Array(m) { IntArray(1 shl n) }
        for (i in 0 until m) {
            for (mask in 1..fullMask) {
                val lsb = mask and -mask
                val j = Integer.numberOfTrailingZeros(lsb)
                val prev = mask xor lsb
                sumCost[i][mask] = sumCost[i][prev] + cost[i][j]
            }
        }

        var dp = IntArray(1 shl n) { INF }
        dp[0] = 0

        for (i in 0 until m) {
            val ndp = IntArray(1 shl n) { INF }
            for (mask in 0..fullMask) {
                val cur = dp[mask]
                if (cur == INF) continue
                var sub = 1
                while (sub <= fullMask) {
                    val newMask = mask or sub
                    val newCost = cur + sumCost[i][sub]
                    if (newCost < ndp[newMask]) {
                        ndp[newMask] = newCost
                    }
                    sub++
                }
            }
            dp = ndp
        }

        return dp[fullMask]
    }
}
```

## Dart

```dart
class Solution {
  int connectTwoGroups(List<List<int>> cost) {
    int n = cost.length;
    int m = cost[0].length;
    int fullMask = (1 << m) - 1;
    const int INF = 1 << 30;

    // Minimum cost to connect any left point to each right point
    List<int> minRight = List.filled(m, INF);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (cost[i][j] < minRight[j]) minRight[j] = cost[i][j];
      }
    }

    List<int> dp = List.filled(1 << m, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
      List<int> ndp = List.filled(1 << m, INF);
      for (int mask = 0; mask <= fullMask; ++mask) {
        int cur = dp[mask];
        if (cur == INF) continue;
        for (int j = 0; j < m; ++j) {
          int newMask = mask | (1 << j);
          int val = cur + cost[i][j];
          if (val < ndp[newMask]) ndp[newMask] = val;
        }
      }
      dp = ndp;
    }

    int answer = INF;
    for (int mask = 0; mask <= fullMask; ++mask) {
      int cur = dp[mask];
      if (cur == INF) continue;
      int extra = 0;
      for (int j = 0; j < m; ++j) {
        if ((mask & (1 << j)) == 0) extra += minRight[j];
      }
      int total = cur + extra;
      if (total < answer) answer = total;
    }

    return answer;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func connectTwoGroups(cost [][]int) int {
	n := len(cost)
	m := len(cost[0])
	fullMask := (1 << m) - 1

	subsetCost := make([][]int, n)
	for i := 0; i < n; i++ {
		subsetCost[i] = make([]int, 1<<m)
		for mask := 1; mask < 1<<m; mask++ {
			lsb := mask & -mask
			bitIdx := bits.TrailingZeros(uint(lsb))
			prev := mask ^ lsb
			subsetCost[i][mask] = subsetCost[i][prev] + cost[i][bitIdx]
		}
	}

	const INF int = 1 << 60
	dp := make([]int, 1<<m)
	for i := range dp {
		dp[i] = INF
	}
	dp[0] = 0

	for i := 0; i < n; i++ {
		ndp := make([]int, 1<<m)
		for j := range ndp {
			ndp[j] = INF
		}
		for maskPrev := 0; maskPrev < 1<<m; maskPrev++ {
			if dp[maskPrev] == INF {
				continue
			}
			base := dp[maskPrev]
			for s := 1; s < 1<<m; s++ {
				newMask := maskPrev | s
				val := base + subsetCost[i][s]
				if val < ndp[newMask] {
					ndp[newMask] = val
				}
			}
		}
		dp = ndp
	}

	return dp[fullMask]
}
```

## Ruby

```ruby
def connect_two_groups(cost)
  n1 = cost.length
  m = cost[0].length
  full_mask = (1 << m) - 1
  INF = 1 << 60

  # precompute sum of costs for each left point and every subset of right points
  sum = Array.new(n1) { Array.new(1 << m, 0) }
  (0...n1).each do |i|
    (1..full_mask).each do |mask|
      lsb = mask & -mask
      idx = lsb.bit_length - 1
      sum[i][mask] = sum[i][mask ^ lsb] + cost[i][idx]
    end
  end

  dp = Array.new(1 << m, INF)
  # first left point must connect to at least one right point
  (1..full_mask).each do |mask|
    dp[mask] = sum[0][mask]
  end

  (1...n1).each do |i|
    newdp = Array.new(1 << m, INF)
    (0..full_mask).each do |mask|
      sub = mask
      while sub > 0
        prev = dp[mask ^ sub]
        if prev < INF
          val = prev + sum[i][sub]
          newdp[mask] = val if val < newdp[mask]
        end
        sub = (sub - 1) & mask
      end
    end
    dp = newdp
  end

  dp[full_mask]
end
```

## Scala

```scala
object Solution {
    def connectTwoGroups(cost: List[List[Int]]): Int = {
        val n1 = cost.length
        val n2 = if (n1 == 0) 0 else cost(0).length
        val fullMask = (1 << n2) - 1
        val INF = Int.MaxValue / 4

        // Convert to array for faster access
        val cArr = Array.ofDim[Int](n1, n2)
        var i = 0
        while (i < n1) {
            val row = cost(i)
            var j = 0
            while (j < n2) {
                cArr(i)(j) = row(j)
                j += 1
            }
            i += 1
        }

        // Precompute sumCost[i][mask] = sum of costs for left i to all right nodes in mask
        val sumCost = Array.ofDim[Int](n1, 1 << n2)
        i = 0
        while (i < n1) {
            val arr = sumCost(i)
            var mask = 1
            while (mask <= fullMask) {
                val lsb = mask & -mask
                val idx = Integer.numberOfTrailingZeros(lsb)
                arr(mask) = arr(mask ^ lsb) + cArr(i)(idx)
                mask += 1
            }
            i += 1
        }

        var dp = Array.fill(1 << n2)(INF)
        dp(0) = 0

        // All non‑empty subsets of right group
        val subsets = (1 to fullMask).toArray

        i = 0
        while (i < n1) {
            val ndp = Array.fill(1 << n2)(INF)
            var maskPrev = 0
            while (maskPrev <= fullMask) {
                val prevVal = dp(maskPrev)
                if (prevVal < INF) {
                    var sIdx = 0
                    while (sIdx < subsets.length) {
                        val sub = subsets(sIdx)
                        val newMask = maskPrev | sub
                        val newCost = prevVal + sumCost(i)(sub)
                        if (newCost < ndp(newMask)) ndp(newMask) = newCost
                        sIdx += 1
                    }
                }
                maskPrev += 1
            }
            dp = ndp
            i += 1
        }

        dp(fullMask)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn connect_two_groups(cost: Vec<Vec<i32>>) -> i32 {
        let m = cost.len();
        let n = cost[0].len();
        let max_mask = 1usize << n;

        // precompute cost of connecting a left point to any subset of right points
        let mut sub_cost = vec![vec![0i32; max_mask]; m];
        for i in 0..m {
            for mask in 1..max_mask {
                let bit = mask.trailing_zeros() as usize;
                let prev = mask ^ (1usize << bit);
                sub_cost[i][mask] = sub_cost[i][prev] + cost[i][bit];
            }
        }

        let inf: i64 = 1i64 << 60;
        let mut dp = vec![inf; max_mask];
        dp[0] = 0;

        for i in 0..m {
            let mut ndp = vec![inf; max_mask];
            for mask in 0..max_mask {
                if dp[mask] == inf {
                    continue;
                }
                let base = dp[mask];
                // each left point must connect to at least one right point
                for s in 1..max_mask {
                    let new_mask = mask | s;
                    let val = base + sub_cost[i][s] as i64;
                    if val < ndp[new_mask] {
                        ndp[new_mask] = val;
                    }
                }
            }
            dp = ndp;
        }

        dp[max_mask - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (connect-two-groups cost)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length cost))
         (m (if (= n 0) 0 (length (first cost))))
         (fullMask (- (arithmetic-shift 1 m) 1))
         (maskCount (add1 fullMask))
         (INF 1000000000)
         ;; convert to vector of vectors for fast indexing
         (cost-vec (list->vector (map list->vector cost)))
         ;; precompute sumCost[i][mask]
         (sum-costs
          (let ((arr (make-vector n)))
            (for ([i (in-range n)])
              (define row (vector-ref cost-vec i))
              (define sums (make-vector maskCount 0))
              (for ([mask (in-range 1 maskCount)])
                (define sum 0)
                (for ([j (in-range m)])
                  (when (not (= 0 (bitwise-and mask (arithmetic-shift 1 j))))
                    (set! sum (+ sum (vector-ref row j)))))
                (vector-set! sums mask sum))
              (vector-set! arr i sums))
            arr)))
    ;; dp initialization
    (define dp (make-vector maskCount INF))
    (vector-set! dp 0 0)
    ;; process each left point
    (for ([i (in-range n)])
      (define ndp (make-vector maskCount INF))
      (for ([mask (in-range maskCount)])
        (let loop ((sub mask))
          (when (> sub 0)
            (define prev-mask (- mask sub)) ; since sub ⊆ mask, xor equals subtraction
            (define prev-cost (vector-ref dp prev-mask))
            (when (< prev-cost INF) ; reachable state
              (define cand (+ prev-cost (vector-ref (vector-ref sum-costs i) sub)))
              (when (< cand (vector-ref ndp mask))
                (vector-set! ndp mask cand)))
            (loop (bitwise-and (- sub 1) mask)))))
      (set! dp ndp))
    (vector-ref dp fullMask)))
```

## Erlang

```erlang
-module(solution).
-export([connect_two_groups/1]).

-spec connect_two_groups(Cost :: [[integer()]]) -> integer().
connect_two_groups(Cost) ->
    M = length(hd(Cost)),
    FullMask = (1 bsl M) - 1,
    SumTuples = [row_sum_tuple(Row, FullMask) || Row <- Cost],
    INF = 1 bsl 60,
    DP0 = #{0 => 0},
    FinalDP = lists:foldl(fun(RowSumTuple, DPPrev) ->
        NewDP = maps:new(),
        UpdatedDP = lists:foldl(fun(Mask, AccDP) ->
            MinCost = min_cost_for_mask(Mask, DPPrev, RowSumTuple, INF),
            maps:put(Mask, MinCost, AccDP)
        end, NewDP, lists:seq(0, FullMask)),
        UpdatedDP
    end, DP0, SumTuples),
    maps:get(FullMask, FinalDP).

row_sum_tuple(Row, FullMask) ->
    Sums = [calc_sum(Row, Mask) || Mask <- lists:seq(0, FullMask)],
    list_to_tuple(Sums).

calc_sum(_Row, 0) -> 0;
calc_sum(Row, Mask) ->
    calc_sum(Row, Mask, 0, 0).

calc_sum(_Row, 0, _Pos, Acc) -> Acc;
calc_sum(Row, Mask, Pos, Acc) ->
    case (Mask band 1) of
        0 ->
            calc_sum(Row, Mask bsr 1, Pos + 1, Acc);
        _ ->
            Cost = lists:nth(Pos + 1, Row),
            calc_sum(Row, Mask bsr 1, Pos + 1, Acc + Cost)
    end.

min_cost_for_mask(Mask, DPPrev, RowSumTuple, INF) ->
    min_cost_submask(Mask, Mask, DPPrev, RowSumTuple, INF, INF).

min_cost_submask(Sub, Mask, DPPrev, RowSumTuple, Best, INF) ->
    Added = Mask band bnot Sub,
    NewBest =
        if
            Added =:= 0 -> Best;
            true ->
                PrevCost = maps:get(Sub, DPPrev, INF),
                case PrevCost of
                    INF -> Best;
                    _ ->
                        CostAdd = element(Added + 1, RowSumTuple),
                        Total = PrevCost + CostAdd,
                        if Total < Best -> Total; true -> Best end
                end
        end,
    if Sub == 0 ->
            NewBest;
       true ->
            NextSub = (Sub - 1) band Mask,
            min_cost_submask(NextSub, Mask, DPPrev, RowSumTuple, NewBest, INF)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec connect_two_groups(cost :: [[integer]]) :: integer
  def connect_two_groups(cost) do
    import Bitwise

    n = length(cost)
    m = cost |> List.first() |> length()
    full_mask = (1 <<< m) - 1
    inf = 1_000_000_000

    min_right =
      for j <- 0..(m - 1) do
        cost
        |> Enum.map(fn row -> Enum.at(row, j) end)
        |> Enum.min()
      end

    dp_initial = %{0 => 0}

    dp_final =
      Enum.reduce(cost, dp_initial, fn row, dp_acc ->
        Enum.reduce(dp_acc, %{}, fn {mask, cur}, acc ->
          Enum.with_index(row)
          |> Enum.reduce(acc, fn {c, j}, inner_acc ->
            new_mask = mask ||| (1 <<< j)
            val = cur + c

            case Map.get(inner_acc, new_mask) do
              nil -> Map.put(inner_acc, new_mask, val)
              existing when val < existing -> Map.put(inner_acc, new_mask, val)
              _ -> inner_acc
            end
          end)
        end)
      end)

    Enum.reduce(dp_final, inf, fn {mask, cur}, best ->
      extra =
        0..(m - 1)
        |> Enum.filter(fn j -> ((mask >>> j) &&& 1) == 0 end)
        |> Enum.map(&Enum.at(min_right, &1))
        |> Enum.sum()

      total = cur + extra
      if total < best, do: total, else: best
    end)
  end
end
```
