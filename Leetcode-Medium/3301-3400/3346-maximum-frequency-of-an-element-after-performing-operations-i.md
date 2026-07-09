# 3346. Maximum Frequency of an Element After Performing Operations I

## Cpp

```cpp
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        sort(nums.begin(), nums.end());
        vector<int> vals;
        vector<int> cnts;
        for (int x : nums) {
            if (vals.empty() || vals.back() != x) {
                vals.push_back(x);
                cnts.push_back(1);
            } else {
                ++cnts.back();
            }
        }
        int m = vals.size();
        vector<long long> pref(m + 1, 0);
        for (int i = 0; i < m; ++i) pref[i + 1] = pref[i] + cnts[i];
        int l = 0;
        int ans = 0;
        for (int r = 0; r < m; ++r) {
            while (vals[r] - vals[l] > k) ++l;
            long long total = pref[r + 1] - pref[l];          // elements in [l, r]
            long long less   = total - cnts[r];               // need operations
            long long possible = cnts[r] + min<long long>(numOperations, less);
            ans = max(ans, (int)possible);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxFrequency(int[] nums, int k, int numOperations) {
        java.util.Arrays.sort(nums);
        long budget = (long) k * numOperations;
        long sum = 0;
        int left = 0;
        int result = 1;
        for (int right = 0; right < nums.length; ++right) {
            sum += nums[right];
            while ((long) nums[right] * (right - left + 1) - sum > budget) {
                sum -= nums[left];
                left++;
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        import bisect
        nums.sort()
        n = len(nums)
        ans = 0
        left = 0
        for right in range(n):
            # shrink window so that max - min <= k
            while nums[right] - nums[left] > k:
                left += 1
            # first occurrence of nums[right] within current window
            idx = bisect.bisect_left(nums, nums[right], left, right + 1)
            ops_needed = idx - left          # elements that need an operation
            if ops_needed <= numOperations:
                ans = max(ans, right - left + 1)
        return ans
```

## Python3

```python
class Solution:
    def maxFrequency(self, nums, k, numOperations):
        from collections import defaultdict, Counter

        if not nums:
            return 0
        # If k == 0, no value can be changed.
        if k == 0:
            return max(Counter(nums).values())

        groups = defaultdict(list)
        for x in nums:
            groups[x % k].append(x)

        ans = 1
        for rem, arr in groups.items():
            arr.sort()
            # Convert to quotient values where each step of +k corresponds to +1 in this space.
            b = [ (x - rem) // k for x in arr ]   # same as x//k because same remainder
            left = 0
            sum_b = 0
            for right, val in enumerate(b):
                sum_b += val
                # required operations to raise all elements in window to b[right]
                while (right - left + 1) * val - sum_b > numOperations:
                    sum_b -= b[left]
                    left += 1
                ans = max(ans, right - left + 1)
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int maxFrequency(int* nums, int numsSize, int k, int numOperations) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);

    int left = 0;
    int cntMax = 0;          // number of elements equal to current max (nums[right])
    int best = 0;

    for (int right = 0; right < numsSize; ++right) {
        if (right == 0 || nums[right] != nums[right - 1]) {
            cntMax = 1;                 // new maximum value starts here
        } else {
            cntMax++;                   // same as previous max, increase count
        }

        while (left <= right &&
               (nums[right] - nums[left] > k ||
                ((right - left + 1) - cntMax) > numOperations)) {

            if (nums[left] == nums[right]) {
                cntMax--;               // removing a max element from the window
            }
            ++left;
        }

        int windowSize = right - left + 1;
        if (windowSize > best) best = windowSize;
    }

    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxFrequency(int[] nums, int k, int numOperations) {
        if (nums == null || nums.Length == 0) return 0;
        Array.Sort(nums);
        long maxOps = (long)k * numOperations; // total increment budget
        long sum = 0;
        int left = 0;
        int result = 1;
        for (int right = 0; right < nums.Length; right++) {
            sum += nums[right];
            while ((long)nums[right] * (right - left + 1) - sum > maxOps) {
                sum -= nums[left];
                left++;
            }
            int windowSize = right - left + 1;
            if (windowSize > result) result = windowSize;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} numOperations
 * @return {number}
 */
var maxFrequency = function(nums, k, numOperations) {
    if (k === 0) {
        const cnt = new Map();
        let ans = 0;
        for (const v of nums) {
            const c = (cnt.get(v) || 0) + 1;
            cnt.set(v, c);
            if (c > ans) ans = c;
        }
        return ans;
    }

    const groups = new Map(); // remainder -> array of scaled values
    for (const v of nums) {
        const r = v % k;
        const s = (v - r) / k; // integer division, safe because both are ints
        if (!groups.has(r)) groups.set(r, []);
        groups.get(r).push(s);
    }

    let answer = 0;

    for (const arr of groups.values()) {
        arr.sort((a, b) => a - b);
        let left = 0;
        let sum = 0; // sum of values in current window
        for (let right = 0; right < arr.length; ++right) {
            sum += arr[right];
            // total ops needed to raise all elements in [left, right] to arr[right]
            while (arr[right] * (right - left + 1) - sum > numOperations) {
                sum -= arr[left];
                ++left;
            }
            const len = right - left + 1;
            if (len > answer) answer = len;
        }
    }

    return answer;
};
```

## Typescript

```typescript
function maxFrequency(nums: number[], k: number, numOperations: number): number {
    if (k === 0) {
        const freq = new Map<number, number>();
        let best = 0;
        for (const v of nums) {
            const c = (freq.get(v) ?? 0) + 1;
            freq.set(v, c);
            if (c > best) best = c;
        }
        return best;
    }

    const groups = new Map<number, number[]>();
    for (const val of nums) {
        const r = ((val % k) + k) % k;
        let arr = groups.get(r);
        if (!arr) {
            arr = [];
            groups.set(r, arr);
        }
        arr.push(val);
    }

    let ans = 0;

    for (const [r, values] of groups.entries()) {
        values.sort((a, b) => a - b);
        const normalized: number[] = new Array(values.length);
        for (let i = 0; i < values.length; ++i) {
            normalized[i] = (values[i] - r) / k;
        }

        let left = 0;
        let sum = 0;
        for (let right = 0; right < normalized.length; ++right) {
            sum += normalized[right];
            while ((normalized[right] * (right - left + 1) - sum) > numOperations) {
                sum -= normalized[left];
                ++left;
            }
            const size = right - left + 1;
            if (size > ans) ans = size;
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
     * @param Integer $k
     * @param Integer $numOperations
     * @return Integer
     */
    function maxFrequency($nums, $k, $numOperations) {
        $budget = $k * $numOperations;
        sort($nums);
        $n = count($nums);
        $left = 0;
        $sum = 0;
        $maxFreq = 1;

        for ($right = 0; $right < $n; $right++) {
            $sum += $nums[$right];
            while ($nums[$right] * ($right - $left + 1) - $sum > $budget) {
                $sum -= $nums[$left];
                $left++;
            }
            $currentLen = $right - $left + 1;
            if ($currentLen > $maxFreq) {
                $maxFreq = $currentLen;
            }
        }

        return $maxFreq;
    }
}
```

## Swift

```swift
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int, _ numOperations: Int) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        var sortedNums = nums.sorted()
        let budget = Int64(k) * Int64(numOperations)
        var left = 0
        var sum: Int64 = 0
        var maxFreq = 1
        
        for right in 0..<n {
            sum += Int64(sortedNums[right])
            while true {
                let windowSize = right - left + 1
                let needed = Int64(sortedNums[right]) * Int64(windowSize) - sum
                if needed <= budget { break }
                sum -= Int64(sortedNums[left])
                left += 1
            }
            maxFreq = max(maxFreq, right - left + 1)
        }
        return maxFreq
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFrequency(nums: IntArray, k: Int, numOperations: Int): Int {
        val n = nums.size
        if (n == 0) return 0
        nums.sort()
        val startIdx = IntArray(n)
        var start = 0
        for (i in 0 until n) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                start = i
            }
            startIdx[i] = start
        }
        var l = 0
        var ans = 0
        for (r in 0 until n) {
            while (nums[r] - nums[l] > k) {
                l++
            }
            val firstPos = startIdx[r]
            val countEqual = if (firstPos >= l) r - firstPos + 1 else 0
            val windowSize = r - l + 1
            var possible = countEqual + numOperations
            if (possible > windowSize) possible = windowSize
            if (possible > ans) ans = possible
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxFrequency(List<int> nums, int k, int numOperations) {
    List<int> a = List.from(nums);
    a.sort();
    int n = a.length;
    List<int> firstPos = List.filled(n, 0);
    int start = 0;
    for (int i = 0; i < n; i++) {
      if (i == 0 || a[i] != a[i - 1]) {
        start = i;
      }
      firstPos[i] = start;
    }

    int left = 0;
    int sum = 0;
    int ans = 1;

    for (int right = 0; right < n; right++) {
      sum += a[right];
      while (true) {
        int totalNeeded = a[right] * (right - left + 1) - sum;
        int opsNeeded = firstPos[right] - left;
        if (totalNeeded <= k && opsNeeded <= numOperations) break;
        sum -= a[left];
        left++;
      }
      int windowSize = right - left + 1;
      if (windowSize > ans) ans = windowSize;
    }

    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func maxFrequency(nums []int, k int, numOperations int) int {
	if len(nums) == 0 {
		return 0
	}
	if k == 0 {
		freq := make(map[int]int)
		maxc := 0
		for _, v := range nums {
			freq[v]++
			if freq[v] > maxc {
				maxc = freq[v]
			}
		}
		return maxc
	}

	groups := make(map[int][]int)
	for _, v := range nums {
		r := v % k
		b := (v - r) / k
		groups[r] = append(groups[r], b)
	}

	ans := 0
	for _, arr := range groups {
		sort.Ints(arr)
		sum := 0
		l := 0
		for rIdx, val := range arr {
			sum += val
			for (val*(rIdx-l+1) - sum) > numOperations {
				sum -= arr[l]
				l++
			}
			if size := rIdx - l + 1; size > ans {
				ans = size
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_frequency(nums, k, num_operations)
  # If k is zero, operations do not change any element.
  return nums.tally.values.max if k == 0

  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }

  ans = 0
  freq.each_key do |v|
    cur = freq[v]
    if num_operations > 0 && freq.key?(v - k)
      cur += [num_operations, freq[v - k]].min
    end
    ans = cur if cur > ans
  end

  # Consider targets that are not originally present but can be formed by adding k.
  if num_operations > 0
    freq.each_key do |a|
      t = a + k
      cur = freq[t] || 0
      cur += [num_operations, freq[a]].min
      ans = cur if cur > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
        val budget: Long = k.toLong * numOperations
        java.util.Arrays.sort(nums)
        var left = 0
        var sum: Long = 0L
        var best = 1
        for (right <- nums.indices) {
            sum += nums(right).toLong
            while (nums(right).toLong * (right - left + 1) - sum > budget) {
                sum -= nums(left).toLong
                left += 1
            }
            val windowSize = right - left + 1
            if (windowSize > best) best = windowSize
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // When k == 0, no element can be increased.
        if k == 0 {
            let mut sorted = nums.clone();
            sorted.sort_unstable();
            let mut max_cnt = 1;
            let mut cur = 1;
            for i in 1..n {
                if sorted[i] == sorted[i - 1] {
                    cur += 1;
                } else {
                    if cur > max_cnt {
                        max_cnt = cur;
                    }
                    cur = 1;
                }
            }
            if cur > max_cnt {
                max_cnt = cur;
            }
            return max_cnt as i32;
        }

        let k_usize = k as usize;
        // Sort nums
        let mut sorted = nums.clone();
        sorted.sort_unstable();

        // Precompute q = val / k and r = val % k
        let mut qs: Vec<i64> = Vec::with_capacity(n);
        let mut rs: Vec<usize> = Vec::with_capacity(n);
        for &val in &sorted {
            let v = val as i64;
            qs.push(v / (k as i64));
            rs.push((val as usize) % k_usize);
        }

        // Fenwick tree for remainder frequencies
        struct Fenwick {
            n: usize,
            bit: Vec<i32>,
        }
        impl Fenwick {
            fn new(n: usize) -> Self {
                Fenwick { n, bit: vec![0; n + 1] }
            }
            fn add(&mut self, mut idx: usize, delta: i32) {
                // internal index is 1‑based
                idx += 1;
                while idx <= self.n {
                    self.bit[idx] += delta;
                    idx += idx & (!idx + 1);
                }
            }
            fn sum(&self, mut idx: usize) -> i32 {
                if idx >= self.n {
                    idx = self.n - 1;
                }
                let mut res = 0;
                idx += 1;
                while idx > 0 {
                    res += self.bit[idx];
                    idx &= idx - 1;
                }
                res
            }
        }

        let mut bit = Fenwick::new(k_usize);
        let mut left: usize = 0;
        let mut sum_q: i64 = 0;
        let mut answer: i32 = 1;
        let max_ops = num_operations as i64;

        for right in 0..n {
            // add right element
            sum_q += qs[right];
            bit.add(rs[right], 1);

            loop {
                let len = (right - left + 1) as i64;
                let q_r = qs[right];
                let r_r = rs[right];
                let cnt_less = if r_r == 0 {
                    0
                } else {
                    bit.sum(r_r - 1) as i64
                };
                // total operations needed for window [left..right]
                let ops_needed = len * q_r - sum_q + cnt_less;
                if ops_needed <= max_ops {
                    break;
                }
                // shrink from left
                sum_q -= qs[left];
                bit.add(rs[left], -1);
                left += 1;
            }

            let current_len = (right - left + 1) as i32;
            if current_len > answer {
                answer = current_len;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (max-frequency nums k numOperations)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((budget (* k numOperations))
         (sorted-vec (list->vector (sort nums <)))
         (n (vector-length sorted-vec)))
    (let loop ((right 0) (left 0) (sum 0) (best 1))
      (if (= right n)
          best
          (let* ((val (vector-ref sorted-vec right))
                 (new-sum (+ sum val)))
            (let-values ([(shrink-left shrink-sum)
                          (let loop-shrink ((l left) (s new-sum))
                            (if (<= (- (* val (+ 1 (- right l))) s) budget)
                                (values l s)
                                (loop-shrink (+ l 1) (- s (vector-ref sorted-vec l)))) )])
              (let* ((window-size (+ 1 (- right shrink-left)))
                     (new-best (if (> window-size best) window-size best)))
                (loop (+ right 1) shrink-left shrink-sum new-best))))))))
```

## Erlang

```erlang
-spec max_frequency(Nums :: [integer()], K :: integer(), NumOperations :: integer()) -> integer().
max_frequency(Nums, K, NumOperations) ->
    case K of
        0 ->
            max_freq_no_change(Nums);
        _ ->
            Sorted = lists:sort(Nums),
            N = length(Sorted),
            SortedArr = array:from_list(Sorted),
            Bit0 = array:new(K + 2, {default, 0}),
            Freq0 = array:new(K, {default, 0}),
            process(0, 0, 0, 0, 1, Bit0, Freq0, SortedArr, N, K, NumOperations)
    end.

%% --------------------------------------------------------------------
%% Helper for the case K == 0 : longest equal run
max_freq_no_change(Nums) ->
    Sorted = lists:sort(Nums),
    max_run(Sorted, 0, undefined).

max_run([], Max, _) -> Max;
max_run([H|T], CurMax, Prev) when Prev =:= H ->
    NewCur = CurMax + 1,
    max_run(T, max(CurMax, NewCur), H);
max_run([H|T], CurMax, _) ->
    max_run(T, max(CurMax, 1), H).

%% --------------------------------------------------------------------
%% Main sliding window processing
process(R, L, SumQ, WinSize, MaxFreq, Bit, Freq, SortedArr, N, K, NumOps) when R == N ->
    MaxFreq;
process(R, L, SumQ, WinSize, MaxFreq, Bit, Freq, SortedArr, N, K, NumOps) ->
    V = array:get(R, SortedArr),
    Q = V div K,
    Rem = V rem K,
    NewSumQ = SumQ + Q,
    {Bit1, Freq1} = add_rem(Bit, Freq, Rem, 1, K),
    WinSize1 = WinSize + 1,

    TargetQ = Q,
    TargetR = Rem,
    Prefix = bit_sum(Bit1, TargetR + 1),
    CntEqRem = array:get(TargetR, Freq1),
    CntRless = WinSize1 - Prefix,
    TotalOps = WinSize1 * (TargetQ + 1) - NewSumQ - CntRless - CntEqRem,

    {L2, SumQ2, WinSize2, Bit2, Freq2} =
        shrink(L, NewSumQ, WinSize1, Bit1, Freq1,
               TotalOps, NumOps, TargetQ, TargetR, SortedArr, K),

    MaxFreq2 = if WinSize2 > MaxFreq -> WinSize2; true -> MaxFreq end,
    process(R + 1, L2, SumQ2, WinSize2, MaxFreq2, Bit2, Freq2,
            SortedArr, N, K, NumOps).

%% --------------------------------------------------------------------
%% Shrink window from the left while operations exceed limit
shrink(L, SumQ, WinSize, Bit, Freq,
       TotalOps, NumOps, _TargetQ, _TargetR, _SortedArr, _K)
    when TotalOps =< NumOps ->
    {L, SumQ, WinSize, Bit, Freq};
shrink(L, SumQ, WinSize, Bit, Freq,
       _TotalOps, NumOps, TargetQ, TargetR, SortedArr, K) ->
    Vl = array:get(L, SortedArr),
    Ql = Vl div K,
    Rl = Vl rem K,
    NewSumQ = SumQ - Ql,
    {NewBit, NewFreq} = add_rem(Bit, Freq, Rl, -1, K),
    L1 = L + 1,
    WinSize1 = WinSize - 1,

    Prefix = bit_sum(NewBit, TargetR + 1),
    CntEqRem = array:get(TargetR, NewFreq),
    CntRless = WinSize1 - Prefix,
    TotalOps1 = WinSize1 * (TargetQ + 1) - NewSumQ - CntRless - CntEqRem,

    shrink(L1, NewSumQ, WinSize1, NewBit, NewFreq,
           TotalOps1, NumOps, TargetQ, TargetR, SortedArr, K).

%% --------------------------------------------------------------------
%% Update BIT and frequency array for a remainder
add_rem(Bit, Freq, Rem, Delta, K) ->
    Index = Rem + 1,
    NewBit = bit_add(Bit, Index, Delta, K + 1),
    OldFreq = array:get(Rem, Freq),
    NewFreq = OldFreq + Delta,
    {NewBit, array:set(Rem, NewFreq, Freq)}.

%% --------------------------------------------------------------------
%% BIT add (1‑based index)
bit_add(Bit, Idx, Delta, MaxIdx) when Idx =< MaxIdx ->
    Val = array:get(Idx, Bit),
    Updated = array:set(Idx, Val + Delta, Bit),
    Next = Idx + (Idx band -Idx),
    bit_add(Updated, Next, Delta, MaxIdx);
bit_add(Bit, _Idx, _Delta, _MaxIdx) -> Bit.

%% --------------------------------------------------------------------
%% BIT prefix sum (inclusive)
bit_sum(_Bit, 0) -> 0;
bit_sum(Bit, Idx) ->
    Val = array:get(Idx, Bit),
    Prev = Idx - (Idx band -Idx),
    bit_sum(Bit, Prev) + Val.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_frequency(nums :: [integer], k :: integer, num_operations :: integer) :: integer
  def max_frequency(nums, k, num_operations) do
    sorted = Enum.sort(nums)
    limit = k * num_operations
    n = length(sorted)

    {best, _left, _sum} =
      Enum.reduce(0..(n - 1), {0, 0, 0}, fn right, {best, left, sum} ->
        val = :lists.nth(right + 1, sorted)   # Enum.at is O(n), use :lists.nth for O(1) on list
        sum = sum + val

        {left, sum} = shrink_window(sorted, left, right, sum, val, limit)

        window_size = right - left + 1
        best = if window_size > best, do: window_size, else: best
        {best, left, sum}
      end)

    best
  end

  defp shrink_window(sorted, left, right, sum, current_val, limit) do
    needed = current_val * (right - left + 1) - sum

    if needed <= limit do
      {left, sum}
    else
      # remove the leftmost element and continue shrinking
      left_elem = :lists.nth(left + 1, sorted)
      shrink_window(sorted, left + 1, right, sum - left_elem, current_val, limit)
    end
  end
end
```
