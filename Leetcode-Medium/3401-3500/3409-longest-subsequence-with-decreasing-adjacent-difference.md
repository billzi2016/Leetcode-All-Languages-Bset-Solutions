# 3409. Longest Subsequence With Decreasing Adjacent Difference

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        const int MAXV = 301; // values and diffs range [0,300]
        static int best[MAXV][MAXV];
        static int suff[MAXV][MAXV + 1]; // suffix maximums, extra column for sentinel
        bool seen[MAXV] = {false};
        int ans = 1;
        
        for (int v : nums) {
            vector<int> curBest(MAXV, 0);
            // try to extend from every previously seen value
            for (int x = 1; x < MAXV; ++x) if (seen[x]) {
                int diff = abs(v - x);
                int prevLen = suff[x][diff]; // max length ending at x with last diff >= diff
                int cand = (prevLen > 0 ? prevLen + 1 : 2); // pair with single element x if needed
                if (cand > curBest[diff]) curBest[diff] = cand;
            }
            
            // update structures for current value v
            for (int d = 0; d < MAXV; ++d) if (curBest[d]) {
                if (curBest[d] > best[v][d]) {
                    best[v][d] = curBest[d];
                    // recompute suffixes for value v from d downwards
                    for (int k = d; k >= 0; --k) {
                        int newVal = max(best[v][k], suff[v][k + 1]);
                        if (newVal == suff[v][k]) break;
                        suff[v][k] = newVal;
                    }
                }
                ans = max(ans, curBest[d]);
            }
            
            // ensure suffix for v is at least 0 beyond max diff
            suff[v][MAXV] = 0;
            seen[v] = true;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Fenwick {
        int n;
        int[] bit;
        Fenwick(int n) {
            this.n = n;
            bit = new int[n + 2];
        }
        void update(int idx, int val) {
            while (idx <= n) {
                if (val > bit[idx]) bit[idx] = val;
                idx += idx & -idx;
            }
        }
        int query(int idx) {
            int res = 0;
            while (idx > 0) {
                if (bit[idx] > res) res = bit[idx];
                idx -= idx & -idx;
            }
            return res;
        }
    }

    public int longestSubsequence(int[] nums) {
        final int MAXV = 300;
        final int MAXD = 300;
        final int BIT_SIZE = MAXD + 1; // indices 1..301

        Fenwick[] fens = new Fenwick[MAXV + 1];
        boolean[] seen = new boolean[MAXV + 1];
        List<Integer> valuesSeen = new ArrayList<>();

        int answer = 1;

        for (int cur : nums) {
            int bestOverall = 1; // subsequence consisting only of cur

            for (int v : valuesSeen) {
                int d = Math.abs(cur - v);
                int idx = MAXD - d + 1; // map diff to BIT index

                Fenwick fenPrev = fens[v];
                int prevLen = fenPrev != null ? fenPrev.query(idx) : 0;

                int cand = (prevLen > 0) ? prevLen + 1 : 2; // length 2 from single v if no prior diff
                if (cand > bestOverall) bestOverall = cand;

                Fenwick fenCur = fens[cur];
                if (fenCur == null) {
                    fenCur = new Fenwick(BIT_SIZE);
                    fens[cur] = fenCur;
                }
                fenCur.update(idx, cand);
            }

            answer = Math.max(answer, bestOverall);

            if (!seen[cur]) {
                seen[cur] = true;
                valuesSeen.add(cur);
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_VAL = 300
        MAX_DIFF = 300  # differences range from 0 to 299 inclusive

        # best[val][d] = max length of subsequence ending with value 'val' and last diff exactly d
        best = [[0] * (MAX_DIFF + 1) for _ in range(MAX_VAL + 1)]
        # suffix_max[val][d] = max_{k >= d} best[val][k]
        suffix = [[0] * (MAX_DIFF + 2) for _ in range(MAX_VAL + 1)]

        seen = [False] * (MAX_VAL + 1)
        ans = 1

        for y in nums:
            # try to extend from any previously seen value x
            for x in range(1, MAX_VAL + 1):
                if not seen[x]:
                    continue
                d = abs(x - y)
                prev_len = suffix[x][d]
                cand = prev_len + 1 if prev_len else 2  # length 2 from a single previous element
                if cand > best[y][d]:
                    best[y][d] = cand
                    if cand > ans:
                        ans = cand

            # recompute suffix maximums for value y
            cur_best = best[y]
            cur_suffix = suffix[y]
            mx = 0
            for d in range(MAX_DIFF, -1, -1):
                if cur_best[d] > mx:
                    mx = cur_best[d]
                cur_suffix[d] = mx

            seen[y] = True

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        MAXV = 300
        MAXD = 300  # differences up to 299, keep a bit extra
        
        dp = [[0] * (MAXD + 1) for _ in range(MAXV + 1)]
        suffix = [[0] * (MAXD + 2) for _ in range(MAXV + 1)]  # extra column for easier handling
        seen = [False] * (MAXV + 1)
        
        ans = 1  # at least one element
        
        for x in nums:
            cur_updates = [0] * (MAXD + 1)
            for y in range(1, MAXV + 1):
                if not seen[y]:
                    continue
                d = abs(x - y)
                
                # start from a single-element subsequence ending at y
                if 2 > cur_updates[d]:
                    cur_updates[d] = 2
                
                prev_len = suffix[y][d]
                if prev_len:
                    cand = prev_len + 1
                    if cand > cur_updates[d]:
                        cur_updates[d] = cand
            
            # apply updates to dp for value x
            for d in range(MAXD + 1):
                val = cur_updates[d]
                if val > dp[x][d]:
                    dp[x][d] = val
                    if val > ans:
                        ans = val
            
            # recompute suffix max for value x (last diff >= d)
            best = 0
            for d in range(MAXD, -1, -1):
                if dp[x][d] > best:
                    best = dp[x][d]
                suffix[x][d] = best
            
            seen[x] = True
        
        return ans
```

## C

```c
int longestSubsequence(int* nums, int numsSize) {
    const int MAX_DIFF = 300;
    const int D = MAX_DIFF;                 // differences from 0..300
    int *dp = (int*)calloc(numsSize * (D + 1), sizeof(int));
    int *suf = (int*)calloc(numsSize * (D + 2), sizeof(int)); // extra column for sentinel

    int ans = 1; // at least one element
    for (int i = 0; i < numsSize; ++i) {
        for (int j = 0; j < i; ++j) {
            int d = nums[i] - nums[j];
            if (d < 0) d = -d;
            int prev = suf[j * (D + 2) + d];          // max length ending at j with last diff >= d
            int cand = prev ? prev + 1 : 2;           // start new pair or extend
            int *dp_i = dp + i * (D + 1);
            if (cand > dp_i[d]) dp_i[d] = cand;
        }
        int *suf_i = suf + i * (D + 2);
        for (int d = D; d >= 0; --d) {
            int val = dp[i * (D + 1) + d];
            if (suf_i[d + 1] > val) val = suf_i[d + 1];
            suf_i[d] = val;
            if (val > ans) ans = val;
        }
    }

    free(dp);
    free(suf);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestSubsequence(int[] nums) {
        const int MAXV = 300;
        const int MAXD = 300; // include 0..300
        int[,] dp = new int[MAXV + 1, MAXD + 1];
        int[,] suffix = new int[MAXV + 1, MAXD + 1];
        bool[] seen = new bool[MAXV + 1];
        int ans = 1;

        foreach (int val in nums) {
            int[] cur = new int[MAXD + 1];

            for (int y = 1; y <= MAXV; ++y) {
                if (!seen[y]) continue;
                int dNew = Math.Abs(val - y);
                int prevLen = suffix[y, dNew];
                int cand = prevLen > 0 ? prevLen + 1 : 2;
                if (cand > cur[dNew]) cur[dNew] = cand;
            }

            for (int d = 0; d <= MAXD; ++d) {
                int c = cur[d];
                if (c > dp[val, d]) {
                    dp[val, d] = c;
                    if (c > ans) ans = c;
                }
            }

            // recompute suffix maximums for this value
            int maxSoFar = 0;
            for (int d = MAXD; d >= 0; --d) {
                if (dp[val, d] > maxSoFar) maxSoFar = dp[val, d];
                suffix[val, d] = maxSoFar;
            }

            seen[val] = true;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubsequence = function(nums) {
    const MAX_VAL = 300;
    const MAX_DIFF = 299;               // max possible absolute difference
    const BIT_SIZE = MAX_DIFF + 1;       // indices for diffs 0..MAX_DIFF

    // Fenwick tree (BIT) for range maximum query on suffix [d, MAX_DIFF]
    // We store values at reversed index: revIdx = MAX_DIFF - d + 1 (1‑based)
    const bits = Array.from({ length: MAX_VAL + 1 }, () => new Uint16Array(BIT_SIZE + 2));

    function bitUpdate(bit, idx, val) {
        while (idx <= BIT_SIZE) {
            if (val > bit[idx]) bit[idx] = val;
            idx += idx & -idx;
        }
    }

    function bitQuery(bit, idx) { // max on prefix [1..idx]
        let res = 0;
        while (idx > 0) {
            const cur = bit[idx];
            if (cur > res) res = cur;
            idx -= idx & -idx;
        }
        return res;
    }

    const seen = new Uint8Array(MAX_VAL + 1);
    let answer = 1; // at least one element

    for (const num of nums) {
        const curBest = new Uint16Array(BIT_SIZE); // best length for each diff ending at current value
        for (let v = 1; v <= MAX_VAL; ++v) {
            const d = Math.abs(num - v);
            if (d > MAX_DIFF) continue;
            const revIdx = MAX_DIFF - d + 1;

            // extend sequences that already have a last difference >= d
            const bestPrev = bitQuery(bits[v], revIdx);
            if (bestPrev > 0) {
                const cand = bestPrev + 1;
                if (cand > curBest[d]) curBest[d] = cand;
            }

            // start from a single previous element of value v
            if (seen[v]) {
                if (curBest[d] < 2) curBest[d] = 2;
            }
        }

        const bitCur = bits[num];
        for (let d = 0; d <= MAX_DIFF; ++d) {
            const len = curBest[d];
            if (len > 0) {
                const revIdx = MAX_DIFF - d + 1;
                bitUpdate(bitCur, revIdx, len);
                if (len > answer) answer = len;
            }
        }

        seen[num] = 1;
    }

    return answer;
};
```

## Typescript

```typescript
function longestSubsequence(nums: number[]): number {
    const MAXV = 300;
    const D = 301; // diff range 0..300
    const best = Array.from({ length: MAXV + 1 }, () => new Uint16Array(D));
    const suffix = Array.from({ length: MAXV + 1 }, () => new Uint16Array(D));
    const seen = new Uint8Array(MAXV + 1);
    let ans = 1;

    for (const cur of nums) {
        const curBest = new Uint16Array(D);

        // try to extend from any previously seen value
        for (let pv = 1; pv <= MAXV; ++pv) {
            if (!seen[pv]) continue;
            const diff = Math.abs(cur - pv);
            const prevLen = suffix[pv][diff];
            const curLen = prevLen > 0 ? prevLen + 1 : 2; // pair with a single element of value pv
            if (curLen > curBest[diff]) curBest[diff] = curLen;
            if (curLen > ans) ans = curLen;
        }

        const bCur = best[cur];
        let needRecalc = false;

        for (let d = 0; d < D; ++d) {
            const val = curBest[d];
            if (val > bCur[d]) {
                bCur[d] = val;
                needRecalc = true;
            }
        }

        if (needRecalc) {
            const suff = suffix[cur];
            let maxVal = 0;
            for (let d = MAXV; d >= 0; --d) {
                const v = bCur[d];
                if (v > maxVal) maxVal = v;
                suff[d] = maxVal;
            }
        }

        seen[cur] = 1;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSubsequence($nums) {
        $maxVal = 300;
        $maxDiff = 300;

        // dp[value][diff] = max length of subsequence ending with this value and last diff = diff
        $dp = array_fill(0, $maxVal + 1, []);
        // prefMax[value][d] = max_{k >= d} dp[value][k]
        $prefMax = array_fill(0, $maxVal + 1, array_fill(0, $maxDiff + 2, 0));
        // whether a value has appeared before
        $hasValue = array_fill(0, $maxVal + 1, false);

        $ans = 1;

        foreach ($nums as $x) {
            // try to extend from every previously seen value y
            for ($y = 1; $y <= $maxVal; $y++) {
                if (!$hasValue[$y]) continue;
                $d = abs($x - $y);
                $prevLen = $prefMax[$y][$d];
                $candidate = ($prevLen > 0) ? $prevLen + 1 : 2;

                if (!isset($dp[$x][$d]) || $candidate > $dp[$x][$d]) {
                    $dp[$x][$d] = $candidate;
                    if ($candidate > $ans) $ans = $candidate;
                }
            }

            // mark current value as seen
            $hasValue[$x] = true;

            // recompute prefMax for value x
            for ($d = $maxDiff; $d >= 0; $d--) {
                $val = $dp[$x][$d] ?? 0;
                $prefMax[$x][$d] = max($val, $prefMax[$x][$d + 1]);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class SegmentTree {
    private var size: Int
    private var tree: [Int]

    init(_ n: Int) {
        self.size = n
        self.tree = Array(repeating: 0, count: 4 * n)
    }

    func update(_ index: Int, _ value: Int) {
        update(1, 0, size - 1, index, value)
    }

    private func update(_ node: Int, _ l: Int, _ r: Int, _ idx: Int, _ val: Int) {
        if l == r {
            if val > tree[node] { tree[node] = val }
            return
        }
        let mid = (l + r) >> 1
        if idx <= mid {
            update(node << 1, l, mid, idx, val)
        } else {
            update(node << 1 | 1, mid + 1, r, idx, val)
        }
        tree[node] = max(tree[node << 1], tree[node << 1 | 1])
    }

    func query(_ left: Int, _ right: Int) -> Int {
        if left > right { return 0 }
        return query(1, 0, size - 1, left, right)
    }

    private func query(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int {
        if ql <= l && r <= qr { return tree[node] }
        let mid = (l + r) >> 1
        var res = 0
        if ql <= mid {
            res = max(res, query(node << 1, l, mid, ql, qr))
        }
        if qr > mid {
            res = max(res, query(node << 1 | 1, mid + 1, r, ql, qr))
        }
        return res
    }
}

class Solution {
    func longestSubsequence(_ nums: [Int]) -> Int {
        let maxVal = 300
        let maxDiff = 299   // possible differences are 0...299

        var segTrees = [SegmentTree]()
        for _ in 0...maxVal {          // index 0 unused, values are 1..300
            segTrees.append(SegmentTree(maxDiff + 1))
        }

        var occCount = Array(repeating: 0, count: maxVal + 1)
        var answer = 1

        for num in nums {
            var bestCurrent = 1
            var tempBest = Array(repeating: 0, count: maxDiff + 1)

            // consider all possible previous values
            for v in 1...maxVal {
                if occCount[v] == 0 && segTrees[v].query(0, maxDiff) == 0 {
                    continue
                }
                let diff = abs(num - v)
                var cand = 0

                if occCount[v] > 0 {          // pair formed with a single previous element
                    cand = max(cand, 2)
                }

                let prevBest = segTrees[v].query(diff, maxDiff)   // extend existing subsequence
                if prevBest > 0 {
                    cand = max(cand, prevBest + 1)
                }

                if cand > 0 {
                    if cand > bestCurrent { bestCurrent = cand }
                    if cand > tempBest[diff] { tempBest[diff] = cand }
                }
            }

            // update structures for current value
            let curTree = segTrees[num]
            for d in 0...maxDiff {
                let val = tempBest[d]
                if val > 0 {
                    curTree.update(d, val)
                }
            }

            occCount[num] += 1
            if bestCurrent > answer { answer = bestCurrent }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MAX_VAL = 300
    private val MAX_DIFF = 300
    private val SIZE = 512 // next power of two >= MAX_DIFF+1
    private val OFFSET = SIZE
    private val seg = Array(MAX_VAL + 1) { IntArray(SIZE * 2) }
    private fun query(v: Int, l: Int, r: Int): Int {
        var left = l + OFFSET
        var right = r + OFFSET
        var res = 0
        while (left <= right) {
            if ((left and 1) == 1) {
                val cur = seg[v][left]
                if (cur > res) res = cur
                left++
            }
            if ((right and 1) == 0) {
                val cur = seg[v][right]
                if (cur > res) res = cur
                right--
            }
            left = left shr 1
            right = right shr 1
        }
        return res
    }

    private fun update(v: Int, diff: Int, value: Int) {
        var pos = diff + OFFSET
        if (value <= seg[v][pos]) return
        seg[v][pos] = value
        var i = pos shr 1
        while (i > 0) {
            val newVal = kotlin.math.max(seg[v][i shl 1], seg[v][(i shl 1) + 1])
            if (newVal == seg[v][i]) break
            seg[v][i] = newVal
            i = i shr 1
        }
    }

    fun longestSubsequence(nums: IntArray): Int {
        val cnt = IntArray(MAX_VAL + 1)
        var answer = 1
        for (x in nums) {
            val updates = IntArray(MAX_DIFF + 1)
            for (y in 1..MAX_VAL) {
                if (cnt[y] == 0) continue
                val diff = kotlin.math.abs(x - y)
                // pair of two elements
                if (updates[diff] < 2) updates[diff] = 2
                // extend existing sequences ending at value y
                val prevLen = query(y, diff, MAX_DIFF)
                if (prevLen > 0) {
                    val cand = prevLen + 1
                    if (cand > updates[diff]) updates[diff] = cand
                }
            }
            for (d in 0..MAX_DIFF) {
                val v = updates[d]
                if (v > 0) {
                    update(x, d, v)
                    if (v > answer) answer = v
                }
            }
            cnt[x]++
        }
        return answer
    }
}
```

## Dart

```dart
class BIT {
  final int n;
  final List<int> _tree;
  BIT(this.n) : _tree = List.filled(n + 1, 0);

  void update(int idx, int val) {
    while (idx <= n) {
      if (val > _tree[idx]) _tree[idx] = val;
      idx += idx & -idx;
    }
  }

  int query(int idx) {
    int res = 0;
    while (idx > 0) {
      if (_tree[idx] > res) res = _tree[idx];
      idx -= idx & -idx;
    }
    return res;
  }
}

class Solution {
  int longestSubsequence(List<int> nums) {
    const int maxVal = 300;
    const int maxDiff = 300; // covers diff from 0..300
    final int bitSize = maxDiff + 1; // indices up to maxDiff+1

    // BIT for each possible value (1..300)
    final List<BIT> bits = List.generate(maxVal + 1, (_) => BIT(bitSize));
    final List<bool> seen = List.filled(maxVal + 1, false);

    int answer = 1; // at least one element

    for (final cur in nums) {
      int bestCur = 1;
      for (int prevVal = 1; prevVal <= maxVal; ++prevVal) {
        if (!seen[prevVal]) continue;
        final int diff = (cur - prevVal).abs();
        final int revIdx = maxDiff - diff + 1; // map suffix [diff..max] to prefix
        final int prevLen = bits[prevVal].query(revIdx);
        final int cand = (prevLen == 0) ? 2 : prevLen + 1;
        if (cand > bestCur) bestCur = cand;
        bits[cur].update(revIdx, cand);
      }
      seen[cur] = true;
      if (bestCur > answer) answer = bestCur;
    }

    return answer;
  }
}
```

## Golang

```go
func longestSubsequence(nums []int) int {
	const maxV = 300
	const maxD = 300 // maximum possible absolute difference (0..300)

	// best[v][d] = longest subsequence ending with value v whose last adjacent diff is d
	best := make([][]int, maxV+1)
	pref := make([][]int, maxV+1)
	for i := 0; i <= maxV; i++ {
		best[i] = make([]int, maxD+2) // extra slot for easier prefix handling
		pref[i] = make([]int, maxD+2)
	}
	seen := make([]int, maxV+1)

	ans := 1

	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}

	for _, x := range nums {
		cand := make([]int, maxD+1)

		for y := 1; y <= maxV; y++ {
			if seen[y] == 0 && pref[y][0] == 0 {
				continue
			}
			diff := abs(x - y)
			prevLen := pref[y][diff]
			if prevLen > 0 {
				if cand[diff] < prevLen+1 {
					cand[diff] = prevLen + 1
				}
			} else if seen[y] > 0 { // start a new pair
				if cand[diff] < 2 {
					cand[diff] = 2
				}
			}
		}

		for d := 0; d <= maxD; d++ {
			if cand[d] > best[x][d] {
				best[x][d] = cand[d]
				if ans < cand[d] {
					ans = cand[d]
				}
			}
		}

		// recompute prefix maxima for value x
		maxSoFar := 0
		for d := maxD; d >= 0; d-- {
			if best[x][d] > maxSoFar {
				maxSoFar = best[x][d]
			}
			pref[x][d] = maxSoFar
		}

		seen[x]++
	}

	return ans
}
```

## Ruby

```ruby
def longest_subsequence(nums)
  max_val = 300
  max_diff = max_val

  dp = Array.new(max_val + 1) { Array.new(max_diff + 1, 0) }
  suff = Array.new(max_val + 1) { Array.new(max_diff + 2, 0) } # extra slot for safety
  seen = Array.new(max_val + 1, false)

  ans = 1

  nums.each do |x|
    new_vals = Array.new(max_diff + 1, 0)

    y = 1
    while y <= max_val
      if seen[y]
        cur_d = (x - y).abs
        prev_len = suff[y][cur_d]
        cand = 0
        if prev_len > 0
          cand = prev_len + 1
        else
          cand = 2
        end
        if cand > new_vals[cur_d]
          new_vals[cur_d] = cand
        end
        ans = cand if cand > ans
      end
      y += 1
    end

    seen[x] = true

    d = max_diff
    while d >= 0
      val = new_vals[d]
      dp[x][d] = val if val > dp[x][d]
      d -= 1
    end

    cur_max = 0
    d = max_diff
    while d >= 0
      cur_val = dp[x][d]
      cur_max = cur_val if cur_val > cur_max
      suff[x][d] = cur_max
      d -= 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def longestSubsequence(nums: Array[Int]): Int = {
        val maxVal = 300
        val maxDiff = maxVal
        val dp = Array.ofDim[Int](maxVal + 1, maxDiff + 1)
        val suffix = Array.ofDim[Int](maxVal + 1, maxDiff + 1)

        var ans = 1

        for (num <- nums) {
            val x = num
            val newVals = new Array[Int](maxDiff + 1)
            System.arraycopy(dp(x), 0, newVals, 0, maxDiff + 1)

            var y = 1
            while (y <= maxVal) {
                val diff = math.abs(x - y)
                var bestPrev = suffix(y)(diff)
                if (bestPrev == 0) bestPrev = 1
                val cand = bestPrev + 1
                if (cand > newVals(diff)) newVals(diff) = cand
                y += 1
            }

            var d = 0
            while (d <= maxDiff) {
                if (newVals(d) > dp(x)(d)) dp(x)(d) = newVals(d)
                if (dp(x)(d) > ans) ans = dp(x)(d)
                d += 1
            }

            var curMax = 0
            d = maxDiff
            while (d >= 0) {
                val v = dp(x)(d)
                if (v > curMax) curMax = v
                suffix(x)(d) = curMax
                d -= 1
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        const MAX_VAL: usize = 300;
        const MAX_DIFF: usize = 300; // covers diff from 0..299

        let mut best = vec![vec![0i32; MAX_DIFF + 1]; MAX_VAL + 1];
        let mut suff = vec![vec![0i32; MAX_DIFF + 1]; MAX_VAL + 1];
        let mut seen = vec![false; MAX_VAL + 1];

        let mut ans = 1i32;

        for &num in nums.iter() {
            let v = num as usize;
            // temporary best lengths for each possible diff ending at current element
            let mut cur = vec![0i32; MAX_DIFF + 1];

            for u in 1..=MAX_VAL {
                if !seen[u] {
                    continue;
                }
                let d = ((v as i32 - u as i32).abs()) as usize;
                // at least a pair of two elements
                let mut cand = 2i32;
                let prev_len = suff[u][d];
                if prev_len > 0 {
                    cand = cand.max(prev_len + 1);
                }
                if cand > cur[d] {
                    cur[d] = cand;
                }
                if cand > ans {
                    ans = cand;
                }
            }

            // update best table for value v
            let mut need_recalc = false;
            for d in 0..=MAX_DIFF {
                let len = cur[d];
                if len > 0 && len > best[v][d] {
                    best[v][d] = len;
                    need_recalc = true;
                }
            }

            // recompute suffix maximums for value v if changed or first time seen
            if need_recalc || !seen[v] {
                let mut cur_max = 0i32;
                for d_rev in (0..=MAX_DIFF).rev() {
                    if best[v][d_rev] > cur_max {
                        cur_max = best[v][d_rev];
                    }
                    suff[v][d_rev] = cur_max;
                }
            }

            seen[v] = true;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (longest-subsequence nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-val 300)
         (size (+ max-val 1))
         ;; best[value][diff] = longest length ending with this value and last diff
         (best-vecs (make-vector size #f))
         (suff-vecs (make-vector size #f)))
    ;; initialise inner vectors
    (for ([i (in-range size)])
      (vector-set! best-vecs i (make-vector size 0))
      (vector-set! suff-vecs i (make-vector size 0)))
    (define seen (make-vector size #f))
    (define ans 1)
    (for ([cur (in-list nums)])
      (define cur-best (make-vector size 0))
      ;; consider all previously seen values
      (for ([prev (in-range 1 size)])
        (when (vector-ref seen prev)
          (define diff (abs (- cur prev))) ; diff in [0,max-val]
          (define best-prev ((vector-ref suff-vecs prev) diff))
          (define cand (if (> best-prev 0) (+ best-prev 1) 2))
          (when (> cand (vector-ref cur-best diff))
            (vector-set! cur-best diff cand)
            (when (> cand ans) (set! ans cand)))))
      ;; update best for current value
      (define best-cur (vector-ref best-vecs cur))
      (for ([d (in-range size)])
        (define val (vector-ref cur-best d))
        (when (> val (vector-ref best-cur d))
          (vector-set! best-cur d val)))
      ;; recompute suffix maximums for current value
      (define suff-cur (make-vector (+ size 1) 0)) ; extra sentinel at end
      (for ([d (in-range max-val -1 -1)])
        (define mx (max (vector-ref best-cur d)
                        (vector-ref suff-cur (+ d 1))))
        (vector-set! suff-cur d mx))
      ;; store suffix without the extra element
      (vector-set! suff-vecs cur (vector-drop-right suff-cur 1))
      (vector-set! seen cur #t))
    ans))
```

## Erlang

```erlang
-spec longest_subsequence(Nums :: [integer()]) -> integer().
longest_subsequence(Nums) ->
    MaxVal = 300,
    BestTab = ets:new(best_tab, [set, public]),
    {Ans,_} =
        lists:foldl(
            fun(X, {CurAns, SufMap}) ->
                {LocalMax, NewSufMap} = process_element(X, SufMap, BestTab),
                {erlang:max(CurAns, LocalMax), NewSufMap}
            end,
            {1, maps:new()},
            Nums),
    ets:delete(BestTab),
    Ans.

process_element(X, SuffixMap, BestTab) ->
    MaxVal = 300,
    FunY =
        fun(Y, CurMax) ->
            Diff = if X >= Y -> X - Y; true -> Y - X end,
            PrevMax = case maps:get(Y, SuffixMap, undefined) of
                undefined -> 0;
                Tuple -> element(Diff + 1, Tuple)
            end,
            Candidate = if PrevMax > 0 -> PrevMax + 1; true -> 2 end,
            Old = case ets:lookup(BestTab, {X, Diff}) of
                [] -> 0;
                [{_, V}] -> V
            end,
            New = erlang:max(Old, Candidate),
            if New > Old ->
                    ets:insert(BestTab, {{X, Diff}, New});
               true -> ok
            end,
            erlang:max(CurMax, New)
        end,
    LocalMax = lists:foldl(FunY, 1, lists:seq(1, MaxVal)),
    SuffixTuple = compute_suffix_tuple(X, BestTab, MaxVal),
    NewSuffixMap = maps:put(X, SuffixTuple, SuffixMap),
    {LocalMax, NewSuffixMap}.

compute_suffix_tuple(Value, BestTab, MaxDiff) ->
    Fun =
        fun(Diff, {Prev, Acc}) ->
            BestVal = case ets:lookup(BestTab, {Value, Diff}) of
                [] -> 0;
                [{_, V}] -> V
            end,
            Cur = erlang:max(BestVal, Prev),
            {Cur, [Cur | Acc]}
        end,
    {_FinalPrev, RevList} =
        lists:foldl(Fun, {0, []}, lists:seq(MaxDiff, 0, -1)),
    List = lists:reverse(RevList),
    list_to_tuple(List).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_subsequence(nums :: [integer]) :: integer
  def longest_subsequence(nums) do
    max_diff = 300
    n = length(nums)
    arr = List.to_tuple(nums)

    best = :array.new(max_diff + 1, default: 0)
    ans = 1

    {_, final_ans} =
      Enum.reduce(0..(n - 1), {best, ans}, fn i, {best_acc, ans_acc} ->
        # build suffix max array from current best
        suffix =
          Enum.reduce(max_diff..0, :array.new(max_diff + 1, default: 0), fn d, acc ->
            val = :array.get(d, best_acc)
            next_val = if d == max_diff, do: 0, else: :array.get(d + 1, acc)
            maxv = if val > next_val, do: val, else: next_val
            :array.set(d, maxv, acc)
          end)

        # compute updates for each possible difference using previous elements
        updates =
          Enum.reduce(0..(i - 1), %{}, fn j, upd_map ->
            d = abs(:erlang.element(i + 1, arr) - :erlang.element(j + 1, arr))
            max_prev = :array.get(d, suffix)
            cur_len = if max_prev > 0, do: max_prev + 1, else: 2
            prev = Map.get(upd_map, d, 0)

            if cur_len > prev,
              do: Map.put(upd_map, d, cur_len),
              else: upd_map
          end)

        # update answer with the best length found at this position
        max_update =
          case Map.values(updates) do
            [] -> 0
            vals -> Enum.max(vals)
          end

        ans_new = if max_update > ans_acc, do: max_update, else: ans_acc

        # merge updates into the global best array
        best_new =
          Enum.reduce(updates, best_acc, fn {d, len}, b_acc ->
            cur = :array.get(d, b_acc)

            if len > cur,
              do: :array.set(d, len, b_acc),
              else: b_acc
          end)

        {best_new, ans_new}
      end)

    final_ans
  end
end
```
