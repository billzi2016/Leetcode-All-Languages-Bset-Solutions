# 1478. Allocate Mailboxes

## Cpp

```cpp
class Solution {
public:
    int minDistance(vector<int>& houses, int k) {
        sort(houses.begin(), houses.end());
        int n = houses.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + houses[i];
        
        vector<vector<int>> cost(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int mid = (i + j) / 2;
                long long left = 1LL * houses[mid] * (mid - i) - (pref[mid] - pref[i]);
                long long right = (pref[j + 1] - pref[mid + 1]) - 1LL * houses[mid] * (j - mid);
                cost[i][j] = (int)(left + right);
            }
        }
        
        const int INF = 1e9;
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, INF));
        dp[0][0] = 0;
        for (int t = 1; t <= k; ++t) {
            for (int m = 1; m <= n; ++m) {
                // we need at least t houses to place t mailboxes
                for (int p = t - 1; p < m; ++p) {
                    if (dp[t - 1][p] == INF) continue;
                    dp[t][m] = min(dp[t][m], dp[t - 1][p] + cost[p][m - 1]);
                }
            }
        }
        return dp[k][n];
    }
};
```

## Java

```java
class Solution {
    public int minDistance(int[] houses, int k) {
        int n = houses.length;
        java.util.Arrays.sort(houses);
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + houses[i];
        }

        int[][] cost = new int[n][n];
        for (int l = 0; l < n; l++) {
            for (int r = l; r < n; r++) {
                int m = (l + r) / 2;
                int left = houses[m] * (m - l) - (prefix[m] - prefix[l]);
                int right = (prefix[r + 1] - prefix[m + 1]) - houses[m] * (r - m);
                cost[l][r] = left + right;
            }
        }

        final int INF = 1_000_000_000;
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 0; i <= n; i++) {
            java.util.Arrays.fill(dp[i], INF);
        }
        dp[0][0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int p = 1; p <= Math.min(k, i); p++) {
                for (int t = p - 1; t < i; t++) {
                    dp[i][p] = Math.min(dp[i][p], dp[t][p - 1] + cost[t][i - 1]);
                }
            }
        }

        return dp[n][k];
    }
}
```

## Python

```python
class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        houses.sort()
        n = len(houses)
        # prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + houses[i]

        # cost[i][j]: min total distance for houses i..j with one mailbox
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                m = (i + j) // 2
                median = houses[m]
                left_cnt = m - i
                left_sum = pref[m] - pref[i]
                right_cnt = j - m
                right_sum = pref[j + 1] - pref[m + 1]
                cost[i][j] = median * left_cnt - left_sum + right_sum - median * right_cnt

        INF = 10 ** 9
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for t in range(1, k + 1):
            for i in range(1, n + 1):
                # try placing the t-th mailbox covering houses p..i-1
                best = INF
                for p in range(t - 1, i):  # need at least t-1 houses before to place previous mailboxes
                    cur = dp[t - 1][p] + cost[p][i - 1]
                    if cur < best:
                        best = cur
                dp[t][i] = best

        return dp[k][n]
```

## Python3

```python
from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + houses[i]

        # cost[i][j]: min total distance for houses i..j with one mailbox
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                left = houses[mid] * (mid - i) - (pref[mid] - pref[i])
                right = (pref[j + 1] - pref[mid + 1]) - houses[mid] * (j - mid)
                cost[i][j] = left + right

        INF = 10 ** 18
        dp = [[INF] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = cost[0][i]

        for m in range(2, k + 1):
            for i in range(m - 1, n):
                best = INF
                # previous split point p ends the (m-1)th mailbox segment
                for p in range(m - 2, i):
                    val = dp[p][m - 1] + cost[p + 1][i]
                    if val < best:
                        best = val
                dp[i][m] = best

        return dp[n - 1][k]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int minDistance(int* houses, int housesSize, int k) {
    if (housesSize == 0) return 0;
    // copy and sort
    int *h = (int *)malloc(sizeof(int) * housesSize);
    for (int i = 0; i < housesSize; ++i) h[i] = houses[i];
    qsort(h, housesSize, sizeof(int), cmp_int);

    // prefix sums
    long long *pref = (long long *)malloc(sizeof(long long) * housesSize);
    pref[0] = h[0];
    for (int i = 1; i < housesSize; ++i) pref[i] = pref[i-1] + h[i];

    // cost[i][j]: min distance to serve houses i..j with one mailbox
    int **cost = (int **)malloc(sizeof(int*) * housesSize);
    for (int i = 0; i < housesSize; ++i) {
        cost[i] = (int *)malloc(sizeof(int) * housesSize);
    }

    for (int i = 0; i < housesSize; ++i) {
        for (int j = i; j < housesSize; ++j) {
            int m = (i + j) / 2;
            long long leftSum = (m > i) ? pref[m-1] - (i>0?pref[i-1]:0) : 0;
            long long rightSum = pref[j] - pref[m];
            long long leftCost = (long long)h[m] * (m - i) - leftSum;
            long long rightCost = rightSum - (long long)h[m] * (j - m);
            cost[i][j] = (int)(leftCost + rightCost);
        }
    }

    // dp[p][i]: min distance for first i+1 houses with p mailboxes
    int **dp = (int **)malloc(sizeof(int*) * (k+1));
    for (int p = 0; p <= k; ++p) {
        dp[p] = (int *)malloc(sizeof(int) * housesSize);
        for (int i = 0; i < housesSize; ++i) dp[p][i] = INT_MAX/2;
    }

    // base case: one mailbox
    for (int i = 0; i < housesSize; ++i) {
        dp[1][i] = cost[0][i];
    }

    for (int p = 2; p <= k; ++p) {
        for (int i = p-1; i < housesSize; ++i) { // need at least p houses
            int best = INT_MAX/2;
            for (int t = p-2; t < i; ++t) {
                int cand = dp[p-1][t] + cost[t+1][i];
                if (cand < best) best = cand;
            }
            dp[p][i] = best;
        }
    }

    int result = dp[k][housesSize-1];

    // free memory
    for (int i = 0; i < housesSize; ++i) free(cost[i]);
    free(cost);
    for (int p = 0; p <= k; ++p) free(dp[p]);
    free(dp);
    free(pref);
    free(h);

    return result;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinDistance(int[] houses, int k) {
        int n = houses.Length;
        if (k >= n) return 0;
        Array.Sort(houses);
        long[] prefix = new long[n];
        for (int i = 0; i < n; i++) {
            prefix[i] = houses[i] + (i > 0 ? prefix[i - 1] : 0);
        }
        int[,] cost = new int[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int m = (i + j) / 2;
                long leftSum = (m > i) ? Sum(prefix, i, m - 1) : 0;
                long rightSum = (j > m) ? Sum(prefix, m + 1, j) : 0;
                long leftCost = (long)houses[m] * (m - i) - leftSum;
                long rightCost = rightSum - (long)houses[m] * (j - m);
                cost[i, j] = (int)(leftCost + rightCost);
            }
        }

        int maxK = Math.Min(k, n);
        int[,] dp = new int[maxK + 1, n];
        const int INF = int.MaxValue / 2;
        for (int t = 0; t <= maxK; t++) {
            for (int i = 0; i < n; i++) dp[t, i] = INF;
        }

        for (int p = 0; p < n; p++) {
            dp[1, p] = cost[0, p];
        }

        for (int t = 2; t <= maxK; t++) {
            for (int p = t - 1; p < n; p++) {
                int best = INF;
                for (int s = t - 2; s < p; s++) {
                    int val = dp[t - 1, s] + cost[s + 1, p];
                    if (val < best) best = val;
                }
                dp[t, p] = best;
            }
        }

        return dp[maxK, n - 1];
    }

    private long Sum(long[] prefix, int l, int r) {
        return prefix[r] - (l > 0 ? prefix[l - 1] : 0);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} houses
 * @param {number} k
 * @return {number}
 */
var minDistance = function(houses, k) {
    houses.sort((a, b) => a - b);
    const n = houses.length;
    if (k >= n) return 0;

    // prefix sums of house positions
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + houses[i];
    }

    // cost[i][j]: min total distance for houses i..j with one mailbox
    const cost = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        for (let j = i; j < n; ++j) {
            const m = Math.floor((i + j) / 2);
            // left side
            const leftCount = m - i;
            const leftSum = prefix[m] - prefix[i];
            const leftCost = houses[m] * leftCount - leftSum;
            // right side
            const rightCount = j - m;
            const rightSum = prefix[j + 1] - prefix[m + 1];
            const rightCost = rightSum - houses[m] * rightCount;
            cost[i][j] = leftCost + rightCost;
        }
    }

    const INF = 1e15;
    // dp[i][c]: min distance for first i houses using c mailboxes
    const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(INF));
    dp[0][0] = 0;

    for (let i = 1; i <= n; ++i) {
        for (let c = 1; c <= k; ++c) {
            // partition point t: first t houses use c-1 mailboxes, rest [t..i-1] use one mailbox
            for (let t = c - 1; t < i; ++t) {
                const val = dp[t][c - 1] + cost[t][i - 1];
                if (val < dp[i][c]) dp[i][c] = val;
            }
        }
    }

    return dp[n][k];
};
```

## Typescript

```typescript
function minDistance(houses: number[], k: number): number {
    houses.sort((a, b) => a - b);
    const n = houses.length;
    const cost: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            const mid = Math.floor((i + j) / 2);
            let sum = 0;
            for (let t = i; t <= j; t++) {
                sum += Math.abs(houses[t] - houses[mid]);
            }
            cost[i][j] = sum;
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dp: number[][] = Array.from({ length: k + 1 }, () => Array(n + 1).fill(INF));
    dp[0][0] = 0;

    for (let p = 1; p <= k; p++) {
        for (let i = 1; i <= n; i++) {
            for (let t = 0; t < i; t++) {
                if (dp[p - 1][t] === INF) continue;
                const cur = dp[p - 1][t] + cost[t][i - 1];
                if (cur < dp[p][i]) dp[p][i] = cur;
            }
        }
    }

    return dp[k][n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $houses
     * @param Integer $k
     * @return Integer
     */
    function minDistance($houses, $k) {
        sort($houses);
        $n = count($houses);

        // Prefix sums of house positions
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $houses[$i];
        }

        // Precompute cost[i][j]: minimal distance for houses i..j with one mailbox
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i; $j < $n; $j++) {
                $mid = intdiv($i + $j, 2);
                $leftCount = $mid - $i;
                $rightCount = $j - $mid;

                $leftSum = $prefix[$mid] - $prefix[$i];
                $rightSum = $prefix[$j + 1] - $prefix[$mid + 1];

                $cost[$i][$j] = ($houses[$mid] * $leftCount - $leftSum) +
                                ($rightSum - $houses[$mid] * $rightCount);
            }
        }

        // DP: dp[i][c] = min distance for first i houses using c mailboxes
        $INF = 1 << 60;
        $dp = array_fill(0, $n + 1, array_fill(0, $k + 1, $INF));
        $dp[0][0] = 0;

        for ($i = 1; $i <= $n; $i++) {
            $maxC = min($k, $i);
            for ($c = 1; $c <= $maxC; $c++) {
                // previous split point t (number of houses before the last segment)
                for ($t = $c - 1; $t < $i; $t++) {
                    if ($dp[$t][$c - 1] === $INF) continue;
                    $candidate = $dp[$t][$c - 1] + $cost[$t][$i - 1];
                    if ($candidate < $dp[$i][$c]) {
                        $dp[$i][$c] = $candidate;
                    }
                }
            }
        }

        return $dp[$n][$k];
    }
}
```

## Swift

```swift
class Solution {
    func minDistance(_ houses: [Int], _ k: Int) -> Int {
        let sorted = houses.sorted()
        let n = sorted.count
        if k >= n { return 0 }
        
        // Precompute cost[i][j]: minimal distance for houses i...j with one mailbox
        var cost = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in i..<n {
                let mid = (i + j) / 2
                var sum = 0
                for t in i...j {
                    sum += abs(sorted[t] - sorted[mid])
                }
                cost[i][j] = sum
            }
        }
        
        let INF = Int.max / 2
        // dp[i][m]: min distance for first i+1 houses using m mailboxes
        var dp = Array(repeating: Array(repeating: INF, count: k + 1), count: n)
        
        // Base case: one mailbox
        for i in 0..<n {
            dp[i][1] = cost[0][i]
        }
        
        if k == 1 { return dp[n - 1][1] }
        
        if k > 1 {
            for m in 2...k {
                for i in 0..<n {
                    // Need at least m houses to place m mailboxes
                    if i + 1 < m { continue }
                    var best = INF
                    // previous split point p, where first p+1 houses use m-1 mailboxes,
                    // and houses (p+1)...i use the last mailbox
                    for p in (m - 2)..<i {
                        let candidate = dp[p][m - 1] + cost[p + 1][i]
                        if candidate < best {
                            best = candidate
                        }
                    }
                    dp[i][m] = best
                }
            }
        }
        
        return dp[n - 1][k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDistance(houses: IntArray, k: Int): Int {
        val n = houses.size
        val a = houses.clone()
        a.sort()
        // prefix sums
        val pre = IntArray(n + 1)
        for (i in 0 until n) {
            pre[i + 1] = pre[i] + a[i]
        }
        // cost[i][j]: min distance for houses i..j with one mailbox
        val cost = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in i until n) {
                val m = (i + j) / 2
                // left side sum
                val left = a[m] * (m - i) - (pre[m] - pre[i])
                // right side sum
                val right = (pre[j + 1] - pre[m + 1]) - a[m] * (j - m)
                cost[i][j] = left + right
            }
        }
        val INF = Int.MAX_VALUE / 2
        val dp = Array(k + 1) { IntArray(n + 1) { INF } }
        dp[0][0] = 0
        for (t in 1..k) {
            for (p in 1..n) {
                var best = INF
                for (s in 0 until p) {
                    val cand = dp[t - 1][s] + cost[s][p - 1]
                    if (cand < best) best = cand
                }
                dp[t][p] = best
            }
        }
        return dp[k][n]
    }
}
```

## Dart

```dart
class Solution {
  int minDistance(List<int> houses, int k) {
    houses.sort();
    int n = houses.length;
    const int INF = 0x3fffffffffffffff; // large enough

    // Prefix sums
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      pref[i + 1] = pref[i] + houses[i];
    }

    // cost[l][r]: minimum distance for houses[l..r] with one mailbox
    List<List<int>> cost = List.generate(n, (_) => List.filled(n, 0));
    for (int l = 0; l < n; l++) {
      for (int r = l; r < n; r++) {
        int m = (l + r) >> 1;
        int leftCount = m - l;
        int leftSum = pref[m] - pref[l];
        int leftCost = houses[m] * leftCount - leftSum;

        int rightCount = r - m;
        int rightSum = pref[r + 1] - pref[m + 1];
        int rightCost = rightSum - houses[m] * rightCount;

        cost[l][r] = leftCost + rightCost;
      }
    }

    // dp[i][j]: min distance for first j houses using i mailboxes
    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(n + 1, INF));
    dp[0][0] = 0;

    for (int i = 1; i <= k; i++) {
      for (int j = i; j <= n; j++) {
        int best = INF;
        // previous split point p: first p houses handled by i-1 mailboxes
        for (int p = i - 1; p < j; p++) {
          int candidate = dp[i - 1][p] + cost[p][j - 1];
          if (candidate < best) best = candidate;
        }
        dp[i][j] = best;
      }
    }

    return dp[k][n];
  }
}
```

## Golang

```go
import "sort"

func minDistance(houses []int, k int) int {
    sort.Ints(houses)
    n := len(houses)

    // prefix sums
    pref := make([]int, n+1)
    for i := 0; i < n; i++ {
        pref[i+1] = pref[i] + houses[i]
    }

    // cost[l][r]: minimal distance for houses[l..r] with one mailbox
    cost := make([][]int, n)
    for i := 0; i < n; i++ {
        cost[i] = make([]int, n)
        for j := i; j < n; j++ {
            m := (i + j) / 2
            leftCnt := m - i
            sumLeft := pref[m] - pref[i]
            leftDist := houses[m]*leftCnt - sumLeft

            rightCnt := j - m
            sumRight := pref[j+1] - pref[m+1]
            rightDist := sumRight - houses[m]*rightCnt

            cost[i][j] = leftDist + rightDist
        }
    }

    const INF int = 1 << 60
    dp := make([][]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([]int, k+1)
        for j := 0; j <= k; j++ {
            dp[i][j] = INF
        }
    }
    dp[0][0] = 0

    for i := 1; i <= n; i++ {
        maxM := k
        if i < maxM {
            maxM = i
        }
        for m := 1; m <= maxM; m++ {
            best := INF
            for p := m - 1; p < i; p++ {
                val := dp[p][m-1] + cost[p][i-1]
                if val < best {
                    best = val
                }
            }
            dp[i][m] = best
        }
    }

    return dp[n][k]
}
```

## Ruby

```ruby
def min_distance(houses, k)
  houses.sort!
  n = houses.size
  # precompute cost for placing one mailbox for segment i..j
  cost = Array.new(n) { Array.new(n, 0) }
  (0...n).each do |i|
    (i...n).each do |j|
      mid = (i + j) / 2
      c = 0
      (i..j).each do |t|
        c += (houses[t] - houses[mid]).abs
      end
      cost[i][j] = c
    end
  end

  inf = 1 << 60
  dp = Array.new(k + 1) { Array.new(n, inf) }

  # one mailbox case
  (0...n).each do |i|
    dp[1][i] = cost[0][i]
  end

  (2..k).each do |m|
    (m - 1...n).each do |i|
      best = inf
      ((m - 2)..(i - 1)).each do |p|
        val = dp[m - 1][p] + cost[p + 1][i]
        best = val if val < best
      end
      dp[m][i] = best
    end
  end

  dp[k][n - 1]
end
```

## Scala

```scala
object Solution {
  def minDistance(houses: Array[Int], k: Int): Int = {
    val n = houses.length
    val sorted = houses.sorted
    val prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + sorted(i).toLong
      i += 1
    }

    // cost[i][j]: minimal distance for houses i..j with one mailbox
    val cost = Array.ofDim[Long](n, n)
    var start = 0
    while (start < n) {
      var end = start
      while (end < n) {
        val mid = (start + end) / 2
        val leftCost = sorted(mid).toLong * (mid - start) - (prefix(mid) - prefix(start))
        val rightCost = (prefix(end + 1) - prefix(mid + 1)) - sorted(mid).toLong * (end - mid)
        cost(start)(end) = leftCost + rightCost
        end += 1
      }
      start += 1
    }

    val INF: Long = Long.MaxValue / 4
    val dp = Array.ofDim[Long](k + 1, n)

    // base case: one mailbox
    i = 0
    while (i < n) {
      dp(1)(i) = cost(0)(i)
      i += 1
    }

    var m = 2
    while (m <= k) {
      var idx = m - 1 // at least m houses for m mailboxes
      while (idx < n) {
        var best = INF
        var p = m - 2 // previous split point
        while (p < idx) {
          val cand = dp(m - 1)(p) + cost(p + 1)(idx)
          if (cand < best) best = cand
          p += 1
        }
        dp(m)(idx) = best
        idx += 1
      }
      m += 1
    }

    dp(k)(n - 1).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_distance(houses: Vec<i32>, k: i32) -> i32 {
        let mut houses = houses;
        houses.sort_unstable();
        let n = houses.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + houses[i] as i64;
        }

        // cost[i][j]: minimal distance for houses[i..=j] with one mailbox
        let mut cost = vec![vec![0i64; n]; n];
        for i in 0..n {
            for j in i..n {
                let m = (i + j) / 2;
                let left = houses[m] as i64 * ((m - i) as i64) - (pref[m] - pref[i]);
                let right = (pref[j + 1] - pref[m + 1]) - houses[m] as i64 * ((j - m) as i64);
                cost[i][j] = left + right;
            }
        }

        let k_usize = k as usize;
        let inf: i64 = i64::MAX / 4;
        let mut dp = vec![vec![inf; n + 1]; k_usize + 1];
        dp[0][0] = 0;

        for t in 1..=k_usize {
            for p in 1..=n {
                let mut best = inf;
                for s in 0..p {
                    let cur = dp[t - 1][s] + cost[s][p - 1];
                    if cur < best {
                        best = cur;
                    }
                }
                dp[t][p] = best;
            }
        }

        dp[k_usize][n] as i32
    }
}
```

## Racket

```racket
(define/contract (min-distance houses k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort houses <))
         (n (length sorted))
         (arr (list->vector sorted))
         (INF 1000000000)
         ;; cost[i][j] = minimal distance for houses i..j with one mailbox
         (cost (let ([cvec (make-vector n)])
                 (for ([i (in-range n)])
                   (vector-set! cvec i (make-vector n 0)))
                 cvec))
         ;; dp[i][c] = minimal distance for first i houses using c mailboxes
         (dp (let ([dvec (make-vector (+ n 1))])
               (for ([i (in-range (+ n 1))])
                 (vector-set! dvec i (make-vector (+ k 1) INF)))
               dvec)))
    ;; compute cost matrix
    (for ([i (in-range n)])
      (for ([j (in-range i n)])
        (let* ((mid (quotient (+ i j) 2))
               (median-pos (vector-ref arr mid))
               (sum 0))
          (for ([t (in-range i (add1 j))])
            (set! sum (+ sum (abs (- (vector-ref arr t) median-pos)))))
          (vector-set! (vector-ref cost i) j sum))))
    ;; initialize dp[0][0] = 0
    (vector-set! (vector-ref dp 0) 0 0)
    ;; DP transitions
    (for ([i (in-range 1 (add1 n))])
      (for ([c (in-range 1 (add1 k))])
        (let ((best INF))
          (for ([p (in-range 0 i)])
            (let* ((prev (vector-ref (vector-ref dp p) (- c 1)))
                   (segment-cost (vector-ref (vector-ref cost p) (- i 1)))
                   (candidate (+ prev segment-cost)))
              (when (< candidate best)
                (set! best candidate))))
          (vector-set! (vector-ref dp i) c best))))
    ;; answer
    (vector-ref (vector-ref dp n) k)))
```

## Erlang

```erlang
-module(solution).
-export([min_distance/2]).

-define(INF, 1073741824).

min_distance(Houses, K) ->
    Sorted = lists:sort(Houses),
    N = length(Sorted),
    HousesT = list_to_tuple(Sorted),
    {_, CumList} = lists:foldl(
        fun(X, {Sum, Acc}) -> {Sum + X, Acc ++ [Sum + X]} end,
        {0, []},
        Sorted),
    PrefixT = list_to_tuple([0 | CumList]),   % index i+1 holds sum of first i houses
    CostMap = build_cost_map(N, HousesT, PrefixT),
    {Ans, _} = dp(N, K, CostMap, #{}, N),
    Ans.

build_cost_map(N, HousesT, PrefixT) ->
    lists:foldl(
        fun(I, AccI) ->
            lists:foldl(
                fun(J, AccJ) ->
                    C = segment_cost(I, J, HousesT, PrefixT),
                    maps:put({I, J}, C, AccJ)
                end,
                AccI,
                lists:seq(I, N))
        end,
        #{},
        lists:seq(1, N)).

segment_cost(I, J, HousesT, PrefixT) ->
    M = (I + J) div 2,
    HouseM = element(M, HousesT),
    LeftSum = element(M + 1, PrefixT) - element(I, PrefixT),
    RightSum = element(J + 1, PrefixT) - element(M + 1, PrefixT),
    HouseM * (M - I + 1) - LeftSum + RightSum - HouseM * (J - M).

dp(0, _K, _CostMap, Cache, _N) ->
    {0, Cache};
dp(_I, 0, _CostMap, Cache, _N) ->
    {?INF, Cache};
dp(I, K, _CostMap, Cache, _N) when K >= I ->
    {0, Cache};
dp(I, K, CostMap, Cache, N) ->
    case maps:find({I, K}, Cache) of
        {ok, Val} ->
            {Val, Cache};
        error ->
            Seq = lists:seq(K - 1, I - 1),
            {MinVal, NewCache} = lists:foldl(
                fun(P, {Acc, C}) ->
                    {Prev, C1} = dp(P, K - 1, CostMap, C, N),
                    CostPKI = maps:get({P + 1, I}, CostMap),
                    Val = Prev + CostPKI,
                    if
                        Val < Acc -> {Val, C1};
                        true -> {Acc, C1}
                    end
                end,
                {?INF, Cache},
                Seq),
            UpdatedCache = maps:put({I, K}, MinVal, NewCache),
            {MinVal, UpdatedCache}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_distance(houses :: [integer], k :: integer) :: integer
  def min_distance(houses, k) do
    houses = Enum.sort(houses)
    n = length(houses)

    # Precompute cost for every segment [i..j] with one mailbox at the median
    cost =
      Enum.reduce(0..(n - 1), %{}, fn i, acc_i ->
        inner =
          Enum.reduce(i..(n - 1), %{}, fn j, acc_j ->
            median_idx = div(i + j, 2)
            median_pos = Enum.at(houses, median_idx)

            dist =
              Enum.reduce(i..j, 0, fn idx, sum ->
                sum + abs(Enum.at(houses, idx) - median_pos)
              end)

            Map.put(acc_j, {i, j}, dist)
          end)

        Map.merge(acc_i, inner)
      end)

    inf = 1_000_000_000
    dp0 = %{{0, 0} => 0}

    dp =
      Enum.reduce(1..n, dp0, fn i, dp_acc ->
        max_m = min(i, k)

        Enum.reduce(1..max_m, dp_acc, fn m, dp_inner ->
          best =
            Enum.reduce(m - 1..i - 1, inf, fn p, cur_best ->
              prev = Map.get(dp_inner, {p, m - 1}, inf)

              if prev == inf do
                cur_best
              else
                c = Map.fetch!(cost, {p, i - 1})
                val = prev + c
                if val < cur_best, do: val, else: cur_best
              end
            end)

          Map.put(dp_inner, {i, m}, best)
        end)
      end)

    Map.get(dp, {n, k}, inf)
  end
end
```
