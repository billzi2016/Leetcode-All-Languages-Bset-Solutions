# 3149. Find the Minimum Cost Array Permutation

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findPermutation(vector<int>& nums) {
        int n = nums.size();
        int fullMask = (1 << n) - 1;
        const int INF = 1e9;
        vector<vector<int>> dp(1 << n, vector<int>(n, -1));
        
        function<int(int,int)> solve = [&](int mask, int last) -> int {
            if (mask == fullMask) return abs(last - nums[0]);
            int &res = dp[mask][last];
            if (res != -1) return res;
            res = INF;
            for (int nxt = 0; nxt < n; ++nxt) {
                if (!(mask & (1 << nxt))) {
                    int cand = abs(last - nums[nxt]) + solve(mask | (1 << nxt), nxt);
                    if (cand < res) res = cand;
                }
            }
            return res;
        };
        
        int startMask = 1 << 0; // perm[0] = 0
        solve(startMask, 0); // fill dp
        
        vector<int> perm;
        perm.push_back(0);
        int mask = startMask;
        int last = 0;
        while (mask != fullMask) {
            for (int nxt = 1; nxt < n; ++nxt) { // lexicographically smallest, start from 1
                if (!(mask & (1 << nxt))) {
                    int cand = abs(last - nums[nxt]) + solve(mask | (1 << nxt), nxt);
                    if (cand == dp[mask][last]) {
                        perm.push_back(nxt);
                        mask |= (1 << nxt);
                        last = nxt;
                        break;
                    }
                }
            }
        }
        return perm;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] findPermutation(int[] nums) {
        int n = nums.length;
        int[][] w = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                w[i][j] = Math.abs(i - nums[j]);
            }
        }
        int fullMask = (1 << n) - 1;
        int[][] memo = new int[1 << n][n];
        for (int[] row : memo) Arrays.fill(row, -1);

        class Solver {
            int dfs(int mask, int cur) {
                if (mask == fullMask) return w[cur][0];
                if (memo[mask][cur] != -1) return memo[mask][cur];
                int best = Integer.MAX_VALUE / 2;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((mask & (1 << nxt)) == 0) {
                        int cost = w[cur][nxt] + dfs(mask | (1 << nxt), nxt);
                        if (cost < best) best = cost;
                    }
                }
                memo[mask][cur] = best;
                return best;
            }
        }

        Solver solver = new Solver();
        solver.dfs(1, 0); // fill memo

        int[] perm = new int[n];
        perm[0] = 0;
        int mask = 1;
        int cur = 0;
        for (int pos = 1; pos < n; pos++) {
            for (int nxt = 0; nxt < n; nxt++) {
                if ((mask & (1 << nxt)) == 0) {
                    int cost = w[cur][nxt] + solver.dfs(mask | (1 << nxt), nxt);
                    if (cost == memo[mask][cur]) {
                        perm[pos] = nxt;
                        mask |= 1 << nxt;
                        cur = nxt;
                        break;
                    }
                }
            }
        }
        return perm;
    }
}
```

## Python

```python
class Solution(object):
    def findPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        full_mask = (1 << n) - 1
        INF = float('inf')
        dp = [[INF] * n for _ in range(1 << n)]
        path = [[None] * n for _ in range(1 << n)]

        start_mask = 1 << 0
        dp[start_mask][0] = 0
        path[start_mask][0] = (0,)

        # precompute edge weights w[a][b] = |a - nums[b]|
        w = [[abs(a - nums[b]) for b in range(n)] for a in range(n)]

        for mask in range(1 << n):
            if not (mask & start_mask):
                continue
            for last in range(n):
                cur_cost = dp[mask][last]
                if cur_cost == INF:
                    continue
                cur_path = path[mask][last]
                # try to go to next node not visited yet
                remaining = (~mask) & full_mask
                nxt = 0
                while remaining:
                    lsb = remaining & -remaining
                    nxt = (lsb.bit_length() - 1)
                    new_mask = mask | (1 << nxt)
                    new_cost = cur_cost + w[last][nxt]
                    if new_cost < dp[new_mask][nxt]:
                        dp[new_mask][nxt] = new_cost
                        path[new_mask][nxt] = cur_path + (nxt,)
                    elif new_cost == dp[new_mask][nxt]:
                        cand_path = cur_path + (nxt,)
                        if cand_path < path[new_mask][nxt]:
                            path[new_mask][nxt] = cand_path
                    remaining ^= lsb

        best_total = INF
        best_perm = None
        for last in range(n):
            if dp[full_mask][last] == INF:
                continue
            total = dp[full_mask][last] + w[last][0]
            perm = path[full_mask][last]
            if total < best_total or (total == best_total and perm < best_perm):
                best_total = total
                best_perm = perm

        return list(best_perm)
```

## Python3

```python
import sys
from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full_mask = (1 << n) - 1

        # edge weight from i to j : |i - nums[j]|
        w = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                w[i][j] = abs(i - nums[j])

        INF = 10 ** 9
        dp = [[INF] * n for _ in range(1 << n)]

        # base: visit only i and return to 0
        for i in range(n):
            dp[1 << i][i] = w[i][0]

        # DP over subsets
        for mask in range(1, full_mask + 1):
            sub = mask
            while sub:
                i = (sub & -sub).bit_length() - 1
                sub ^= (1 << i)
                if mask == (1 << i):
                    continue
                prev_mask = mask ^ (1 << i)
                best = INF
                pm = prev_mask
                while pm:
                    j = (pm & -pm).bit_length() - 1
                    pm ^= (1 << j)
                    cand = w[i][j] + dp[prev_mask][j]
                    if cand < best:
                        best = cand
                dp[mask][i] = best

        best_total = dp[full_mask][0]

        # Reconstruct lexicographically smallest permutation starting with 0
        path = [0]
        mask = 1 << 0
        last = 0
        cur_cost = 0

        while len(path) < n:
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                new_cost = cur_cost + w[last][nxt]
                rem_mask = full_mask ^ (mask | (1 << nxt))
                total_possible = new_cost + dp[rem_mask | (1 << nxt)][nxt]
                if total_possible == best_total:
                    path.append(nxt)
                    mask |= 1 << nxt
                    last = nxt
                    cur_cost = new_cost
                    break

        return path
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int edgeCost(int u, int v, int *nums) {
    int diff = u - nums[v];
    return diff >= 0 ? diff : -diff;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPermutation(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int fullMask = (1 << n) - 1;
    const int INF = INT_MAX / 4;

    // dp[mask][last] = minimal cost to complete tour from state (mask,last)
    int **dp = (int **)malloc((fullMask + 1) * sizeof(int *));
    for (int i = 0; i <= fullMask; ++i) {
        dp[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) dp[i][j] = INF;
    }

    // Bottom‑up DP over masks in decreasing order
    for (int mask = fullMask; mask >= 0; --mask) {
        for (int last = 0; last < n; ++last) {
            if (!(mask & (1 << last))) continue;
            if (mask == fullMask) {
                dp[mask][last] = edgeCost(last, 0, nums);
            } else {
                int best = INF;
                for (int nxt = 0; nxt < n; ++nxt) {
                    if (mask & (1 << nxt)) continue;
                    int cand = edgeCost(last, nxt, nums) + dp[mask | (1 << nxt)][nxt];
                    if (cand < best) best = cand;
                }
                dp[mask][last] = best;
            }
        }
    }

    int minTotal = dp[1 << 0][0];

    // Reconstruct lexicographically smallest permutation achieving minTotal
    int *perm = (int *)malloc(n * sizeof(int));
    perm[0] = 0;
    int mask = 1 << 0;
    int cur = 0;
    int acc = 0;

    for (int pos = 1; pos < n; ++pos) {
        for (int nxt = 0; nxt < n; ++nxt) {
            if (mask & (1 << nxt)) continue;
            int total = acc + edgeCost(cur, nxt, nums) + dp[mask | (1 << nxt)][nxt];
            if (total == minTotal) {
                perm[pos] = nxt;
                acc += edgeCost(cur, nxt, nums);
                mask |= 1 << nxt;
                cur = nxt;
                break;
            }
        }
    }

    // Free DP memory
    for (int i = 0; i <= fullMask; ++i) free(dp[i]);
    free(dp);

    *returnSize = n;
    return perm;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindPermutation(int[] nums) {
        int n = nums.Length;
        int maxMask = 1 << n;
        const int INF = int.MaxValue / 4;

        int[,] dp = new int[maxMask, n];
        ulong[,] code = new ulong[maxMask, n];
        int[,] pre = new int[maxMask, n];

        for (int mask = 0; mask < maxMask; mask++) {
            for (int i = 0; i < n; i++) {
                dp[mask, i] = INF;
                code[mask, i] = ulong.MaxValue;
                pre[mask, i] = -2; // unreachable
            }
        }

        // Initialize states with first move from 0 to i (i != 0)
        for (int i = 1; i < n; i++) {
            int mask = 1 << i;
            dp[mask, i] = Math.Abs(0 - nums[i]);
            code[mask, i] = (ulong)i;
            pre[mask, i] = -1; // start
        }

        // DP over subsets
        for (int mask = 0; mask < maxMask; mask++) {
            if ((mask & 1) != 0) continue; // bit 0 should never be set
            for (int last = 1; last < n; last++) {
                if (((mask >> last) & 1) == 0) continue;
                int curCost = dp[mask, last];
                if (curCost == INF) continue;

                for (int nxt = 1; nxt < n; nxt++) {
                    if (((mask >> nxt) & 1) != 0) continue;
                    int newMask = mask | (1 << nxt);
                    int add = Math.Abs(last - nums[nxt]);
                    int newCost = curCost + add;
                    ulong newCode = (code[mask, last] << 4) | (ulong)nxt;

                    if (newCost < dp[newMask, nxt] ||
                        (newCost == dp[newMask, nxt] && newCode < code[newMask, nxt])) {
                        dp[newMask, nxt] = newCost;
                        code[newMask, nxt] = newCode;
                        pre[newMask, nxt] = last;
                    }
                }
            }
        }

        int fullMask = ((1 << n) - 1) ^ 1; // all except bit 0
        int bestLast = -1;
        int bestTotal = INF;
        ulong bestCode = ulong.MaxValue;

        for (int last = 1; last < n; last++) {
            if (((fullMask >> last) & 1) == 0) continue;
            int curCost = dp[fullMask, last];
            if (curCost == INF) continue;
            int total = curCost + Math.Abs(last - nums[0]);
            ulong ccode = code[fullMask, last];

            if (total < bestTotal || (total == bestTotal && ccode < bestCode)) {
                bestTotal = total;
                bestLast = last;
                bestCode = ccode;
            }
        }

        // Reconstruct permutation
        int[] perm = new int[n];
        perm[0] = 0;
        List<int> seq = new List<int>();
        int maskCur = fullMask;
        int cur = bestLast;
        while (cur != -1) {
            seq.Add(cur);
            int p = pre[maskCur, cur];
            maskCur ^= (1 << cur);
            cur = p;
        }
        seq.Reverse();
        for (int i = 0; i < seq.Count; i++) {
            perm[i + 1] = seq[i];
        }

        return perm;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findPermutation = function(nums) {
    const n = nums.length;
    const FULL = (1 << n) - 1;
    const INF = 1e9;

    // dpCost[mask][last] = minimal cost to reach 'last' having visited mask
    const dpCost = new Array(1 << n);
    const dpPrev = new Array(1 << n);
    for (let m = 0; m <= FULL; ++m) {
        dpCost[m] = new Float64Array(n);
        dpCost[m].fill(INF);
        dpPrev[m] = new Int16Array(n);
        dpPrev[m].fill(-1);
    }
    dpCost[1 << 0][0] = 0; // start at 0

    const buildPath = (mask, last) => {
        const path = [];
        let curMask = mask;
        let cur = last;
        while (cur !== -1) {
            path.push(cur);
            const prev = dpPrev[curMask][cur];
            if (prev === -1) break;
            curMask ^= (1 << cur);
            cur = prev;
        }
        path.reverse();
        return path;
    };

    for (let mask = 0; mask <= FULL; ++mask) {
        for (let last = 0; last < n; ++last) {
            if ((mask & (1 << last)) === 0) continue;
            const curCost = dpCost[mask][last];
            if (curCost >= INF) continue;
            for (let nxt = 0; nxt < n; ++nxt) {
                if (mask & (1 << nxt)) continue;
                const newMask = mask | (1 << nxt);
                const newCost = curCost + Math.abs(last - nums[nxt]);
                if (newCost < dpCost[newMask][nxt]) {
                    dpCost[newMask][nxt] = newCost;
                    dpPrev[newMask][nxt] = last;
                } else if (newCost === dpCost[newMask][nxt]) {
                    // tie-breaking: choose lexicographically smaller path
                    const candPath = buildPath(mask, last);
                    candPath.push(nxt);
                    const bestPath = buildPath(newMask, nxt); // current stored path
                    let better = false;
                    for (let i = 0; i < candPath.length; ++i) {
                        if (candPath[i] !== bestPath[i]) {
                            better = candPath[i] < bestPath[i];
                            break;
                        }
                    }
                    if (better) dpPrev[newMask][nxt] = last;
                }
            }
        }
    }

    let bestCost = INF;
    let bestPerm = null;

    for (let last = 0; last < n; ++last) {
        const curCost = dpCost[FULL][last];
        if (curCost >= INF) continue;
        const total = curCost + Math.abs(last - nums[0]);
        const perm = buildPath(FULL, last);
        if (total < bestCost) {
            bestCost = total;
            bestPerm = perm;
        } else if (total === bestCost) {
            let better = false;
            for (let i = 0; i < n; ++i) {
                if (perm[i] !== bestPerm[i]) {
                    better = perm[i] < bestPerm[i];
                    break;
                }
            }
            if (better) bestPerm = perm;
        }
    }

    return bestPerm;
};
```

## Typescript

```typescript
function findPermutation(nums: number[]): number[] {
    const n = nums.length;
    const fullMask = (1 << n) - 1;
    const INF = Number.MAX_SAFE_INTEGER;

    const dp: number[][] = Array.from({ length: 1 << n }, () => Array(n).fill(INF));
    const path: (number[] | null)[][] = Array.from({ length: 1 << n }, () => Array(n).fill(null));

    dp[1][0] = 0;
    path[1][0] = [0];

    for (let mask = 0; mask <= fullMask; mask++) {
        for (let last = 0; last < n; last++) {
            const curCost = dp[mask][last];
            if (curCost === INF) continue;
            const curPath = path[mask][last] as number[];
            for (let nxt = 0; nxt < n; nxt++) {
                if ((mask >> nxt) & 1) continue;
                const newMask = mask | (1 << nxt);
                const newCost = curCost + Math.abs(last - nums[nxt]);
                const candPath = curPath.concat(nxt);

                if (newCost < dp[newMask][nxt]) {
                    dp[newMask][nxt] = newCost;
                    path[newMask][nxt] = candPath;
                } else if (newCost === dp[newMask][nxt]) {
                    const existingPath = path[newMask][nxt] as number[];
                    let better = false;
                    for (let i = 0; i < candPath.length; i++) {
                        if (candPath[i] < existingPath[i]) { better = true; break; }
                        else if (candPath[i] > existingPath[i]) { break; }
                    }
                    if (better) path[newMask][nxt] = candPath;
                }
            }
        }
    }

    let bestCost = INF;
    let bestPerm: number[] | null = null;

    for (let last = 0; last < n; last++) {
        const curCost = dp[fullMask][last];
        if (curCost === INF) continue;
        const total = curCost + Math.abs(last - nums[0]);
        const candPath = path[fullMask][last] as number[];
        if (total < bestCost) {
            bestCost = total;
            bestPerm = candPath;
        } else if (total === bestCost && bestPerm) {
            let better = false;
            for (let i = 0; i < n; i++) {
                if (candPath[i] < bestPerm[i]) { better = true; break; }
                else if (candPath[i] > bestPerm[i]) { break; }
            }
            if (better) bestPerm = candPath;
        }
    }

    return bestPerm!;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findPermutation($nums) {
        $n = count($nums);
        $fullMask = (1 << $n) - 1;

        // precompute edge weights w[i][j] = |i - nums[j]|
        $w = [];
        for ($i = 0; $i < $n; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) {
                $row[$j] = abs($i - $nums[$j]);
            }
            $w[$i] = $row;
        }

        $memo = [];

        // lexicographic array comparison
        $compare = function($a, $b) {
            $lenA = count($a);
            $lenB = count($b);
            $len  = min($lenA, $lenB);
            for ($i = 0; $i < $len; $i++) {
                if ($a[$i] < $b[$i]) return -1;
                if ($a[$i] > $b[$i]) return 1;
            }
            if ($lenA == $lenB) return 0;
            return ($lenA < $lenB) ? -1 : 1;
        };

        // DP with memoization returning minimal remaining cost and path
        $dfs = function($mask, $cur) use (&$dfs, &$memo, $n, $fullMask, $w, $compare) {
            if (isset($memo[$mask][$cur])) {
                return $memo[$mask][$cur];
            }
            if ($mask == $fullMask) {
                // only need to go back to start (0)
                $res = ['cost' => $w[$cur][0], 'path' => []];
                $memo[$mask][$cur] = $res;
                return $res;
            }

            $bestCost = PHP_INT_MAX;
            $bestPath = null;

            for ($j = 0; $j < $n; $j++) {
                if (($mask >> $j) & 1) continue; // already visited
                $sub   = $dfs($mask | (1 << $j), $j);
                $total = $w[$cur][$j] + $sub['cost'];

                if ($total < $bestCost) {
                    $bestCost = $total;
                    $bestPath = array_merge([$j], $sub['path']);
                } elseif ($total == $bestCost) {
                    $candidate = array_merge([$j], $sub['path']);
                    if ($compare($candidate, $bestPath) < 0) {
                        $bestPath = $candidate;
                    }
                }
            }

            $res = ['cost' => $bestCost, 'path' => $bestPath];
            $memo[$mask][$cur] = $res;
            return $res;
        };

        // start from node 0
        $startMask = 1 << 0;
        $result    = $dfs($startMask, 0);
        $perm      = array_merge([0], $result['path']);
        return $perm;
    }
}
```

## Swift

```swift
class Solution {
    func findPermutation(_ nums: [Int]) -> [Int] {
        let n = nums.count
        let fullMask = (1 << n) - 1
        var memo = Array(repeating: Array(repeating: -1, count: n), count: 1 << n)
        
        func remainingCost(_ mask: Int, _ last: Int) -> Int {
            if memo[mask][last] != -1 { return memo[mask][last] }
            if mask == fullMask {
                let cost = abs(last - nums[0])
                memo[mask][last] = cost
                return cost
            }
            var best = Int.max / 2
            for next in 0..<n where (mask & (1 << next)) == 0 {
                let c = abs(last - nums[next]) + remainingCost(mask | (1 << next), next)
                if c < best { best = c }
            }
            memo[mask][last] = best
            return best
        }
        
        let startMask = 1 << 0
        let bestCost = remainingCost(startMask, 0)
        
        var mask = startMask
        var last = 0
        var curCost = 0
        var perm: [Int] = [0]
        
        while mask != fullMask {
            for next in 0..<n where (mask & (1 << next)) == 0 {
                let edge = abs(last - nums[next])
                let total = curCost + edge + remainingCost(mask | (1 << next), next)
                if total == bestCost {
                    perm.append(next)
                    curCost += edge
                    mask |= (1 << next)
                    last = next
                    break
                }
            }
        }
        
        return perm
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPermutation(nums: IntArray): IntArray {
        val n = nums.size
        val fullMask = (1 shl n) - 1

        // Precompute costs: cost[i][j] = |i - nums[j]|
        val cost = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                cost[i][j] = kotlin.math.abs(i - nums[j])
            }
        }

        // dp[mask][last] = minimal additional cost to finish the cycle
        val dp = Array(1 shl n) { IntArray(n) { -1 } }

        fun dfs(mask: Int, last: Int): Int {
            if (dp[mask][last] != -1) return dp[mask][last]
            if (mask == fullMask) {
                dp[mask][last] = cost[last][0] // return to start
                return dp[mask][last]
            }
            var best = Int.MAX_VALUE / 2
            var remaining = fullMask xor mask
            while (remaining != 0) {
                val bit = remaining and -remaining
                val nxt = Integer.numberOfTrailingZeros(bit)
                val cand = cost[last][nxt] + dfs(mask or bit, nxt)
                if (cand < best) best = cand
                remaining -= bit
            }
            dp[mask][last] = best
            return best
        }

        // Compute minimal total cost starting from 0
        dfs(1 shl 0, 0)

        // Reconstruct lexicographically smallest permutation achieving the minimal cost
        val result = IntArray(n)
        result[0] = 0
        var idx = 1
        var mask = 1 shl 0
        var last = 0
        while (mask != fullMask) {
            val curBest = dp[mask][last]
            for (nxt in 0 until n) {
                if ((mask and (1 shl nxt)) == 0) {
                    val nextMask = mask or (1 shl nxt)
                    val cand = cost[last][nxt] + dp[nextMask][nxt]
                    if (cand == curBest) {
                        result[idx++] = nxt
                        mask = nextMask
                        last = nxt
                        break
                    }
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findPermutation(List<int> nums) {
    int n = nums.length;
    // Precompute weight matrix w[i][j] = |i - nums[j]|
    List<List<int>> w = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        w[i][j] = (i - nums[j]).abs();
      }
    }

    int fullMask = (1 << n) - 1;
    const int INF = 1 << 30;

    // memo[mask][i] = minimal additional cost to finish tour starting at i with visited mask
    List<List<int>> memo =
        List.generate(1 << n, (_) => List.filled(n, -1));

    int solve(int mask, int cur) {
      if (mask == fullMask) {
        return w[cur][0]; // return to start
      }
      if (memo[mask][cur] != -1) return memo[mask][cur];
      int best = INF;
      for (int nxt = 0; nxt < n; ++nxt) {
        if ((mask & (1 << nxt)) == 0) {
          int cost = w[cur][nxt] + solve(mask | (1 << nxt), nxt);
          if (cost < best) best = cost;
        }
      }
      memo[mask][cur] = best;
      return best;
    }

    // Start from node 0
    int startMask = 1 << 0;
    solve(startMask, 0); // fill memo

    List<int> perm = [0];
    int mask = startMask;
    int cur = 0;
    while (mask != fullMask) {
      for (int nxt = 0; nxt < n; ++nxt) {
        if ((mask & (1 << nxt)) == 0) {
          int cost = w[cur][nxt] + solve(mask | (1 << nxt), nxt);
          if (cost == solve(mask, cur)) {
            perm.add(nxt);
            mask |= (1 << nxt);
            cur = nxt;
            break;
          }
        }
      }
    }
    return perm;
  }
}
```

## Golang

```go
func findPermutation(nums []int) []int {
    n := len(nums)
    const INF = int(1 << 60)

    // precompute cost[i][j] = |i - nums[j]|
    cost := make([][]int, n)
    for i := 0; i < n; i++ {
        cost[i] = make([]int, n)
        for j := 0; j < n; j++ {
            diff := i - nums[j]
            if diff < 0 {
                diff = -diff
            }
            cost[i][j] = diff
        }
    }

    size := 1 << n
    dp := make([][]int, size)
    for i := 0; i < size; i++ {
        dp[i] = make([]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = INF
        }
    }
    dp[1<<0][0] = 0

    for mask := 0; mask < size; mask++ {
        if (mask&1) == 0 { // must contain node 0 to be reachable
            continue
        }
        for last := 0; last < n; last++ {
            cur := dp[mask][last]
            if cur == INF {
                continue
            }
            for nxt := 0; nxt < n; nxt++ {
                if mask&(1<<nxt) != 0 {
                    continue
                }
                newMask := mask | (1 << nxt)
                nd := cur + cost[last][nxt]
                if nd < dp[newMask][nxt] {
                    dp[newMask][nxt] = nd
                }
            }
        }
    }

    fullMask := size - 1
    minCost := INF
    for last := 0; last < n; last++ {
        total := dp[fullMask][last] + cost[last][0]
        if total < minCost {
            minCost = total
        }
    }

    // memoization for remaining cost to finish tour from a state
    memo := make([][]int, size)
    for i := 0; i < size; i++ {
        memo[i] = make([]int, n)
        for j := 0; j < n; j++ {
            memo[i][j] = -1
        }
    }

    var dfs func(mask, last int) int
    dfs = func(mask, last int) int {
        if mask == fullMask {
            return cost[last][0]
        }
        if memo[mask][last] != -1 {
            return memo[mask][last]
        }
        best := INF
        for nxt := 0; nxt < n; nxt++ {
            if mask&(1<<nxt) != 0 {
                continue
            }
            cand := cost[last][nxt] + dfs(mask|1<<nxt, nxt)
            if cand < best {
                best = cand
            }
        }
        memo[mask][last] = best
        return best
    }

    // reconstruct lexicographically smallest optimal permutation starting with 0
    res := make([]int, n)
    res[0] = 0
    mask := 1 << 0
    last := 0
    for pos := 1; pos < n; pos++ {
        for nxt := 0; nxt < n; nxt++ {
            if mask&(1<<nxt) != 0 {
                continue
            }
            newMask := mask | (1 << nxt)
            // check that this edge can be part of an optimal tour
            if dp[newMask][nxt] == dp[mask][last]+cost[last][nxt] && dp[newMask][nxt]+dfs(newMask, nxt) == minCost {
                res[pos] = nxt
                mask = newMask
                last = nxt
                break
            }
        }
    }
    return res
}
```

## Ruby

```ruby
def find_permutation(nums)
  n = nums.length
  full_mask = (1 << n) - 1
  # precompute edge weights w[a][b] = |a - nums[b]|
  w = Array.new(n) { Array.new(n, 0) }
  n.times do |a|
    n.times do |b|
      w[a][b] = (a - nums[b]).abs
    end
  end

  INF = 1 << 60
  memo = Array.new(1 << n) { Array.new(n) }

  dfs = nil
  dfs = ->(mask, last) {
    cached = memo[mask][last]
    return cached unless cached.nil?
    if mask == full_mask
      val = w[last][0] # return to start
    else
      best = INF
      n.times do |nxt|
        next if (mask & (1 << nxt)) != 0
        cost = w[last][nxt] + dfs.call(mask | (1 << nxt), nxt)
        best = cost if cost < best
      end
      val = best
    end
    memo[mask][last] = val
    val
  }

  # minimal total cost starting from 0 with only 0 visited
  dfs.call(1 << 0, 0)

  perm = [0]
  mask = 1 << 0
  cur = 0
  while mask != full_mask
    n.times do |nxt|
      next if (mask & (1 << nxt)) != 0
      if w[cur][nxt] + dfs.call(mask | (1 << nxt), nxt) == dfs.call(mask, cur)
        perm << nxt
        mask |= (1 << nxt)
        cur = nxt
        break
      end
    end
  end

  perm
end
```

## Scala

```scala
object Solution {
    def findPermutation(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val fullMask = (1 << n) - 1
        val INF = Int.MaxValue / 4

        // precompute edge weights w(u,v) = |u - nums[v]|
        val w = Array.ofDim[Int](n, n)
        var i = 0
        while (i < n) {
            var j = 0
            while (j < n) {
                w(i)(j) = math.abs(i - nums(j))
                j += 1
            }
            i += 1
        }

        // dp[mask][last] = minimal additional cost to start at 'last',
        // having visited exactly the nodes in mask, and eventually return to 0
        val size = 1 << n
        val dp = Array.fill(size, n)(INF)

        // base case: all nodes visited, just go back to 0
        var last = 0
        while (last < n) {
            dp(fullMask)(last) = w(last)(0)
            last += 1
        }

        // fill DP for masks in decreasing order
        var mask = fullMask - 1
        while (mask >= 0) {
            i = 0
            while (i < n) {
                if (((mask >> i) & 1) == 1) { // i is in mask, can be 'last'
                    var best = INF
                    var nxt = 0
                    var notVisitedMask = (~mask) & fullMask
                    var j = 0
                    while (j < n) {
                        if (((notVisitedMask >> j) & 1) == 1) {
                            val cand = w(i)(j) + dp(mask | (1 << j))(j)
                            if (cand < best) best = cand
                        }
                        j += 1
                    }
                    // when mask is full, loop above doesn't run; value already set.
                    dp(mask)(i) = best
                }
                i += 1
            }
            mask -= 1
        }

        // reconstruct lexicographically smallest optimal permutation starting with 0
        val perm = new Array[Int](n)
        perm(0) = 0
        var curMask = 1 << 0
        var curLast = 0
        var pos = 1
        while (pos < n) {
            var chosen = -1
            var nxtIdx = 0
            var found = false
            while (nxtIdx < n && !found) {
                if (((curMask >> nxtIdx) & 1) == 0) { // not visited yet
                    val cand = w(curLast)(nxtIdx) + dp(curMask | (1 << nxtIdx))(nxtIdx)
                    if (cand == dp(curMask)(curLast)) {
                        chosen = nxtIdx
                        found = true
                    }
                }
                nxtIdx += 1
            }
            perm(pos) = chosen
            curMask |= 1 << chosen
            curLast = chosen
            pos += 1
        }

        perm
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_permutation(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let full_mask: usize = (1usize << n) - 1;
        const INF: i32 = i32::MAX / 2;

        // dp[mask][last] = minimal cost to start at 0, visit 'mask' (including last), end at 'last',
        // and eventually return to 0 after visiting all nodes.
        let mut dp = vec![vec![INF; n]; full_mask + 1];

        // Base case: when all nodes are visited, need to go back to start (0)
        for last in 0..n {
            dp[full_mask][last] = ((last as i32) - nums[0]).abs();
        }

        // Fill DP for masks with decreasing number of bits
        for mask in (0..full_mask).rev() {
            if (mask & 1) == 0 { continue; } // start node (0) must be included in all reachable states
            for last in 0..n {
                if (mask & (1 << last)) == 0 { continue; }
                let mut best = INF;
                for nxt in 0..n {
                    if (mask & (1 << nxt)) != 0 { continue; }
                    let edge = ((last as i32) - nums[nxt]).abs();
                    let cand = edge + dp[mask | (1 << nxt)][nxt];
                    if cand < best {
                        best = cand;
                    }
                }
                dp[mask][last] = best;
            }
        }

        // Reconstruct lexicographically smallest permutation starting with 0
        let mut perm: Vec<i32> = Vec::with_capacity(n);
        perm.push(0);
        let mut mask: usize = 1; // only node 0 visited
        let mut last: usize = 0;

        while mask != full_mask {
            for nxt in 0..n {
                if (mask & (1 << nxt)) != 0 { continue; }
                let edge = ((last as i32) - nums[nxt]).abs();
                let total = edge + dp[mask | (1 << nxt)][nxt];
                if total == dp[mask][last] {
                    perm.push(nxt as i32);
                    mask |= 1 << nxt;
                    last = nxt;
                    break;
                }
            }
        }

        perm
    }
}
```

## Racket

```racket
(define/contract (find-permutation nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (mask-count (arithmetic-shift 1 (sub1 n))) ; 2^(n-1)
         (full-mask (sub1 mask-count))            ; all bits set for nodes 1..n-1
         ;; dpCost[mask][last] = minimal cost, INF if unreachable
         (dp-cost (make-vector mask-count))
         ;; dpPath[mask][last] = best path list from first after 0 up to last
         (dp-path (make-vector mask-count)))
    ;; initialise inner vectors
    (for ([m mask-count])
      (vector-set! dp-cost m (make-vector n +inf.0))
      (vector-set! dp-path m (make-vector n #f)))
    ;; weight matrix w[i][j] = |i - nums[j]|
    (define w (let ((mat (make-vector n)))
                (for ([i n])
                  (let ((row (make-vector n 0)))
                    (for ([j n])
                      (vector-set! row j (abs (- i (list-ref nums j)))))
                    (vector-set! mat i row)))
                mat))
    ;; helpers
    (define (bit i) (arithmetic-shift 1 i))
    (define (bit-set? mask idx)
      (not (= 0 (bitwise-and mask (bit idx)))))
    (define (lexicographic-less? a b)
      (let loop ((as a) (bs b))
        (cond [(null? as) #f] ; equal
              [(null? bs) #f]
              [else (let ((x (car as)) (y (car bs)))
                      (if (< x y) #t
                          (if (> x y) #f
                              (loop (cdr as) (cdr bs)))))])))
    ;; initialise states with first move from 0 to i
    (for ([i (in-range 1 n)])
      (let* ((mask (bit (sub1 i)))               ; bit for node i
             (cost (vector-ref (vector-ref w 0) i))
             (inner-cost (vector-ref dp-cost mask))
             (inner-path (vector-ref dp-path mask)))
        (vector-set! inner-cost i cost)
        (vector-set! inner-path i (list i))))
    ;; DP over subsets
    (for ([mask (in-range mask-count)])
      (for ([last (in-range 1 n)])
        (let ((curCost (vector-ref (vector-ref dp-cost mask) last)))
          (when (< curCost +inf.0)
            (define curPath (vector-ref (vector-ref dp-path mask) last))
            (for ([next (in-range 1 n)])
              (unless (bit-set? mask (sub1 next)) ; not visited yet
                (let* ((newMask (bitwise-ior mask (bit (sub1 next))))
                       (newCost (+ curCost (vector-ref (vector-ref w last) next)))
                       (inner-cost (vector-ref dp-cost newMask))
                       (inner-path (vector-ref dp-path newMask))
                       (oldCost (vector-ref inner-cost next))
                       (candidatePath (append curPath (list next))))
                  (cond [(< newCost oldCost)
                         (vector-set! inner-cost next newCost)
                         (vector-set! inner-path next candidatePath)]
                        [(= newCost oldCost)
                         (define oldPath (vector-ref inner-path next))
                         (when (or (not oldPath) (lexicographic-less? candidatePath oldPath))
                           (vector-set! inner-path next candidatePath))])))))))))
    ;; choose best final permutation
    (let ((best-cost +inf.0)
          (best-perm #f))
      (for ([last (in-range 1 n)])
        (let ((cost (vector-ref (vector-ref dp-cost full-mask) last)))
          (when (< cost +inf.0)
            (define total (+ cost (vector-ref (vector-ref w last) 0))) ; return to 0
            (define path (vector-ref (vector-ref dp-path full-mask) last))
            (define perm (cons 0 path)) ; final permutation
            (cond [(> best-cost total)
                   (set! best-cost total)
                   (set! best-perm perm)]
                  [(= best-cost total)
                   (when (lexicographic-less? perm best-perm)
                     (set! best-perm perm))]))))
      best-perm)))
```

## Erlang

```erlang
-export([find_permutation/1]).

find_permutation(Nums) ->
    N = length(Nums),
    NumTuple = list_to_tuple(Nums),
    MaxMask = (1 bsl N) - 1,
    InitDP = maps:put({1 bsl 0, 0}, {0, [0]}, maps:new()),
    DP = process_masks(N, NumTuple, MaxMask, 0, InitDP),
    {_Cost, BestPath} = find_best(N, NumTuple, MaxMask, DP, undefined),
    BestPath.

process_masks(_N, _NumTuple, MaxMask, Mask, DP) when Mask > MaxMask ->
    DP;
process_masks(N, NumTuple, MaxMask, Mask, DP) ->
    DP1 = process_mask_last(N, NumTuple, Mask, 0, DP),
    process_masks(N, NumTuple, MaxMask, Mask + 1, DP1).

process_mask_last(_N, _NumTuple, _Mask, Last, DP) when Last >= _N ->
    DP;
process_mask_last(N, NumTuple, Mask, Last, DP) ->
    case maps:find({Mask, Last}, DP) of
        {ok, {Cost, Path}} ->
            DP2 = expand_from_state(N, NumTuple, Mask, Last, Cost, Path, DP),
            process_mask_last(N, NumTuple, Mask, Last + 1, DP2);
        error ->
            process_mask_last(N, NumTuple, Mask, Last + 1, DP)
    end.

expand_from_state(N, NumTuple, Mask, Last, Cost, Path, DP) ->
    expand_next(0, N, NumTuple, Mask, Last, Cost, Path, DP).

expand_next(Next, N, _NumTuple, _Mask, _Last, _Cost, _Path, DP) when Next >= N ->
    DP;
expand_next(Next, N, NumTuple, Mask, Last, Cost, Path, DP) ->
    case (Mask band (1 bsl Next)) of
        0 ->
            NewMask = Mask bor (1 bsl Next),
            W = erlang:abs(Last - element(Next + 1, NumTuple)),
            NewCost = Cost + W,
            NewPath = Path ++ [Next],
            Key = {NewMask, Next},
            DP1 = case maps:find(Key, DP) of
                {ok, {OldCost, OldPath}} ->
                    if NewCost < OldCost orelse (NewCost == OldCost andalso lexicographically_smaller(NewPath, OldPath)) ->
                        maps:put(Key, {NewCost, NewPath}, DP);
                       true -> DP
                    end;
                error ->
                    maps:put(Key, {NewCost, NewPath}, DP)
            end,
            expand_next(Next + 1, N, NumTuple, Mask, Last, Cost, Path, DP1);
        _ ->
            expand_next(Next + 1, N, NumTuple, Mask, Last, Cost, Path, DP)
    end.

find_best(N, NumTuple, FullMask, DP, undefined) ->
    find_best_last(0, N - 1, NumTuple, FullMask, DP, undefined);
find_best(N, NumTuple, FullMask, DP, CurrentBest) ->
    find_best_last(0, N - 1, NumTuple, FullMask, DP, CurrentBest).

find_best_last(L, MaxL, _NumTuple, _FullMask, _DP, Best) when L > MaxL ->
    Best;
find_best_last(L, MaxL, NumTuple, FullMask, DP, Best) ->
    case maps:find({FullMask, L}, DP) of
        {ok, {Cost, Path}} ->
            Total = Cost + erlang:abs(L - element(1, NumTuple)),
            NewBest = case Best of
                undefined -> {Total, Path};
                {BestCost, BestPath} ->
                    if Total < BestCost orelse (Total == BestCost andalso lexicographically_smaller(Path, BestPath)) ->
                        {Total, Path};
                       true -> {BestCost, BestPath}
                    end
            end,
            find_best_last(L + 1, MaxL, NumTuple, FullMask, DP, NewBest);
        error ->
            find_best_last(L + 1, MaxL, NumTuple, FullMask, DP, Best)
    end.

lexicographically_smaller([A|RestA], [B|RestB]) when A < B -> true;
lexicographically_smaller([A|RestA], [B|RestB]) when A > B -> false;
lexicographically_smaller([A|RestA], [A|RestB]) ->
    lexicographically_smaller(RestA, RestB);
lexicographically_smaller(_, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec find_permutation(nums :: [integer]) :: [integer]
  def find_permutation(nums) do
    n = length(nums)
    full_mask = (1 <<< n) - 1

    w_map =
      for i <- 0..(n - 1), j <- 0..(n - 1), into: %{} do
        {{i, j}, abs(i - Enum.at(nums, j))}
      end

    dp = build_dp(n, full_mask, w_map)
    build_perm(1 <<< 0, 0, [0], full_mask, n, w_map, dp)
  end

  defp build_dp(n, full_mask, w_map) do
    Enum.reduce(full_mask..0, %{}, fn mask, acc ->
      Enum.reduce(0..(n - 1), acc, fn last, acc2 ->
        if (mask &&& (1 <<< last)) != 0 do
          val =
            if mask == full_mask do
              Map.fetch!(w_map, {last, 0})
            else
              Enum.reduce(0..(n - 1), :infinity, fn nxt, cur_min ->
                if (mask &&& (1 <<< nxt)) == 0 do
                  next_mask = mask ||| (1 <<< nxt)
                  candidate =
                    Map.fetch!(w_map, {last, nxt}) + Map.get(acc2, {next_mask, nxt})
                  if candidate < cur_min, do: candidate, else: cur_min
                else
                  cur_min
                end
              end)
            end

          Map.put(acc2, {mask, last}, val)
        else
          acc2
        end
      end)
    end)
  end

  defp build_perm(mask, last, acc, full_mask, n, w_map, dp) do
    if mask == full_mask do
      Enum.reverse(acc)
    else
      chosen =
        Enum.find(0..(n - 1), fn nxt ->
          (mask &&& (1 <<< nxt)) == 0 and
            (Map.fetch!(w_map, {last, nxt}) +
               Map.get(dp, {mask ||| (1 <<< nxt), nxt})) ==
              Map.get(dp, {mask, last})
        end)

      build_perm(mask ||| (1 <<< chosen), chosen, [chosen | acc], full_mask, n, w_map, dp)
    end
  end
end
```
