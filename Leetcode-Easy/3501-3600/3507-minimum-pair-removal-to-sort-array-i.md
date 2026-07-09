# 3507. Minimum Pair Removal to Sort Array I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        const int INF = 1e9;
        int n = nums.size();
        // memo[pos][last+1], where last = -1..n-1
        vector<vector<int>> dp(n + 1, vector<int>(n + 2, -1));
        function<int(int,int)> solve = [&](int pos, int lastIdx) -> int {
            if (pos == n) return 0;
            int &res = dp[pos][lastIdx + 1];
            if (res != -1) return res;
            res = INF;
            // Option 1: keep nums[pos] if non-decreasing
            if (lastIdx == -1 || nums[pos] >= nums[lastIdx]) {
                res = min(res, solve(pos + 1, pos));
            }
            // Option 2: delete a pair starting at pos
            if (pos + 1 < n) {
                int cand = solve(pos + 2, lastIdx);
                if (cand != INF) res = min(res, 1 + cand);
            }
            return res;
        };
        return solve(0, -1);
    }
};
```

## Java

```java
class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int best = 0;
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] <= nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            best = Math.max(best, dp[i]);
        }
        int removed = n - best;
        return (removed + 1) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] <= nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        lnds = max(dp)
        return n - lnds
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9

        @lru_cache(None)
        def dp(i: int, prev: int) -> int:
            # prev is sentinel -1001 meaning no previous kept element
            if i >= n:
                return 0
            # option to keep current if possible
            best = INF
            cur = nums[i]
            if prev == -1001 or cur >= prev:
                best = dp(i + 1, cur)
            # option to delete a pair starting at i
            if i + 1 < n:
                best = min(best, 1 + dp(i + 2, prev))
            return best

        ans = dp(0, -1001)
        return ans
```

## C

```c
int dp[51][52];
int *gnums;
int gn;

int solve(int i, int lastIdx) {
    if (i >= gn) return 0;
    int &res = dp[i][lastIdx + 1];
    if (res != -1) return res;
    const int INF = 1000;
    res = INF;
    int prevVal = (lastIdx == -1 ? -2000 : gnums[lastIdx]);
    // keep current element
    if (gnums[i] >= prevVal) {
        int cand = solve(i + 1, i);
        if (cand < res) res = cand;
    }
    // delete a pair starting at i
    if (i + 1 < gn) {
        int cand = 1 + solve(i + 2, lastIdx);
        if (cand < res) res = cand;
    }
    return res;
}

int minimumPairRemoval(int* nums, int numsSize) {
    gnums = nums;
    gn = numsSize;
    for (int i = 0; i <= gn; ++i)
        for (int j = 0; j < 52; ++j)
            dp[i][j] = -1;
    return solve(0, -1);
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        int n = nums.Length;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) dp[i] = -1;

        for (int i = 0; i < n; i++) {
            if ((i & 1) == 0) dp[i] = 1; // can start at even index
            for (int j = 0; j < i; j++) {
                if (dp[j] == -1) continue;
                if (((i - j) & 1) == 1 && nums[j] <= nums[i]) {
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
        }

        int best = 0; // empty subsequence is always valid
        for (int i = 0; i < n; i++) {
            if (dp[i] == -1) continue;
            if (((n - 1 - i) & 1) == 0) { // suffix length even
                best = Math.Max(best, dp[i]);
            }
        }

        return (n - best) / 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumPairRemoval = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    const dp = new Array(n).fill(1);
    let best = 1;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] <= nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        best = Math.max(best, dp[i]);
    }
    return n - best;
};
```

## Typescript

```typescript
function minimumPairRemoval(nums: number[]): number {
    const n = nums.length;
    const memo: number[][] = Array.from({ length: n + 1 }, () => Array(n + 1).fill(-1));
    const INF = 1e9;

    function dfs(pos: number, lastIdx: number): number {
        if (pos >= n) return 0;
        const keyLast = lastIdx + 1; // shift -1 to 0
        if (memo[pos][keyLast] !== -1) return memo[pos][keyLast];

        let best = INF;

        // Keep current element if it maintains non-decreasing order
        if (lastIdx === -1 || nums[lastIdx] <= nums[pos]) {
            const keep = dfs(pos + 1, pos);
            if (keep < best) best = keep;
        }

        // Remove a pair starting at current position
        if (pos + 1 < n) {
            const removePair = 1 + dfs(pos + 2, lastIdx);
            if (removePair < best) best = removePair;
        }

        memo[pos][keyLast] = best;
        return best;
    }

    return dfs(0, -1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumPairRemoval($nums) {
        $n = count($nums);
        if ($n <= 1) return 0;
        // dp[i] = longest valid subsequence ending at i
        $dp = array_fill(0, $n, -1000);
        for ($i = 0; $i < $n; $i++) {
            if (($i & 1) == 0) { // start must be even index
                $dp[$i] = 1;
            }
        }
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ((($i - $j) & 1) == 1 && $nums[$j] <= $nums[$i] && $dp[$j] > 0) {
                    $dp[$i] = max($dp[$i], $dp[$j] + 1);
                }
            }
        }
        $best = 0;
        $endParity = ($n - 1) & 1; // last kept index must have this parity
        for ($i = 0; $i < $n; $i++) {
            if ((($i & 1) == $endParity) && $dp[$i] > $best) {
                $best = $dp[$i];
            }
        }
        // operations needed = (total elements - kept elements) / 2
        return intdiv($n - $best, 2);
    }
}
```

## Swift

```swift
class Solution {
    func minimumPairRemoval(_ nums: [Int]) -> Int {
        var arr = nums
        var operations = 0
        while true {
            var idx = -1
            for i in 0..<(arr.count - 1) {
                if arr[i] > arr[i + 1] {
                    idx = i
                    break
                }
            }
            if idx == -1 { break }
            // Remove the decreasing adjacent pair
            arr.remove(at: idx + 1)
            arr.remove(at: idx)
            operations += 1
        }
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumPairRemoval(nums: IntArray): Int {
        val n = nums.size
        val dp = IntArray(n)
        var maxLen = if (n % 2 == 0) 0 else 1  // baseline for parity constraint
        for (i in 0 until n) {
            dp[i] = if (i % 2 == 0) 1 else 0
            for (j in 0 until i) {
                if ((i % 2 != j % 2) && nums[j] <= nums[i] && dp[j] > 0) {
                    dp[i] = maxOf(dp[i], dp[j] + 1)
                }
            }
            if (dp[i] > 0 && dp[i] % 2 == n % 2) {
                maxLen = maxOf(maxLen, dp[i])
            }
        }
        return (n - maxLen) / 2
    }
}
```

## Dart

```dart
class Solution {
  int minimumPairRemoval(List<int> nums) {
    int n = nums.length;
    if (n == 0) return 0;
    List<int> dp = List.filled(n, 1);
    int best = 1;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (nums[j] <= nums[i]) {
          dp[i] = dp[i].clamp(1, dp[j] + 1);
          if (dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
        }
      }
      if (dp[i] > best) best = dp[i];
    }
    return n - best;
  }
}
```

## Golang

```go
func minimumPairRemoval(nums []int) int {
    n := len(nums)
    const negInf = -1 << 60
    dp := make([]int, n)
    for i := range dp {
        dp[i] = negInf
    }
    // build DP for subsequences respecting parity constraints
    for i := 0; i < n; i++ {
        if i%2 == 0 { // can start at even index
            dp[i] = 1
        }
        for j := 0; j < i; j++ {
            if dp[j] != negInf && nums[j] <= nums[i] && (i-j)%2 == 1 {
                if cand := dp[j] + 1; cand > dp[i] {
                    dp[i] = cand
                }
            }
        }
    }

    best := 0
    // subsequence must end at index with same parity as n-1 (suffix deletions even)
    for i := 0; i < n; i++ {
        if (n-1-i)%2 == 0 && dp[i] > best {
            best = dp[i]
        }
    }

    // If no valid subsequence and n is even, we can delete all elements
    if best == 0 && n%2 == 0 {
        best = 0
    }

    return (n - best) / 2
}
```

## Ruby

```ruby
def minimum_pair_removal(nums)
  stack = []
  ops = 0
  nums.each do |x|
    if stack.empty? || x >= stack[-1]
      stack << x
    else
      ops += 1
      stack.pop
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
  def minimumPairRemoval(nums: Array[Int]): Int = {
    import scala.util.control.Breaks.{break, breakable}
    var ops = 0
    val stack = new scala.collection.mutable.ArrayStack[Int]()
    for (x <- nums) {
      stack.push(x)
      breakable {
        while (stack.size >= 2) {
          val last = stack.pop()
          val second = stack.pop()
          if (second > last) {
            ops += 1
          } else {
            stack.push(second)
            stack.push(last)
            break
          }
        }
      }
    }
    ops
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut dp = vec![1usize; n];
        let mut best = 1usize;
        for i in 0..n {
            for j in 0..i {
                if nums[j] <= nums[i] && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1;
                }
            }
            if dp[i] > best {
                best = dp[i];
            }
        }
        (n - best) as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-pair-removal nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums))
         (dp (make-vector n -1000))) ; sentinel for impossible
    (define (even? x) (= (remainder x 2) 0))
    ;; initialize and transition
    (for ([i (in-range n)])
      (when (even? i)                     ; prefix before first kept must be even
        (vector-set! dp i 1))             ; keep only nums[i]
      (for ([j (in-range i)])
        (when (and (<= (vector-ref v j) (vector-ref v i))
                   (even? (- i j 1)))    ; gap between kept elements must be even
          (let ((cand (+ (vector-ref dp j) 1)))
            (when (> cand (vector-ref dp i))
              (vector-set! dp i cand))))))
    ;; find best length respecting suffix parity
    (let ((best (if (even? n) 0 -1000))) ; empty subsequence allowed when n even
      (for ([i (in-range n)])
        (let ((val (vector-ref dp i)))
          (when (and (>= val 0) (even? (- n i 1))) ; suffix after last kept must be even
            (set! best (max best val)))))
      (/ (- n best) 2))))
```

## Erlang

```erlang
-spec minimum_pair_removal(Nums :: [integer()]) -> integer().
minimum_pair_removal(Nums) ->
    N = length(Nums),
    LastParity = (N - 1) band 1,
    Indices = lists:seq(0, N - 1),
    DPList = loop(Indices, Nums, [], []),
    MaxK = max_k(DPList, LastParity, 0, 0),
    (N - MaxK) div 2.

%% Build DP list where DP[i] is the longest valid subsequence ending at index i
loop([], _Nums, _Processed, DPs) ->
    lists:reverse(DPs);
loop([I | Rest], Nums, Processed, DPs) ->
    Val = lists:nth(I + 1, Nums),
    Start = case I band 1 of
                0 -> 1;
                _ -> 0
            end,
    MaxPrev = max_prev(I, Val, Processed, 0),
    DP_i = if Start > MaxPrev -> Start; true -> MaxPrev end,
    NewProcessed = [{I, Val, DP_i} | Processed],
    loop(Rest, Nums, NewProcessed, [DP_i | DPs]).

%% Find best previous DP where indices differ by odd and values are non‑decreasing
max_prev(_I, _Val, [], Best) ->
    Best;
max_prev(I, Val, [{J, Vj, DPj} | Rest], Best) ->
    DiffParity = ((I - J) band 1),
    Candidate = if DiffParity == 1, Val >= Vj -> DPj + 1; true -> Best end,
    NewBest = case Candidate > Best of
                 true -> Candidate;
                 false -> Best
             end,
    max_prev(I, Val, Rest, NewBest).

%% Get the maximum DP value whose index parity matches the required ending parity
max_k([], _Parity, _Idx, Max) ->
    Max;
max_k([DPi | Rest], Parity, Idx, Max) ->
    NewMax = if (Idx band 1) == Parity, DPi > Max -> DPi; true -> Max end,
    max_k(Rest, Parity, Idx + 1, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_pair_removal(nums :: [integer]) :: integer
  def minimum_pair_removal(nums) do
    {ops, _stack} =
      Enum.reduce(nums, {0, []}, fn x, {cnt, []} ->
        {cnt, [x]}
      end, fn x, {cnt, [top | rest] = stack} ->
        if top > x do
          {cnt + 1, rest}
        else
          {cnt, [x | stack]}
        end
      end)

    ops
  end
end
```
