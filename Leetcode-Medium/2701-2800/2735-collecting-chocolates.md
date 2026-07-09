# 2735. Collecting Chocolates

## Cpp

```cpp
class Solution {
public:
    long long minCost(std::vector<int>& nums, int x) {
        int n = nums.size();
        std::vector<long long> cur(n);
        for (int i = 0; i < n; ++i) cur[i] = nums[i];
        long long ans = LLONG_MAX;
        for (int R = 0; R < n; ++R) {
            long long sum = 0;
            for (int i = 0; i < n; ++i) sum += cur[i];
            long long total = sum + (long long)x * R;
            if (total < ans) ans = total;
            if (R == n - 1) break;
            for (int i = 0; i < n; ++i) {
                int idx = (i - (R + 1)) % n;
                if (idx < 0) idx += n;
                cur[i] = std::min(cur[i], (long long)nums[idx]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minCost(int[] nums, int x) {
        int n = nums.length;
        long best = Long.MAX_VALUE;
        for (int m = 0; m < n; ++m) { // number of rotations performed
            long total = (long) x * m;
            for (int t = 0; t < n; ++t) {
                int curMin = Integer.MAX_VALUE;
                for (int d = 0; d <= m; ++d) {
                    int idx = t - d;
                    if (idx < 0) idx += n;
                    if (nums[idx] < curMin) curMin = nums[idx];
                }
                total += curMin;
            }
            if (total < best) best = total;
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        from collections import deque
        n = len(nums)
        arr = nums + nums  # duplicate for circular handling
        best_total = float('inf')
        for K in range(n):            # number of rotations performed
            w = K + 1                 # window size
            dq = deque()
            sum_min = 0
            for i, val in enumerate(arr):
                while dq and arr[dq[-1]] >= val:
                    dq.pop()
                dq.append(i)
                if dq[0] <= i - w:   # remove indices out of current window
                    dq.popleft()
                if i >= w - 1:
                    # consider windows that end in the second copy (i from n to 2n-1)
                    if n <= i < 2 * n:
                        sum_min += arr[dq[0]]
            total = x * K + sum_min
            if total < best_total:
                best_total = total
        return best_total
```

## Python3

```python
import collections
from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ext = nums + nums  # length 2n for circular handling
        best = float('inf')
        for R in range(n):  # number of rotations performed
            win = R + 1
            dq = collections.deque()
            mins = [0] * (2 * n)
            for i, val in enumerate(ext):
                while dq and ext[dq[-1]] >= val:
                    dq.pop()
                dq.append(i)
                if dq[0] <= i - win:
                    dq.popleft()
                if i >= win - 1:
                    mins[i] = ext[dq[0]]
            total = R * x
            for t in range(n):
                end_idx = t + n  # window ending at original position t
                total += mins[end_idx]
            if total < best:
                best = total
        return best
```

## C

```c
long long minCost(int* nums, int numsSize, int x) {
    long long totalSum = 0;
    for (int i = 0; i < numsSize; ++i) totalSum += nums[i];
    // find minimum value and its first index
    int minIdx = 0;
    int minVal = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < minVal) {
            minVal = nums[i];
            minIdx = i;
        }
    }
    // duplicate array for circular prefix sums
    int n = numsSize;
    long long *pref = (long long*)malloc(sizeof(long long) * (2 * n + 1));
    pref[0] = 0;
    for (int i = 0; i < 2 * n; ++i) {
        pref[i + 1] = pref[i] + nums[i % n];
    }
    long long ans = totalSum; // case with no rotations
    for (int start = 0; start < n; ++start) {
        int offset = (start - minIdx + n) % n;
        for (int len = 1; len <= n; ++len) {
            long long segSum = pref[start + len] - pref[start];
            long long cur = totalSum - segSum
                           + (long long)len * minVal
                           + (long long)x * (offset + len - 1);
            if (cur < ans) ans = cur;
        }
    }
    free(pref);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MinCost(int[] nums, int x) {
        int n = nums.Length;
        long answer = long.MaxValue;
        int[] curMin = new int[n];
        Array.Copy(nums, curMin, n); // O = 0 minima are the original costs

        for (int rotations = 0; rotations < n; rotations++) {
            if (rotations > 0) {
                for (int i = 0; i < n; i++) {
                    int idx = i - rotations;
                    if (idx < 0) idx += n;
                    if (nums[idx] < curMin[i]) {
                        curMin[i] = nums[idx];
                    }
                }
            }

            long total = (long)rotations * x;
            for (int i = 0; i < n; i++) {
                total += curMin[i];
            }
            if (total < answer) answer = total;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minCost = function(nums, x) {
    const n = nums.length;
    // current minimal cost for each type after considering rotations up to current k
    const curMins = nums.slice(); // copy of original costs
    let sumMins = curMins.reduce((a, b) => a + b, 0);
    let answer = sumMins; // case with 0 rotations

    for (let k = 1; k < n; ++k) {
        for (let i = 0; i < n; ++i) {
            const idx = (i - k + n) % n;
            const val = nums[idx];
            if (val < curMins[i]) {
                sumMins -= curMins[i];
                curMins[i] = val;
                sumMins += curMins[i];
            }
        }
        const total = k * x + sumMins;
        if (total < answer) answer = total;
    }

    return answer;
};
```

## Typescript

```typescript
function minCost(nums: number[], x: number): number {
    const n = nums.length;
    const ext = nums.concat(nums); // length 2n
    let answer = Number.MAX_SAFE_INTEGER;

    for (let R = 0; R < n; ++R) {
        const windowSize = R + 1;
        const deque: number[] = []; // store indices, values increasing
        let sum = 0;

        for (let idx = 0; idx < 2 * n; ++idx) {
            // remove out-of-window indices
            while (deque.length && deque[0] <= idx - windowSize) {
                deque.shift();
            }
            // maintain monotonic increasing values
            while (deque.length && ext[deque[deque.length - 1]] >= ext[idx]) {
                deque.pop();
            }
            deque.push(idx);

            // when we have a full window ending at position idx,
            // and this corresponds to original index i = idx - n (0 <= i < n)
            if (idx >= n && idx - n < n) {
                sum += ext[deque[0]];
            }
        }

        const total = x * R + sum;
        if (total < answer) answer = total;
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @return Integer
     */
    function minCost($nums, $x) {
        $n = count($nums);
        // Minimum cost for each type with current allowed rotations (initially 0)
        $minCosts = $nums;
        $sumMin = array_sum($minCosts);
        $ans = $sumMin; // no rotation

        for ($r = 1; $r < $n; $r++) {
            for ($i = 0; $i < $n; $i++) {
                $idx = $i - $r;
                if ($idx < 0) {
                    $idx += $n;
                }
                $val = $nums[$idx];
                if ($val < $minCosts[$i]) {
                    $sumMin -= $minCosts[$i];
                    $minCosts[$i] = $val;
                    $sumMin += $val;
                }
            }
            $total = $sumMin + $x * $r;
            if ($total < $ans) {
                $ans = $total;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ nums: [Int], _ x: Int) -> Int {
        let n = nums.count
        var best = nums               // minimal cost for each type with current K rotations
        var currentSum = best.reduce(0, +)
        var answer = currentSum       // case K = 0 (no operations)

        if n == 1 { return answer }

        for k in 1..<n {
            for t in 0..<n {
                let idx = (t - k + n) % n
                if nums[idx] < best[t] {
                    currentSum -= best[t]
                    best[t] = nums[idx]
                    currentSum += best[t]
                }
            }
            let total = k * x + currentSum
            if total < answer { answer = total }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(nums: IntArray, x: Int): Long {
        val n = nums.size
        var answer = Long.MAX_VALUE
        val totalSize = 2 * n
        for (r in 0 until n) {
            val window = r + 1
            val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
            var sumMin = 0L
            for (i in 0 until totalSize) {
                val curVal = nums[i % n]
                while (!deque.isEmpty() && nums[deque.peekLast() % n] >= curVal) {
                    deque.pollLast()
                }
                deque.addLast(i)
                if (deque.peekFirst() <= i - window) {
                    deque.pollFirst()
                }
                if (i >= n && i < 2 * n) {
                    sumMin += nums[deque.peekFirst() % n].toLong()
                }
            }
            val total = sumMin + x.toLong() * r
            if (total < answer) answer = total
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minCost(List<int> nums, int x) {
    int n = nums.length;
    int best = 1 << 62; // sufficiently large
    for (int k = 0; k < n; k++) {
      int total = k * x;
      for (int t = 0; t < n; t++) {
        int minVal = nums[t];
        for (int s = 1; s <= k; s++) {
          int idx = t - s;
          if (idx < 0) idx += n;
          int val = nums[idx];
          if (val < minVal) minVal = val;
        }
        total += minVal;
      }
      if (total < best) best = total;
    }
    return best;
  }
}
```

## Golang

```go
func minCost(nums []int, x int) int64 {
    n := len(nums)
    // minVals[t] stores the minimal cost to collect type t using rotations up to current k
    minVals := make([]int, n)
    copy(minVals, nums)

    var sum int64
    for _, v := range minVals {
        sum += int64(v)
    }

    best := sum // case with 0 rotations

    for k := 1; k < n; k++ {
        for t := 0; t < n; t++ {
            idx := t - k
            if idx < 0 {
                idx += n
            }
            v := nums[idx]
            if v < minVals[t] {
                sum -= int64(minVals[t])
                minVals[t] = v
                sum += int64(v)
            }
        }
        total := sum + int64(k)*int64(x)
        if total < best {
            best = total
        }
    }

    return best
}
```

## Ruby

```ruby
def min_cost(nums, x)
  n = nums.length
  mins = nums.clone
  sum_mins = mins.sum
  best = sum_mins

  (1...n).each do |r|
    n.times do |j|
      idx = (j - r) % n
      val = nums[idx]
      if val < mins[j]
        sum_mins -= (mins[j] - val)
        mins[j] = val
      end
    end
    total = sum_mins + r * x
    best = total if total < best
  end

  best
end
```

## Scala

```scala
object Solution {
    def minCost(nums: Array[Int], x: Int): Long = {
        val n = nums.length
        var answer = Long.MaxValue
        for (k <- 0 until n) {
            var sum = 0L
            for (t <- 0 until n) {
                var mn = Long.MaxValue
                var step = 0
                while (step <= k) {
                    val idxRaw = t - step
                    val idx = if (idxRaw >= 0) idxRaw % n else ((idxRaw % n) + n) % n
                    val v = nums(idx).toLong
                    if (v < mn) mn = v
                    step += 1
                }
                sum += mn
            }
            val total = sum + x.toLong * k
            if (total < answer) answer = total
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(nums: Vec<i32>, x: i32) -> i64 {
        let n = nums.len();
        let mut cur_min: Vec<i64> = nums.iter().map(|&v| v as i64).collect();
        let mut total_sum: i64 = cur_min.iter().sum();
        let mut ans = total_sum; // M = 0
        let x_i64 = x as i64;
        for m in 1..n {
            for i in 0..n {
                let idx = (i + n - m) % n;
                let val = nums[idx] as i64;
                if val < cur_min[i] {
                    total_sum -= cur_min[i];
                    cur_min[i] = val;
                    total_sum += cur_min[i];
                }
            }
            let cost = (m as i64) * x_i64 + total_sum;
            if cost < ans {
                ans = cost;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-cost nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums))
         (sums (make-vector n 0)))
    ;; compute sums[k] = sum over i of min in window size k+1 ending at i
    (for ([i (in-range n)])
      (let ((cur-min (vector-ref v i)))
        ;; k = 0
        (vector-set! sums 0 (+ (vector-ref sums 0) cur-min))
        (let loop ((k 1) (cmin cur-min))
          (when (< k n)
            (define idx (modulo (- i k) n))
            (define val (vector-ref v idx))
            (define new-min (if (< val cmin) val cmin))
            (vector-set! sums k (+ (vector-ref sums k) new-min))
            (loop (+ k 1) new-min)))))
    ;; find minimal total cost
    (let ((ans (+ (vector-ref sums 0) (* x 0))))
      (for ([k (in-range n)])
        (define total (+ (vector-ref sums k) (* x k)))
        (when (< total ans) (set! ans total)))
      ans)))
```

## Erlang

```erlang
-spec min_cost(Nums :: [integer()], X :: integer()) -> integer().
min_cost(Nums, X) ->
    Sum = lists:sum(Nums),
    MinVal = lists:min(Nums),
    N = length(Nums),
    Strategy2 = N * MinVal + (N - 1) * X,
    if
        Sum < Strategy2 -> Sum;
        true -> Strategy2
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(nums :: [integer], x :: integer) :: integer
  def min_cost(nums, x) do
    n = length(nums)
    arr = List.to_tuple(nums)

    # initial minima are the numbers themselves
    cur_mins = Tuple.to_list(arr)
    total = Enum.sum(cur_mins)
    ans = total

    # try all possible numbers of rotations R = 1 .. n-1
    for r <- 1..(n - 1) do
      {new_mins_rev, new_total} =
        Enum.reduce(Enum.with_index(cur_mins), {[], total}, fn {min_val, i},
                                                               {list_acc, acc_total} ->
          idx = rem(i - r + n, n)
          val = elem(arr, idx)

          if val < min_val do
            {[val | list_acc], acc_total - min_val + val}
          else
            {[min_val | list_acc], acc_total}
          end
        end)

      cur_mins = Enum.reverse(new_mins_rev)
      total = new_total
      cost = total + r * x
      ans = if cost < ans, do: cost, else: ans
    end

    ans
  end
end
```
