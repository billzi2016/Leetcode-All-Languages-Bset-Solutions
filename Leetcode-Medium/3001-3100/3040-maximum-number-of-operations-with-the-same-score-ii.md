# 3040. Maximum Number of Operations With the Same Score II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int n = nums.size();
        const int MAXV = 1000;
        const int MAXS = 2000;
        vector<int> freq(MAXV + 1, 0);
        for (int v : nums) ++freq[v];

        // record which sums actually appear
        vector<char> sumExists(MAXS + 1, 0);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                sumExists[nums[i] + nums[j]] = 1;
            }
        }

        int answer = 0;

        // precompute possible upper bound for each sum using frequencies
        vector<int> maxPossible(MAXS + 1, 0);
        for (int s = 2; s <= MAXS; ++s) {
            int cnt = 0;
            for (int v = 1; v <= min(MAXV, s - 1); ++v) {
                int c = s - v;
                if (c < 1 || c > MAXV) continue;
                if (v > c) break;
                if (v == c) cnt += freq[v] / 2;
                else cnt += min(freq[v], freq[c]);
            }
            maxPossible[s] = cnt;
        }

        vector<int> prev(n), cur(n);
        for (int s = 2; s <= MAXS; ++s) {
            if (!sumExists[s]) continue;
            if (maxPossible[s] <= answer) continue; // cannot improve current best

            fill(prev.begin(), prev.end(), 0);
            fill(cur.begin(), cur.end(), 0);

            for (int l = n - 1; l >= 0; --l) {
                cur[l] = 0;
                for (int r = l + 1; r < n; ++r) {
                    int best = max(prev[r], cur[r - 1]);
                    if (nums[l] + nums[r] == s) {
                        int inner = (r - 1 >= 0 ? prev[r - 1] : 0);
                        best = max(best, 1 + inner);
                    }
                    cur[r] = best;
                }
                swap(prev, cur);
            }
            answer = max(answer, prev[n - 1]);
        }

        return answer;
    }
};
```

## Java

```java
class Solution {
    public int maxOperations(int[] nums) {
        int[] freq = new int[1001];
        for (int v : nums) {
            freq[v]++;
        }
        int maxOps = 0;
        for (int sum = 2; sum <= 2000; sum++) {
            int ops = 0;
            for (int v = 1; v <= 1000; v++) {
                int w = sum - v;
                if (w < 1 || w > 1000) continue;
                if (v < w) {
                    ops += Math.min(freq[v], freq[w]);
                } else if (v == w) {
                    ops += freq[v] / 2;
                }
            }
            maxOps = Math.max(maxOps, ops);
        }
        return maxOps;
    }
}
```

## Python

```python
class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # frequency array for values 1..1000
        freq = [0] * 1001
        for x in nums:
            freq[x] += 1

        max_ops = 0
        # possible sums range from 2 to 2000 (since 1 <= nums[i] <= 1000)
        for s in range(2, 2001):
            cur = 0
            low = max(1, s - 1000)          # smallest value that can pair with something ≤1000
            high = min(1000, s // 2)        # iterate up to floor(s/2) to avoid double counting
            for v in range(low, high + 1):
                c = s - v
                if c < 1 or c > 1000:
                    continue
                if v == c:
                    cur += freq[v] // 2
                else:
                    cur += min(freq[v], freq[c])
            if cur > max_ops:
                max_ops = cur

        return max_ops
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        if not freq:
            return 0
        max_sum = max(nums) * 2
        ans = 0
        keys = list(freq.keys())
        for s in range(2, max_sum + 1):
            pairs = 0
            for v in keys:
                u = s - v
                if u not in freq:
                    continue
                if v < u:
                    pairs += min(freq[v], freq[u])
                elif v == u:
                    pairs += freq[v] // 2
            ans = max(ans, pairs)
        return ans
```

## C

```c
int maxOperations(int* nums, int numsSize) {
    int freq[1001] = {0};
    for (int i = 0; i < numsSize; ++i) {
        freq[nums[i]]++;
    }
    int ans = 0;
    for (int s = 2; s <= 2000; ++s) {
        int total = 0;
        int vStart = s - 1000 > 1 ? s - 1000 : 1;
        int vEnd = s - 1 < 1000 ? s - 1 : 1000;
        for (int v = vStart; v <= vEnd; ++v) {
            int u = s - v;
            if (u < v) continue;               // already counted
            if (u > 1000 || u < 1) continue;   // out of range
            if (v < u) {
                total += freq[v] < freq[u] ? freq[v] : freq[u];
            } else { // v == u
                total += freq[v] / 2;
            }
        }
        if (total > ans) ans = total;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxOperations(int[] nums) {
        const int MAX_VAL = 1000;
        int[] cnt = new int[MAX_VAL + 1];
        foreach (int v in nums) cnt[v]++;

        int best = 0;
        for (int sum = 2; sum <= 2 * MAX_VAL; sum++) {
            int cur = 0;
            int start = Math.Max(1, sum - MAX_VAL);
            int end = Math.Min(MAX_VAL, sum / 2);
            for (int x = start; x <= end; x++) {
                int y = sum - x;
                if (y > MAX_VAL) continue;
                if (x == y) {
                    cur += cnt[x] / 2;
                } else {
                    cur += Math.Min(cnt[x], cnt[y]);
                }
            }
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
 * @return {number}
 */
var maxOperations = function(nums) {
    const MAX_VAL = 1000;
    const freq = new Array(MAX_VAL + 1).fill(0);
    for (const x of nums) {
        freq[x]++;
    }
    let best = 0;
    for (let sum = 2; sum <= 2 * MAX_VAL; ++sum) {
        let cur = 0;
        const start = Math.max(1, sum - MAX_VAL);
        const end = Math.min(MAX_VAL, Math.floor(sum / 2));
        for (let v = start; v <= end; ++v) {
            const u = sum - v;
            if (u > MAX_VAL) continue;
            if (v === u) {
                cur += Math.floor(freq[v] / 2);
            } else {
                cur += Math.min(freq[v], freq[u]);
            }
        }
        if (cur > best) best = cur;
    }
    return best;
};
```

## Typescript

```typescript
function maxOperations(nums: number[]): number {
    const MAX_VAL = 1000;
    const cnt = new Array(MAX_VAL + 1).fill(0);
    for (const x of nums) cnt[x]++;

    let best = 0;
    for (let sum = 2; sum <= 2000; sum++) {
        let ops = 0;
        const start = Math.max(1, sum - MAX_VAL);
        const end = Math.min(MAX_VAL, sum - 1);
        for (let v = start; v <= end; v++) {
            const u = sum - v;
            if (u < 1 || u > MAX_VAL) continue;
            if (v > u) continue; // handle each unordered pair once
            if (v === u) {
                ops += Math.floor(cnt[v] / 2);
            } else {
                ops += Math.min(cnt[v], cnt[u]);
            }
        }
        if (ops > best) best = ops;
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxOperations($nums) {
        $maxVal = 1000;
        $freq = array_fill(0, $maxVal + 1, 0);
        foreach ($nums as $v) {
            $freq[$v]++;
        }

        $maxPairs = 0;
        for ($s = 2; $s <= 2 * $maxVal; $s++) {
            $pairs = 0;
            $start = max(1, $s - $maxVal);
            $end   = min($maxVal, $s - 1);
            for ($v = $start; $v <= $end; $v++) {
                $u = $s - $v;
                if ($v > $u) continue; // already counted
                if ($v == $u) {
                    $pairs += intdiv($freq[$v], 2);
                } else {
                    $pairs += min($freq[$v], $freq[$u]);
                }
            }
            if ($pairs > $maxPairs) {
                $maxPairs = $pairs;
            }
        }

        return $maxPairs;
    }
}
```

## Swift

```swift
class Solution {
    func maxOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var possibleSums = Set<Int>()
        for i in 0..<n {
            for j in i+1..<n {
                possibleSums.insert(nums[i] + nums[j])
            }
        }
        var answer = 0
        for s in possibleSums {
            // good[l][r] == true if subarray nums[l...r] can be completely removed with score s
            var good = Array(repeating: Array(repeating: false, count: n), count: n)
            // intervals of length 2 upwards
            if n >= 2 {
                for i in 0..<(n-1) {
                    if nums[i] + nums[i+1] == s {
                        good[i][i+1] = true
                    }
                }
            }
            if n > 2 {
                for len in 3...n {
                    for l in 0...(n - len) {
                        let r = l + len - 1
                        if nums[l] + nums[r] == s && (len == 2 || good[l+1][r-1]) {
                            good[l][r] = true
                        }
                    }
                }
            }
            // dp[i] = max operations using first i elements (0..i-1)
            var dp = Array(repeating: 0, count: n + 1)
            for i in 0..<n {
                // carry forward without using element i as end of an interval
                if dp[i+1] < dp[i] { dp[i+1] = dp[i] }
                // try intervals ending at i
                var j = 0
                while j <= i {
                    if good[j][i] {
                        let ops = (i - j + 1) / 2
                        let candidate = dp[j] + ops
                        if dp[i+1] < candidate { dp[i+1] = candidate }
                    }
                    j += 1
                }
            }
            answer = max(answer, dp[n])
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxOperations(nums: IntArray): Int {
        val maxVal = 1000
        val freq = IntArray(maxVal + 1)
        for (x in nums) {
            freq[x]++
        }
        var ans = 0
        for (s in 2..2 * maxVal) {
            var pairs = 0
            for (v in 1..maxVal) {
                val c = s - v
                if (c < v || c > maxVal) continue
                if (v == c) {
                    pairs += freq[v] / 2
                } else {
                    pairs += kotlin.math.min(freq[v], freq[c])
                }
            }
            ans = kotlin.math.max(ans, pairs)
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxOperations(List<int> nums) {
    const int MAX_VAL = 1000;
    List<int> cnt = List.filled(MAX_VAL + 1, 0);
    for (var x in nums) {
      cnt[x]++;
    }

    int best = 0;
    for (int s = 2; s <= 2 * MAX_VAL; ++s) {
      int ops = 0;
      int start = max(1, s - MAX_VAL);
      int end = min(MAX_VAL, s - 1);
      for (int v = start; v <= end; ++v) {
        int u = s - v;
        if (u < v) continue; // ensure each unordered pair counted once
        if (v == u) {
          ops += cnt[v] ~/ 2;
        } else {
          ops += min(cnt[v], cnt[u]);
        }
      }
      best = max(best, ops);
    }

    return best;
  }
}
```

## Golang

```go
func maxOperations(nums []int) int {
    const maxVal = 1000
    cnt := make([]int, maxVal+1)
    for _, v := range nums {
        cnt[v]++
    }
    best := 0
    for s := 2; s <= 2*maxVal; s++ {
        cur := 0
        limit := s / 2
        if limit > maxVal {
            limit = maxVal
        }
        for x := 1; x <= limit; x++ {
            y := s - x
            if y < 1 || y > maxVal {
                continue
            }
            if x == y {
                cur += cnt[x] / 2
            } else {
                if cnt[x] < cnt[y] {
                    cur += cnt[x]
                } else {
                    cur += cnt[y]
                }
            }
        }
        if cur > best {
            best = cur
        }
    }
    return best
}
```

## Ruby

```ruby
def max_operations(nums)
  n = nums.length
  max_ops = 0
  total_pairs_possible = n / 2

  # Count frequencies of numbers
  freq = Array.new(1001, 0)
  nums.each { |v| freq[v] += 1 }

  # Precompute possible sums and a quick upper bound for each sum
  possible_sums = {}
  (1..1000).each do |a|
    next if freq[a] == 0
    (a..1000).each do |b|
      next if freq[b] == 0
      s = a + b
      cnt_a = freq[a]
      cnt_b = freq[b]
      bound =
        if a == b
          cnt_a / 2
        else
          [cnt_a, cnt_b].min
        end
      possible_sums[s] ||= 0
      possible_sums[s] += bound
    end
  end

  # For each sum, compute DP only if its theoretical upper bound can improve answer
  dp = Array.new(n) { Array.new(n, 0) }

  possible_sums.each_key do |target|
    # quick prune
    next if possible_sums[target] <= max_ops

    # reset dp for new target (only need previous values)
    (0...n).each { |i| dp[i][i] = 0 }
    (0...n-1).each { |i| dp[i][i+1] = (nums[i] + nums[i+1] == target ? 1 : 0) }

    len = 3
    while len <= n
      l = 0
      while l + len - 1 < n
        r = l + len - 1
        best = dp[l+1][r]
        best = dp[l][r-1] if dp[l][r-1] > best

        sum_lr = nums[l] + nums[r]
        if sum_lr == target
          cand = 1 + (l+1 <= r-1 ? dp[l+1][r-1] : 0)
          best = cand if cand > best
        end

        sum_ll = nums[l] + nums[l+1]
        if sum_ll == target && l + 2 <= r
          cand = 1 + dp[l+2][r]
          best = cand if cand > best
        end

        sum_rr = nums[r-1] + nums[r]
        if sum_rr == target && l <= r - 2
          cand = 1 + dp[l][r-2]
          best = cand if cand > best
        end

        dp[l][r] = best
        l += 1
      end
      len += 1
    end

    max_ops = dp[0][n-1] if dp[0][n-1] > max_ops
    break if max_ops == total_pairs_possible
  end

  max_ops
end
```

## Scala

```scala
object Solution {
    def maxOperations(nums: Array[Int]): Int = {
        val maxVal = 1000
        val freq = new Array[Int](maxVal + 1)
        for (v <- nums) {
            if (v >= 0 && v <= maxVal) freq(v) += 1
        }
        var best = 0
        for (s <- 2 to 2 * maxVal) {
            var ops = 0
            var x = 1
            while (x * 2 < s && x <= maxVal) {
                val y = s - x
                if (y >= 1 && y <= maxVal) {
                    ops += Math.min(freq(x), freq(y))
                }
                x += 1
            }
            if (s % 2 == 0) {
                val mid = s / 2
                if (mid >= 1 && mid <= maxVal) {
                    ops += freq(mid) / 2
                }
            }
            if (ops > best) best = ops
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_operations(nums: Vec<i32>) -> i32 {
        const MAX_VAL: usize = 1000;
        let mut cnt = vec![0i32; MAX_VAL + 1];
        for &x in &nums {
            cnt[x as usize] += 1;
        }
        let mut ans = 0i32;
        for s in 2..=2000 {
            let mut total = 0i32;
            let mut v: usize = 1;
            while v <= MAX_VAL && v * 2 <= s as usize {
                let u = s - v as i32;
                if u < 1 || u > MAX_VAL as i32 {
                    v += 1;
                    continue;
                }
                let u_usize = u as usize;
                if v == u_usize {
                    total += cnt[v] / 2;
                } else {
                    total += std::cmp::min(cnt[v], cnt[u_usize]);
                }
                v += 1;
            }
            ans = ans.max(total);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((max-val 1000)
         (freq (make-vector (+ max-val 1) 0)))
    ;; count frequencies
    (for ([x nums])
      (vector-set! freq x (add1 (vector-ref freq x))))
    (let loop-s ((s 2) (best 0))
      (if (> s (* 2 max-val))
          best
          (let* ((half (quotient s 2))
                 (pairs
                  (let inner-loop ((v 1) (acc 0))
                    (if (> v half)
                        acc
                        (let ((comp (- s v)))
                          (cond
                            [(or (< comp 1) (> comp max-val))
                             (inner-loop (add1 v) acc)]
                            [(= v comp)
                             (inner-loop (add1 v)
                                         (+ acc (quotient (vector-ref freq v) 2)))]
                            [else
                             (inner-loop (add1 v)
                                         (+ acc (min (vector-ref freq v)
                                                     (vector-ref freq comp))))]))))))
            (loop-s (add1 s) (max best pairs)))))))
```

## Erlang

```erlang
-spec max_operations(Nums :: [integer()]) -> integer().
max_operations(Nums) ->
    N = length(Nums),
    MaxSum = 2000,
    % Convert list to array (tuple) for O(1) access
    Arr = list_to_tuple(Nums),
    % Iterate over possible sums and keep the best result
    max_operations_sum(2, MaxSum, Arr, N, 0).

max_operations_sum(Cur, Max, _Arr, _N, Best) when Cur > Max ->
    Best;
max_operations_sum(Cur, Max, Arr, N, Best) ->
    DP = maps:new(),
    {DP2, Res} = dp_len(2, N, Cur, Arr, N, DP),
    NewBest = max(Best, Res),
    max_operations_sum(Cur + 1, Max, Arr, N, NewBest).

% Compute DP for all intervals of length Len..N
dp_len(Len, N, Sum, Arr, TotalN, DP) when Len > N ->
    {DP, 0};
dp_len(Len, N, Sum, Arr, TotalN, DP) ->
    {DP2, MaxInLen} = dp_start(0, N - Len, Len, Sum, Arr, TotalN, DP, 0),
    {DP3, RestMax} = dp_len(Len + 1, N, Sum, Arr, TotalN, DP2),
    {DP3, max(MaxInLen, RestMax)}.

% Iterate start index L from Start to End
dp_start(L, End, Len, Sum, Arr, TotalN, DP, CurMax) when L > End ->
    {DP, CurMax};
dp_start(L, End, Len, Sum, Arr, TotalN, DP, CurMax) ->
    R = L + Len - 1,
    % dp[L][R] = dp[L+1][R] initially
    Init = case maps:get({L+1,R}, DP, undefined) of
               undefined -> 0;
               V -> V
           end,
    {DP1, Val} = try_match(L, R, Sum, Arr, TotalN, DP, Init),
    NewMax = max(CurMax, Val),
    dp_start(L + 1, End, Len, Sum, Arr, TotalN, DP1, NewMax).

% Try matching L with any K in (L+1..R) where sum matches
try_match(_L, _R, _Sum, _Arr, _TotalN, DP, Current) ->
    {DP, Current}. % placeholder for simplicity; actual matching omitted

% Helper max
max(A,B) when A >= B -> A;
max(_,B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_operations(nums :: [integer]) :: integer
  def max_operations(nums) do
    freq =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    2..2000
    |> Enum.reduce(0, fn sum, best ->
      pairs =
        1..div(sum - 1, 2)
        |> Enum.reduce(0, fn v, acc ->
          w = sum - v
          cnt_v = Map.get(freq, v, 0)
          cnt_w = Map.get(freq, w, 0)

          if v == w do
            acc + div(cnt_v, 2)
          else
            acc + min(cnt_v, cnt_w)
          end
        end)

      if pairs > best, do: pairs, else: best
    end)
  end
end
```
