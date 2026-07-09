# 3429. Paint House IV

## Cpp

```cpp
class Solution {
public:
    long long minCost(int n, vector<vector<int>>& cost) {
        const long long INF = (1LL<<60);
        int pairs = n / 2;
        // dp[a][b] : minimal cost up to previous pair with left color a and right color b
        long long dp[3][3];
        for(int i=0;i<3;++i) for(int j=0;j<3;++j) dp[i][j]=INF;
        // first pair (0, n-1)
        for(int a=0;a<3;++a){
            for(int b=0;b<3;++b){
                dp[a][b] = (long long)cost[0][a] + cost[n-1][b];
            }
        }
        // process remaining pairs
        for(int idx=1; idx<pairs; ++idx){
            long long ndp[3][3];
            for(int i=0;i<3;++i) for(int j=0;j<3;++j) ndp[i][j]=INF;
            int leftIdx = idx;
            int rightIdx = n-1-idx;
            for(int pa=0;pa<3;++pa){
                for(int pb=0;pb<3;++pb){
                    long long prev = dp[pa][pb];
                    if(prev==INF) continue;
                    for(int ca=0;ca<3;++ca){
                        if(ca==pa) continue; // adjacent left houses must differ
                        for(int cb=0;cb<3;++cb){
                            if(cb==pb) continue; // adjacent right houses must differ
                            long long cur = prev + cost[leftIdx][ca] + cost[rightIdx][cb];
                            if(cur < ndp[ca][cb]) ndp[ca][cb]=cur;
                        }
                    }
                }
            }
            for(int i=0;i<3;++i) for(int j=0;j<3;++j) dp[i][j]=ndp[i][j];
        }
        long long ans = INF;
        // final pair houses are adjacent, enforce different colors
        for(int a=0;a<3;++a){
            for(int b=0;b<3;++b){
                if(a==b) continue;
                ans = min(ans, dp[a][b]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minCost(int n, int[][] cost) {
        final long INF = Long.MAX_VALUE / 4;
        long[][] dpPrev = new long[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                dpPrev[i][j] = INF;
            }
        }

        int pairs = n / 2;
        for (int idx = 0; idx < pairs; idx++) {
            int left = idx;
            int right = n - 1 - idx;
            long[][] dpCurr = new long[3][3];
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    dpCurr[i][j] = INF;
                }
            }

            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    if (left + 1 == right && a == b) continue; // adjacent middle houses
                    long curCost = cost[left][a] + cost[right][b];
                    if (idx == 0) {
                        dpCurr[a][b] = curCost;
                    } else {
                        long bestPrev = INF;
                        for (int pa = 0; pa < 3; pa++) {
                            if (pa == a) continue; // left adjacency
                            for (int pb = 0; pb < 3; pb++) {
                                if (pb == b) continue; // right adjacency
                                long prev = dpPrev[pa][pb];
                                if (prev < bestPrev) bestPrev = prev;
                            }
                        }
                        if (bestPrev != INF) {
                            dpCurr[a][b] = curCost + bestPrev;
                        }
                    }
                }
            }
            dpPrev = dpCurr;
        }

        long answer = INF;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (dpPrev[i][j] < answer) answer = dpPrev[i][j];
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, n, cost):
        """
        :type n: int
        :type cost: List[List[int]]
        :rtype: int
        """
        m = n // 2  # number of pairs
        INF = 10**18

        # dp[cl][cr] = minimal cost up to current pair with left house color cl, right house color cr
        dp = [[INF] * 3 for _ in range(3)]
        for cl in range(3):
            for cr in range(3):
                dp[cl][cr] = cost[0][cl] + cost[m][cr]

        for i in range(1, m):
            ndp = [[INF] * 3 for _ in range(3)]
            left_idx = i
            right_idx = i + m
            for cl in range(3):          # color of current left house
                for cr in range(3):      # color of current right house
                    cur_cost = cost[left_idx][cl] + cost[right_idx][cr]
                    best = INF
                    for pl in range(3):  # previous left color
                        if pl == cl:
                            continue
                        for pr in range(3):  # previous right color
                            if pr == cr:
                                continue
                            val = dp[pl][pr] + cur_cost
                            if val < best:
                                best = val
                    ndp[cl][cr] = best
            dp = ndp

        ans = INF
        for cl in range(3):
            for cr in range(3):
                if dp[cl][cr] < ans:
                    ans = dp[cl][cr]
        return int(ans)
```

## Python3

```python
import sys
from typing import List

class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        m = n // 2
        INF = 10 ** 18
        ans = INF

        # iterate over all possible colors for the first pair (house 0 and house m)
        for c0a in range(3):
            for c0b in range(3):
                if c0a == c0b:
                    continue
                dp = [[INF] * 3 for _ in range(3)]
                dp[c0a][c0b] = cost[0][c0a] + cost[m][c0b]

                # process remaining pairs i (1 .. m-1)
                for i in range(1, m):
                    ndp = [[INF] * 3 for _ in range(3)]
                    ca_cost = cost[i]
                    cb_cost = cost[i + m]
                    for pa in range(3):
                        for pb in range(3):
                            cur = dp[pa][pb]
                            if cur == INF:
                                continue
                            for ca in range(3):
                                if ca == pa:
                                    continue
                                for cb in range(3):
                                    if cb == pb or ca == cb:
                                        continue
                                    val = cur + ca_cost[ca] + cb_cost[cb]
                                    if val < ndp[ca][cb]:
                                        ndp[ca][cb] = val
                    dp = ndp

                # after processing all pairs, enforce wrap adjacency between last A (index m-1) and first B (index 0)
                for la in range(3):
                    for lb in range(3):
                        cur = dp[la][lb]
                        if cur == INF:
                            continue
                        if la != c0b:  # adjacency constraint across the middle
                            if cur < ans:
                                ans = cur
        return ans
```

## C

```c
#include <limits.h>

long long minCost(int n, int** cost, int costSize, int* costColSize) {
    int m = n / 2; // number of columns (pairs)
    const long long INF = (1LL<<60);
    long long answer = INF;

    // Iterate over all possible colors for the first column (a0, b0)
    for (int a0 = 0; a0 < 3; ++a0) {
        for (int b0 = 0; b0 < 3; ++b0) {
            if (a0 == b0) continue; // pair constraint
            long long dp[3][3];
            long long ndp[3][3];
            // initialize all to INF
            for (int i = 0; i < 3; ++i)
                for (int j = 0; j < 3; ++j)
                    dp[i][j] = INF;
            dp[a0][b0] = (long long)cost[0][a0] + cost[m][b0];

            // Process remaining columns
            for (int col = 1; col < m; ++col) {
                for (int i = 0; i < 3; ++i)
                    for (int j = 0; j < 3; ++j)
                        ndp[i][j] = INF;

                for (int pa = 0; pa < 3; ++pa) {
                    for (int pb = 0; pb < 3; ++pb) {
                        long long curVal = dp[pa][pb];
                        if (curVal == INF) continue;
                        for (int ca = 0; ca < 3; ++ca) {
                            if (ca == pa) continue; // adjacency top
                            for (int cb = 0; cb < 3; ++cb) {
                                if (cb == pb) continue; // adjacency bottom
                                if (ca == cb) continue; // pair constraint
                                long long cand = curVal + cost[col][ca] + cost[m + col][cb];
                                if (cand < ndp[ca][cb]) ndp[ca][cb] = cand;
                            }
                        }
                    }
                }

                // copy back
                for (int i = 0; i < 3; ++i)
                    for (int j = 0; j < 3; ++j)
                        dp[i][j] = ndp[i][j];
            }

            // After processing all columns, enforce adjacency between last top and first bottom: a_last != b0
            for (int alast = 0; alast < 3; ++alast) {
                for (int blast = 0; blast < 3; ++blast) {
                    long long val = dp[alast][blast];
                    if (val == INF) continue;
                    if (alast == b0) continue; // must differ from first bottom color
                    if (val < answer) answer = val;
                }
            }
        }
    }

    return answer;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MinCost(int n, int[][] cost) {
        int m = n / 2;
        const long INF = (long)4e18;
        long[,] prev = new long[3, 3];
        long[,] cur = new long[3, 3];

        // Initialize for first pair (0 and m)
        for (int cA = 0; cA < 3; ++cA) {
            for (int cB = 0; cB < 3; ++cB) {
                prev[cA, cB] = cost[0][cA] + (long)cost[m][cB];
            }
        }

        // Process remaining pairs
        for (int i = 1; i < m; ++i) {
            int idxA = i;
            int idxB = i + m;
            for (int cA = 0; cA < 3; ++cA) {
                for (int cB = 0; cB < 3; ++cB) {
                    long best = INF;
                    for (int pA = 0; pA < 3; ++pA) {
                        if (pA == cA) continue; // adjacent in first row
                        for (int pB = 0; pB < 3; ++pB) {
                            if (pB == cB) continue; // adjacent in second row
                            long val = prev[pA, pB];
                            if (val < best) best = val;
                        }
                    }
                    cur[cA, cB] = best + cost[idxA][cA] + (long)cost[idxB][cB];
                }
            }
            // swap prev and cur
            var temp = prev;
            prev = cur;
            cur = temp;
        }

        long answer = INF;
        for (int cA = 0; cA < 3; ++cA) {
            for (int cB = 0; cB < 3; ++cB) {
                if (prev[cA, cB] < answer) answer = prev[cA, cB];
            }
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} cost
 * @return {number}
 */
var minCost = function(n, cost) {
    const m = n / 2;
    // precompute combined costs for each pair (i, i+m)
    const pairCosts = new Array(m);
    for (let i = 0; i < m; i++) {
        const arr = new Array(9);
        for (let c1 = 0; c1 < 3; c1++) {
            for (let c2 = 0; c2 < 3; c2++) {
                arr[c1 * 3 + c2] = cost[i][c1] + cost[i + m][c2];
            }
        }
        pairCosts[i] = arr;
    }

    // dp over pairs, state is (color of first half, color of second half) encoded as idx = c1*3 + c2
    let dpPrev = pairCosts[0].slice(); // initialize with first pair costs

    for (let i = 1; i < m; i++) {
        const curCost = pairCosts[i];
        const dpCurr = new Array(9).fill(Infinity);
        for (let s = 0; s < 9; s++) {
            const c1 = Math.floor(s / 3);
            const c2 = s % 3;
            let bestPrev = Infinity;
            for (let p = 0; p < 9; p++) {
                const pc1 = Math.floor(p / 3);
                const pc2 = p % 3;
                if (pc1 !== c1 && pc2 !== c2) { // adjacent houses must differ in each half
                    if (dpPrev[p] < bestPrev) bestPrev = dpPrev[p];
                }
            }
            dpCurr[s] = curCost[s] + bestPrev;
        }
        dpPrev = dpCurr;
    }

    return Math.min(...dpPrev);
};
```

## Typescript

```typescript
function minCost(n: number, cost: number[][]): number {
    const m = n >> 1; // n is even
    const INF = Number.MAX_SAFE_INTEGER;
    // dpPrev[leftColor][rightColor] = minimal cost up to previous pair
    let dpPrev: number[][] = Array.from({ length: 3 }, () => Array(3).fill(INF));

    for (let i = 0; i < m; i++) {
        const leftIdx = i;
        const rightIdx = n - 1 - i;
        const dpCurr: number[][] = Array.from({ length: 3 }, () => Array(3).fill(INF));
        if (i === 0) {
            // No previous colors to consider
            for (let lc = 0; lc < 3; lc++) {
                for (let rc = 0; rc < 3; rc++) {
                    if (lc !== rc) {
                        dpCurr[lc][rc] = cost[leftIdx][lc] + cost[rightIdx][rc];
                    }
                }
            }
        } else {
            for (let plc = 0; plc < 3; plc++) {
                for (let prc = 0; prc < 3; prc++) {
                    const prevVal = dpPrev[plc][prc];
                    if (prevVal === INF) continue;
                    for (let lc = 0; lc < 3; lc++) {
                        if (lc === plc) continue; // adjacent left houses must differ
                        for (let rc = 0; rc < 3; rc++) {
                            if (rc === prc) continue; // adjacent right houses must differ
                            if (lc === rc) continue; // mirrored pair must differ
                            const curCost = prevVal + cost[leftIdx][lc] + cost[rightIdx][rc];
                            if (curCost < dpCurr[lc][rc]) {
                                dpCurr[lc][rc] = curCost;
                            }
                        }
                    }
                }
            }
        }
        dpPrev = dpCurr;
    }

    let ans = INF;
    for (let lc = 0; lc < 3; lc++) {
        for (let rc = 0; rc < 3; rc++) {
            if (dpPrev[lc][rc] < ans) ans = dpPrev[lc][rc];
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $cost
     * @return Integer
     */
    function minCost($n, $cost) {
        $half = intdiv($n, 2);
        $INF = 1 << 60; // sufficiently large
        
        // dp[leftColor][rightColor] = minimal cost up to previous pair
        $dp = [];
        for ($i = 0; $i < 3; $i++) {
            $dp[$i] = array_fill(0, 3, $INF);
        }
        
        // initialize with the first pair (index 0 and half)
        for ($cL = 0; $cL < 3; $cL++) {
            for ($cR = 0; $cR < 3; $cR++) {
                if ($cL == $cR) continue; // opposite houses must differ
                $dp[$cL][$cR] = $cost[0][$cL] + $cost[$half][$cR];
            }
        }
        
        // process remaining pairs
        for ($k = 1; $k < $half; $k++) {
            $newDp = [];
            for ($i = 0; $i < 3; $i++) {
                $newDp[$i] = array_fill(0, 3, $INF);
            }
            
            for ($prevL = 0; $prevL < 3; $prevL++) {
                for ($prevR = 0; $prevR < 3; $prevR++) {
                    $prevVal = $dp[$prevL][$prevR];
                    if ($prevVal >= $INF) continue;
                    
                    // try all valid current color combinations
                    for ($curL = 0; $curL < 3; $curL++) {
                        if ($curL == $prevL) continue; // adjacent left houses must differ
                        for ($curR = 0; $curR < 3; $curR++) {
                            if ($curR == $prevR) continue; // adjacent right houses must differ
                            if ($curL == $curR) continue; // opposite houses must differ
                            
                            $costSum = $cost[$k][$curL] + $cost[$k + $half][$curR];
                            $newVal = $prevVal + $costSum;
                            if ($newVal < $newDp[$curL][$curR]) {
                                $newDp[$curL][$curR] = $newVal;
                            }
                        }
                    }
                }
            }
            
            $dp = $newDp;
        }
        
        // find minimal total cost
        $answer = $INF;
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                if ($dp[$i][$j] < $answer) {
                    $answer = $dp[$i][$j];
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
    func minCost(_ n: Int, _ cost: [[Int]]) -> Int {
        let k = n / 2
        let INF = Int64.max / 4
        var dp = Array(repeating: Array(repeating: INF, count: 3), count: 3)
        
        // first column (i = 0)
        for lc in 0..<3 {
            for rc in 0..<3 where lc != rc {
                dp[lc][rc] = Int64(cost[0][lc] + cost[n - 1][rc])
            }
        }
        
        if k == 1 {
            var ans = INF
            for lc in 0..<3 {
                for rc in 0..<3 where lc != rc {
                    ans = min(ans, dp[lc][rc])
                }
            }
            return Int(ans)
        }
        
        // process remaining columns
        if k > 1 {
            for i in 1..<k {
                var newdp = Array(repeating: Array(repeating: INF, count: 3), count: 3)
                let leftIdx = i
                let rightIdx = n - 1 - i
                for lc in 0..<3 {
                    for rc in 0..<3 where lc != rc {
                        let addCost = Int64(cost[leftIdx][lc] + cost[rightIdx][rc])
                        var bestPrev: Int64 = INF
                        for plc in 0..<3 where plc != lc {
                            for prc in 0..<3 where prc != rc {
                                bestPrev = min(bestPrev, dp[plc][prc])
                            }
                        }
                        if bestPrev < INF {
                            newdp[lc][rc] = bestPrev + addCost
                        }
                    }
                }
                dp = newdp
            }
        }
        
        var ans = INF
        for lc in 0..<3 {
            for rc in 0..<3 where lc != rc {
                ans = min(ans, dp[lc][rc])
            }
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(n: Int, cost: Array<IntArray>): Long {
        val INF = Long.MAX_VALUE / 4
        var dp = Array(3) { LongArray(3) { INF } }
        // first outer pair (0, n-1)
        for (cL in 0..2) {
            for (cR in 0..2) {
                if (cL != cR) {
                    dp[cL][cR] = cost[0][cL].toLong() + cost[n - 1][cR].toLong()
                }
            }
        }
        var left = 1
        var right = n - 2
        while (left <= right) {
            val newDp = Array(3) { LongArray(3) { INF } }
            for (cL in 0..2) {
                for (cR in 0..2) {
                    if (cL == cR) continue // symmetric houses must differ
                    val add = cost[left][cL].toLong() + cost[right][cR].toLong()
                    for (pL in 0..2) {
                        if (cL == pL) continue // adjacent left houses must differ
                        for (pR in 0..2) {
                            if (cR == pR) continue // adjacent right houses must differ
                            val prev = dp[pL][pR]
                            if (prev < INF) {
                                val cand = prev + add
                                if (cand < newDp[cL][cR]) newDp[cL][cR] = cand
                            }
                        }
                    }
                }
            }
            dp = newDp
            left++
            right--
        }
        var ans = INF
        for (i in 0..2) {
            for (j in 0..2) {
                if (dp[i][j] < ans) ans = dp[i][j]
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minCost(int n, List<List<int>> cost) {
    const int INF = 1 << 60;
    const int C = 3;
    int m = n ~/ 2;

    // dpPrev[leftColor][rightColor] = minimal cost up to current processed pair
    List<List<int>> dpPrev =
        List.generate(C, (_) => List.filled(C, INF), growable: false);

    // Initialize with the outermost pair (i = 0)
    for (int cl = 0; cl < C; ++cl) {
      for (int cr = 0; cr < C; ++cr) {
        if (cl == cr) continue; // symmetric houses must differ
        dpPrev[cl][cr] = cost[0][cl] + cost[n - 1][cr];
      }
    }

    // Process inner pairs
    for (int i = 1; i < m; ++i) {
      List<List<int>> dpCurr =
          List.generate(C, (_) => List.filled(C, INF), growable: false);
      int leftIdx = i;
      int rightIdx = n - 1 - i;

      for (int prevL = 0; prevL < C; ++prevL) {
        for (int prevR = 0; prevR < C; ++prevR) {
          int base = dpPrev[prevL][prevR];
          if (base >= INF) continue;
          for (int cl = 0; cl < C; ++cl) {
            if (cl == prevL) continue; // adjacent left houses differ
            for (int cr = 0; cr < C; ++cr) {
              if (cr == prevR) continue; // adjacent right houses differ
              if (cl == cr) continue; // symmetric houses differ
              int val = base + cost[leftIdx][cl] + cost[rightIdx][cr];
              if (val < dpCurr[cl][cr]) dpCurr[cl][cr] = val;
            }
          }
        }
      }
      dpPrev = dpCurr;
    }

    int ans = INF;
    for (int l = 0; l < C; ++l) {
      for (int r = 0; r < C; ++r) {
        if (dpPrev[l][r] < ans) ans = dpPrev[l][r];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func minCost(n int, cost [][]int) int64 {
	const INF int64 = 1 << 60
	half := n / 2

	var dp [3][3]int64
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			dp[i][j] = int64(cost[0][i]) + int64(cost[half][j])
		}
	}

	for idx := 1; idx < half; idx++ {
		var ndp [3][3]int64
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				ndp[i][j] = INF
			}
		}
		leftIdx := idx
		rightIdx := half + idx

		for pl := 0; pl < 3; pl++ {
			for pr := 0; pr < 3; pr++ {
				cur := dp[pl][pr]
				if cur == INF {
					continue
				}
				for cl := 0; cl < 3; cl++ {
					if cl == pl {
						continue
					}
					for cr := 0; cr < 3; cr++ {
						if cr == pr {
							continue
						}
						val := cur + int64(cost[leftIdx][cl]) + int64(cost[rightIdx][cr])
						if val < ndp[cl][cr] {
							ndp[cl][cr] = val
						}
					}
				}
			}
		}
		dp = ndp
	}

	ans := INF
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if dp[i][j] < ans {
				ans = dp[i][j]
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_cost(n, cost)
  INF = 1 << 60
  size = 4 # index 0 for sentinel (-1), 1..3 for colors 0..2
  dp = Array.new(size) { Array.new(size, INF) }
  dp[0][0] = 0

  m = n / 2
  (0...m).each do |k|
    new_dp = Array.new(size) { Array.new(size, INF) }
    left_idx = k
    right_idx = n - 1 - k
    (0..3).each do |pl|
      (0..3).each do |pr|
        cur_val = dp[pl][pr]
        next if cur_val >= INF
        (0..2).each do |cl|
          next if pl != 0 && cl == pl - 1
          (0..2).each do |cr|
            next if cr == cl
            next if pr != 0 && cr == pr - 1
            nl = cl + 1
            nr = cr + 1
            cost_sum = cur_val + cost[left_idx][cl] + cost[right_idx][cr]
            new_dp[nl][nr] = cost_sum if cost_sum < new_dp[nl][nr]
          end
        end
      end
    end
    dp = new_dp
  end

  ans = INF
  (0..3).each do |pl|
    (0..3).each do |pr|
      ans = dp[pl][pr] if dp[pl][pr] < ans
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minCost(n: Int, cost: Array[Array[Int]]): Long = {
        if (n == 0) return 0L
        var prev = Array[Long](
            cost(0)(0).toLong,
            cost(0)(1).toLong,
            cost(0)(2).toLong
        )
        for (i <- 1 until n) {
            val cur = new Array[Long](3)
            // color 0
            cur(0) = cost(i)(0).toLong + math.min(prev(1), prev(2))
            // color 1
            cur(1) = cost(i)(1).toLong + math.min(prev(0), prev(2))
            // color 2
            cur(2) = cost(i)(2).toLong + math.min(prev(0), prev(1))
            prev = cur
        }
        prev.min
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(n: i32, cost: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let half = n / 2;
        const INF: i64 = 1_i64 << 60;
        let mut answer = INF;

        for c0 in 0..3 {
            for cmid in 0..3 {
                // dp for previous house, initialized with only c0 allowed at position 0
                let mut dp_prev = [INF; 3];
                dp_prev[c0] = cost[0][c0] as i64;

                for i in 1..n {
                    let mut dp_cur = [INF; 3];
                    for cur in 0..3 {
                        if i == half && cur != cmid {
                            continue;
                        }
                        for prev in 0..3 {
                            if cur == prev {
                                continue;
                            }
                            let val = dp_prev[prev] + cost[i][cur] as i64;
                            if val < dp_cur[cur] {
                                dp_cur[cur] = val;
                            }
                        }
                    }
                    dp_prev = dp_cur;
                }

                // last house (index n-1) must differ from first house color c0
                for last in 0..3 {
                    if last == c0 {
                        continue;
                    }
                    answer = answer.min(dp_prev[last]);
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (min-cost n cost)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([half (/ n 2)]
         [cost-vec (list->vector (map list->vector cost))]
         [INF 1000000000000000])
    (define (make-dp)
      (vector (vector INF INF INF)
              (vector INF INF INF)
              (vector INF INF INF)))
    (define dpPrev (make-dp))
    ;; initialize first pair
    (for ([c1 (in-range 3)])
      (for ([c2 (in-range 3)])
        (when (not (= c1 c2))
          (let* ([cst1 ((vector-ref (vector-ref cost-vec 0) c1))]
                 [cst2 ((vector-ref (vector-ref cost-vec half) c2))])
            (vector-set! (vector-ref dpPrev c1) c2 (+ cst1 cst2))))))
    ;; process remaining pairs
    (for ([i (in-range 1 half)])
      (define dpCurr (make-dp))
      (for ([c1 (in-range 3)])
        (for ([c2 (in-range 3)])
          (when (not (= c1 c2))
            (let* ([cur (+ ((vector-ref (vector-ref cost-vec i) c1))
                           ((vector-ref (vector-ref cost-vec (+ i half)) c2)))])
              (define minPrev INF)
              (for ([p1 (in-range 3)])
                (for ([p2 (in-range 3)])
                  (when (and (not (= p1 p2))
                             (not (= p1 c1))
                             (not (= p2 c2)))
                    (let ([val ((vector-ref (vector-ref dpPrev p1) p2))])
                      (when (< val minPrev)
                        (set! minPrev val)))) ))
              (vector-set! (vector-ref dpCurr c1) c2 (+ cur minPrev))))))
      (set! dpPrev dpCurr))
    ;; find answer
    (define ans INF)
    (for ([c1 (in-range 3)])
      (for ([c2 (in-range 3)])
        (when (not (= c1 c2))
          (let ([val ((vector-ref (vector-ref dpPrev c1) c2))])
            (when (< val ans) (set! ans val))))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/2]).

-define(INF, 1 bsl 60).

min_cost(N, Cost) ->
    M = N div 2,
    {LeftList, RightList} = lists:split(M, Cost),
    Combos = [{L,R} || L <- [0,1,2], R <- [0,1,2]],
    lists:foldl(fun({InitL, InitR}, Acc) ->
        % initial cost for first pair
        FirstLeftCost  = lists:nth(InitL + 1, hd(LeftList)),
        FirstRightCost = lists:nth(InitR + 1, hd(RightList)),
        InitCost = FirstLeftCost + FirstRightCost,
        DP0 = [ if I == (InitL*3+InitR) -> InitCost; true -> ?INF end
                || I <- lists:seq(0,8)],
        % process remaining pairs
        FinalDP = process_pairs(tl(LeftList), tl(RightList), DP0),
        % enforce cross adjacency between last left and first right
        MinVal = min_last(FinalDP, InitR),
        case Acc of
            undefined -> MinVal;
            _ when MinVal < Acc -> MinVal;
            _ -> Acc
        end
    end, undefined, Combos).

process_pairs([], [], DP) ->
    DP;
process_pairs([LC|LT], [RC|RT], DPPrev) ->
    NewDP = [
        begin
            MinPrev = min_prev(DPPrev, CurL, CurR),
            if MinPrev == ?INF -> ?INF;
               true -> MinPrev + lists:nth(CurL+1, LC) + lists:nth(CurR+1, RC)
            end
        end
        || CurL <- [0,1,2], CurR <- [0,1,2]
    ],
    process_pairs(LT, RT, NewDP).

min_prev(DPPrev, CurL, CurR) ->
    lists:foldl(fun(Idx, Acc) ->
        PrevL = Idx div 3,
        PrevR = Idx rem 3,
        if PrevL =/= CurL andalso PrevR =/= CurR ->
                Val = lists:nth(Idx+1, DPPrev),
                if Val < Acc -> Val; true -> Acc end;
           true -> Acc
        end
    end, ?INF, lists:seq(0,8)).

min_last(DP, FirstRight) ->
    lists:foldl(fun(Idx, Acc) ->
        L = Idx div 3,
        if L =/= FirstRight ->
                Val = lists:nth(Idx+1, DP),
                if Val < Acc -> Val; true -> Acc end;
           true -> Acc
        end
    end, ?INF, lists:seq(0,8)).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(n :: integer, cost :: [[integer]]) :: integer
  def min_cost(n, cost) do
    half = div(n, 2)
    inf = 1 <<< 60

    # Initialize dp for the first pair (i = 0)
    dp =
      Enum.reduce(0..2, %{}, fn cl, acc ->
        Enum.reduce(0..2, acc, fn cr, acc2 ->
          if cl != cr do
            c = Enum.at(cost, 0) |> Enum.at(cl)
            d = Enum.at(cost, n - 1) |> Enum.at(cr)
            Map.put(acc2, {cl, cr}, c + d)
          else
            acc2
          end
        end)
      end)

    # Process remaining pairs
    dp =
      if half > 1 do
        Enum.reduce(1..(half - 1), dp, fn i, cur_dp ->
          left_row = Enum.at(cost, i)
          right_row = Enum.at(cost, n - 1 - i)

          new_dp =
            Enum.reduce(cur_dp, %{}, fn {{pl, pr}, prev_cost}, ndp ->
              Enum.reduce(0..2, ndp, fn cl, ndp2 ->
                if cl == pl do
                  ndp2
                else
                  Enum.reduce(0..2, ndp2, fn cr, ndp3 ->
                    cond do
                      cr == pr -> ndp3
                      cl == cr -> ndp3
                      true ->
                        total = prev_cost + Enum.at(left_row, cl) + Enum.at(right_row, cr)
                        key = {cl, cr}
                        existing = Map.get(ndp3, key, inf)

                        if total < existing do
                          Map.put(ndp3, key, total)
                        else
                          ndp3
                        end
                    end
                  end)
                end
              end)
            end)

          new_dp
        end)
      else
        dp
      end

    dp |> Map.values() |> Enum.min()
  end
end
```
