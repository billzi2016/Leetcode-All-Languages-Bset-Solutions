# 2333. Minimum Sum of Squared Difference

## Cpp

```cpp
class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        using ll = long long;
        int n = nums1.size();
        vector<ll> diffs(n);
        ll maxDiff = 0;
        for (int i = 0; i < n; ++i) {
            diffs[i] = std::llabs((ll)nums1[i] - (ll)nums2[i]);
            if (diffs[i] > maxDiff) maxDiff = diffs[i];
        }
        ll K = (ll)k1 + (ll)k2;
        // binary search minimal possible maximum difference after at most K reductions
        ll low = 0, high = maxDiff;
        while (low < high) {
            ll mid = (low + high) / 2;
            ll need = 0;
            for (ll d : diffs) {
                if (d > mid) {
                    need += d - mid;
                    if (need > K) break; // early stop
                }
            }
            if (need <= K) high = mid;
            else low = mid + 1;
        }
        ll M = low;
        if (M == 0) return 0LL; // can reduce all to zero, extra ops are optional
        
        ll need = 0;
        ll cntM = 0;
        ll sumSq = 0;
        for (ll d : diffs) {
            if (d > M) {
                need += d - M;
                ++cntM;
                sumSq += M * M; // after reducing to M
            } else {
                sumSq += d * d;
            }
        }
        ll rem = K - need; // remaining operations, guaranteed < cntM
        ll reduceFromM = std::min(cntM, rem);
        if (reduceFromM > 0) {
            sumSq -= reduceFromM * M * M;
            ll m1 = M - 1;
            sumSq += reduceFromM * m1 * m1;
        }
        return sumSq;
    }
};
```

## Java

```java
class Solution {
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.length;
        int maxPossibleDiff = 100000; // because nums values are up to 1e5
        long[] freq = new long[maxPossibleDiff + 1];
        int maxDiff = 0;
        for (int i = 0; i < n; i++) {
            int diff = Math.abs(nums1[i] - nums2[i]);
            freq[diff]++;
            if (diff > maxDiff) maxDiff = diff;
        }
        long remaining = (long) k1 + k2;

        for (int cur = maxDiff; cur > 0 && remaining > 0; cur--) {
            if (freq[cur] == 0) continue;
            long take = Math.min(remaining, freq[cur]);
            freq[cur] -= take;
            freq[cur - 1] += take;
            remaining -= take;
        }

        if (remaining > 0) { // all diffs are zero, extra operations increase some differences
            long base = remaining / n;
            long extra = remaining % n;
            long ans = (n - extra) * base * base + extra * (base + 1) * (base + 1);
            return ans;
        } else {
            long ans = 0L;
            for (int i = 0; i <= maxDiff; i++) {
                if (freq[i] != 0) {
                    ans += (long) i * i * freq[i];
                }
            }
            return ans;
        }
    }
}
```

## Python

```python
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        K = k1 + k2
        total_diff = sum(diffs)

        # If we can eliminate all differences and still have moves left,
        # distribute the remaining moves evenly.
        if K >= total_diff:
            remain = K - total_diff
            n = len(diffs)
            base = remain // n
            extra = remain % n
            return (n - extra) * (base * base) + extra * ((base + 1) * (base + 1))

        # Binary search the smallest threshold such that reducing all diffs above it
        # uses at most K moves.
        low, high = 0, max(diffs)
        while low < high:
            mid = (low + high) // 2
            needed = 0
            for d in diffs:
                if d > mid:
                    needed += d - mid
            if needed > K:
                low = mid + 1
            else:
                high = mid

        threshold = low
        used = 0
        total = 0
        count_eq = 0  # number of diffs that are exactly 'threshold' after reduction
        for d in diffs:
            if d > threshold:
                used += d - threshold
                total += threshold * threshold
                count_eq += 1
            elif d == threshold:
                total += threshold * threshold
                count_eq += 1
            else:  # d < threshold
                total += d * d

        leftover = K - used
        if leftover > 0:
            # each extra reduction changes x^2 to (x-1)^2, decreasing the sum by (2*x - 1)
            total -= leftover * (2 * threshold - 1)

        return total
```

## Python3

```python
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_ops = k1 + k2
        sum_diff = sum(diffs)
        if total_ops >= sum_diff:
            leftover = total_ops - sum_diff
            return leftover % 2

        lo, hi = 0, max(diffs)
        while lo < hi:
            mid = (lo + hi) // 2
            needed = 0
            for d in diffs:
                if d > mid:
                    needed += d - mid
            if needed <= total_ops:
                hi = mid
            else:
                lo = mid + 1
        t = lo

        ops_used = 0
        for d in diffs:
            if d > t:
                ops_used += d - t
        leftover = total_ops - ops_used

        max_val = t
        freq = [0] * (max_val + 1)
        for d in diffs:
            if d > t:
                freq[t] += 1
            else:
                freq[d] += 1

        for v in range(max_val, 0, -1):
            if leftover == 0:
                break
            cnt = freq[v]
            if cnt == 0:
                continue
            move = cnt if cnt <= leftover else leftover
            freq[v] -= move
            freq[v - 1] += move
            leftover -= move

        ans = 0
        for v, c in enumerate(freq):
            if c:
                ans += c * (v * v)
        return ans
```

## C

```c
#include <stdlib.h>
#include <math.h>

long long minSumSquareDiff(int* nums1, int nums1Size, int* nums2, int nums2Size, int k1, int k2) {
    int n = nums1Size;
    int maxDiff = 0;
    // First pass to compute diffs and find maximum
    int *diffs = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        int d = nums1[i] - nums2[i];
        if (d < 0) d = -d;
        diffs[i] = d;
        if (d > maxDiff) maxDiff = d;
    }

    // Frequency array for each possible diff value
    long long *freq = (long long*)calloc(maxDiff + 2, sizeof(long long));
    for (int i = 0; i < n; ++i) {
        freq[diffs[i]]++;
    }
    free(diffs);

    long long ops = (long long)k1 + (long long)k2;

    // Reduce differences greedily from largest to smallest
    for (int cur = maxDiff; cur > 0 && ops > 0; --cur) {
        long long cnt = freq[cur];
        if (cnt == 0) continue;
        if (ops >= cnt) {
            freq[cur - 1] += cnt;
            ops -= cnt;
            freq[cur] = 0;
        } else {
            // partially reduce
            freq[cur] -= ops;          // remaining at current level
            freq[cur - 1] += ops;      // those reduced by one
            ops = 0;
            break;
        }
    }

    // Compute final sum of squares
    long long result = 0;
    for (int i = 0; i <= maxDiff; ++i) {
        if (freq[i]) {
            result += freq[i] * (long long)i * (long long)i;
        }
    }

    free(freq);
    return result;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MinSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.Length;
        long totalOps = (long)k1 + k2;
        int maxDiff = 0;
        long sumDiffs = 0;
        int[] diffs = new int[n];
        for (int i = 0; i < n; i++) {
            int d = Math.Abs(nums1[i] - nums2[i]);
            diffs[i] = d;
            sumDiffs += d;
            if (d > maxDiff) maxDiff = d;
        }
        if (totalOps >= sumDiffs) return 0L;

        long[] freq = new long[maxDiff + 1];
        foreach (int d in diffs) {
            freq[d]++;
        }

        int cur = maxDiff;
        long cnt = freq[cur]; // number of elements with diff >= cur
        while (cur > 0 && totalOps > 0) {
            if (totalOps >= cnt) {
                totalOps -= cnt;
                cur--;
                cnt += freq[cur];
            } else {
                long rem = totalOps; // how many of the 'cnt' elements we can reduce one more step
                long result = 0L;

                long countCur = cnt - rem;
                if (countCur > 0) result += countCur * ((long)cur * cur);

                long countCurMinus1 = freq[cur - 1] + rem;
                if (countCurMinus1 > 0) result += countCurMinus1 * ((long)(cur - 1) * (cur - 1));

                for (int i = 0; i <= cur - 2; i++) {
                    if (freq[i] != 0) result += freq[i] * ((long)i * i);
                }
                return result;
            }
        }

        // If we exit the loop, either cur == 0 or totalOps == 0
        if (cur == 0) return 0L;

        long finalResult = 0L;
        if (cnt > 0) finalResult += cnt * ((long)cur * cur);
        for (int i = 0; i < cur; i++) {
            if (freq[i] != 0) finalResult += freq[i] * ((long)i * i);
        }
        return finalResult;
    }
}
```

## Javascript

```javascript
var minSumSquareDiff = function(nums1, nums2, k1, k2) {
    const n = nums1.length;
    let maxDiff = 0;
    let sumDiff = 0;
    const diffs = new Array(n);
    for (let i = 0; i < n; i++) {
        const d = Math.abs(nums1[i] - nums2[i]);
        diffs[i] = d;
        sumDiff += d;
        if (d > maxDiff) maxDiff = d;
    }
    let K = k1 + k2;
    if (K >= sumDiff) {
        const remaining = K - sumDiff;
        return remaining % 2;
    }
    const freq = new Uint32Array(maxDiff + 1);
    for (let i = 0; i < n; i++) {
        freq[diffs[i]]++;
    }
    let remaining = K;
    for (let cur = maxDiff; cur > 0 && remaining > 0; cur--) {
        const cnt = freq[cur];
        if (cnt === 0) continue;
        if (remaining >= cnt) {
            freq[cur] = 0;
            freq[cur - 1] += cnt;
            remaining -= cnt;
        } else {
            const move = remaining;
            freq[cur] = cnt - move;
            freq[cur - 1] += move;
            remaining = 0;
            break;
        }
    }
    let ans = 0;
    for (let i = 0; i <= maxDiff; i++) {
        if (freq[i]) {
            ans += i * i * freq[i];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minSumSquareDiff(nums1: number[], nums2: number[], k1: number, k2: number): number {
    const n = nums1.length;
    let maxDiff = 0;
    const diffs = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        const d = Math.abs(nums1[i] - nums2[i]);
        diffs[i] = d;
        if (d > maxDiff) maxDiff = d;
    }
    // ensure size at least 2 to handle possible index 1 later
    const size = Math.max(maxDiff, 1) + 1;
    const freq = new Uint32Array(size);
    for (const d of diffs) {
        freq[d]++;
    }

    let ops = k1 + k2;
    let cur = maxDiff;
    while (ops > 0 && cur > 0) {
        if (freq[cur] === 0) {
            cur--;
            continue;
        }
        const take = Math.min(ops, freq[cur]);
        freq[cur] -= take;
        freq[cur - 1] += take;
        ops -= take;
        if (freq[cur] === 0) cur--;
    }

    if (ops > 0 && (ops & 1)) {
        // one leftover operation makes a zero diff become 1
        freq[1] = (freq[1] ?? 0) + 1;
    }

    let result = 0;
    for (let d = 0; d < size; d++) {
        const cnt = freq[d];
        if (cnt === 0) continue;
        result += cnt * d * d;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k1
     * @param Integer $k2
     * @return Integer
     */
    function minSumSquareDiff($nums1, $nums2, $k1, $k2) {
        $n = count($nums1);
        $maxDiff = 0;
        $diffs = [];
        for ($i = 0; $i < $n; $i++) {
            $d = abs($nums1[$i] - $nums2[$i]);
            $diffs[] = $d;
            if ($d > $maxDiff) {
                $maxDiff = $d;
            }
        }

        // frequency of each difference value
        $freq = array_fill(0, $maxDiff + 1, 0);
        foreach ($diffs as $d) {
            $freq[$d]++;
        }

        $ops = $k1 + $k2; // total operations available

        for ($cur = $maxDiff; $cur > 0 && $ops > 0; $cur--) {
            $cnt = $freq[$cur];
            if ($cnt == 0) {
                continue;
            }
            if ($ops >= $cnt) {
                // reduce all cnt elements by 1
                $freq[$cur - 1] += $cnt;
                $ops -= $cnt;
                // $freq[$cur] becomes zero implicitly
            } else {
                // only part of them can be reduced
                $reduce = $ops;               // number of elements we move down
                $remain = $cnt - $reduce;     // stay at current level
                $freq[$cur] = $remain;
                $freq[$cur - 1] += $reduce;
                $ops = 0;
            }
        }

        $result = 0;
        for ($d = 0; $d <= $maxDiff; $d++) {
            if ($freq[$d] > 0) {
                $result += $freq[$d] * $d * $d;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minSumSquareDiff(_ nums1: [Int], _ nums2: [Int], _ k1: Int, _ k2: Int) -> Int {
        let n = nums1.count
        var diffs = [Int]()
        diffs.reserveCapacity(n)
        var maxDiff = 0
        for i in 0..<n {
            let d = abs(nums1[i] - nums2[i])
            diffs.append(d)
            if d > maxDiff { maxDiff = d }
        }
        
        var freq = [Int](repeating: 0, count: maxDiff + 1)
        for d in diffs {
            freq[d] += 1
        }
        
        var remainingOps = Int64(k1) + Int64(k2)
        
        if maxDiff > 0 && remainingOps > 0 {
            var cumulative = 0   // number of elements with diff >= current level
            var cur = maxDiff
            while cur > 0 && remainingOps > 0 {
                cumulative += freq[cur]
                if cumulative == 0 {
                    cur -= 1
                    continue
                }
                let need = Int64(cumulative)   // ops to lower all these by 1
                if remainingOps >= need {
                    // move all down one level
                    freq[cur] = 0
                    freq[cur - 1] += cumulative
                    remainingOps -= need
                    cur -= 1
                } else {
                    let move = Int(remainingOps)   // how many to move down
                    freq[cur] = cumulative - move
                    freq[cur - 1] += move
                    remainingOps = 0
                    break
                }
            }
        }
        
        var answer: Int64 = 0
        if remainingOps > 0 {
            // all diffs are zero, distribute the leftover operations
            let n64 = Int64(n)
            let q = remainingOps / n64
            let r = remainingOps % n64
            answer = (n64 - r) * q * q + r * (q + 1) * (q + 1)
        } else {
            for d in 0...maxDiff {
                let cnt = freq[d]
                if cnt > 0 {
                    let c64 = Int64(cnt)
                    let d64 = Int64(d)
                    answer += c64 * d64 * d64
                }
            }
        }
        
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSumSquareDiff(nums1: IntArray, nums2: IntArray, k1: Int, k2: Int): Long {
        val n = nums1.size
        var maxDiff = 0
        val diffs = IntArray(n)
        for (i in 0 until n) {
            val d = kotlin.math.abs(nums1[i] - nums2[i])
            diffs[i] = d
            if (d > maxDiff) maxDiff = d
        }
        if (maxDiff == 0) return 0L

        val freq = LongArray(maxDiff + 1)
        for (d in diffs) {
            freq[d]++
        }

        var remaining = k1.toLong() + k2.toLong()
        var cur = maxDiff
        var cum = 0L

        while (cur > 0 && remaining > 0) {
            if (freq[cur] != 0L) {
                cum += freq[cur]
                freq[cur] = 0L
            }
            // also include any cumulative count already present from higher levels
            if (cum == 0L) {
                cur--
                continue
            }
            if (remaining >= cum) {
                remaining -= cum
                // all cum elements move down one level, stay in cum for next iteration
            } else {
                val reduced = remaining
                freq[cur] = cum - reduced
                freq[cur - 1] += reduced
                remaining = 0L
                break
            }
            cur--
        }

        if (remaining == 0L && cur >= 0) {
            // cum elements are now at level 'cur'
            freq[cur] += cum
        }

        var answer = 0L
        for (i in 0..maxDiff) {
            val cnt = freq[i]
            if (cnt != 0L) {
                answer += cnt * i.toLong() * i.toLong()
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minSumSquareDiff(List<int> nums1, List<int> nums2, int k1, int k2) {
    int n = nums1.length;
    List<int> diffs = List.filled(n, 0);
    int maxDiff = 0;
    int totalDiffSum = 0;
    for (int i = 0; i < n; i++) {
      int d = (nums1[i] - nums2[i]).abs();
      diffs[i] = d;
      if (d > maxDiff) maxDiff = d;
      totalDiffSum += d;
    }

    int k = k1 + k2;
    if (k >= totalDiffSum) return 0;

    // binary search minimal possible maximum difference after reductions
    int lo = 0, hi = maxDiff;
    while (lo < hi) {
      int mid = ((lo + hi) >> 1);
      int need = 0;
      for (int d in diffs) {
        if (d > mid) need += d - mid;
      }
      if (need <= k) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    int low = lo;

    // compute operations used to bring all diffs down to at most low
    int opsUsed = 0;
    for (int d in diffs) {
      if (d > low) opsUsed += d - low;
    }
    int remaining = k - opsUsed;

    // frequency of current differences after capping at low
    List<int> freq = List.filled(low + 1, 0);
    for (int d in diffs) {
      int v = d <= low ? d : low;
      freq[v]++;
    }

    int cur = low;
    while (remaining > 0 && cur > 0) {
      if (freq[cur] == 0) {
        cur--;
        continue;
      }
      int take = freq[cur];
      if (take > remaining) take = remaining;
      freq[cur] -= take;
      freq[cur - 1] += take;
      remaining -= take;
    }

    int result = 0;
    for (int v = 0; v <= low; v++) {
      if (freq[v] != 0) {
        result += v * v * freq[v];
      }
    }
    return result;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func minSumSquareDiff(nums1 []int, nums2 []int, k1 int, k2 int) int64 {
	n := len(nums1)
	diffs := make([]int64, n)
	for i := 0; i < n; i++ {
		d := nums1[i] - nums2[i]
		if d < 0 {
			d = -d
		}
		diffs[i] = int64(d)
	}
	sort.Slice(diffs, func(i, j int) bool { return diffs[i] > diffs[j] })

	K := int64(k1 + k2)
	i := 0
	for i < n && K > 0 {
		cur := diffs[i]
		j := i + 1
		for j < n && diffs[j] == cur {
			j++
		}
		var nextVal int64 = 0
		if j < n {
			nextVal = diffs[j]
		}
		cnt := int64(j) // number of elements in the current prefix
		diffLevel := cur - nextVal
		need := diffLevel * cnt
		if K >= need {
			for idx := i; idx < j; idx++ {
				diffs[idx] = nextVal
			}
			K -= need
			i = j
		} else {
			dec := K / cnt
			rem := K % cnt
			newVal := cur - dec
			for idx := i; idx < j; idx++ {
				diffs[idx] = newVal
			}
			for idx := i; idx < i+int(rem); idx++ {
				diffs[idx]--
			}
			K = 0
		}
	}

	var ans int64 = 0
	for _, v := range diffs {
		ans += v * v
	}
	return ans
}
```

## Ruby

```ruby
def min_sum_square_diff(nums1, nums2, k1, k2)
  n = nums1.length
  diffs = []
  max_diff = 0
  total_needed = 0

  (0...n).each do |i|
    d = (nums1[i] - nums2[i]).abs
    diffs << d
    total_needed += d
    max_diff = d if d > max_diff
  end

  k = k1 + k2

  if k >= total_needed
    leftover = k - total_needed
    q, r = leftover.divmod(n)
    return (n - r) * q * q + r * (q + 1) * (q + 1)
  else
    freq = Array.new(max_diff + 1, 0)
    diffs.each { |d| freq[d] += 1 }

    d = max_diff
    while k > 0 && d > 0
      if freq[d] == 0
        d -= 1
        next
      end
      take = [freq[d], k].min
      freq[d] -= take
      freq[d - 1] += take
      k -= take
    end

    sum = 0
    (0..max_diff).each do |i|
      cnt = freq[i]
      sum += cnt * i * i if cnt > 0
    end
    return sum
  end
end
```

## Scala

```scala
object Solution {
    def minSumSquareDiff(nums1: Array[Int], nums2: Array[Int], k1: Int, k2: Int): Long = {
        val n = nums1.length
        val diffs = new Array[Int](n)
        var maxDiff = 0
        var totalSum: Long = 0L
        var i = 0
        while (i < n) {
            val d = Math.abs(nums1(i) - nums2(i))
            diffs(i) = d
            if (d > maxDiff) maxDiff = d
            totalSum += d
            i += 1
        }
        var K: Long = k1.toLong + k2.toLong
        if (K >= totalSum) {
            val R = K - totalSum
            val t = R / n
            val r = (R % n).toInt
            val base = t * t
            val inc = (t + 1) * (t + 1)
            return (n - r).toLong * base + r.toLong * inc
        }
        var low = 0
        var high = maxDiff
        while (low < high) {
            val mid = (low + high) >>> 1
            var opsNeeded: Long = 0L
            var j = 0
            while (j < n && opsNeeded <= K) {
                val d = diffs(j)
                if (d > mid) opsNeeded += (d - mid)
                j += 1
            }
            if (opsNeeded > K) low = mid + 1 else high = mid
        }
        val L = low
        var opsUsed: Long = 0L
        val pq = new java.util.PriorityQueue[Int](java.util.Collections.reverseOrder())
        i = 0
        while (i < n) {
            val d = diffs(i)
            if (d > L) {
                opsUsed += (d - L)
                pq.add(L)
            } else {
                pq.add(d)
            }
            i += 1
        }
        var rem = (K - opsUsed).toInt // rem < n
        while (rem > 0) {
            val cur = pq.poll()
            if (cur > 0) pq.add(cur - 1) else pq.add(0)
            rem -= 1
        }
        var result: Long = 0L
        while (!pq.isEmpty) {
            val v = pq.poll()
            result += v.toLong * v
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_sum_square_diff(nums1: Vec<i32>, nums2: Vec<i32>, k1: i32, k2: i32) -> i64 {
        let n = nums1.len();
        let mut diffs: Vec<usize> = Vec::with_capacity(n);
        let mut max_diff: usize = 0;
        for i in 0..n {
            let d = (nums1[i] as i64 - nums2[i] as i64).abs() as usize;
            if d > max_diff {
                max_diff = d;
            }
            diffs.push(d);
        }

        // frequency of each difference value
        let mut freq: Vec<i64> = vec![0; max_diff + 1];
        for &d in &diffs {
            freq[d] += 1;
        }

        let mut k: i64 = (k1 as i64) + (k2 as i64);
        let mut cur = max_diff;

        while k > 0 && cur > 0 {
            if freq[cur] == 0 {
                cur -= 1;
                continue;
            }
            let take = std::cmp::min(freq[cur], k);
            freq[cur] -= take;
            freq[cur - 1] += take;
            k -= take;
            if freq[cur] == 0 {
                cur -= 1;
            }
        }

        let mut ans: i64 = 0;
        for d in 0..=max_diff {
            let cnt = freq[d];
            if cnt > 0 {
                let dd = d as i64;
                ans += dd * dd * cnt;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-sum-square-diff nums1 nums2 k1 k2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length nums1))
         (diffs (for/list ([a nums1] [b nums2]) (abs (- a b))))
         (total-diff (apply + diffs))
         (k (+ k1 k2)))
    (if (>= k total-diff)
        ;; all differences can be reduced to zero, distribute remaining ops
        (let* ((rem-ops (- k total-diff))
               (q (quotient rem-ops n))
               (r (remainder rem-ops n))
               (sq-q (* q q))
               (sq-q1 (* (+ q 1) (+ q 1))))
          (+ (* r sq-q1)
             (* (- n r) sq-q)))
        ;; need to reduce but cannot eliminate all differences
        (let* ((maxd (apply max diffs))
               (needed
                (lambda (t)
                  (for/sum ([d diffs]) (max 0 (- d t)))))
               (binary-search
                (let loop ((lo 0) (hi maxd))
                  (if (= lo hi)
                      lo
                      (let* ((mid (quotient (+ lo hi) 2))
                             (need (needed mid)))
                        (if (<= need k)
                            (loop lo mid)
                            (loop (+ mid 1) hi))))))
               (t binary-search)
               (need-t (needed t))
               (left (- k need-t))
               (cnt-big (for/sum ([d diffs]) (if (> d t) 1 0)))
               (sum-sq
                (for/sum ([d diffs])
                  (let ((v (if (> d t) t d)))
                    (* v v))))
               (dec (* left (- (* 2 t) 1))))
          (- sum-sq dec)))))
```

## Erlang

```erlang
-spec min_sum_square_diff(Nums1 :: [integer()], Nums2 :: [integer()], K1 :: integer(), K2 :: integer()) -> integer().
min_sum_square_diff(Nums1, Nums2, K1, K2) ->
    Diffs = lists:map(fun({A,B}) -> abs(A - B) end,
                      lists:zip(Nums1, Nums2)),
    TotalOps = K1 + K2,
    SumDiffs = lists:foldl(fun(X, Acc) -> Acc + X end, 0, Diffs),
    case TotalOps >= SumDiffs of
        true ->
            Remaining = TotalOps - SumDiffs,
            N = length(Diffs),
            BaseInc = div(Remaining, N),
            Extra = rem(Remaining, N),
            SqBase = BaseInc * BaseInc,
            SqBasePlus = (BaseInc + 1) * (BaseInc + 1),
            (N - Extra) * SqBase + Extra * SqBasePlus;
        false ->
            Sorted = lists:reverse(lists:sort(Diffs)),
            reduce(Sorted, TotalOps)
    end.

reduce(Sorted, Ops) -> go_loop_hd(Sorted, Ops).

go_loop_hd([Prev|Rest], Ops) -> go(Prev, 1, Rest, Ops).

go(_Prev, _Count, [], _Ops) ->
    0;
go(Prev, Count, Rest, Ops) ->
    case Rest of
        [] ->
            stop(Prev, Count, [], Ops);
        [H|T] ->
            Next = H,
            Need = (Prev - Next) * Count,
            if Ops >= Need ->
                    go(Next, Count + 1, T, Ops - Need);
               true ->
                    stop(Prev, Count, Rest, Ops)
            end
    end.

stop(Prev, Count, Rest, Ops) ->
    Q = div(Ops, Count),
    R = rem(Ops, Count),
    BaseVal = Prev - Q,
    SqBase = BaseVal * BaseVal,
    SqBaseMinus = (BaseVal - 1) * (BaseVal - 1),
    SumFirst = (Count - R) * SqBase + R * SqBaseMinus,
    SumRest = lists:foldl(fun(X, Acc) -> Acc + X * X end, 0, Rest),
    SumFirst + SumRest.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_sum_square_diff(nums1 :: [integer], nums2 :: [integer], k1 :: integer, k2 :: integer) :: integer
  def min_sum_square_diff(nums1, nums2, k1, k2) do
    diffs = Enum.zip(nums1, nums2) |> Enum.map(fn {a, b} -> abs(a - b) end)
    total_ops = k1 + k2

    sum_diffs = Enum.reduce(diffs, 0, &+/2)

    if total_ops >= sum_diffs do
      0
    else
      max_diff = Enum.max(diffs)

      # binary search for minimal possible maximum difference after reductions
      m = binary_search_min_max(diffs, total_ops, 0, max_diff)

      needed = needed_ops(diffs, m)
      rem = total_ops - needed

      freq = build_freq_map(diffs, m)

      {_, _, final_freq} = reduce_remaining(rem, m, freq)

      compute_sum(final_freq)
    end
  end

  defp binary_search_min_max(diffs, ops, low, high) do
    if low < high do
      mid = div(low + high, 2)
      needed = needed_ops(diffs, mid)

      if needed <= ops do
        binary_search_min_max(diffs, ops, low, mid)
      else
        binary_search_min_max(diffs, ops, mid + 1, high)
      end
    else
      low
    end
  end

  defp needed_ops(diffs, target) do
    Enum.reduce(diffs, 0, fn d, acc -> acc + max(d - target, 0) end)
  end

  defp build_freq_map(diffs, m) do
    Enum.reduce(diffs, %{}, fn d, acc ->
      diff = if d > m, do: m, else: d
      Map.update(acc, diff, 1, &(&1 + 1))
    end)
  end

  defp inc_map(map, key, delta) do
    Map.update(map, key, delta, &(&1 + delta))
  end

  defp reduce_remaining(rem, cur_max, freq) when rem == 0 or cur_max == 0 do
    {rem, cur_max, freq}
  end

  defp reduce_remaining(rem, cur_max, freq) do
    cnt = Map.get(freq, cur_max, 0)

    cond do
      cnt == 0 ->
        reduce_remaining(rem, cur_max - 1, freq)

      rem >= cnt ->
        freq = Map.put(freq, cur_max, 0)
        freq = inc_map(freq, cur_max - 1, cnt)
        reduce_remaining(rem - cnt, cur_max - 1, freq)

      true ->
        # partial reduction
        freq = Map.put(freq, cur_max, cnt - rem)
        freq = inc_map(freq, cur_max - 1, rem)
        {0, cur_max, freq}
    end
  end

  defp compute_sum(freq) do
    Enum.reduce(freq, 0, fn {v, c}, acc -> acc + v * v * c end)
  end
end
```
