# 1093. Statistics from a Large Sample

## Cpp

```cpp
class Solution {
public:
    vector<double> sampleStats(vector<int>& count) {
        long long totalCount = 0;
        long long totalSum = 0;
        int minVal = -1, maxVal = -1;
        int modeVal = -1;
        long long modeCnt = -1;
        
        for (int i = 0; i < 256; ++i) {
            if (count[i] == 0) continue;
            if (minVal == -1) minVal = i;
            maxVal = i;
            totalCount += count[i];
            totalSum += (long long)i * count[i];
            if ((long long)count[i] > modeCnt) {
                modeCnt = count[i];
                modeVal = i;
            }
        }
        
        double mean = (double)totalSum / (double)totalCount;
        
        auto kth = [&](long long k) -> int {
            long long cum = 0;
            for (int i = 0; i < 256; ++i) {
                cum += count[i];
                if (cum >= k) return i;
            }
            return 255; // should never reach here
        };
        
        double median;
        if (totalCount % 2 == 1) {
            long long k = (totalCount + 1) / 2;
            median = (double)kth(k);
        } else {
            long long k1 = totalCount / 2;
            long long k2 = k1 + 1;
            double m1 = kth(k1);
            double m2 = kth(k2);
            median = (m1 + m2) / 2.0;
        }
        
        return { (double)minVal, (double)maxVal, mean, median, (double)modeVal };
    }
};
```

## Java

```java
class Solution {
    public double[] sampleStats(int[] count) {
        int min = -1;
        int max = -1;
        long total = 0L;
        long sum = 0L;
        int modeIdx = 0;
        int modeCount = 0;

        for (int i = 0; i < 256; i++) {
            int c = count[i];
            if (c > 0) {
                if (min == -1) min = i;
                max = i;
                total += c;
                sum += (long) i * c;
                if (c > modeCount) {
                    modeCount = c;
                    modeIdx = i;
                }
            }
        }

        double mean = (double) sum / total;

        long leftPos, rightPos;
        if ((total & 1L) == 0) { // even
            leftPos = total / 2;
            rightPos = leftPos + 1;
        } else { // odd
            leftPos = rightPos = (total + 1) / 2;
        }

        int leftVal = -1, rightVal = -1;
        long cum = 0L;
        for (int i = 0; i < 256; i++) {
            cum += count[i];
            if (leftVal == -1 && cum >= leftPos) leftVal = i;
            if (rightVal == -1 && cum >= rightPos) {
                rightVal = i;
                break;
            }
        }

        double median = (leftVal + rightVal) / 2.0;

        return new double[]{min, max, mean, median, modeIdx};
    }
}
```

## Python

```python
class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        # minimum
        min_val = next(i for i, c in enumerate(count) if c > 0)
        # maximum
        max_val = len(count) - 1 - next(i for i, c in enumerate(reversed(count)) if c > 0)
        # total count and sum of values
        total = 0
        total_sum = 0
        mode_val = 0
        mode_cnt = 0
        for i, c in enumerate(count):
            if c:
                total += c
                total_sum += i * c
                if c > mode_cnt:
                    mode_cnt = c
                    mode_val = i
        mean = total_sum / float(total)

        # helper to find k-th element (1-indexed)
        def kth(k):
            cum = 0
            for i, c in enumerate(count):
                cum += c
                if cum >= k:
                    return i
            return -1  # should never happen

        if total % 2 == 1:
            median = float(kth((total + 1) // 2))
        else:
            left = kth(total // 2)
            right = kth(total // 2 + 1)
            median = (left + right) / 2.0

        return [float(min_val), float(max_val), mean, median, float(mode_val)]
```

## Python3

```python
from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = 0
        total_sum = 0
        min_val = None
        max_val = None
        mode_val = 0
        max_cnt = -1

        for i, c in enumerate(count):
            if c:
                if min_val is None:
                    min_val = i
                max_val = i
                total += c
                total_sum += i * c
                if c > max_cnt:
                    max_cnt = c
                    mode_val = i

        mean = total_sum / total

        def kth(k: int) -> int:
            cum = 0
            for i, c in enumerate(count):
                cum += c
                if cum >= k:
                    return i
            return -1  # should never reach here

        if total % 2 == 1:
            median = float(kth((total + 1) // 2))
        else:
            left = kth(total // 2)
            right = kth(total // 2 + 1)
            median = (left + right) / 2.0

        return [float(min_val), float(max_val), mean, median, float(mode_val)]
```

## C

```c
#include <stdlib.h>

static int findK(const int* cnt, int sz, long long k) {
    long long cum = 0;
    for (int i = 0; i < sz; ++i) {
        cum += cnt[i];
        if (cum >= k) return i;
    }
    return -1; // should never reach here
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* sampleStats(int* count, int countSize, int* returnSize) {
    long long total = 0;
    long long sum = 0;
    int minVal = -1, maxVal = -1;
    int modeVal = 0;
    int maxCount = -1;

    for (int i = 0; i < countSize; ++i) {
        if (count[i] > 0) {
            if (minVal == -1) minVal = i;
            maxVal = i;
            if (count[i] > maxCount) {
                maxCount = count[i];
                modeVal = i;
            }
            total += (long long)count[i];
            sum   += (long long)i * count[i];
        }
    }

    double mean = (double)sum / (double)total;

    double median;
    if (total % 2 == 1) {
        long long target = (total + 1) / 2;
        int val = findK(count, countSize, target);
        median = (double)val;
    } else {
        long long leftPos  = total / 2;
        long long rightPos = leftPos + 1;
        int leftVal  = findK(count, countSize, leftPos);
        int rightVal = findK(count, countSize, rightPos);
        median = ((double)leftVal + (double)rightVal) / 2.0;
    }

    double* res = (double*)malloc(sizeof(double) * 5);
    res[0] = (double)minVal;
    res[1] = (double)maxVal;
    res[2] = mean;
    res[3] = median;
    res[4] = (double)modeVal;

    *returnSize = 5;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public double[] SampleStats(int[] count) {
        int min = -1;
        int max = -1;
        int mode = -1;
        long total = 0;
        long sum = 0;
        long maxCount = -1;

        for (int i = 0; i < count.Length; i++) {
            int c = count[i];
            if (c > 0) {
                if (min == -1) min = i;
                max = i;
                if ((long)c > maxCount) {
                    maxCount = c;
                    mode = i;
                }
                total += c;
                sum += (long)i * c;
            }
        }

        double mean = (double)sum / total;

        long leftPos = (total + 1) / 2;
        long rightPos = (total % 2 == 0) ? (total / 2 + 1) : leftPos;

        int leftVal = -1, rightVal = -1;
        long cum = 0;
        for (int i = 0; i < count.Length; i++) {
            cum += count[i];
            if (leftVal == -1 && cum >= leftPos) leftVal = i;
            if (rightVal == -1 && cum >= rightPos) { rightVal = i; break; }
        }

        double median = (leftVal + rightVal) / 2.0;

        return new double[] { min, max, mean, median, mode };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} count
 * @return {number[]}
 */
var sampleStats = function(count) {
    let min = -1, max = -1;
    let total = 0;
    let sum = 0;
    let mode = -1, maxCount = -1;

    for (let i = 0; i < 256; ++i) {
        const c = count[i];
        if (c > 0) {
            if (min === -1) min = i;
            max = i;
            total += c;
            sum += i * c;
            if (c > maxCount) {
                maxCount = c;
                mode = i;
            }
        }
    }

    const mean = sum / total;

    const findKth = (k) => {
        let cum = 0;
        for (let i = 0; i < 256; ++i) {
            cum += count[i];
            if (cum >= k) return i;
        }
        return -1;
    };

    let median;
    if (total % 2 === 1) {
        const k = Math.floor(total / 2) + 1;
        median = findKth(k);
    } else {
        const k1 = total / 2;
        const k2 = k1 + 1;
        const v1 = findKth(k1);
        const v2 = findKth(k2);
        median = (v1 + v2) / 2;
    }

    return [min, max, mean, median, mode];
};
```

## Typescript

```typescript
function sampleStats(count: number[]): number[] {
    let min = -1;
    let max = -1;
    let total = 0;
    let sum = 0;
    let mode = -1;
    let modeCount = -1;

    for (let i = 0; i < 256; i++) {
        const c = count[i];
        if (c > 0) {
            if (min === -1) min = i;
            max = i;
            total += c;
            sum += i * c;
            if (c > modeCount) {
                modeCount = c;
                mode = i;
            }
        }
    }

    const mean = sum / total;

    let median: number;
    if (total % 2 === 1) {
        const target = Math.floor(total / 2) + 1;
        let cum = 0;
        for (let i = 0; i < 256; i++) {
            cum += count[i];
            if (cum >= target) {
                median = i;
                break;
            }
        }
    } else {
        const leftPos = total / 2;
        const rightPos = leftPos + 1;
        let cum = 0;
        let leftVal = -1;
        let rightVal = -1;
        for (let i = 0; i < 256; i++) {
            cum += count[i];
            if (leftVal === -1 && cum >= leftPos) leftVal = i;
            if (rightVal === -1 && cum >= rightPos) {
                rightVal = i;
                break;
            }
        }
        median = (leftVal + rightVal) / 2;
    }

    return [min, max, mean, median, mode];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $count
     * @return Float[]
     */
    function sampleStats($count) {
        $min = null;
        $max = null;
        $sum = 0;
        $total = 0;
        $mode = 0;
        $maxCount = -1;

        foreach ($count as $i => $c) {
            if ($c > 0) {
                if ($min === null) $min = $i;
                $max = $i;
                $total += $c;
                $sum += $i * $c;
                if ($c > $maxCount) {
                    $maxCount = $c;
                    $mode = $i;
                }
            }
        }

        $mean = $sum / $total;

        // median calculation
        if ($total % 2 == 1) { // odd
            $k = intdiv($total, 2) + 1; // 1‑based position
            $cum = 0;
            foreach ($count as $i => $c) {
                $cum += $c;
                if ($cum >= $k) {
                    $median = (float)$i;
                    break;
                }
            }
        } else { // even
            $k1 = intdiv($total, 2);
            $k2 = $k1 + 1;
            $cum = 0;
            $m1 = null;
            $m2 = null;
            foreach ($count as $i => $c) {
                $cum += $c;
                if ($m1 === null && $cum >= $k1) {
                    $m1 = $i;
                }
                if ($m2 === null && $cum >= $k2) {
                    $m2 = $i;
                    break;
                }
            }
            $median = ($m1 + $m2) / 2.0;
        }

        return [(float)$min, (float)$max, $mean, $median, (float)$mode];
    }
}
```

## Swift

```swift
class Solution {
    func sampleStats(_ count: [Int]) -> [Double] {
        var minVal = -1
        var maxVal = -1
        var modeVal = 0
        var maxCount = 0
        var totalCount: Int64 = 0
        var totalSum: Int64 = 0
        
        for i in 0..<256 {
            let c = count[i]
            if c > 0 {
                if minVal == -1 { minVal = i }
                maxVal = i
                if c > maxCount {
                    maxCount = c
                    modeVal = i
                }
                totalCount += Int64(c)
                totalSum += Int64(i) * Int64(c)
            }
        }
        
        let mean = Double(totalSum) / Double(totalCount)
        var median: Double = 0.0
        
        if totalCount % 2 == 1 {
            let target = (totalCount + 1) / 2
            var cum: Int64 = 0
            for i in 0..<256 {
                cum += Int64(count[i])
                if cum >= target {
                    median = Double(i)
                    break
                }
            }
        } else {
            let leftTarget = totalCount / 2
            let rightTarget = leftTarget + 1
            var cum: Int64 = 0
            var leftVal = -1
            var rightVal = -1
            for i in 0..<256 {
                cum += Int64(count[i])
                if leftVal == -1 && cum >= leftTarget {
                    leftVal = i
                }
                if rightVal == -1 && cum >= rightTarget {
                    rightVal = i
                    break
                }
            }
            median = (Double(leftVal) + Double(rightVal)) / 2.0
        }
        
        return [Double(minVal), Double(maxVal), mean, median, Double(modeVal)]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sampleStats(count: IntArray): DoubleArray {
        var min = -1
        var max = -1
        var mode = -1
        var modeCount = 0L
        var total = 0L
        var sum = 0L

        for (i in 0..255) {
            val c = count[i].toLong()
            if (c > 0) {
                if (min == -1) min = i
                max = i
                total += c
                sum += i.toLong() * c
                if (c > modeCount) {
                    modeCount = c
                    mode = i
                }
            }
        }

        val mean = sum.toDouble() / total

        val median: Double = if (total % 2L == 1L) {
            val target = (total + 1) / 2
            var cum = 0L
            var medVal = -1
            for (i in 0..255) {
                cum += count[i].toLong()
                if (cum >= target) {
                    medVal = i
                    break
                }
            }
            medVal.toDouble()
        } else {
            val target1 = total / 2
            val target2 = target1 + 1
            var cum = 0L
            var v1 = -1
            var v2 = -1
            for (i in 0..255) {
                cum += count[i].toLong()
                if (v1 == -1 && cum >= target1) {
                    v1 = i
                }
                if (cum >= target2) {
                    v2 = i
                    break
                }
            }
            (v1 + v2) / 2.0
        }

        return doubleArrayOf(min.toDouble(), max.toDouble(), mean, median, mode.toDouble())
    }
}
```

## Dart

```dart
class Solution {
  List<double> sampleStats(List<int> count) {
    int total = 0;
    int minVal = -1;
    int maxVal = -1;
    int modeVal = -1;
    int modeCount = -1;
    int sumInt = 0;

    for (int i = 0; i < count.length; i++) {
      int c = count[i];
      if (c > 0) {
        if (minVal == -1) minVal = i;
        maxVal = i;
        sumInt += i * c;
        total += c;
        if (c > modeCount) {
          modeCount = c;
          modeVal = i;
        }
      }
    }

    double mean = sumInt / total;

    double median;
    if (total % 2 == 1) {
      int k = (total + 1) ~/ 2;
      int val = _kth(count, k);
      median = val.toDouble();
    } else {
      int k1 = total ~/ 2;
      int k2 = k1 + 1;
      int v1 = _kth(count, k1);
      int v2 = _kth(count, k2);
      median = (v1 + v2) / 2.0;
    }

    return [
      minVal.toDouble(),
      maxVal.toDouble(),
      mean,
      median,
      modeVal.toDouble()
    ];
  }

  int _kth(List<int> count, int k) {
    int cum = 0;
    for (int i = 0; i < count.length; i++) {
      cum += count[i];
      if (cum >= k) return i;
    }
    return -1; // unreachable
  }
}
```

## Golang

```go
func sampleStats(count []int) []float64 {
    var totalCount int64
    var sum int64
    minIdx := -1
    maxIdx := -1
    modeIdx := 0
    var modeCnt int64 = -1

    for i, c := range count {
        if c > 0 {
            if minIdx == -1 {
                minIdx = i
            }
            maxIdx = i
            if int64(c) > modeCnt {
                modeCnt = int64(c)
                modeIdx = i
            }
        }
        totalCount += int64(c)
        sum += int64(i) * int64(c)
    }

    mean := float64(sum) / float64(totalCount)

    // helper to find k-th element (1-indexed) in the expanded sample
    findKth := func(k int64) int {
        var cum int64
        for i, c := range count {
            cum += int64(c)
            if cum >= k {
                return i
            }
        }
        return -1 // should never reach here
    }

    var median float64
    if totalCount%2 == 1 {
        k := (totalCount + 1) / 2
        median = float64(findKth(k))
    } else {
        k1 := totalCount / 2
        k2 := k1 + 1
        v1 := findKth(k1)
        v2 := findKth(k2)
        median = (float64(v1) + float64(v2)) / 2.0
    }

    return []float64{
        float64(minIdx),
        float64(maxIdx),
        mean,
        median,
        float64(modeIdx),
    }
}
```

## Ruby

```ruby
def sample_stats(count)
  total = 0
  sum = 0
  mode = 0
  max_cnt = -1
  min_val = nil
  max_val = nil

  count.each_with_index do |c, i|
    next if c == 0
    total += c
    sum += i * c
    min_val = i if min_val.nil?
    max_val = i
    if c > max_cnt
      max_cnt = c
      mode = i
    end
  end

  mean = sum.to_f / total

  if total.odd?
    k = (total + 1) / 2
    cum = 0
    median_val = nil
    count.each_with_index do |c, i|
      cum += c
      if cum >= k
        median_val = i
        break
      end
    end
    median = median_val.to_f
  else
    k1 = total / 2
    k2 = k1 + 1
    cum = 0
    val1 = nil
    val2 = nil
    count.each_with_index do |c, i|
      cum += c
      if val1.nil? && cum >= k1
        val1 = i
      end
      if cum >= k2
        val2 = i
        break
      end
    end
    median = (val1 + val2) / 2.0
  end

  [min_val.to_f, max_val.to_f, mean, median, mode.to_f]
end
```

## Scala

```scala
object Solution {
    def sampleStats(count: Array[Int]): Array[Double] = {
        var totalCount: Long = 0L
        var sum: Long = 0L
        var minVal = -1
        var maxVal = -1
        var modeVal = -1
        var modeCount: Long = -1L

        for (i <- 0 until 256) {
            val c = count(i).toLong
            if (c > 0) {
                if (minVal == -1) minVal = i
                maxVal = i
                totalCount += c
                sum += c * i
                if (c > modeCount) {
                    modeCount = c
                    modeVal = i
                }
            }
        }

        val mean = sum.toDouble / totalCount

        def findKth(k: Long): Int = {
            var cum: Long = 0L
            for (i <- 0 until 256) {
                cum += count(i).toLong
                if (cum >= k) return i
            }
            -1 // unreachable due to constraints
        }

        val median = if (totalCount % 2 == 1) {
            findKth((totalCount + 1) / 2).toDouble
        } else {
            val left = findKth(totalCount / 2)
            val right = findKth(totalCount / 2 + 1)
            (left + right) / 2.0
        }

        Array(minVal.toDouble, maxVal.toDouble, mean, median, modeVal.toDouble)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sample_stats(count: Vec<i32>) -> Vec<f64> {
        let mut min_val: i32 = -1;
        let mut max_val: i32 = -1;
        let mut total: i64 = 0;
        let mut sum: i64 = 0;
        let mut mode_val: i32 = -1;
        let mut mode_cnt: i64 = -1;

        for (i, &c) in count.iter().enumerate() {
            if c > 0 {
                if min_val == -1 {
                    min_val = i as i32;
                }
                max_val = i as i32;
                total += c as i64;
                sum += (i as i64) * (c as i64);
                if (c as i64) > mode_cnt {
                    mode_cnt = c as i64;
                    mode_val = i as i32;
                }
            }
        }

        let mean = sum as f64 / total as f64;

        // helper to find k-th element (1-indexed)
        fn kth(count: &Vec<i32>, k: i64) -> i32 {
            let mut cum = 0i64;
            for (i, &c) in count.iter().enumerate() {
                cum += c as i64;
                if cum >= k {
                    return i as i32;
                }
            }
            255 // fallback, should never happen
        }

        let median = if total % 2 == 1 {
            let k = (total + 1) / 2;
            kth(&count, k) as f64
        } else {
            let k1 = total / 2;
            let k2 = k1 + 1;
            (kth(&count, k1) as f64 + kth(&count, k2) as f64) / 2.0
        };

        vec![
            min_val as f64,
            max_val as f64,
            mean,
            median,
            mode_val as f64,
        ]
    }
}
```

## Racket

```racket
(define/contract (sample-stats count)
  (-> (listof exact-integer?) (listof flonum?))
  (let* ((len (length count)))
    (unless (= len 256) (error "count length must be 256"))
    ;; gather basic statistics
    (define-values (min max total sum mode modecnt)
      (for/fold ([min #f] [max #f] [total 0] [sum 0] [mode -1] [modecnt -1])
                ([i (in-range len)]
                 [c (in-list count)])
        (define new-min
          (if (and (> c 0) (or (not min) (< i min))) i min))
        (define new-max
          (if (> c 0) i max))
        (define new-total (+ total c))
        (define new-sum (+ sum (* i c)))
        (if (> c modecnt)
            (values new-min new-max new-total new-sum i c)
            (values new-min new-max new-total new-sum mode modecnt))))
    ;; helper to find k‑th element (1‑based) in the multiset
    (define (find-k k)
      (let loop ((i 0) (cum 0))
        (if (= i len)
            (error "k out of range")
            (let* ((c (list-ref count i))
                   (new-cum (+ cum c)))
              (if (>= new-cum k)
                  i
                  (loop (+ i 1) new-cum))))))
    ;; median computation
    (define median
      (if (odd? total)
          (exact->inexact (find-k (add1 (quotient total 2)))) ; (total+1)/2
          (let* ((left (find-k (quotient total 2)))
                 (right (find-k (+ 1 (quotient total 2)))))
            (/ (+ left right) 2.0))))
    ;; assemble result as list of flonums
    (list (exact->inexact min)
          (exact->inexact max)
          (exact->inexact (/ sum total))
          median
          (exact->inexact mode))))
```

## Erlang

```erlang
-module(solution).
-export([sample_stats/1]).
-spec sample_stats(Count :: [integer()]) -> [float()].

sample_stats(Count) ->
    {MinIdx, MaxIdx, ModeIdx, Sum, Total} =
        lists:foldl(
            fun({Idx, C}, {MinAcc, MaxAcc, {ModeIdxAcc, ModeCntAcc}, SumAcc, TotAcc}) ->
                NewMin = case MinAcc of
                    undefined when C > 0 -> Idx;
                    _ -> MinAcc
                end,
                NewMax = if C > 0 -> Idx; true -> MaxAcc end,
                {NewModeIdx, NewModeCnt} =
                    if C > ModeCntAcc ->
                        {Idx, C};
                       true ->
                        {ModeIdxAcc, ModeCntAcc}
                    end,
                {NewMin, NewMax, {NewModeIdx, NewModeCnt}, SumAcc + Idx*C, TotAcc + C}
            end,
            {undefined, undefined, {0, -1}, 0, 0},
            lists:zip(lists:seq(0,255), Count)),
    MinF = float(MinIdx),
    MaxF = float(MaxIdx),
    MeanF = Sum / Total,
    ModeF = float(ModeIdx),
    MedianF =
        case Total rem 2 of
            1 ->
                K = (Total + 1) div 2,
                V = kth(K, Count),
                float(V);
            0 ->
                K1 = Total div 2,
                K2 = K1 + 1,
                V1 = kth(K1, Count),
                V2 = kth(K2, Count),
                (V1 + V2) / 2.0
        end,
    [MinF, MaxF, MeanF, MedianF, ModeF].

kth(K, Count) ->
    kth_helper(K, Count, 0).

kth_helper(_K, [], _Idx) -> undefined;
kth_helper(K, [C|Rest], Idx) ->
    if K =< C ->
            Idx;
       true ->
            kth_helper(K - C, Rest, Idx + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sample_stats(count :: [integer]) :: [float]
  def sample_stats(count) do
    {total, sum, mode_val, _mode_cnt, min_val, max_val} =
      Enum.with_index(count)
      |> Enum.reduce({0, 0, nil, -1, nil, nil}, fn {c, i},
                                                   {tot, s, mval, mcnt, minv, maxv} ->
        tot2 = tot + c
        s2 = s + c * i

        {mval2, mcnt2} =
          if c > mcnt do
            {i, c}
          else
            {mval, mcnt}
          end

        minv2 =
          cond do
            minv != nil -> minv
            c > 0 -> i
            true -> nil
          end

        maxv2 = if c > 0, do: i, else: maxv

        {tot2, s2, mval2, mcnt2, minv2, maxv2}
      end)

    mean = sum / total

    median =
      if rem(total, 2) == 1 do
        k = div(total, 2) + 1
        find_kth(count, k) * 1.0
      else
        k1 = div(total, 2)
        k2 = k1 + 1
        (find_kth(count, k1) + find_kth(count, k2)) / 2.0
      end

    [min_val * 1.0, max_val * 1.0, mean, median, mode_val * 1.0]
  end

  defp find_kth(count, k) do
    Enum.reduce_while(Enum.with_index(count), 0, fn {c, i}, acc ->
      new_acc = acc + c

      if new_acc >= k do
        {:halt, i}
      else
        {:cont, new_acc}
      end
    end)
  end
end
```
