# 3022. Minimize OR of Remaining Elements Using Operations

## Cpp

```cpp
class Solution {
public:
    int minOrAfterOperations(vector<int>& nums, int k) {
        int n = nums.size();
        int overall_and = nums[0];
        int overall_or = 0;
        for (int x : nums) {
            overall_and &= x;
            overall_or |= x;
        }
        auto can = [&](int mask)->bool{
            if ((overall_and & mask) != 0) return false;
            int blocks = 0;
            int i = 0;
            while (i < n) {
                int cur = nums[i];
                if ((cur & mask) == 0) {
                    ++blocks;
                    ++i;
                    continue;
                }
                int j = i + 1;
                while (j < n && (cur & mask) != 0) {
                    cur &= nums[j];
                    ++j;
                }
                // after loop, condition must be satisfied because overall_and & mask == 0
                ++blocks;
                i = j;
            }
            long ops_needed = (long)n - blocks;
            return ops_needed <= k;
        };
        
        int mask = 0;
        for (int b = 30; b >= 0; --b) {
            int tryMask = mask | (1 << b);
            if (can(tryMask)) mask = tryMask;
        }
        return overall_or & (~mask);
    }
};
```

## Java

```java
class Solution {
    public int minOrAfterOperations(int[] nums, int k) {
        int n = nums.length;
        int overallAnd = nums[0];
        int totalOr = nums[0];
        for (int i = 1; i < n; ++i) {
            overallAnd &= nums[i];
            totalOr |= nums[i];
        }
        int mask = 0;
        // numbers are less than 2^30, so bits 0..29 are relevant
        for (int bit = 29; bit >= 0; --bit) {
            int testMask = mask | (1 << bit);
            if (isFeasible(nums, k, overallAnd, testMask)) {
                mask = testMask;
            }
        }
        return totalOr & ~mask;
    }

    private boolean isFeasible(int[] nums, int k, int overallAnd, int mask) {
        // If any bit we want to clear is present in the AND of all numbers,
        // it can never be cleared.
        if ((overallAnd & mask) != 0) return false;

        int segments = 0;
        int cur = -1; // all bits set
        for (int v : nums) {
            cur &= v;
            if ((cur & mask) == 0) {
                ++segments;
                cur = -1;
            }
        }
        int minOps = nums.length - segments;
        return minOps <= k;
    }
}
```

## Python

```python
class Solution(object):
    def minOrAfterOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        total_and = nums[0]
        for v in nums[1:]:
            total_and &= v

        ALL_ONES = (1 << 30) - 1  # since nums[i] < 2^30

        def feasible(mask):
            if total_and & mask:
                return False
            cnt = 0
            cur = ALL_ONES
            for v in nums:
                cur &= v
                if (cur & mask) == 0:
                    cnt += 1
                    cur = ALL_ONES
            min_ops = n - cnt
            return min_ops <= k

        mask = 0
        ans = 0
        for b in range(29, -1, -1):
            test_mask = mask | (1 << b)
            if feasible(test_mask):
                mask = test_mask
            else:
                ans |= (1 << b)
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        overall_or = 0
        for v in nums:
            overall_or |= v

        mask = 0

        # check if a given mask can be cleared with at most k operations
        def feasible(m: int) -> bool:
            seg = 0
            i = 0
            while i < n:
                cur_and = nums[i]
                j = i
                # extend segment until all forbidden bits are cleared
                while (cur_and & m) != 0 and j + 1 < n:
                    j += 1
                    cur_and &= nums[j]
                if (cur_and & m) != 0:   # cannot clear this bit even with whole suffix
                    return False
                seg += 1
                i = j + 1
            merges_needed = n - seg
            return merges_needed <= k

        for b in range(29, -1, -1):
            trial = mask | (1 << b)
            if feasible(trial):
                mask = trial

        return overall_or & (~mask)
```

## C

```c
int minOrAfterOperations(int* nums, int numsSize, int k) {
    // Compute total AND of all numbers
    int total_and = nums[0];
    for (int i = 1; i < numsSize; ++i) total_and &= nums[i];

    // Helper lambda to check feasibility for a given mask
    auto feasible = [&](int mask) -> bool {
        if ((total_and & mask) != 0) return false;
        int groups = 0;
        int cur = -1;
        bool inSeg = false;
        for (int i = 0; i < numsSize; ++i) {
            if (!inSeg) {
                cur = nums[i];
                inSeg = true;
            } else {
                cur &= nums[i];
            }
            if ((cur & mask) == 0) {
                groups++;
                inSeg = false;
            }
        }
        // If the last segment didn't satisfy the condition, it will be merged with previous one,
        // which effectively means we don't increase groups for it.
        int ops_needed = numsSize - groups;
        return ops_needed <= k;
    };

    int zeroMask = 0;                     // bits we can force to be zero
    for (int b = 29; b >= 0; --b) {      // numbers are < 2^30
        int testMask = zeroMask | (1 << b);
        if (feasible(testMask)) {
            zeroMask = testMask;
        }
    }

    int allBits = (1 << 30) - 1;          // bits up to 29 set
    int answer = allBits ^ zeroMask;      // bits we couldn't clear remain 1
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOrAfterOperations(int[] nums, int k) {
        int n = nums.Length;
        int overallAnd = nums[0];
        foreach (int v in nums) overallAnd &= v;

        int mask = 0; // bits we can eliminate
        for (int bit = 30; bit >= 0; --bit) {
            int testMask = mask | (1 << bit);
            if ((overallAnd & testMask) != 0) continue; // impossible to clear this bit

            int ops = 0;
            int i = 0;
            while (i < n) {
                if ((nums[i] & testMask) == 0) {
                    i++;
                    continue;
                }
                ops++; // need one operation for this bad segment
                while (i < n && (nums[i] & testMask) != 0) i++;
            }

            if (ops <= k) mask = testMask;
        }

        int answer = 0;
        for (int bit = 30; bit >= 0; --bit) {
            if ((mask & (1 << bit)) == 0) answer |= (1 << bit);
        }
        return answer;
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
var minOrAfterOperations = function(nums, k) {
    const n = nums.length;
    let totalAnd = nums[0];
    for (let i = 1; i < n; ++i) totalAnd &= nums[i];

    let ans = 0;
    let mask = 0;

    for (let bit = 29; bit >= 0; --bit) {
        const candMask = mask | (1 << bit);
        if ((totalAnd & candMask) !== 0) {
            ans |= (1 << bit);
            continue;
        }

        let ops = 0;
        let extra = false;
        for (let i = 0; i < n - 1;) {
            if ((nums[i] & candMask) !== 0) {
                ++ops;
                if ((nums[i + 1] & candMask) !== 0) extra = true;
                i += 2;
            } else {
                ++i;
            }
        }

        const minOps = ops + (extra ? 1 : 0);
        if (minOps <= k) {
            mask = candMask; // can eliminate this bit
        } else {
            ans |= (1 << bit);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function minOrAfterOperations(nums: number[], k: number): number {
    const n = nums.length;
    let totalOr = 0;
    let overallAnd = nums[0];
    for (const v of nums) {
        totalOr |= v;
        overallAnd &= v;
    }

    const can = (mask: number): boolean => {
        if ((overallAnd & mask) !== 0) return false;
        let groups = 0;
        let cur = -1; // all bits set
        for (const v of nums) {
            cur &= v;
            if ((cur & mask) === 0) {
                groups++;
                cur = -1;
            }
        }
        const opsNeeded = n - groups;
        return opsNeeded <= k;
    };

    let mask = 0;
    for (let b = 30; b >= 0; --b) {
        const tentative = mask | (1 << b);
        if (can(tentative)) mask = tentative;
    }

    const result = totalOr & (~mask);
    return result >>> 0;
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
    function minOrAfterOperations($nums, $k) {
        $n = count($nums);
        $fullMask = (1 << 30) - 1; // bits 0..29 set
        $mask = 0;
        for ($bit = 29; $bit >= 0; $bit--) {
            $candidate = $mask | (1 << $bit);
            if ($this->canAchieve($candidate, $nums, $k, $fullMask)) {
                $mask = $candidate;
            }
        }
        // bits not eliminated remain in the answer
        return $fullMask ^ $mask;
    }

    private function canAchieve($mask, $nums, $k, $fullMask) {
        $n = count($nums);
        // overall AND of all numbers
        $totalAnd = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $totalAnd &= $nums[$i];
        }
        if (($totalAnd & $mask) != 0) {
            return false;
        }

        $cnt = 0;          // number of valid segments
        $cur = $fullMask;  // current segment AND (start with all bits set)
        foreach ($nums as $v) {
            $cur &= $v;
            if (($cur & $mask) == 0) {
                $cnt++;
                $cur = $fullMask;
            }
        }

        $ops = $n - $cnt; // merges needed
        if ($cur != $fullMask) { // leftover segment still has forbidden bits
            $ops++;              // need one extra merge
        }
        return $ops <= $k;
    }
}
```

## Swift

```swift
class Solution {
    func minOrAfterOperations(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var totalAnd = nums[0]
        for v in nums { totalAnd &= v }
        var mask = 0
        // bits up to 30 because nums[i] < 2^30
        for b in stride(from: 30, through: 0, by: -1) {
            let candidate = mask | (1 << b)
            if (totalAnd & candidate) != 0 { continue }
            var ops = 0
            var i = 0
            while i < n {
                if (nums[i] & candidate) != 0 {
                    ops += 1
                    i += 2   // merge this element with the next one
                } else {
                    i += 1
                }
            }
            if ops <= k { mask = candidate }
        }
        let allBitsMask = (1 << 31) - 1
        return totalAnd | ((~mask) & allBitsMask)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOrAfterOperations(nums: IntArray, k: Int): Int {
        val n = nums.size
        var totalAnd = nums[0]
        for (i in 1 until n) {
            totalAnd = totalAnd and nums[i]
        }
        var mask = 0
        var answer = 0
        // numbers are less than 2^30, so bits 29..0 are enough
        for (b in 29 downTo 0) {
            val bit = 1 shl b
            val newMask = mask or bit
            // if totalAnd still has this bit, impossible to clear it
            if ((totalAnd and newMask) != 0) {
                answer = answer or bit
                continue
            }
            var ops = 0
            var i = 0
            while (i < n) {
                if ((nums[i] and newMask) != 0) {
                    ops++
                    // skip consecutive elements that also contain forbidden bits
                    while (i + 1 < n && (nums[i + 1] and newMask) != 0) {
                        i++
                    }
                }
                i++
            }
            val needed = if (totalAnd == 0) ops else ops + 1
            if (needed <= k) {
                mask = newMask   // we can eliminate this bit
            } else {
                answer = answer or bit
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minOrAfterOperations(List<int> nums, int k) {
    int n = nums.length;
    int totalAnd = nums[0];
    int totalOr = nums[0];
    for (int i = 1; i < n; i++) {
      totalAnd &= nums[i];
      totalOr |= nums[i];
    }
    const int ALL_ONES = (1 << 30) - 1;
    int mask = 0;

    for (int b = 29; b >= 0; b--) {
      int tryMask = mask | (1 << b);
      if ((totalAnd & tryMask) != 0) continue; // impossible to clear this bit

      int segCount = 0;
      int cur = ALL_ONES;
      for (int num in nums) {
        cur &= num;
        if ((cur & tryMask) == 0) {
          segCount++;
          cur = ALL_ONES;
        }
      }
      int opsNeeded = n - segCount;
      if (opsNeeded <= k) {
        mask = tryMask;
      }
    }

    return totalOr & (~mask & ALL_ONES);
  }
}
```

## Golang

```go
func minOrAfterOperations(nums []int, k int) int {
    n := len(nums)
    totalOr := 0
    overallAnd := ^0
    for _, v := range nums {
        totalOr |= v
        overallAnd &= v
    }
    mask := 0
    // bits up to 29 because nums[i] < 2^30
    for b := 29; b >= 0; b-- {
        tryMask := mask | (1 << b)
        if (overallAnd & tryMask) != 0 {
            continue // impossible to eliminate this bit
        }
        ops := 0
        x := ^0
        i := 0
        for i < n {
            cur := nums[i]
            for (cur&tryMask) != 0 && i+1 < n {
                ops++
                i++
                cur &= nums[i]
            }
            x &= cur
            i++
        }
        if (x & tryMask) != 0 {
            ops++ // one extra operation needed
        }
        if ops <= k {
            mask = tryMask
        }
    }
    return totalOr & ^mask
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_or_after_operations(nums, k)
  n = nums.length
  overall_and = nums.reduce { |a, b| a & b }
  overall_or = nums.reduce { |a, b| a | b }

  mask = 0

  # check if a given mask can be eliminated with at most k operations
  feasible = lambda do |m|
    return false if (overall_and & m) != 0

    ops = 0
    i = 0
    while i < n
      if (nums[i] & m) != 0
        ops += 1
        i += 2   # merge with the next element
      else
        i += 1
      end
    end

    # after performing these merges, compute AND of remaining elements
    cur_and = (1 << 30) - 1
    i = 0
    while i < n
      if i + 1 < n && (nums[i] & m) != 0
        merged = nums[i] & nums[i + 1]
        cur_and &= merged
        i += 2
      else
        cur_and &= nums[i]
        i += 1
      end
    end

    ops += 1 if (cur_and & m) != 0
    ops <= k
  end

  (29).downto(0) do |bit|
    trial = mask | (1 << bit)
    mask = trial if feasible.call(trial)
  end

  overall_or & (~mask)
end
```

## Scala

```scala
object Solution {
    def minOrAfterOperations(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        var overallAnd = nums(0)
        var i = 1
        while (i < n) {
            overallAnd &= nums(i)
            i += 1
        }

        def can(mask: Int): Boolean = {
            if ((overallAnd & mask) != 0) return false
            var ops = 0
            var idx = 0
            while (idx < n) {
                if ((nums(idx) & mask) != 0) {
                    var len = 0
                    while (idx < n && (nums(idx) & mask) != 0) {
                        len += 1
                        idx += 1
                    }
                    ops += (len + 1) / 2
                } else {
                    idx += 1
                }
            }
            ops <= k
        }

        var elimMask = 0
        val maxBit = 30 // numbers are < 2^30
        for (b <- (maxBit - 1) to 0 by -1) {
            val trial = elimMask | (1 << b)
            if (can(trial)) {
                elimMask = trial
            }
        }
        val fullMask = (1 << maxBit) - 1
        fullMask ^ elimMask
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_or_after_operations(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        // total AND of all numbers
        let mut total_and = nums[0];
        for &v in nums.iter().skip(1) {
            total_and &= v;
        }
        // overall OR of all numbers
        let mut overall_or = 0i32;
        for &v in &nums {
            overall_or |= v;
        }

        // helper closure to check feasibility of a mask
        let feasible = |mask: i32| -> bool {
            if (total_and & mask) != 0 {
                return false;
            }
            let mut cnt = 0usize;
            for &v in &nums {
                if (v & mask) != 0 {
                    cnt += 1;
                }
            }
            cnt <= k_usize
        };

        let mut mask: i32 = 0;
        // bits up to 30 (since nums[i] < 2^30)
        for b in (0..=30).rev() {
            let candidate = mask | (1 << b);
            if feasible(candidate) {
                mask = candidate;
            }
        }

        overall_or & !mask
    }
}
```

## Racket

```racket
(define/contract (min-or-after-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (letrec
      ((min-ops-needed
        (lambda (mask)
          (let ((all-and (foldl bitwise-and -1 nums)))
            (if (not (= 0 (bitwise-and all-and mask)))
                +inf.0
                (let loop ((cnt 0) (cur (car nums)) (rest (cdr nums)) (rem '()))
                  (if (null? rest)
                      (let* ((final-rem (cons cur rem))
                             (overall-and (foldl bitwise-and -1 final-rem)))
                        (+ cnt (if (= 0 (bitwise-and overall-and mask)) 0 1)))
                      (let ((next (car rest))
                            (rest-tail (cdr rest)))
                        (if (not (= 0 (bitwise-and cur mask))) ; cur is bad
                            (loop (+ cnt 1) (bitwise-and cur next) rest-tail rem)
                            (loop cnt next rest-tail (cons cur rem))))))))))
       (find-mask
        (lambda (b current-mask)
          (if (< b 0)
              current-mask
              (let ((try-mask (bitwise-ior current-mask (arithmetic-shift 1 b))))
                (if (<= (min-ops-needed try-mask) k)
                    (find-mask (- b 1) try-mask)
                    (find-mask (- b 1) current-mask)))))))
    (let* ((mask (find-mask 29 0))
           (overall-or (foldl bitwise-ior 0 nums))
           (answer (bitwise-and overall-or (bitwise-not mask))))
      answer)))
```

## Erlang

```erlang
-spec min_or_after_operations([integer()], integer()) -> integer().
min_or_after_operations(Nums, K) ->
    OrigOr = lists:foldl(fun(X, Acc) -> X bor Acc end, 0, Nums),
    Len = length(Nums),
    AllOnes = (1 bsl 30) - 1,
    TotalAndAll = case Nums of
        [] -> 0;
        [H|T] -> lists:foldl(fun(X, Acc) -> X band Acc end, H, T)
    end,
    MaxBit = 29,
    Mask = lists:foldl(
        fun(BitPos, MaskAcc) ->
            TrialMask = MaskAcc bor (1 bsl BitPos),
            case TotalAndAll band TrialMask of
                0 ->
                    {Cnt, _} =
                        lists:foldl(
                            fun(Num, {C, Cur}) ->
                                NewCur = Cur band Num,
                                if (NewCur band TrialMask) == 0 ->
                                        {C + 1, AllOnes};
                                   true -> {C, NewCur}
                                end
                            end,
                            {0, AllOnes},
                            Nums),
                    OpsNeeded = Len - Cnt,
                    if OpsNeeded =< K ->
                        TrialMask;
                       true ->
                        MaskAcc
                    end;
                _ ->
                    MaskAcc
            end
        end,
        0,
        lists:seq(MaxBit, 0, -1)
    ),
    OrigOr band bnot(Mask).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec min_or_after_operations(nums :: [integer], k :: integer) :: integer
  def min_or_after_operations(nums, k) do
    max_bits = 30
    full_mask = (1 <<< max_bits) - 1

    total_and =
      Enum.reduce(nums, full_mask, fn x, acc -> acc &&& x end)

    total_or =
      Enum.reduce(nums, 0, fn x, acc -> acc ||| x end)

    mask =
      Enum.reduce(Enum.reverse(0..(max_bits - 1)), 0, fn bit, cur_mask ->
        tentative = cur_mask ||| (1 <<< bit)

        if feasible?(nums, k, tentative, total_and) do
          tentative
        else
          cur_mask
        end
      end)

    result = total_or &&& bnot(mask)
    result &&& full_mask
  end

  defp feasible?(nums, k, mask, total_and) do
    if (total_and &&& mask) != 0 do
      false
    else
      min_ops(nums, mask) <= k
    end
  end

  defp min_ops(nums, mask) do
    {ops, len, cur_and} =
      Enum.reduce(nums, {0, 0, nil}, fn x, {ops, len, cur_and} ->
        cond do
          cur_and == nil ->
            if (x &&& mask) == 0 do
              {ops, 0, nil}
            else
              {ops, 1, x}
            end

          true ->
            new_and = cur_and &&& x
            new_len = len + 1

            if (new_and &&& mask) == 0 do
              {ops + new_len - 1, 0, nil}
            else
              {ops, new_len, new_and}
            end
        end
      end)

    if cur_and != nil do
      ops + 1
    else
      ops
    end
  end
end
```
