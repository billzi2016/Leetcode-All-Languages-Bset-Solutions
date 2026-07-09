# 3068. Find the Maximum Sum of Node Values

## Cpp

```cpp
class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        long long base = 0;
        long long sumPos = 0;
        int cntPos = 0;
        long long minPos = LLONG_MAX;
        long long maxNonPos = LLONG_MIN; // includes zero and negatives
        
        for (int v : nums) {
            base += v;
        }
        
        for (int v : nums) {
            long long xorVal = (long long)(v ^ k);
            long long diff = xorVal - v;
            if (diff > 0) {
                sumPos += diff;
                cntPos++;
                if (diff < minPos) minPos = diff;
            } else {
                if (diff > maxNonPos) maxNonPos = diff; // could be zero
            }
        }
        
        if (cntPos % 2 == 0) {
            return base + sumPos;
        } else {
            long long option1 = base + sumPos - minPos; // drop smallest positive gain
            long long option2 = LLONG_MIN;
            if (maxNonPos != LLONG_MIN) {
                option2 = base + sumPos + maxNonPos; // add best non-positive gain (zero or negative)
            }
            return max(option1, option2);
        }
    }
};
```

## Java

```java
class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        long baseSum = 0;
        long posSum = 0;
        int posCount = 0;
        long minPosDelta = Long.MAX_VALUE; // smallest positive delta
        long maxNonPosDelta = Long.MIN_VALUE; // largest delta <= 0

        for (int num : nums) {
            baseSum += num;
            long xorVal = (long)(num ^ k);
            long delta = xorVal - num;
            if (delta > 0) {
                posSum += delta;
                posCount++;
                if (delta < minPosDelta) minPosDelta = delta;
            } else {
                if (delta > maxNonPosDelta) maxNonPosDelta = delta;
            }
        }

        if (posCount % 2 == 0) {
            return baseSum + posSum;
        } else {
            long optionDrop = baseSum + posSum - minPosDelta; // drop one positive
            long optionAdd = Long.MIN_VALUE;
            if (maxNonPosDelta != Long.MIN_VALUE) {
                optionAdd = baseSum + posSum + maxNonPosDelta; // add a non‑positive delta
            }
            return Math.max(optionDrop, optionAdd);
        }
    }
}
```

## Python

```python
class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        total = sum(nums)
        pos_sum = 0
        min_pos = None   # smallest positive diff
        max_nonpos = -10**18  # largest non-positive diff (could be zero or negative)

        for v in nums:
            diff = (v ^ k) - v
            if diff > 0:
                pos_sum += diff
                if min_pos is None or diff < min_pos:
                    min_pos = diff
            else:
                if diff > max_nonpos:
                    max_nonpos = diff

        # count of positive diffs
        cnt_pos = 0
        for v in nums:
            if (v ^ k) - v > 0:
                cnt_pos += 1

        if cnt_pos % 2 == 0:
            return total + pos_sum
        # odd number of positives: need to adjust parity
        # option1: drop the smallest positive diff
        opt1 = total + pos_sum - (min_pos if min_pos is not None else 0)
        # option2: add the best non-positive diff (could be zero or negative)
        opt2 = total + pos_sum + max_nonpos
        return max(opt1, opt2)
```

## Python3

```python
from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = sum(nums)
        pos_count = 0
        min_pos_delta = float('inf')
        max_nonpos_delta = -10**18  # sentinel for no non-positive delta
        
        for v in nums:
            delta = (v ^ k) - v
            if delta > 0:
                total += delta
                pos_count += 1
                if delta < min_pos_delta:
                    min_pos_delta = delta
            else:
                if delta > max_nonpos_delta:
                    max_nonpos_delta = delta
        
        if pos_count % 2 == 0:
            return total
        # need to adjust parity
        option_remove = total - min_pos_delta
        option_add = total + max_nonpos_delta if max_nonpos_delta != -10**18 else -10**18
        return max(option_remove, option_add)
```

## C

```c
#include <limits.h>
#include <stddef.h>

long long maximumValueSum(int* nums, int numsSize, int k, int** edges, int edgesSize, int* edgesColSize) {
    (void)edges;      // unused
    (void)edgesSize;  // unused
    (void)edgesColSize; // unused

    long long base = 0;
    long long sumPos = 0;
    int posCount = 0;
    int minPosDelta = INT_MAX;
    int maxNonPosDelta = INT_MIN;

    for (int i = 0; i < numsSize; ++i) {
        int xorVal = nums[i] ^ k;
        int delta = xorVal - nums[i];
        base += nums[i];

        if (delta > 0) {
            ++posCount;
            sumPos += delta;
            if (delta < minPosDelta) minPosDelta = delta;
        } else {
            if (delta > maxNonPosDelta) maxNonPosDelta = delta;
        }
    }

    if ((posCount & 1) == 0) {
        return base + sumPos;
    }

    long long option1 = base + sumPos - minPosDelta; // drop smallest positive delta
    long long option2 = LLONG_MIN;
    if (maxNonPosDelta != INT_MIN) { // there exists a non‑positive delta
        option2 = base + sumPos + maxNonPosDelta; // add best non‑positive delta
    }
    return option1 > option2 ? option1 : option2;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public long MaximumValueSum(int[] nums, int k, int[][] edges) {
        long baseSum = 0;
        long sumPosDiff = 0;
        int posCount = 0;
        long minPosDiff = long.MaxValue;
        long maxNonPosDiff = long.MinValue; // includes zero and negatives

        foreach (int val in nums) {
            baseSum += val;
            long xorVal = (long)(val ^ k);
            long diff = xorVal - val;
            if (diff > 0) {
                posCount++;
                sumPosDiff += diff;
                if (diff < minPosDiff) minPosDiff = diff;
            } else {
                if (diff > maxNonPosDiff) maxNonPosDiff = diff;
            }
        }

        long gain = sumPosDiff;
        if ((posCount & 1) == 1) { // odd number of positive diffs
            long optionDropSmallestPos = sumPosDiff - minPosDiff;
            long optionAddBestNonPos = sumPosDiff + maxNonPosDiff; // may be negative
            gain = Math.Max(optionDropSmallestPos, optionAddBestNonPos);
        }

        return baseSum + gain;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} edges
 * @return {number}
 */
var maximumValueSum = function(nums, k, edges) {
    let baseSum = 0;
    let posCount = 0;
    let posSum = 0;
    let minPosDiff = Infinity;      // smallest positive diff
    let maxNonPosDiff = -Infinity;  // largest diff that is <= 0

    for (let i = 0; i < nums.length; ++i) {
        const a = nums[i];
        const b = a ^ k;
        const diff = b - a;

        baseSum += a;

        if (diff > 0) {
            posCount++;
            posSum += diff;
            if (diff < minPosDiff) minPosDiff = diff;
        } else {
            if (diff > maxNonPosDiff) maxNonPosDiff = diff;
        }
    }

    if (posCount % 2 === 0) {
        return baseSum + posSum;
    }

    // Need to make the selected set size even
    const optionRemoveOnePositive = baseSum + posSum - minPosDiff;
    let optionAddNonPositive = -Infinity;
    if (maxNonPosDiff !== -Infinity) {
        optionAddNonPositive = baseSum + posSum + maxNonPosDiff;
    }

    return Math.max(optionRemoveOnePositive, optionAddNonPositive);
};
```

## Typescript

```typescript
function maximumValueSum(nums: number[], k: number, edges: number[][]): number {
    let baseSum = 0;
    const positiveDeltas: number[] = [];
    let minPosDelta = Infinity;
    let maxNonPosDelta = -Infinity; // largest delta that is <= 0

    for (let i = 0; i < nums.length; ++i) {
        const val = nums[i];
        baseSum += val;
        const xorVal = val ^ k;
        const delta = xorVal - val;

        if (delta > 0) {
            positiveDeltas.push(delta);
            if (delta < minPosDelta) minPosDelta = delta;
        } else {
            if (delta > maxNonPosDelta) maxNonPosDelta = delta;
        }
    }

    const posCount = positiveDeltas.length;
    let sumPos = 0;
    for (const d of positiveDeltas) sumPos += d;

    if (posCount % 2 === 0) {
        return baseSum + sumPos;
    } else {
        // Need even count: either drop the smallest positive delta,
        // or add the best non-positive delta (if it exists).
        const optionDrop = baseSum + sumPos - minPosDelta;
        let best = optionDrop;

        if (maxNonPosDelta !== -Infinity) {
            const optionAdd = baseSum + sumPos + maxNonPosDelta;
            if (optionAdd > best) best = optionAdd;
        }

        return best;
    }
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer[][] $edges
     * @return Integer
     */
    function maximumValueSum($nums, $k, $edges) {
        $base = 0;
        foreach ($nums as $v) {
            $base += $v;
        }
        $posCount = 0;
        $posSum = 0;
        $minPos = PHP_INT_MAX;
        $maxNeg = -PHP_INT_MAX;
        $n = count($nums);
        for ($i = 0; $i < $n; ++$i) {
            $xor = $nums[$i] ^ $k;
            $diff = $xor - $nums[$i];
            if ($diff > 0) {
                $posCount++;
                $posSum += $diff;
                if ($diff < $minPos) {
                    $minPos = $diff;
                }
            } else {
                if ($diff > $maxNeg) {
                    $maxNeg = $diff;
                }
            }
        }
        if ($posCount == 0) {
            return $base;
        }
        if (($posCount & 1) == 0) {
            return $base + $posSum;
        } else {
            $option1 = $base + $posSum - $minPos; // drop smallest positive diff
            $option2 = ($maxNeg > -PHP_INT_MAX / 2) ? $base + $posSum + $maxNeg : PHP_INT_MIN;
            return max($option1, $option2);
        }
    }
}
```

## Swift

```swift
class Solution {
    func maximumValueSum(_ nums: [Int], _ k: Int, _ edges: [[Int]]) -> Int {
        var baseSum = 0
        var positiveSum = 0
        var positiveCount = 0
        var minPositive = Int.max
        var maxNonPositive = Int.min
        
        for num in nums {
            baseSum += num
            let xorVal = num ^ k
            let diff = xorVal - num
            if diff > 0 {
                positiveSum += diff
                positiveCount += 1
                if diff < minPositive { minPositive = diff }
            } else {
                if diff > maxNonPositive { maxNonPositive = diff }
            }
        }
        
        var result = baseSum + positiveSum
        if positiveCount % 2 == 1 {
            // Need to make the count even
            let dropSmallestPos = baseSum + positiveSum - minPositive
            var addBestNonPos = Int.min
            if maxNonPositive != Int.min {
                addBestNonPos = baseSum + positiveSum + maxNonPositive
            }
            result = max(dropSmallestPos, addBestNonPos)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumValueSum(nums: IntArray, k: Int, edges: Array<IntArray>): Long {
        var base = 0L
        var sumPos = 0L
        var posCount = 0
        var minPosDelta = Long.MAX_VALUE
        var maxNegDelta = Long.MIN_VALUE

        for (num in nums) {
            val xorVal = num xor k
            val delta = xorVal.toLong() - num.toLong()
            base += num.toLong()
            if (delta > 0) {
                posCount++
                sumPos += delta
                if (delta < minPosDelta) minPosDelta = delta
            } else {
                if (delta > maxNegDelta) maxNegDelta = delta
            }
        }

        return if (posCount % 2 == 0) {
            base + sumPos
        } else {
            var best = Long.MIN_VALUE
            // Option 1: drop the smallest positive delta
            if (minPosDelta != Long.MAX_VALUE) {
                best = maxOf(best, base + sumPos - minPosDelta)
            }
            // Option 2: add the largest non‑positive delta
            if (maxNegDelta != Long.MIN_VALUE) {
                best = maxOf(best, base + sumPos + maxNegDelta)
            }
            best
        }
    }
}
```

## Dart

```dart
class Solution {
  int maximumValueSum(List<int> nums, int k, List<List<int>> edges) {
    int n = nums.length;
    int total = 0;
    for (int v in nums) total += v;

    int posCount = 0;
    int posMin = 0x7FFFFFFFFFFFFFFF; // large sentinel
    int? negMax; // largest non‑positive diff

    for (int i = 0; i < n; ++i) {
      int diff = (nums[i] ^ k) - nums[i];
      if (diff > 0) {
        total += diff;
        posCount++;
        if (diff < posMin) posMin = diff;
      } else {
        if (negMax == null || diff > negMax) negMax = diff;
      }
    }

    if (posCount % 2 == 0) return total;

    int best = total - posMin; // remove smallest positive gain
    if (negMax != null) {
      int candidate = total + negMax!;
      if (candidate > best) best = candidate;
    }
    return best;
  }
}
```

## Golang

```go
func maximumValueSum(nums []int, k int, edges [][]int) int64 {
    // The tree structure is irrelevant for the solution.
    // We can toggle any even number of nodes (xor with k) to maximize the sum.
    maxInt := ^int64(0) >> 1
    minInt := -maxInt - 1

    var baseSum int64
    var posSum int64
    var posCount int
    minPosDiff := maxInt      // smallest positive diff
    maxNegOrZeroDiff := minInt // largest non-positive diff

    for _, v := range nums {
        val := int64(v)
        baseSum += val
        xorVal := int64(v ^ k)
        diff := xorVal - val
        if diff > 0 {
            posSum += diff
            posCount++
            if diff < minPosDiff {
                minPosDiff = diff
            }
        } else {
            if diff > maxNegOrZeroDiff {
                maxNegOrZeroDiff = diff
            }
        }
    }

    if posCount%2 == 0 {
        return baseSum + posSum
    }

    // Need to make the count of toggled nodes even.
    // Option 1: remove the smallest positive contribution.
    opt1 := baseSum + posSum - minPosDiff
    // Option 2: add the best non-positive contribution (could be zero).
    opt2 := baseSum + posSum + maxNegOrZeroDiff

    if opt1 > opt2 {
        return opt1
    }
    return opt2
}
```

## Ruby

```ruby
def maximum_value_sum(nums, k, edges)
  total = nums.sum
  pos_sum = 0
  count_pos = 0
  min_positive = nil
  max_nonpositive = -Float::INFINITY

  nums.each do |v|
    gain = (v ^ k) - v
    if gain > 0
      pos_sum += gain
      count_pos += 1
      min_positive = gain if min_positive.nil? || gain < min_positive
    else
      max_nonpositive = gain if gain > max_nonpositive
    end
  end

  if count_pos.even?
    total + pos_sum
  else
    option_remove_min = total + pos_sum - (min_positive || 0)
    option_add_max_nonpos = max_nonpositive > -Float::INFINITY ? total + pos_sum + max_nonpositive : -Float::INFINITY
    [option_remove_min, option_add_max_nonpos].max
  end
end
```

## Scala

```scala
object Solution {
  def maximumValueSum(nums: Array[Int], k: Int, edges: Array[Array[Int]]): Long = {
    var total: Long = 0L
    var sumPos: Long = 0L
    var cntPos = 0
    var minPos: Long = Long.MaxValue
    var maxNeg: Long = Long.MinValue

    val n = nums.length
    var i = 0
    while (i < n) {
      val v = nums(i).toLong
      total += v
      val xorVal = (nums(i) ^ k).toLong
      val diff = xorVal - v
      if (diff > 0) {
        sumPos += diff
        cntPos += 1
        if (diff < minPos) minPos = diff
      } else {
        if (diff > maxNeg) maxNeg = diff
      }
      i += 1
    }

    if ((cntPos & 1) == 0) {
      total + sumPos
    } else {
      var ans: Long = Long.MinValue
      ans = math.max(ans, total + sumPos - minPos)
      if (maxNeg != Long.MinValue) {
        ans = math.max(ans, total + sumPos + maxNeg)
      }
      ans
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, _edges: Vec<Vec<i32>>) -> i64 {
        let mut base_sum: i64 = 0;
        let mut sum_pos: i64 = 0;
        let mut cnt_pos: usize = 0;
        let mut min_positive: i64 = i64::MAX;
        let mut max_nonpositive: i64 = i64::MIN;

        for &val in &nums {
            base_sum += val as i64;
            let xor_val = (val as i64) ^ (k as i64);
            let delta = xor_val - val as i64;
            if delta > 0 {
                sum_pos += delta;
                cnt_pos += 1;
                if delta < min_positive {
                    min_positive = delta;
                }
            } else {
                if delta > max_nonpositive {
                    max_nonpositive = delta;
                }
            }
        }

        let extra = if cnt_pos % 2 == 0 {
            sum_pos
        } else {
            // option: remove the smallest positive delta
            let mut best = sum_pos - min_positive;
            // option: add the largest non-positive delta (if exists)
            if max_nonpositive != i64::MIN {
                let alt = sum_pos + max_nonpositive;
                if alt > best {
                    best = alt;
                }
            }
            best
        };

        base_sum + extra
    }
}
```

## Racket

```racket
(define/contract (maximum-value-sum nums k edges)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((base-sum (foldl + 0 nums))
         (neg-inf (- (expt 2 60)))          ; a sufficiently small sentinel
         (init (list 0 0 #f #f)))           ; pos-sum, pos-count, min-pos, max-nonpos
    (define (process num acc)
      (let* ((gain (- (bitwise-xor num k) num))
             (pos-sum (first acc))
             (pos-count (second acc))
             (min-pos (third acc))
             (max-nonpos (fourth acc)))
        (if (> gain 0)
            (list (+ pos-sum gain)
                  (+ pos-count 1)
                  (if (or (not min-pos) (< gain min-pos)) gain min-pos)
                  max-nonpos)
            (list pos-sum
                  pos-count
                  min-pos
                  (if (or (not max-nonpos) (> gain max-nonpos)) gain max-nonpos)))))
    (let* ((final-acc (foldl process init nums))
           (pos-sum (first final-acc))
           (pos-count (second final-acc))
           (min-pos (third final-acc))
           (max-nonpos (fourth final-acc)))
      (if (even? pos-count)
          (+ base-sum pos-sum)
          (let* ((option1 (if min-pos
                              (- (+ base-sum pos-sum) min-pos)
                              neg-inf))
                 (option2 (if max-nonpos
                              (+ (+ base-sum pos-sum) max-nonpos)
                              neg-inf))
                 (best (max option1 option2 base-sum)))
            best)))))
```

## Erlang

```erlang
-spec maximum_value_sum(Nums :: [integer()], K :: integer(), Edges :: [[integer()]]) -> integer().
maximum_value_sum(Nums, K, _Edges) ->
    Base = lists:sum(Nums),
    Inf = 1 bsl 60,
    {SumPos, CountPos, MinPos, MaxNeg} =
        lists:foldl(fun(Num, {Sp, Cp, Mp, Mn}) ->
            Delta = (Num bxor K) - Num,
            if
                Delta > 0 ->
                    NewSp = Sp + Delta,
                    NewCp = Cp + 1,
                    NewMp = erlang:min(Mp, Delta),
                    {NewSp, NewCp, NewMp, Mn};
                true ->
                    NewMn = erlang:max(Mn, Delta),
                    {Sp, Cp, Mp, NewMn}
            end
        end, {0, 0, Inf, -Inf}, Nums),
    case CountPos rem 2 of
        0 -> Base + SumPos;
        1 ->
            Option1 = Base + SumPos - MinPos,
            Option2 = Base + SumPos + MaxNeg,
            erlang:max(Option1, Option2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_value_sum(nums :: [integer], k :: integer, edges :: [[integer]]) :: integer
  def maximum_value_sum(nums, k, _edges) do
    require Bitwise

    base = Enum.sum(nums)

    {total, cnt, pos_min, neg_max} =
      Enum.reduce(nums, {base, 0, nil, nil}, fn num, {tot, c, pmin, nmax} ->
        gain = Bitwise.bxor(num, k) - num

        if gain > 0 do
          new_pmin =
            case pmin do
              nil -> gain
              _ -> if gain < pmin, do: gain, else: pmin
            end

          {tot + gain, c + 1, new_pmin, nmax}
        else
          new_nmax =
            case nmax do
              nil -> gain
              _ -> if gain > nmax, do: gain, else: nmax
            end

          {tot, c, pmin, new_nmax}
        end
      end)

    if rem(cnt, 2) == 0 do
      total
    else
      option1 = total - (pos_min || 0)
      option2 =
        case neg_max do
          nil -> -9_223_372_036_854_775_808
          _ -> total + neg_max
        end

      if option1 > option2, do: option1, else: option2
    end
  end
end
```
