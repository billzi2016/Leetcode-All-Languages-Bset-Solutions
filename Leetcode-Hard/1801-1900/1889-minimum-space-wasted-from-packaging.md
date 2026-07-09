# 1889. Minimum Space Wasted From Packaging

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
        const long long MOD = 1000000007LL;
        sort(packages.begin(), packages.end());
        int n = packages.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + packages[i];
        long long best = LLONG_MAX;
        int maxPkg = packages.back();

        for (auto& bvec : boxes) {
            vector<int> b = bvec;
            sort(b.begin(), b.end());
            if (b.empty() || b.back() < maxPkg) continue;

            long long waste = 0;
            int prevIdx = 0;
            for (int sz : b) {
                int idx = upper_bound(packages.begin(), packages.end(), sz) - packages.begin();
                int cnt = idx - prevIdx;
                if (cnt > 0) {
                    long long sumPkg = pref[idx] - pref[prevIdx];
                    waste += (long long)sz * cnt - sumPkg;
                }
                prevIdx = idx;
                if (prevIdx == n) break;
            }
            best = min(best, waste);
        }

        if (best == LLONG_MAX) return -1;
        return (int)(best % MOD);
    }
};
```

## Java

```java
class Solution {
    private static int upperBound(int[] arr, int target) {
        int l = 0, r = arr.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (arr[m] <= target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l; // first index > target
    }

    public int minWastedSpace(int[] packages, int[][] boxes) {
        final long MOD = 1_000_000_007L;
        Arrays.sort(packages);
        int n = packages.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + packages[i];
        }
        int maxPkg = packages[n - 1];
        long best = Long.MAX_VALUE;

        for (int[] supplier : boxes) {
            Arrays.sort(supplier);
            if (supplier[supplier.length - 1] < maxPkg) continue; // cannot fit all
            long waste = 0;
            int prevIdx = 0;
            for (int size : supplier) {
                int idx = upperBound(packages, size); // first package > size
                if (idx > prevIdx) {
                    long sumPkg = pref[idx] - pref[prevIdx];
                    waste += (long) size * (idx - prevIdx) - sumPkg;
                }
                prevIdx = idx;
                if (prevIdx == n) break; // all packages assigned
            }
            best = Math.min(best, waste);
        }

        return best == Long.MAX_VALUE ? -1 : (int) (best % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def minWastedSpace(self, packages, boxes):
        """
        :type packages: List[int]
        :type boxes: List[List[int]]
        :rtype: int
        """
        import bisect
        MOD = 10**9 + 7

        packages.sort()
        n = len(packages)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + packages[i]

        best = float('inf')

        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < packages[-1]:
                continue

            waste = 0
            prev = 0
            for size in supplier:
                idx = bisect.bisect_right(packages, size)
                if idx > prev:
                    waste += (idx - prev) * size - (prefix[idx] - prefix[prev])
                    prev = idx
                if prev == n:
                    break

            if waste < best:
                best = waste

        return -1 if best == float('inf') else best % MOD
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10**9 + 7
        packages.sort()
        n = len(packages)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + packages[i]

        best = float('inf')
        max_pkg = packages[-1]

        for blist in boxes:
            blist.sort()
            if blist[-1] < max_pkg:
                continue
            waste = 0
            prev = 0
            for size in blist:
                idx = bisect.bisect_right(packages, size)
                if idx > prev:
                    cnt = idx - prev
                    sum_pkgs = prefix[idx] - prefix[prev]
                    waste += cnt * size - sum_pkgs
                    prev = idx
                if prev == n:
                    break
            if prev == n and waste < best:
                best = waste

        return -1 if best == float('inf') else best % MOD
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

static int upper_bound(int *arr, int size, int target) {
    int l = 0, r = size;
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] <= target)
            l = m + 1;
        else
            r = m;
    }
    return l; // first index > target
}

int minWastedSpace(int* packages, int packagesSize, int** boxes, int boxesSize, int* boxesColSize) {
    const int MOD = 1000000007;
    if (packagesSize == 0) return 0;

    qsort(packages, packagesSize, sizeof(int), cmp_int);

    long long *pref = (long long *)malloc((packagesSize + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 1; i <= packagesSize; ++i)
        pref[i] = pref[i - 1] + packages[i - 1];

    int maxPkg = packages[packagesSize - 1];
    long long best = LLONG_MAX;

    for (int s = 0; s < boxesSize; ++s) {
        int len = boxesColSize[s];
        if (len == 0) continue;
        qsort(boxes[s], len, sizeof(int), cmp_int);
        if (boxes[s][len - 1] < maxPkg) continue; // cannot fit largest package

        long long waste = 0;
        int prevIdx = 0;

        for (int i = 0; i < len && prevIdx < packagesSize; ++i) {
            int bsize = boxes[s][i];
            int idx = upper_bound(packages, packagesSize, bsize);
            if (idx > prevIdx) {
                long long cnt = idx - prevIdx;
                waste += (long long)bsize * cnt - (pref[idx] - pref[prevIdx]);
                if (waste >= best) break; // no need to continue
                prevIdx = idx;
            }
        }

        if (prevIdx == packagesSize && waste < best)
            best = waste;
    }

    free(pref);
    if (best == LLONG_MAX) return -1;
    return (int)(best % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int MinWastedSpace(int[] packages, int[][] boxes) {
        const int MOD = 1000000007;
        Array.Sort(packages);
        int n = packages.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + packages[i];

        long best = long.MaxValue;
        int maxPkg = packages[n - 1];

        foreach (var supplier in boxes) {
            int m = supplier.Length;
            int[] sorted = new int[m];
            Array.Copy(supplier, sorted, m);
            Array.Sort(sorted);
            if (sorted[m - 1] < maxPkg) continue; // cannot fit largest package

            long waste = 0;
            int prevIdx = 0;

            foreach (int size in sorted) {
                int idx = UpperBound(packages, size); // first index > size
                int cnt = idx - prevIdx;
                if (cnt > 0) {
                    long sumPkg = pref[idx] - pref[prevIdx];
                    waste += (long)size * cnt - sumPkg;
                }
                prevIdx = idx;
                if (prevIdx == n) break; // all packages assigned
            }

            if (waste < best) best = waste;
        }

        return best == long.MaxValue ? -1 : (int)(best % MOD);
    }

    private int UpperBound(int[] arr, int target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} packages
 * @param {number[][]} boxes
 * @return {number}
 */
var minWastedSpace = function(packages, boxes) {
    const MOD = 1e9 + 7;
    packages.sort((a, b) => a - b);
    const n = packages.length;
    const prefix = new Array(n);
    for (let i = 0; i < n; ++i) {
        prefix[i] = packages[i] + (i > 0 ? prefix[i - 1] : 0);
    }
    const maxPkg = packages[n - 1];
    
    // binary search: first index > target
    function upperBound(arr, target) {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] <= target) l = m + 1;
            else r = m;
        }
        return l;
    }
    
    let best = Infinity;
    
    for (const supplier of boxes) {
        // sort box sizes
        const sorted = supplier.slice().sort((a, b) => a - b);
        if (sorted[sorted.length - 1] < maxPkg) continue; // cannot fit largest package
        
        let waste = 0;
        let prevIdx = -1;
        for (const size of sorted) {
            const ub = upperBound(packages, size);
            const curIdx = ub - 1;
            if (curIdx > prevIdx) {
                const cnt = curIdx - prevIdx;
                const sumPkg = prefix[curIdx] - (prevIdx >= 0 ? prefix[prevIdx] : 0);
                waste += cnt * size - sumPkg;
            }
            prevIdx = curIdx;
            if (prevIdx === n - 1) break; // all packages assigned
        }
        if (prevIdx === n - 1 && waste < best) {
            best = waste;
        }
    }
    
    return best === Infinity ? -1 : ((best % MOD) + MOD) % MOD;
};
```

## Typescript

```typescript
function minWastedSpace(packages: number[], boxes: number[][]): number {
    const MOD = 1_000_000_007;
    packages.sort((a, b) => a - b);
    const n = packages.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + packages[i];
    }

    function upperBound(arr: number[], target: number): number {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] <= target) l = m + 1;
            else r = m;
        }
        return l; // first index > target
    }

    let best = Infinity;

    for (const supplier of boxes) {
        const sorted = supplier.slice().sort((a, b) => a - b);
        if (sorted[sorted.length - 1] < packages[n - 1]) continue; // cannot fit largest package

        let waste = 0;
        let covered = 0;

        for (const size of sorted) {
            const idx = upperBound(packages, size); // first > size
            if (idx > covered) {
                const cnt = idx - covered;
                const sumPkg = prefix[idx] - prefix[covered];
                waste += size * cnt - sumPkg;
            }
            covered = Math.max(covered, idx);
            if (covered === n) break;
        }

        if (covered === n) {
            best = Math.min(best, waste);
        }
    }

    return best === Infinity ? -1 : best % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $packages
     * @param Integer[][] $boxes
     * @return Integer
     */
    function minWastedSpace($packages, $boxes) {
        $mod = 1000000007;
        sort($packages);
        $n = count($packages);
        // prefix sums: prefix[i] = sum of first i packages (0-indexed)
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $prefix[$i + 1] = $prefix[$i] + $packages[$i];
        }

        // helper: upper bound (first index > target)
        $upperBound = function($arr, $target) {
            $low = 0;
            $high = count($arr);
            while ($low < $high) {
                $mid = intdiv($low + $high, 2);
                if ($arr[$mid] <= $target) {
                    $low = $mid + 1;
                } else {
                    $high = $mid;
                }
            }
            return $low;
        };

        $best = PHP_INT_MAX;

        foreach ($boxes as $boxArr) {
            sort($boxArr);
            // if the largest box cannot fit the biggest package, skip
            if (end($boxArr) < $packages[$n - 1]) {
                continue;
            }

            $waste = 0;
            $prevIdx = 0; // first unassigned package index

            foreach ($boxArr as $size) {
                // find rightmost package that fits in this box size
                $rightExclusive = $upperBound($packages, $size); // first > size
                $right = $rightExclusive - 1;
                if ($right >= $prevIdx) {
                    $cnt = $right - $prevIdx + 1;
                    $sumPkg = $prefix[$right + 1] - $prefix[$prevIdx];
                    $waste += $size * $cnt - $sumPkg;
                    $prevIdx = $right + 1;
                }
                if ($prevIdx == $n) {
                    break; // all packages assigned
                }
            }

            if ($prevIdx == $n && $waste < $best) {
                $best = $waste;
            }
        }

        return $best === PHP_INT_MAX ? -1 : $best % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func minWastedSpace(_ packages: [Int], _ boxes: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let sortedPackages = packages.sorted()
        let n = sortedPackages.count
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(sortedPackages[i])
        }
        guard let maxPackage = sortedPackages.last else { return -1 }
        var minWaste = Int64.max
        
        for supplierBoxes in boxes {
            var boxSizes = supplierBoxes.sorted()
            if boxSizes.isEmpty { continue }
            if boxSizes.last! < maxPackage { continue }
            
            var waste: Int64 = 0
            var prevIdx = 0   // number of packages already assigned
            
            for size in boxSizes {
                let idx = upperBound(sortedPackages, size) // first index > size
                if idx > prevIdx {
                    let sumRange = prefix[idx] - prefix[prevIdx]
                    waste += Int64(size) * Int64(idx - prevIdx) - sumRange
                    prevIdx = idx
                }
                if prevIdx == n { break }
            }
            
            if prevIdx == n && waste < minWaste {
                minWaste = waste
            }
        }
        
        if minWaste == Int64.max {
            return -1
        } else {
            return Int(minWaste % Int64(MOD))
        }
    }
    
    private func upperBound(_ arr: [Int], _ target: Int) -> Int {
        var left = 0
        var right = arr.count
        while left < right {
            let mid = (left + right) >> 1
            if arr[mid] <= target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    private fun upperBound(arr: IntArray, target: Int): Int {
        var l = 0
        var r = arr.size
        while (l < r) {
            val m = (l + r) ushr 1
            if (arr[m] <= target) {
                l = m + 1
            } else {
                r = m
            }
        }
        return l
    }

    fun minWastedSpace(packages: IntArray, boxes: Array<IntArray>): Int {
        val MOD = 1_000_000_007L
        val n = packages.size
        val pkgs = packages.clone()
        pkgs.sort()
        val pref = LongArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + pkgs[i].toLong()
        }
        var answer = Long.MAX_VALUE

        for (b in boxes) {
            if (b.isEmpty()) continue
            val arr = b.clone()
            arr.sort()
            if (arr.last() < pkgs.last()) continue

            var waste = 0L
            var prevIdx = 0
            for (size in arr) {
                val idx = upperBound(pkgs, size)
                if (idx <= prevIdx) continue
                val count = idx - prevIdx
                val sumPkg = pref[idx] - pref[prevIdx]
                waste += size.toLong() * count - sumPkg
                prevIdx = idx
                if (prevIdx == n) break
            }
            if (prevIdx == n && waste < answer) {
                answer = waste
            }
        }

        return if (answer == Long.MAX_VALUE) -1 else ((answer % MOD).toInt())
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int minWastedSpace(List<int> packages, List<List<int>> boxes) {
    packages.sort();
    int n = packages.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + packages[i];
    }
    int maxPackage = packages[n - 1];
    int? bestWaste;

    for (var supplier in boxes) {
      supplier.sort();
      if (supplier.isEmpty || supplier.last < maxPackage) continue;

      int waste = 0;
      int prevIdx = 0; // number of packages already placed

      for (int size in supplier) {
        int idx = _upperBound(packages, size); // count of packages <= size
        if (idx > prevIdx) {
          int cnt = idx - prevIdx;
          int sumPkg = prefix[idx] - prefix[prevIdx];
          waste += size * cnt - sumPkg;
          prevIdx = idx;
        }
        if (prevIdx == n) break;
      }

      if (prevIdx == n) {
        if (bestWaste == null || waste < bestWaste) bestWaste = waste;
      }
    }

    return bestWaste == null ? -1 : bestWaste % _mod;
  }

  int _upperBound(List<int> arr, int target) {
    int lo = 0, hi = arr.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (arr[mid] <= target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}
```

## Golang

```go
package main

import "sort"

func minWastedSpace(packages []int, boxes [][]int) int {
	const MOD int64 = 1000000007
	sort.Ints(packages)
	n := len(packages)

	prefix := make([]int64, n)
	for i, v := range packages {
		if i == 0 {
			prefix[i] = int64(v)
		} else {
			prefix[i] = prefix[i-1] + int64(v)
		}
	}

	maxPkg := packages[n-1]
	minWaste := int64(^uint64(0) >> 1) // MaxInt64

	for _, b := range boxes {
		sort.Ints(b)
		if b[len(b)-1] < maxPkg {
			continue
		}
		var waste int64
		prevIdx := -1
		for _, size := range b {
			idx := sort.Search(len(packages), func(i int) bool { return packages[i] > size }) - 1
			if idx <= prevIdx {
				continue
			}
			cnt := idx - prevIdx
			sum := prefix[idx]
			if prevIdx >= 0 {
				sum -= prefix[prevIdx]
			}
			waste += int64(size)*int64(cnt) - sum
			prevIdx = idx
			if waste >= minWaste {
				break
			}
		}
		if prevIdx == n-1 && waste < minWaste {
			minWaste = waste
		}
	}

	if minWaste == int64(^uint64(0)>>1) {
		return -1
	}
	return int(minWaste % MOD)
}
```

## Ruby

```ruby
def min_wasted_space(packages, boxes)
  mod = 1_000_000_007
  packages.sort!
  n = packages.size
  prefix = Array.new(n + 1, 0)
  (1..n).each { |i| prefix[i] = prefix[i - 1] + packages[i - 1] }
  max_pkg = packages[-1]
  ans = Float::INFINITY

  # binary search: first index > target
  upper_bound = lambda do |arr, target|
    l = 0
    r = arr.length
    while l < r
      m = (l + r) / 2
      if arr[m] <= target
        l = m + 1
      else
        r = m
      end
    end
    l
  end

  boxes.each do |barr|
    sorted = barr.sort
    next if sorted[-1] < max_pkg

    waste = 0
    prev_idx = 0

    sorted.each do |size|
      hi = upper_bound.call(packages, size) # number of packages <= size
      cnt = hi - prev_idx
      if cnt > 0
        sum_pkg = prefix[hi] - prefix[prev_idx]
        waste += cnt * size - sum_pkg
      end
      prev_idx = hi
      break if prev_idx == n
    end

    ans = [ans, waste].min if prev_idx == n
  end

  return -1 if ans == Float::INFINITY
  ans % mod
end
```

## Scala

```scala
object Solution {
  def minWastedSpace(packages: Array[Int], boxes: Array[Array[Int]]): Int = {
    val MOD = 1000000007L
    java.util.Arrays.sort(packages)
    val n = packages.length
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + packages(i).toLong
      i += 1
    }
    val maxPkg = packages(n - 1)
    var best: Long = Long.MaxValue

    for (bArr <- boxes) {
      if (bArr.nonEmpty && bArr.max >= maxPkg) { // quick check without sorting whole array
        val sorted = bArr.clone()
        java.util.Arrays.sort(sorted)
        var waste: Long = 0L
        var prevIdx = 0
        var stop = false
        var idxBox = 0
        while (idxBox < sorted.length && prevIdx < n && !stop) {
          val size = sorted(idxBox)

          // upper bound search for last package <= size starting from prevIdx
          var lo = prevIdx
          var hi = n
          while (lo < hi) {
            val mid = (lo + hi) >>> 1
            if (packages(mid) <= size) lo = mid + 1 else hi = mid
          }
          val last = lo - 1 // index of last package that fits this box size

          if (last >= prevIdx) {
            val cnt = last - prevIdx + 1
            waste += size.toLong * cnt - (pref(last + 1) - pref(prevIdx))
            if (waste >= best) stop = true
            prevIdx = last + 1
          }
          idxBox += 1
        }
        if (!stop && prevIdx == n) {
          if (waste < best) best = waste
        }
      }
    }

    if (best == Long.MaxValue) -1 else ((best % MOD).toInt)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_wasted_space(packages: Vec<i32>, boxes: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = packages.len();
        if n == 0 {
            return 0;
        }
        // sort packages and build prefix sums
        let mut pkgs = packages.clone();
        pkgs.sort_unstable();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + pkgs[i] as i64;
        }
        let max_pkg = *pkgs.last().unwrap();

        let mut best: i64 = i64::MAX;

        for mut supplier_boxes in boxes.into_iter() {
            if supplier_boxes.is_empty() {
                continue;
            }
            supplier_boxes.sort_unstable();
            // If the largest box cannot fit the biggest package, skip this supplier
            if *supplier_boxes.last().unwrap() < max_pkg {
                continue;
            }

            let mut waste: i64 = 0;
            let mut prev_idx: usize = 0;

            for &b in &supplier_boxes {
                // number of packages that can fit into box size b
                let idx = pkgs.partition_point(|&x| x <= b);
                if idx > prev_idx {
                    let cnt = (idx - prev_idx) as i64;
                    let sum_pkg = pref[idx] - pref[prev_idx];
                    waste += cnt * b as i64 - sum_pkg;
                    // early stop if already worse than current best
                    if waste >= best {
                        break;
                    }
                    prev_idx = idx;
                }
                if prev_idx == n {
                    break;
                }
            }

            if prev_idx == n && waste < best {
                best = waste;
            }
        }

        if best == i64::MAX {
            -1
        } else {
            (best % MOD) as i32
        }
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (upper-bound vec target)
  (let loop ((lo 0) (hi (vector-length vec)))
    (if (= lo hi)
        lo
        (let* ((mid (quotient (+ lo hi) 2))
               (val (vector-ref vec mid)))
          (if (<= val target)
              (loop (+ mid 1) hi)
              (loop lo mid))))))

(define/contract (min-wasted-space packages boxes)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted-packages (sort packages <))
         (n (length sorted-packages))
         (pkg-vec (list->vector sorted-packages))
         (pref (make-vector (+ n 1) 0)))
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1)
                   (+ (vector-ref pref i) (vector-ref pkg-vec i))))
    (define min-waste #f)
    (for ([supplier boxes])
      (when (not (null? supplier))
        (let* ((sorted-boxes (sort supplier <))
               (max-box (list-ref sorted-boxes (- (length sorted-boxes) 1)))
               (largest-pkg (if (= n 0) 0 (vector-ref pkg-vec (- n 1)))))
          (when (>= max-box largest-pkg)
            (let loop ((i 0) (prevIdx 0) (waste 0))
              (if (= i (length sorted-boxes))
                  (when (= prevIdx n)
                    (set! min-waste
                          (if min-waste (min min-waste waste) waste)))
                  (let* ((b (list-ref sorted-boxes i))
                         (idx (upper-bound pkg-vec b))
                         (new-waste (+ waste (* b (- idx prevIdx))
                                      (- (vector-ref pref idx)
                                         (vector-ref pref prevIdx)))))
                    (loop (+ i 1) idx new-waste))))))))
    (if min-waste
        (modulo min-waste MOD)
        -1)))
```

## Erlang

```erlang
-spec min_wasted_space(Packages :: [integer()], Boxes :: [[integer()]]) -> integer().
min_wasted_space(Packages, Boxes) ->
    SortedPkgs = lists:sort(Packages),
    N = length(SortedPkgs),
    PkgTuple = list_to_tuple(SortedPkgs),
    PrefixTuple = build_prefix_tuple(SortedPkgs),
    MaxPkg = element(N, PkgTuple),
    MinWaste = find_min_waste(Boxes, N, PkgTuple, PrefixTuple, MaxPkg, undefined),
    case MinWaste of
        undefined -> -1;
        _ -> MinWaste rem 1000000007
    end.

build_prefix_tuple(Pkgs) ->
    PrefixList = prefix_sums(Pkgs, [], 0),
    list_to_tuple([0 | PrefixList]).

prefix_sums([], Acc, _) -> lists:reverse(Acc);
prefix_sums([H|T], Acc, Sum) ->
    NewSum = Sum + H,
    prefix_sums(T, [NewSum|Acc], NewSum).

find_min_waste([], _N, _PkgTuple, _PrefixTuple, _MaxPkg, Min) -> Min;
find_min_waste([BoxList|Rest], N, PkgTuple, PrefixTuple, MaxPkg, CurrentMin) ->
    SortedBoxes = lists:sort(BoxList),
    case lists:last(SortedBoxes) >= MaxPkg of
        false ->
            find_min_waste(Rest, N, PkgTuple, PrefixTuple, MaxPkg, CurrentMin);
        true ->
            Waste = compute_waste(SortedBoxes, N, PkgTuple, PrefixTuple),
            NewMin = case CurrentMin of
                undefined -> Waste;
                _ when Waste < CurrentMin -> Waste;
                _ -> CurrentMin
            end,
            find_min_waste(Rest, N, PkgTuple, PrefixTuple, MaxPkg, NewMin)
    end.

compute_waste(BoxesSorted, N, PkgTuple, PrefixTuple) ->
    compute_waste(BoxesSorted, 0, 0, N, PkgTuple, PrefixTuple).

compute_waste([], _PrevIdx, AccWaste, _N, _PkgTuple, _PrefixTuple) -> AccWaste;
compute_waste([B|Rest], PrevIdx, AccWaste, N, PkgTuple, PrefixTuple) ->
    TotalIdx = binary_search(B, N, PkgTuple),
    Count = TotalIdx - PrevIdx,
    case Count > 0 of
        true ->
            SumPkgs = element(TotalIdx+1, PrefixTuple) - element(PrevIdx+1, PrefixTuple),
            NewAcc = AccWaste + B*Count - SumPkgs,
            compute_waste(Rest, TotalIdx, NewAcc, N, PkgTuple, PrefixTuple);
        false ->
            compute_waste(Rest, PrevIdx, AccWaste, N, PkgTuple, PrefixTuple)
    end.

binary_search(Size, N, Tuple) ->
    binary_search(1, N, Size, Tuple, 0).

binary_search(Low, High, Size, Tuple, Best) when Low =< High ->
    Mid = (Low + High) div 2,
    Val = element(Mid, Tuple),
    if
        Val =< Size ->
            binary_search(Mid+1, High, Size, Tuple, Mid);
        true ->
            binary_search(Low, Mid-1, Size, Tuple, Best)
    end;
binary_search(_, _, _, _, Best) -> Best.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec min_wasted_space(packages :: [integer], boxes :: [[integer]]) :: integer
  def min_wasted_space(packages, boxes) do
    mod = 1_000_000_007

    sorted_pkgs = Enum.sort(packages)
    n = length(sorted_pkgs)

    # prefix sums: pref[i] = sum of first i packages, pref[0]=0
    {pref_tail, _} =
      Enum.map_reduce(sorted_pkgs, 0, fn x, acc ->
        new = acc + x
        {new, new}
      end)

    pref = [0 | pref_tail]
    pref_tuple = List.to_tuple(pref)
    pkg_tuple = List.to_tuple(sorted_pkgs)
    max_pkg = List.last(sorted_pkgs)

    min_waste =
      Enum.reduce(boxes, nil, fn box_list, cur_min ->
        sorted_boxes = Enum.sort(box_list)

        # if the largest box cannot fit the biggest package, skip
        if List.last(sorted_boxes) < max_pkg do
          cur_min
        else
          {last_idx, waste} =
            Enum.reduce(sorted_boxes, {-1, 0}, fn b, {prev_idx, acc_waste} ->
              idx = upper_bound(pkg_tuple, b)

              if idx > prev_idx do
                count = idx - prev_idx
                sum_pkgs = elem(pref_tuple, idx + 1) - elem(pref_tuple, prev_idx + 1)
                added = b * count - sum_pkgs
                {idx, acc_waste + added}
              else
                {prev_idx, acc_waste}
              end
            end)

          if last_idx == n - 1 do
            case cur_min do
              nil -> waste
              _ -> min(cur_min, waste)
            end
          else
            cur_min
          end
        end
      end)

    case min_waste do
      nil -> -1
      w -> rem(w, mod)
    end
  end

  # binary search: returns the last index where value <= size, or -1 if none
  defp upper_bound(tuple, size) do
    n = tuple_size(tuple)
    upper_bound(tuple, size, 0, n - 1, -1)
  end

  defp upper_bound(_tuple, _size, lo, hi, acc) when lo > hi, do: acc

  defp upper_bound(tuple, size, lo, hi, acc) do
    mid = div(lo + hi, 2)
    val = elem(tuple, mid)

    if val <= size do
      upper_bound(tuple, size, mid + 1, hi, mid)
    else
      upper_bound(tuple, size, lo, mid - 1, acc)
    end
  end
end
```
