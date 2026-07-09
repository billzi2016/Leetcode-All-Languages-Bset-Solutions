# 2786. Visit Array Positions to Maximize Score

## Cpp

```cpp
class Solution {
public:
    long long maxScore(std::vector<int>& nums, int x) {
        const long long INF_NEG = LLONG_MIN / 4;
        long long bestEven = INF_NEG, bestOdd = INF_NEG;
        long long ans = nums[0];
        if (nums[0] % 2 == 0) bestEven = nums[0];
        else bestOdd = nums[0];

        for (size_t i = 1; i < nums.size(); ++i) {
            long long cur;
            if (nums[i] % 2 == 0) { // even
                long long candSame = bestEven;               // no penalty
                long long candDiff = bestOdd - x;             // parity change penalty
                cur = nums[i] + std::max(candSame, candDiff);
                bestEven = std::max(bestEven, cur);
            } else { // odd
                long long candSame = bestOdd;
                long long candDiff = bestEven - x;
                cur = nums[i] + std::max(candSame, candDiff);
                bestOdd = std::max(bestOdd, cur);
            }
            ans = std::max(ans, cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxScore(int[] nums, int x) {
        int n = nums.length;
        final long NEG = Long.MIN_VALUE / 4;
        long bestEven = NEG;
        long bestOdd = NEG;
        long ans = NEG;

        // Initialize with position 0
        long dp0 = nums[0];
        if ((nums[0] & 1) == 0) {
            bestEven = dp0;
        } else {
            bestOdd = dp0;
        }
        ans = dp0;

        for (int i = 1; i < n; ++i) {
            long dp;
            if ((nums[i] & 1) == 0) { // even
                long candSame = bestEven == NEG ? NEG : bestEven + nums[i];
                long candDiff = bestOdd == NEG ? NEG : bestOdd + nums[i] - x;
                dp = Math.max(candSame, candDiff);
                if (dp > bestEven) {
                    bestEven = dp;
                }
            } else { // odd
                long candSame = bestOdd == NEG ? NEG : bestOdd + nums[i];
                long candDiff = bestEven == NEG ? NEG : bestEven + nums[i] - x;
                dp = Math.max(candSame, candDiff);
                if (dp > bestOdd) {
                    bestOdd = dp;
                }
            }
            if (dp > ans) {
                ans = dp;
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        INF_NEG = -10**18
        best_even = INF_NEG
        best_odd = INF_NEG

        # start at position 0
        dp0 = nums[0]
        if nums[0] % 2 == 0:
            best_even = dp0
        else:
            best_odd = dp0

        max_score = dp0

        for i in range(1, len(nums)):
            val = nums[i]
            parity = val & 1  # 0 even, 1 odd

            if parity == 0:  # even
                same = best_even + val if best_even != INF_NEG else INF_NEG
                diff = best_odd + val - x if best_odd != INF_NEG else INF_NEG
            else:  # odd
                same = best_odd + val if best_odd != INF_NEG else INF_NEG
                diff = best_even + val - x if best_even != INF_NEG else INF_NEG

            cur = max(same, diff)
            # update best for this parity
            if parity == 0:
                if cur > best_even:
                    best_even = cur
            else:
                if cur > best_odd:
                    best_odd = cur

            if cur > max_score:
                max_score = cur

        return max_score
```

## Python3

```python
from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        INF_NEG = -10**18
        best_even = INF_NEG
        best_odd = INF_NEG

        # start at position 0
        dp0 = nums[0]
        if nums[0] % 2 == 0:
            best_even = dp0
        else:
            best_odd = dp0

        ans = dp0

        for i in range(1, len(nums)):
            val = nums[i]
            if val % 2 == 0:
                cand_same = best_even + val if best_even != INF_NEG else INF_NEG
                cand_diff = best_odd + val - x if best_odd != INF_NEG else INF_NEG
                dpi = max(cand_same, cand_diff)
                best_even = max(best_even, dpi)
            else:
                cand_same = best_odd + val if best_odd != INF_NEG else INF_NEG
                cand_diff = best_even + val - x if best_even != INF_NEG else INF_NEG
                dpi = max(cand_same, cand_diff)
                best_odd = max(best_odd, dpi)

            ans = max(ans, dpi)

        return ans
```

## C

```c
#include <limits.h>

long long maxScore(int* nums, int numsSize, int x) {
    const long long NEG_INF = -(1LL << 60);
    long long best[2] = {NEG_INF, NEG_INF};
    
    int p0 = nums[0] & 1;
    long long dp0 = (long long)nums[0];
    best[p0] = dp0;
    long long answer = dp0;
    
    for (int i = 1; i < numsSize; ++i) {
        int val = nums[i];
        int p = val & 1;
        
        long long same = best[p];
        long long opp = best[1 - p];
        long long candSame = same;
        long long candOpp = (opp == NEG_INF) ? NEG_INF : opp - x;
        long long prevBest = candSame > candOpp ? candSame : candOpp;
        
        long long dp = (long long)val + prevBest;
        if (dp > answer) answer = dp;
        if (dp > best[p]) best[p] = dp;
    }
    
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxScore(int[] nums, int x) {
        int n = nums.Length;
        const long NEG_INF = long.MinValue / 4; // safe negative sentinel
        long bestEven = NEG_INF, bestOdd = NEG_INF;
        long ans;

        long dp0 = nums[0];
        if ((nums[0] & 1) == 0) {
            bestEven = dp0;
        } else {
            bestOdd = dp0;
        }
        ans = dp0;

        for (int i = 1; i < n; i++) {
            int parity = nums[i] & 1;
            long same = parity == 0 ? bestEven : bestOdd;
            long opp = parity == 0 ? bestOdd : bestEven;

            long candidate = same;
            if (opp != NEG_INF) {
                candidate = Math.Max(candidate, opp - x);
            }

            long dpi = nums[i] + candidate;

            if (parity == 0) {
                bestEven = Math.Max(bestEven, dpi);
            } else {
                bestOdd = Math.Max(bestOdd, dpi);
            }
            ans = Math.Max(ans, dpi);
        }

        return ans;
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
var maxScore = function(nums, x) {
    const n = nums.length;
    // best[0] for even parity, best[1] for odd parity
    const best = [Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY];
    const firstParity = nums[0] & 1;
    best[firstParity] = nums[0];
    let answer = nums[0];

    for (let i = 1; i < n; ++i) {
        const p = nums[i] & 1; // current parity
        const same = best[p];
        const opp = best[1 - p];
        const cur = nums[i] + Math.max(same, opp - x);
        if (cur > answer) answer = cur;
        if (cur > best[p]) best[p] = cur;
    }
    return answer;
};
```

## Typescript

```typescript
function maxScore(nums: number[], x: number): number {
    const n = nums.length;
    let bestEven = Number.NEGATIVE_INFINITY;
    let bestOdd = Number.NEGATIVE_INFINITY;
    let answer = Number.NEGATIVE_INFINITY;

    // Initialize with the first position
    const firstVal = nums[0];
    if (firstVal % 2 === 0) {
        bestEven = firstVal;
    } else {
        bestOdd = firstVal;
    }
    answer = firstVal;

    for (let i = 1; i < n; i++) {
        const val = nums[i];
        let dp: number;
        if (val % 2 === 0) {
            const sameParity = bestEven;
            const diffParity = bestOdd - x;
            dp = val + Math.max(sameParity, diffParity);
            if (dp > bestEven) bestEven = dp;
        } else {
            const sameParity = bestOdd;
            const diffParity = bestEven - x;
            dp = val + Math.max(sameParity, diffParity);
            if (dp > bestOdd) bestOdd = dp;
        }
        if (dp > answer) answer = dp;
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
    function maxScore($nums, $x) {
        $n = count($nums);
        // Initialize best scores for even and odd parity positions.
        $negInf = -PHP_INT_MAX;
        $bestEven = $negInf;
        $bestOdd  = $negInf;

        // Starting position
        $dp = $nums[0];
        if ($nums[0] % 2 == 0) {
            $bestEven = $dp;
        } else {
            $bestOdd = $dp;
        }
        $ans = $dp;

        for ($i = 1; $i < $n; ++$i) {
            $val = $nums[$i];
            if ($val % 2 == 0) { // even
                $same = $bestEven;
                $opp  = $bestOdd - $x;
                $maxPrev = max($same, $opp);
            } else { // odd
                $same = $bestOdd;
                $opp  = $bestEven - $x;
                $maxPrev = max($same, $opp);
            }
            $dp = $val + $maxPrev;

            if ($val % 2 == 0) {
                if ($dp > $bestEven) $bestEven = $dp;
            } else {
                if ($dp > $bestOdd) $bestOdd = $dp;
            }

            if ($dp > $ans) $ans = $dp;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ nums: [Int], _ x: Int) -> Int {
        var bestEven = Int.min / 2
        var bestOdd = Int.min / 2
        var answer = Int.min
        
        for i in 0..<nums.count {
            let val = nums[i]
            var dp: Int
            if i == 0 {
                dp = val
            } else {
                if val % 2 == 0 {
                    let sameParity = bestEven + val
                    let diffParity = bestOdd + val - x
                    dp = max(sameParity, diffParity)
                } else {
                    let sameParity = bestOdd + val
                    let diffParity = bestEven + val - x
                    dp = max(sameParity, diffParity)
                }
            }
            
            if val % 2 == 0 {
                if dp > bestEven { bestEven = dp }
            } else {
                if dp > bestOdd { bestOdd = dp }
            }
            if dp > answer { answer = dp }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(nums: IntArray, x: Int): Long {
        val n = nums.size
        val xl = x.toLong()
        var bestEven = Long.MIN_VALUE / 4
        var bestOdd = Long.MIN_VALUE / 4

        // dp for index 0
        var dp0 = nums[0].toLong()
        if ((nums[0] and 1) == 0) {
            bestEven = dp0
        } else {
            bestOdd = dp0
        }
        var answer = dp0

        for (i in 1 until n) {
            val curVal = nums[i].toLong()
            val isEven = (nums[i] and 1) == 0
            val bestPrev = if (isEven) {
                maxOf(bestEven, bestOdd - xl)
            } else {
                maxOf(bestOdd, bestEven - xl)
            }
            val dpi = curVal + bestPrev
            answer = maxOf(answer, dpi)

            if (isEven) {
                if (dpi > bestEven) bestEven = dpi
            } else {
                if (dpi > bestOdd) bestOdd = dpi
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(List<int> nums, int x) {
    const int NEG_INF = -0x7FFFFFFFFFFFFFFF; // sufficiently small negative
    int n = nums.length;
    int dp0 = nums[0];
    int maxEven = (nums[0] & 1) == 0 ? dp0 : NEG_INF;
    int maxOdd = (nums[0] & 1) != 0 ? dp0 : NEG_INF;

    for (int i = 1; i < n; ++i) {
      int val = nums[i];
      bool isEven = (val & 1) == 0;
      int same = isEven ? maxEven : maxOdd;
      int opp = isEven ? maxOdd : maxEven;

      int bestPrev = same;
      if (opp != NEG_INF) {
        int cand = opp - x;
        if (cand > bestPrev) bestPrev = cand;
      }

      int dpi = val + bestPrev;
      if (isEven) {
        if (dpi > maxEven) maxEven = dpi;
      } else {
        if (dpi > maxOdd) maxOdd = dpi;
      }
    }

    return maxEven > maxOdd ? maxEven : maxOdd;
  }
}
```

## Golang

```go
func maxScore(nums []int, x int) int64 {
    const INF_NEG = -1 << 60
    bestEven, bestOdd := INF_NEG, INF_NEG

    // initialize with position 0
    dp0 := int64(nums[0])
    if nums[0]%2 == 0 {
        bestEven = dp0
    } else {
        bestOdd = dp0
    }

    for i := 1; i < len(nums); i++ {
        val := int64(nums[i])
        parity := nums[i] & 1

        var same, diff int64
        if parity == 0 {
            same = bestEven
            diff = bestOdd
        } else {
            same = bestOdd
            diff = bestEven
        }

        candidate := same
        if tmp := diff - int64(x); tmp > candidate {
            candidate = tmp
        }
        dp := candidate + val

        if parity == 0 {
            if dp > bestEven {
                bestEven = dp
            }
        } else {
            if dp > bestOdd {
                bestOdd = dp
            }
        }
    }

    if bestEven > bestOdd {
        return bestEven
    }
    return bestOdd
}
```

## Ruby

```ruby
def max_score(nums, x)
  n = nums.length
  dp0 = nums[0]
  neg_inf = -(1 << 60)

  best_even = neg_inf
  best_odd  = neg_inf

  if nums[0].even?
    best_even = dp0
  else
    best_odd = dp0
  end

  max_score = dp0

  (1...n).each do |i|
    val = nums[i]
    if val.even?
      same = best_even
      diff = best_odd
    else
      same = best_odd
      diff = best_even
    end

    cand_same = same + val
    cand_diff = diff + val - x
    dp_i = cand_same > cand_diff ? cand_same : cand_diff

    if val.even?
      best_even = dp_i if dp_i > best_even
    else
      best_odd = dp_i if dp_i > best_odd
    end

    max_score = dp_i if dp_i > max_score
  end

  max_score
end
```

## Scala

```scala
object Solution {
    def maxScore(nums: Array[Int], x: Int): Long = {
        val n = nums.length
        var bestEven: Long = Long.MinValue
        var bestOdd: Long = Long.MinValue

        // Initialize with the first element
        var dp0: Long = nums(0).toLong
        if ((nums(0) & 1) == 0) bestEven = dp0 else bestOdd = dp0
        var ans: Long = dp0

        var i = 1
        while (i < n) {
            val v = nums(i).toLong
            val isEven = (nums(i) & 1) == 0
            var cur: Long = Long.MinValue

            if (isEven) {
                if (bestEven != Long.MinValue) cur = math.max(cur, bestEven + v)
                if (bestOdd != Long.MinValue) cur = math.max(cur, bestOdd + v - x)
            } else {
                if (bestOdd != Long.MinValue) cur = math.max(cur, bestOdd + v)
                if (bestEven != Long.MinValue) cur = math.max(cur, bestEven + v - x)
            }

            // Update the best values for this parity
            if (isEven) {
                if (cur > bestEven) bestEven = cur
            } else {
                if (cur > bestOdd) bestOdd = cur
            }

            if (cur > ans) ans = cur
            i += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(nums: Vec<i32>, x: i32) -> i64 {
        let mut best_even: i64 = i64::MIN / 4;
        let mut best_odd: i64 = i64::MIN / 4;
        let mut ans: i64 = 0;

        // initialize with the first element
        let first = nums[0] as i64;
        if nums[0] % 2 == 0 {
            best_even = first;
        } else {
            best_odd = first;
        }
        ans = first;

        for &v in nums.iter().skip(1) {
            let val = v as i64;
            let parity = (v & 1) as usize; // 0 = even, 1 = odd
            let same = if parity == 0 { best_even } else { best_odd };
            let opp = if parity == 0 { best_odd } else { best_even };

            let mut best_prev = same;
            let cand = opp - x as i64;
            if cand > best_prev {
                best_prev = cand;
            }

            let dp_i = val + best_prev;

            if parity == 0 {
                if dp_i > best_even {
                    best_even = dp_i;
                }
            } else {
                if dp_i > best_odd {
                    best_odd = dp_i;
                }
            }

            if dp_i > ans {
                ans = dp_i;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-score nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)]
         [sentinel (- (expt 2 60))] ; sufficiently small negative number
         [first (vector-ref v 0)]
         [best-even (if (even? first) first sentinel)]
         [best-odd  (if (odd?  first) first sentinel)]
         [max-so-far first])
    (let loop ([i 1]
               [be best-even]
               [bo best-odd]
               [ans max-so-far])
      (if (>= i n)
          ans
          (let* ([num (vector-ref v i)]
                 [candidate (if (even? num)
                                (max be (+ bo (- x)))
                                (max bo (+ be (- x))))]
                 [dp (+ num candidate)]
                 [new-be (if (even? num) (max be dp) be)]
                 [new-bo (if (odd?  num) (max bo dp) bo)]
                 [new-ans (max ans dp)])
            (loop (add1 i) new-be new-bo new-ans))))))
```

## Erlang

```erlang
-spec max_score(Nums :: [integer()], X :: integer()) -> integer().
max_score(Nums, X) ->
    case Nums of
        [] -> 0;
        [First | Rest] ->
            NegInf = -1000000000000,
            DP0 = First,
            {BestEven0, BestOdd0} =
                if First rem 2 == 0 ->
                        {DP0, NegInf};
                   true ->
                        {NegInf, DP0}
                end,
            MaxAns0 = DP0,
            {_FinalEven, _FinalOdd, Result} = lists:foldl(
                fun(Num, {BestEven, BestOdd, CurMax}) ->
                    if Num rem 2 == 0 ->
                            Same = BestEven,
                            Opp = case BestOdd of
                                      NegInf -> NegInf;
                                      _ -> BestOdd - X
                                  end,
                            DP = erlang:max(Same, Opp) + Num,
                            NewBestEven = erlang:max(BestEven, DP),
                            {NewBestEven, BestOdd, erlang:max(CurMax, DP)};
                       true ->
                            Same = BestOdd,
                            Opp = case BestEven of
                                      NegInf -> NegInf;
                                      _ -> BestEven - X
                                  end,
                            DP = erlang:max(Same, Opp) + Num,
                            NewBestOdd = erlang:max(BestOdd, DP),
                            {BestEven, NewBestOdd, erlang:max(CurMax, DP)}
                    end
                end,
                {BestEven0, BestOdd0, MaxAns0},
                Rest),
            Result
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(nums :: [integer], x :: integer) :: integer
  def max_score(nums, x) do
    inf_neg = -10_000_000_000_000_000_000

    first = hd(nums)

    {best_even, best_odd} =
      if rem(first, 2) == 0 do
        {first, nil}
      else
        {nil, first}
      end

    ans = first

    tl(nums)
    |> Enum.reduce({best_even, best_odd, ans}, fn val, {be, bo, a} ->
      even = rem(val, 2) == 0

      cand_same =
        if even do
          if be != nil, do: be + val, else: inf_neg
        else
          if bo != nil, do: bo + val, else: inf_neg
        end

      cand_diff =
        if even do
          if bo != nil, do: bo + val - x, else: inf_neg
        else
          if be != nil, do: be + val - x, else: inf_neg
        end

      dp = max(cand_same, cand_diff)
      a2 = max(a, dp)

      {new_be, new_bo} =
        if even do
          {max(be || inf_neg, dp), bo}
        else
          {be, max(bo || inf_neg, dp)}
        end

      {new_be, new_bo, a2}
    end)
    |> elem(2)
  end
end
```
