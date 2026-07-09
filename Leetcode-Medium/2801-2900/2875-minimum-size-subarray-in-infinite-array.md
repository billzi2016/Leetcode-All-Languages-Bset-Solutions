# 2875. Minimum Size Subarray in Infinite Array

## Cpp

```cpp
class Solution {
public:
    int minSizeSubarray(vector<int>& nums, int target) {
        using ll = long long;
        const ll INF = (1LL<<60);
        int n = nums.size();
        ll S = 0;
        for (int v : nums) S += v;

        // Case 1: subarray within a single copy (no wrap)
        int ans = INT_MAX;
        ll sum = 0;
        int left = 0;
        for (int right = 0; right < n; ++right) {
            sum += nums[right];
            while (left <= right && sum > target) {
                sum -= nums[left++];
            }
            if (sum == target) {
                ans = min(ans, right - left + 1);
            }
        }

        // Special handling when n == 1
        if (n == 1) {
            ll a = nums[0];
            if (target % a == 0) {
                ll len = target / a;
                ans = min<int>(ans, (int)len);
            }
            return ans == INT_MAX ? -1 : ans;
        }

        // Build map: remainder -> (prefix sum, length)
        unordered_map<ll, pair<ll,int>> mp;
        mp.reserve(n*2);
        mp[0] = {0LL, 0};
        ll pref = 0;
        for (int i = 0; i < n; ++i) {
            pref += nums[i];
            ll rem = pref % S;
            if (!mp.count(rem)) {
                mp[rem] = {pref, i + 1};
            }
        }

        // Helper lambda to try combine suffix and prefix
        auto tryCombine = [&](ll suffixSum, int lenSuffix) {
            if (suffixSum > target) return;
            ll need = target - suffixSum;               // remaining sum to be covered by prefixes and full periods
            ll rem = need % S;
            auto it = mp.find(rem);
            if (it == mp.end()) return;
            ll prefSum = it->second.first;
            int lenPref = it->second.second;
            if (prefSum > need) return;                // cannot exceed needed sum
            ll k = (need - prefSum) / S;               // number of whole periods in the middle
            ll totalLen = (ll)lenSuffix + (ll)lenPref + k * n;
            if (totalLen <= INT_MAX)
                ans = min<int>(ans, (int)totalLen);
        };

        // Empty suffix case
        tryCombine(0LL, 0);

        // Iterate over all possible non‑empty suffixes
        ll suffixSum = 0;
        int lenSuffix = 0;
        for (int i = n - 1; i >= 0; --i) {
            suffixSum += nums[i];
            ++lenSuffix;
            tryCombine(suffixSum, lenSuffix);
        }

        return ans == INT_MAX ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minSizeSubarray(int[] nums, int target) {
        int n = nums.length;
        long total = 0L;
        for (int v : nums) total += v;

        // Build doubled array
        int[] dbl = new int[2 * n];
        for (int i = 0; i < 2 * n; i++) {
            dbl[i] = nums[i % n];
        }

        // helper to find minimal length subarray with exact sum S within doubled array
        java.util.function.LongFunction<Integer> minLenForSum = (long S) -> {
            if (S == 0) return 0;
            long cur = 0L;
            int left = 0;
            int best = Integer.MAX_VALUE;
            for (int right = 0; right < dbl.length; right++) {
                cur += dbl[right];
                while (cur > S && left <= right) {
                    cur -= dbl[left++];
                }
                if (cur == S) {
                    int len = right - left + 1;
                    if (len < best) best = len;
                }
            }
            return best == Integer.MAX_VALUE ? -1 : best;
        };

        long maxCycles = target / total; // floor division
        int answer = Integer.MAX_VALUE;

        for (long cycles = Math.max(0, maxCycles - 1); cycles <= maxCycles; cycles++) {
            long remaining = target - cycles * total;
            if (remaining < 0) continue;
            int lenRem = minLenForSum.apply(remaining);
            if (lenRem != -1) {
                long totalLen = cycles * n + lenRem;
                if (totalLen <= Integer.MAX_VALUE && totalLen < answer) {
                    answer = (int) totalLen;
                }
            }
        }

        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
}
```

## Python

```python
class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)  # S
        if total == 0:
            return -1

        INF = 10 ** 18
        ans = INF

        base_k = target // total
        r = target % total

        # helper to find minimal length of subarray with exact sum X (X>0)
        def min_len_exact(X):
            if X <= 0:
                return INF
            left = 0
            cur = 0
            best = INF
            for right in range(2 * n):
                cur += nums[right % n]
                while cur > X and left <= right:
                    cur -= nums[left % n]
                    left += 1
                if cur == X:
                    length = right - left + 1
                    if length < best:
                        best = length
            return best

        # case: only whole periods
        if r == 0:
            ans = min(ans, base_k * n)

        # candidate sums to check
        candidates = []

        if r != 0:
            # sum equal to remainder (within one copy)
            candidates.append((r, 0))          # a//total = 0
            # sum equal to total + remainder (spans two copies)
            candidates.append((total + r, 1))   # a//total = 1
        else:
            # r == 0, need sums that are multiples of total but not zero length
            candidates.append((total, 1))       # one full copy
            if base_k >= 2:                     # two full copies possible within limit
                candidates.append((2 * total, 2))

        for X, a_div in candidates:
            if X > 2 * total:   # cannot be represented with at most two copies
                continue
            length_a = min_len_exact(X)
            if length_a == INF:
                continue
            k_remain = base_k - a_div
            if k_remain < 0:
                continue
            total_len = length_a + k_remain * n
            if total_len < ans:
                ans = total_len

        return -1 if ans == INF else ans
```

## Python3

```python
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)

        INF = 10**18
        ans = INF

        # Subarray completely inside one copy (no wrap)
        left = 0
        cur = 0
        for right in range(n):
            cur += nums[right]
            while cur > target and left <= right:
                cur -= nums[left]
                left += 1
            if cur == target:
                ans = min(ans, right - left + 1)

        # Build suffix sum -> minimal length map (including empty suffix)
        suffix_len = {0: 0}
        s = 0
        for i in range(n - 1, -1, -1):
            s += nums[i]
            length = n - i
            if s not in suffix_len:
                suffix_len[s] = length

        # Iterate over all prefixes (including empty)
        pref = 0
        for i in range(0, n + 1):
            if pref <= target:
                remaining = target - pref
                k = remaining // total if total else 0
                rem = remaining - k * total
                if rem in suffix_len:
                    length = i + suffix_len[rem] + k * n
                    ans = min(ans, length)
            if i < n:
                pref += nums[i]

        return -1 if ans == INF else ans
```

## C

```c
#include <stddef.h>
#include <limits.h>
#include <stdlib.h>

int minSizeSubarray(int* nums, int numsSize, int target) {
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];
    
    // Prefix sums
    long long *pref = (long long *)malloc((numsSize + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < numsSize; ++i) pref[i + 1] = pref[i] + nums[i];
    
    // Map prefix value to its index (first occurrence)
    struct Node { long long key; int idx; struct Node *next; };
    const size_t MOD = 200003; // a prime larger than typical n
    struct Node **hash = (struct Node **)calloc(MOD, sizeof(struct Node *));
    
    for (int i = 0; i <= numsSize; ++i) {
        size_t h = ((unsigned long long)pref[i]) % MOD;
        struct Node *node = (struct Node *)malloc(sizeof(struct Node));
        node->key = pref[i];
        node->idx = i;
        node->next = hash[h];
        hash[h] = node;
    }
    
    auto findIdx = [&](long long key)->int {
        size_t h = ((unsigned long long)key) % MOD;
        for (struct Node *p = hash[h]; p; p = p->next)
            if (p->key == key) return p->idx;
        return -1;
    };
    
    const long long INF = LLONG_MAX / 4;
    long long ans = INF;
    long long T = target;
    
    for (int i = 0; i < numsSize; ++i) {
        long long need = (T + pref[i]) % total;
        int r = findIdx(need);
        if (r == -1) continue;
        long long numerator = T + pref[i] - pref[r];
        if (numerator < 0) continue;
        if (numerator % total != 0) continue; // safety
        long long q = numerator / total;
        long long len = q * numsSize + (r - i);
        if (len <= 0) continue;
        if (len < ans) ans = len;
    }
    
    // free hash table
    for (size_t i = 0; i < MOD; ++i) {
        struct Node *p = hash[i];
        while (p) {
            struct Node *tmp = p;
            p = p->next;
            free(tmp);
        }
    }
    free(hash);
    free(pref);
    
    if (ans == INF) return -1;
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinSizeSubarray(int[] nums, int target) {
        int n = nums.Length;
        long total = 0;
        foreach (int v in nums) total += v;
        long tgt = target;

        // Prefix sums and remainder to minimal length map
        var remToLen = new Dictionary<long, int>();
        long prefSum = 0;
        remToLen[0] = 0; // empty prefix

        for (int i = 0; i < n; i++) {
            prefSum += nums[i];
            long rem = prefSum % total;
            if (!remToLen.ContainsKey(rem)) {
                remToLen[rem] = i + 1; // length up to index i
            }
        }

        // Prefix sums array for suffix calculations
        long[] prefix = new long[n + 1];
        prefix[0] = 0;
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        const long INF = long.MaxValue / 4;
        long answer = INF;

        // Iterate over possible suffix start positions
        for (int i = 0; i <= n; i++) {
            long suffixSum = total - prefix[i];          // sum from i to end of one copy
            int suffixLen = n - i;                       // length of that suffix
            long remaining = tgt - suffixSum;
            if (remaining < 0) continue;

            long fullCopies = remaining / total;
            long rem = remaining % total;

            if (remToLen.TryGetValue(rem, out int prefixLen)) {
                long curLen = suffixLen + fullCopies * n + prefixLen;
                if (curLen < answer) answer = curLen;
            }
        }

        return answer == INF ? -1 : (int)answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var minSizeSubarray = function(nums, target) {
    const n = nums.length;
    let ans = Infinity;

    // Case 1: subarray completely inside one copy (no wrap)
    let left = 0, sum = 0;
    for (let right = 0; right < n; ++right) {
        sum += nums[right];
        while (sum > target && left <= right) {
            sum -= nums[left++];
        }
        if (sum === target) {
            ans = Math.min(ans, right - left + 1);
        }
    }

    // Prefix sums map: sum -> minimal length
    const prefMap = new Map();
    prefMap.set(0, 0);
    let curPref = 0;
    for (let i = 0; i < n; ++i) {
        curPref += nums[i];
        if (!prefMap.has(curPref)) {
            prefMap.set(curPref, i + 1);
        }
    }
    const totalSum = curPref; // sum of whole array

    // Iterate over all possible suffixes (including empty)
    let suffixSum = 0;
    for (let i = n; i >= 0; --i) {
        const suffixLen = n - i; // length of suffix starting at i
        if (i < n) suffixSum += nums[i]; // accumulate when moving leftwards

        const remaining = target - suffixSum;
        if (remaining < 0) continue;

        const k = Math.floor(remaining / totalSum);
        const remMod = remaining % totalSum;

        if (prefMap.has(remMod)) {
            const totalLen = suffixLen + prefMap.get(remMod) + k * n;
            ans = Math.min(ans, totalLen);
        }
    }

    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minSizeSubarray(nums: number[], target: number): number {
    const n = nums.length;
    const total = nums.reduce((a, b) => a + b, 0);
    let ans = Number.MAX_SAFE_INTEGER;

    // Sliding window on two concatenated copies to handle wrap‑around subarrays of length ≤ n
    const arr = nums.concat(nums);
    let left = 0;
    let sum = 0;
    for (let right = 0; right < arr.length; ++right) {
        sum += arr[right];
        while (sum > target && left <= right) {
            sum -= arr[left++];
        }
        // keep window size ≤ n
        while (right - left + 1 > n) {
            sum -= arr[left++];
        }
        if (sum === target) {
            const len = right - left + 1;
            if (len < ans) ans = len;
        }
    }

    // Prefix sums map: sum -> length
    const prefMap = new Map<number, number>();
    let cur = 0;
    prefMap.set(0, 0);
    for (let i = 0; i < n; ++i) {
        cur += nums[i];
        prefMap.set(cur, i + 1);
    }

    // Prefix sums array for quick suffix computation
    const prefixSums = new Array<number>(n + 1);
    prefixSums[0] = 0;
    for (let i = 1; i <= n; ++i) {
        prefixSums[i] = prefixSums[i - 1] + nums[i - 1];
    }

    // Consider subarrays that may contain whole cycles
    for (let i = 0; i <= n; ++i) { // i is start index within a period, i=n means empty suffix
        const suffSum = total - (i === n ? total : prefixSums[i]);
        const lenSuff = n - i;
        const remaining = target - suffSum;
        if (remaining < 0) continue;

        const k = Math.floor(remaining / total);
        const prefNeeded = remaining - k * total; // 0 ≤ prefNeeded ≤ total
        if (prefMap.has(prefNeeded)) {
            const lenPref = prefMap.get(prefNeeded)!;
            const length = lenSuff + k * n + lenPref;
            if (length < ans) ans = length;
        }
    }

    return ans === Number.MAX_SAFE_INTEGER ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function minSizeSubarray($nums, $target) {
        $n = count($nums);
        // prefix sums and map sum -> length (first occurrence)
        $pref = array_fill(0, $n + 1, 0);
        $sumToLen = [];
        $sumToLen[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] + $nums[$i];
            $sumToLen[$pref[$i + 1]] = $i + 1; // unique because nums > 0
        }
        $total = $pref[$n];

        $ans = PHP_INT_MAX;

        // Case 1: subarray inside a single copy (no wrap)
        $left = 0;
        $curr = 0;
        for ($right = 0; $right < $n; $right++) {
            $curr += $nums[$right];
            while ($curr > $target && $left <= $right) {
                $curr -= $nums[$left];
                $left++;
            }
            if ($curr == $target) {
                $len = $right - $left + 1;
                if ($len < $ans) $ans = $len;
            }
        }

        // Case 2: subarray that may wrap and include whole cycles
        for ($i = 0; $i <= $n; $i++) {
            $suffixSum = $total - $pref[$i];          // sum from i to end of a copy
            $lenSuffix = $n - $i;                     // length of that suffix
            $remaining = $target - $suffixSum;
            if ($remaining < 0) continue;

            // number of full cycles after the suffix
            $k = intdiv($remaining, $total);
            $need = $remaining - $k * $total;        // required prefix sum (0 <= need < total)

            if (isset($sumToLen[$need])) {
                $len = $lenSuffix + $k * $n + $sumToLen[$need];
                if ($len < $ans) $ans = $len;
            }
        }

        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minSizeSubarray(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var total = 0
        for v in nums { total += v }
        
        // Prefix sums map: sum -> minimal length achieving this sum from start
        var prefMap = [Int:Int]()
        var curPref = 0
        prefMap[0] = 0
        for i in 0..<n {
            curPref += nums[i]
            if prefMap[curPref] == nil {
                prefMap[curPref] = i + 1
            }
        }
        
        // Suffix sums list (including empty suffix)
        var suffixes: [(sum: Int, len: Int)] = []
        suffixes.append((0, 0))
        var curSuf = 0
        for idx in stride(from: n - 1, through: 0, by: -1) {
            curSuf += nums[idx]
            let length = n - idx
            suffixes.append((curSuf, length))
        }
        
        let targetLL = Int64(target)
        let totalLL = Int64(total)
        var best: Int64 = Int64.max
        
        for (sufSum, sufLen) in suffixes {
            let sumLL = Int64(sufSum)
            if sumLL > targetLL { continue }
            let remaining = targetLL - sumLL
            // total is always > 0 because nums[i] >= 1
            let k = remaining / totalLL
            let r = remaining % totalLL
            if let prefLen = prefMap[Int(r)] {
                let curLen = Int64(sufLen) + k * Int64(n) + Int64(prefLen)
                if curLen < best { best = curLen }
            }
        }
        
        return best == Int64.max ? -1 : Int(best)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSizeSubarray(nums: IntArray, target: Int): Int {
        val n = nums.size
        var minLen = Int.MAX_VALUE
        var left = 0L
        var sum = 0L
        var rightIdx = 0
        // minimum element to bound the needed repetitions
        var minVal = Int.MAX_VALUE
        for (v in nums) if (v < minVal) minVal = v

        // maximum number of elements we may need to examine:
        // at most one full copy plus enough extra elements to reach target using the smallest value.
        val maxSteps = n + target / minVal + 2
        while (rightIdx < maxSteps) {
            sum += nums[rightIdx % n].toLong()
            rightIdx++
            while (sum >= target) {
                if (sum == target.toLong()) {
                    val len = rightIdx - left.toInt()
                    if (len < minLen) minLen = len
                }
                sum -= nums[(left % n).toInt()].toLong()
                left++
            }
        }
        return if (minLen == Int.MAX_VALUE) -1 else minLen
    }
}
```

## Dart

```dart
class Solution {
  int minSizeSubarray(List<int> nums, int target) {
    int n = nums.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = pref[i] + nums[i];
    }
    int total = pref[n];

    const int INF = 1 << 60;
    int ans = INF;

    // Case 1: subarray within a single copy using sliding window
    int left = 0;
    int sum = 0;
    for (int right = 0; right < n; ++right) {
      sum += nums[right];
      while (sum > target && left <= right) {
        sum -= nums[left];
        left++;
      }
      if (sum == target) {
        ans = ans < (right - left + 1) ? ans : (right - left + 1);
      }
    }

    // Map prefix sum to smallest index
    Map<int, int> prefIndex = {};
    for (int i = 0; i <= n; ++i) {
      if (!prefIndex.containsKey(pref[i])) {
        prefIndex[pref[i]] = i;
      }
    }

    // Case 2: subarray crossing copies (suffix + k*total + prefix)
    for (int a = 0; a < n; ++a) {
      int suffix = total - pref[a];
      if (suffix > target) continue;
      int remaining = target - suffix;
      int k = remaining ~/ total;
      int needPrefix = remaining - k * total;

      if (needPrefix == 0) {
        int len = (n - a) + k * n;
        ans = ans < len ? ans : len;
      } else {
        int? b = prefIndex[needPrefix];
        if (b != null) {
          int len = (n - a) + k * n + b;
          ans = ans < len ? ans : len;
        }
      }
    }

    // Case 3: subarray consisting of whole cycles only
    if (target % total == 0) {
      int cycles = target ~/ total;
      int len = cycles * n;
      ans = ans < len ? ans : len;
    }

    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minSizeSubarray(nums []int, target int) int {
    n := len(nums)
    pref := make([]int64, n+1)
    for i := 0; i < n; i++ {
        pref[i+1] = pref[i] + int64(nums[i])
    }
    totalSum := pref[n]
    // map each prefix sum value to its earliest index
    idxMap := make(map[int64]int, n+1)
    for i := 0; i <= n; i++ {
        if _, ok := idxMap[pref[i]]; !ok {
            idxMap[pref[i]] = i
        }
    }

    const INF int64 = 1<<62 - 1
    ans := INF
    target64 := int64(target)

    for i := 0; i < n; i++ {
        base := pref[i]                     // sum up to position i (exclusive)
        needTotal := base + target64        // cumulative sum we need at end position
        rem := needTotal % totalSum         // required remainder modulo totalSum
        idx, ok := idxMap[rem]
        if !ok {
            continue
        }
        cycles := (needTotal - rem) / totalSum // number of full periods between start and end
        length := cycles*int64(n) + int64(idx-i)
        if length > 0 && length < ans {
            ans = length
        }
    }

    if ans == INF {
        return -1
    }
    return int(ans)
}
```

## Ruby

```ruby
def min_size_subarray(nums, target)
  n = nums.length
  total = nums.sum

  find_min_len = lambda do |need|
    return nil if need <= 0
    arr = nums + nums
    left = 0
    cur = 0
    min_len = nil
    (0...arr.length).each do |right|
      cur += arr[right]
      while cur > need && left <= right
        cur -= arr[left]
        left += 1
      end
      if cur == need
        len = right - left + 1
        min_len = len if min_len.nil? || len < min_len
      end
    end
    min_len
  end

  rem = target % total
  full_cycles = target / total

  if rem == 0
    ans = full_cycles * n
    # try to replace one whole cycle with a shorter subarray that also sums to total
    len_total = find_min_len.call(total)
    if len_total && len_total < n && full_cycles > 0
      cand = (full_cycles - 1) * n + len_total
      ans = [ans, cand].min
    end
    ans
  else
    len_rem = find_min_len.call(rem)
    return -1 unless len_rem
    full_cycles * n + len_rem
  end
end
```

## Scala

```scala
object Solution {
    def minSizeSubarray(nums: Array[Int], target: Int): Int = {
        val n = nums.length
        val totalSum: Long = nums.map(_.toLong).sum
        val t: Long = target.toLong

        // Map from remainder to (earliest prefix sum, its length)
        import scala.collection.mutable
        val remMap = mutable.HashMap[Long, (Long, Int)]()
        remMap.put(0L, (0L, 0)) // empty prefix

        var prefSum: Long = 0L
        for (i <- 1 to n) {
            prefSum += nums(i - 1).toLong
            val r = prefSum % totalSum
            if (!remMap.contains(r)) {
                remMap.put(r, (prefSum, i))
            }
        }

        var answer: Long = Long.MaxValue

        var suffixSum: Long = 0L
        var suffixLen: Int = 0

        // iterate suffixes from empty to full array
        for (i <- n to 0 by -1) {
            val remaining = t - suffixSum
            if (remaining >= 0) {
                val r = remaining % totalSum
                remMap.get(r).foreach { case (preSum, preLen) =>
                    if (preSum <= remaining) {
                        val k: Long = (remaining - preSum) / totalSum
                        val totalLen: Long = suffixLen.toLong + preLen.toLong + k * n.toLong
                        if (totalLen < answer) answer = totalLen
                    }
                }
            }
            if (i > 0) {
                suffixSum += nums(i - 1).toLong
                suffixLen += 1
            }
        }

        if (answer == Long.MaxValue) -1 else answer.toInt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn min_size_subarray(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let target_i64 = target as i64;
        let mut total_sum: i64 = 0;
        for &v in &nums {
            total_sum += v as i64;
        }

        // Prefix sums and map sum -> length
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let mut pre_map: HashMap<i64, usize> = HashMap::new();
        for i in 1..=n {
            pre_map.insert(pref[i], i);
        }

        const INF: i64 = i64::MAX / 4;
        let mut ans = INF;

        // Sliding window on at most two periods (covers cases without many full cycles)
        let mut l: usize = 0;
        let mut cur: i64 = 0;
        let limit = 2 * n;
        for r in 0..limit {
            cur += nums[r % n] as i64;
            while cur > target_i64 && l <= r {
                cur -= nums[l % n] as i64;
                l += 1;
            }
            if cur == target_i64 {
                let len = (r - l + 1) as i64;
                if len < ans {
                    ans = len;
                }
            }
        }

        // Subarray consisting only of full cycles
        if total_sum != 0 && target_i64 % total_sum == 0 {
            let k = target_i64 / total_sum;
            let len = k * n as i64;
            if len < ans {
                ans = len;
            }
        }

        // Cases with suffix + k full cycles + prefix
        for i in 0..=n {
            let suff_sum = if i < n { total_sum - pref[i] } else { 0 };
            let len_suff = (n - i) as i64; // zero when i == n

            if suff_sum > target_i64 {
                continue;
            }
            let remaining = target_i64 - suff_sum;
            let k = remaining / total_sum;
            let r = remaining % total_sum;

            if r == 0 {
                let len = len_suff + k * n as i64;
                if len < ans {
                    ans = len;
                }
            } else if let Some(&len_pre) = pre_map.get(&(r as i64)) {
                let len = len_suff + k * n as i64 + len_pre as i64;
                if len < ans {
                    ans = len;
                }
            }
        }

        if ans == INF {
            -1
        } else {
            ans as i32
        }
    }
}
```

## Racket

```racket
(define/contract (min-size-subarray nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         ;; total sum of one copy
         (total (let loop ((i 0) (s 0))
                  (if (= i n)
                      s
                      (loop (+ i 1) (+ s (vector-ref vec i))))))
         ;; shortest subarray completely inside one copy (sliding window)
         (best-within (let loop ((left 0) (right 0) (curr 0) (best #f))
                        (cond
                          [(= left n) best]
                          [(and (< right n) (< curr target))
                           (loop left (+ right 1) (+ curr (vector-ref vec right)) best)]
                          [(= curr target)
                           (let ((len (- right left)))
                             (loop left (+ right 1)
                                   (+ curr (if (< right n) (vector-ref vec right) 0))
                                   (if best (min best len) len)))]
                          [else ; curr > target or right == n
                           (if (= left right)
                               (loop (+ left 1) (+ right 1) 0 best)
                               (loop (+ left 1) right (- curr (vector-ref vec left)) best))])))
         ;; map remainder -> (sum . length) for prefixes, keep minimal sum/length per remainder
         (pref-hash (let ((h (make-hash)))
                      (hash-set! h 0 (cons 0 0))
                      (let loop ((i 0) (s 0))
                        (when (< i n)
                          (set! s (+ s (vector-ref vec i)))
                          (define rem (modulo s total))
                          (unless (hash-has-key? h rem)
                            (hash-set! h rem (cons s (+ i 1)))) ; length = i+1
                          (loop (+ i 1) s)))
                      h))
         ;; iterate over all suffixes (including empty) and combine with prefix info
         (best-all (let loop ((i n) (suff-sum 0) (best best-within))
                     (if (< i 0)
                         best
                         (let* ((suff-len (- n i))          ; length of suffix starting at i (0 when i=n)
                                (remaining (- target suff-sum)))
                           (define new-best
                             (if (>= remaining 0)
                                 (let* ((rem (modulo remaining total))
                                        (pref-pair (hash-ref pref-hash rem #f)))
                                   (if pref-pair
                                       (let* ((p (car pref-pair))
                                              (lenp (cdr pref-pair)))
                                         (if (<= p remaining)
                                             (let* ((cycles (quotient (- remaining p) total))
                                                    (total-len (+ suff-len lenp (* cycles n))))
                                               (if best (min best total-len) total-len))
                                             best))
                                       best))
                                 best)))
                           (loop (- i 1)
                                 (+ suff-sum (if (= i n) 0 (vector-ref vec i)))
                                 new-best))))))
    (if best-all best-all -1)))
```

## Erlang

```erlang
-spec min_size_subarray(Nums :: [integer()], Target :: integer()) -> integer().
min_size_subarray(Nums, Target) ->
    N = length(Nums),
    %% Build prefix sums list and map sum->index (first occurrence)
    {PrefList, PrefMap, Total} = build_prefix(Nums, 0, [], #{}, 0),
    PrefTuple = list_to_tuple(PrefList), % 1‑based indexing
    Infinity = 1 bsl 60,
    Min0 = 
        case Total of
            0 -> Infinity; % not possible as nums[i] >= 1
            _ ->
                K0 = Target div Total,
                R0 = Target - K0 * Total,
                LenBase0 = K0 * N,
                case R0 of
                    0 -> LenBase0;
                    _ ->
                        case maps:find(R0, PrefMap) of
                            {ok, J} -> LenBase0 + (J + 1);
                            error -> Infinity
                        end
                end
        end,
    Min = find_min(N, Total, Target, PrefTuple, PrefMap, Min0, 0),
    case Min of
        X when X < Infinity -> X;
        _ -> -1
    end.

%% Recursively build prefix sums list (in order) and map sum->index.
build_prefix([], _, AccListRev, Map, Sum) ->
    {lists:reverse(AccListRev), Map, Sum};
build_prefix([H|T], Index, AccListRev, Map, AccSum) ->
    NewSum = AccSum + H,
    NewMap = maps:put(NewSum, Index, Map),
    build_prefix(T, Index + 1, [NewSum | AccListRev], NewMap, NewSum).

%% Iterate over start positions i = 0 .. N-1 to update minimal length.
find_min(N, Total, Target, PrefTuple, PrefMap, Min, I) when I < N ->
    PrevSum =
        case I of
            0 -> 0;
            _ -> erlang:element(I, PrefTuple)
        end,
    Suffix = Total - PrevSum,
    NewMin =
        if
            Suffix > Target ->
                Min; % cannot start here
            true ->
                RemTotal = Target - Suffix,
                K = RemTotal div Total,
                R = RemTotal - K * Total,
                LenBase = (N - I) + K * N,
                case R of
                    0 ->
                        min(Min, LenBase);
                    _ ->
                        case maps:find(R, PrefMap) of
                            {ok, J} -> min(Min, LenBase + (J + 1));
                            error -> Min
                        end
                end
        end,
    find_min(N, Total, Target, PrefTuple, PrefMap, NewMin, I + 1);
find_min(_, _, _, _, _, Min, _) ->
    Min.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_size_subarray(nums :: [integer], target :: integer) :: integer
  def min_size_subarray(nums, target) do
    n = length(nums)
    total = Enum.sum(nums)

    q = div(target, total)
    r = rem(target, total)
    base_len = q * n

    if r == 0 do
      base_len
    else
      double = nums ++ nums
      tup = List.to_tuple(double)
      len_double = tuple_size(tup)

      {min_len, _} =
        Enum.reduce(0..len_double - 1, {:infinity, %{left: 0, sum: 0}}, fn right, {cur_min, acc} ->
          sum = acc.sum + elem(tup, right)
          left = acc.left

          {sum2, left2} = shrink(sum, left, tup, right, r, n)

          cur_min =
            if sum2 == r do
              len = right - left2 + 1
              if cur_min == :infinity or len < cur_min, do: len, else: cur_min
            else
              cur_min
            end

          {cur_min, %{left: left2, sum: sum2}}
        end)

      if min_len == :infinity do
        -1
      else
        base_len + min_len
      end
    end
  end

  defp shrink(sum, left, tup, right, target, n) do
    cond do
      sum > target or (right - left + 1) > n ->
        shrink(sum - elem(tup, left), left + 1, tup, right, target, n)

      true ->
        {sum, left}
    end
  end
end
```
