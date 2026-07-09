# 1655. Distribute Repeating Integers

## Cpp

```cpp
class Solution {
public:
    bool canDistribute(vector<int>& nums, vector<int>& quantity) {
        unordered_map<int,int> cnt;
        for (int x : nums) ++cnt[x];
        vector<int> freq;
        freq.reserve(cnt.size());
        for (auto &p : cnt) freq.push_back(p.second);
        
        int m = quantity.size();
        int fullMask = (1<<m) - 1;
        vector<int> subsetSum(1<<m,0);
        for (int mask=1; mask<=fullMask; ++mask){
            int lsb = __builtin_ctz(mask);
            int prev = mask ^ (1<<lsb);
            subsetSum[mask] = subsetSum[prev] + quantity[lsb];
        }
        
        vector<char> dp(1<<m, 0), ndp;
        dp[0] = 1;
        for (int f : freq){
            ndp = dp; // copy current states
            for (int mask=0; mask<=fullMask; ++mask){
                if (!dp[mask]) continue;
                int remain = fullMask ^ mask;
                for (int sub = remain; sub; sub = (sub-1) & remain){
                    if (subsetSum[sub] <= f){
                        ndp[mask | sub] = 1;
                    }
                }
            }
            dp.swap(ndp);
        }
        return dp[fullMask];
    }
};
```

## Java

```java
class Solution {
    public boolean canDistribute(int[] nums, int[] quantity) {
        // count frequencies of each unique number
        java.util.Map<Integer, Integer> map = new java.util.HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int[] freq = new int[map.size()];
        int idx = 0;
        for (int v : map.values()) {
            freq[idx++] = v;
        }

        int m = quantity.length;
        int fullMask = (1 << m) - 1;

        // precompute sum of quantities for every subset
        int[] sum = new int[1 << m];
        for (int mask = 1; mask <= fullMask; ++mask) {
            int lsb = Integer.numberOfTrailingZeros(mask);
            int prev = mask ^ (1 << lsb);
            sum[mask] = sum[prev] + quantity[lsb];
        }

        // DP over subsets
        boolean[] dp = new boolean[1 << m];
        dp[0] = true;

        for (int f : freq) {
            boolean[] ndp = dp.clone();
            for (int mask = 0; mask <= fullMask; ++mask) {
                if (!dp[mask]) continue;
                int remain = fullMask ^ mask;
                // iterate over non‑empty subsets of remaining customers
                for (int sub = remain; sub > 0; sub = (sub - 1) & remain) {
                    if (sum[sub] <= f) {
                        ndp[mask | sub] = true;
                    }
                }
            }
            dp = ndp;
        }

        return dp[fullMask];
    }
}
```

## Python

```python
class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        from collections import Counter

        freq = list(Counter(nums).values())
        m = len(quantity)
        full_mask = (1 << m) - 1

        # precompute sum of quantities for each subset mask
        subset_sum = [0] * (1 << m)
        for mask in range(1, 1 << m):
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)
            prev = mask ^ lsb
            subset_sum[mask] = subset_sum[prev] + quantity[idx]

        dp = [False] * (1 << m)
        dp[0] = True

        for f in freq:
            ndp = dp[:]  # copy current reachable states
            for mask in range(1 << m):
                if not dp[mask]:
                    continue
                remaining = full_mask ^ mask
                sub = remaining
                while sub:
                    if subset_sum[sub] <= f:
                        ndp[mask | sub] = True
                    sub = (sub - 1) & remaining
            dp = ndp

        return dp[full_mask]
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = list(Counter(nums).values())
        m = len(quantity)
        full_mask = (1 << m) - 1

        # precompute sum of quantities for each subset mask
        sum_qty = [0] * (1 << m)
        for mask in range(1, 1 << m):
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)
            sum_qty[mask] = sum_qty[mask ^ lsb] + quantity[idx]

        dp = [False] * (1 << m)
        dp[0] = True

        for f in freq:
            ndp = dp[:]
            for mask in range(1 << m):
                if not dp[mask]:
                    continue
                remaining = full_mask ^ mask
                sub = remaining
                while sub:
                    if sum_qty[sub] <= f:
                        ndp[mask | sub] = True
                    sub = (sub - 1) & remaining
            dp = ndp

        return dp[full_mask]
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

bool canDistribute(int* nums, int numsSize, int* quantity, int quantitySize) {
    if (quantitySize == 0) return true;
    
    // Count frequencies of each unique number
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int freq[55];
    int k = 0;
    for (int i = 0; i < numsSize; ) {
        int j = i;
        while (j < numsSize && nums[j] == nums[i]) ++j;
        freq[k++] = j - i;
        i = j;
    }
    
    int totalMasks = 1 << quantitySize;
    int *sumMask = (int *)malloc(totalMasks * sizeof(int));
    for (int mask = 0; mask < totalMasks; ++mask) {
        int s = 0;
        for (int i = 0; i < quantitySize; ++i)
            if (mask & (1 << i)) s += quantity[i];
        sumMask[mask] = s;
    }
    
    bool dp[1024] = {false};
    dp[0] = true;
    bool newdp[1024];
    
    for (int idx = 0; idx < k; ++idx) {
        int f = freq[idx];
        // copy current dp to newdp
        for (int m = 0; m < totalMasks; ++m) newdp[m] = dp[m];
        
        for (int mask = 0; mask < totalMasks; ++mask) {
            if (!dp[mask]) continue;
            int remaining = ((totalMasks - 1) ^ mask);
            // iterate over non‑empty submasks of remaining
            for (int sub = remaining; sub; sub = (sub - 1) & remaining) {
                if (sumMask[sub] <= f) {
                    newdp[mask | sub] = true;
                }
            }
        }
        // move newdp to dp
        for (int m = 0; m < totalMasks; ++m) dp[m] = newdp[m];
    }
    
    bool result = dp[totalMasks - 1];
    free(sumMask);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool CanDistribute(int[] nums, int[] quantity) {
        // Count frequencies of each unique number
        var freqMap = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!freqMap.ContainsKey(x)) freqMap[x] = 0;
            freqMap[x]++;
        }
        List<int> freqs = new List<int>(freqMap.Values);
        // Sort frequencies descending to improve pruning
        freqs.Sort((a, b) => b.CompareTo(a));

        int m = quantity.Length;
        int totalMask = 1 << m;

        // Precompute sum of quantities for every subset mask
        int[] subsetSum = new int[totalMask];
        for (int mask = 1; mask < totalMask; ++mask) {
            int lsb = mask & -mask;                     // lowest set bit
            int idx = BitOperations.TrailingZeroCount(lsb);
            subsetSum[mask] = subsetSum[mask ^ lsb] + quantity[idx];
        }

        int nFreq = freqs.Count;
        var dp = new int[nFreq, totalMask];
        for (int i = 0; i < nFreq; ++i)
            for (int j = 0; j < totalMask; ++j)
                dp[i, j] = -1; // unknown

        bool Dfs(int idx, int mask) {
            if (mask == 0) return true;
            if (idx == nFreq) return false;
            if (dp[idx, mask] != -1) return dp[idx, mask] == 1;

            int f = freqs[idx];
            // Iterate over all submasks of 'mask'
            for (int sub = mask; ; sub = (sub - 1) & mask) {
                if (subsetSum[sub] <= f) {
                    if (Dfs(idx + 1, mask ^ sub)) {
                        dp[idx, mask] = 1;
                        return true;
                    }
                }
                if (sub == 0) break;
            }

            dp[idx, mask] = 0;
            return false;
        }

        return Dfs(0, totalMask - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} quantity
 * @return {boolean}
 */
var canDistribute = function(nums, quantity) {
    const freqMap = new Map();
    for (const x of nums) {
        freqMap.set(x, (freqMap.get(x) || 0) + 1);
    }
    const freqs = Array.from(freqMap.values());
    
    const m = quantity.length;
    const fullMask = (1 << m) - 1;
    
    // quick check: total needed cannot exceed total available
    let totalNeed = 0;
    for (const q of quantity) totalNeed += q;
    if (totalNeed > nums.length) return false;
    
    // precompute sum of quantities for every subset mask
    const sumMask = new Array(1 << m).fill(0);
    for (let mask = 1; mask <= fullMask; ++mask) {
        let s = 0;
        for (let i = 0; i < m; ++i) {
            if ((mask >> i) & 1) s += quantity[i];
        }
        sumMask[mask] = s;
    }
    
    // dp[mask] == true if we can satisfy customers in 'mask' using processed frequencies
    let dp = new Array(1 << m).fill(false);
    dp[0] = true;
    
    for (const f of freqs) {
        const ndp = dp.slice(); // copy current states, we may add new ones
        for (let mask = 0; mask <= fullMask; ++mask) {
            if (!dp[mask]) continue;
            const remaining = fullMask ^ mask;
            // iterate over non‑empty submasks of remaining
            for (let sub = remaining; sub > 0; sub = (sub - 1) & remaining) {
                if (sumMask[sub] <= f) {
                    ndp[mask | sub] = true;
                }
            }
        }
        dp = ndp;
        if (dp[fullMask]) return true; // early success
    }
    
    return dp[fullMask];
};
```

## Typescript

```typescript
function canDistribute(nums: number[], quantity: number[]): boolean {
    const freqMap = new Map<number, number>();
    for (const v of nums) {
        freqMap.set(v, (freqMap.get(v) ?? 0) + 1);
    }
    const freqs = Array.from(freqMap.values());

    const m = quantity.length;
    const fullMask = (1 << m) - 1;

    // precompute sum of quantities for every subset mask
    const sumQty = new Array<number>(fullMask + 1).fill(0);
    for (let mask = 1; mask <= fullMask; ++mask) {
        const lowbit = mask & -mask;
        const idx = Math.round(Math.log2(lowbit));
        sumQty[mask] = sumQty[mask ^ lowbit] + quantity[idx];
    }

    let dp = new Array<boolean>(fullMask + 1).fill(false);
    dp[0] = true;

    for (const cnt of freqs) {
        const next = dp.slice();
        for (let mask = 0; mask <= fullMask; ++mask) {
            if (!dp[mask]) continue;
            let remaining = fullMask ^ mask;
            // iterate over all non‑empty submasks of remaining
            for (let sub = remaining; sub; sub = (sub - 1) & remaining) {
                if (sumQty[sub] <= cnt) {
                    next[mask | sub] = true;
                }
            }
        }
        dp = next;
    }

    return dp[fullMask];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $quantity
     * @return Boolean
     */
    function canDistribute($nums, $quantity) {
        // Count frequencies of each unique number
        $cnt = array_count_values($nums);
        $freqs = array_values($cnt); // list of frequencies

        $m = count($quantity);
        $fullMask = (1 << $m) - 1;

        // Precompute sum of quantities for every subset mask
        $subsetSum = array_fill(0, 1 << $m, 0);
        for ($mask = 1; $mask <= $fullMask; $mask++) {
            $sum = 0;
            for ($i = 0; $i < $m; $i++) {
                if ($mask & (1 << $i)) {
                    $sum += $quantity[$i];
                }
            }
            $subsetSum[$mask] = $sum;
        }

        // DP over subsets
        $dp = array_fill(0, 1 << $m, false);
        $dp[0] = true;

        foreach ($freqs as $f) {
            $newDp = $dp; // copy current states
            for ($mask = 0; $mask <= $fullMask; $mask++) {
                if (!$dp[$mask]) continue;
                $remaining = $fullMask ^ $mask; // customers not yet satisfied
                // iterate over all non‑empty subsets of remaining
                for ($sub = $remaining; $sub > 0; $sub = ($sub - 1) & $remaining) {
                    if ($subsetSum[$sub] <= $f) {
                        $newDp[$mask | $sub] = true;
                    }
                }
            }
            $dp = $newDp;
        }

        return $dp[$fullMask];
    }
}
```

## Swift

```swift
class Solution {
    func canDistribute(_ nums: [Int], _ quantity: [Int]) -> Bool {
        // Count frequencies of each unique number
        var freqDict = [Int:Int]()
        for num in nums {
            freqDict[num, default: 0] += 1
        }
        let freqs = Array(freqDict.values)
        
        let m = quantity.count
        let fullMask = (1 << m) - 1
        let maxMask = 1 << m
        
        // Precompute sum of quantities for every subset mask
        var subsetSum = [Int](repeating: 0, count: maxMask)
        if m > 0 {
            for mask in 1..<maxMask {
                let lowbit = mask & -mask
                let idx = lowbit.trailingZeroBitCount
                subsetSum[mask] = subsetSum[mask ^ lowbit] + quantity[idx]
            }
        }
        
        var dp = [Bool](repeating: false, count: maxMask)
        dp[0] = true
        
        for f in freqs {
            var newDP = dp
            for mask in 0..<maxMask where dp[mask] {
                let remaining = fullMask ^ mask
                var sub = remaining
                while sub > 0 {
                    if subsetSum[sub] <= f {
                        newDP[mask | sub] = true
                    }
                    sub = (sub - 1) & remaining
                }
            }
            dp = newDP
        }
        
        return dp[fullMask]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canDistribute(nums: IntArray, quantity: IntArray): Boolean {
        val m = quantity.size
        val fullMask = (1 shl m) - 1

        // precompute sum of quantities for each subset mask
        val subsetSum = IntArray(1 shl m)
        for (mask in 1 until (1 shl m)) {
            val lsb = mask and -mask
            val idx = Integer.numberOfTrailingZeros(lsb)
            subsetSum[mask] = subsetSum[mask xor lsb] + quantity[idx]
        }

        // count frequencies of each unique number
        val freqMap = HashMap<Int, Int>()
        for (num in nums) {
            freqMap[num] = (freqMap[num] ?: 0) + 1
        }
        val freqs = freqMap.values.toIntArray()

        var dp = BooleanArray(1 shl m)
        dp[0] = true

        for (f in freqs) {
            val ndp = dp.clone()
            for (mask in 0..fullMask) {
                if (!dp[mask]) continue
                val remaining = fullMask xor mask
                var sub = remaining
                while (sub > 0) {
                    if (subsetSum[sub] <= f) {
                        ndp[mask or sub] = true
                    }
                    sub = (sub - 1) and remaining
                }
            }
            dp = ndp
        }

        return dp[fullMask]
    }
}
```

## Dart

```dart
class Solution {
  bool canDistribute(List<int> nums, List<int> quantity) {
    // Count frequencies of each distinct number.
    final Map<int, int> freqMap = {};
    for (final x in nums) {
      freqMap[x] = (freqMap[x] ?? 0) + 1;
    }
    final List<int> freqs = freqMap.values.toList();

    final int m = quantity.length;
    final int totalMask = 1 << m;

    // Precompute sum of quantities for every subset of customers.
    final List<int> subsetSum = List.filled(totalMask, 0);
    for (int mask = 1; mask < totalMask; ++mask) {
      final int lowBit = mask & -mask;
      final int idx = lowBit.bitLength - 1; // position of the bit
      subsetSum[mask] = subsetSum[mask ^ lowBit] + quantity[idx];
    }

    List<bool> dp = List.filled(totalMask, false);
    dp[0] = true;

    for (final f in freqs) {
      final List<bool> ndp = List.from(dp);
      for (int mask = 0; mask < totalMask; ++mask) {
        if (!dp[mask]) continue;
        final int remaining = (totalMask - 1) ^ mask;
        // Iterate over all non‑empty subsets of the remaining customers.
        for (int sub = remaining; sub > 0; sub = (sub - 1) & remaining) {
          if (subsetSum[sub] <= f) {
            ndp[mask | sub] = true;
          }
        }
      }
      dp = ndp;
    }

    return dp[totalMask - 1];
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func canDistribute(nums []int, quantity []int) bool {
	// Count frequencies of each unique number
	freqMap := make(map[int]int)
	for _, v := range nums {
		freqMap[v]++
	}
	freqs := make([]int, 0, len(freqMap))
	for _, c := range freqMap {
		freqs = append(freqs, c)
	}

	m := len(quantity)
	if m == 0 {
		return true
	}
	fullMask := (1 << m) - 1

	// Precompute total quantity needed for each subset mask
	need := make([]int, 1<<m)
	for mask := 1; mask <= fullMask; mask++ {
		lowbit := mask & -mask
		idx := bits.TrailingZeros(uint(lowbit))
		need[mask] = need[mask^lowbit] + quantity[idx]
	}

	dp := make([]bool, 1<<m)
	dp[0] = true

	for _, f := range freqs {
		next := make([]bool, 1<<m)
		copy(next, dp) // keep states where we don't use this frequency
		for mask := 0; mask <= fullMask; mask++ {
			if !dp[mask] {
				continue
			}
			remain := fullMask ^ mask
			sub := remain
			for sub > 0 {
				if need[sub] <= f {
					next[mask|sub] = true
				}
				sub = (sub - 1) & remain
			}
		}
		dp = next
	}

	return dp[fullMask]
}
```

## Ruby

```ruby
def can_distribute(nums, quantity)
  freq_hash = Hash.new(0)
  nums.each { |x| freq_hash[x] += 1 }
  freqs = freq_hash.values

  m = quantity.length
  full_mask = (1 << m) - 1

  return false if quantity.sum > nums.size

  # precompute sum of quantities for every subset mask
  subset_sum = Array.new(1 << m, 0)
  (0...(1 << m)).each do |mask|
    total = 0
    m.times do |i|
      total += quantity[i] if (mask >> i) & 1 == 1
    end
    subset_sum[mask] = total
  end

  dp = Array.new(1 << m, false)
  dp[0] = true

  freqs.each do |f|
    prev = dp.clone
    (0..full_mask).each do |mask|
      next unless prev[mask]
      remaining = full_mask ^ mask
      sub = remaining
      while sub > 0
        if subset_sum[sub] <= f
          dp[mask | sub] = true
        end
        sub = (sub - 1) & remaining
      end
    end
    return true if dp[full_mask]
  end

  dp[full_mask]
end
```

## Scala

```scala
object Solution {
  def canDistribute(nums: Array[Int], quantity: Array[Int]): Boolean = {
    import scala.collection.mutable
    val countMap = mutable.Map[Int, Int]()
    for (num <- nums) {
      countMap(num) = countMap.getOrElse(num, 0) + 1
    }
    val freqs = countMap.values.toArray
    val m = quantity.length
    val totalMask = (1 << m) - 1

    // precompute sum of quantities for each subset mask
    val sumQuant = new Array[Int](1 << m)
    for (mask <- 1 to totalMask) {
      val lsb = mask & -mask
      val idx = Integer.numberOfTrailingZeros(lsb)
      sumQuant(mask) = sumQuant(mask ^ lsb) + quantity(idx)
    }

    var dp = new Array[Boolean](1 << m)
    dp(0) = true

    for (f <- freqs) {
      val ndp = dp.clone()
      for (mask <- 0 to totalMask if dp(mask)) {
        var remaining = totalMask ^ mask
        var sub = remaining
        while (sub != 0) {
          if (sumQuant(sub) <= f) {
            ndp(mask | sub) = true
          }
          sub = (sub - 1) & remaining
        }
      }
      dp = ndp
    }

    dp(totalMask)
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn can_distribute(nums: Vec<i32>, quantity: Vec<i32>) -> bool {
        // Count frequencies of each unique number
        let mut freq_map: HashMap<i32, usize> = HashMap::new();
        for num in nums {
            *freq_map.entry(num).or_insert(0) += 1;
        }
        let freqs: Vec<usize> = freq_map.values().cloned().collect();

        let m = quantity.len();
        let full_mask: usize = (1 << m) - 1;

        // Precompute sum of quantities for every subset
        let mut subset_sum = vec![0usize; 1 << m];
        for mask in 1..(1 << m) {
            let lowbit = mask & (!mask + 1);
            let idx = lowbit.trailing_zeros() as usize;
            let prev = mask ^ lowbit;
            subset_sum[mask] = subset_sum[prev] + quantity[idx] as usize;
        }

        // DP over subsets
        let mut dp = vec![false; 1 << m];
        dp[0] = true;

        for &f in freqs.iter() {
            let mut ndp = dp.clone();
            for mask in 0..(1 << m) {
                if !dp[mask] {
                    continue;
                }
                // remaining customers not yet satisfied
                let mut sub = (!mask) & full_mask;
                while sub > 0 {
                    if subset_sum[sub] <= f {
                        ndp[mask | sub] = true;
                    }
                    sub = (sub - 1) & ((!mask) & full_mask);
                }
            }
            dp = ndp;
        }

        dp[full_mask]
    }
}
```

## Racket

```racket
(define (can-distribute nums quantity)
  (let* ((freq-hash (make-hash))
         (add-count
          (lambda (x)
            (hash-update! freq-hash x (lambda (v) (+ v 1)) 0))))
    (for-each add-count nums)
    (define freqs (hash-values freq-hash))
    (define m (length quantity))
    (define allMask (sub1 (arithmetic-shift 1 m))) ; 2^m - 1

    ;; precompute sum of quantities for each subset mask
    (define sums (make-vector (add1 allMask) 0))
    (for ([mask (in-range (add1 allMask))])
      (let ((sum 0))
        (for ([i (in-range m)])
          (when (not (zero? (bitwise-and mask (arithmetic-shift 1 i))))
            (set! sum (+ sum (list-ref quantity i)))))
        (vector-set! sums mask sum)))

    ;; DP over masks
    (define cur (make-vector (add1 allMask) #f))
    (vector-set! cur 0 #t)

    (for ([freq freqs])
      (define next (vector-copy cur)) ; copy current states
      (for ([mask (in-range (add1 allMask))]
            #:when (vector-ref cur mask))
        (for ([sub (in-range 1 (add1 allMask))])
          (when (and (= (bitwise-and mask sub) 0)
                     (<= (vector-ref sums sub) freq))
            (vector-set! next (bitwise-ior mask sub) #t))))
      (set! cur next))

    (vector-ref cur allMask)))
```

## Erlang

```erlang
-spec can_distribute([integer()], [integer()]) -> boolean().
can_distribute(Nums, Quantity) ->
    FreqMap = lists:foldl(fun(N, Acc) ->
        maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
    end, #{}, Nums),
    Frequencies = maps:values(FreqMap),
    M = length(Quantity),
    FullMask = (1 bsl M) - 1,
    SumTuple = precompute_sums(Quantity, M),
    Size = FullMask + 1,
    DP0 = erlang:make_tuple(Size, false),
    DPInit = set_elem(DP0, 0, true),
    FinalDP = lists:foldl(fun(Freq, DpAcc) ->
        update_dp(Freq, DpAcc, SumTuple, FullMask)
    end, DPInit, Frequencies),
    get_elem(FinalDP, FullMask).

precompute_sums(Qty, M) ->
    Full = (1 bsl M) - 1,
    Tuple0 = erlang:make_tuple(Full + 1, 0),
    lists:foldl(fun(Mask, Acc) ->
        Sum = mask_sum(Qty, Mask),
        set_elem(Acc, Mask, Sum)
    end, Tuple0, lists:seq(0, Full)).

mask_sum(Qty, Mask) -> mask_sum(Qty, Mask, 0, 0).

mask_sum(_Qty, 0, _Idx, Acc) -> Acc;
mask_sum(Qty, Mask, Idx, Acc) ->
    Bit = Mask band 1,
    NewAcc = if Bit =:= 1 -> Acc + lists:nth(Idx + 1, Qty); true -> Acc end,
    mask_sum(Qty, Mask bsr 1, Idx + 1, NewAcc).

update_dp(Freq, DpPrev, SumTuple, FullMask) ->
    lists:foldl(fun(Mask, DpAcc) ->
        case get_elem(DpPrev, Mask) of
            true ->
                Rem = FullMask band bnot Mask,
                SubMasks = submasks(Rem),
                lists:foldl(fun(Sub, DpInner) ->
                    Sum = get_elem(SumTuple, Sub),
                    if Sum =< Freq -> set_elem(DpInner, Mask bor Sub, true); true -> DpInner end
                end, DpAcc, SubMasks);
            false -> DpAcc
        end
    end, DpPrev, lists:seq(0, FullMask)).

submasks(Rem) -> submasks(Rem, Rem, []).

submasks(_Orig, 0, Acc) -> Acc;
submasks(Orig, Sub, Acc) ->
    submasks(Orig, (Sub - 1) band Orig, [Sub | Acc]).

set_elem(Tuple, Index, Value) ->
    setelement(Index + 1, Tuple, Value).

get_elem(Tuple, Index) ->
    element(Index + 1, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_distribute(nums :: [integer], quantity :: [integer]) :: boolean
  def can_distribute(nums, quantity) do
    import Bitwise

    # frequencies of each distinct number
    freqs = nums |> Enum.frequencies() |> Map.values()

    m = length(quantity)
    total_masks = 1 <<< m

    # precompute sum of quantities for every subset mask
    sums =
      Enum.map(0..total_masks - 1, fn mask ->
        Enum.reduce(0..m - 1, 0, fn i, acc ->
          if (mask >>> i) &&& 1 == 1 do
            acc + Enum.at(quantity, i)
          else
            acc
          end
        end)
      end)

    # DP over subsets using a set of reachable masks
    reachable = MapSet.new([0])

    Enum.reduce(freqs, reachable, fn f, cur_set ->
      next_set =
        Enum.reduce(cur_set, MapSet.new(), fn mask, acc ->
          Enum.reduce(0..total_masks - 1, acc, fn submask, a ->
            if (mask &&& submask) == 0 and Enum.at(sums, submask) <= f do
              MapSet.put(a, mask ||| submask)
            else
              a
            end
          end)
        end)

      # also keep the previous reachable masks (skip using this frequency)
      MapSet.union(cur_set, next_set)
    end)
    |> MapSet.member?(total_masks - 1)
  end
end
```
