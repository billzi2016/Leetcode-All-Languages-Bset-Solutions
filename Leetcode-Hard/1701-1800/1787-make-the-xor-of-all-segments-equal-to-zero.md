# 1787. Make the XOR of All Segments Equal to Zero

## Cpp

```cpp
class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        const int MAXX = 1024; // since nums[i] < 2^10
        const int INF = 1e9;
        int n = nums.size();
        vector<vector<int>> cnt(k, vector<int>(MAXX, 0));
        vector<int> sz(k, 0);
        for (int i = 0; i < n; ++i) {
            int g = i % k;
            cnt[g][nums[i]]++;
            sz[g]++;
        }
        // store distinct values per group to iterate efficiently
        vector<vector<int>> vals(k);
        for (int g = 0; g < k; ++g) {
            for (int v = 0; v < MAXX; ++v) {
                if (cnt[g][v] > 0) vals[g].push_back(v);
            }
        }

        vector<int> dp(MAXX, INF);
        dp[0] = 0;
        for (int g = 0; g < k; ++g) {
            vector<int> ndp(MAXX, INF);
            int minPrev = INF;
            for (int x = 0; x < MAXX; ++x) {
                if (dp[x] < minPrev) minPrev = dp[x];
            }
            // transitions using existing values in the group
            for (int prevX = 0; prevX < MAXX; ++prevX) {
                if (dp[prevX] == INF) continue;
                int baseCost = dp[prevX];
                for (int v : vals[g]) {
                    int curX = prevX ^ v;
                    int cost = baseCost + sz[g] - cnt[g][v];
                    if (cost < ndp[curX]) ndp[curX] = cost;
                }
            }
            // transitions where we change all elements to a value not present (cost = sz[g])
            for (int curX = 0; curX < MAXX; ++curX) {
                int cost = minPrev + sz[g];
                if (cost < ndp[curX]) ndp[curX] = cost;
            }
            dp.swap(ndp);
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public int minChanges(int[] nums, int k) {
        int n = nums.length;
        final int MAXV = 1024; // since nums[i] < 2^10
        int[][] cnt = new int[k][MAXV];
        for (int i = 0; i < n; i++) {
            cnt[i % k][nums[i]]++;
        }
        final int NEG_INF = -1_000_000_0;
        int[] dp = new int[MAXV];
        java.util.Arrays.fill(dp, NEG_INF);
        dp[0] = 0;
        for (int g = 0; g < k; g++) {
            int[] ndp = new int[MAXV];
            java.util.Arrays.fill(ndp, NEG_INF);
            for (int xorPrev = 0; xorPrev < MAXV; xorPrev++) {
                if (dp[xorPrev] == NEG_INF) continue;
                for (int v = 0; v < MAXV; v++) {
                    int keep = cnt[g][v];
                    int newXor = xorPrev ^ v;
                    ndp[newXor] = Math.max(ndp[newXor], dp[xorPrev] + keep);
                }
            }
            dp = ndp;
        }
        int maxKeep = dp[0];
        return n - maxKeep;
    }
}
```

## Python

```python
class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MAX_XOR = 1024  # since nums[i] < 2^10
        INF = 10 ** 9

        dp = [INF] * MAX_XOR
        dp[0] = 0

        for start in range(k):
            group = nums[start::k]
            sz = len(group)
            freq = {}
            for v in group:
                freq[v] = freq.get(v, 0) + 1

            ndp = [INF] * MAX_XOR
            # transitions using values that appear in the group
            for cur_xor in range(MAX_XOR):
                if dp[cur_xor] == INF:
                    continue
                for v, cnt in freq.items():
                    cost = sz - cnt  # changes needed to make all elements equal to v
                    nx = cur_xor ^ v
                    new_val = dp[cur_xor] + cost
                    if new_val < ndp[nx]:
                        ndp[nx] = new_val

            # transition using any value not present in the group (cost = sz)
            min_prev = min(dp)  # best previous cost regardless of xor
            base_cost = min_prev + sz
            for i in range(MAX_XOR):
                if ndp[i] > base_cost:
                    ndp[i] = base_cost

            dp = ndp

        return dp[0]
```

## Python3

```python
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAX_XOR = 1 << 10  # 1024
        INF = 10 ** 9

        # Build groups based on index modulo k
        groups = [[] for _ in range(k)]
        for i, val in enumerate(nums):
            groups[i % k].append(val)

        dp = [INF] * MAX_XOR
        dp[0] = 0

        for grp in groups:
            size = len(grp)
            freq = {}
            for v in grp:
                freq[v] = freq.get(v, 0) + 1

            ndp = [INF] * MAX_XOR
            min_prev = min(dp)

            # Transition using values that actually appear in the group
            for prev_xor in range(MAX_XOR):
                if dp[prev_xor] == INF:
                    continue
                base_cost = dp[prev_xor]
                for v, cnt in freq.items():
                    new_xor = prev_xor ^ v
                    cost = base_cost + size - cnt
                    if cost < ndp[new_xor]:
                        ndp[new_xor] = cost

            # Transition using any value not present (cost = size)
            base_all = min_prev + size
            for xor_val in range(MAX_XOR):
                if base_all < ndp[xor_val]:
                    ndp[xor_val] = base_all

            dp = ndp

        return dp[0]
```

## C

```c
#include <stdlib.h>
#include <string.h>

int minChanges(int* nums, int numsSize, int k) {
    const int MAXV = 1024;               // values are in [0, 2^10)
    const int INF = 1e9;

    /* frequency tables for each column (mod k) */
    int **freq = (int **)malloc(k * sizeof(int *));
    for (int i = 0; i < k; ++i) {
        freq[i] = (int *)calloc(MAXV, sizeof(int));
    }
    int *colSize = (int *)calloc(k, sizeof(int));

    for (int i = 0; i < numsSize; ++i) {
        int col = i % k;
        ++colSize[col];
        ++freq[col][nums[i]];
    }

    int dp[MAXV], ndp[MAXV];
    for (int i = 0; i < MAXV; ++i) dp[i] = INF;
    dp[0] = 0;

    for (int col = 0; col < k; ++col) {
        /* minimum of previous dp, used for arbitrary value choice */
        int minPrev = INF;
        for (int x = 0; x < MAXV; ++x)
            if (dp[x] < minPrev) minPrev = dp[x];

        /* start with the cost of changing whole column to any value */
        for (int y = 0; y < MAXV; ++y)
            ndp[y] = minPrev + colSize[col];

        /* consider values that actually appear in this column */
        for (int v = 0; v < MAXV; ++v) {
            int cnt = freq[col][v];
            if (cnt == 0) continue;
            int costChange = colSize[col] - cnt;
            for (int prev = 0; prev < MAXV; ++prev) {
                int nxor = prev ^ v;
                int cand = dp[prev] + costChange;
                if (cand < ndp[nxor]) ndp[nxor] = cand;
            }
        }

        /* move to next column */
        memcpy(dp, ndp, sizeof(dp));
    }

    int answer = dp[0];

    for (int i = 0; i < k; ++i) free(freq[i]);
    free(freq);
    free(colSize);

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinChanges(int[] nums, int k) {
        int n = nums.Length;
        var groups = new List<Dictionary<int,int>>();
        var groupSize = new int[k];
        for (int i = 0; i < k; i++) groups.Add(new Dictionary<int,int>());
        for (int i = 0; i < n; i++) {
            int g = i % k;
            groupSize[g]++;
            int val = nums[i];
            var dict = groups[g];
            if (dict.ContainsKey(val)) dict[val]++; else dict[val] = 1;
        }

        const int MAXXOR = 1024; // since nums[i] < 2^10
        const int INF = 1_000_000_0;
        int[] dp = new int[MAXXOR];
        for (int i = 0; i < MAXXOR; i++) dp[i] = INF;
        dp[0] = 0;

        for (int g = 0; g < k; g++) {
            int sz = groupSize[g];
            var freq = groups[g];

            // find minimal previous dp value
            int minPrev = INF;
            for (int i = 0; i < MAXXOR; i++) {
                if (dp[i] < minPrev) minPrev = dp[i];
            }

            int[] ndp = new int[MAXXOR];
            // baseline: choose any value not necessarily present
            int baseCost = minPrev + sz;
            for (int i = 0; i < MAXXOR; i++) ndp[i] = baseCost;

            // improve using values that actually appear in the group
            for (int xorPrev = 0; xorPrev < MAXXOR; xorPrev++) {
                int prevCost = dp[xorPrev];
                if (prevCost == INF) continue;
                foreach (var kv in freq) {
                    int val = kv.Key;
                    int cnt = kv.Value;
                    int newXor = xorPrev ^ val;
                    int cand = prevCost + sz - cnt;
                    if (cand < ndp[newXor]) ndp[newXor] = cand;
                }
            }

            dp = ndp;
        }

        return dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minChanges = function(nums, k) {
    const n = nums.length;
    const groupSize = new Array(k).fill(0);
    const freqs = Array.from({length: k}, () => ({}));
    
    for (let i = 0; i < n; i++) {
        const g = i % k;
        const val = nums[i];
        groupSize[g]++;
        const map = freqs[g];
        map[val] = (map[val] || 0) + 1;
    }
    
    const MAXV = 1024; // values are < 2^10
    let dpPrev = new Array(MAXV).fill(Infinity);
    dpPrev[0] = 0;
    
    for (let g = 0; g < k; g++) {
        const size = groupSize[g];
        if (size === 0) continue;
        const freqMap = freqs[g];
        
        // global minimum of previous DP
        let minPrev = Infinity;
        for (let x = 0; x < MAXV; x++) {
            if (dpPrev[x] < minPrev) minPrev = dpPrev[x];
        }
        const baseCost = size + minPrev;
        const dpNext = new Array(MAXV).fill(baseCost);
        
        // consider values that actually appear in the group
        for (const key in freqMap) {
            const v = Number(key);
            const cnt = freqMap[key];
            const costV = size - cnt; // changes needed if we set this value for the whole group
            for (let x = 0; x < MAXV; x++) {
                const cand = dpPrev[x ^ v] + costV;
                if (cand < dpNext[x]) dpNext[x] = cand;
            }
        }
        dpPrev = dpNext;
    }
    
    return dpPrev[0];
};
```

## Typescript

```typescript
function minChanges(nums: number[], k: number): number {
    const MAX_XOR = 1024; // since nums[i] < 2^10
    const groupSize = new Array(k).fill(0);
    const groupFreq: Map<number, number>[] = Array.from({ length: k }, () => new Map());

    for (let i = 0; i < nums.length; i++) {
        const g = i % k;
        groupSize[g]++;
        const m = groupFreq[g];
        m.set(nums[i], (m.get(nums[i]) ?? 0) + 1);
    }

    let dp = new Array(MAX_XOR).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0;

    for (let idx = 0; idx < k; idx++) {
        const sz = groupSize[idx];
        const freqMap = groupFreq[idx];
        const ndp = new Array(MAX_XOR).fill(Number.MAX_SAFE_INTEGER);

        // Use existing values in the group
        for (let prevXor = 0; prevXor < MAX_XOR; prevXor++) {
            const base = dp[prevXor];
            if (base === Number.MAX_SAFE_INTEGER) continue;
            for (const [val, cnt] of freqMap.entries()) {
                const cost = base + sz - cnt;
                const nx = prevXor ^ val;
                if (cost < ndp[nx]) ndp[nx] = cost;
            }
        }

        // Change all elements in the group to any value
        let minPrev = Number.MAX_SAFE_INTEGER;
        for (let v = 0; v < MAX_XOR; v++) {
            if (dp[v] < minPrev) minPrev = dp[v];
        }
        const allCost = minPrev + sz;
        for (let target = 0; target < MAX_XOR; target++) {
            if (allCost < ndp[target]) ndp[target] = allCost;
        }

        dp = ndp;
    }

    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minChanges($nums, $k) {
        $n = count($nums);
        $INF = 1 << 30;
        $dp = array_fill(0, 1024, $INF);
        $dp[0] = 0;

        for ($r = 0; $r < $k; $r++) {
            $freq = [];
            $sz = 0;
            for ($i = $r; $i < $n; $i += $k) {
                $val = $nums[$i];
                if (!isset($freq[$val])) {
                    $freq[$val] = 0;
                }
                $freq[$val]++;
                $sz++;
            }

            // baseline: change whole group to any value (cost = sz)
            $newdp = array_fill(0, 1024, $INF);
            $minPrev = $INF;
            foreach ($dp as $v) {
                if ($v < $minPrev) {
                    $minPrev = $v;
                }
            }
            for ($xor = 0; $xor < 1024; $xor++) {
                $newdp[$xor] = $minPrev + $sz;
            }

            foreach ($freq as $val => $cnt) {
                for ($prevXor = 0; $prevXor < 1024; $prevXor++) {
                    $cost = $dp[$prevXor] + $sz - $cnt;
                    $newXor = $prevXor ^ $val;
                    if ($cost < $newdp[$newXor]) {
                        $newdp[$newXor] = $cost;
                    }
                }
            }

            $dp = $newdp;
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func minChanges(_ nums: [Int], _ k: Int) -> Int {
        let INF = Int.max / 2
        var dp = Array(repeating: INF, count: 1024)
        dp[0] = 0
        
        for i in 0..<k {
            var freq = [Int:Int]()
            var cnt = 0
            var idx = i
            while idx < nums.count {
                let val = nums[idx]
                freq[val, default: 0] += 1
                cnt += 1
                idx += k
            }
            
            var newdp = Array(repeating: INF, count: 1024)
            var minPrev = INF
            for v in dp where v < minPrev {
                minPrev = v
            }
            
            // Use existing values in the group
            for prevXor in 0..<1024 where dp[prevXor] != INF {
                let base = dp[prevXor]
                for (value, f) in freq {
                    let newXor = prevXor ^ value
                    let cost = base + cnt - f
                    if cost < newdp[newXor] {
                        newdp[newXor] = cost
                    }
                }
            }
            
            // Change all elements to a value not present (cost = cnt)
            for xorVal in 0..<1024 {
                let cost = minPrev + cnt
                if cost < newdp[xorVal] {
                    newdp[xorVal] = cost
                }
            }
            
            dp = newdp
        }
        
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minChanges(nums: IntArray, k: Int): Int {
        val n = nums.size
        val MAX_XOR = 1024 // since nums[i] < 2^10
        var dp = IntArray(MAX_XOR) { Int.MAX_VALUE / 2 }
        dp[0] = 0
        for (r in 0 until k) {
            val freq = HashMap<Int, Int>()
            var cnt = 0
            var idx = r
            while (idx < n) {
                freq[nums[idx]] = (freq[nums[idx]] ?: 0) + 1
                cnt++
                idx += k
            }
            // minimum previous cost regardless of xor (changing all elements to any value)
            var minPrev = Int.MAX_VALUE / 2
            for (v in dp) if (v < minPrev) minPrev = v

            val newDp = IntArray(MAX_XOR) { minPrev + cnt } // transition with changing all elements
            for (prevXor in 0 until MAX_XOR) {
                val prevCost = dp[prevXor]
                if (prevCost >= Int.MAX_VALUE / 4) continue
                for ((value, f) in freq) {
                    val newXor = prevXor xor value
                    val cost = prevCost + cnt - f
                    if (cost < newDp[newXor]) newDp[newXor] = cost
                }
            }
            dp = newDp
        }
        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int minChanges(List<int> nums, int k) {
    const int MAX_XOR = 1 << 10; // 1024
    const int INF = 1 << 30;

    // Build frequency maps for each group modulo k
    List<Map<int, int>> freqMaps = List.generate(k, (_) => <int, int>{});
    List<int> groupSize = List.filled(k, 0);
    for (int i = 0; i < nums.length; ++i) {
      int g = i % k;
      groupSize[g]++;
      freqMaps[g][nums[i]] = (freqMaps[g][nums[i]] ?? 0) + 1;
    }

    List<int> dpPrev = List.filled(MAX_XOR, INF);
    dpPrev[0] = 0;

    for (int idx = 0; idx < k; ++idx) {
      int sz = groupSize[idx];
      Map<int, int> freq = freqMaps[idx];

      List<int> dpCurr = List.filled(MAX_XOR, INF);

      for (int prevXor = 0; prevXor < MAX_XOR; ++prevXor) {
        if (dpPrev[prevXor] == INF) continue;
        int baseCost = dpPrev[prevXor];
        // Try all values present in this group
        for (var entry in freq.entries) {
          int val = entry.key;
          int sameCnt = entry.value;
          int cost = sz - sameCnt; // changes needed to make whole group equal to val
          int newXor = prevXor ^ val;
          int total = baseCost + cost;
          if (total < dpCurr[newXor]) {
            dpCurr[newXor] = total;
          }
        }
      }

      dpPrev = dpCurr;
    }

    return dpPrev[0];
  }
}
```

## Golang

```go
func minChanges(nums []int, k int) int {
	const MAXXOR = 1 << 10 // 1024
	INF := 1 << 30

	// group elements by index modulo k
	groups := make([][]int, k)
	for i, v := range nums {
		groups[i%k] = append(groups[i%k], v)
	}

	dp := make([]int, MAXXOR)
	for i := 0; i < MAXXOR; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	for _, group := range groups {
		freq := make(map[int]int)
		for _, v := range group {
			freq[v]++
		}
		size := len(group)

		ndp := make([]int, MAXXOR)
		for i := 0; i < MAXXOR; i++ {
			ndp[i] = INF
		}

		// minimal previous cost (used when we change the whole group to a new value)
		minPrev := INF
		for _, v := range dp {
			if v < minPrev {
				minPrev = v
			}
		}

		// transition using values present in the current group
		for prevXor, prevCost := range dp {
			if prevCost == INF {
				continue
			}
			for val, cnt := range freq {
				newXor := prevXor ^ val
				cost := prevCost + size - cnt
				if cost < ndp[newXor] {
					ndp[newXor] = cost
				}
			}
		}

		// transition when we change the whole group to any other value (cost = size)
		for newXor := 0; newXor < MAXXOR; newXor++ {
			if minPrev+size < ndp[newXor] {
				ndp[newXor] = minPrev + size
			}
		}

		dp = ndp
	}

	return dp[0]
}
```

## Ruby

```ruby
def min_changes(nums, k)
  max_val = 1 << 10 # values are < 2^10
  groups = Array.new(k) { Hash.new(0) }
  nums.each_with_index do |num, i|
    r = i % k
    groups[r][num] += 1
  end

  neg_inf = -1 << 60
  dp = Array.new(max_val, neg_inf)
  dp[0] = 0

  groups.each do |cnt|
    max_prev = dp.max
    newdp = Array.new(max_val, max_prev) # choose any value (freq 0)

    (0...max_val).each do |xor_prev|
      next if dp[xor_prev] < 0
      cnt.each do |val, freq|
        nx = xor_prev ^ val
        kept = dp[xor_prev] + freq
        newdp[nx] = kept if kept > newdp[nx]
      end
    end

    dp = newdp
  end

  max_kept = dp[0]
  nums.length - max_kept
end
```

## Scala

```scala
object Solution {
    def minChanges(nums: Array[Int], k: Int): Int = {
        val MAX_XOR = 1 << 10 // 1024
        val INF = 1_000_000_0
        var dp = Array.fill(MAX_XOR)(INF)
        dp(0) = 0

        for (groupIdx <- 0 until k) {
            var i = groupIdx
            val freq = scala.collection.mutable.Map[Int, Int]()
            var size = 0
            while (i < nums.length) {
                val v = nums(i)
                freq(v) = freq.getOrElse(v, 0) + 1
                size += 1
                i += k
            }

            var minPrev = INF
            var idx = 0
            while (idx < MAX_XOR) {
                if (dp(idx) < minPrev) minPrev = dp(idx)
                idx += 1
            }

            val newDp = Array.fill(MAX_XOR)(size + minPrev)

            for ((value, cnt) <- freq) {
                var t = 0
                while (t < MAX_XOR) {
                    val candidate = dp(t ^ value) + size - cnt
                    if (candidate < newDp(t)) newDp(t) = candidate
                    t += 1
                }
            }

            dp = newDp
        }

        dp(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_changes(nums: Vec<i32>, k: i32) -> i32 {
        let k_usize = k as usize;
        let mut groups: Vec<Vec<i32>> = vec![Vec::new(); k_usize];
        for (i, &v) in nums.iter().enumerate() {
            groups[i % k_usize].push(v);
        }
        const MAX_XOR: usize = 1024; // values are < 2^10
        let inf: i32 = 1_000_000_0;
        let mut dp = vec![inf; MAX_XOR];
        dp[0] = 0;
        for group in groups.iter() {
            let size = group.len() as i32;
            let mut freq = vec![0i32; MAX_XOR];
            let mut present: Vec<usize> = Vec::new();
            for &v in group.iter() {
                let idx = v as usize;
                if freq[idx] == 0 {
                    present.push(idx);
                }
                freq[idx] += 1;
            }
            // global minimum of previous dp
            let mut global_min = inf;
            for &val in dp.iter() {
                if val < global_min {
                    global_min = val;
                }
            }
            let mut new_dp = vec![inf; MAX_XOR];
            for x in 0..MAX_XOR {
                let mut best_inner = global_min;
                for &v in present.iter() {
                    let cand = dp[x ^ v] - freq[v];
                    if cand < best_inner {
                        best_inner = cand;
                    }
                }
                new_dp[x] = size + best_inner;
            }
            dp = new_dp;
        }
        dp[0]
    }
}
```

## Racket

```racket
(define/contract (min-changes nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [INF 1000000000]
         [MAXXOR 1024] ; since nums[i] < 2^10
         [dp (make-vector MAXXOR INF)])
    (vector-set! dp 0 0)
    (let loop-groups ([r 0] [dp-current dp])
      (if (= r k)
          (vector-ref dp-current 0)
          (let* ([freq (make-hash)]
                 [size 0]
                 ;; build frequency map for this group
                 )
            (for ([idx (in-range r n k)])
              (let ([v (vector-ref arr idx)])
                (hash-set! freq v (+ 1 (hash-ref freq v 0)))
                (set! size (+ size 1))))
            (define min-prev
              (let loop-min ([i 0] [best INF])
                (if (= i MAXXOR)
                    best
                    (loop-min (+ i 1) (min best (vector-ref dp-current i))))))
            (define newdp (make-vector MAXXOR INF))
            ;; initialize with changing all elements to an arbitrary value
            (for ([cur (in-range MAXXOR)])
              (vector-set! newdp cur (+ min-prev size)))
            ;; improve using existing values in the group
            (hash-for-each freq
                           (lambda (val cnt)
                             (for ([p (in-range MAXXOR)])
                               (let* ([prev-cost (vector-ref dp-current p)]
                                      [cur (bitwise-xor p val)]
                                      [cost (+ prev-cost (- size cnt))])
                                 (when (< cost (vector-ref newdp cur))
                                   (vector-set! newdp cur cost))))))

            (loop-groups (+ r 1) newdp))))))
```

## Erlang

```erlang
-module(solution).
-export([min_changes/2]).

-define(INF, 1073741824). % large number

min_changes(Nums, K) ->
    N = length(Nums),
    %% Build groups: map from group index to {Size, FreqMap}
    InitGroups = maps:from_list([{I, {0, #{}}} || I <- lists:seq(0, K - 1)]),
    Indexed = lists:zip(lists:seq(0, N - 1), Nums),
    Groups = lists:foldl(fun({Idx, Val}, Acc) ->
        G = Idx rem K,
        {Size, Freq} = maps:get(G, Acc),
        NewSize = Size + 1,
        OldCnt = maps:get(Val, Freq, 0),
        NewFreq = maps:put(Val, OldCnt + 1, Freq),
        maps:put(G, {NewSize, NewFreq}, Acc)
    end, InitGroups, Indexed),

    %% DP initialization
    DP0 = #{0 => 0},
    FinalDP = lists:foldl(fun(GroupIdx, DPPrev) ->
        {Size, FreqMap} = maps:get(GroupIdx, Groups),
        DistinctVals = maps:keys(FreqMap),
        DistinctCount = length(DistinctVals),

        MinPrev = lists:min(maps:values(DPPrev)),

        %% Transitions using present values
        DPAfterPresent = maps:fold(fun(PrevXor, PrevCost, DPAcc) ->
            Base = PrevCost,
            lists:foldl(fun(Val, InnerDP) ->
                Freq = maps:get(Val, FreqMap),
                Cost = Size - Freq,
                NewXor = PrevXor bxor Val,
                NewCost = Base + Cost,
                update_min(InnerDP, NewXor, NewCost)
            end, DPAcc, DistinctVals)
        end, #{}, DPPrev),

        %% Transitions using any absent value (uniform cost) if possible
        DPNext =
            case DistinctCount < 1024 of
                true ->
                    lists:foldl(fun(X, AccDP) ->
                        NewCost = MinPrev + Size,
                        update_min(AccDP, X, NewCost)
                    end, DPAfterPresent, lists:seq(0, 1023));
                false ->
                    DPAfterPresent
            end,
        DPNext
    end, DP0, lists:seq(0, K - 1)),

    maps:get(0, FinalDP).

%% Helper to keep minimal value for a key in map
update_min(Map, Key, NewVal) ->
    case maps:get(Key, Map, undefined) of
        undefined -> maps:put(Key, NewVal, Map);
        Old when NewVal < Old -> maps:put(Key, NewVal, Map);
        _ -> Map
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_changes(nums :: [integer], k :: integer) :: integer
  def min_changes(nums, k) do
    groups =
      Enum.with_index(nums)
      |> Enum.reduce(%{}, fn {val, idx}, acc ->
        r = rem(idx, k)

        {sz, cnts} = Map.get(acc, r, {0, %{}})
        new_cnts = Map.update(cnts, val, 1, &(&1 + 1))
        Map.put(acc, r, {sz + 1, new_cnts})
      end)

    inf = 1_000_000
    dp_initial = :array.new(1024, default: inf) |> :array.set(0, 0)

    dp_final =
      0..(k - 1)
      |> Enum.reduce(dp_initial, fn r, dp_acc ->
        {len, cnts} = Map.get(groups, r, {0, %{}})

        global_min =
          Enum.reduce(0..1023, inf, fn i, acc_min ->
            v = :array.get(i, dp_acc)
            if v < acc_min, do: v, else: acc_min
          end)

        base = len + global_min
        new_dp = :array.new(1024, default: base)

        new_dp =
          Enum.reduce(cnts, new_dp, fn {v, c}, ndp ->
            cost_change = len - c

            Enum.reduce(0..1023, ndp, fn p, ndp_inner ->
              prev = :array.get(p, dp_acc)

              if prev < inf do
                nx = Bitwise.bxor(p, v)
                nc = prev + cost_change
                cur = :array.get(nx, ndp_inner)

                if nc < cur do
                  :array.set(nx, nc, ndp_inner)
                else
                  ndp_inner
                end
              else
                ndp_inner
              end
            end)
          end)

        new_dp
      end)

    :array.get(0, dp_final)
  end
end
```
