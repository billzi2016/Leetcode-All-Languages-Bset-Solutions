# 2902. Count of Sub-Multisets With Bounded Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countSubMultisets(vector<int>& nums, int l, int r) {
        const int MOD = 1'000'000'007;
        int maxVal = 0;
        for (int x : nums) maxVal = max(maxVal, x);
        vector<int> freq(maxVal + 1, 0);
        long long totalSum = 0;
        int zeroCnt = 0;
        for (int x : nums) {
            if (x == 0) ++zeroCnt;
            else {
                ++freq[x];
                totalSum += x;
            }
        }
        int S = (int)totalSum; // sum of positive numbers, <= 20000
        vector<int> dp(S + 1, 0), ndp(S + 1, 0);
        dp[0] = 1;

        for (int v = 1; v <= maxVal; ++v) {
            int c = freq[v];
            if (c == 0) continue;
            fill(ndp.begin(), ndp.end(), 0);
            for (int mod = 0; mod < v; ++mod) {
                long long window = 0;
                int idx = 0;
                for (int s = mod; s <= S; s += v, ++idx) {
                    // add current dp[s] to sliding window
                    window += dp[s];
                    if (window >= MOD) window -= MOD;
                    // remove element that is out of the window size c+1
                    if (idx > c) {
                        int remPos = s - (c + 1) * v;
                        window -= dp[remPos];
                        if (window < 0) window += MOD;
                    }
                    ndp[s] = (int)window;
                }
            }
            dp.swap(ndp);
        }

        long long ans = 0;
        for (int s = l; s <= r && s <= S; ++s) {
            ans += dp[s];
            if (ans >= MOD) ans -= MOD;
        }
        // incorporate zeros
        ans = ans * (zeroCnt + 1LL) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countSubMultisets(java.util.List<Integer> nums, int l, int r) {
        final int MOD = 1_000_000_007;
        final int MAX_VAL = 20000;
        int[] freq = new int[MAX_VAL + 1];
        int totalSum = 0;
        for (int x : nums) {
            freq[x]++;
            totalSum += x;
        }
        int S = totalSum;
        int[] dp = new int[S + 1];
        dp[0] = 1;

        for (int v = 0; v <= MAX_VAL; ++v) {
            int cnt = freq[v];
            if (cnt == 0) continue;
            if (v == 0) {
                long mult = cnt + 1L;
                for (int i = 0; i <= S; ++i) {
                    dp[i] = (int) ((dp[i] * mult) % MOD);
                }
                continue;
            }
            int[] ndp = new int[S + 1];
            for (int mod = 0; mod < v; ++mod) {
                long sum = 0;
                for (int k = 0, idx = mod; idx <= S; ++k, idx += v) {
                    sum += dp[idx];
                    if (k - cnt - 1 >= 0) {
                        int removeIdx = mod + (k - cnt - 1) * v;
                        sum -= dp[removeIdx];
                    }
                    ndp[idx] = (int) (sum % MOD);
                }
            }
            dp = ndp;
        }

        long ans = 0;
        int start = Math.max(l, 0);
        int end = Math.min(r, S);
        for (int s = start; s <= end; ++s) {
            ans += dp[s];
            if (ans >= MOD) ans -= MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubMultisets(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        total_sum = sum(nums)
        from collections import Counter, deque
        freq = Counter(nums)

        dp = [0] * (total_sum + 1)
        dp[0] = 1

        for val, cnt in freq.items():
            if val == 0:
                factor = cnt + 1
                for i in range(total_sum + 1):
                    dp[i] = dp[i] * factor % MOD
                continue

            ndp = [0] * (total_sum + 1)
            for rem in range(val):
                dq = deque()
                window = 0
                for s in range(rem, total_sum + 1, val):
                    window = (window + dp[s]) % MOD
                    dq.append(dp[s])
                    if len(dq) > cnt + 1:
                        removed = dq.popleft()
                        window = (window - removed) % MOD
                    ndp[s] = window
            dp = ndp

        r = min(r, total_sum)
        ans = sum(dp[l:r+1]) % MOD
        return ans
```

## Python3

```python
import sys
from collections import Counter
from typing import List

MOD = 10**9 + 7

class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        total_sum = sum(nums)
        dp = [0] * (total_sum + 1)
        dp[0] = 1
        freq = Counter(nums)

        for v, c in freq.items():
            if v == 0:
                factor = c + 1
                for i in range(total_sum + 1):
                    dp[i] = dp[i] * factor % MOD
                continue

            newdp = [0] * (total_sum + 1)
            step = v
            for rem in range(step):
                window = 0
                idxs = list(range(rem, total_sum + 1, step))
                for t, idx in enumerate(idxs):
                    window = (window + dp[idx]) % MOD
                    if t > c:
                        remove_idx = idxs[t - c - 1]
                        window = (window - dp[remove_idx]) % MOD
                    newdp[idx] = window
            dp = newdp

        l = max(l, 0)
        r = min(r, total_sum)
        if l > r:
            return 0
        ans = sum(dp[l:r+1]) % MOD
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int countSubMultisets(int* nums, int numsSize, int l, int r) {
    const int MOD = 1000000007;
    static int freq[20001];
    memset(freq, 0, sizeof(freq));
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        freq[v]++;
        total += v;
    }
    int maxSum = total;
    int *dp = (int*)calloc(maxSum + 1, sizeof(int));
    int *ndp = (int*)calloc(maxSum + 1, sizeof(int));
    dp[0] = 1;

    /* handle zeros separately */
    if (freq[0] > 0) {
        long long mult = freq[0] + 1LL;
        for (int s = 0; s <= maxSum; ++s) {
            dp[s] = (int)((dp[s] * mult) % MOD);
        }
    }

    for (int val = 1; val <= 20000; ++val) {
        int cnt = freq[val];
        if (cnt == 0) continue;
        memset(ndp, 0, (maxSum + 1) * sizeof(int));
        for (int mod = 0; mod < val; ++mod) {
            long long window = 0;
            int k = 0;
            for (int s = mod; s <= maxSum; s += val, ++k) {
                window += dp[s];
                if (window >= MOD) window -= MOD;
                if (k - cnt - 1 >= 0) {
                    int remPos = mod + (k - cnt - 1) * val;
                    window -= dp[remPos];
                    if (window < 0) window += MOD;
                }
                ndp[s] = (int)window;
            }
        }
        int *tmp = dp; dp = ndp; ndp = tmp;
    }

    long long ans = 0;
    if (l > maxSum) {
        ans = 0;
    } else {
        if (r > maxSum) r = maxSum;
        for (int s = l; s <= r; ++s) {
            ans += dp[s];
            if (ans >= MOD) ans -= MOD;
        }
    }

    free(dp);
    free(ndp);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    public int CountSubMultisets(IList<int> nums, int l, int r) {
        int maxVal = 20000;
        int[] freq = new int[maxVal + 1];
        int totalSum = 0;
        foreach (int x in nums) {
            freq[x]++;
            totalSum += x;
        }
        if (totalSum > maxVal) totalSum = maxVal; // safety, though constraints guarantee <=20000

        int[] dp = new int[totalSum + 1];
        dp[0] = 1;

        // handle zero value separately
        int zeroCount = freq[0];
        if (zeroCount > 0) {
            long factor = zeroCount + 1L;
            for (int i = 0; i <= totalSum; i++) {
                dp[i] = (int)(dp[i] * factor % MOD);
            }
        }

        // process non-zero values
        for (int v = 1; v <= maxVal; v++) {
            int c = freq[v];
            if (c == 0) continue;
            int[] ndp = new int[totalSum + 1];
            for (int rem = 0; rem < v; rem++) {
                long window = 0;
                int t = 0;
                for (int idx = rem; idx <= totalSum; idx += v, t++) {
                    // add current dp value to the sliding window
                    window += dp[idx];
                    if (window >= MOD) window -= MOD;

                    // remove value that falls out of the window size (c+1)
                    if (t > c) {
                        int removeIdx = idx - (c + 1) * v;
                        window -= dp[removeIdx];
                        if (window < 0) window += MOD;
                    }
                    ndp[idx] = (int)window;
                }
            }
            dp = ndp;
        }

        // compute answer
        long ans = 0;
        int upper = Math.Min(r, totalSum);
        for (int s = l; s <= upper; s++) {
            ans += dp[s];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var countSubMultisets = function(nums, l, r) {
    const MOD = 1000000007;
    let zeroCount = 0;
    const freq = new Map();
    let totalSum = 0;
    for (const x of nums) {
        if (x === 0) {
            ++zeroCount;
        } else {
            totalSum += x;
            freq.set(x, (freq.get(x) || 0) + 1);
        }
    }
    const limit = Math.min(r, totalSum);
    let dp = new Array(limit + 1).fill(0);
    dp[0] = 1;

    for (const [v, c] of freq.entries()) {
        const newdp = new Array(limit + 1).fill(0);
        for (let rem = 0; rem < v && rem <= limit; ++rem) {
            let sum = 0;
            for (let idx = rem, k = 0; idx <= limit; idx += v, ++k) {
                sum = (sum + dp[idx]) % MOD;
                if (k - c - 1 >= 0) {
                    const removeIdx = rem + (k - c - 1) * v;
                    sum = (sum - dp[removeIdx]) % MOD;
                    if (sum < 0) sum += MOD;
                }
                newdp[idx] = sum;
            }
        }
        dp = newdp;
    }

    const factor = (zeroCount + 1) % MOD;
    for (let i = 0; i <= limit; ++i) {
        dp[i] = (dp[i] * factor) % MOD;
    }

    let ans = 0;
    const start = Math.max(l, 0);
    const end = Math.min(r, limit);
    for (let s = start; s <= end; ++s) {
        ans += dp[s];
        if (ans >= MOD) ans -= MOD;
    }
    return ans % MOD;
};
```

## Typescript

```typescript
function countSubMultisets(nums: number[], l: number, r: number): number {
    const MOD = 1_000_000_007;
    const freq = new Map<number, number>();
    let totalSum = 0;
    for (const x of nums) {
        freq.set(x, (freq.get(x) ?? 0) + 1);
        if (x > 0) totalSum += x;
    }
    const zeroCount = freq.get(0) ?? 0;

    let dp: number[] = new Array(totalSum + 1).fill(0);
    dp[0] = 1;

    for (const [value, count] of freq.entries()) {
        if (value === 0) continue;
        const v = value;
        const c = count;
        const ndp: number[] = new Array(totalSum + 1).fill(0);
        for (let mod = 0; mod < v; ++mod) {
            let windowSum = 0;
            for (let k = 0, idx = mod; idx <= totalSum; ++k, idx += v) {
                windowSum += dp[idx];
                if (windowSum >= MOD) windowSum -= MOD;
                if (k > c) {
                    const removeIdx = idx - (c + 1) * v;
                    windowSum -= dp[removeIdx];
                    if (windowSum < 0) windowSum += MOD;
                }
                ndp[idx] = windowSum;
            }
        }
        dp = ndp;
    }

    let ans = 0;
    const start = Math.max(l, 0);
    const end = Math.min(r, totalSum);
    for (let s = start; s <= end; ++s) {
        ans += dp[s];
        if (ans >= MOD) ans -= MOD;
    }
    const factor = (zeroCount + 1) % MOD;
    return (ans * factor) % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function countSubMultisets($nums, $l, $r) {
        $mod = 1000000007;
        $maxSum = array_sum($nums);
        // frequency map
        $freq = [];
        foreach ($nums as $val) {
            if (!isset($freq[$val])) $freq[$val] = 0;
            $freq[$val]++;
        }

        $dp = array_fill(0, $maxSum + 1, 0);
        $dp[0] = 1;

        foreach ($freq as $v => $c) {
            $ndp = array_fill(0, $maxSum + 1, 0);
            for ($rem = 0; $rem < $v; $rem++) {
                $window = 0;
                $t = 0;
                for ($idx = $rem; $idx <= $maxSum; $idx += $v, $t++) {
                    // add current dp value to window
                    $window += $dp[$idx];
                    if ($window >= $mod) $window -= $mod;

                    // remove value that exceeds count c
                    if ($t > $c) {
                        $removeIdx = $rem + ($t - $c - 1) * $v;
                        $window -= $dp[$removeIdx];
                        if ($window < 0) $window += $mod;
                    }
                    $ndp[$idx] = $window;
                }
            }
            $dp = $ndp;
        }

        $ans = 0;
        $upper = min($r, $maxSum);
        for ($s = $l; $s <= $upper; $s++) {
            $ans += $dp[$s];
            if ($ans >= $mod) $ans -= $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSubMultisets(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        let MOD = 1_000_000_007
        var freq = [Int:Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        let zeroCount = freq[0] ?? 0
        if zeroCount > 0 { freq.removeValue(forKey: 0) }

        let maxSum = r
        var dp = [Int](repeating: 0, count: maxSum + 1)
        dp[0] = 1

        for (value, count) in freq {
            if value == 0 { continue }
            let v = value
            let c = count
            var ndp = [Int](repeating: 0, count: maxSum + 1)

            if v > maxSum {
                ndp = dp   // cannot take any of this value without exceeding r
            } else {
                for rem in 0..<v {
                    var sum = 0
                    var k = 0
                    var s = rem
                    while s <= maxSum {
                        sum += dp[s]
                        if sum >= MOD { sum -= MOD }
                        if k > c {
                            let idxRemove = rem + (k - c - 1) * v
                            sum -= dp[idxRemove]
                            if sum < 0 { sum += MOD }
                        }
                        ndp[s] = sum
                        k += 1
                        s += v
                    }
                }
            }
            dp = ndp
        }

        var ans = 0
        let multiplier = (zeroCount + 1) % MOD
        if l <= maxSum {
            let upper = min(r, maxSum)
            for s in l...upper {
                var val = dp[s]
                val = Int((Int64(val) * Int64(multiplier)) % Int64(MOD))
                ans += val
                if ans >= MOD { ans -= MOD }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubMultisets(nums: List<Int>, l: Int, r: Int): Int {
        val MOD = 1_000_000_007L
        var zeroCount = 0
        val freq = HashMap<Int, Int>()
        var totalSum = 0
        for (num in nums) {
            if (num == 0) {
                zeroCount++
            } else {
                freq[num] = (freq.getOrDefault(num, 0) + 1)
                totalSum += num
            }
        }
        val maxSum = totalSum
        var dp = LongArray(maxSum + 1)
        dp[0] = 1L

        for ((value, count) in freq.entries) {
            val v = value
            val c = count
            val newDp = LongArray(maxSum + 1)
            var rem = 0
            while (rem < v) {
                var windowSum = 0L
                var idx = rem
                var t = 0
                while (idx <= maxSum) {
                    windowSum += dp[idx]
                    if (t > c) {
                        val removeIdx = idx - (c + 1) * v
                        windowSum -= dp[removeIdx]
                    }
                    var cur = windowSum % MOD
                    if (cur < 0) cur += MOD
                    newDp[idx] = cur
                    idx += v
                    t++
                }
                rem++
            }
            dp = newDp
        }

        val factor = (zeroCount + 1).toLong() % MOD
        if (factor != 1L) {
            for (i in dp.indices) {
                dp[i] = (dp[i] * factor) % MOD
            }
        }

        var ans = 0L
        val start = maxOf(l, 0)
        val end = minOf(r, maxSum)
        if (start <= end) {
            for (s in start..end) {
                ans += dp[s]
                if (ans >= MOD) ans -= MOD
            }
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int countSubMultisets(List<int> nums, int l, int r) {
    // Count frequencies
    final Map<int, int> freq = {};
    for (var x in nums) {
      freq[x] = (freq[x] ?? 0) + 1;
    }

    // Handle zeros separately
    final int zeroCount = freq.remove(0) ?? 0;

    // Total sum of non‑zero elements (guaranteed ≤ 20000)
    int totalSum = 0;
    freq.forEach((value, cnt) {
      totalSum += value * cnt;
    });

    // DP array: dp[s] = number of sub‑multisets with sum s
    List<int> dp = List.filled(totalSum + 1, 0);
    dp[0] = 1;

    // Process each distinct non‑zero value using bounded knapsack (sliding window)
    for (final entry in freq.entries) {
      final int v = entry.key;
      final int c = entry.value;
      final List<int> prev = List.from(dp);

      for (int rem = 0; rem < v; ++rem) {
        int sumWindow = 0;
        int idx = rem;
        int k = 0;
        while (idx <= totalSum) {
          if (k > c) {
            sumWindow -= prev[idx - (c + 1) * v];
          }
          sumWindow += prev[idx];

          int val = sumWindow % _MOD;
          if (val < 0) val += _MOD;
          dp[idx] = val;

          idx += v;
          ++k;
        }
      }
    }

    // Multiply by choices of zeros (any number from 0..zeroCount)
    final int zeroFactor = (zeroCount + 1) % _MOD;

    int ans = 0;
    int start = l.clamp(0, totalSum);
    int end = r.clamp(0, totalSum);
    for (int s = start; s <= end; ++s) {
      ans = (ans + dp[s] * zeroFactor) % _MOD;
    }
    return ans;
  }
}
```

## Golang

```go
const MOD int = 1000000007

func countSubMultisets(nums []int, l int, r int) int {
    maxVal := 20000
    cnt := make([]int, maxVal+1)
    totalSum := 0
    for _, v := range nums {
        cnt[v]++
        totalSum += v
    }

    dp := make([]int, totalSum+1)
    dp[0] = 1

    // handle zeros separately
    if cnt[0] > 0 {
        factor := cnt[0] + 1
        for i := 0; i <= totalSum; i++ {
            dp[i] = int(int64(dp[i]) * int64(factor) % MOD)
        }
    }

    // process non-zero values using bounded knapsack with sliding window
    for v := 1; v <= maxVal; v++ {
        c := cnt[v]
        if c == 0 {
            continue
        }
        ndp := make([]int, totalSum+1)
        for rem := 0; rem < v; rem++ {
            var sum int64 = 0
            t := 0
            for s := rem; s <= totalSum; s += v {
                sum += int64(dp[s])
                if t > c {
                    idx := s - (c+1)*v
                    sum -= int64(dp[idx])
                }
                ndp[s] = int(sum % MOD)
                t++
            }
        }
        dp = ndp
    }

    if l > totalSum {
        return 0
    }
    if r > totalSum {
        r = totalSum
    }
    ans := 0
    for s := l; s <= r; s++ {
        ans += dp[s]
        if ans >= MOD {
            ans -= MOD
        }
    }
    return ans
}
```

## Ruby

```ruby
MOD = 1_000_000_007

# @param {Integer[]} nums
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def count_sub_multisets(nums, l, r)
  total_sum = nums.sum
  freq = Hash.new(0)
  nums.each { |v| freq[v] += 1 }

  dp = Array.new(total_sum + 1, 0)
  dp[0] = 1

  freq.each do |value, count|
    new_dp = Array.new(total_sum + 1, 0)
    value.times do |rem|
      sum = 0
      t = 0
      s = rem + t * value
      while s <= total_sum
        sum += dp[s]
        if t > count
          prev_s = rem + (t - count - 1) * value
          sum -= dp[prev_s]
        end
        new_dp[s] = sum % MOD
        t += 1
        s = rem + t * value
      end
    end
    dp = new_dp
  end

  ans = 0
  upper = [r, total_sum].min
  if l <= upper
    (l..upper).each { |s| ans += dp[s] }
  end
  ans % MOD
end
```

## Scala

```scala
object Solution {
    def countSubMultisets(nums: List[Int], l: Int, r: Int): Int = {
        val MOD = 1000000007L
        // frequency of each value
        val freq = scala.collection.mutable.Map[Int, Int]()
        var totalSum = 0
        for (v <- nums) {
            totalSum += v
            freq(v) = freq.getOrElse(v, 0) + 1
        }
        val maxSum = totalSum
        var dp = new Array[Long](maxSum + 1)
        dp(0) = 1L

        for ((value, count) <- freq) {
            if (value == 0) {
                val mult = (count + 1).toLong % MOD
                var i = 0
                while (i <= maxSum) {
                    dp(i) = (dp(i) * mult) % MOD
                    i += 1
                }
            } else {
                val ndp = new Array[Long](maxSum + 1)
                val v = value
                var rem = 0
                while (rem < v) {
                    var sumWindow = 0L
                    var k = 0
                    var idx = rem
                    while (idx <= maxSum) {
                        sumWindow += dp(idx)
                        if (k > count) {
                            val removeIdx = idx - (count + 1) * v
                            sumWindow -= dp(removeIdx)
                        }
                        ndp(idx) = ((sumWindow % MOD) + MOD) % MOD
                        k += 1
                        idx += v
                    }
                    rem += 1
                }
                dp = ndp
            }
        }

        var ans = 0L
        val start = math.max(l, 0)
        val end = math.min(r, maxSum)
        var s = start
        while (s <= end) {
            ans += dp(s)
            if (ans >= MOD) ans -= MOD
            s += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_sub_multisets(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        use std::collections::HashMap;

        // frequency of each value
        let mut freq: HashMap<usize, usize> = HashMap::new();
        let mut total_sum: usize = 0;
        for &x in nums.iter() {
            let v = x as usize;
            *freq.entry(v).or_insert(0) += 1;
            total_sum += v;
        }

        // dp[s] = number of ways to obtain sum s using processed values
        let mut dp: Vec<i64> = vec![0; total_sum + 1];
        dp[0] = 1;

        for (&value, &cnt) in freq.iter() {
            let v = value;
            let c = cnt;
            let mut ndp: Vec<i64> = vec![0; total_sum + 1];

            // sliding window over each residue class modulo v
            for rem in 0..v {
                let mut window: i64 = 0;
                let mut t: usize = 0;
                while rem + t * v <= total_sum {
                    let idx = rem + t * v;

                    // add dp[idx] to the window
                    window += dp[idx];
                    if window >= MOD { window -= MOD; }

                    // remove element that slides out of the window (if any)
                    if t > c {
                        let sub_idx = rem + (t - c - 1) * v;
                        window -= dp[sub_idx];
                        if window < 0 { window += MOD; }
                    }

                    ndp[idx] = window;
                    t += 1;
                }
            }
            dp = ndp;
        }

        let l_usize = l as usize;
        let r_usize = r as usize;
        if l_usize > total_sum {
            return 0;
        }
        let upper = std::cmp::min(r_usize, total_sum);
        let mut ans: i64 = 0;
        for s in l_usize..=upper {
            ans += dp[s];
            if ans >= MOD { ans -= MOD; }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (count-sub-multisets nums l r)
  (let* ((max-sum (apply + nums))
         (freq (make-hash)))
    ;; build frequency map
    (for ([x nums])
      (hash-update! freq x add1 0))
    (define dp (make-vector (+ max-sum 1) 0))
    (vector-set! dp 0 1)
    ;; process each distinct value with bounded knapsack DP
    (for ([(val cnt) (in-hash freq)])
      (define v val)
      (define c cnt)
      (define ndp (make-vector (+ max-sum 1) 0))
      (let loop-rem ((rem 0))
        (when (< rem v)
          (let ((sum 0))
            (let inner ((k 0))
              (define idx (+ rem (* k v)))
              (when (<= idx max-sum)
                (set! sum (modulo (+ sum (vector-ref dp idx)) MOD))
                (when (> k c)
                  (let ((subIdx (+ rem (* (- k c 1) v))))
                    (set! sum (modulo (- sum (vector-ref dp subIdx)) MOD))))
                (vector-set! ndp idx sum)
                (inner (add1 k)))))
          (loop-rem (add1 rem))))
      (set! dp ndp))
    ;; accumulate answer for sums in [l, r]
    (let ((ans 0))
      (for ([s (in-range l (add1 r))])
        (when (<= s max-sum)
          (set! ans (modulo (+ ans (vector-ref dp s)) MOD))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_sub_multisets/3]).

-define(MOD, 1000000007).

-spec count_sub_multisets(Nums :: [integer()], L :: integer(), R :: integer()) -> integer().
count_sub_multisets(Nums, L, R) ->
    CountMap = build_counts(maps:new(), Nums),
    Items = maps:to_list(CountMap),                     % [{Value, Count}]
    MaxSum = R,
    DP0 = array:new(MaxSum + 1, {default, 0}),
    DPPrev = array:set(0, 1, DP0),
    DPF = lists:foldl(fun({V, C}, AccDP) -> process_value(V, C, AccDP, MaxSum) end,
                     DPPrev, Items),
    sum_range(DPF, L, R).

build_counts(Map, []) ->
    Map;
build_counts(Map, [H|T]) ->
    NewMap = maps:update_with(H,
                fun(Old) -> Old + 1 end,
                1,
                Map),
    build_counts(NewMap, T).

process_value(V, C, DPPrev, MaxSum) ->
    DPNew0 = array:new(MaxSum + 1, {default, 0}),
    DPNew = process_remainders(0, V - 1, V, C, DPPrev, DPNew0, MaxSum),
    DPNew.

process_remainders(CurRem, MaxRem, _V, _C, _DPPrev, DPAcc, _MaxSum) when CurRem > MaxRem ->
    DPAcc;
process_remainders(CurRem, MaxRem, V, C, DPPrev, DPAcc, MaxSum) ->
    Updated = slide_rem(CurRem, V, C, DPPrev, DPAcc, MaxSum, 0, 0),
    process_remainders(CurRem + 1, MaxRem, V, C, DPPrev, Updated, MaxSum).

slide_rem(Idx, _V, _C, _DPPrev, DPAcc, MaxSum, _K, _Sum) when Idx > MaxSum ->
    DPAcc;
slide_rem(Idx, V, C, DPPrev, DPAcc, MaxSum, K, Sum0) ->
    ValPrev = array:get(Idx, DPPrev),
    Sum1 = (Sum0 + ValPrev) rem ?MOD,
    Sum2 = if
        K > C ->
            SubIdx = Idx - (C + 1) * V,
            SubVal = array:get(SubIdx, DPPrev),
            ((Sum1 - SubVal) rem ?MOD + ?MOD) rem ?MOD;
        true -> Sum1
    end,
    DPAcc2 = array:set(Idx, Sum2, DPAcc),
    slide_rem(Idx + V, V, C, DPPrev, DPAcc2, MaxSum, K + 1, Sum2).

sum_range(DP, L, R) ->
    sum_range(L, R, DP, 0).

sum_range(I, R, _DP, Acc) when I > R ->
    Acc;
sum_range(I, R, DP, Acc) ->
    Val = array:get(I, DP),
    NewAcc = (Acc + Val) rem ?MOD,
    sum_range(I + 1, R, DP, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_sub_multisets(nums :: [integer], l :: integer, r :: integer) :: integer
  def count_sub_multisets(nums, l, r) do
    mod = 1_000_000_007

    # frequency map
    freq =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    zero_cnt = Map.get(freq, 0, 0)
    multiplier = rem(zero_cnt + 1, mod)

    # remove zeros from processing
    items =
      freq
      |> Enum.filter(fn {k, _v} -> k != 0 end)

    max_sum = r

    # dp array: index => count of ways to achieve that sum
    dp = :array.new(max_sum + 1, default: 0)
    dp = :array.set(0, 1, dp)

    Enum.each(items, fn {val, cnt} ->
      new_dp = :array.new(max_sum + 1, default: 0)

      # process each residue class modulo val
      0..(val - 1)
      |> Enum.reduce(new_dp, fn rem_class, ndp_acc ->
        max_k = div(max_sum - rem_class, val)

        {_, ndp_final} =
          0..max_k
          |> Enum.reduce({0, ndp_acc}, fn k, {win_sum, ndp_inner} ->
            idx = rem_class + k * val
            cur = :array.get(idx, dp)
            win_sum = rem(win_sum + cur, mod)

            if k > cnt do
              rm_idx = rem_class + (k - cnt - 1) * val
              rm_val = :array.get(rm_idx, dp)
              win_sum = rem(win_sum - rm_val + mod, mod)
            end

            ndp_inner = :array.set(idx, win_sum, ndp_inner)
            {win_sum, ndp_inner}
          end)

        ndp_final
      end)

      # update dp for next iteration
      dp = new_dp
    end)

    ans =
      l..r
      |> Enum.reduce(0, fn s, acc ->
        rem(acc + :array.get(s, dp), mod)
      end)

    rem(ans * multiplier, mod)
  end
end
```
