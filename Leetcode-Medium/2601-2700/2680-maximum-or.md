# 2680. Maximum OR

## Cpp

```cpp
class Solution {
public:
    long long maximumOr(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> pref(n), suff(n);
        for (int i = 0; i < n; ++i) {
            pref[i] = (i ? pref[i-1] : 0) | (long long)nums[i];
        }
        for (int i = n - 1; i >= 0; --i) {
            suff[i] = (i + 1 < n ? suff[i+1] : 0) | (long long)nums[i];
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long others = 0;
            if (i > 0) others |= pref[i-1];
            if (i + 1 < n) others |= suff[i+1];
            long long shifted = ((long long)nums[i]) << k;
            ans = max(ans, others | shifted);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumOr(int[] nums, int k) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] | (long) nums[i];
        }
        long[] suffix = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1] | (long) nums[i];
        }
        long max = 0;
        long shiftFactor = 1L << k; // 2^k
        for (int i = 0; i < n; i++) {
            long otherOr = prefix[i] | suffix[i + 1];
            long shifted = ((long) nums[i]) * shiftFactor; // equivalent to left shift by k
            long candidate = otherOr | shifted;
            if (candidate > max) {
                max = candidate;
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] | nums[i]
        suff = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] | nums[i]
        ans = 0
        shift_val = k
        for i in range(n):
            rest_or = pref[i] | suff[i + 1]
            cand = rest_or | (nums[i] << shift_val)
            if cand > ans:
                ans = cand
        return ans
```

## Python3

```python
class Solution:
    def maximumOr(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] | nums[i]
        suff = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] | nums[i]

        ans = 0
        shift = k
        for i in range(n):
            others = pref[i] | suff[i + 1]
            cand = (nums[i] << shift) | others
            if cand > ans:
                ans = cand
        return ans
```

## C

```c
#include <stdlib.h>

long long maximumOr(int* nums, int numsSize, int k) {
    int n = numsSize;
    unsigned long long *pref = (unsigned long long *)malloc((n + 1) * sizeof(unsigned long long));
    unsigned long long *suff = (unsigned long long *)malloc((n + 1) * sizeof(unsigned long long));

    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] | (unsigned long long)nums[i];
    }

    suff[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        suff[i] = suff[i + 1] | (unsigned long long)nums[i];
    }

    unsigned long long best = 0;
    for (int i = 0; i < n; ++i) {
        unsigned long long other = pref[i] | suff[i + 1];
        unsigned long long shifted = ((unsigned long long)nums[i]) << k;
        unsigned long long cur = other | shifted;
        if (cur > best) best = cur;
    }

    free(pref);
    free(suff);
    return (long long)best;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximumOr(int[] nums, int k) {
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] | (long)nums[i];
        }
        long[] suff = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suff[i] = suff[i + 1] | (long)nums[i];
        }

        long best = 0;
        for (int i = 0; i < n; i++) {
            long shifted = ((long)nums[i]) << k;
            long cur = shifted | pref[i] | suff[i + 1];
            if (cur > best) best = cur;
        }
        return best;
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
var maximumOr = function(nums, k) {
    const n = nums.length;
    const bigNums = nums.map(v => BigInt(v));
    const shift = BigInt(k);
    
    const prefix = new Array(n + 1).fill(0n);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] | bigNums[i];
    }
    
    const suffix = new Array(n + 1).fill(0n);
    for (let i = n - 1; i >= 0; --i) {
        suffix[i] = suffix[i + 1] | bigNums[i];
    }
    
    let maxRes = 0n;
    for (let i = 0; i < n; ++i) {
        const other = prefix[i] | suffix[i + 1];
        const shifted = bigNums[i] << shift;
        const cand = shifted | other;
        if (cand > maxRes) maxRes = cand;
    }
    
    return Number(maxRes);
};
```

## Typescript

```typescript
function maximumOr(nums: number[], k: number): number {
    const n = nums.length;
    const prefix = new Array<bigint>(n);
    const suffix = new Array<bigint>(n);

    for (let i = 0; i < n; i++) {
        const val = BigInt(nums[i]);
        if (i === 0) prefix[i] = val;
        else prefix[i] = prefix[i - 1] | val;
    }

    for (let i = n - 1; i >= 0; i--) {
        const val = BigInt(nums[i]);
        if (i === n - 1) suffix[i] = val;
        else suffix[i] = suffix[i + 1] | val;
    }

    let best = 0n;
    const shift = BigInt(k);

    for (let i = 0; i < n; i++) {
        const shifted = BigInt(nums[i]) << shift;
        let otherOr = 0n;
        if (i > 0) otherOr |= prefix[i - 1];
        if (i + 1 < n) otherOr |= suffix[i + 1];
        const candidate = shifted | otherOr;
        if (candidate > best) best = candidate;
    }

    return Number(best);
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
    function maximumOr($nums, $k) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] | $nums[$i];
        }
        $suff = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $suff[$i] = $suff[$i + 1] | $nums[$i];
        }
        $max = 0;
        foreach ($nums as $idx => $val) {
            $other = $pref[$idx] | $suff[$idx + 1];
            $candidate = ($val << $k) | $other;
            if ($candidate > $max) {
                $max = $candidate;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximumOr(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] | nums[i]
        }
        var suffix = Array(repeating: 0, count: n + 1)
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                suffix[i] = suffix[i + 1] | nums[i]
            }
        }
        var result = 0
        let shift = k
        for i in 0..<n {
            let withoutI = prefix[i] | suffix[i + 1]
            let shifted = nums[i] << shift
            let total = withoutI | shifted
            if total > result {
                result = total
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumOr(nums: IntArray, k: Int): Long {
        val n = nums.size
        val pref = LongArray(n)
        var curPref = 0L
        for (i in 0 until n) {
            curPref = curPref or nums[i].toLong()
            pref[i] = curPref
        }
        val suff = LongArray(n)
        var curSuff = 0L
        for (i in n - 1 downTo 0) {
            curSuff = curSuff or nums[i].toLong()
            suff[i] = curSuff
        }
        var ans = 0L
        for (i in 0 until n) {
            val left = if (i > 0) pref[i - 1] else 0L
            val right = if (i + 1 < n) suff[i + 1] else 0L
            val shifted = nums[i].toLong() shl k
            val total = left or shifted or right
            if (total > ans) ans = total
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumOr(List<int> nums, int k) {
    int n = nums.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] | nums[i];
    }
    List<int> suffix = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
      suffix[i] = suffix[i + 1] | nums[i];
    }

    int best = 0;
    for (int i = 0; i < n; i++) {
      int othersOr = prefix[i] | suffix[i + 1];
      int candidate = (nums[i] << k) | othersOr;
      if (candidate > best) best = candidate;
    }
    return best;
  }
}
```

## Golang

```go
func maximumOr(nums []int, k int) int64 {
    n := len(nums)
    pref := make([]int64, n+1)
    for i := 0; i < n; i++ {
        pref[i+1] = pref[i] | int64(nums[i])
    }
    suf := make([]int64, n+1)
    for i := n - 1; i >= 0; i-- {
        suf[i] = suf[i+1] | int64(nums[i])
    }

    factor := int64(1) << uint(k) // 2^k
    var ans int64
    for i := 0; i < n; i++ {
        withoutI := pref[i] | suf[i+1]
        shifted := int64(nums[i]) * factor
        total := withoutI | shifted
        if total > ans {
            ans = total
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_or(nums, k)
  n = nums.length
  prefix = Array.new(n)
  suffix = Array.new(n)

  (0...n).each do |i|
    prefix[i] = i.zero? ? nums[i] : (prefix[i - 1] | nums[i])
  end

  (n - 1).downto(0) do |i|
    suffix[i] = i == n - 1 ? nums[i] : (suffix[i + 1] | nums[i])
  end

  ans = prefix[-1]

  (0...n).each do |i|
    or_except = 0
    or_except |= prefix[i - 1] if i > 0
    or_except |= suffix[i + 1] if i < n - 1
    candidate = (nums[i] << k) | or_except
    ans = candidate if candidate > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumOr(nums: Array[Int], k: Int): Long = {
        val n = nums.length
        val prefix = new Array[Long](n + 1)
        for (i <- 0 until n) {
            prefix(i + 1) = prefix(i) | nums(i).toLong
        }
        val suffix = new Array[Long](n + 1)
        for (i <- (n - 1) to 0 by -1) {
            suffix(i) = suffix(i + 1) | nums(i).toLong
        }
        var ans: Long = 0L
        for (i <- 0 until n) {
            val cur = prefix(i) | (nums(i).toLong << k) | suffix(i + 1)
            if (cur > ans) ans = cur
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_or(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut pre = vec![0i64; n + 1];
        for i in 0..n {
            pre[i + 1] = pre[i] | nums[i] as i64;
        }
        let mut suf = vec![0i64; n + 1];
        for i in (0..n).rev() {
            suf[i] = suf[i + 1] | nums[i] as i64;
        }
        let shift = k as u32;
        let mut ans: i64 = 0;
        for i in 0..n {
            let shifted = (nums[i] as i64) << shift;
            let total = pre[i] | shifted | suf[i + 1];
            if total > ans {
                ans = total;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-or nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v   (list->vector nums))
         (n   (vector-length v))
         (pref (make-vector (+ n 1) 0))
         (suff (make-vector (+ n 1) 0)))
    ;; prefix OR
    (for ([i (in-range n)])
      (vector-set! pref (add1 i)
                   (bitwise-ior (vector-ref pref i) (vector-ref v i))))
    ;; suffix OR
    (for ([i (in-range (sub1 n) -1 -1)])
      (vector-set! suff i
                   (bitwise-ior (vector-ref suff (add1 i)) (vector-ref v i))))
    (let loop ((i 0) (best 0))
      (if (= i n)
          best
          (let* ((other (bitwise-ior (vector-ref pref i) (vector-ref suff i)))
                 (cand  (bitwise-ior other (* (vector-ref v i) (arithmetic-shift 1 k)))))
            (loop (add1 i) (max best cand)))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_or/2]).

-spec maximum_or(Nums :: [integer()], K :: integer()) -> integer().
maximum_or(Nums, K) ->
    % Compute suffix ORs for each position (including an extra 0 at the end)
    SuffixFull = lists:foldr(fun(X, Acc) -> [X bor hd(Acc) | Acc] end, [0], Nums),
    % Drop the first element to get suffix after each index
    SuffixAfter = tl(SuffixFull),
    loop(Nums, SuffixAfter, K, 0, 0).

loop([], [], _K, _PrevOr, Max) ->
    Max;
loop([Num|Rest], [Suf|Sufs], K, PrevOr, Max) ->
    Shifted = Num bsl K,
    Total = (PrevOr bor Shifted) bor Suf,
    NewMax = if Total > Max -> Total; true -> Max end,
    NextPrev = PrevOr bor Num,
    loop(Rest, Sufs, K, NextPrev, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_or(nums :: [integer], k :: integer) :: integer
  def maximum_or(nums, k) do
    n = length(nums)

    # Build suffix OR tuple: suff[i] = nums[i] | ... | nums[n-1]
    suff_list =
      Enum.reduce(Enum.reverse(nums), [], fn x, acc ->
        case acc do
          [] -> [x]
          _ -> [(hd(acc) ||| x) | acc]
        end
      end)

    suff_tuple = List.to_tuple(suff_list)

    {max_or, _} =
      Enum.with_index(nums)
      |> Enum.reduce({0, 0}, fn {val, i}, {best, pref_or} ->
        left = pref_or
        right = if i == n - 1, do: 0, else: elem(suff_tuple, i + 1)

        others = left ||| right
        candidate = others ||| (val <<< k)
        new_best = if candidate > best, do: candidate, else: best

        {new_best, pref_or ||| val}
      end)

    max_or
  end
end
```
