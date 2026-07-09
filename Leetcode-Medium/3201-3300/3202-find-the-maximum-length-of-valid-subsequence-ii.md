# 3202. Find the Maximum Length of Valid Subsequence II

## Cpp

```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<vector<int>> dp(k, vector<int>(k, 0));
        vector<int> cnt(k, 0);
        int ans = 1; // at least one element
        for (int num : nums) {
            int cur = num % k;
            for (int prev = 0; prev < k; ++prev) {
                if (cnt[prev] > 0) {
                    dp[prev][cur] = max(dp[prev][cur], 2);
                }
                if (dp[cur][prev] > 0) {
                    dp[prev][cur] = max(dp[prev][cur], dp[cur][prev] + 1);
                }
                ans = max(ans, dp[prev][cur]);
            }
            cnt[cur]++; // include current element for future pairs
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumLength(int[] nums, int k) {
        int[][] dp = new int[k][k]; // dp[i][j]: max length ending with remainders i (second last), j (last)
        int[] single = new int[k];   // whether a remainder has appeared at least once
        int ans = 0;
        for (int num : nums) {
            int r = num % k;
            ans = Math.max(ans, 1); // subsequence of length 1

            for (int p = 0; p < k; ++p) {
                if (single[p] > 0) {               // start a new pair
                    dp[p][r] = Math.max(dp[p][r], single[p] + 1);
                }
                if (dp[r][p] > 0) {                 // extend an existing alternating subsequence
                    dp[p][r] = Math.max(dp[p][r], dp[r][p] + 1);
                }
            }

            for (int p = 0; p < k; ++p) {
                ans = Math.max(ans, dp[p][r]);
            }

            single[r] = Math.max(single[r], 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        # Try each possible value of (first + second) % k
        for val in range(k):
            dp = [0] * k  # dp[r] = max length ending with remainder r
            for num in nums:
                cur = num % k
                prev = (val - cur) % k
                cand = dp[prev] + 1 if dp[prev] else 1
                if cand > dp[cur]:
                    dp[cur] = cand
                if dp[cur] > ans:
                    ans = dp[cur]
        return ans
```

## Python3

```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        ans = 0
        for num in nums:
            cur = num % k
            # start a subsequence of length 1
            if dp[cur][cur] < 1:
                dp[cur][cur] = 1
                ans = max(ans, 1)
            # snapshot the row where second-last remainder is cur
            prev_row = dp[cur][:]
            for prev in range(k):
                if prev_row[prev]:
                    new_len = prev_row[prev] + 1
                    if dp[prev][cur] < new_len:
                        dp[prev][cur] = new_len
                        ans = max(ans, new_len)
        return ans
```

## C

```c
#include <string.h>

int maximumLength(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int val = 0; val < k; ++val) {
        int dp[1005];
        memset(dp, 0, sizeof(int) * k);
        for (int i = 0; i < numsSize; ++i) {
            int cur = nums[i] % k;
            int prev = val - cur;
            prev %= k;
            if (prev < 0) prev += k;
            int cand = dp[prev] + 1;
            if (cand > dp[cur]) dp[cur] = cand;
            if (dp[cur] < 1) dp[cur] = 1;
        }
        for (int i = 0; i < k; ++i) {
            if (dp[i] > ans) ans = dp[i];
        }
    }
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaximumLength(int[] nums, int k) {
        int n = nums.Length;
        int[,] dp = new int[k, k]; // dp[prev][last]
        int[] best = new int[k];   // longest subsequence ending with remainder r
        int answer = 0;

        foreach (int num in nums) {
            int cur = ((num % k) + k) % k;

            // snapshot of best before using current element as previous
            int[] prevBest = new int[k];
            Array.Copy(best, prevBest, k);

            // try to form/extend subsequences ending with remainder cur
            for (int p = 0; p < k; ++p) {
                // start a new pair using a previous subsequence that ends with remainder p
                if (prevBest[p] > 0) {
                    int cand = prevBest[p] + 1;
                    if (cand > dp[p, cur]) dp[p, cur] = cand;
                }

                // extend an alternating pattern: ... cur , p -> add cur as new element
                int ext = dp[cur, p];
                if (ext > 0) {
                    int cand2 = ext + 1;
                    if (cand2 > dp[p, cur]) dp[p, cur] = cand2;
                }

                // update answer with the best length for this pair
                if (dp[p, cur] > answer) answer = dp[p, cur];
            }

            // ensure a single element subsequence exists
            if (best[cur] < 1) best[cur] = 1;
            if (best[cur] > answer) answer = best[cur];

            // update best ending with remainder cur using any pair that ends with cur
            int maxEndCur = best[cur];
            for (int p = 0; p < k; ++p) {
                if (dp[p, cur] > maxEndCur) maxEndCur = dp[p, cur];
            }
            best[cur] = maxEndCur;
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
var maximumLength = function(nums, k) {
    const dp = Array.from({ length: k }, () => new Int32Array(k));
    const seen = new Uint16Array(k);
    let ans = nums.length > 0 ? 1 : 0;
    
    for (const num of nums) {
        const cur = ((num % k) + k) % k; // ensure non‑negative remainder
        
        // Extend existing subsequences where the last two remainders are (cur, prev)
        for (let prev = 0; prev < k; ++prev) {
            const len = dp[cur][prev];
            if (len > 0) {
                const newLen = len + 1;
                if (newLen > dp[prev][cur]) dp[prev][cur] = newLen;
                if (newLen > ans) ans = newLen;
            }
        }
        
        // Start a new pair with any previously seen remainder
        for (let prev = 0; prev < k; ++prev) {
            if (seen[prev] > 0) {
                if (dp[prev][cur] < 2) dp[prev][cur] = 2;
                if (ans < 2) ans = 2;
            }
        }
        
        seen[cur]++;
    }
    
    return ans;
};
```

## Typescript

```typescript
function maximumLength(nums: number[], k: number): number {
    const best = new Array(k).fill(0);
    const dp: number[][] = Array.from({ length: k }, () => new Array(k).fill(0));
    let ans = 0;
    for (const num of nums) {
        const r = ((num % k) + k) % k;
        const oldBest = best.slice();
        const oldRow = dp[r].slice(); // copy row where first index is r
        if (best[r] < 1) best[r] = 1;
        for (let p = 0; p < k; ++p) {
            if (oldBest[p] > 0) {
                const cand = oldBest[p] + 1;
                if (cand > dp[p][r]) dp[p][r] = cand;
            }
            if (oldRow[p] > 0) {
                const cand = oldRow[p] + 1;
                if (cand > dp[p][r]) dp[p][r] = cand;
            }
        }
        for (let p = 0; p < k; ++p) {
            if (dp[p][r] > best[r]) best[r] = dp[p][r];
        }
        if (best[r] > ans) ans = best[r];
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
    function maximumLength($nums, $k) {
        // dp[i][j] = max length of a valid subsequence whose last two remainders are i (second last) and j (last)
        $dp = array_fill(0, $k, array_fill(0, $k, 0));
        // single[r] = max length of a valid subsequence ending with remainder r (any parity), at least 1
        $single = array_fill(0, $k, 0);
        $ans = 0;

        foreach ($nums as $num) {
            $c = $num % $k;
            // ensure single element subsequence exists
            if ($single[$c] < 1) {
                $single[$c] = 1;
                if ($ans < 1) $ans = 1;
            }

            // keep a copy of the row dp[c][*] before we modify it in this iteration
            $oldRow = $dp[$c];

            for ($p = 0; $p < $k; ++$p) {
                // start/extend from a subsequence that ends with remainder $p (single element or longer)
                if ($single[$p] > 0) {
                    $len = $single[$p] + 1;
                    if ($len > $dp[$p][$c]) {
                        $dp[$p][$c] = $len;
                        if ($len > $ans) $ans = $len;
                    }
                }

                // extend an alternating pattern where the last two remainders are (c, p)
                $prevLen = $oldRow[$p];
                if ($prevLen > 0) {
                    $len2 = $prevLen + 1;
                    if ($len2 > $dp[$p][$c]) {
                        $dp[$p][$c] = $len2;
                        if ($len2 > $ans) $ans = $len2;
                    }
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: k), count: k)
        var seen = Array(repeating: false, count: k)
        var ans = 0
        for num in nums {
            let cur = ((num % k) + k) % k
            if dp[cur][cur] < 1 {
                dp[cur][cur] = 1
                if ans < 1 { ans = 1 }
            }
            // start a subsequence of length 2 with any previously seen remainder
            for prev in 0..<k where seen[prev] {
                if dp[prev][cur] < 2 {
                    dp[prev][cur] = 2
                    if ans < 2 { ans = 2 }
                }
            }
            // extend existing alternating subsequences
            let oldRow = dp[cur]
            for prev in 0..<k {
                let val = oldRow[prev]
                if val > 0 {
                    let newLen = val + 1
                    if dp[prev][cur] < newLen {
                        dp[prev][cur] = newLen
                        if ans < newLen { ans = newLen }
                    }
                }
            }
            seen[cur] = true
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        val dp = Array(k) { IntArray(k) }
        var answer = 0
        for (num in nums) {
            val cur = ((num % k) + k) % k
            val prevVals = dp[cur].clone()
            for (prev in 0 until k) {
                val cand = prevVals[prev] + 1
                if (cand > dp[prev][cur]) {
                    dp[prev][cur] = cand
                    if (cand > answer) answer = cand
                }
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumLength(List<int> nums, int k) {
    // DP table where dp[i][j] is the max length of a valid subsequence
    // whose last two elements have remainders i (second last) and j (last).
    List<List<int>> dp = List.generate(k, (_) => List.filled(k, 0));
    for (int num in nums) {
      int cur = ((num % k) + k) % k;
      // Snapshot of the row corresponding to 'cur' before we modify dp.
      List<int> rowCur = List.from(dp[cur]);
      for (int prev = 0; prev < k; ++prev) {
        int candidate = rowCur[prev] + 1;
        if (candidate > dp[prev][cur]) {
          dp[prev][cur] = candidate;
        }
      }
    }
    int ans = 0;
    for (int i = 0; i < k; ++i) {
      for (int j = 0; j < k; ++j) {
        if (dp[i][j] > ans) ans = dp[i][j];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maximumLength(nums []int, k int) int {
    // dp[i][j] = max length of a valid subsequence whose last two elements
    // have remainders i (second‑last) and j (last) modulo k.
    dp := make([][]int, k)
    for i := 0; i < k; i++ {
        dp[i] = make([]int, k)
    }
    seen := make([]bool, k) // whether a remainder has appeared at least once
    ans := 1                // at least one element can always be taken

    for _, v := range nums {
        cur := v % k

        // snapshot the row dp[cur][*] before we start updating with this element
        prevRow := make([]int, k)
        copy(prevRow, dp[cur])

        for prev := 0; prev < k; prev++ {
            // Extend an existing subsequence whose last two remainders are (cur, prev)
            if prevRow[prev] > 0 {
                if newLen := prevRow[prev] + 1; dp[prev][cur] < newLen {
                    dp[prev][cur] = newLen
                    if ans < newLen {
                        ans = newLen
                    }
                }
            }
            // Start a new pair from a single element with remainder 'prev'
            if seen[prev] {
                if dp[prev][cur] < 2 {
                    dp[prev][cur] = 2
                    if ans < 2 {
                        ans = 2
                    }
                }
            }
        }

        // mark current remainder as seen for future pairs
        seen[cur] = true
    }

    return ans
}
```

## Ruby

```ruby
def maximum_length(nums, k)
  # single[i] = max length of a valid subsequence ending with remainder i
  single = Array.new(k, 0)
  # dp[i][j] = max length of a valid subsequence whose last two remainders are i (second‑last) and j (last)
  dp = Array.new(k) { Array.new(k, 0) }
  ans = 0

  nums.each do |num|
    cur = num % k
    # start a new subsequence of length 1 if not already present
    if single[cur] < 1
      single[cur] = 1
      ans = [ans, 1].max
    end

    old_single = single.dup          # state before this element
    old_row = dp[cur].dup            # dp[cur][*] before updates

    (0...k).each do |prev|
      # extend from a subsequence whose last two remainders are cur, prev
      if old_row[prev] > 0
        new_len = old_row[prev] + 1
        if new_len > dp[prev][cur]
          dp[prev][cur] = new_len
          ans = [ans, new_len].max
          single[cur] = [single[cur], new_len].max
        end
      end

      # start/extend from any subsequence ending with remainder prev
      if old_single[prev] > 0
        new_len2 = old_single[prev] + 1
        if new_len2 > dp[prev][cur]
          dp[prev][cur] = new_len2
          ans = [ans, new_len2].max
          single[cur] = [single[cur], new_len2].max
        end
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int], k: Int): Int = {
        val dp = Array.ofDim[Int](k, k)
        val seen = new Array[Boolean](k)
        var ans = 1 // at least one element can be taken

        for (num <- nums) {
            val cur = ((num % k) + k) % k
            for (prev <- 0 until k) {
                var best = 0
                if (dp(cur)(prev) > 0) {
                    best = dp(cur)(prev) + 1
                } else if (seen(prev)) {
                    best = 2
                }
                if (best > dp(prev)(cur)) {
                    dp(prev)(cur) = best
                }
            }
            seen(cur) = true
        }

        for (i <- 0 until k; j <- 0 until k) {
            if (dp(i)(j) > ans) ans = dp(i)(j)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 1;
        let k_usize = k as usize;
        for val in 0..k {
            let mut dp = vec![0i32; k_usize];
            for &num in nums.iter() {
                let r = ((num % k) + k) % k;
                let p = ((val - r) % k + k) % k;
                let ri = r as usize;
                let pi = p as usize;
                if dp[pi] > 0 {
                    dp[ri] = dp[ri].max(dp[pi] + 1);
                }
                dp[ri] = dp[ri].max(1);
            }
            for &len in dp.iter() {
                if len > ans {
                    ans = len;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((kvec (make-vector k))
         (dp (for/vector ([i (in-range k)]) (make-vector k 0)))
         (best-start (make-vector k 0))
         (ans 0))
    (for ([num nums])
      (define cur (remainder num k))
      ;; extend from single-element subsequences
      (for ([prev (in-range k)])
        (let ((bs (vector-ref best-start prev)))
          (when (> bs 0)
            (let* ((old (vector-ref (vector-ref dp prev) cur))
                   (new (+ bs 1)))
              (when (> new old)
                (vector-set! (vector-ref dp prev) cur new))))))
      ;; extend from existing pairs
      (for ([prev (in-range k)])
        (let ((val (vector-ref (vector-ref dp cur) prev)))
          (when (> val 0)
            (let* ((old (vector-ref (vector-ref dp prev) cur))
                   (new (+ val 1)))
              (when (> new old)
                (vector-set! (vector-ref dp prev) cur new))))))
      ;; ensure single element subsequence exists
      (let ((cur-best (vector-ref best-start cur)))
        (when (< cur-best 1)
          (vector-set! best-start cur 1)))
      )
    ;; compute answer
    (for ([i (in-range k)])
      (set! ans (max ans (vector-ref best-start i)))
      (let ((row (vector-ref dp i)))
        (for ([j (in-range k)])
          (set! ans (max ans (vector-ref row j))))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([maximum_length/2]).

maximum_length(Nums, K) ->
    Dp0 = #{},
    Cnt0 = #{},
    {DpFinal,_} = lists:foldl(fun(Num, {DP, CNT}) ->
        Cur = Num rem K,
        %% start new length‑2 subsequences using previous remainders
        PrevKeys = maps:keys(CNT),
        DP1 = lists:foldl(fun(Prev, Acc) ->
                Key = {Prev, Cur},
                case maps:get(Key, Acc, 0) of
                    Old when Old < 2 -> maps:put(Key, 2, Acc);
                    _ -> Acc
                end
            end, DP, PrevKeys),
        %% extend existing sequences where last two remainders are (Cur,Prev)
        DP2 = lists:foldl(fun(Prev, Acc) ->
                Len = maps:get({Cur, Prev}, Acc, 0),
                if Len > 0 ->
                        NewLen = Len + 1,
                        Key = {Prev, Cur},
                        case maps:get(Key, Acc, 0) of
                            Old when NewLen > Old -> maps:put(Key, NewLen, Acc);
                            _ -> Acc
                        end;
                   true -> Acc
                end
            end, DP1, lists:seq(0, K-1)),
        %% update count map for current remainder
        CNT2 = case maps:get(Cur, CNT, 0) of
                    C -> maps:put(Cur, C + 1, CNT)
               end,
        {DP2, CNT2}
    end, {Dp0, Cnt0}, Nums),
    MaxLen = case maps:values(DpFinal) of
                [] -> 0;
                Vs -> lists:max(Vs)
             end,
    if MaxLen < 1 -> 1; true -> MaxLen end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer], k :: integer) :: integer
  def maximum_length(nums, k) do
    {_, _, answer} =
      Enum.reduce(nums, {%{}, MapSet.new(), if(nums == [], do: 0, else: 1)}, fn num,
                                                                              {dp, seen, ans} ->
        cur = rem(num, k)

        # Start new pairs with previously seen remainders (length 2)
        dp_after_pairs =
          Enum.reduce(0..k - 1, dp, fn prev, acc_dp ->
            if MapSet.member?(seen, prev) do
              key = {prev, cur}
              case Map.get(acc_dp, key, 0) do
                existing when existing < 2 -> Map.put(acc_dp, key, 2)
                _ -> acc_dp
              end
            else
              acc_dp
            end
          end)

        # Extend existing sequences where the remainder two steps back equals cur
        {dp_after_extend, ans_after_extend} =
          Enum.reduce(0..k - 1, {dp_after_pairs, ans}, fn prev,
                                                         {inner_dp, inner_ans} ->
            len = Map.get(inner_dp, {cur, prev}, 0)

            if len > 0 do
              new_len = len + 1
              key = {prev, cur}
              updated_dp =
                case Map.get(inner_dp, key, 0) do
                  existing when existing < new_len -> Map.put(inner_dp, key, new_len)
                  _ -> inner_dp
                end

              {updated_dp, max(inner_ans, new_len)}
            else
              {inner_dp, inner_ans}
            end
          end)

        # Record current remainder as seen
        {dp_after_extend, MapSet.put(seen, cur), ans_after_extend}
      end)

    answer
  end
end
```
