# 1000. Minimum Cost to Merge Stones

## Cpp

```cpp
class Solution {
public:
    int mergeStones(vector<int>& stones, int k) {
        int n = stones.size();
        if ((n - 1) % (k - 1) != 0) return -1;
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + stones[i];
        const int INF = 1e9;
        // dp[l][r][t]: min cost to merge [l..r] into t piles
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(k + 1, INF)));
        for (int i = 0; i < n; ++i) dp[i][i][1] = 0;
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                // compute costs for t piles where t > 1
                for (int t = 2; t <= k && t <= len; ++t) {
                    int best = INF;
                    for (int m = l; m < r; ++m) {
                        if (dp[l][m][t - 1] == INF || dp[m + 1][r][1] == INF) continue;
                        best = min(best, dp[l][m][t - 1] + dp[m + 1][r][1]);
                    }
                    dp[l][r][t] = best;
                }
                // compute cost to merge into one pile if possible
                if ((len - 1) % (k - 1) == 0) {
                    if (dp[l][r][k] != INF) {
                        dp[l][r][1] = dp[l][r][k] + pref[r + 1] - pref[l];
                    }
                }
            }
        }
        return dp[0][n - 1][1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int mergeStones(int[] stones, int k) {
        int n = stones.length;
        if ((n - 1) % (k - 1) != 0) return -1;

        int INF = Integer.MAX_VALUE / 2;
        int[][] prefix = new int[n + 1][];
        int[] pre = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = pre[i] + stones[i];
        }

        int[][][] dp = new int[n][n][k + 1];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                Arrays.fill(dp[i][j], INF);
            }
        }

        for (int i = 0; i < n; ++i) dp[i][i][1] = 0;

        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                // merge into m piles where 2 <= m <= k
                for (int m = 2; m <= k; ++m) {
                    int best = INF;
                    for (int t = i; t < j; ++t) {
                        if (dp[i][t][m - 1] == INF || dp[t + 1][j][1] == INF) continue;
                        best = Math.min(best, dp[i][t][m - 1] + dp[t + 1][j][1]);
                    }
                    dp[i][j][m] = best;
                }
                // merge into one pile if possible
                if ((len - 1) % (k - 1) == 0) {
                    int costK = dp[i][j][k];
                    if (costK != INF) {
                        dp[i][j][1] = costK + pre[j + 1] - pre[i];
                    }
                }
            }
        }

        return dp[0][n - 1][1] == INF ? -1 : dp[0][n - 1][1];
    }
}
```

## Python

```python
class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        INF = float('inf')
        dp = [[[INF] * (k + 1) for _ in range(n)] for __ in range(n)]
        for i in range(n):
            dp[i][i][1] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # compute costs to merge into t piles (2..k)
                for t in range(2, k + 1):
                    if (length - t) % (k - 1):
                        continue
                    best = INF
                    # split points spaced by (k-1)
                    for mid in range(i, j, k - 1):
                        left = dp[i][mid][t - 1]
                        right = dp[mid + 1][j][1]
                        if left == INF or right == INF:
                            continue
                        cur = left + right
                        if cur < best:
                            best = cur
                    dp[i][j][t] = best
                # after we can merge k piles into one pile
                if (length - 1) % (k - 1) == 0 and dp[i][j][k] != INF:
                    dp[i][j][1] = dp[i][j][k] + prefix[j + 1] - prefix[i]

        return int(dp[0][n - 1][1]) if dp[0][n - 1][1] != INF else -1
```

## Python3

```python
from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if n == 1:
            return 0
        # Feasibility check
        if (n - 1) % (k - 1):
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def interval_sum(i: int, j: int) -> int:
            return prefix[j + 1] - prefix[i]

        INF = float('inf')
        # dp[i][j][m]: min cost to merge stones i..j into m piles
        dp = [[[INF] * (k + 1) for _ in range(n)] for __ in range(n)]

        for i in range(n):
            dp[i][i][1] = 0

        # length of interval
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                # compute costs for merging into m piles (2..k)
                for m in range(2, k + 1):
                    best = INF
                    # split point
                    for t in range(i, j):
                        # left part p piles, right part m-p piles
                        for p in range(1, m):
                            if dp[i][t][p] == INF or dp[t + 1][j][m - p] == INF:
                                continue
                            cost = dp[i][t][p] + dp[t + 1][j][m - p]
                            if cost < best:
                                best = cost
                    dp[i][j][m] = best

                # after we can merge k piles into one, add interval sum
                if (length - 1) % (k - 1) == 0:
                    if dp[i][j][k] != INF:
                        dp[i][j][1] = dp[i][j][k] + interval_sum(i, j)

        ans = dp[0][n - 1][1]
        return -1 if ans == INF else ans
```

## C

```c
#include <stddef.h>

int mergeStones(int* stones, int stonesSize, int k) {
    if (stonesSize == 0) return -1;
    if ((stonesSize - 1) % (k - 1) != 0) return -1;

    const int INF = 1000000000;
    int n = stonesSize;

    int pref[31];
    pref[0] = 0;
    for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + stones[i];

    #define SUM(i, j) (pref[(j) + 1] - pref[i])

    static int dp[30][30][31];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            for (int m = 1; m <= k; ++m)
                dp[i][j][m] = INF;

    for (int i = 0; i < n; ++i) dp[i][i][1] = 0;

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            for (int m = 2; m <= k; ++m) {
                if ((len - m) % (k - 1) != 0) continue;
                int best = INF;
                for (int t = i; t < j; ++t) {
                    if (dp[i][t][m - 1] == INF || dp[t + 1][j][1] == INF) continue;
                    int cand = dp[i][t][m - 1] + dp[t + 1][j][1];
                    if (cand < best) best = cand;
                }
                dp[i][j][m] = best;
            }
            if ((len - 1) % (k - 1) == 0 && dp[i][j][k] != INF) {
                dp[i][j][1] = dp[i][j][k] + SUM(i, j);
            }
        }
    }

    int ans = dp[0][n - 1][1];
    return (ans == INF) ? -1 : ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MergeStones(int[] stones, int k) {
        int n = stones.Length;
        if ((n - 1) % (k - 1) != 0) return -1;

        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];

        int INF = 1_000_000_000;
        int[,,] dp = new int[n, n, k + 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int m = 1; m <= k; m++)
                    dp[i, j, m] = INF;

        for (int i = 0; i < n; i++) dp[i, i, 1] = 0;

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                // compute dp[i][j][m] for m = 2..k
                for (int m = 2; m <= k; m++) {
                    int best = INF;
                    for (int mid = i; mid < j; mid++) {
                        if (dp[i, mid, m - 1] == INF || dp[mid + 1, j, 1] == INF) continue;
                        int cand = dp[i, mid, m - 1] + dp[mid + 1, j, 1];
                        if (cand < best) best = cand;
                    }
                    dp[i, j, m] = best;
                }
                // compute cost to merge into one pile if possible
                if ((len - 1) % (k - 1) == 0) {
                    int val = dp[i, j, k];
                    if (val != INF) {
                        int sum = prefix[j + 1] - prefix[i];
                        dp[i, j, 1] = val + sum;
                    }
                }
            }
        }

        return dp[0, n - 1, 1] == INF ? -1 : dp[0, n - 1, 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @param {number} k
 * @return {number}
 */
var mergeStones = function(stones, k) {
    const n = stones.length;
    if (n === 1) return 0;
    // Feasibility check
    if ((n - 1) % (k - 1) !== 0) return -1;

    // Prefix sums for interval sum queries
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + stones[i];
    }
    const rangeSum = (l, r) => prefix[r + 1] - prefix[l];

    // dp[i][j][t]: min cost to merge stones[i..j] into t piles
    const dp = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => new Array(k + 1).fill(Infinity))
    );

    for (let i = 0; i < n; ++i) {
        dp[i][i][1] = 0;
    }

    // Length of interval
    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;

            // Compute dp[i][j][t] for t = 2..k
            for (let t = 2; t <= k; ++t) {
                let best = Infinity;
                // split point
                for (let m = i; m < j; ++m) {
                    if (dp[i][m][t - 1] === Infinity || dp[m + 1][j][1] === Infinity) continue;
                    const cur = dp[i][m][t - 1] + dp[m + 1][j][1];
                    if (cur < best) best = cur;
                }
                dp[i][j][t] = best;
            }

            // If we can finally merge k piles into one pile
            if ((len - 1) % (k - 1) === 0) {
                const costK = dp[i][j][k];
                if (costK !== Infinity) {
                    dp[i][j][1] = costK + rangeSum(i, j);
                }
            }
        }
    }

    return dp[0][n - 1][1] === Infinity ? -1 : dp[0][n - 1][1];
};
```

## Typescript

```typescript
function mergeStones(stones: number[], k: number): number {
    const n = stones.length;
    if ((n - 1) % (k - 1) !== 0) return -1;

    const INF = Number.MAX_SAFE_INTEGER;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) prefix[i + 1] = prefix[i] + stones[i];
    const rangeSum = (l: number, r: number): number => prefix[r + 1] - prefix[l];

    // dp[i][j][t]: min cost to merge stones[i..j] into t piles
    const dp: number[][][] = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => new Array(k + 1).fill(INF))
    );

    for (let i = 0; i < n; ++i) dp[i][i][1] = 0;

    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            // compute costs for merging into t piles where t > 1
            for (let t = 2; t <= k; ++t) {
                if ((len - t) % (k - 1) !== 0) continue; // impossible size
                let best = INF;
                for (let m = i; m < j; ++m) {
                    const left = dp[i][m][t - 1];
                    const right = dp[m + 1][j][1];
                    if (left === INF || right === INF) continue;
                    const cur = left + right;
                    if (cur < best) best = cur;
                }
                dp[i][j][t] = best;
            }
            // possibly merge k piles into one
            if ((len - 1) % (k - 1) === 0) {
                const costK = dp[i][j][k];
                if (costK < INF) dp[i][j][1] = costK + rangeSum(i, j);
            }
        }
    }

    const ans = dp[0][n - 1][1];
    return ans === INF ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @param Integer $k
     * @return Integer
     */
    function mergeStones($stones, $k) {
        $n = count($stones);
        if (($n - 1) % ($k - 1) !== 0) {
            return -1;
        }

        // prefix sums
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $stones[$i];
        }

        $INF = PHP_INT_MAX;
        // dp[i][j]: min cost to merge stones i..j into one pile (if possible)
        $dp = array_fill(0, $n, array_fill(0, $n, $INF));
        for ($i = 0; $i < $n; $i++) {
            $dp[$i][$i] = 0;
        }

        // length of interval
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i + $len <= $n; $i++) {
                $j = $i + $len - 1;
                $best = $INF;

                // try splitting at positions spaced by (k-1)
                for ($mid = $i; $mid < $j; $mid += $k - 1) {
                    if ($dp[$i][$mid] === $INF || $dp[$mid + 1][$j] === $INF) {
                        continue;
                    }
                    $cand = $dp[$i][$mid] + $dp[$mid + 1][$j];
                    if ($cand < $best) {
                        $best = $cand;
                    }
                }

                $dp[$i][$j] = $best;

                // If this interval can be merged into one pile, add the sum cost
                if ((($len - 1) % ($k - 1)) === 0 && $dp[$i][$j] !== $INF) {
                    $dp[$i][$j] += $prefix[$j + 1] - $prefix[$i];
                }
            }
        }

        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func mergeStones(_ stones: [Int], _ K: Int) -> Int {
        let n = stones.count
        if (n - 1) % (K - 1) != 0 { return -1 }
        let INF = Int.max / 2
        
        // prefix sums for range sum queries
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + stones[i]
        }
        func rangeSum(_ l: Int, _ r: Int) -> Int {
            return prefix[r + 1] - prefix[l]
        }
        
        // dp[i][j][m]: min cost to merge stones i...j into m piles
        var dp = Array(
            repeating: Array(
                repeating: Array(repeating: INF, count: K + 1),
                count: n),
            count: n)
        
        for i in 0..<n {
            dp[i][i][1] = 0
        }
        
        if n == 1 { return 0 }
        
        for len in 2...n {
            for i in 0...(n - len) {
                let j = i + len - 1
                let maxM = min(K, len)
                if maxM >= 2 {
                    for m in 2...maxM {
                        var best = INF
                        var t = i
                        while t < j {
                            if dp[i][t][m - 1] < INF && dp[t + 1][j][1] < INF {
                                let cost = dp[i][t][m - 1] + dp[t + 1][j][1]
                                if cost < best { best = cost }
                            }
                            t += 1
                        }
                        dp[i][j][m] = best
                    }
                }
                // If we can merge into K piles, then we can merge those K piles into one pile
                if K <= len && dp[i][j][K] < INF {
                    dp[i][j][1] = dp[i][j][K] + rangeSum(i, j)
                }
            }
        }
        
        let result = dp[0][n - 1][1]
        return result >= INF ? -1 : result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mergeStones(stones: IntArray, k: Int): Int {
        val n = stones.size
        if ((n - 1) % (k - 1) != 0) return -1
        val INF = 1_000_000_000
        val prefix = IntArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + stones[i]
        }
        fun sum(l: Int, r: Int): Int = prefix[r + 1] - prefix[l]

        // dp[i][j][t]: min cost to merge stones i..j into t piles
        val dp = Array(n) { Array(n) { IntArray(k + 1) { INF } } }
        for (i in 0 until n) {
            dp[i][i][1] = 0
        }

        for (len in 2..n) {
            for (i in 0..n - len) {
                val j = i + len - 1
                // compute costs for t = 2 .. k
                for (t in 2..k) {
                    var best = INF
                    for (m in i until j) {
                        val left = dp[i][m][t - 1]
                        val right = dp[m + 1][j][1]
                        if (left < INF && right < INF) {
                            val cand = left + right
                            if (cand < best) best = cand
                        }
                    }
                    dp[i][j][t] = best
                }
                // compute cost for merging into one pile if possible
                if ((len - 1) % (k - 1) == 0) {
                    val costK = dp[i][j][k]
                    if (costK < INF) {
                        dp[i][j][1] = costK + sum(i, j)
                    }
                }
            }
        }

        return dp[0][n - 1][1]
    }
}
```

## Dart

```dart
class Solution {
  int mergeStones(List<int> stones, int k) {
    int n = stones.length;
    if ((n - 1) % (k - 1) != 0) return -1;

    const int INF = 1 << 60;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + stones[i];
    }
    int sum(int l, int r) => prefix[r + 1] - prefix[l];

    // dp[i][j][m]: min cost to merge stones[i..j] into m piles
    List<List<List<int>>> dp = List.generate(
        n,
        (_) => List.generate(
            n, (_) => List.filled(k + 1, INF)));

    for (int i = 0; i < n; ++i) {
      dp[i][i][1] = 0;
    }

    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;

        // compute dp[i][j][m] for m = 2..k
        for (int m = 2; m <= k; ++m) {
          int best = INF;
          // split point t where left part can become 1 pile
          for (int t = i; t < j; t += k - 1) {
            if (dp[i][t][1] == INF || dp[t + 1][j][m - 1] == INF) continue;
            int cand = dp[i][t][1] + dp[t + 1][j][m - 1];
            if (cand < best) best = cand;
          }
          dp[i][j][m] = best;
        }

        // try to merge into one pile if possible
        if ((len - 1) % (k - 1) == 0 && dp[i][j][k] != INF) {
          dp[i][j][1] = dp[i][j][k] + sum(i, j);
        }
      }
    }

    int ans = dp[0][n - 1][1];
    return ans >= INF ? -1 : ans;
  }
}
```

## Golang

```go
func mergeStones(stones []int, k int) int {
	const INF = int(1 << 60)

	n := len(stones)
	if (n-1)%(k-1) != 0 {
		return -1
	}

	// prefix sums
	prefix := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + stones[i]
	}
	sum := func(l, r int) int { // inclusive l,r
		return prefix[r+1] - prefix[l]
	}

	// dp[i][j][t]: min cost to merge stones[i..j] into t piles
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, k+1)
			for t := 1; t <= k; t++ {
				dp[i][j][t] = INF
			}
		}
	}

	for i := 0; i < n; i++ {
		dp[i][i][1] = 0
	}

	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1

			// compute dp[i][j][t] for t = 2..k
			for t := 2; t <= k; t++ {
				best := INF
				for m := i; m < j; m++ {
					for left := 1; left < t; left++ {
						right := t - left
						if dp[i][m][left] == INF || dp[m+1][j][right] == INF {
							continue
						}
						cost := dp[i][m][left] + dp[m+1][j][right]
						if cost < best {
							best = cost
						}
					}
				}
				dp[i][j][t] = best
			}

			// if we can merge k piles into 1 pile, add the sum cost
			if dp[i][j][k] != INF {
				dp[i][j][1] = dp[i][j][k] + sum(i, j)
			}
		}
	}

	ans := dp[0][n-1][1]
	if ans >= INF {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def merge_stones(stones, k)
  n = stones.length
  return -1 if (n - 1) % (k - 1) != 0

  # Prefix sums for O(1) range sum
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + stones[i] }
  range_sum = ->(l, r) { prefix[r + 1] - prefix[l] }

  inf = 1 << 60
  dp = Array.new(n) { Array.new(n, 0) }      # min cost to reach a state with piles count ≡ 1 (mod k-1)
  cost_one = Array.new(n) { Array.new(n, inf) } # min cost to merge interval into one pile

  n.times do |i|
    dp[i][i] = 0
    cost_one[i][i] = 0
  end

  (2..n).each do |len|
    (0..(n - len)).each do |i|
      j = i + len - 1

      # Compute minimal cost to reduce interval to a "valid" pile count
      best = inf
      m = i
      while m < j
        cur = dp[i][m] + dp[m + 1][j]
        best = cur if cur < best
        m += k - 1
      end

      # If the interval size already satisfies (len-1) % (k-1) == 0,
      # we can keep it as is with zero additional cost.
      if ((len - 1) % (k - 1)).zero?
        best = 0 if best > 0
      end
      dp[i][j] = best

      # If we can finally merge this interval into one pile, add the sum cost
      if ((len - 1) % (k - 1)).zero?
        total = dp[i][j] + range_sum.call(i, j)
        cost_one[i][j] = total
        dp[i][j] = total if total < dp[i][j]
      else
        cost_one[i][j] = inf
      end
    end
  end

  ans = cost_one[0][n - 1]
  ans >= inf ? -1 : ans
end
```

## Scala

```scala
object Solution {
    def mergeStones(stones: Array[Int], k: Int): Int = {
        val n = stones.length
        if ((n - 1) % (k - 1) != 0) return -1

        val prefix = new Array[Int](n + 1)
        var i = 0
        while (i < n) {
            prefix(i + 1) = prefix(i) + stones(i)
            i += 1
        }
        def rangeSum(l: Int, r: Int): Int = prefix(r + 1) - prefix(l)

        val INF = Int.MaxValue / 2
        val dp = Array.ofDim[Int](n, n) // dp[i][j] minimal cost to merge [i,j] into optimal piles

        var len = 2
        while (len <= n) {
            var left = 0
            while (left + len - 1 < n) {
                val right = left + len - 1
                var best = INF
                var m = left
                while (m < right) {
                    if ((m - left) % (k - 1) == 0) {
                        val cur = dp(left)(m) + dp(m + 1)(right)
                        if (cur < best) best = cur
                    }
                    m += 1
                }
                dp(left)(right) = best
                if ((len - 1) % (k - 1) == 0 && dp(left)(right) < INF) {
                    dp(left)(right) += rangeSum(left, right)
                }
                left += 1
            }
            len += 1
        }

        val ans = dp(0)(n - 1)
        if (ans >= INF) -1 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge_stones(stones: Vec<i32>, k: i32) -> i32 {
        let n = stones.len();
        if (n - 1) % ((k as usize) - 1) != 0 {
            return -1;
        }
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + stones[i] as i64;
        }
        const INF: i64 = 1_i64 << 60;
        let k_usize = k as usize;
        let mut dp = vec![vec![vec![INF; k_usize + 1]; n]; n];
        for i in 0..n {
            dp[i][i][1] = 0;
        }
        for len in 2..=n {
            for i in 0..=n - len {
                let j = i + len - 1;
                // compute dp[i][j][m] for m = 2..k
                for m in 2..=k_usize {
                    let mut best = INF;
                    let step = k_usize - 1;
                    let mut mid = i;
                    while mid < j {
                        if dp[i][mid][1] != INF && dp[mid + 1][j][m - 1] != INF {
                            best = best.min(dp[i][mid][1] + dp[mid + 1][j][m - 1]);
                        }
                        mid += step;
                    }
                    dp[i][j][m] = best;
                }
                // try to merge into one pile if possible
                if (len - 1) % (k_usize - 1) == 0 {
                    let sum = prefix[j + 1] - prefix[i];
                    if dp[i][j][k_usize] != INF {
                        dp[i][j][1] = dp[i][j][1].min(dp[i][j][k_usize] + sum);
                    }
                }
            }
        }
        let ans = dp[0][n - 1][1];
        if ans == INF { -1 } else { ans as i32 }
    }
}
```

## Racket

```racket
(define/contract (merge-stones stones k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length stones))
         (mod (- k 1)))
    (if (not (= (remainder (- n 1) mod) 0))
        -1
        (let* ((INF 1000000000)
               ;; prefix sums
               (ps (let ((vec (make-vector (+ n 1) 0)))
                     (for ([i (in-range n)])
                       (vector-set! vec (+ i 1)
                                    (+ (vector-ref vec i) (list-ref stones i))))
                     vec))
               (range-sum (lambda (l r)
                            (- (vector-ref ps (+ r 1)) (vector-ref ps l))))
               ;; dp and best matrices
               (dp (for/vector ([i n]) (make-vector n INF)))
               (best (for/vector ([i n]) (make-vector n INF))))
          ;; base cases: single pile costs zero
          (for ([i (in-range n)])
            (vector-set! (vector-ref dp i) i 0)
            (vector-set! (vector-ref best i) i 0))
          ;; DP over interval lengths
          (for ([len (in-range 2 (+ n 1))])
            (let ((max-i (- n len)))
              (for ([i (in-range 0 (+ max-i 1))])
                (let* ((j (+ i len -1))
                       (best-cost INF))
                  ;; combine subintervals; step = k-1
                  (for ([mid (in-range i j mod)])
                    (let* ((left (vector-ref (vector-ref best i) mid))
                           (right (vector-ref (vector-ref best (+ mid 1)) j))
                           (cand (+ left right)))
                      (when (< cand best-cost)
                        (set! best-cost cand))))
                  ;; if interval can be merged into one pile, add sum
                  (when (= (remainder (- len 1) mod) 0)
                    (let ((total (+ best-cost (range-sum i j))))
                      (vector-set! (vector-ref dp i) j total)
                      (when (< total best-cost)
                        (set! best-cost total))))
                  ;; store the minimal cost for this interval in best matrix
                  (vector-set! (vector-ref best i) j best-cost)))))
          (let ((ans (vector-ref (vector-ref dp 0) (- n 1))))
            (if (>= ans INF) -1 ans))))))
```

## Erlang

```erlang
-module(solution).
-export([merge_stones/2]).

-define(INF, 1152921504606846976). % 2^60

merge_stones(Stones, K) ->
    N = length(Stones),
    case (N - 1) rem (K - 1) of
        0 -> ok;
        _ -> -1
    end,
    Prefix = prefix_sum(Stones),
    DP0 = init_base(maps:new(), N),
    DP = fill_all(N, K, Prefix, ?INF, DP0),
    case maps:find({0, N-1, 1}, DP) of
        {ok, Val} -> Val;
        error -> -1
    end.

%% Build prefix sum list where element at index i (0‑based) is sum of first i stones.
prefix_sum(Stones) ->
    prefix_sum(Stones, 0, [0]).

prefix_sum([], _Sum, Acc) ->
    lists:reverse(Acc);
prefix_sum([H|T], Sum, Acc) ->
    New = Sum + H,
    prefix_sum(T, New, [New | Acc]).

%% Initialize dp[i,i,1] = 0.
init_base(DP, N) ->
    lists:foldl(fun(I, Acc) -> maps:put({I, I, 1}, 0, Acc) end,
                DP,
                lists:seq(0, N-1)).

fill_all(N, K, Prefix, INF, DP) ->
    lists:foldl(fun(Len, AccDP) -> fill_len(Len, N, K, Prefix, INF, AccDP) end,
                DP,
                lists:seq(2, N)).

fill_len(Len, N, K, Prefix, INF, DP) ->
    lists:foldl(
      fun(I, AccDP) ->
          J = I + Len - 1,
          %% compute dp[i,j,t] for t = 2 .. K
          AccDP_T =
            lists:foldl(
              fun(T, DAcc) ->
                  Min = min_split(I, J, T, Prefix, DAcc, INF),
                  case Min of
                      INF -> DAcc;
                      _   -> maps:put({I, J, T}, Min, DAcc)
                  end
              end,
              AccDP,
              lists:seq(2, K)),
          %% possibly compute dp[i,j,1]
          DP_Final =
            if ((Len - 1) rem (K - 1)) =:= 0 ->
                case maps:get({I, J, K}, AccDP_T, INF) of
                    INF -> AccDP_T;
                    ValK ->
                        SumIJ = sum_range(Prefix, I, J),
                        maps:put({I, J, 1}, ValK + SumIJ, AccDP_T)
                end;
               true -> AccDP_T
            end,
          DP_Final
      end,
      DP,
      lists:seq(0, N - Len)).

%% Minimum cost to merge interval [I,J] into T piles.
min_split(I, J, T, Prefix, DP, INF) ->
    lists:foldl(
      fun(Mid, Acc) ->
          Left  = maps:get({I, Mid, T-1}, DP, INF),
          Right = maps:get({Mid+1, J, 1}, DP, INF),
          if Left =/= INF andalso Right =/= INF ->
                 Cand = Left + Right,
                 case Cand < Acc of
                     true -> Cand;
                     false -> Acc
                 end;
             true -> Acc
          end
      end,
      INF,
      lists:seq(I, J-1)).

sum_range(Prefix, I, J) ->
    get_prefix(Prefix, J+1) - get_prefix(Prefix, I).

get_prefix(Prefix, Index) ->
    %% Index is 0‑based; lists:nth expects 1‑based.
    lists:nth(Index + 1, Prefix).
```

## Elixir

```elixir
defmodule Solution do
  @inf 1_000_000_000

  @spec merge_stones(stones :: [integer], k :: integer) :: integer
  def merge_stones(stones, k) do
    n = length(stones)

    # If final merging to one pile is impossible
    if rem(n - 1, k - 1) != 0 do
      -1
    else
      prefix = build_prefix(stones)
      {ans, _} = dfs(0, n - 1, 1, stones, prefix, k, %{})
      if ans >= @inf, do: -1, else: ans
    end
  end

  # Build prefix sum list where prefix[0] = 0 and prefix[i+1] = sum of first i elements
  defp build_prefix(stones) do
    Enum.reduce(stones, [0], fn v, acc ->
      [hd(acc) + v | acc]
    end)
    |> Enum.reverse()
  end

  # Sum of stones[i..j] inclusive using prefix sums
  defp range_sum(prefix, i, j) do
    Enum.at(prefix, j + 1) - Enum.at(prefix, i)
  end

  # dfs returns {cost, updated_memo}
  defp dfs(i, j, t, stones, prefix, k, memo) do
    key = {i, j, t}

    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        len = j - i + 1

        # feasibility check: (len - t) must be divisible by (k-1)
        result =
          cond do
            i == j ->
              if t == 1, do: 0, else: @inf

            rem(len - t, k - 1) != 0 ->
              @inf

            t == 1 ->
              # need to first merge into k piles then add sum
              {cost_k, memo1} = dfs(i, j, k, stones, prefix, k, memo)
              if cost_k >= @inf do
                {@inf, memo1}
              else
                total = cost_k + range_sum(prefix, i, j)
                {total, Map.put(memo1, key, total)}
              end

            true ->
              # t > 1: split into left (t-1 piles) and right (1 pile)
              {best, memo2} =
                Enum.reduce(i..(j - 1), {@inf, memo}, fn mid, {cur_best, cur_memo} ->
                  {left, memo_left} = dfs(i, mid, t - 1, stones, prefix, k, cur_memo)
                  {right, memo_right} = dfs(mid + 1, j, 1, stones, prefix, k, memo_left)

                  cand =
                    if left < @inf and right < @inf do
                      left + right
                    else
                      @inf
                    end

                  new_best = if cand < cur_best, do: cand, else: cur_best
                  {new_best, memo_right}
                end)

              {best, Map.put(memo2, key, best)}
          end

        # result may be a tuple when t == 1 case handled above; normalize
        case result do
          {val, new_memo} -> {val, new_memo}
          val -> {val, Map.put(memo, key, val)}
        end
    end
  end
end
```
