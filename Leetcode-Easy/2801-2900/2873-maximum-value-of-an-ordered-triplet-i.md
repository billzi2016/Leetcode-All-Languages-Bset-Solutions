# 2873. Maximum Value of an Ordered Triplet I

## Cpp

```cpp
class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        int imax = nums[0];
        int dmax = INT_MIN;
        for (int k = 2; k < n; ++k) {
            int j = k - 1;
            dmax = max(dmax, imax - nums[j]);
            ans = max(ans, (long long)dmax * nums[k]);
            imax = max(imax, nums[j]);
        }
        return ans > 0 ? ans : 0;
    }
};
```

## Java

```java
class Solution {
    public long maximumTripletValue(int[] nums) {
        int n = nums.length;
        long answer = 0L;
        int maxLeft = nums[0];
        long bestDiff = Long.MIN_VALUE;
        for (int k = 2; k < n; ++k) {
            int j = k - 1;
            long diff = (long) maxLeft - (long) nums[j];
            if (diff > bestDiff) {
                bestDiff = diff;
            }
            if (nums[j] > maxLeft) {
                maxLeft = nums[j];
            }
            long candidate = bestDiff * (long) nums[k];
            if (candidate > answer) {
                answer = candidate;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0

        imax = nums[0]          # max value for i seen so far
        dmax = float('-inf')    # max (nums[i] - nums[j]) for i<j processed so far
        ans = 0

        for idx in range(1, n):
            # current index acts as k; use best difference from earlier positions
            if dmax != float('-inf'):
                candidate = dmax * nums[idx]
                if candidate > ans:
                    ans = candidate

            # now treat current index as j for future ks
            diff = imax - nums[idx]
            if diff > dmax:
                dmax = diff

            # update imax with current element for future i's
            if nums[idx] > imax:
                imax = nums[idx]

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        imax = nums[0]
        dmax = -10**18
        ans = 0
        for i in range(1, n):
            if i >= 2:
                prod = dmax * nums[i]
                if prod > ans:
                    ans = prod
            diff = imax - nums[i]
            if diff > dmax:
                dmax = diff
            if nums[i] > imax:
                imax = nums[i]
        return ans if ans > 0 else 0
```

## C

```c
long long maximumTripletValue(int* nums, int numsSize) {
    if (numsSize < 3) return 0;
    int n = numsSize;
    int leftMax[101];
    int rightMax[101];

    int cur = nums[0];
    for (int i = 1; i < n; ++i) {
        leftMax[i] = cur;               // max in [0, i)
        if (nums[i] > cur) cur = nums[i];
    }

    int curR = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        rightMax[i] = curR;             // max in (i, n)
        if (nums[i] > curR) curR = nums[i];
    }

    long long best = 0;
    for (int j = 1; j <= n - 2; ++j) {
        long long diff = (long long)leftMax[j] - (long long)nums[j];
        long long val = diff * (long long)rightMax[j];
        if (val > best) best = val;
    }
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaximumTripletValue(int[] nums)
    {
        int n = nums.Length;
        long imax = nums[0];
        long dmax = long.MinValue;
        long answer = 0;

        for (int idx = 1; idx < n; ++idx)
        {
            if (idx >= 2 && dmax != long.MinValue)
            {
                long val = dmax * (long)nums[idx];
                if (val > answer)
                    answer = val;
            }

            long diff = imax - (long)nums[idx];
            if (diff > dmax)
                dmax = diff;

            if (nums[idx] > imax)
                imax = nums[idx];
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    const n = nums.length;
    if (n < 3) return 0;
    let maxI = nums[0];          // maximum of nums[i] for i < current j
    let bestDiff = -Infinity;    // maximum (nums[i] - nums[j]) for i < j processed so far
    let ans = 0;
    let j = 1;                   // next index to process as middle element
    
    for (let k = 2; k < n; ++k) {
        while (j <= k - 1) {
            const diff = maxI - nums[j];
            if (diff > bestDiff) bestDiff = diff;
            if (nums[j] > maxI) maxI = nums[j];
            ++j;
        }
        if (bestDiff > 0) {
            const val = bestDiff * nums[k];
            if (val > ans) ans = val;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maximumTripletValue(nums: number[]): number {
    const n = nums.length;
    if (n < 3) return 0;

    // prefix maximums: pref[i] = max of nums[0..i]
    const pref: number[] = new Array(n);
    pref[0] = nums[0];
    for (let i = 1; i < n; ++i) {
        pref[i] = Math.max(pref[i - 1], nums[i]);
    }

    let ans = 0;
    // j is the middle index
    for (let j = 1; j <= n - 2; ++j) {
        const imax = pref[j - 1];          // max nums[i] with i < j
        const diff = imax - nums[j];
        for (let k = j + 1; k < n; ++k) {
            const val = diff * nums[k];
            if (val > ans) ans = val;
        }
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
    function maximumTripletValue($nums) {
        $n = count($nums);
        if ($n < 3) return 0;
        $imax = $nums[0];
        $dmax = PHP_INT_MIN;
        $ans = 0;
        for ($j = 1; $j < $n - 1; ++$j) {
            // update best difference using current i max and nums[j]
            $diff = $imax - $nums[$j];
            if ($diff > $dmax) {
                $dmax = $diff;
            }
            // evaluate all possible k > j
            for ($k = $j + 1; $k < $n; ++$k) {
                $value = $dmax * $nums[$k];
                if ($value > $ans) {
                    $ans = $value;
                }
            }
            // update i max for future iterations
            if ($nums[$j] > $imax) {
                $imax = $nums[$j];
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumTripletValue(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 3 { return 0 }
        var maxI = nums[0]
        var bestDiff = Int.min
        var ans = 0
        for j in 1..<(n - 1) {
            let diff = maxI - nums[j]
            if diff > bestDiff {
                bestDiff = diff
            }
            if bestDiff > 0 {
                for k in (j + 1)..<n {
                    let val = bestDiff * nums[k]
                    if val > ans {
                        ans = val
                    }
                }
            }
            if nums[j] > maxI {
                maxI = nums[j]
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTripletValue(nums: IntArray): Long {
        val n = nums.size
        if (n < 3) return 0L

        val leftMax = IntArray(n)
        var curLeft = nums[0]
        for (i in 1 until n) {
            leftMax[i] = curLeft
            if (nums[i] > curLeft) curLeft = nums[i]
        }

        val rightMax = IntArray(n)
        var curRight = nums[n - 1]
        for (i in n - 2 downTo 0) {
            rightMax[i] = curRight
            if (nums[i] > curRight) curRight = nums[i]
        }

        var ans = 0L
        for (j in 1 until n - 1) {
            val diff = leftMax[j] - nums[j]
            val value = diff.toLong() * rightMax[j].toLong()
            if (value > ans) ans = value
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  int maximumTripletValue(List<int> nums) {
    int n = nums.length;
    int ans = 0;
    int imax = nums[0];
    for (int j = 1; j <= n - 2; ++j) {
      imax = math.max(imax, nums[j - 1]);
      for (int k = j + 1; k < n; ++k) {
        int val = (imax - nums[j]) * nums[k];
        if (val > ans) ans = val;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maximumTripletValue(nums []int) int64 {
    n := len(nums)
    if n < 3 {
        return 0
    }
    leftMax := make([]int, n)
    curLeft := nums[0]
    for i := 1; i < n; i++ {
        leftMax[i] = curLeft
        if nums[i] > curLeft {
            curLeft = nums[i]
        }
    }

    rightMax := make([]int, n)
    curRight := nums[n-1]
    for i := n - 2; i >= 0; i-- {
        rightMax[i] = curRight
        if nums[i] > curRight {
            curRight = nums[i]
        }
    }

    var ans int64 = 0
    for j := 1; j <= n-2; j++ {
        diff := leftMax[j] - nums[j]
        if diff <= 0 {
            continue
        }
        val := int64(diff) * int64(rightMax[j])
        if val > ans {
            ans = val
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_triplet_value(nums)
  n = nums.length
  max_i = nums[0]
  best_diff = -Float::INFINITY
  ans = 0

  (1...n).each do |k|
    if best_diff != -Float::INFINITY
      candidate = best_diff * nums[k]
      ans = candidate if candidate > ans
    end

    diff = max_i - nums[k]
    best_diff = diff if diff > best_diff

    max_i = nums[k] if nums[k] > max_i
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumTripletValue(nums: Array[Int]): Long = {
        val n = nums.length
        if (n < 3) return 0L

        // prefix maximums: leftMax(i) = max of nums[0..i-1]
        val leftMax = new Array[Int](n)
        var curLeft = nums(0)
        for (i <- 1 until n) {
            leftMax(i) = curLeft
            if (nums(i) > curLeft) curLeft = nums(i)
        }

        // suffix maximums: rightMax(i) = max of nums[i+1..n-1]
        val rightMax = new Array[Int](n)
        var curRight = nums(n - 1)
        for (i <- (0 until n - 1).reverse) {
            rightMax(i) = curRight
            if (nums(i) > curRight) curRight = nums(i)
        }

        var ans: Long = 0L
        for (j <- 1 until n - 1) {
            val diff = leftMax(j) - nums(j)
            val value = diff.toLong * rightMax(j).toLong
            if (value > ans) ans = value
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        let mut imax = nums[0] as i64;
        let mut best_diff = i64::MIN;
        let mut ans: i64 = 0;

        for idx in 1..n {
            if idx >= 2 && best_diff != i64::MIN {
                let val = best_diff * nums[idx] as i64;
                if val > ans {
                    ans = val;
                }
            }
            let diff_candidate = imax - nums[idx] as i64;
            if diff_candidate > best_diff {
                best_diff = diff_candidate;
            }
            if (nums[idx] as i64) > imax {
                imax = nums[idx] as i64;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-triplet-value nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (if (< n 3)
        0
        (let ([max-val 0]
              [max-i (vector-ref vec 0)])
          (for ([j (in-range 1 (- n 1))])
            (set! max-i (max max-i (vector-ref vec (sub1 j))))
            (let ([diff (- max-i (vector-ref vec j))])
              (when (> diff 0)
                (for ([k (in-range (add1 j) n)])
                  (let ([val (* diff (vector-ref vec k))])
                    (when (> val max-val)
                      (set! max-val val)))))))
          max-val))))
```

## Erlang

```erlang
-spec maximum_triplet_value([integer()]) -> integer().
maximum_triplet_value(Nums) ->
    case Nums of
        [_|_] = List when length(List) >= 3 ->
            [First | Rest] = List,
            loop(Rest, First, -(1 bsl 60), 0);
        _ -> 0
    end.

loop([], _Imx, _Dmax, Ans) ->
    Ans;
loop([X|Tail], Imx, Dmax, Ans) ->
    Candidate = Dmax * X,
    NewAns = erlang:max(Ans, Candidate),
    Diff = Imx - X,
    NewDmax = erlang:max(Dmax, Diff),
    NewImx = erlang:max(Imx, X),
    loop(Tail, NewImx, NewDmax, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_triplet_value(nums :: [integer]) :: integer
  def maximum_triplet_value(nums) do
    n = length(nums)

    values =
      for i <- 0..(n - 3), j <- (i + 1)..(n - 2) do
        diff = Enum.at(nums, i) - Enum.at(nums, j)

        if diff > 0 do
          max_k = Enum.max(Enum.slice(nums, j + 1, n - (j + 1)))
          diff * max_k
        else
          nil
        end
      end

    case Enum.filter(values, & &1) do
      [] -> 0
      list -> Enum.max(list)
    end
  end
end
```
