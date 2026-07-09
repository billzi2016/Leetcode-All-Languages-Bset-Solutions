# 1959. Minimum Total Space Wasted With K Resizing Operations

## Cpp

```cpp
class Solution {
public:
    int minSpaceWastedKResizing(vector<int>& nums, int k) {
        int n = nums.size();
        const long long INF = (1LL<<60);
        // precompute cost[l][r]
        vector<vector<long long>> cost(n, vector<long long>(n, 0));
        for (int l = 0; l < n; ++l) {
            int mx = 0;
            long long sum = 0;
            for (int r = l; r < n; ++r) {
                mx = max(mx, nums[r]);
                sum += nums[r];
                cost[l][r] = (long long)(r - l + 1) * mx - sum;
            }
        }
        int maxGroups = k + 1;
        vector<vector<long long>> dp(maxGroups + 1, vector<long long>(n + 1, INF));
        dp[0][0] = 0;
        for (int g = 1; g <= maxGroups; ++g) {
            for (int i = 1; i <= n; ++i) {
                long long best = INF;
                for (int p = 0; p < i; ++p) {
                    if (dp[g-1][p] == INF) continue;
                    best = min(best, dp[g-1][p] + cost[p][i-1]);
                }
                dp[g][i] = best;
            }
        }
        long long ans = INF;
        for (int g = 1; g <= maxGroups; ++g) {
            ans = min(ans, dp[g][n]);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minSpaceWastedKResizing(int[] nums, int k) {
        int n = nums.length;
        long[][] cost = new long[n][n];
        for (int i = 0; i < n; i++) {
            int curMax = 0;
            long curSum = 0;
            for (int j = i; j < n; j++) {
                curMax = Math.max(curMax, nums[j]);
                curSum += nums[j];
                cost[i][j] = (long) (j - i + 1) * curMax - curSum;
            }
        }

        int maxSeg = Math.min(k + 1, n);
        long INF = Long.MAX_VALUE / 4;
        long[][] dp = new long[n][maxSeg + 1];
        for (int i = 0; i < n; i++) {
            for (int s = 0; s <= maxSeg; s++) dp[i][s] = INF;
        }

        for (int i = 0; i < n; i++) {
            dp[i][1] = cost[0][i];
        }

        for (int seg = 2; seg <= maxSeg; seg++) {
            for (int i = seg - 1; i < n; i++) { // need at least seg elements to have seg segments
                long best = INF;
                for (int p = seg - 2; p < i; p++) {
                    if (dp[p][seg - 1] == INF) continue;
                    long cand = dp[p][seg - 1] + cost[p + 1][i];
                    if (cand < best) best = cand;
                }
                dp[i][seg] = best;
            }
        }

        long ans = INF;
        for (int seg = 1; seg <= maxSeg; seg++) {
            ans = Math.min(ans, dp[n - 1][seg]);
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # prefix sums for quick range sum
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # cost[l][r]: waste if one segment covers nums[l..r]
        cost = [[0] * n for _ in range(n)]
        for l in range(n):
            cur_max = 0
            for r in range(l, n):
                cur_max = max(cur_max, nums[r])
                total = (r - l + 1) * cur_max
                seg_sum = pref[r + 1] - pref[l]
                cost[l][r] = total - seg_sum

        # dp[i][c]: minimum waste for prefix [0..i] using exactly c resizes (c+1 segments)
        INF = 10 ** 18
        max_c = min(k, n - 1)
        dp = [[INF] * (max_c + 1) for _ in range(n)]

        # base case: no resize (single segment from 0 to i)
        for i in range(n):
            dp[i][0] = cost[0][i]

        # fill DP
        for c in range(1, max_c + 1):
            for i in range(n):
                if i < c:  # not enough elements to have c resizes
                    continue
                best = INF
                # last segment starts at l (>=1) and ends at i
                for l in range(1, i + 1):
                    prev = dp[l - 1][c - 1]
                    if prev == INF:
                        continue
                    cur = prev + cost[l][i]
                    if cur < best:
                        best = cur
                dp[i][c] = best

        # answer: minimum waste with at most k resizes
        ans = min(dp[n - 1][c] for c in range(max_c + 1))
        return ans
```

## Python3

```python
class Solution:
    def minSpaceWastedKResizing(self, nums, k):
        n = len(nums)
        # precompute cost[l][r]: waste for segment [l, r] inclusive
        cost = [[0]*n for _ in range(n)]
        for l in range(n):
            cur_max = 0
            cur_sum = 0
            for r in range(l, n):
                cur_max = max(cur_max, nums[r])
                cur_sum += nums[r]
                length = r - l + 1
                cost[l][r] = cur_max * length - cur_sum

        INF = 10**18
        # dp[i][c]: min waste for first i elements using c segments
        dp = [[INF]*(k+2) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            max_c = min(i, k+1)
            for c in range(1, max_c+1):
                # transition: last segment starts at p (0-indexed), covers [p, i-1]
                for p in range(c-1, i):
                    prev = dp[p][c-1]
                    if prev == INF:
                        continue
                    cur = prev + cost[p][i-1]
                    if cur < dp[i][c]:
                        dp[i][c] = cur

        ans = min(dp[n][c] for c in range(1, k+2))
        return ans
```

## C

```c
#include <limits.h>

int minSpaceWastedKResizing(int* nums, int numsSize, int k) {
    int n = numsSize;
    const long long INF = (1LL << 60);
    
    /* prefix sums */
    long long pref[205];
    pref[0] = 0;
    for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
    
    /* cost[l][r]: waste if one segment covers [l, r] */
    static long long cost[205][205];
    for (int l = 0; l < n; ++l) {
        int curMax = 0;
        for (int r = l; r < n; ++r) {
            if (nums[r] > curMax) curMax = nums[r];
            long long sum = pref[r + 1] - pref[l];
            cost[l][r] = (long long)(r - l + 1) * curMax - sum;
        }
    }
    
    /* dp[i][r]: minimum waste for first i elements using exactly r resizes */
    static long long dp[205][205];
    for (int i = 0; i <= n; ++i)
        for (int r = 0; r <= k; ++r)
            dp[i][r] = INF;
    
    for (int r = 0; r <= k; ++r) dp[0][r] = 0;
    
    for (int i = 1; i <= n; ++i) {
        dp[i][0] = cost[0][i - 1];
        for (int r = 1; r <= k; ++r) {
            long long best = INF;
            for (int p = 1; p < i; ++p) {          // split before index p
                if (dp[p][r - 1] == INF) continue;
                long long cand = dp[p][r - 1] + cost[p][i - 1];
                if (cand < best) best = cand;
            }
            dp[i][r] = best;
        }
    }
    
    long long ans = INF;
    for (int r = 0; r <= k; ++r)
        if (dp[n][r] < ans) ans = dp[n][r];
    
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSpaceWastedKResizing(int[] nums, int k)
    {
        int n = nums.Length;
        long[,] cost = new long[n, n];
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        for (int l = 0; l < n; l++)
        {
            int curMax = 0;
            for (int r = l; r < n; r++)
            {
                if (nums[r] > curMax) curMax = nums[r];
                long sum = prefix[r + 1] - prefix[l];
                cost[l, r] = (long)(r - l + 1) * curMax - sum;
            }
        }

        int maxGroups = k + 1;
        const long INF = (long)4e18;
        long[,] dp = new long[n + 1, maxGroups + 1];
        for (int i = 0; i <= n; i++)
            for (int g = 0; g <= maxGroups; g++)
                dp[i, g] = INF;

        dp[0, 0] = 0;
        for (int i = 1; i <= n; i++)
        {
            for (int g = 1; g <= maxGroups; g++)
            {
                long best = INF;
                for (int p = 0; p < i; p++)
                {
                    if (dp[p, g - 1] == INF) continue;
                    long cand = dp[p, g - 1] + cost[p, i - 1];
                    if (cand < best) best = cand;
                }
                dp[i, g] = best;
            }
        }

        long ans = INF;
        for (int g = 1; g <= maxGroups; g++)
            if (dp[n, g] < ans) ans = dp[n, g];

        return (int)ans;
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
var minSpaceWastedKResizing = function(nums, k) {
    const n = nums.length;
    // precompute waste cost for every subarray [l..r]
    const cost = Array.from({ length: n }, () => Array(n).fill(0));
    for (let l = 0; l < n; ++l) {
        let mx = 0, sum = 0;
        for (let r = l; r < n; ++r) {
            mx = Math.max(mx, nums[r]);
            sum += nums[r];
            cost[l][r] = (r - l + 1) * mx - sum;
        }
    }

    const maxSeg = Math.min(k + 1, n);
    const INF = Number.MAX_SAFE_INTEGER;
    // dp[s][i]: min waste for first i elements using exactly s segments
    const dp = Array.from({ length: maxSeg + 1 }, () => Array(n + 1).fill(INF));
    dp[0][0] = 0;

    for (let s = 1; s <= maxSeg; ++s) {
        for (let i = 1; i <= n; ++i) {
            let best = INF;
            // previous cut position p, segment is nums[p..i-1]
            for (let p = s - 1; p < i; ++p) {
                if (dp[s - 1][p] !== INF) {
                    const val = dp[s - 1][p] + cost[p][i - 1];
                    if (val < best) best = val;
                }
            }
            dp[s][i] = best;
        }
    }

    let answer = INF;
    for (let s = 1; s <= maxSeg; ++s) {
        if (dp[s][n] < answer) answer = dp[s][n];
    }
    return answer;
};
```

## Typescript

```typescript
function minSpaceWastedKResizing(nums: number[], k: number): number {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

    // cost[l][r]: waste if a segment from l to r uses size = max(nums[l..r])
    const cost: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let l = 0; l < n; l++) {
        let mx = 0;
        for (let r = l; r < n; r++) {
            if (nums[r] > mx) mx = nums[r];
            const sum = prefix[r + 1] - prefix[l];
            cost[l][r] = mx * (r - l + 1) - sum;
        }
    }

    const maxGroups = Math.min(k + 1, n);
    const INF = Number.MAX_SAFE_INTEGER;
    const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(maxGroups + 1).fill(INF));
    dp[0][0] = 0;

    for (let i = 1; i <= n; i++) {
        for (let g = 1; g <= Math.min(i, maxGroups); g++) {
            let best = INF;
            // previous cut at position p (segment starts at p)
            for (let p = g - 1; p <= i - 1; p++) {
                const prev = dp[p][g - 1];
                if (prev === INF) continue;
                const cur = cost[p][i - 1];
                const cand = prev + cur;
                if (cand < best) best = cand;
            }
            dp[i][g] = best;
        }
    }

    let answer = INF;
    for (let g = 1; g <= maxGroups; g++) {
        if (dp[n][g] < answer) answer = dp[n][g];
    }
    return answer;
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
    function minSpaceWastedKResizing($nums, $k) {
        $n = count($nums);
        // prefix sums
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        }

        // precompute cost[l][r]
        $cost = array_fill(0, $n, []);
        for ($l = 0; $l < $n; $l++) {
            $maxVal = 0;
            for ($r = $l; $r < $n; $r++) {
                if ($nums[$r] > $maxVal) {
                    $maxVal = $nums[$r];
                }
                $sum = $prefix[$r + 1] - $prefix[$l];
                $cost[$l][$r] = $maxVal * ($r - $l + 1) - $sum;
            }
        }

        $maxGroups = min($k + 1, $n);
        // dp[g][i]: min waste for first i+1 elements using exactly g groups
        $dp = array_fill(0, $maxGroups + 1, []);
        for ($g = 1; $g <= $maxGroups; $g++) {
            $dp[$g] = array_fill(0, $n, PHP_INT_MAX);
        }

        // base: one group
        for ($i = 0; $i < $n; $i++) {
            $dp[1][$i] = $cost[0][$i];
        }

        // transitions
        for ($g = 2; $g <= $maxGroups; $g++) {
            // need at least g elements to form g groups
            for ($i = $g - 1; $i < $n; $i++) {
                $best = PHP_INT_MAX;
                // previous segment ends at p, start new at p+1
                for ($p = $g - 2; $p <= $i - 1; $p++) {
                    $candidate = $dp[$g - 1][$p] + $cost[$p + 1][$i];
                    if ($candidate < $best) {
                        $best = $candidate;
                    }
                }
                $dp[$g][$i] = $best;
            }
        }

        $ans = PHP_INT_MAX;
        for ($g = 1; $g <= $maxGroups; $g++) {
            if ($dp[$g][$n - 1] < $ans) {
                $ans = $dp[$g][$n - 1];
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minSpaceWastedKResizing(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var waste = Array(repeating: Array(repeating: 0, count: n), count: n)
        for l in 0..<n {
            var maxVal = 0
            var sum = 0
            for r in l..<n {
                let val = nums[r]
                if val > maxVal { maxVal = val }
                sum += val
                waste[l][r] = (r - l + 1) * maxVal - sum
            }
        }
        let INF = Int.max / 4
        var dp = Array(repeating: Array(repeating: INF, count: k + 1), count: n)
        for i in 0..<n {
            dp[i][0] = waste[0][i]
        }
        if k > 0 {
            for cuts in 1...k {
                for i in 0..<n {
                    if i == 0 { continue }
                    var best = INF
                    for p in 0..<i {
                        let prev = dp[p][cuts - 1]
                        if prev == INF { continue }
                        let candidate = prev + waste[p + 1][i]
                        if candidate < best {
                            best = candidate
                        }
                    }
                    dp[i][cuts] = best
                }
            }
        }
        var answer = INF
        for cuts in 0...k {
            if dp[n - 1][cuts] < answer {
                answer = dp[n - 1][cuts]
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSpaceWastedKResizing(nums: IntArray, k: Int): Int {
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + nums[i].toLong()
        }
        val cost = Array(n) { LongArray(n) }
        for (l in 0 until n) {
            var curMax = 0
            for (r in l until n) {
                if (nums[r] > curMax) curMax = nums[r]
                val sum = prefix[r + 1] - prefix[l]
                cost[l][r] = (r - l + 1).toLong() * curMax - sum
            }
        }
        val INF = Long.MAX_VALUE / 4
        val dp = Array(k + 1) { LongArray(n + 1) { INF } }
        for (c in 0..k) {
            dp[c][0] = 0L
        }
        for (i in 1..n) {
            dp[0][i] = cost[0][i - 1]
        }
        for (cuts in 1..k) {
            for (i in 1..n) {
                var best = INF
                for (p in 0 until i) {
                    val cand = dp[cuts - 1][p] + cost[p][i - 1]
                    if (cand < best) best = cand
                }
                dp[cuts][i] = best
            }
        }
        var ans = INF
        for (c in 0..k) {
            if (dp[c][n] < ans) ans = dp[c][n]
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minSpaceWastedKResizing(List<int> nums, int k) {
    int n = nums.length;
    // Precompute waste for every segment [i, j]
    List<List<int>> cost = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; i++) {
      int maxVal = 0;
      int sum = 0;
      for (int j = i; j < n; j++) {
        if (nums[j] > maxVal) maxVal = nums[j];
        sum += nums[j];
        cost[i][j] = (j - i + 1) * maxVal - sum;
      }
    }

    int segments = k + 1;
    const int INF = 0x7FFFFFFFFFFFFFFF; // large sentinel
    List<List<int>> dp = List.generate(segments + 1, (_) => List.filled(n + 1, INF));
    dp[0][0] = 0;

    for (int t = 1; t <= segments; t++) {
      for (int i = 1; i <= n; i++) {
        int best = INF;
        // previous cut position p: first t-1 segments cover [0, p-1], last segment is [p, i-1]
        for (int p = t - 1; p < i; p++) {
          if (dp[t - 1][p] == INF) continue;
          int cur = dp[t - 1][p] + cost[p][i - 1];
          if (cur < best) best = cur;
        }
        dp[t][i] = best;
      }
    }

    return dp[segments][n];
  }
}
```

## Golang

```go
func minSpaceWastedKResizing(nums []int, k int) int {
    n := len(nums)
    // prefix sums for quick segment sum
    pref := make([]int64, n+1)
    for i := 0; i < n; i++ {
        pref[i+1] = pref[i] + int64(nums[i])
    }

    // cost[l][r]: waste if a single size is used from l to r inclusive
    cost := make([][]int64, n)
    for i := 0; i < n; i++ {
        cost[i] = make([]int64, n)
        maxV := 0
        for j := i; j < n; j++ {
            if nums[j] > maxV {
                maxV = nums[j]
            }
            length := j - i + 1
            sumSeg := pref[j+1] - pref[i]
            waste := int64(length*maxV) - sumSeg
            cost[i][j] = waste
        }
    }

    // maximum number of segments allowed (initial size counts as first segment)
    maxSeg := k + 1

    const INF int64 = 1 << 60
    dp := make([][]int64, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int64, maxSeg+1) // index from 1..maxSeg
        for s := 0; s <= maxSeg; s++ {
            dp[i][s] = INF
        }
    }

    // base case: one segment covering [0..i]
    for i := 0; i < n; i++ {
        dp[i][1] = cost[0][i]
    }

    // DP over number of segments
    for seg := 2; seg <= maxSeg; seg++ {
        // need at least seg elements to form seg non‑empty segments
        for i := seg - 1; i < n; i++ {
            best := INF
            // previous cut position p ends the (seg-1)th segment
            for p := seg - 2; p < i; p++ {
                if dp[p][seg-1] == INF {
                    continue
                }
                val := dp[p][seg-1] + cost[p+1][i]
                if val < best {
                    best = val
                }
            }
            dp[i][seg] = best
        }
    }

    // answer: minimal waste using up to k+1 segments
    ans := INF
    for seg := 1; seg <= maxSeg; seg++ {
        if dp[n-1][seg] < ans {
            ans = dp[n-1][seg]
        }
    }
    return int(ans)
}
```

## Ruby

```ruby
def min_space_wasted_k_resizing(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + nums[i] }

  waste = Array.new(n) { Array.new(n, 0) }
  (0...n).each do |l|
    max_val = 0
    (l...n).each do |r|
      max_val = [max_val, nums[r]].max
      total = pref[r + 1] - pref[l]
      waste[l][r] = (r - l + 1) * max_val - total
    end
  end

  max_seg = k + 1
  inf = 1 << 60
  dp = Array.new(max_seg + 1) { Array.new(n + 1, inf) }
  dp[0][0] = 0

  (1..n).each { |i| dp[1][i] = waste[0][i - 1] }

  (2..max_seg).each do |s|
    (s..n).each do |i|
      best = inf
      ((s - 1)..(i - 1)).each do |p|
        val = dp[s - 1][p] + waste[p][i - 1]
        best = val if val < best
      end
      dp[s][i] = best
    end
  end

  ans = inf
  (1..max_seg).each { |s| ans = dp[s][n] if dp[s][n] < ans }
  ans
end
```

## Scala

```scala
object Solution {
    def minSpaceWastedKResizing(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val cost = Array.ofDim[Int](n, n)
        for (l <- 0 until n) {
            var curMax = 0
            var curSum = 0L
            for (r <- l until n) {
                if (nums(r) > curMax) curMax = nums(r)
                curSum += nums(r).toLong
                val len = r - l + 1
                cost(l)(r) = ((len.toLong * curMax) - curSum).toInt
            }
        }

        val maxSeg = k + 1
        val INF = Int.MaxValue / 2
        val dp = Array.ofDim[Int](n + 1, maxSeg + 1)
        for (i <- 0 to n) java.util.Arrays.fill(dp(i), INF)
        dp(0)(0) = 0

        for (t <- 1 to n) {
            val limitSeg = math.min(t, maxSeg)
            for (seg <- 1 to limitSeg) {
                var best = INF
                var p = seg - 1
                while (p <= t - 1) {
                    val prev = dp(p)(seg - 1)
                    if (prev != INF) {
                        val cand = prev + cost(p)(t - 1)
                        if (cand < best) best = cand
                    }
                    p += 1
                }
                dp(t)(seg) = best
            }
        }

        var ans = INF
        for (seg <- 1 to maxSeg) {
            if (dp(n)(seg) < ans) ans = dp(n)(seg)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_space_wasted_k_resizing(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        // precompute waste for each segment [i..j] without resizing
        let mut cost = vec![vec![0i64; n]; n];
        for i in 0..n {
            let mut maxv = 0i64;
            let mut sum = 0i64;
            for j in i..n {
                let val = nums[j] as i64;
                if val > maxv { maxv = val; }
                sum += val;
                cost[i][j] = (j - i + 1) as i64 * maxv - sum;
            }
        }

        let max_seg = k as usize + 1; // number of segments allowed
        let inf: i64 = i64::MAX / 4;
        let mut dp = vec![vec![inf; n + 1]; max_seg + 1];
        dp[0][0] = 0;

        for s in 1..=max_seg {
            for i in 1..=n {
                if s - 1 > i - 1 { continue; } // not enough elements for previous segments
                let mut best = inf;
                for j in (s - 1)..i {
                    let prev = dp[s - 1][j];
                    if prev == inf { continue; }
                    let cand = prev + cost[j][i - 1];
                    if cand < best {
                        best = cand;
                    }
                }
                dp[s][i] = best;
            }
        }

        let mut ans = inf;
        for s in 1..=max_seg {
            if dp[s][n] < ans {
                ans = dp[s][n];
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-space-wasted-k-resizing nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         ;; prefix sums
         (pref (let ((v (make-vector (+ n 1) 0)))
                 (let loop ((i 0))
                   (when (< i n)
                     (vector-set! v (+ i 1) (+ (vector-ref v i) (vector-ref arr i)))
                     (loop (+ i 1))))
                 v))
         ;; cost[l][r] = waste if one segment covers l..r inclusive
         (cost (let ((c (make-vector n)))
                 (let loop-l ((l 0))
                   (when (< l n)
                     (let ((row (make-vector n 0)))
                       (let loop-r ((r l) (maxv 0))
                         (when (<= r (- n 1))
                           (set! maxv (max maxv (vector-ref arr r)))
                           (define sum (- (vector-ref pref (+ r 1)) (vector-ref pref l)))
                           (define len (+ (- r l) 1))
                           (vector-set! row r (- (* len maxv) sum))
                           (loop-r (+ r 1) maxv)))
                       (vector-set! c l row)
                       (loop-l (+ l 1))))
                 c))
         (maxSeg (min (+ k 1) n))
         (INF 1000000000000000)
         ;; dp[s][i] = min waste for first i elements using exactly s segments
         (dp (let ((d (make-vector (+ maxSeg 1))))
               (let loop-s ((s 0))
                 (when (<= s maxSeg)
                   (vector-set! d s (make-vector (+ n 1) INF))
                   (loop-s (+ s 1)))
                 d))))
    ;; base case: zero elements with zero segments costs zero
    (vector-set! (vector-ref dp 0) 0 0)
    ;; DP over number of segments
    (let loop-s ((s 1))
      (when (<= s maxSeg)
        (let ((dpPrev (vector-ref dp (- s 1)))
              (dpCurr (vector-ref dp s)))
          (let loop-i ((i 1))
            (when (<= i n)
              (let* ((best
                      (let loop-p ((p 0) (cur INF))
                        (if (< p i)
                            (let* ((prev (vector-ref dpPrev p))
                                   (cand (if (< prev INF)
                                             (+ prev (vector-ref (vector-ref cost p) (- i 1)))
                                             INF))
                                   (new-cur (if (< cand cur) cand cur)))
                              (loop-p (+ p 1) new-cur))
                            cur))))
                (vector-set! dpCurr i best)
                (loop-i (+ i 1))))))
        (loop-s (+ s 1))))
    ;; answer: minimum over at most maxSeg segments
    (let ((ans
            (let loop-s2 ((s 1) (cur INF))
              (if (> s maxSeg)
                  cur
                  (let ((val (vector-ref (vector-ref dp s) n)))
                    (loop-s2 (+ s 1) (if (< val cur) val cur)))))))
      ans)))
```

## Erlang

```erlang
-spec min_space_wasted_k_resizing([integer()], integer()) -> integer().
min_space_wasted_k_resizing(Nums, K) ->
    N = length(Nums),
    Prefix = build_prefix(Nums),
    NumTuple = list_to_tuple(Nums),
    PrefixTuple = list_to_tuple(Prefix),
    CostMap = build_cost(N, NumTuple, PrefixTuple, #{}),
    DP0 = init_dp(N, CostMap, #{}),
    DP = fill_dp(N, K, CostMap, DP0),
    min_answer(N, K, DP).

build_prefix(Nums) ->
    build_prefix_rev(Nums, [0], 0).

build_prefix_rev([], Acc, _) -> lists:reverse(Acc);
build_prefix_rev([H|T], Acc, Sum) ->
    NewSum = Sum + H,
    build_prefix_rev(T, [NewSum | Acc], NewSum).

build_cost(N, NumTuple, PrefixTuple, Map) ->
    build_cost_l(0, N, NumTuple, PrefixTuple, Map).

build_cost_l(L, N, _NumTuple, _PrefixTuple, Map) when L >= N -> Map;
build_cost_l(L, N, NumTuple, PrefixTuple, Map) ->
    {NewMap,_} = cost_inner(L, L, N-1, 0, NumTuple, PrefixTuple, Map),
    build_cost_l(L+1, N, NumTuple, PrefixTuple, NewMap).

cost_inner(_L, R, MaxR, CurMax, _NumTuple, _PrefixTuple, Map) when R > MaxR ->
    {Map, CurMax};
cost_inner(L, R, MaxR, CurMax, NumTuple, PrefixTuple, Map) ->
    Val = element(R+1, NumTuple),
    NewMax = erlang:max(CurMax, Val),
    SumSeg = element(R+1, PrefixTuple) - element(L, PrefixTuple),
    Waste = NewMax * (R-L+1) - SumSeg,
    UpdatedMap = maps:put({L,R}, Waste, Map),
    cost_inner(L, R+1, MaxR, NewMax, NumTuple, PrefixTuple, UpdatedMap).

init_dp(N, CostMap, DP) ->
    init_dp_i(1, N, CostMap, DP).

init_dp_i(I, N, _CostMap, DP) when I > N -> DP;
init_dp_i(I, N, CostMap, DP) ->
    Waste = maps:get({0, I-1}, CostMap),
    NewDP = maps:put({I,0}, Waste, DP),
    init_dp_i(I+1, N, CostMap, NewDP).

fill_dp(N, K, CostMap, DP) ->
    fill_j(1, K, N, CostMap, DP).

fill_j(J, MaxJ, _N, _CostMap, DP) when J > MaxJ -> DP;
fill_j(J, MaxJ, N, CostMap, DP) ->
    DP2 = compute_i(1, N, J, CostMap, DP),
    fill_j(J+1, MaxJ, N, CostMap, DP2).

compute_i(I, N, _J, _CostMap, DP) when I > N -> DP;
compute_i(I, N, J, CostMap, DP) ->
    Best = best_for_i(I, J, CostMap, DP),
    NewDP = maps:put({I,J}, Best, DP),
    compute_i(I+1, N, J, CostMap, NewDP).

best_for_i(I, J, CostMap, DP) ->
    Base = maps:get({0, I-1}, CostMap),
    best_over_p(1, I-1, I, J, CostMap, DP, Base).

best_over_p(P, MaxP, _I, _J, _CostMap, _DP, Best) when P > MaxP -> Best;
best_over_p(P, MaxP, I, J, CostMap, DP, Best) ->
    Prev = maps:get({P, J-1}, DP, 1 bsl 60),
    Seg = maps:get({P, I-1}, CostMap),
    Cand = Prev + Seg,
    NewBest = if Cand < Best -> Cand; true -> Best end,
    best_over_p(P+1, MaxP, I, J, CostMap, DP, NewBest).

min_answer(N, K, DP) ->
    min_answer_j(0, K, N, DP, 1 bsl 60).

min_answer_j(J, MaxJ, _N, _DP, Min) when J > MaxJ -> Min;
min_answer_j(J, MaxJ, N, DP, Min) ->
    Val = maps:get({N,J}, DP),
    NewMin = if Val < Min -> Val; true -> Min end,
    min_answer_j(J+1, MaxJ, N, DP, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_space_wasted_k_resizing(nums :: [integer], k :: integer) :: integer
  def min_space_wasted_k_resizing(nums, k) do
    n = length(nums)

    # prefix sums
    pref =
      Enum.reduce(nums, [0], fn x, acc ->
        [hd(acc) + x | acc]
      end)
      |> Enum.reverse()

    # waste[l][r] = (r-l+1)*max(l..r) - sum(l..r)
    waste =
      Enum.map(0..(n - 1), fn l ->
        {rev_row, _} =
          Enum.reduce(l..(n - 1), {[], 0}, fn r, {row_acc, cur_max} ->
            cur_max = max(cur_max, Enum.at(nums, r))
            sum = Enum.at(pref, r + 1) - Enum.at(pref, l)
            w = (r - l + 1) * cur_max - sum
            {[w | row_acc], cur_max}
          end)

        row = Enum.reverse(rev_row)
        zeros = List.duplicate(0, l)
        zeros ++ row
      end)

    large = 1 <<< 60

    # dp base: no resize (c = 0)
    dp0 =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, {i, 0}, Enum.at(Enum.at(waste, 0), i))
      end)

    dp_final =
      Enum.reduce(1..k, dp0, fn c, dp_acc ->
        Enum.reduce(0..(n - 1), dp_acc, fn i, dp2 ->
          if c > i do
            Map.put(dp2, {i, c}, large)
          else
            best =
              Enum.reduce(1..i, large, fn p, cur_best ->
                prev = Map.get(dp2, {p - 1, c - 1})
                w = Enum.at(Enum.at(waste, p), i)
                val = prev + w
                if val < cur_best, do: val, else: cur_best
              end)

            Map.put(dp2, {i, c}, best)
          end
        end)
      end)

    Enum.min(
      for c <- 0..k do
        Map.get(dp_final, {n - 1, c})
      end
    )
  end
end
```
