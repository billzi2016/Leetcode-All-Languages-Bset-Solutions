# 3381. Maximum Subarray Sum With Length Divisible by K

## Cpp

```cpp
class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> minPref(k, LLONG_MAX);
        minPref[0] = 0; // prefix sum of length 0 has remainder 0
        long long pref = 0;
        long long ans = LLONG_MIN;
        for (int i = 1; i <= n; ++i) {
            pref += nums[i - 1];
            int rem = i % k;
            if (minPref[rem] != LLONG_MAX) {
                ans = max(ans, pref - minPref[rem]);
            }
            minPref[rem] = min(minPref[rem], pref);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long[] minPref = new long[k];
        java.util.Arrays.fill(minPref, Long.MAX_VALUE);
        // prefix sum before any element (index 0)
        minPref[0] = 0L;
        long pref = 0L;
        long ans = Long.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            pref += nums[i - 1];
            int rem = i % k;
            if (minPref[rem] != Long.MAX_VALUE) {
                long candidate = pref - minPref[rem];
                if (candidate > ans) ans = candidate;
            }
            if (pref < minPref[rem]) {
                minPref[rem] = pref;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        INF = 10**30
        min_pref = [INF] * k
        pref = 0
        min_pref[0] = 0  # prefix sum of length 0 has remainder 0
        ans = -INF
        for i, val in enumerate(nums, 1):
            pref += val
            rem = i % k
            if min_pref[rem] != INF:
                cand = pref - min_pref[rem]
                if cand > ans:
                    ans = cand
            if pref < min_pref[rem]:
                min_pref[rem] = pref
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10**20
        min_pref = [INF] * k
        min_pref[0] = 0  # prefix sum at index 0 has remainder 0
        pref = 0
        ans = -INF
        for i, val in enumerate(nums, 1):
            pref += val
            rem = i % k
            if min_pref[rem] != INF:
                ans = max(ans, pref - min_pref[rem])
            if pref < min_pref[rem]:
                min_pref[rem] = pref
        return ans
```

## C

```c
#include <limits.h>
#include <stdlib.h>

long long maxSubarraySum(int* nums, int numsSize, int k) {
    long long *minPref = (long long*)malloc(sizeof(long long) * k);
    for (int i = 0; i < k; ++i) minPref[i] = LLONG_MAX;
    
    long long prefix = 0;
    minPref[0] = 0;               // prefix sum at index 0, remainder 0
    long long ans = LLONG_MIN;   // best answer
    
    for (int i = 1; i <= numsSize; ++i) {
        prefix += nums[i - 1];
        int rem = i % k;
        if (minPref[rem] != LLONG_MAX) {
            long long cand = prefix - minPref[rem];
            if (cand > ans) ans = cand;
        }
        if (prefix < minPref[rem]) minPref[rem] = prefix;
    }
    
    free(minPref);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxSubarraySum(int[] nums, int k) {
        int n = nums.Length;
        long[] minPref = new long[k];
        for (int i = 0; i < k; i++) minPref[i] = long.MaxValue;
        minPref[0] = 0; // prefix sum at index 0

        long pref = 0;
        long ans = long.MinValue;

        for (int i = 1; i <= n; i++) {
            pref += nums[i - 1];
            int rem = i % k;

            if (minPref[rem] != long.MaxValue) {
                long cand = pref - minPref[rem];
                if (cand > ans) ans = cand;
            }

            if (pref < minPref[rem]) minPref[rem] = pref;
        }

        return ans;
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
var maxSubarraySum = function(nums, k) {
    const n = nums.length;
    const minPref = new Array(k).fill(Infinity);
    // prefix sum at index 0 is 0, remainder 0
    minPref[0] = 0;
    let pref = 0;
    let ans = -Infinity;
    for (let i = 1; i <= n; i++) {
        pref += nums[i - 1];
        const rem = i % k;
        if (minPref[rem] !== Infinity) {
            const cand = pref - minPref[rem];
            if (cand > ans) ans = cand;
        }
        if (pref < minPref[rem]) minPref[rem] = pref;
    }
    return ans;
};
```

## Typescript

```typescript
function maxSubarraySum(nums: number[], k: number): number {
    const minPref = new Array(k).fill(Infinity);
    let prefix = 0;
    // prefix sum at index 0
    minPref[0] = 0;
    let ans = -Infinity;

    for (let i = 1; i <= nums.length; i++) {
        prefix += nums[i - 1];
        const rem = i % k;
        if (minPref[rem] !== Infinity) {
            const cand = prefix - minPref[rem];
            if (cand > ans) ans = cand;
        }
        if (prefix < minPref[rem]) minPref[rem] = prefix;
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
     * @return Integer
     */
    function maxSubarraySum($nums, $k) {
        $n = count($nums);
        $pref = 0;
        $minPref = array_fill(0, $k, null);
        $ans = -PHP_INT_MAX;

        for ($i = 0; $i <= $n; $i++) {
            $rem = $i % $k;
            if ($minPref[$rem] !== null) {
                $candidate = $pref - $minPref[$rem];
                if ($candidate > $ans) {
                    $ans = $candidate;
                }
            }

            if ($minPref[$rem] === null || $pref < $minPref[$rem]) {
                $minPref[$rem] = $pref;
            }

            if ($i < $n) {
                $pref += $nums[$i];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var minPref = Array(repeating: Int.max, count: k)
        var prefix = 0
        minPref[0] = 0
        var ans = Int.min
        
        for i in 1...n {
            prefix += nums[i - 1]
            let r = i % k
            if minPref[r] != Int.max {
                let candidate = prefix - minPref[r]
                if candidate > ans { ans = candidate }
            }
            if prefix < minPref[r] {
                minPref[r] = prefix
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubarraySum(nums: IntArray, k: Int): Long {
        val minPref = LongArray(k) { Long.MAX_VALUE }
        var prefix = 0L
        minPref[0] = 0L
        var answer = Long.MIN_VALUE
        for (i in 1..nums.size) {
            prefix += nums[i - 1].toLong()
            val rem = i % k
            if (minPref[rem] != Long.MAX_VALUE) {
                val candidate = prefix - minPref[rem]
                if (candidate > answer) answer = candidate
            }
            if (prefix < minPref[rem]) minPref[rem] = prefix
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxSubarraySum(List<int> nums, int k) {
    const int INF = 1 << 60;
    List<int> minPref = List.filled(k, INF);
    minPref[0] = 0; // prefix sum at index 0
    int pref = 0;
    int ans = -INF;

    for (int j = 1; j <= nums.length; ++j) {
      pref += nums[j - 1];
      int rem = j % k;
      if (minPref[rem] != INF) {
        int cand = pref - minPref[rem];
        if (cand > ans) ans = cand;
      }
      if (pref < minPref[rem]) minPref[rem] = pref;
    }

    return ans;
  }
}
```

## Golang

```go
func maxSubarraySum(nums []int, k int) int64 {
    n := len(nums)
    const INF int64 = 1<<63 - 1
    minPref := make([]int64, k)
    for i := 0; i < k; i++ {
        minPref[i] = INF
    }
    pref := int64(0)
    minPref[0] = 0 // prefix sum at index 0 has remainder 0
    ans := - (1 << 63) // MinInt64

    for i := 1; i <= n; i++ {
        pref += int64(nums[i-1])
        r := i % k
        if minPref[r] != INF {
            cand := pref - minPref[r]
            if cand > ans {
                ans = cand
            }
        }
        if pref < minPref[r] {
            minPref[r] = pref
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_subarray_sum(nums, k)
  min_prefix = Array.new(k, Float::INFINITY)
  pref = 0
  min_prefix[0] = 0
  ans = - (1 << 62)

  nums.each_with_index do |val, idx|
    pref += val
    i = idx + 1
    rem = i % k

    if min_prefix[rem] != Float::INFINITY
      cand = pref - min_prefix[rem]
      ans = cand if cand > ans
    end

    min_prefix[rem] = pref if pref < min_prefix[rem]
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxSubarraySum(nums: Array[Int], k: Int): Long = {
        val minPref = Array.fill[Long](k)(Long.MaxValue)
        var pref: Long = 0L
        minPref(0) = 0L
        var ans: Long = Long.MinValue

        for (i <- 1 to nums.length) {
            pref += nums(i - 1).toLong
            val r = i % k
            if (minPref(r) != Long.MaxValue) {
                val cand = pref - minPref(r)
                if (cand > ans) ans = cand
            }
            if (pref < minPref(r)) minPref(r) = pref
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k_usize = k as usize;
        let mut min_pref = vec![i64::MAX; k_usize];
        // prefix sum at index 0
        min_pref[0] = 0;
        let mut pref: i64 = 0;
        let mut ans = i64::MIN;

        for (idx, &val) in nums.iter().enumerate() {
            pref += val as i64;
            let i = idx + 1; // current prefix length
            let rem = i % k_usize;
            if min_pref[rem] != i64::MAX {
                let cand = pref - min_pref[rem];
                if cand > ans {
                    ans = cand;
                }
            }
            if pref < min_pref[rem] {
                min_pref[rem] = pref;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (min-pref (make-vector k #f))
         (max-abs (* n 1000000000)) ; upper bound on absolute sum
         (ans (box (- max-abs))))   ; start with very small value
    ;; prefix sum of length 0 has remainder 0 and value 0
    (vector-set! min-pref 0 0)
    (let loop ((i 1) (pref 0))
      (if (> i n)
          (unbox ans)
          (let* ((pref (+ pref (vector-ref arr (- i 1))))
                 (rem (modulo i k))
                 (minv (vector-ref min-pref rem)))
            (when minv
              (let ((cand (- pref minv)))
                (when (> cand (unbox ans))
                  (set-box! ans cand))))
            (if (or (not minv) (< pref minv))
                (vector-set! min-pref rem pref)
                (void))
            (loop (+ i 1) pref))))))
```

## Erlang

```erlang
-spec max_subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
max_subarray_sum(Nums, K) ->
    MaxNeg = -1000000000000000000,
    loop(Nums, K, 0, 0, #{0 => 0}, MaxNeg).

loop([], _K, _Idx, _Pref, _MinMap, Ans) -> Ans;
loop([H|T], K, Idx, Pref, MinMap, Ans) ->
    NewPref = Pref + H,
    NewIdx = Idx + 1,
    Rem = NewIdx rem K,
    % compute candidate if a previous prefix with same remainder exists
    NewAns =
        case maps:find(Rem, MinMap) of
            {ok, MinVal} ->
                Cand = NewPref - MinVal,
                if Cand > Ans -> Cand; true -> Ans end;
            error -> Ans
        end,
    % update minimal prefix sum for this remainder
    UpdatedMinMap =
        case maps:find(Rem, MinMap) of
            {ok, Existing} when NewPref < Existing ->
                maps:put(Rem, NewPref, MinMap);
            {ok, _Existing} ->
                MinMap;
            error ->
                maps:put(Rem, NewPref, MinMap)
        end,
    loop(T, K, NewIdx, NewPref, UpdatedMinMap, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_subarray_sum(nums :: [integer], k :: integer) :: integer
  def max_subarray_sum(nums, k) do
    inf = 1 <<< 60
    ans = -inf
    pref = 0

    min_mods = :array.new(k, default: inf)
    min_mods = :array.set(0, 0, min_mods)

    {_final_pref, _final_mods, final_ans} =
      Enum.with_index(nums)
      |> Enum.reduce({pref, min_mods, ans}, fn {num, idx}, {cur_pref, cur_mods, cur_ans} ->
        new_pref = cur_pref + num
        mod = rem(idx + 1, k)

        min_val = :array.get(mod, cur_mods)
        cand = new_pref - min_val
        new_ans = if cand > cur_ans, do: cand, else: cur_ans

        new_min = if new_pref < min_val, do: new_pref, else: min_val
        new_mods = :array.set(mod, new_min, cur_mods)

        {new_pref, new_mods, new_ans}
      end)

    final_ans
  end
end
```
