# 3434. Maximum Frequency After Subarray Operation

## Cpp

```cpp
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int n = nums.size();
        int totalK = 0;
        for (int v : nums) if (v == k) ++totalK;
        int bestOverall = 0;
        // values are in [1,50]
        for (int t = 1; t <= 50; ++t) {
            if (t == k) continue;
            int cur = 0, best = 0;
            for (int v : nums) {
                int add = 0;
                if (v == t) add = 1;
                else if (v == k) add = -1;
                cur = max(0, cur + add);
                best = max(best, cur);
            }
            bestOverall = max(bestOverall, best);
        }
        return totalK + bestOverall;
    }
};
```

## Java

```java
class Solution {
    public int maxFrequency(int[] nums, int k) {
        int originalK = 0;
        int[] maxCnt = new int[51];
        int[] cur = new int[51];
        for (int val : nums) {
            if (val == k) {
                originalK++;
                java.util.Arrays.fill(cur, 0);
            } else {
                cur[val]++;
                if (cur[val] > maxCnt[val]) {
                    maxCnt[val] = cur[val];
                }
            }
        }
        int best = 0;
        for (int v = 1; v <= 50; v++) {
            if (v == k) continue;
            if (maxCnt[v] > best) best = maxCnt[v];
        }
        return originalK + best;
    }
}
```

## Python

```python
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_k = 0
        for x in nums:
            if x == k:
                total_k += 1

        # values are within [1,50]
        MAX_VAL = 51
        cur = [0] * MAX_VAL
        best = [0] * MAX_VAL

        for x in nums:
            if x == k:
                # reset current segment counts
                for v in range(1, MAX_VAL):
                    cur[v] = 0
            else:
                cur[x] += 1
                if cur[x] > best[x]:
                    best[x] = cur[x]

        max_extra = 0
        for v in range(1, MAX_VAL):
            if v != k and best[v] > max_extra:
                max_extra = best[v]

        return total_k + max_extra
```

## Python3

```python
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        orig_k = sum(1 for x in nums if x == k)
        ans = orig_k
        # values are limited to 1..50
        for v in range(1, 51):
            if v == k:
                continue
            cur = best = 0
            for num in nums:
                if num == v:
                    cur += 1
                elif num == k:
                    cur -= 1
                # else cur unchanged
                if cur < 0:
                    cur = 0
                if cur > best:
                    best = cur
            if orig_k + best > ans:
                ans = orig_k + best
        return ans
```

## C

```c
int maxFrequency(int* nums, int numsSize, int k) {
    int total_k = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == k) total_k++;
    }
    int bestGain = 0;
    for (int v = 1; v <= 50; ++v) {
        if (v == k) continue;
        int cur = 0, maxHere = 0;
        for (int i = 0; i < numsSize; ++i) {
            int val = 0;
            if (nums[i] == v) val = 1;
            else if (nums[i] == k) val = -1;
            cur += val;
            if (cur < 0) cur = 0;
            if (cur > maxHere) maxHere = cur;
        }
        if (maxHere > bestGain) bestGain = maxHere;
    }
    return total_k + bestGain;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaxFrequency(int[] nums, int k) {
        int totalK = 0;
        foreach (int num in nums) if (num == k) totalK++;

        int bestDelta = 0; // we can always choose empty subarray

        for (int v = 1; v <= 50; v++) {
            if (v == k) continue;

            int current = int.MinValue;
            int bestForV = int.MinValue;

            foreach (int num in nums) {
                int val = 0;
                if (num == v) val = 1;
                else if (num == k) val = -1;

                if (current == int.MinValue)
                    current = val;
                else
                    current = Math.Max(val, current + val);

                bestForV = Math.Max(bestForV, current);
            }

            if (bestForV > bestDelta) bestDelta = bestForV;
        }

        return totalK + Math.Max(0, bestDelta);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxFrequency = function(nums, k) {
    const MAX_VAL = 50;
    const freq = new Array(MAX_VAL + 1).fill(0);
    for (const num of nums) {
        freq[num]++;
    }
    let ans = freq[k];
    let bestOther = 0;
    for (let v = 1; v <= MAX_VAL; v++) {
        if (v !== k && freq[v] > bestOther) {
            bestOther = freq[v];
        }
    }
    return ans + bestOther;
};
```

## Typescript

```typescript
function maxFrequency(nums: number[], k: number): number {
    const MAX_VAL = 50;
    let totalK = 0;
    const globalMax = new Array(MAX_VAL + 1).fill(0);
    let cur = new Array(MAX_VAL + 1).fill(0);

    for (const num of nums) {
        if (num === k) {
            totalK++;
            for (let v = 1; v <= MAX_VAL; v++) {
                if (cur[v] > globalMax[v]) globalMax[v] = cur[v];
                cur[v] = 0;
            }
        } else {
            cur[num]++;
        }
    }

    // process the last block
    for (let v = 1; v <= MAX_VAL; v++) {
        if (cur[v] > globalMax[v]) globalMax[v] = cur[v];
    }

    let bestAdd = 0;
    for (let v = 1; v <= MAX_VAL; v++) {
        if (v === k) continue;
        if (globalMax[v] > bestAdd) bestAdd = globalMax[v];
    }

    return totalK + bestAdd;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxFrequency($nums, $k) {
        $totalK = 0;
        foreach ($nums as $num) {
            if ($num == $k) {
                $totalK++;
            }
        }

        $maxAns = $totalK; // no operation or delta = 0

        for ($v = 1; $v <= 50; $v++) {
            if ($v == $k) continue;

            $cur = 0;
            $best = 0;
            foreach ($nums as $num) {
                if ($num == $v) {
                    $val = 1;
                } elseif ($num == $k) {
                    $val = -1;
                } else {
                    $val = 0;
                }

                $cur += $val;
                if ($cur < 0) $cur = 0;
                if ($cur > $best) $best = $cur;
            }

            $candidate = $totalK + $best;
            if ($candidate > $maxAns) {
                $maxAns = $candidate;
            }
        }

        return $maxAns;
    }
}
```

## Swift

```swift
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int) -> Int {
        var totalK = 0
        for v in nums {
            if v == k { totalK += 1 }
        }
        var bestGain = 0
        for a in 1...50 where a != k {
            var cur = 0
            var maxSum = 0
            for v in nums {
                if v == a {
                    cur += 1
                } else if v == k {
                    cur -= 1
                }
                if cur < 0 { cur = 0 }
                if cur > maxSum { maxSum = cur }
            }
            if maxSum > bestGain { bestGain = maxSum }
        }
        return totalK + bestGain
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFrequency(nums: IntArray, k: Int): Int {
        val n = nums.size
        var totalK = 0
        for (v in nums) if (v == k) totalK++
        var answer = totalK

        // Values are within [1,50] according to constraints
        for (target in 1..50) {
            if (target == k) continue
            var cur = 0
            var best = Int.MIN_VALUE
            for (i in 0 until n) {
                val w = when {
                    nums[i] == target -> 1
                    nums[i] == k -> -1
                    else -> 0
                }
                cur = if (cur > 0) cur + w else w
                if (cur > best) best = cur
            }
            if (best > 0) {
                answer = kotlin.math.max(answer, totalK + best)
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxFrequency(List<int> nums, int k) {
    int n = nums.length;
    int originalK = 0;
    for (int v in nums) {
      if (v == k) originalK++;
    }

    int bestDelta = 0;

    // Values are between 1 and 50 inclusive.
    for (int target = 1; target <= 50; target++) {
      if (target == k) continue;
      int cur = 0;
      int maxSum = 0;
      for (int i = 0; i < n; i++) {
        int w = 0;
        if (nums[i] == target) {
          w = 1;
        } else if (nums[i] == k) {
          w = -1;
        }
        cur = cur > 0 ? cur + w : w;
        if (cur < 0) cur = 0;
        if (cur > maxSum) maxSum = cur;
      }
      if (maxSum > bestDelta) bestDelta = maxSum;
    }

    return originalK + bestDelta;
  }
}
```

## Golang

```go
func maxFrequency(nums []int, k int) int {
    totalK := 0
    for _, v := range nums {
        if v == k {
            totalK++
        }
    }
    ans := totalK
    for target := 1; target <= 50; target++ {
        if target == k {
            continue
        }
        cur, best := 0, 0
        for _, v := range nums {
            if v == target {
                cur++
            } else if v == k {
                cur--
            }
            if cur < 0 {
                cur = 0
            }
            if cur > best {
                best = cur
            }
        }
        if totalK+best > ans {
            ans = totalK + best
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_frequency(nums, k)
  total_k = nums.count(k)
  best_gain = 0
  (1..50).each do |t|
    next if t == k
    cur = 0
    max_sum = 0
    nums.each do |num|
      val = if num == t
        1
      elsif num == k
        -1
      else
        0
      end
      cur = [val, cur + val].max
      max_sum = [max_sum, cur].max
    end
    best_gain = [best_gain, max_sum].max
  end
  total_k + best_gain
end
```

## Scala

```scala
object Solution {
    def maxFrequency(nums: Array[Int], k: Int): Int = {
        var totalK = 0
        for (v <- nums) if (v == k) totalK += 1

        val counts = new Array[Int](51)
        var bestAdd = 0
        var i = 0
        while (i < nums.length) {
            val v = nums(i)
            if (v == k) {
                java.util.Arrays.fill(counts, 0)
            } else {
                counts(v) += 1
                if (counts(v) > bestAdd) bestAdd = counts(v)
            }
            i += 1
        }
        totalK + bestAdd
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32) -> i32 {
        let total_k = nums.iter().filter(|&&x| x == k).count() as i32;
        let mut answer = total_k;
        for v in 1..=50 {
            if v == k { continue; }
            let mut cur = 0i32;
            let mut best = 0i32;
            for &num in nums.iter() {
                let delta = if num == v { 1 } else if num == k { -1 } else { 0 };
                cur = (cur + delta).max(0);
                if cur > best {
                    best = cur;
                }
            }
            answer = answer.max(total_k + best);
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (max-frequency nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((total-k (for/sum ([x nums]) (if (= x k) 1 0)))
         (ans total-k))
    (for ([v (in-range 1 51)])
      (when (not (= v k))
        (let ((cur 0)
              (best 0))
          (for ([x nums])
            (cond
              [(= x v) (set! cur (+ cur 1))]
              [(= x k) (set! cur (- cur 1))]
              [else (void)])
            (when (< cur 0) (set! cur 0))
            (when (> cur best) (set! best cur)))
          (when (> (+ total-k best) ans)
            (set! ans (+ total-k best))))))
    ans))
```

## Erlang

```erlang
-spec max_frequency([integer()], integer()) -> integer().
max_frequency(Nums, K) ->
    TotalK = count_k(Nums, K),
    MaxDelta = max_delta(Nums, K, 1, 0),
    TotalK + MaxDelta.

count_k([], _) -> 0;
count_k([H|T], K) ->
    (if H == K -> 1; true -> 0 end) + count_k(T, K).

max_delta(_Nums, _K, V, Acc) when V > 50 -> Acc;
max_delta(Nums, K, V, Acc) when V =< 50 ->
    case V of
        K -> max_delta(Nums, K, V+1, Acc);
        _ ->
            Best = kadane(Nums, K, V, 0, 0),
            NewAcc = if Best > Acc -> Best; true -> Acc end,
            max_delta(Nums, K, V+1, NewAcc)
    end.

kadane([], _, _, _, Best) -> Best;
kadane([H|T], K, V, Curr, Best) ->
    Weight = case H of
        V -> 1;
        K -> -1;
        _ -> 0
    end,
    NewCurrTmp = Curr + Weight,
    NewCurr = if NewCurrTmp > 0 -> NewCurrTmp; true -> 0 end,
    NewBest = if NewCurr > Best -> NewCurr; true -> Best end,
    kadane(T, K, V, NewCurr, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_frequency(nums :: [integer], k :: integer) :: integer
  def max_frequency(nums, k) do
    {total_k, %{max: extra}} =
      Enum.reduce(nums, {0, %{max: 0, counts: %{}}}, fn num, {tk, acc} ->
        if num == k do
          # reset the current segment counts, keep the best seen so far
          {tk + 1, %{max: acc.max, counts: %{}}}
        else
          cnt = Map.get(acc.counts, num, 0) + 1
          new_counts = Map.put(acc.counts, num, cnt)
          new_max = if cnt > acc.max, do: cnt, else: acc.max
          {tk, %{max: new_max, counts: new_counts}}
        end
      end)

    total_k + extra
  end
end
```
