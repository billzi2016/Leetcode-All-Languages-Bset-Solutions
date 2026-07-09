# 2172. Maximum AND Sum of Array

## Cpp

```cpp
class Solution {
public:
    int maximumANDSum(vector<int>& nums, int numSlots) {
        int n = nums.size();
        int totalPos = 2 * numSlots;
        int fullMask = 1 << totalPos;
        const int NEG_INF = -1e9;
        vector<int> dp(fullMask, NEG_INF);
        dp[0] = 0;
        for (int mask = 0; mask < fullMask; ++mask) {
            if (dp[mask] == NEG_INF) continue;
            int used = __builtin_popcount((unsigned)mask);
            if (used >= n) continue;
            int curNum = nums[used];
            for (int pos = 0; pos < totalPos; ++pos) {
                if (!(mask & (1 << pos))) {
                    int slotIdx = pos / 2 + 1;
                    int newMask = mask | (1 << pos);
                    dp[newMask] = max(dp[newMask], dp[mask] + (curNum & slotIdx));
                }
            }
        }
        int ans = 0;
        for (int mask = 0; mask < fullMask; ++mask) {
            if (__builtin_popcount((unsigned)mask) == n) {
                ans = max(ans, dp[mask]);
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumANDSum(int[] nums, int numSlots) {
        int totalPos = numSlots * 2;
        int maxMask = 1 << totalPos;
        int[] dp = new int[maxMask];
        Arrays.fill(dp, Integer.MIN_VALUE);
        dp[0] = 0;

        for (int mask = 0; mask < maxMask; ++mask) {
            if (dp[mask] == Integer.MIN_VALUE) continue;
            int i = Integer.bitCount(mask); // number of numbers already placed
            if (i >= nums.length) continue;
            for (int pos = 0; pos < totalPos; ++pos) {
                if ((mask & (1 << pos)) == 0) {
                    int slot = pos / 2 + 1;
                    int newMask = mask | (1 << pos);
                    dp[newMask] = Math.max(dp[newMask], dp[mask] + (nums[i] & slot));
                }
            }
        }

        int ans = 0;
        for (int mask = 0; mask < maxMask; ++mask) {
            if (Integer.bitCount(mask) == nums.length) {
                ans = Math.max(ans, dp[mask]);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        n = len(nums)
        total_positions = 2 * numSlots
        slot_of_pos = [(i // 2) + 1 for i in range(total_positions)]
        dp = {0: 0}  # mask -> max sum
        for idx, val in enumerate(nums):
            newdp = {}
            for mask, cur_sum in dp.items():
                # try to place current number into any free position
                for p in range(total_positions):
                    if not (mask >> p) & 1:
                        nmask = mask | (1 << p)
                        added = val & slot_of_pos[p]
                        ns = cur_sum + added
                        if nmask not in newdp or ns > newdp[nmask]:
                            newdp[nmask] = ns
            dp = newdp
        return max(dp.values())
```

## Python3

```python
from typing import List

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        total_pos = 2 * numSlots
        size = 1 << total_pos
        dp = [-1] * size
        dp[0] = 0

        for mask in range(1, size):
            cnt = mask.bit_count()
            if cnt > n:
                continue
            idx = cnt - 1  # current number index
            sub = mask
            while sub:
                lsb = sub & -sub
                pos = (lsb.bit_length() - 1)          # position index 0..2*numSlots-1
                prev = mask ^ lsb
                if dp[prev] != -1:
                    val = dp[prev] + (nums[idx] & ((pos // 2) + 1))
                    if val > dp[mask]:
                        dp[mask] = val
                sub ^= lsb

        ans = 0
        for mask in range(size):
            if mask.bit_count() == n:
                if dp[mask] > ans:
                    ans = dp[mask]
        return ans
```

## C

```c
#include <limits.h>

int maximumANDSum(int* nums, int numsSize, int numSlots) {
    int totalBits = numSlots * 2;
    int maxMask = 1 << totalBits;
    // Initialize dp with very small values
    int *dp = (int *)malloc(sizeof(int) * maxMask);
    for (int i = 0; i < maxMask; ++i) dp[i] = INT_MIN;
    dp[0] = 0;

    for (int mask = 0; mask < maxMask; ++mask) {
        int used = __builtin_popcount(mask);
        if (used >= numsSize) continue;
        int curVal = dp[mask];
        if (curVal == INT_MIN) continue;
        int num = nums[used];
        for (int slot = 0; slot < numSlots; ++slot) {
            int pos1 = slot * 2;
            int pos2 = slot * 2 + 1;
            int add = num & (slot + 1);
            if (!(mask & (1 << pos1))) {
                int nMask = mask | (1 << pos1);
                if (curVal + add > dp[nMask]) dp[nMask] = curVal + add;
            }
            if (!(mask & (1 << pos2))) {
                int nMask = mask | (1 << pos2);
                if (curVal + add > dp[nMask]) dp[nMask] = curVal + add;
            }
        }
    }

    int ans = 0;
    for (int mask = 0; mask < maxMask; ++mask) {
        if (__builtin_popcount(mask) == numsSize && dp[mask] > ans) {
            ans = dp[mask];
        }
    }

    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution {
    public int MaximumANDSum(int[] nums, int numSlots) {
        int n = nums.Length;
        int totalPos = numSlots * 2;
        int maxMask = 1 << totalPos;
        int[] dp = new int[maxMask];
        Array.Fill(dp, -1);
        dp[0] = 0;
        int answer = 0;

        for (int mask = 0; mask < maxMask; ++mask) {
            if (dp[mask] == -1) continue;
            int used = BitOperations.PopCount((uint)mask);
            if (used == n) {
                if (dp[mask] > answer) answer = dp[mask];
                continue;
            }
            int curNum = nums[used];
            for (int pos = 0; pos < totalPos; ++pos) {
                if ((mask & (1 << pos)) != 0) continue;
                int slot = pos / 2 + 1;
                int newMask = mask | (1 << pos);
                int val = dp[mask] + (curNum & slot);
                if (val > dp[newMask]) dp[newMask] = val;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} numSlots
 * @return {number}
 */
var maximumANDSum = function(nums, numSlots) {
    const n = nums.length;
    const totalPos = numSlots * 2;               // each slot has two positions
    const maxMask = 1 << totalPos;

    // precompute popcount for all masks
    const popcnt = new Uint8Array(maxMask);
    for (let mask = 1; mask < maxMask; ++mask) {
        popcnt[mask] = popcnt[mask >> 1] + (mask & 1);
    }

    // slot number for each position index
    const slotNum = new Int8Array(totalPos);
    for (let i = 0; i < totalPos; ++i) {
        slotNum[i] = Math.floor(i / 2) + 1;
    }

    const dp = new Int32Array(maxMask);
    // fill with very small number
    for (let i = 0; i < maxMask; ++i) dp[i] = -1e9;
    dp[0] = 0;

    for (let mask = 0; mask < maxMask; ++mask) {
        const used = popcnt[mask];
        if (used >= n) continue; // all numbers already placed
        const curVal = dp[mask];
        if (curVal < -1e8) continue;
        const num = nums[used];
        for (let pos = 0; pos < totalPos; ++pos) {
            if ((mask & (1 << pos)) === 0) {
                const newMask = mask | (1 << pos);
                const cand = curVal + (num & slotNum[pos]);
                if (cand > dp[newMask]) dp[newMask] = cand;
            }
        }
    }

    let ans = 0;
    for (let mask = 0; mask < maxMask; ++mask) {
        if (popcnt[mask] === n && dp[mask] > ans) ans = dp[mask];
    }
    return ans;
};
```

## Typescript

```typescript
function maximumANDSum(nums: number[], numSlots: number): number {
    const m = numSlots * 2;
    const totalMask = 1 << m;
    const NEG = -1e9;
    let dp = new Int32Array(totalMask);
    for (let i = 0; i < totalMask; i++) dp[i] = NEG;
    dp[0] = 0;

    for (const num of nums) {
        const ndp = new Int32Array(totalMask);
        for (let i = 0; i < totalMask; i++) ndp[i] = NEG;
        for (let mask = 0; mask < totalMask; mask++) {
            const cur = dp[mask];
            if (cur === NEG) continue;
            for (let j = 0; j < m; j++) {
                if ((mask >> j) & 1) continue;
                const slot = (j >> 1) + 1;
                const newMask = mask | (1 << j);
                const val = cur + (num & slot);
                if (val > ndp[newMask]) ndp[newMask] = val;
            }
        }
        dp = ndp;
    }

    let ans = 0;
    for (let mask = 0; mask < totalMask; mask++) {
        if (dp[mask] > ans) ans = dp[mask];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $numSlots
     * @return Integer
     */
    function maximumANDSum($nums, $numSlots) {
        $n = count($nums);
        $m = $numSlots * 2;                 // total positions
        $maxMask = 1 << $m;

        // precompute popcount for all masks
        $popcnt = array_fill(0, $maxMask, 0);
        for ($mask = 1; $mask < $maxMask; ++$mask) {
            $popcnt[$mask] = $popcnt[$mask >> 1] + ($mask & 1);
        }

        // slot number for each position
        $slotNum = [];
        for ($i = 0; $i < $m; ++$i) {
            $slotNum[$i] = intdiv($i, 2) + 1;
        }

        // dp[mask] = max sum using positions indicated by mask
        $dp = array_fill(0, $maxMask, -1);
        $dp[0] = 0;

        for ($mask = 0; $mask < $maxMask; ++$mask) {
            if ($dp[$mask] < 0) continue;
            $k = $popcnt[$mask]; // how many numbers already placed
            if ($k >= $n) continue;
            $num = $nums[$k];
            for ($i = 0; $i < $m; ++$i) {
                if ((($mask >> $i) & 1) == 0) { // position i is free
                    $newMask = $mask | (1 << $i);
                    $val = $dp[$mask] + ($num & $slotNum[$i]);
                    if ($val > $dp[$newMask]) {
                        $dp[$newMask] = $val;
                    }
                }
            }
        }

        $ans = 0;
        for ($mask = 0; $mask < $maxMask; ++$mask) {
            if ($popcnt[$mask] == $n && $dp[$mask] > $ans) {
                $ans = $dp[$mask];
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumANDSum(_ nums: [Int], _ numSlots: Int) -> Int {
        let n = nums.count
        let totalPos = 2 * numSlots
        let limit = 1 << totalPos
        var dp = Array(repeating: -1_000_000_000, count: limit)
        dp[0] = 0
        
        for mask in 0..<limit {
            let cur = dp[mask]
            if cur < 0 { continue }
            let k = mask.nonzeroBitCount
            if k >= n { continue }
            let num = nums[k]
            var p = 0
            while p < totalPos {
                if (mask & (1 << p)) == 0 {
                    let slot = p / 2 + 1
                    let newMask = mask | (1 << p)
                    let val = cur + (num & slot)
                    if val > dp[newMask] {
                        dp[newMask] = val
                    }
                }
                p += 1
            }
        }
        
        var ans = 0
        for mask in 0..<limit where mask.nonzeroBitCount == n {
            ans = max(ans, dp[mask])
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumANDSum(nums: IntArray, numSlots: Int): Int {
        val n = nums.size
        val m = numSlots * 2
        val totalMask = 1 shl m
        val dp = IntArray(totalMask) { -1 }
        dp[0] = 0
        for (mask in 1 until totalMask) {
            val bits = Integer.bitCount(mask)
            if (bits > n) continue
            val idx = bits - 1
            var best = -1
            var sub = mask
            while (sub != 0) {
                val lsb = sub and -sub
                val pos = Integer.numberOfTrailingZeros(lsb)
                val prevMask = mask xor lsb
                if (dp[prevMask] >= 0) {
                    val slotIdx = pos / 2 + 1
                    val cand = dp[prevMask] + (nums[idx] and slotIdx)
                    if (cand > best) best = cand
                }
                sub -= lsb
            }
            dp[mask] = best
        }
        var ans = 0
        for (mask in 0 until totalMask) {
            if (Integer.bitCount(mask) == n && dp[mask] > ans) {
                ans = dp[mask]
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumANDSum(List<int> nums, int numSlots) {
    int n = nums.length;
    int totalPos = numSlots * 2;
    int maxMask = 1 << totalPos;
    List<int> dp = List.filled(maxMask, -1);
    dp[0] = 0;
    int answer = 0;

    for (int mask = 0; mask < maxMask; ++mask) {
      if (dp[mask] < 0) continue;
      int used = _popCount(mask);
      if (used == n) {
        if (dp[mask] > answer) answer = dp[mask];
        continue;
      }
      for (int p = 0; p < totalPos; ++p) {
        if ((mask & (1 << p)) == 0) {
          int newMask = mask | (1 << p);
          int slotNum = (p ~/ 2) + 1;
          int val = dp[mask] + (nums[used] & slotNum);
          if (val > dp[newMask]) dp[newMask] = val;
        }
      }
    }

    return answer;
  }

  int _popCount(int x) {
    int cnt = 0;
    while (x != 0) {
      x &= x - 1;
      cnt++;
    }
    return cnt;
  }
}
```

## Golang

```go
func maximumANDSum(nums []int, numSlots int) int {
    n := len(nums)
    bits := 2 * numSlots
    maxMask := 1 << bits

    memo := make([][]int, n+1)
    for i := 0; i <= n; i++ {
        memo[i] = make([]int, maxMask)
        for j := 0; j < maxMask; j++ {
            memo[i][j] = -1
        }
    }

    var dfs func(idx int, mask int) int
    dfs = func(idx int, mask int) int {
        if idx == n {
            return 0
        }
        if memo[idx][mask] != -1 {
            return memo[idx][mask]
        }
        best := 0
        for s := 0; s < numSlots; s++ {
            slotIdx := s + 1
            andVal := nums[idx] & slotIdx

            b0 := 1 << (2 * s)
            if mask&b0 == 0 {
                val := andVal + dfs(idx+1, mask|b0)
                if val > best {
                    best = val
                }
            }

            b1 := 1 << (2*s + 1)
            if mask&b1 == 0 {
                val := andVal + dfs(idx+1, mask|b1)
                if val > best {
                    best = val
                }
            }
        }
        memo[idx][mask] = best
        return best
    }

    return dfs(0, 0)
}
```

## Ruby

```ruby
def maximum_and_sum(nums, num_slots)
  n = nums.length
  total_positions = num_slots * 2
  max_mask = 1 << total_positions
  neg_inf = -(1 << 60)

  dp = Array.new(max_mask, neg_inf)
  dp[0] = 0

  popcnt = Array.new(max_mask, 0)
  (1...max_mask).each do |i|
    popcnt[i] = popcnt[i >> 1] + (i & 1)
  end

  answer = 0
  (0...max_mask).each do |mask|
    cur = dp[mask]
    next if cur == neg_inf
    cnt = popcnt[mask]

    if cnt == n
      answer = cur if cur > answer
      next
    end

    num = nums[cnt]
    (0...total_positions).each do |pos|
      next if (mask & (1 << pos)) != 0
      slot = (pos / 2) + 1
      new_mask = mask | (1 << pos)
      val = cur + (num & slot)
      dp[new_mask] = val if val > dp[new_mask]
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
  def maximumANDSum(nums: Array[Int], numSlots: Int): Int = {
    val n = nums.length
    val m = numSlots * 2
    val totalMask = 1 << m
    val NEG_INF = Int.MinValue / 4
    val dp = Array.fill(totalMask)(NEG_INF)
    dp(0) = 0

    for (mask <- 0 until totalMask) {
      val cnt = Integer.bitCount(mask)
      if (cnt < n && dp(mask) != NEG_INF) {
        val curNum = nums(cnt)
        var j = 0
        while (j < m) {
          if ((mask & (1 << j)) == 0) {
            val slotIdx = j / 2 + 1
            val newMask = mask | (1 << j)
            val value = dp(mask) + (curNum & slotIdx)
            if (value > dp(newMask)) dp(newMask) = value
          }
          j += 1
        }
      }
    }

    var ans = 0
    for (mask <- 0 until totalMask) {
      if (Integer.bitCount(mask) == n && dp(mask) > ans) ans = dp(mask)
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_and_sum(nums: Vec<i32>, num_slots: i32) -> i32 {
        let n = nums.len();
        let m = (num_slots as usize) * 2;
        let total_masks = 1usize << m;
        let mut dp = vec![-1i32; total_masks];
        dp[0] = 0;
        for mask in 0..total_masks {
            if dp[mask] < 0 {
                continue;
            }
            let k = mask.count_ones() as usize;
            if k == n {
                continue;
            }
            let num = nums[k];
            for j in 0..m {
                if (mask >> j) & 1 == 0 {
                    let slot = (j / 2 + 1) as i32;
                    let new_mask = mask | (1usize << j);
                    let val = dp[mask] + (num & slot);
                    if dp[new_mask] < val {
                        dp[new_mask] = val;
                    }
                }
            }
        }
        let mut ans = 0i32;
        for mask in 0..total_masks {
            if mask.count_ones() as usize == n && dp[mask] > ans {
                ans = dp[mask];
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-and-sum nums numSlots)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (total-pos (* 2 numSlots))
         (maxMask (arithmetic-shift 1 total-pos))
         (dp (make-vector maxMask -1000000))
         (popcnt (make-vector maxMask 0)))
    ;; precompute popcounts
    (for ([mask (in-range maxMask)])
      (vector-set! popcnt mask (bitwise-bit-count mask)))
    (vector-set! dp 0 0)
    (for ([mask (in-range maxMask)])
      (define cur (vector-ref dp mask))
      (when (> cur -1000000) ; reachable state
        (define used (vector-ref popcnt mask))
        (when (< used n)
          (define num (list-ref nums used))
          (for ([p (in-range total-pos)])
            (when (= (bitwise-and mask (arithmetic-shift 1 p)) 0)
              (define newMask (bitwise-ior mask (arithmetic-shift 1 p)))
              (define slot (+ (quotient p 2) 1))
              (define val (bitwise-and num slot))
              (define candidate (+ cur val))
              (when (> candidate (vector-ref dp newMask))
                (vector-set! dp newMask candidate))))))))
    ;; find answer among masks using exactly n positions
    (let ((ans -1000000))
      (for ([mask (in-range maxMask)])
        (when (= (vector-ref popcnt mask) n)
          (define val (vector-ref dp mask))
          (when (> val ans) (set! ans val))))
      ans)))
```

## Erlang

```erlang
-spec maximum_and_sum(Nums :: [integer()], NumSlots :: integer()) -> integer().
maximum_and_sum(Nums, NumSlots) ->
    Pow3 = gen_pow3_tuple(NumSlots),
    TotalStates = pow_int(3, NumSlots),
    InitDP = list_to_tuple(lists:duplicate(TotalStates, -1)),
    DP0 = put_element(1, InitDP, 0), % mask 0 has value 0
    FinalDP = lists:foldl(
        fun(Num, DPPrev) ->
            NewDP = list_to_tuple(lists:duplicate(TotalStates, -1)),
            process_masks(Num, NumSlots, Pow3, DPPrev, NewDP)
        end,
        DP0,
        Nums),
    lists:max(tuple_to_list(FinalDP)).

%% generate tuple of powers of 3: pow3[i] = 3^(i-1) for i=1..N
gen_pow3_tuple(N) -> gen_pow3_tuple(1, N, 1, []).

gen_pow3_tuple(I, N, Acc, AccList) when I > N ->
    list_to_tuple(lists:reverse(AccList));
gen_pow3_tuple(I, N, Acc, AccList) ->
    gen_pow3_tuple(I + 1, N, Acc * 3, [Acc | AccList]).

%% integer exponentiation
pow_int(_, 0) -> 1;
pow_int(Base, Exp) when Exp > 0 -> pow_int(Base, Exp - 1, 1).
pow_int(_Base, 0, Acc) -> Acc;
pow_int(Base, Exp, Acc) ->
    pow_int(Base, Exp - 1, Acc * Base).

%% process all masks for a given number
process_masks(Num, NumSlots, Pow3, DPPrev, DPNew) ->
    Size = tuple_size(DPPrev),
    loop_masks(0, Size - 1, Num, NumSlots, Pow3, DPPrev, DPNew).

loop_masks(Index, MaxIdx, _Num, _NumSlots, _Pow3, _DPPrev, DP) when Index > MaxIdx ->
    DP;
loop_masks(Index, MaxIdx, Num, NumSlots, Pow3, DPPrev, DP) ->
    CurVal = element(Index + 1, DPPrev),
    DP1 = if
        CurVal >= 0 ->
            place_in_slots(Num, NumSlots, Pow3, Index, CurVal, DP);
        true -> DP
    end,
    loop_masks(Index + 1, MaxIdx, Num, NumSlots, Pow3, DPPrev, DP1).

place_in_slots(Num, NumSlots, Pow3, Mask, CurVal, DP) ->
    place_slot(1, Num, NumSlots, Pow3, Mask, CurVal, DP).

place_slot(I, _Num, NumSlots, _Pow3, _Mask, _CurVal, DP) when I > NumSlots ->
    DP;
place_slot(I, Num, NumSlots, Pow3, Mask, CurVal, DP) ->
    Pow = element(I, Pow3),
    Digit = (Mask div Pow) rem 3,
    DP1 = if
        Digit < 2 ->
            NewMask = Mask + Pow,
            NewVal = CurVal + (Num band I),
            OldVal = element(NewMask + 1, DP),
            MaxV = case NewVal > OldVal of true -> NewVal; false -> OldVal end,
            put_element(NewMask + 1, DP, MaxV);
        true -> DP
    end,
    place_slot(I + 1, Num, NumSlots, Pow3, Mask, CurVal, DP1).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_and_sum(nums :: [integer], num_slots :: integer) :: integer
  def maximum_and_sum(nums, num_slots) do
    require Bitwise

    total = num_slots * 2
    max_mask = 1 <<< total
    n = length(nums)

    dp_initial = %{0 => 0}

    dp =
      Enum.reduce(0..max_mask - 1, dp_initial, fn mask, acc ->
        case Map.get(acc, mask) do
          nil ->
            acc

          cur ->
            k = bitcount(mask)

            if k < n do
              num = Enum.at(nums, k)

              Enum.reduce(0..total - 1, acc, fn pos, inner_acc ->
                if (mask &&& (1 <<< pos)) == 0 do
                  slot = div(pos, 2) + 1
                  new_mask = mask ||| (1 <<< pos)
                  val = cur + Bitwise.band(num, slot)

                  prev = Map.get(inner_acc, new_mask, -1)

                  if val > prev do
                    Map.put(inner_acc, new_mask, val)
                  else
                    inner_acc
                  end
                else
                  inner_acc
                end
              end)
            else
              acc
            end
        end
      end)

    Enum.reduce(dp, 0, fn {mask, value}, best ->
      if bitcount(mask) == n and value > best do
        value
      else
        best
      end
    end)
  end

  defp bitcount(0), do: 0
  defp bitcount(x) do
    (x &&& 1) + bitcount(x >>> 1)
  end
end
```
