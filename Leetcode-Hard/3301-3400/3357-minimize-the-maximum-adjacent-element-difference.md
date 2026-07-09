# 3357. Minimize the Maximum Adjacent Element Difference

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        long long maxFixed = 0;
        for (int i = 0; i + 1 < n; ++i) {
            if (nums[i] != -1 && nums[i+1] != -1) {
                maxFixed = max(maxFixed, (long long)abs(nums[i] - nums[i+1]));
            }
        }

        auto feasible = [&](long long D)->bool{
            if (maxFixed > D) return false;
            vector<pair<long long,long long>> segs;
            for (int i = 0; i < n; ++i) {
                if (nums[i] != -1) continue;
                long long low = LLONG_MIN/4, high = LLONG_MAX/4;
                bool has = false;
                if (i > 0 && nums[i-1] != -1) {
                    low = max(low, (long long)nums[i-1] - D);
                    high = min(high, (long long)nums[i-1] + D);
                    has = true;
                }
                if (i + 1 < n && nums[i+1] != -1) {
                    low = max(low, (long long)nums[i+1] - D);
                    high = min(high, (long long)nums[i+1] + D);
                    has = true;
                }
                if (!has) continue; // no constraint from known neighbors
                if (low > high) return false;
                segs.emplace_back(low, high);
            }

            if (segs.empty()) return true;

            long long Lmax = LLONG_MIN/4, Rmin = LLONG_MAX/4;
            for (auto &p : segs) {
                Lmax = max(Lmax, p.first);
                Rmin = min(Rmin, p.second);
            }

            if (Lmax <= Rmin) {
                long long cand = max(Lmax, 1LL);
                return cand <= Rmin;
            }
            if (Lmax - Rmin > D) return false;

            // intervals completely left of Lmax
            long long leftLowMax = LLONG_MIN/4, leftHighMin = LLONG_MAX/4;
            // intervals completely right of Rmin
            long long rightLowMax = LLONG_MIN/4, rightHighMin = LLONG_MAX/4;

            for (auto &p : segs) {
                if (p.second < Lmax) { // left side
                    leftLowMax = max(leftLowMax, p.first);
                    leftHighMin = min(leftHighMin, p.second);
                } else if (p.first > Rmin) { // right side
                    rightLowMax = max(rightLowMax, p.first);
                    rightHighMin = min(rightHighMin, p.second);
                }
            }

            bool left_ok = (leftLowMax == LLONG_MIN/4) || (leftLowMax <= leftHighMin && leftHighMin >= 1);
            bool right_ok = (rightLowMax == LLONG_MIN/4) || (rightLowMax <= rightHighMin && rightHighMin >= 1);
            return left_ok && right_ok;
        };

        long long lo = 0, hi = 1000000000LL; // sufficient upper bound
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (feasible(mid)) hi = mid;
            else lo = mid + 1;
        }
        return (int)lo;
    }
};
```

## Java

```java
class Solution {
    public int minDifference(int[] nums) {
        int n = nums.length;
        long baseKnown = 0;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] != -1 && nums[i + 1] != -1) {
                baseKnown = Math.max(baseKnown, Math.abs((long) nums[i] - nums[i + 1]));
            }
        }

        java.util.ArrayList<Long> valsList = new java.util.ArrayList<>();
        long needSingle = 0;

        int i = 0;
        while (i < n) {
            if (nums[i] == -1) {
                int start = i;
                while (i < n && nums[i] == -1) i++;
                int end = i - 1;
                int len = end - start + 1;

                Long leftVal = (start > 0 && nums[start - 1] != -1) ? (long) nums[start - 1] : null;
                Long rightVal = (i < n && nums[i] != -1) ? (long) nums[i] : null;

                if (leftVal != null) valsList.add(leftVal);
                if (rightVal != null) valsList.add(rightVal);

                if (len == 1 && leftVal != null && rightVal != null) {
                    long diff = Math.abs(leftVal - rightVal);
                    needSingle = Math.max(needSingle, (diff + 1) / 2);
                }
            } else {
                i++;
            }
        }

        if (valsList.isEmpty()) {
            long ans = Math.max(baseKnown, needSingle);
            return (int) ans;
        }

        long[] vals = new long[valsList.size()];
        for (int k = 0; k < vals.length; k++) vals[k] = valsList.get(k);
        java.util.Arrays.sort(vals);

        // binary search minimal D
        long low = 0, high = 1_000_000_000L;
        while (low < high) {
            long mid = (low + high) >>> 1;
            if (feasible(vals, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        long answer = Math.max(baseKnown, Math.max(needSingle, low));
        return (int) answer;
    }

    private boolean feasible(long[] vals, long D) {
        int n = vals.length;
        long minV = vals[0];
        long maxV = vals[n - 1];
        if (maxV - minV <= 2 * D) return true;

        // try split point
        for (int i = 0; i < n - 1; i++) {
            long prefMin = vals[0];
            long prefMax = vals[i];
            if (prefMax - prefMin > 2 * D) continue;

            long suffMin = vals[i + 1];
            long suffMax = maxV;
            if (suffMax - suffMin > 2 * D) continue;

            long pLeft = prefMax - D;
            long pRight = prefMin + D;
            long sLeft = suffMax - D;
            long sRight = suffMin + D;

            long dist = 0;
            if (pRight < sLeft) {
                dist = sLeft - pRight;
            } else if (sRight < pLeft) {
                dist = pLeft - sRight;
            }
            if (dist <= D) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_known = 0
        lo = None
        hi = None

        for i, v in enumerate(nums):
            if v != -1:
                if i > 0 and nums[i - 1] != -1:
                    max_known = max(max_known, abs(v - nums[i - 1]))
            else:  # v == -1
                if i > 0 and nums[i - 1] != -1:
                    nb = nums[i - 1]
                    lo = nb if lo is None else min(lo, nb)
                    hi = nb if hi is None else max(hi, nb)
                if i + 1 < n and nums[i + 1] != -1:
                    nb = nums[i + 1]
                    lo = nb if lo is None else min(lo, nb)
                    hi = nb if hi is None else max(hi, nb)

        if lo is None:  # all elements are -1
            return 0

        d = (hi - lo + 1) // 2  # ceil((hi-lo)/2)
        return max(max_known, d)
```

## Python3

```python
class Solution:
    def minDifference(self, nums):
        n = len(nums)
        max_fixed = 0
        neighbors = []
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            if a != -1 and b != -1:
                diff = abs(a - b)
                if diff > max_fixed:
                    max_fixed = diff
        for i, v in enumerate(nums):
            if v == -1:
                if i > 0 and nums[i - 1] != -1:
                    neighbors.append(nums[i - 1])
                if i + 1 < n and nums[i + 1] != -1:
                    neighbors.append(nums[i + 1])
        if not neighbors:
            return max_fixed
        mn = min(neighbors)
        mx = max(neighbors)
        need = (mx - mn + 1) // 2
        return max(max_fixed, need)
```

## C

```c
int minDifference(int* nums, int numsSize) {
    long long maxKnownDiff = 0;
    long long minNeighbor = (long long)1e18;
    long long maxNeighbor = -(long long)1e18;
    for (int i = 0; i < numsSize - 1; ++i) {
        if (nums[i] != -1 && nums[i + 1] != -1) {
            long long diff = llabs((long long)nums[i] - (long long)nums[i + 1]);
            if (diff > maxKnownDiff) maxKnownDiff = diff;
        }
    }
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == -1) continue;
        // left neighbor
        if (i > 0 && nums[i - 1] == -1) {
            if (nums[i] < minNeighbor) minNeighbor = nums[i];
            if (nums[i] > maxNeighbor) maxNeighbor = nums[i];
        }
        // right neighbor
        if (i + 1 < numsSize && nums[i + 1] == -1) {
            if (nums[i] < minNeighbor) minNeighbor = nums[i];
            if (nums[i] > maxNeighbor) maxNeighbor = nums[i];
        }
    }
    if (minNeighbor > maxNeighbor) { // no -1 adjacent to known numbers
        return (int)maxKnownDiff;
    }
    long long diff = maxNeighbor - minNeighbor;
    long long candidate = (diff + 1) / 2; // ceil(diff/2)
    long long answer = maxKnownDiff > candidate ? maxKnownDiff : candidate;
    return (int)answer;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public int MinDifference(int[] nums) {
        int n = nums.Length;
        long low = 0, high = 1000000000L;
        // Precompute left and right known values
        long[] leftKnown = new long[n];
        long last = long.MinValue;
        for (int i = 0; i < n; i++) {
            if (nums[i] != -1) last = nums[i];
            leftKnown[i] = last;
        }
        long[] rightKnown = new long[n];
        last = long.MaxValue;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] != -1) last = nums[i];
            rightKnown[i] = last;
        }

        bool Feasible(long d) {
            // check known-known adjacent differences
            for (int i = 0; i < n - 1; i++) {
                if (nums[i] != -1 && nums[i + 1] != -1) {
                    if (Math.Abs((long)nums[i] - (long)nums[i + 1]) > d) return false;
                }
            }

            bool hasMissing = false;
            bool hasConstraint = false;
            long Lmax = long.MinValue;
            long Rmin = long.MaxValue;

            for (int i = 0; i < n; i++) {
                if (nums[i] != -1) continue;
                hasMissing = true;
                bool leftExist = leftKnown[i] != long.MinValue;
                bool rightExist = rightKnown[i] != long.MaxValue;

                if (!leftExist && !rightExist) {
                    // whole array may be all -1, no constraint from this position
                    continue;
                }

                long L, R;
                if (leftExist && rightExist) {
                    long a = leftKnown[i];
                    long b = rightKnown[i];
                    long leftInt = Math.Max(a, b) - d;
                    long rightInt = Math.Min(a, b) + d;
                    if (leftInt > rightInt) return false; // empty intersection
                    L = leftInt;
                    R = rightInt;
                } else if (leftExist) {
                    long a = leftKnown[i];
                    L = a - d;
                    R = a + d;
                } else { // only right exists
                    long b = rightKnown[i];
                    L = b - d;
                    R = b + d;
                }

                hasConstraint = true;
                if (L > Lmax) Lmax = L;
                if (R < Rmin) Rmin = R;
            }

            if (!hasMissing) return true; // no -1 at all
            if (!hasConstraint) return true; // all positions have no known neighbors

            // need a segment of length d intersecting all intervals
            // feasible iff Lmax - d <= Rmin
            return (Lmax - d) <= Rmin;
        }

        while (low < high) {
            long mid = (low + high) / 2;
            if (Feasible(mid)) high = mid;
            else low = mid + 1;
        }
        return (int)low;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minDifference = function(nums) {
    let maxKnownDiff = 0;
    const n = nums.length;
    let mn = Infinity, mx = -Infinity;
    
    for (let i = 0; i < n; ++i) {
        if (nums[i] !== -1) {
            // check left neighbor for known-known diff
            if (i > 0 && nums[i-1] !== -1) {
                const diff = Math.abs(nums[i] - nums[i-1]);
                if (diff > maxKnownDiff) maxKnownDiff = diff;
            }
            // collect neighbors of -1 positions
            if (i > 0 && nums[i-1] === -1) {
                if (nums[i] < mn) mn = nums[i];
                if (nums[i] > mx) mx = nums[i];
            }
            if (i + 1 < n && nums[i+1] === -1) {
                if (nums[i] < mn) mn = nums[i];
                if (nums[i] > mx) mx = nums[i];
            }
        }
    }
    
    // If there were no neighbors (all -1), answer is 0
    if (mn === Infinity) return 0;
    
    const need = Math.ceil((mx - mn) / 2);
    return Math.max(maxKnownDiff, need);
};
```

## Typescript

```typescript
function minDifference(nums: number[]): number {
    const n = nums.length;
    let maxAdj = 0;
    for (let i = 0; i < n - 1; ++i) {
        if (nums[i] !== -1 && nums[i + 1] !== -1) {
            const d = Math.abs(nums[i] - nums[i + 1]);
            if (d > maxAdj) maxAdj = d;
        }
    }

    let minNeighbor = Number.MAX_SAFE_INTEGER;
    let maxNeighbor = -1;

    for (let i = 0; i < n; ++i) {
        if (nums[i] === -1) {
            if (i > 0 && nums[i - 1] !== -1) {
                const v = nums[i - 1];
                if (v < minNeighbor) minNeighbor = v;
                if (v > maxNeighbor) maxNeighbor = v;
            }
            if (i + 1 < n && nums[i + 1] !== -1) {
                const v = nums[i + 1];
                if (v < minNeighbor) minNeighbor = v;
                if (v > maxNeighbor) maxNeighbor = v;
            }
        }
    }

    if (maxNeighbor === -1) return 0; // all elements are -1

    const diff = maxNeighbor - minNeighbor;
    const need = Math.ceil(diff / 2);
    return Math.max(maxAdj, need);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minDifference($nums) {
        $n = count($nums);
        $maxKnownDiff = 0;
        // compute max diff between consecutive known numbers
        for ($i = 0; $i < $n - 1; ++$i) {
            if ($nums[$i] != -1 && $nums[$i + 1] != -1) {
                $diff = abs($nums[$i] - $nums[$i + 1]);
                if ($diff > $maxKnownDiff) $maxKnownDiff = $diff;
            }
        }

        // collect values adjacent to -1
        $adj = [];
        for ($i = 0; $i < $n; ++$i) {
            if ($nums[$i] == -1) {
                if ($i > 0 && $nums[$i - 1] != -1) $adj[] = $nums[$i - 1];
                if ($i + 1 < $n && $nums[$i + 1] != -1) $adj[] = $nums[$i + 1];
            }
        }

        if (empty($adj)) {
            // no constraints from -1 positions
            return $maxKnownDiff;
        }

        $loVal = min($adj);
        $hiVal = max($adj);

        $left = 0;
        $right = 1000000000; // upper bound for d

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            $x = $loVal + $mid;

            $minR = PHP_INT_MAX;
            $maxR = -PHP_INT_MAX;

            foreach ($adj as $b) {
                if (abs($b - $x) > $mid) {
                    if ($b < $minR) $minR = $b;
                    if ($b > $maxR) $maxR = $b;
                }
            }

            if ($minR === PHP_INT_MAX || ($maxR - $minR) <= 2 * $mid) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }

        $d = $left;
        return max($maxKnownDiff, $d);
    }
}
```

## Swift

```swift
class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        var maxKnown = 0
        // maximum difference between consecutive known elements
        for i in 1..<n {
            if nums[i] != -1 && nums[i-1] != -1 {
                maxKnown = max(maxKnown, abs(nums[i] - nums[i-1]))
            }
        }
        var neighborVals = [Int]()
        // collect values adjacent to missing positions
        for i in 0..<n where nums[i] == -1 {
            if i > 0 && nums[i-1] != -1 {
                neighborVals.append(nums[i-1])
            }
            if i + 1 < n && nums[i+1] != -1 {
                neighborVals.append(nums[i+1])
            }
        }
        if neighborVals.isEmpty {
            return maxKnown
        }
        var minV = Int.max
        var maxV = Int.min
        for v in neighborVals {
            if v < minV { minV = v }
            if v > maxV { maxV = v }
        }
        let candidate = (maxV - minV + 1) / 2   // ceil division
        return max(maxKnown, candidate)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDifference(nums: IntArray): Int {
        var maxDiff = 0
        var mn = Int.MAX_VALUE
        var mx = Int.MIN_VALUE
        for (i in 0 until nums.size - 1) {
            val a = nums[i]
            val b = nums[i + 1]
            if (a != -1 && b != -1) {
                maxDiff = kotlin.math.max(maxDiff, kotlin.math.abs(a - b))
            } else {
                if (a == -1 && b != -1) {
                    mn = kotlin.math.min(mn, b)
                    mx = kotlin.math.max(mx, b)
                }
                if (b == -1 && a != -1) {
                    mn = kotlin.math.min(mn, a)
                    mx = kotlin.math.max(mx, a)
                }
            }
        }
        if (mn == Int.MAX_VALUE) return 0
        val d = ((mx - mn) + 1) / 2  // ceil division of (mx-mn)/2
        return kotlin.math.max(maxDiff, d)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minDifference(List<int> nums) {
    int n = nums.length;
    // Precompute maximum known-known difference
    int maxKnownDiff = 0;
    for (int i = 0; i < n - 1; i++) {
      if (nums[i] != -1 && nums[i + 1] != -1) {
        int diff = (nums[i] - nums[i + 1]).abs();
        if (diff > maxKnownDiff) maxKnownDiff = diff;
      }
    }

    bool can(int d) {
      // known-known pairs must satisfy d
      for (int i = 0; i < n - 1; i++) {
        if (nums[i] != -1 && nums[i + 1] != -1) {
          int diff = (nums[i] - nums[i + 1]).abs();
          if (diff > d) return false;
        }
      }

      const int INF = 2000000000; // sufficiently large
      List<List<int>> intervals = [];

      for (int i = 0; i < n; i++) {
        if (nums[i] == -1) {
          int? leftVal;
          int? rightVal;
          if (i > 0 && nums[i - 1] != -1) leftVal = nums[i - 1];
          if (i + 1 < n && nums[i + 1] != -1) rightVal = nums[i + 1];

          if (leftVal == null && rightVal == null) continue; // no constraints

          int low = 1;
          int high = INF;

          if (leftVal != null) {
            low = max(low, leftVal - d);
            high = min(high, leftVal + d);
          }
          if (rightVal != null) {
            low = max(low, rightVal - d);
            high = min(high, rightVal + d);
          }

          if (low > high) return false;
          intervals.add([low, high]);
        }
      }

      if (intervals.isEmpty) return true;

      intervals.sort((a, b) => a[0].compareTo(b[0]));

      // Greedy cover with at most two points
      int p1 = intervals[0][1];
      int idx = 0;
      while (idx < intervals.length &&
          intervals[idx][0] <= p1 &&
          p1 <= intervals[idx][1]) {
        idx++;
      }
      if (idx == intervals.length) return true;

      int maxL = intervals[idx][0];
      int minR = intervals[idx][1];
      for (int j = idx + 1; j < intervals.length; j++) {
        maxL = max(maxL, intervals[j][0]);
        minR = min(minR, intervals[j][1]);
      }
      return maxL <= minR;
    }

    int low = 0;
    int high = 1000000000; // upper bound for answer
    while (low < high) {
      int mid = (low + high) >> 1;
      if (can(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func minDifference(nums []int) int {
    n := len(nums)
    const INF = int(1<<60 - 1)

    maxBase := 0
    // compute max diff between known-known adjacent elements
    for i := 0; i < n-1; i++ {
        if nums[i] != -1 && nums[i+1] != -1 {
            diff := nums[i] - nums[i+1]
            if diff < 0 {
                diff = -diff
            }
            if diff > maxBase {
                maxBase = diff
            }
        }
    }

    minV, maxV := INF, -INF
    // collect values adjacent to -1
    for i := 0; i < n; i++ {
        if nums[i] == -1 {
            if i > 0 && nums[i-1] != -1 {
                v := nums[i-1]
                if v < minV {
                    minV = v
                }
                if v > maxV {
                    maxV = v
                }
            }
            if i+1 < n && nums[i+1] != -1 {
                v := nums[i+1]
                if v < minV {
                    minV = v
                }
                if v > maxV {
                    maxV = v
                }
            }
        }
    }

    // all elements are -1
    if maxV == -INF {
        return 0
    }

    // minimal possible maximal difference using optimal x,y
    diff := maxV - minV
    candidate := (diff + 1) / 2 // ceil(diff/2)

    if candidate < maxBase {
        return maxBase
    }
    return candidate
}
```

## Ruby

```ruby
def min_difference(nums)
  n = nums.length
  cur_max = 0
  i = 0
  while i < n - 1
    a = nums[i]
    b = nums[i + 1]
    if a != -1 && b != -1
      diff = (a - b).abs
      cur_max = diff if diff > cur_max
    end
    i += 1
  end

  adj_vals = []
  i = 0
  while i < n
    if nums[i] == -1
      adj_vals << nums[i - 1] if i > 0 && nums[i - 1] != -1
      adj_vals << nums[i + 1] if i + 1 < n && nums[i + 1] != -1
    end
    i += 1
  end

  return cur_max if adj_vals.empty?

  mn = adj_vals.min
  mx = adj_vals.max
  d2 = (mx - mn + 1) / 2   # ceil division
  [cur_max, d2].max
end
```

## Scala

```scala
object Solution {
    def minDifference(nums: Array[Int]): Int = {
        val n = nums.length
        var baseMax = 0L
        for (i <- 0 until n - 1) {
            if (nums(i) != -1 && nums(i + 1) != -1) {
                val diff = Math.abs(nums(i).toLong - nums(i + 1))
                if (diff > baseMax) baseMax = diff
            }
        }

        var lo = 0L
        var hi = 1000000000L
        while (lo < hi) {
            val mid = (lo + hi) >>> 1
            if (feasible(nums, baseMax, mid)) hi = mid else lo = mid + 1
        }
        lo.toInt
    }

    private def feasible(nums: Array[Int], baseMax: Long, d: Long): Boolean = {
        if (d < baseMax) return false
        val n = nums.length
        var L = Long.MinValue // max of lower bounds
        var R = Long.MaxValue // min of upper bounds
        var anyConstraint = false

        for (i <- 0 until n) {
            if (nums(i) == -1) {
                var low = 1L
                var high = Long.MaxValue
                var has = false

                if (i > 0 && nums(i - 1) != -1) {
                    val v = nums(i - 1).toLong
                    low = Math.max(low, v - d)
                    high = Math.min(high, v + d)
                    has = true
                }
                if (i + 1 < n && nums(i + 1) != -1) {
                    val v = nums(i + 1).toLong
                    low = Math.max(low, v - d)
                    high = Math.min(high, v + d)
                    has = true
                }

                if (!has) {
                    // no known neighbor, this position imposes no restriction
                } else {
                    anyConstraint = true
                    if (low > high) return false
                    L = Math.max(L, low)
                    R = Math.min(R, high)
                }
            }
        }

        if (!anyConstraint) return true
        if (L <= R) true else (L - R) <= d
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut max_known_diff: i64 = 0;
        for i in 0..n - 1 {
            if nums[i] != -1 && nums[i + 1] != -1 {
                let diff = (nums[i] as i64 - nums[i + 1] as i64).abs();
                if diff > max_known_diff {
                    max_known_diff = diff;
                }
            }
        }

        let mut min_neighbor: i64 = i64::MAX;
        let mut max_neighbor: i64 = i64::MIN;

        for i in 0..n {
            if nums[i] == -1 {
                if i > 0 && nums[i - 1] != -1 {
                    let val = nums[i - 1] as i64;
                    if val < min_neighbor {
                        min_neighbor = val;
                    }
                    if val > max_neighbor {
                        max_neighbor = val;
                    }
                }
                if i + 1 < n && nums[i + 1] != -1 {
                    let val = nums[i + 1] as i64;
                    if val < min_neighbor {
                        min_neighbor = val;
                    }
                    if val > max_neighbor {
                        max_neighbor = val;
                    }
                }
            }
        }

        if min_neighbor == i64::MAX {
            return 0;
        }

        let candidate = (max_neighbor - min_neighbor + 1) / 2; // ceil division
        let ans = std::cmp::max(max_known_diff, candidate);
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (let loop ((i 0) (prev-val #f) (prev-idx -1) (ans 0) (found? #f))
      (if (= i n)
          (if found? ans 0)
          (let ((v (vector-ref vec i)))
            (if (= v -1)
                (loop (+ i 1) prev-val prev-idx ans found?)
                (let* ((new-found? #t)
                       (candidate
                        (if prev-val
                            (let* ((diff (abs (- v prev-val)))
                                   (gap (- i prev-idx 1))
                                   (c (cond [(= gap 0) diff]
                                            [(= gap 1) (quotient (+ diff 1) 2)] ; ceil(diff/2)
                                            [else (quotient (+ diff 2) 3)]))) ; ceil(diff/3)
                              (max ans c))
                            ans)))
                  (loop (+ i 1) v i candidate new-found?))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_difference/1]).

-spec min_difference(Nums :: [integer()]) -> integer().
min_difference(Nums) ->
    case Nums of
        [] -> 0;
        [First|Rest] ->
            {CurMax, Vals} = loop(Rest, First, 0, []),
            case Vals of
                [] -> CurMax;
                _ ->
                    Lo = lists:min(Vals),
                    Hi = lists:max(Vals),
                    Diff = Hi - Lo,
                    D = (Diff + 1) div 2,
                    max(CurMax, D)
            end
    end.

loop([], _Prev, CurMax, Vals) ->
    {CurMax, Vals};
loop([H|T], Prev, CurMax, Vals) ->
    case {Prev, H} of
        {-1, -1} ->
            loop(T, H, CurMax, Vals);
        {-1, Val} when Val =/= -1 ->
            NewVals = [Val | Vals],
            loop(T, H, CurMax, NewVals);
        {Val, -1} when Val =/= -1 ->
            NewVals = [Val | Vals],
            loop(T, H, CurMax, NewVals);
        {Val1, Val2} ->
            Diff = abs(Val1 - Val2),
            NewCurMax = max(CurMax, Diff),
            loop(T, H, NewCurMax, Vals)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_difference(nums :: [integer]) :: integer
  def min_difference(nums) do
    {fixed_max, s_list} = process(nums, 0, [])

    if s_list == [] do
      fixed_max
    else
      s = Enum.sort(s_list)

      feasible = fn d ->
        max_len = 2 * d
        first_end = hd(s) + max_len

        i =
          Enum.find_index(s, fn v -> v > first_end end)
          || length(s)

        if i == length(s) do
          true
        else
          List.last(s) - Enum.at(s, i) <= max_len
        end
      end

      d_opt = binary_search(0, 1_000_000_000, feasible)
      max(fixed_max, d_opt)
    end
  end

  defp process([a, b | rest], fixed_max, s_acc) do
    new_fixed =
      if a != -1 and b != -1 do
        max(fixed_max, abs(a - b))
      else
        fixed_max
      end

    new_s =
      cond do
        a == -1 and b != -1 -> [b | s_acc]
        b == -1 and a != -1 -> [a | s_acc]
        true -> s_acc
      end

    process([b | rest], new_fixed, new_s)
  end

  defp process(_, fixed_max, s_acc), do: {fixed_max, s_acc}

  defp binary_search(l, r, feasible) when l < r do
    mid = div(l + r, 2)

    if feasible.(mid) do
      binary_search(l, mid, feasible)
    else
      binary_search(mid + 1, r, feasible)
    end
  end

  defp binary_search(l, _r, _feasible), do: l
end
```
