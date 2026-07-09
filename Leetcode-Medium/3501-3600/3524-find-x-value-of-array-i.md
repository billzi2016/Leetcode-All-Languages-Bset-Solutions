# 3524. Find X Value of Array I

## Cpp

```cpp
class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> ans(k, 0);
        vector<long long> prev(k, 0), cur(k, 0);
        for (int val : nums) {
            int a = val % k;
            fill(cur.begin(), cur.end(), 0);
            // subarray consisting of only this element
            cur[a] += 1;
            // extend previous subarrays
            for (int r = 0; r < k; ++r) {
                if (prev[r]) {
                    int nr = (r * a) % k;
                    cur[nr] += prev[r];
                }
            }
            for (int r = 0; r < k; ++r) ans[r] += cur[r];
            prev.swap(cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] resultArray(int[] nums, int k) {
        long[] ans = new long[k];
        long[] prev = new long[k];
        for (int num : nums) {
            long[] cur = new long[k];
            int a = num % k;
            // subarray consisting of only this element
            cur[a] += 1;
            // extend previous subarrays
            for (int r = 0; r < k; ++r) {
                if (prev[r] == 0) continue;
                int newR = (int)((r * 1L * a) % k);
                cur[newR] += prev[r];
            }
            // accumulate results
            for (int r = 0; r < k; ++r) {
                ans[r] += cur[r];
            }
            prev = cur;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        dp = [0] * k  # subarrays ending at previous index
        for val in nums:
            a = val % k
            new_dp = [0] * k
            if any(dp):
                for r in range(k):
                    cnt = dp[r]
                    if cnt:
                        nr = (r * a) % k
                        new_dp[nr] += cnt
            # subarray consisting of only current element
            new_dp[a] += 1
            for r in range(k):
                ans[r] += new_dp[r]
            dp = new_dp
        return ans
```

## Python3

```python
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k  # counts of subarrays ending at previous index with each remainder
        for val in nums:
            m = val % k
            new_dp = [0] * k
            # start a new subarray consisting only of current element
            new_dp[m] += 1
            # extend previous subarrays
            for r in range(k):
                cnt = dp[r]
                if cnt:
                    nr = (r * m) % k
                    new_dp[nr] += cnt
            # accumulate results
            for r in range(k):
                ans[r] += new_dp[r]
            dp = new_dp
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

long long* resultArray(int* nums, int numsSize, int k, int* returnSize) {
    *returnSize = k;
    long long* res = (long long*)calloc(k, sizeof(long long));
    long long dpPrev[5] = {0};

    for (int i = 0; i < numsSize; ++i) {
        int curMod = nums[i] % k;
        long long dpCurr[5] = {0};

        // subarray consisting of only the current element
        dpCurr[curMod] += 1;

        // extend previous subarrays
        for (int r = 0; r < k; ++r) {
            if (dpPrev[r]) {
                int newR = (r * curMod) % k;
                dpCurr[newR] += dpPrev[r];
            }
        }

        // accumulate results and prepare for next iteration
        for (int r = 0; r < k; ++r) {
            res[r] += dpCurr[r];
            dpPrev[r] = dpCurr[r];
        }
    }

    return res;
}
```

## Csharp

```csharp
public class Solution {
    public long[] ResultArray(int[] nums, int k) {
        long[] ans = new long[k];
        long[] dp = new long[k];
        foreach (int num in nums) {
            int cur = num % k;
            long[] ndp = new long[k];
            for (int r = 0; r < k; ++r) {
                if (dp[r] == 0) continue;
                int nr = (int)((long)r * cur % k);
                ndp[nr] += dp[r];
            }
            ndp[cur] += 1;
            for (int r = 0; r < k; ++r) {
                ans[r] += ndp[r];
            }
            dp = ndp;
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
 * @return {number[]}
 */
var resultArray = function(nums, k) {
    const ans = new Array(k).fill(0);
    let dp = new Array(k).fill(0); // counts of subarrays ending at previous index
    
    for (let i = 0; i < nums.length; ++i) {
        const mod = nums[i] % k;
        const ndp = new Array(k).fill(0);
        
        // start a new subarray with only nums[i]
        ndp[mod] += 1;
        
        // extend previous subarrays
        for (let r = 0; r < k; ++r) {
            if (dp[r] !== 0) {
                const nr = (r * mod) % k;
                ndp[nr] += dp[r];
            }
        }
        
        // accumulate results
        for (let r = 0; r < k; ++r) {
            ans[r] += ndp[r];
        }
        
        dp = ndp;
    }
    
    return ans;
};
```

## Typescript

```typescript
function resultArray(nums: number[], k: number): number[] {
    const res = new Array(k).fill(0);
    let prev = new Array(k).fill(0);
    for (const num of nums) {
        const a = ((num % k) + k) % k;
        const cur = new Array(k).fill(0);
        cur[a] += 1; // subarray consisting only of current element
        for (let r = 0; r < k; ++r) {
            const cnt = prev[r];
            if (cnt !== 0) {
                const nr = (r * a) % k;
                cur[nr] += cnt;
            }
        }
        for (let r = 0; r < k; ++r) {
            res[r] += cur[r];
        }
        prev = cur;
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function resultArray($nums, $k) {
        $ans = array_fill(0, $k, 0);
        $dp = array_fill(0, $k, 0);

        foreach ($nums as $val) {
            $a = $val % $k;
            $new = array_fill(0, $k, 0);
            // subarray consisting of only current element
            $new[$a] += 1;

            for ($r = 0; $r < $k; $r++) {
                if ($dp[$r] == 0) continue;
                $mod = ($r * $a) % $k;
                $new[$mod] += $dp[$r];
            }

            for ($x = 0; $x < $k; $x++) {
                $ans[$x] += $new[$x];
            }
            $dp = $new;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func resultArray(_ nums: [Int], _ k: Int) -> [Int] {
        var result = Array(repeating: 0, count: k)
        var prev = Array(repeating: 0, count: k)
        
        for num in nums {
            let curMod = num % k
            var curr = Array(repeating: 0, count: k)
            
            // Subarray consisting of only the current element
            curr[curMod] += 1
            
            // Extend previous subarrays ending at the prior index
            if k > 0 {
                for r in 0..<k {
                    let cnt = prev[r]
                    if cnt != 0 {
                        let newR = (r * curMod) % k
                        curr[newR] += cnt
                    }
                }
            }
            
            // Accumulate counts into the final result
            for r in 0..<k {
                result[r] += curr[r]
            }
            
            prev = curr
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun resultArray(nums: IntArray, k: Int): LongArray {
        val ans = LongArray(k)
        var dp = LongArray(k)
        for (num in nums) {
            val a = num % k
            val newDp = LongArray(k)
            // extend previous subarrays
            for (r in 0 until k) {
                val cnt = dp[r]
                if (cnt != 0L) {
                    val nr = (r * a) % k
                    newDp[nr] += cnt
                }
            }
            // start new subarray at current position
            newDp[a] += 1L
            // accumulate results
            for (r in 0 until k) {
                ans[r] += newDp[r]
            }
            dp = newDp
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> resultArray(List<int> nums, int k) {
    List<int> ans = List.filled(k, 0);
    List<int> prev = List.filled(k, 0);
    for (int num in nums) {
      int curMod = num % k;
      List<int> curr = List.filled(k, 0);
      // subarray consisting of only this element
      curr[curMod] += 1;
      // extend previous subarrays
      for (int r = 0; r < k; ++r) {
        int cnt = prev[r];
        if (cnt == 0) continue;
        int newR = (r * curMod) % k;
        curr[newR] += cnt;
      }
      // accumulate results
      for (int r = 0; r < k; ++r) {
        ans[r] += curr[r];
      }
      prev = curr;
    }
    return ans;
  }
}
```

## Golang

```go
func resultArray(nums []int, k int) []int64 {
    ans := make([]int64, k)
    dp := make([]int64, k)

    for _, num := range nums {
        val := num % k
        newdp := make([]int64, k)

        // extend previous subarrays
        for r := 0; r < k; r++ {
            if dp[r] == 0 {
                continue
            }
            nr := (r * val) % k
            newdp[nr] += dp[r]
        }

        // subarray consisting of only current element
        newdp[val%k]++

        // accumulate to answer and set dp for next iteration
        for r := 0; r < k; r++ {
            ans[r] += newdp[r]
            dp[r] = newdp[r]
        }
    }

    return ans
}
```

## Ruby

```ruby
def result_array(nums, k)
  ans = Array.new(k, 0)
  dp = Array.new(k, 0)

  nums.each do |num|
    a = num % k
    new_dp = Array.new(k, 0)

    # subarray consisting of only current element
    new_dp[a] += 1

    # extend previous subarrays
    (0...k).each do |r|
      cnt = dp[r]
      next if cnt == 0
      t = (r * a) % k
      new_dp[t] += cnt
    end

    # accumulate results
    (0...k).each { |r| ans[r] += new_dp[r] }

    dp = new_dp
  end

  ans
end
```

## Scala

```scala
object Solution {
    def resultArray(nums: Array[Int], k: Int): Array[Long] = {
        val res = new Array[Long](k)
        var prev = new Array[Long](k)

        var i = 0
        while (i < nums.length) {
            val a = ((nums(i) % k) + k) % k
            val cur = new Array[Long](k)

            // subarray consisting of only this element
            cur(a) += 1

            var p = 0
            while (p < k) {
                val cnt = prev(p)
                if (cnt != 0) {
                    val r = (p * a) % k
                    cur(r) += cnt
                }
                p += 1
            }

            var rIdx = 0
            while (rIdx < k) {
                res(rIdx) += cur(rIdx)
                rIdx += 1
            }

            prev = cur
            i += 1
        }

        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn result_array(nums: Vec<i32>, k: i32) -> Vec<i64> {
        let k_usize = k as usize;
        let mut dp = vec![0i64; k_usize];
        let mut ans = vec![0i64; k_usize];

        for &val in nums.iter() {
            let a_mod = (val % k) as usize;
            let mut ndp = vec![0i64; k_usize];
            // subarray consisting only of current element
            ndp[a_mod] += 1;
            // extend previous subarrays
            for r in 0..k_usize {
                if dp[r] != 0 {
                    let nr = ((r as i32 * a_mod as i32) % k) as usize;
                    ndp[nr] += dp[r];
                }
            }
            // accumulate to answer
            for r in 0..k_usize {
                ans[r] += ndp[r];
            }
            dp = ndp;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (result‑array nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ((ans (make-vector k 0))
        (cur (make-vector k 0)))
    (for ([a nums])
      (let* ((mod-a (remainder a k))
             (nxt   (make-vector k 0)))
        ;; subarray consisting of only a
        (vector-set! nxt mod-a (+ (vector-ref nxt mod-a) 1))
        ;; extend previous subarrays
        (for ([r (in-range k)])
          (let ((cnt (vector-ref cur r)))
            (when (> cnt 0)
              (define new-r (remainder (* r mod-a) k))
              (vector-set! nxt new-r (+ (vector-ref nxt new-r) cnt)))))
        ;; accumulate to answer
        (for ([r (in-range k)])
          (let ((cnt (vector-ref nxt r)))
            (when (> cnt 0)
              (vector-set! ans r (+ (vector-ref ans r) cnt)))))
        ;; update cur for next iteration
        (for ([i (in-range k)])
          (vector-set! cur i (vector-ref nxt i)))))
    (vector->list ans)))
```

## Erlang

```erlang
-module(solution).
-export([result_array/2]).

%% Increment element at position Index by Inc in a list.
-spec inc_at(integer(), integer(), [integer()]) -> [integer()].
inc_at(0, Inc, [H|T]) ->
    [(H + Inc) | T];
inc_at(N, Inc, [H|T]) when N > 0 ->
    [H | inc_at(N - 1, Inc, T)].

%% Element‑wise addition of two equal‑length lists.
-spec add_lists([integer()], [integer()]) -> [integer()].
add_lists([], []) -> [];
add_lists([X|Xs], [Y|Ys]) ->
    [X + Y | add_lists(Xs, Ys)].

%% Combine previous subarray counts with current element modulo K.
-spec combine_prev([integer()], integer(), [integer()], integer(), integer()) -> [integer()].
combine_prev([], _A, NextAcc, _Idx, _K) ->
    NextAcc;
combine_prev([Cnt|Rest], A, NextAcc, Idx, K) ->
    NewNext = case Cnt of
        0 -> NextAcc;
        _ ->
            R = (Idx * A) rem K,
            inc_at(R, Cnt, NextAcc)
    end,
    combine_prev(Rest, A, NewNext, Idx + 1, K).

%% Main function: count subarrays by product modulo K.
-spec result_array([integer()], integer()) -> [integer()].
result_array(Nums, K) ->
    Zero = lists:duplicate(K, 0),
    {_, Res} = lists:foldl(
        fun(Num, {Prev, Acc}) ->
            A = Num rem K,
            NextStart = inc_at(A, 1, Zero),               % subarray consisting of only Num
            Next = combine_prev(Prev, A, NextStart, 0, K),
            NewAcc = add_lists(Acc, Next),
            {Next, NewAcc}
        end,
        {Zero, Zero},
        Nums
    ),
    Res.
```

## Elixir

```elixir
defmodule Solution do
  @spec result_array(nums :: [integer], k :: integer) :: [integer]
  def result_array(nums, k) do
    init_dp = List.duplicate(0, k)
    init_ans = List.duplicate(0, k)

    {_, final_ans} =
      Enum.reduce(nums, {init_dp, init_ans}, fn num, {prev_dp, acc_ans} ->
        a = rem(num, k)

        # start new subarray consisting only of current element
        cur = List.update_at(List.duplicate(0, k), a, fn v -> v + 1 end)

        # extend previous subarrays
        cur =
          Enum.with_index(prev_dp)
          |> Enum.reduce(cur, fn {cnt, idx}, acc ->
            if cnt == 0 do
              acc
            else
              new_rem = rem(idx * a, k)
              List.update_at(acc, new_rem, fn v -> v + cnt end)
            end
          end)

        # accumulate results
        new_ans =
          Enum.map(Enum.with_index(acc_ans), fn {cnt, idx} ->
            cnt + Enum.at(cur, idx)
          end)

        {cur, new_ans}
      end)

    final_ans
  end
end
```
