# 1802. Maximum Value at a Given Index in a Bounded Array

## Cpp

```cpp
class Solution {
public:
    long long sideSum(long long len, long long peak) {
        if (peak >= len) {
            long long first = peak - len + 1;
            return (peak + first) * len / 2;
        } else {
            long long seqSum = (peak + 1) * peak / 2; // sum 1..peak
            long long ones = len - peak;
            return seqSum + ones;
        }
    }

    bool can(int n, int index, long long maxSum, long long val) {
        long long leftLen = index + 1LL;
        long long rightLen = (long long)n - index;
        long long total = sideSum(leftLen, val) + sideSum(rightLen, val) - val;
        return total <= maxSum;
    }

    int maxValue(int n, int index, int maxSum) {
        long long low = 1, high = maxSum;
        while (low < high) {
            long long mid = (low + high + 1) >> 1;
            if (can(n, index, maxSum, mid))
                low = mid;
            else
                high = mid - 1;
        }
        return (int)low;
    }
};
```

## Java

```java
class Solution {
    public int maxValue(int n, int index, int maxSum) {
        long low = 1;
        long high = maxSum;
        while (low < high) {
            long mid = (low + high + 1) / 2;
            if (canAchieve(mid, n, index, maxSum)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return (int) low;
    }

    private boolean canAchieve(long value, int n, int index, int maxSum) {
        long leftLen = index;
        long rightLen = n - index - 1L;
        long total = calc(leftLen, value) + calc(rightLen, value) + value;
        return total <= (long) maxSum;
    }

    private long calc(long len, long val) {
        if (len == 0) return 0;
        if (len < val) {
            long first = val - 1;
            long last = val - len;
            return (first + last) * len / 2;
        } else {
            long sumDecreasing = val * (val - 1) / 2;
            long extraOnes = len - (val - 1);
            return sumDecreasing + extraOnes;
        }
    }
}
```

## Python

```python
class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def side_sum(length, peak):
            if length == 0:
                return 0
            if peak > length:
                # decreasing sequence without hitting 1
                first = peak - 1
                last = peak - length
                return (first + last) * length // 2
            else:
                # reach 1 and fill the rest with ones
                dec_len = peak - 1  # number of terms >0 before reaching 1
                dec_sum = dec_len * (dec_len + 1) // 2  # sum 1..dec_len
                ones = length - dec_len
                return dec_sum + ones

        left_len = index          # elements to the left of index
        right_len = n - index - 1 # elements to the right of index

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            total = side_sum(left_len, mid) + side_sum(right_len, mid) + mid
            if total <= maxSum:
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## Python3

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left_len = index
        right_len = n - index - 1

        def min_sum(val: int) -> int:
            # sum on the left side
            if val > left_len:
                left_sum = (val - 1 + val - left_len) * left_len // 2
            else:
                left_sum = val * (val - 1) // 2 + (left_len - val + 1)

            # sum on the right side
            if val > right_len:
                right_sum = (val - 1 + val - right_len) * right_len // 2
            else:
                right_sum = val * (val - 1) // 2 + (right_len - val + 1)

            return left_sum + right_sum + val

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if min_sum(mid) <= maxSum:
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stddef.h>

static long long side_sum(long long len, long long val) {
    if (len == 0) return 0;
    if (val > len) {
        // decreasing sequence without reaching 1
        long long first = val - 1;
        long long last  = val - len;
        return (first + last) * len / 2;
    } else {
        // reaches 1, then fill remaining with 1s
        long long cnt = val - 1;                 // numbers >0 before hitting 1
        long long sum = cnt * (cnt + 1) / 2;      // sum of 1..cnt
        sum += (len - cnt);                       // the rest are all 1s
        return sum;
    }
}

int maxValue(int n, int index, int maxSum) {
    long long N = n, idx = index, limit = maxSum;
    long long low = 1, high = limit;

    while (low < high) {
        long long mid = (low + high + 1) / 2;   // try larger value
        long long left_len  = idx;
        long long right_len = N - idx - 1;

        long long total = side_sum(left_len, mid) +
                          side_sum(right_len, mid) + mid;

        if (total <= limit)
            low = mid;
        else
            high = mid - 1;
    }
    return (int)low;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxValue(int n, int index, int maxSum)
    {
        long low = 1;
        long high = maxSum;

        while (low < high)
        {
            long mid = (low + high + 1) >> 1; // upper middle
            if (CanAchieve(mid, n, index, maxSum))
                low = mid;
            else
                high = mid - 1;
        }

        return (int)low;
    }

    private bool CanAchieve(long value, int n, int index, int maxSum)
    {
        long leftLen = index;
        long rightLen = n - index - 1;

        long sum = value + SumSide(value - 1, leftLen) + SumSide(value - 1, rightLen);
        return sum <= maxSum;
    }

    // Computes minimal sum of a side given the highest starting number (value-1)
    private long SumSide(long start, long length)
    {
        if (length == 0) return 0;

        if (start >= length)
        {
            // arithmetic sequence from start down to start - length + 1
            long first = start;
            long last = start - length + 1;
            return (first + last) * length / 2;
        }
        else
        {
            // descending to 1, then fill remaining with 1s
            long sumDesc = start * (start + 1) / 2; // sum of 1..start
            long ones = length - start;
            return sumDesc + ones;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} index
 * @param {number} maxSum
 * @return {number}
 */
var maxValue = function(n, index, maxSum) {
    const leftLen = index;
    const rightLen = n - index - 1;

    // compute minimal total sum when nums[index] = val
    const getTotal = (val) => {
        const sideSum = (len, v) => {
            if (v > len) {
                // decreasing sequence without hitting 1
                const first = v - 1;
                const last = v - len;
                return ((first + last) * len) / 2;
            } else {
                // reaches 1 and the rest are ones
                const sumDesc = (v * (v - 1)) / 2; // sum of 1..(v-1)
                const ones = len - (v - 1);
                return sumDesc + ones;
            }
        };
        return sideSum(leftLen, val) + sideSum(rightLen, val) + val;
    };

    let low = 1, high = maxSum;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (getTotal(mid) <= maxSum) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maxValue(n: number, index: number, maxSum: number): number {
    const maxSumBig = BigInt(maxSum);
    function side(len: number, peak: number): bigint {
        if (len === 0) return 0n;
        const lenBig = BigInt(len);
        const peakBig = BigInt(peak);
        if (peak > len) {
            const first = peakBig - 1n;
            const last = peakBig - lenBig;
            return (first + last) * lenBig / 2n;
        } else {
            const decreasingSum = (peakBig - 1n) * peakBig / 2n;
            const extraOnes = BigInt(len - (peak - 1));
            return decreasingSum + extraOnes;
        }
    }
    function can(peak: number): boolean {
        const leftLen = index;
        const rightLen = n - index - 1;
        const total = side(leftLen, peak) + side(rightLen, peak) + BigInt(peak);
        return total <= maxSumBig;
    }
    let low = 1, high = maxSum;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $index
     * @param Integer $maxSum
     * @return Integer
     */
    function maxValue($n, $index, $maxSum) {
        $low = 1;
        $high = $maxSum;
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canFit($n, $index, $maxSum, $mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }

    private function canFit($n, $index, $maxSum, $value) {
        $leftLen = $index;
        $rightLen = $n - $index - 1;

        $leftSum = $this->sideSum($leftLen, $value);
        $rightSum = $this->sideSum($rightLen, $value);

        $total = $leftSum + $rightSum + $value;
        return $total <= $maxSum;
    }

    private function sideSum($len, $value) {
        if ($len == 0) {
            return 0;
        }
        $peak = $value - 1; // maximum decreasing value we can place next to the peak
        if ($len <= $peak) {
            // arithmetic series from (value-1) down to (value-len)
            $first = $value - 1;
            $last = $value - $len;
            return intdiv(($first + $last) * $len, 2);
        } else {
            // we can go down to 1, then the rest are all 1s
            $sumDec = intdiv($value * $peak, 2); // sum of values from (value-1) down to 1
            $remaining = $len - $peak;
            return $sumDec + $remaining;
        }
    }
}
```

## Swift

```swift
class Solution {
    func maxValue(_ n: Int, _ index: Int, _ maxSum: Int) -> Int {
        let n64 = Int64(n)
        let idx64 = Int64(index)
        let maxSum64 = Int64(maxSum)

        func sideSum(_ length: Int64, _ peak: Int64) -> Int64 {
            if length == 0 { return 0 }
            if peak > length {
                // decreasing sequence without hitting 1
                let first = peak - 1
                let last = peak - length
                return (first + last) * length / 2
            } else {
                // reaches 1, then fill with ones
                let descCount = peak - 1          // number of terms before reaching 1
                let sumDesc = descCount * peak / 2   // sum 1..peak-1
                let ones = length - descCount
                return sumDesc + ones
            }
        }

        func totalSum(for value: Int64) -> Int64 {
            let leftLen = idx64
            let rightLen = n64 - idx64 - 1
            let left = sideSum(leftLen, value)
            let right = sideSum(rightLen, value)
            return left + right + value
        }

        var low: Int64 = 1
        var high: Int64 = maxSum64

        while low < high {
            let mid = (low + high + 1) / 2
            if totalSum(for: mid) <= maxSum64 {
                low = mid
            } else {
                high = mid - 1
            }
        }

        return Int(low)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxValue(n: Int, index: Int, maxSum: Int): Int {
        val leftLen = index.toLong()
        val rightLen = (n - index - 1).toLong()
        var low = 1L
        var high = maxSum.toLong()
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (calc(mid, leftLen, rightLen) <= maxSum.toLong()) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low.toInt()
    }

    private fun calc(value: Long, leftLen: Long, rightLen: Long): Long {
        val leftSum = sideSum(leftLen, value)
        val rightSum = sideSum(rightLen, value)
        return leftSum + rightSum + value
    }

    private fun sideSum(len: Long, peak: Long): Long {
        if (len == 0L) return 0L
        return if (peak > len) {
            // decreasing sequence without hitting 1
            val first = peak - 1
            val last = peak - len
            (first + last) * len / 2
        } else {
            // hits 1, then the rest are ones
            val decLen = peak - 1
            val sumDec = peak * decLen / 2
            val ones = len - decLen
            sumDec + ones
        }
    }
}
```

## Dart

```dart
class Solution {
  int maxValue(int n, int index, int maxSum) {
    int left = 1;
    int right = maxSum;
    while (left < right) {
      int mid = ((left + right + 1) >> 1);
      if (_can(mid, n, index, maxSum)) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    return left;
  }

  bool _can(int value, int n, int index, int maxSum) {
    int leftCount = index;
    int rightCount = n - index - 1;

    int leftSum = _sideSum(value, leftCount);
    int rightSum = _sideSum(value, rightCount);

    int total = leftSum + rightSum + value;
    return total <= maxSum;
  }

  int _sideSum(int peak, int count) {
    if (count == 0) return 0;
    if (peak > count) {
      // descending sequence without hitting 1
      int last = peak - count; // >= 1
      // sum of arithmetic series from peak-1 down to last
      return ((peak - 1 + last) * count) ~/ 2;
    } else {
      // reach 1 and fill remaining positions with 1s
      int sumDesc = (peak * (peak - 1)) ~/ 2; // sum of 1..(peak-1)
      int extraOnes = count - (peak - 1);
      return sumDesc + extraOnes;
    }
  }
}
```

## Golang

```go
func maxValue(n int, index int, maxSum int) int {
	n64 := int64(n)
	idx64 := int64(index)
	maxSum64 := int64(maxSum)

	calcSide := func(lenSide, val int64) int64 {
		if lenSide == 0 {
			return 0
		}
		if val > lenSide {
			first := val - 1
			last := val - lenSide
			return (first + last) * lenSide / 2
		}
		sumSeq := val * (val - 1) / 2
		rest := lenSide - (val - 1)
		return sumSeq + rest
	}

	possible := func(val int64) bool {
		left := calcSide(idx64, val)
		right := calcSide(n64-idx64-1, val)
		total := left + right + val
		return total <= maxSum64
	}

	low, high := int64(1), maxSum64
	for low < high {
		mid := (low + high + 1) / 2
		if possible(mid) {
			low = mid
		} else {
			high = mid - 1
		}
	}
	return int(low)
}
```

## Ruby

```ruby
def max_value(n, index, max_sum)
  left_len = index
  right_len = n - index - 1

  calc_side = lambda do |len, peak|
    return 0 if len == 0
    if peak > len
      first = peak - 1
      last = peak - len
      (first + last) * len / 2
    else
      descending_len = peak - 1
      sum_desc = descending_len * peak / 2
      ones = len - descending_len
      sum_desc + ones
    end
  end

  low = 1
  high = max_sum

  while low < high
    mid = (low + high + 1) / 2
    total = calc_side.call(left_len, mid) + calc_side.call(right_len, mid) + mid
    if total <= max_sum
      low = mid
    else
      high = mid - 1
    end
  end

  low
end
```

## Scala

```scala
object Solution {
  def maxValue(n: Int, index: Int, maxSum: Int): Int = {
    val nLong = n.toLong
    val idxLong = index.toLong

    def sideSum(len: Long, peak: Long): Long = {
      if (len == 0) return 0L
      if (peak >= len) {
        // descending sequence without hitting 1
        val first = peak
        val last = peak - len + 1
        (first + last) * len / 2
      } else {
        // descend to 1, then fill with ones
        val sumDesc = (peak + 1) * peak / 2 // sum of 1..peak
        val ones = len - peak
        sumDesc + ones
      }
    }

    def totalSum(v: Long): Long = {
      val leftLen = idxLong
      val rightLen = nLong - idxLong - 1
      val left = sideSum(leftLen, v - 1)
      val right = sideSum(rightLen, v - 1)
      left + right + v
    }

    var lo: Long = 1L
    var hi: Long = maxSum.toLong

    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (totalSum(mid) <= maxSum) lo = mid else hi = mid - 1
    }
    lo.toInt
  }
}
```

## Rust

```rust
use std::cmp;

impl Solution {
    pub fn max_value(n: i32, index: i32, max_sum: i32) -> i32 {
        let n = n as i64;
        let idx = index as i64;
        let max_sum = max_sum as i64;

        // minimal sum contributed by one side (excluding the peak itself)
        fn side_sum(len: i64, peak: i64) -> i64 {
            if len == 0 {
                return 0;
            }
            if peak > len {
                // decreasing sequence without hitting 1
                let first = peak - 1;
                let last = peak - len;
                (first + last) * len / 2
            } else {
                // reaches 1, then the rest are all 1's
                let sum_to_one = (peak - 1) * peak / 2; // 1 + ... + (peak-1)
                let ones = len - (peak - 1);
                sum_to_one + ones
            }
        }

        let mut low: i64 = 1;
        let mut high: i64 = max_sum;

        while low < high {
            let mid = (low + high + 1) / 2;
            let left_len = idx;
            let right_len = n - idx - 1;
            let total = side_sum(left_len, mid) + side_sum(right_len, mid) + mid;
            if total <= max_sum {
                low = mid;
            } else {
                high = mid - 1;
            }
        }

        low as i32
    }
}
```

## Racket

```racket
(define/contract (max-value n index maxSum)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (letrec ([calc
            (lambda (len peak)
              (if (>= peak len)
                  (let* ([first (- peak (- len 1))]
                         [sum   (quotient (* (+ peak first) len) 2)])
                    sum)
                  (let* ([sum1 (quotient (* (+ peak 1) peak) 2)]
                         [sum2 (- len peak)])
                    (+ sum1 sum2))))]
           [feasible?
            (lambda (peak)
              (let* ([leftLen  (+ index 1)]
                     [rightLen (- n index)]
                     [leftSum  (calc leftLen peak)]
                     [rightSum (calc rightLen peak)]
                     [total    (- (+ leftSum rightSum) peak)])
                (<= total maxSum)))])
    (let loop ([lo 1] [hi maxSum])
      (if (= lo hi)
          lo
          (let* ([mid (quotient (+ lo hi 1) 2)])
            (if (feasible? mid)
                (loop mid hi)
                (loop lo (- mid 1))))))))
```

## Erlang

```erlang
-spec max_value(N :: integer(), Index :: integer(), MaxSum :: integer()) -> integer().
max_value(N, Index, MaxSum) ->
    binary_search(1, MaxSum, N, Index, MaxSum).

binary_search(Low, High, N, Index, MaxSum) when Low < High ->
    Mid = (Low + High + 1) div 2,
    case total_sum(N, Index, Mid) =< MaxSum of
        true -> binary_search(Mid, High, N, Index, MaxSum);
        false -> binary_search(Low, Mid - 1, N, Index, MaxSum)
    end;
binary_search(Low, _High, _N, _Index, _MaxSum) ->
    Low.

total_sum(N, Index, V) ->
    LeftLen = Index,
    RightLen = N - Index - 1,
    SumLeft = side_sum(LeftLen, V),
    SumRight = side_sum(RightLen, V),
    SumLeft + SumRight + V.

side_sum(0, _V) -> 0;
side_sum(Len, V) ->
    if
        V > Len ->
            First = V - 1,
            Last = V - Len,
            (First + Last) * Len div 2;
        true ->
            Full = V - 1,
            SumFull = V * (V - 1) div 2,
            Extra = Len - Full,
            SumFull + Extra
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_value(n :: integer, index :: integer, max_sum :: integer) :: integer
  def max_value(n, index, max_sum) do
    binary_search(1, max_sum, n, index, max_sum)
  end

  defp binary_search(low, high, _n, _index, _max_sum) when low == high, do: low

  defp binary_search(low, high, n, index, max_sum) do
    mid = div(low + high + 1, 2)

    if total_sum(n, index, mid) <= max_sum do
      binary_search(mid, high, n, index, max_sum)
    else
      binary_search(low, mid - 1, n, index, max_sum)
    end
  end

  defp total_sum(n, index, value) do
    left_len = index
    right_len = n - index - 1

    left_sum = side_sum(left_len, value)
    right_sum = side_sum(right_len, value)

    left_sum + right_sum + value
  end

  defp side_sum(0, _v), do: 0

  defp side_sum(len, v) when v > len do
    a = v - 1
    b = v - len
    (a + b) * len |> div(2)
  end

  defp side_sum(len, v) do
    sum_desc = v * (v - 1) |> div(2)
    rest = len - v + 1
    sum_desc + rest
  end
end
```
