# 3583. Count Special Triplets

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1'000'000'007;
    struct BIT {
        int n;
        vector<int> bit;
        BIT(int n): n(n), bit(n+1,0) {}
        void add(int idx, long long val){
            for(++idx; idx<=n; idx+=idx&-idx){
                int cur = bit[idx];
                int nv = (cur + val) % MOD;
                if(nv<0) nv+=MOD;
                bit[idx]=nv;
            }
        }
        long long sumPrefix(int idx){
            long long res=0;
            for(++idx; idx>0; idx-=idx&-idx){
                res += bit[idx];
                if(res>=MOD) res-=MOD;
            }
            return res;
        }
        long long rangeSum(int l, int r){
            if(l>r) return 0;
            long long ans = sumPrefix(r);
            if(l>0){
                ans -= sumPrefix(l-1);
                if(ans<0) ans+=MOD;
            }
            return ans;
        }
    };
    
    int specialTriplets(vector<int>& nums) {
        int n = nums.size();
        int maxVal = 0;
        for(int v: nums) if(v>maxVal) maxVal=v;
        vector<int> left(maxVal+1,0), right(maxVal+1,0);
        for(int v: nums) right[v]++;
        BIT bit(maxVal+2);
        long long ans=0;
        for(int j=0;j<n;++j){
            int x = nums[j];
            // remove current from right side
            long long oldProd = 1LL*left[x]*right[x]%MOD;
            right[x]--;
            long long newProd = 1LL*left[x]*right[x]%MOD;
            bit.add(x, (newProd - oldProd + MOD)%MOD);
            
            // query contributions for values >= nums[j]
            ans += bit.rangeSum(x, maxVal);
            if(ans>=MOD) ans-=MOD;
            
            // add current to left side
            oldProd = 1LL*left[x]*right[x]%MOD;
            left[x]++;
            newProd = 1LL*left[x]*right[x]%MOD;
            bit.add(x, (newProd - oldProd + MOD)%MOD);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static class Fenwick {
        private final long[] tree;
        private final int n;
        Fenwick(int n) {
            this.n = n;
            this.tree = new long[n + 2];
        }
        void add(int idx, long delta) {
            // idx is value (0..max), shift by +1 for 1-indexed BIT
            for (int i = idx + 1; i <= n + 1; i += i & -i) {
                tree[i] += delta;
            }
        }
        long sumPrefix(int idx) { // sum of [0, idx]
            long res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i) {
                res += tree[i];
            }
            return res;
        }
        long rangeSum(int l, int r) { // inclusive
            if (l > r) return 0;
            return sumPrefix(r) - (l == 0 ? 0 : sumPrefix(l - 1));
        }
    }

    public int specialTriplets(int[] nums) {
        final long MOD = 1_000_000_007L;
        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;

        int[] totalFreq = new int[maxVal + 1];
        for (int v : nums) totalFreq[v]++;

        int[] prevCnt = new int[maxVal + 1];
        int[] nextCnt = totalFreq.clone();

        Fenwick bit = new Fenwick(maxVal + 1); // stores prevCnt[v] * nextCnt[v]

        long ans = 0;
        for (int v : nums) {
            int a = prevCnt[v];          // current prev count
            int bOld = nextCnt[v];       // includes current position

            // remove current element from future side
            bit.add(v, -a);              // product changes by -a
            nextCnt[v]--;                // now bNew = bOld - 1

            // contribution for this middle index
            long contrib = bit.rangeSum(v, maxVal);
            ans += contrib;
            if (ans >= MOD) ans -= MOD;

            int bNew = nextCnt[v];
            // add current element to past side
            bit.add(v, bNew);            // product changes by +bNew
            prevCnt[v]++;
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        if not nums:
            return 0
        max_val = max(nums)
        size = max_val + 2

        # Fenwick Tree for sum of products cntPrev[v] * cntNext[v]
        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, idx, delta):
                i = idx + 1
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i

            def query(self, idx):
                # sum of [0..idx]
                if idx < 0:
                    return 0
                i = idx + 1
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

        cntPrev = [0] * (max_val + 1)
        cntNext = [0] * (max_val + 1)
        for v in nums:
            cntNext[v] += 1

        bit = BIT(size)
        total_pairs = 0
        ans = 0

        for val in nums:
            # move current element from future to middle (remove from cntNext)
            delta_remove = -cntPrev[val]          # product decreases by cntPrev[val]
            cntNext[val] -= 1
            total_pairs += delta_remove
            bit.add(val, delta_remove)

            # contribution for this j
            less_sum = bit.query(val - 1)         # sum of products for values < val
            ans = (ans + (total_pairs - less_sum)) % MOD

            # add current element to cntPrev (it becomes part of left side)
            delta_add = cntNext[val]              # product increases by cntNext[val]
            cntPrev[val] += 1
            total_pairs += delta_add
            bit.add(val, delta_add)

        return ans % MOD
```

## Python3

```python
class Solution:
    def specialTriplets(self, nums):
        from collections import Counter
        MOD = 10**9 + 7
        after = Counter(nums)
        before = Counter()
        ans = 0
        for x in nums:
            after[x] -= 1
            if after[x] == 0:
                del after[x]
            # contribution: sum over each value v of before[v] * after[v]
            # iterate over smaller dict to keep O(n)
            if len(before) < len(after):
                for v, cnt_before in before.items():
                    cnt_after = after.get(v, 0)
                    if cnt_after:
                        ans += cnt_before * cnt_after
            else:
                for v, cnt_after in after.items():
                    cnt_before = before.get(v, 0)
                    if cnt_before:
                        ans += cnt_before * cnt_after
            ans %= MOD
            before[x] += 1
        return ans % MOD
```

## C

```c
#include <stdlib.h>

int specialTriplets(int* nums, int numsSize) {
    const int MOD = 1000000007;
    // Determine maximum value to size frequency arrays
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    int freqSize = maxVal + 1;
    int *freqPrev = (int*)calloc(freqSize, sizeof(int));
    int *freqNext = (int*)calloc(freqSize, sizeof(int));
    
    // Build initial next frequencies
    for (int i = 0; i < numsSize; ++i) {
        freqNext[nums[i]]++;
    }
    
    long long totalPairs = 0;   // sum over v of prev[v] * next[v]
    long long ans = 0;
    
    for (int idx = 0; idx < numsSize; ++idx) {
        int x = nums[idx];
        // move current element from next to the middle position
        freqNext[x]--;
        totalPairs -= (long long)freqPrev[x];   // prev[x] * next[x] decreased by prev[x]
        
        if (totalPairs < 0) totalPairs = 0; // safety, though shouldn't be negative
        
        ans += totalPairs;
        if (ans >= MOD) ans %= MOD;
        
        // add current element to prev side
        freqPrev[x]++;
        totalPairs += (long long)freqNext[x];   // prev[x] increased, product grows by next[x]
    }
    
    free(freqPrev);
    free(freqNext);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
public class Solution {
    public int SpecialTriplets(int[] nums) {
        const int MOD = 1000000007;
        int n = nums.Length;
        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;
        int size = maxVal + 1;
        long[] prev = new long[size];
        long[] next = new long[size];
        foreach (int v in nums) next[v]++;
        long total = 0;
        long ans = 0;
        for (int idx = 0; idx < n; idx++) {
            int val = nums[idx];
            // move current element from future to middle
            next[val]--;
            total -= prev[val]; // remove contributions involving this value as right end
            if (total < 0) total += MOD; // keep non-negative for modulo safety (though we use long)
            ans = (ans + total) % MOD;
            // move current element to past
            prev[val]++;
            total += next[val];
        }
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var specialTriplets = function(nums) {
    const MOD = 1000000007;
    const freqPrev = new Map();
    const freqNext = new Map();
    
    for (const x of nums) {
        freqNext.set(x, (freqNext.get(x) || 0) + 1);
    }
    
    let ans = 0;
    for (let j = 0; j < nums.length; ++j) {
        const cur = nums[j];
        // move cur from next to current
        const cntNext = freqNext.get(cur);
        if (cntNext === 1) freqNext.delete(cur);
        else freqNext.set(cur, cntNext - 1);
        
        const target = cur * 2;
        const left = freqPrev.get(target) || 0;
        const right = freqNext.get(target) || 0;
        ans = (ans + left * right) % MOD;
        
        // add cur to prev
        freqPrev.set(cur, (freqPrev.get(cur) || 0) + 1);
    }
    
    return ans;
};
```

## Typescript

```typescript
function specialTriplets(nums: number[]): number {
    const MOD = 1_000_000_007;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    const next = new Array(maxVal + 1).fill(0);
    for (const v of nums) next[v]++;

    const prev = new Array(maxVal + 1).fill(0);
    let totalPairs = 0;
    let ans = 0;

    for (const val of nums) {
        // move current element from right side to middle
        totalPairs -= prev[val];
        next[val]--;

        // add contributions where this index is the middle one
        ans += totalPairs;
        if (ans >= MOD) ans %= MOD;

        // now move current element to left side for future middles
        totalPairs += next[val];
        prev[val]++;
    }

    return ans % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function specialTriplets($nums) {
        $mod = 1000000007;
        $maxVal = 0;
        foreach ($nums as $v) {
            if ($v > $maxVal) $maxVal = $v;
        }
        // frequency arrays
        $cntPrev = array_fill(0, $maxVal + 1, 0);
        $cntNext = array_fill(0, $maxVal + 1, 0);
        foreach ($nums as $v) {
            $cntNext[$v]++;
        }

        $totalPairs = 0;
        $ans = 0;

        foreach ($nums as $x) {
            // move current element from next to middle
            $cntNext[$x]--;
            // remove pairs that lose this element as a possible k
            $totalPairs -= $cntPrev[$x];
            if ($totalPairs < 0) $totalPairs += $mod; // keep non‑negative for modulo ops

            // add contribution for current j
            $ans = ($ans + $totalPairs) % $mod;

            // now current element becomes part of the left side for future j's
            $totalPairs += $cntNext[$x];
            if ($totalPairs >= $mod) $totalPairs -= $mod;
            $cntPrev[$x]++;
        }

        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func specialTriplets(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var maxVal = 0
        for v in nums { if v > maxVal { maxVal = v } }
        var next = Array(repeating: 0, count: maxVal + 1)
        for v in nums { next[v] += 1 }
        var prev = Array(repeating: 0, count: maxVal + 1)
        var total: Int64 = 0
        var ans: Int64 = 0
        
        for x in nums {
            // remove current from next side
            next[x] -= 1
            // adjust total because contribution of value x decreased by prev[x]
            total -= Int64(prev[x])
            
            // add current total to answer
            ans += total
            if ans >= Int64(mod) { ans %= Int64(mod) }
            
            // move current element to prev side, increasing contribution by next[x]
            total += Int64(next[x])
            prev[x] += 1
        }
        return Int(ans % Int64(mod))
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private const val MOD = 1_000_000_007L

    private class BIT(private val size: Int) {
        private val tree = LongArray(size + 2)
        fun add(idx0: Int, delta: Long) {
            var idx = idx0
            var d = (delta % MOD + MOD) % MOD
            while (idx <= size) {
                tree[idx] = (tree[idx] + d) % MOD
                idx += idx and -idx
            }
        }
        fun sum(idx0: Int): Long {
            var idx = idx0
            var res = 0L
            while (idx > 0) {
                res = (res + tree[idx]) % MOD
                idx -= idx and -idx
            }
            return res
        }
        fun rangeSum(l: Int, r: Int): Long {
            if (l > r) return 0L
            var res = (sum(r) - sum(l - 1)) % MOD
            if (res < 0) res += MOD
            return res
        }
    }

    fun specialTriplets(nums: IntArray): Int {
        val n = nums.size
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v
        val freqPrev = IntArray(maxVal + 1)
        val freqNext = IntArray(maxVal + 1)
        for (v in nums) freqNext[v]++

        val bit = BIT(maxVal + 2) // 1-indexed, store contribution cntPrev[v]*cntNext[v]

        var ans = 0L
        for (j in 0 until n) {
            val v = nums[j]
            // remove current from next side
            var oldContrib = freqPrev[v].toLong() * freqNext[v]
            freqNext[v]--
            var newContrib = freqPrev[v].toLong() * freqNext[v]
            bit.add(v + 1, newContrib - oldContrib)

            // query contributions for values greater than current value
            val add = bit.rangeSum(v + 2, maxVal + 1)
            ans += add
            if (ans >= MOD) ans -= MOD

            // add current to prev side
            oldContrib = freqPrev[v].toLong() * freqNext[v]
            freqPrev[v]++
            newContrib = freqPrev[v].toLong() * freqNext[v]
            bit.add(v + 1, newContrib - oldContrib)
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  int specialTriplets(List<int> nums) {
    int n = nums.length;
    int maxVal = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }
    int limit = maxVal * 2 + 1;
    List<int> left = List.filled(limit, 0);
    List<int> right = List.filled(limit, 0);
    for (int v in nums) {
      right[v]++;
    }

    int ans = 0;
    for (int j = 0; j < n; ++j) {
      int val = nums[j];
      right[val]--;
      int target = val * 2;
      if (target < limit) {
        ans = (ans + left[target] * right[target]) % _mod;
      }
      left[val]++;
    }
    return ans;
  }
}
```

## Golang

```go
func specialTriplets(nums []int) int {
	const MOD int64 = 1000000007
	type pair struct{ cnt, sum int64 }
	freqCnt := make(map[int]int64)
	freqSum := make(map[int]int64)

	var ans int64
	for idx, v := range nums {
		if c := freqCnt[v]; c > 0 {
			contrib := c*int64(idx-1) - freqSum[v]
			ans += contrib
			if ans >= MOD {
				ans %= MOD
			}
		}
		freqCnt[v]++
		freqSum[v] += int64(idx)
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
def special_triplets(nums)
  mod = 1_000_000_007
  last_idx = {}
  ans = 0
  nums.each_with_index do |v, i|
    if (prev = last_idx[v])
      ans += 1 if i - prev > 1
      ans -= mod if ans >= mod
    end
    last_idx[v] = i
  end
  ans % mod
end
```

## Scala

```scala
object Solution {
    def specialTriplets(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        if (nums.isEmpty) return 0
        val maxVal = nums.max
        val size = maxVal + 2 // for BIT indexing (value+1)
        class Fenwick(n: Int) {
            private val tree = new Array[Long](n + 2)
            def add(idx0: Int, delta: Long): Unit = {
                var i = idx0
                while (i <= n) {
                    tree(i) += delta
                    i += i & -i
                }
            }
            def sum(idx0: Int): Long = {
                var res = 0L
                var i = idx0
                while (i > 0) {
                    res += tree(i)
                    i -= i & -i
                }
                res
            }
            def rangeSum(l: Int, r: Int): Long = {
                if (l > r) 0L else sum(r) - sum(l - 1)
            }
        }

        val freqPrev = new Array[Long](maxVal + 1)
        val freqNext = new Array[Long](maxVal + 1)
        for (v <- nums) {
            freqNext(v) += 1
        }

        val bit = new Fenwick(maxVal + 2)

        var ans = 0L

        for (j <- nums.indices) {
            val v = nums(j)
            // remove current element from future counts
            freqNext(v) -= 1
            // update BIT: product[v] decreases by freqPrev[v]
            bit.add(v + 1, -freqPrev(v))

            // query sum of products for values greater than v
            val contrib = bit.rangeSum(v + 2, maxVal + 1)
            ans += contrib
            if (ans >= MOD) ans %= MOD

            // add current element to previous counts
            // update BIT: product[v] increases by freqNext[v]
            bit.add(v + 1, freqNext(v))
            freqPrev(v) += 1
        }

        ((ans % MOD).toInt)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        if n < 3 { return 0; }

        // freq of values to the right of current index
        let mut right: HashMap<i32, i64> = HashMap::new();
        for &v in &nums {
            *right.entry(v).or_insert(0) += 1;
        }

        let mut left: HashMap<i32, i64> = HashMap::new();
        let mut ans: i64 = 0;

        // iterate j as middle element
        for (j, &mid) in nums.iter().enumerate() {
            // move current mid from right to left
            *right.get_mut(&mid).unwrap() -= 1;
            if *right.get(&mid).unwrap() == 0 { right.remove(&mid); }

            // count contributions: number of i<j with value v > mid
            // times number of k>j with same value v
            for (&v, &cnt_left) in left.iter() {
                if v > mid {
                    if let Some(&cnt_right) = right.get(&v) {
                        ans = (ans + cnt_left * cnt_right) % MOD;
                    }
                }
            }

            // add current mid to left frequencies
            *left.entry(mid).or_insert(0) += 1;
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (special-triplets nums)
  (let* ([n (length nums)]
         [next-hash (make-hash)])
    ;; build frequency of all elements
    (for ([v nums])
      (hash-set! next-hash v (+ (hash-ref next-hash v 0) 1)))
    (define prev-hash (make-hash))
    (define cur 0)
    (define ans 0)
    (for ([v nums])
      ;; move current element from next to processing
      (let* ([next-count (hash-ref next-hash v)])
        (hash-set! next-hash v (- next-count 1)))
      ;; update cur because cntNext[v] decreased by 1
      (set! cur (- cur (hash-ref prev-hash v 0)))
      ;; add current contribution to answer
      (set! ans (modulo (+ ans cur) MOD))
      ;; now include current element into prev
      (let ([prev-count (hash-ref prev-hash v 0)]
            [next-count-after (hash-ref next-hash v 0)])
        (hash-set! prev-hash v (+ prev-count 1))
        ;; update cur because cntPrev[v] increased by 1
        (set! cur (+ cur next-count-after))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([special_triplets/1]).

-define(MOD, 1000000007).

special_triplets(Nums) ->
    NextMap = build_counts(Nums, #{}),
    process(Nums, NextMap, #{}, 0, 0).

build_counts([], Map) -> Map;
build_counts([H|T], Map) ->
    Count = maps:get(H, Map, 0),
    build_counts(T, maps:put(H, Count + 1, Map)).

process([], _Next, _Prev, _Total, Ans) ->
    Ans rem ?MOD;
process([X|Rest], NextMap, PrevMap, Total, Ans) ->
    PrevCount = maps:get(X, PrevMap, 0),
    NextCount = maps:get(X, NextMap),
    NewNextCount = NextCount - 1,
    NextMap2 = if
        NewNextCount == 0 -> maps:remove(X, NextMap);
        true -> maps:put(X, NewNextCount, NextMap)
    end,
    Total1 = Total - PrevCount,
    Ans1 = (Ans + (Total1 rem ?MOD)) rem ?MOD,
    Total2 = Total1 + NewNextCount,
    PrevMap2 = maps:put(X, PrevCount + 1, PrevMap),
    process(Rest, NextMap2, PrevMap2, Total2, Ans1).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec special_triplets(nums :: [integer]) :: integer
  def special_triplets(nums) do
    mod = 1_000_000_007
    n = length(nums)
    nums_t = List.to_tuple(nums)

    # previous less element indices, -1 if none
    ple = compute_prev_less(nums_t, n)
    # next less element indices, n if none
    nle = compute_next_less(nums_t, n)

    # map value -> tuple of sorted positions
    pos_map =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        v = elem(nums_t, i)
        Map.update(acc, v, [i], &[i | &1])
      end)
      |> Enum.map(fn {k, lst} -> {k, List.to_tuple(Enum.reverse(lst))} end)
      |> Map.new()

    ans =
      Enum.reduce(0..(n - 1), 0, fn j, acc ->
        v = elem(nums_t, j)
        left_limit = :array.get(j, ple) + 1
        right_limit = :array.get(j, nle) - 1

        positions = Map.fetch!(pos_map, v)

        left_cnt =
          if left_limit <= j - 1 do
            count_in_range(positions, left_limit, j - 1)
          else
            0
          end

        right_cnt =
          if j + 1 <= right_limit do
            count_in_range(positions, j + 1, right_limit)
          else
            0
          end

        (acc + left_cnt * right_cnt) |> rem(mod)
      end)

    ans
  end

  # previous less element index for each position
  defp compute_prev_less(nums_t, n) do
    ple = :array.new(n, default: -1)

    {ple_arr, _stack} =
      Enum.reduce(0..(n - 1), {ple, []}, fn i, {arr, stack} ->
        val = elem(nums_t, i)
        new_stack = pop_while(stack, fn idx -> elem(nums_t, idx) >= val end)

        ple_idx = if new_stack == [], do: -1, else: hd(new_stack)
        arr = :array.set(i, ple_idx, arr)
        {arr, [i | new_stack]}
      end)

    ple_arr
  end

  # next less element index for each position
  defp compute_next_less(nums_t, n) do
    nle = :array.new(n, default: n)

    {nle_arr, _stack} =
      Enum.reduce((0..(n - 1)) |> Enum.reverse(), {nle, []}, fn i, {arr, stack} ->
        val = elem(nums_t, i)
        new_stack = pop_while(stack, fn idx -> elem(nums_t, idx) >= val end)

        nle_idx = if new_stack == [], do: n, else: hd(new_stack)
        arr = :array.set(i, nle_idx, arr)
        {arr, [i | new_stack]}
      end)

    nle_arr
  end

  defp pop_while([], _cond), do: []
  defp pop_while([h | t] = stack, cond) when is_function(cond, 1) do
    if cond.(h), do: pop_while(t, cond), else: stack
  end

  # count positions in sorted tuple within [l, r]
  defp count_in_range(pos_tuple, l, r) when l > r, do: 0
  defp count_in_range(pos_tuple, l, r) do
    size = tuple_size(pos_tuple)
    left = lower_bound(pos_tuple, size, l)
    right = upper_bound(pos_tuple, size, r)
    max(right - left, 0)
  end

  # first index with value >= target
  defp lower_bound(_tup, size, _target) when size == 0, do: 0
  defp lower_bound(tup, size, target) do
    lb(0, size, tup, target)
  end

  defp lb(low, high, tup, target) when low < high do
    mid = div(low + high, 2)
    val = elem(tup, mid)

    if val < target do
      lb(mid + 1, high, tup, target)
    else
      lb(low, mid, tup, target)
    end
  end

  defp lb(low, _high, _tup, _target), do: low

  # first index with value > target
  defp upper_bound(_tup, size, _target) when size == 0, do: 0
  defp upper_bound(tup, size, target) do
    ub(0, size, tup, target)
  end

  defp ub(low, high, tup, target) when low < high do
    mid = div(low + high, 2)
    val = elem(tup, mid)

    if val <= target do
      ub(mid + 1, high, tup, target)
    else
      ub(low, mid, tup, target)
    end
  end

  defp ub(low, _high, _tup, _target), do: low
end
```
