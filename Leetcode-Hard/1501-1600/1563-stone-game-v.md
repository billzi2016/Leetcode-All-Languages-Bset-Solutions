# 1563. Stone Game V

## Cpp

```cpp
class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        if (n <= 1) return 0;
        vector<long long> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) pre[i + 1] = pre[i] + stoneValue[i];
        vector<vector<long long>> dp(n, vector<long long>(n, 0));
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                long long best = 0;
                for (int i = l; i < r; ++i) {
                    long long left = pre[i + 1] - pre[l];
                    long long right = pre[r + 1] - pre[i + 1];
                    if (left < right) {
                        best = max(best, left + dp[l][i]);
                    } else if (left > right) {
                        best = max(best, right + dp[i + 1][r]);
                    } else { // equal
                        best = max(best, left + dp[l][i]);
                        best = max(best, right + dp[i + 1][r]);
                    }
                }
                dp[l][r] = best;
            }
        }
        return (int)dp[0][n - 1];
    }
};
```

## Java

```java
class Solution {
    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        if (n == 1) return 0;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stoneValue[i];
        }
        long[][] dp = new long[n][n];
        // dp[l][r] is already 0 when l == r
        for (int len = 2; len <= n; len++) {
            for (int l = 0; l + len - 1 < n; l++) {
                int r = l + len - 1;
                long best = 0;
                for (int k = l; k < r; k++) {
                    long leftSum = prefix[k + 1] - prefix[l];
                    long rightSum = prefix[r + 1] - prefix[k + 1];
                    long cur;
                    if (leftSum < rightSum) {
                        cur = leftSum + dp[l][k];
                    } else if (leftSum > rightSum) {
                        cur = rightSum + dp[k + 1][r];
                    } else {
                        cur = Math.max(leftSum + dp[l][k], rightSum + dp[k + 1][r]);
                    }
                    if (cur > best) best = cur;
                }
                dp[l][r] = best;
            }
        }
        return (int) dp[0][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n <= 1:
            return 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = 0
                # try all possible splits
                for k in range(i, j):
                    left_sum = prefix[k + 1] - prefix[i]
                    right_sum = prefix[j + 1] - prefix[k + 1]
                    if left_sum < right_sum:
                        cand = left_sum + dp[i][k]
                    elif left_sum > right_sum:
                        cand = right_sum + dp[k + 1][j]
                    else:  # equal, Alice can choose the better side
                        cand = max(left_sum + dp[i][k], right_sum + dp[k + 1][j])
                    if cand > best:
                        best = cand
                dp[i][j] = best

        return dp[0][n - 1]
```

## Python3

```python
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]

                # binary search greatest k with left_sum * 2 <= total
                lo, hi = i, j - 1
                bestk = i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    left = prefix[mid + 1] - prefix[i]
                    if left * 2 <= total:
                        bestk = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                cur = 0
                # case: left <= right
                if bestk >= i:
                    left = prefix[bestk + 1] - prefix[i]
                    cur = max(cur, left + dp[i][bestk])
                # case: left > right (use split at bestk+1)
                nxt = bestk + 1
                if nxt <= j - 1:
                    right = prefix[j + 1] - prefix[nxt]
                    cur = max(cur, right + dp[nxt][j])

                # equality case where left == right
                if bestk >= i:
                    left = prefix[bestk + 1] - prefix[i]
                    if left * 2 == total:
                        cur = max(cur,
                                  left + dp[i][bestk],
                                  left + dp[bestk + 1][j])

                dp[i][j] = cur

        return dp[0][n - 1]
```

## C

```c
#include <stdio.h>
#include <string.h>

static long long pref[502];
static int dp[502][502];
static int n;

int solve(int l, int r) {
    if (l >= r) return 0;
    if (dp[l][r] != -1) return dp[l][r];
    int best = 0;
    for (int k = l; k < r; ++k) {
        long long leftSum = pref[k + 1] - pref[l];
        long long rightSum = pref[r + 1] - pref[k + 1];
        if (leftSum < rightSum) {
            int cand = (int)(leftSum + solve(l, k));
            if (cand > best) best = cand;
        } else if (leftSum > rightSum) {
            int cand = (int)(rightSum + solve(k + 1, r));
            if (cand > best) best = cand;
        } else { // equal
            int cand = (int)leftSum + (solve(l, k) > solve(k + 1, r) ? solve(l, k) : solve(k + 1, r));
            if (cand > best) best = cand;
        }
    }
    dp[l][r] = best;
    return best;
}

int stoneGameV(int* stoneValue, int stoneValueSize) {
    n = stoneValueSize;
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + stoneValue[i];
    }
    memset(dp, -1, sizeof(dp));
    return solve(0, n - 1);
}
```

## Csharp

```csharp
public class Solution {
    public int StoneGameV(int[] stoneValue) {
        int n = stoneValue.Length;
        if (n == 1) return 0;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stoneValue[i];
        }
        long[,] dp = new long[n, n];
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                long best = 0;
                for (int k = l; k < r; ++k) {
                    long leftSum = prefix[k + 1] - prefix[l];
                    long rightSum = prefix[r + 1] - prefix[k + 1];
                    if (leftSum < rightSum) {
                        long cand = leftSum + dp[l, k];
                        if (cand > best) best = cand;
                    } else if (leftSum > rightSum) {
                        long cand = rightSum + dp[k + 1, r];
                        if (cand > best) best = cand;
                    } else {
                        long cand = leftSum + System.Math.Max(dp[l, k], dp[k + 1, r]);
                        if (cand > best) best = cand;
                    }
                }
                dp[l, r] = best;
            }
        }
        return (int)dp[0, n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stoneValue
 * @return {number}
 */
var stoneGameV = function(stoneValue) {
    const n = stoneValue.length;
    if (n <= 1) return 0;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + stoneValue[i];
    }
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    for (let len = 2; len <= n; ++len) {
        for (let l = 0; l + len - 1 < n; ++l) {
            const r = l + len - 1;
            let best = 0;
            for (let i = l; i < r; ++i) {
                const leftSum = prefix[i + 1] - prefix[l];
                const rightSum = prefix[r + 1] - prefix[i + 1];
                let cand;
                if (leftSum < rightSum) {
                    cand = leftSum + dp[l][i];
                } else if (leftSum > rightSum) {
                    cand = rightSum + dp[i + 1][r];
                } else {
                    cand = leftSum + Math.max(dp[l][i], dp[i + 1][r]);
                }
                if (cand > best) best = cand;
            }
            dp[l][r] = best;
        }
    }
    return dp[0][n - 1];
};
```

## Typescript

```typescript
function stoneGameV(stoneValue: number[]): number {
    const n = stoneValue.length;
    if (n === 1) return 0;

    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + stoneValue[i];
    }
    const rangeSum = (l: number, r: number): number => prefix[r + 1] - prefix[l];

    const dp: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));

    for (let len = 2; len <= n; len++) {
        for (let i = 0; i + len - 1 < n; i++) {
            const j = i + len - 1;
            let best = 0;
            for (let k = i; k < j; k++) {
                const left = rangeSum(i, k);
                const right = rangeSum(k + 1, j);
                if (left < right) {
                    const val = left + dp[i][k];
                    if (val > best) best = val;
                } else if (left > right) {
                    const val = right + dp[k + 1][j];
                    if (val > best) best = val;
                } else {
                    const v1 = left + dp[i][k];
                    const v2 = right + dp[k + 1][j];
                    if (v1 > best) best = v1;
                    if (v2 > best) best = v2;
                }
            }
            dp[i][j] = best;
        }
    }

    return dp[0][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stoneValue
     * @return Integer
     */
    function stoneGameV($stoneValue) {
        $n = count($stoneValue);
        if ($n <= 1) return 0;

        // prefix sums
        $pre = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $pre[$i + 1] = $pre[$i] + $stoneValue[$i];
        }

        // dp[l][r]: max score for subarray l..r
        $dp = array_fill(0, $n, array_fill(0, $n, 0));

        for ($len = 2; $len <= $n; ++$len) {
            for ($l = 0; $l + $len - 1 < $n; ++$l) {
                $r = $l + $len - 1;
                $best = 0;
                for ($k = $l; $k < $r; ++$k) {
                    $leftSum = $pre[$k + 1] - $pre[$l];
                    $rightSum = $pre[$r + 1] - $pre[$k + 1];
                    if ($leftSum < $rightSum) {
                        $cand = $leftSum + $dp[$l][$k];
                    } elseif ($leftSum > $rightSum) {
                        $cand = $rightSum + $dp[$k + 1][$r];
                    } else { // equal
                        $cand = $leftSum + max($dp[$l][$k], $dp[$k + 1][$r]);
                    }
                    if ($cand > $best) {
                        $best = $cand;
                    }
                }
                $dp[$l][$r] = $best;
            }
        }

        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func stoneGameV(_ stoneValue: [Int]) -> Int {
        let n = stoneValue.count
        if n <= 1 { return 0 }
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + stoneValue[i]
        }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        if n >= 2 {
            for length in 2...n {
                let limit = n - length
                var l = 0
                while l <= limit {
                    let r = l + length - 1
                    var best = 0
                    var k = l
                    while k < r {
                        let leftSum = prefix[k + 1] - prefix[l]
                        let rightSum = prefix[r + 1] - prefix[k + 1]
                        if leftSum == rightSum {
                            let cand = leftSum + max(dp[l][k], dp[k + 1][r])
                            if cand > best { best = cand }
                        } else if leftSum < rightSum {
                            let cand = leftSum + dp[l][k]
                            if cand > best { best = cand }
                        } else {
                            let cand = rightSum + dp[k + 1][r]
                            if cand > best { best = cand }
                        }
                        k += 1
                    }
                    dp[l][r] = best
                    l += 1
                }
            }
        }
        return dp[0][n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGameV(stoneValue: IntArray): Int {
        val n = stoneValue.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + stoneValue[i]
        }
        val dp = Array(n) { IntArray(n) { -1 } }

        fun dfs(l: Int, r: Int): Int {
            if (l == r) return 0
            if (dp[l][r] != -1) return dp[l][r]
            var best = 0
            for (i in l until r) {
                val sumL = prefix[i + 1] - prefix[l]
                val sumR = prefix[r + 1] - prefix[i + 1]
                when {
                    sumL < sumR -> {
                        val cand = sumL.toInt() + dfs(l, i)
                        if (cand > best) best = cand
                    }
                    sumL > sumR -> {
                        val cand = sumR.toInt() + dfs(i + 1, r)
                        if (cand > best) best = cand
                    }
                    else -> {
                        val cand = sumL.toInt() + maxOf(dfs(l, i), dfs(i + 1, r))
                        if (cand > best) best = cand
                    }
                }
            }
            dp[l][r] = best
            return best
        }

        return dfs(0, n - 1)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int stoneGameV(List<int> stoneValue) {
    int n = stoneValue.length;
    if (n <= 1) return 0;

    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + stoneValue[i];
    }

    // dp[l][r] stores the maximum score for subarray [l..r]
    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));

    for (int len = 2; len <= n; ++len) {
      for (int l = 0; l + len - 1 < n; ++l) {
        int r = l + len - 1;
        int best = 0;
        for (int k = l; k < r; ++k) {
          int leftSum = prefix[k + 1] - prefix[l];
          int rightSum = prefix[r + 1] - prefix[k + 1];
          int candidate;
          if (leftSum < rightSum) {
            candidate = leftSum + dp[l][k];
          } else if (leftSum > rightSum) {
            candidate = rightSum + dp[k + 1][r];
          } else {
            candidate = leftSum + max(dp[l][k], dp[k + 1][r]);
          }
          if (candidate > best) best = candidate;
        }
        dp[l][r] = best;
      }
    }

    return dp[0][n - 1];
  }
}
```

## Golang

```go
func stoneGameV(stoneValue []int) int {
    n := len(stoneValue)
    if n <= 1 {
        return 0
    }
    prefix := make([]int, n+1)
    for i := 0; i < n; i++ {
        prefix[i+1] = prefix[i] + stoneValue[i]
    }

    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, n)
    }

    for length := 2; length <= n; length++ {
        for l := 0; l+length-1 < n; l++ {
            r := l + length - 1
            best := 0
            for i := l; i < r; i++ {
                sumL := prefix[i+1] - prefix[l]
                sumR := prefix[r+1] - prefix[i+1]
                if sumL < sumR {
                    cand := sumL + dp[l][i]
                    if cand > best {
                        best = cand
                    }
                } else if sumL > sumR {
                    cand := sumR + dp[i+1][r]
                    if cand > best {
                        best = cand
                    }
                } else { // equal sums
                    cand1 := sumL + dp[l][i]
                    if cand1 > best {
                        best = cand1
                    }
                    cand2 := sumR + dp[i+1][r] // same as sumL + dp[i+1][r]
                    if cand2 > best {
                        best = cand2
                    }
                }
            }
            dp[l][r] = best
        }
    }

    return dp[0][n-1]
}
```

## Ruby

```ruby
def stone_game_v(stone_value)
  n = stone_value.length
  return 0 if n <= 1

  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + stone_value[i] }

  dp = Array.new(n) { Array.new(n, 0) }

  (2..n).each do |len|
    i = 0
    while i + len - 1 < n
      j = i + len - 1
      total = pref[j + 1] - pref[i]

      lo = i
      hi = j - 1
      while lo < hi
        mid = (lo + hi) / 2
        left_sum = pref[mid + 1] - pref[i]
        if left_sum * 2 < total
          lo = mid + 1
        else
          hi = mid
        end
      end

      best = 0
      [lo, lo - 1].each do |k|
        next if k < i || k >= j
        left = pref[k + 1] - pref[i]
        right = total - left
        cand =
          if left < right
            left + dp[i][k]
          elsif left > right
            right + dp[k + 1][j]
          else
            left + [dp[i][k], dp[k + 1][j]].max
          end
        best = cand if cand > best
      end

      dp[i][j] = best
      i += 1
    end
  end

  dp[0][n - 1]
end
```

## Scala

```scala
object Solution {
    def stoneGameV(stoneValue: Array[Int]): Int = {
        val n = stoneValue.length
        if (n <= 1) return 0
        val pref = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            pref(i + 1) = pref(i) + stoneValue(i).toLong
            i += 1
        }
        val dp = Array.ofDim[Int](n, n)

        var len = 2
        while (len <= n) {
            var l = 0
            while (l + len - 1 < n) {
                val r = l + len - 1
                var best = 0
                var k = l
                while (k < r) {
                    val leftSum = pref(k + 1) - pref(l)
                    val rightSum = pref(r + 1) - pref(k + 1)
                    if (leftSum < rightSum) {
                        val cand = (leftSum + dp(l)(k)).toInt
                        if (cand > best) best = cand
                    } else if (leftSum > rightSum) {
                        val cand = (rightSum + dp(k + 1)(r)).toInt
                        if (cand > best) best = cand
                    } else {
                        val sum = leftSum.toInt
                        val cand = sum + math.max(dp(l)(k), dp(k + 1)(r))
                        if (cand > best) best = cand
                    }
                    k += 1
                }
                dp(l)(r) = best
                l += 1
            }
            len += 1
        }

        dp(0)(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game_v(stone_value: Vec<i32>) -> i32 {
        let n = stone_value.len();
        if n <= 1 {
            return 0;
        }
        // prefix sums
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + stone_value[i] as i64;
        }

        // dp[l][r]: max score for subarray [l, r]
        let mut dp = vec![vec![0i64; n]; n];

        for len in 2..=n {
            for l in 0..=n - len {
                let r = l + len - 1;
                let mut best = 0i64;
                for k in l..r {
                    let left_sum = pref[k + 1] - pref[l];
                    let right_sum = pref[r + 1] - pref[k + 1];
                    if left_sum < right_sum {
                        let cand = left_sum + dp[l][k];
                        if cand > best {
                            best = cand;
                        }
                    } else if left_sum > right_sum {
                        let cand = right_sum + dp[k + 1][r];
                        if cand > best {
                            best = cand;
                        }
                    } else {
                        // equal sums, Alice can choose which part remains
                        let cand = left_sum + dp[l][k].max(dp[k + 1][r]);
                        if cand > best {
                            best = cand;
                        }
                    }
                }
                dp[l][r] = best;
            }
        }

        dp[0][n - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (stone-game-v stoneValue)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((arr (list->vector stoneValue))
         (n (vector-length arr))
         (ps (make-vector (+ n 1) 0)))
    ;; prefix sums
    (for ([i (in-range n)])
      (vector-set! ps (add1 i) (+ (vector-ref ps i) (vector-ref arr i))))
    (if (= n 1)
        0
        (let ((dp (make-vector n)))
          ;; initialize dp rows
          (for ([i (in-range n)])
            (vector-set! dp i (make-vector n 0)))
          ;; DP over lengths
          (for ([len (in-range 2 (add1 n))])
            (let ((max-start (- n len))) ; inclusive max start index
              (for ([i (in-range 0 (add1 max-start))])
                (let* ((j (+ i len -1))
                       (best 0))
                  (for ([k (in-range i j)])
                    (let* ((left (- (vector-ref ps (add1 k)) (vector-ref ps i)))
                           (right (- (vector-ref ps (add1 j)) (vector-ref ps (add1 k))))
                           (cand (cond [(< left right)
                                        (+ left (vector-ref (vector-ref dp i) k))]
                                       [(> left right)
                                        (+ right (vector-ref (vector-ref dp (add1 k)) j))]
                                       [else
                                        (max (+ left (vector-ref (vector-ref dp i) k))
                                             (+ right (vector-ref (vector-ref dp (add1 k)) j)))])))
                      (when (> cand best)
                        (set! best cand))))
                  (vector-set! (vector-ref dp i) j best)))))
          (vector-ref (vector-ref dp 0) (sub1 n))))))
```

## Erlang

```erlang
-spec stone_game_v([integer()]) -> integer().
stone_game_v(StoneValue) ->
    N = length(StoneValue),
    case N of
        0 -> 0;
        1 -> 0;
        _ ->
            PrefixTuple = build_prefix_tuple(StoneValue),
            {Score, _} = dp(0, N - 1, PrefixTuple, #{}),
            Score
    end.

build_prefix_tuple(Values) ->
    {RevList, _Sum} =
        lists:foldl(
          fun(V, {Acc, S}) -> {[S + V | Acc], S + V} end,
          {[], 0},
          Values),
    PrefixList = lists:reverse(RevList),
    list_to_tuple([0 | PrefixList]).

dp(L, R, Prefix, Memo) ->
    case maps:find({L, R}, Memo) of
        {ok, Score} ->
            {Score, Memo};
        error ->
            if L == R ->
                    NewMemo = maps:put({L, R}, 0, Memo),
                    {0, NewMemo};
               true ->
                    {MaxScore, FinalMemo} = dp_loop(L, R, Prefix, Memo, 0, L),
                    UpdatedMemo = maps:put({L, R}, MaxScore, FinalMemo),
                    {MaxScore, UpdatedMemo}
            end
    end.

dp_loop(_L, _R, _Prefix, Memo, MaxScore, I) when I > _R - 1 ->
    {MaxScore, Memo};
dp_loop(L, R, Prefix, Memo, MaxScore, I) ->
    LeftSum = element(I + 1, Prefix) - element(L, Prefix),
    RightSum = element(R + 1, Prefix) - element(I + 1, Prefix),
    case compare(LeftSum, RightSum) of
        less ->
            {ScoreL, Memo1} = dp(L, I, Prefix, Memo),
            NewScore = LeftSum + ScoreL,
            NewMax = erlang:max(MaxScore, NewScore),
            dp_loop(L, R, Prefix, Memo1, NewMax, I + 1);
        greater ->
            {ScoreR, Memo1} = dp(I + 1, R, Prefix, Memo),
            NewScore = RightSum + ScoreR,
            NewMax = erlang:max(MaxScore, NewScore),
            dp_loop(L, R, Prefix, Memo1, NewMax, I + 1);
        equal ->
            {ScoreL, Memo1} = dp(L, I, Prefix, Memo),
            {ScoreR, Memo2} = dp(I + 1, R, Prefix, Memo1),
            ScoreOpt1 = LeftSum + ScoreL,
            ScoreOpt2 = RightSum + ScoreR,
            NewMax = erlang:max(MaxScore, erlang:max(ScoreOpt1, ScoreOpt2)),
            dp_loop(L, R, Prefix, Memo2, NewMax, I + 1)
    end.

compare(A, B) when A < B -> less;
compare(A, B) when A > B -> greater;
compare(_, _) -> equal.
```

## Elixir

```elixir
defmodule Solution do
  @spec stone_game_v(stone_value :: [integer]) :: integer
  def stone_game_v(stone_value) do
    n = length(stone_value)

    if n == 1 do
      0
    else
      # prefix sums with leading 0
      pref_list = [0 | Enum.scan(stone_value, &+/2)]
      pref = List.to_tuple(pref_list)

      table = :ets.new(:dp_table, [:set, :private])

      # helper to get dp value from ETS (returns 0 if not present)
      get_dp = fn i, j ->
        case :ets.lookup(table, {i, j}) do
          [{_, val}] -> val
          [] -> 0
        end
      end

      for len <- 2..n do
        max_i = n - len
        for i <- 0..max_i do
          j = i + len - 1

          best =
            Enum.reduce(i..(j - 1), 0, fn k, acc ->
              left = elem(pref, k + 1) - elem(pref, i)
              right = elem(pref, j + 1) - elem(pref, k + 1)

              candidate =
                cond do
                  left == right ->
                    dp_left = get_dp.(i, k)
                    dp_right = get_dp.(k + 1, j)
                    left + max(dp_left, dp_right)

                  left < right ->
                    dp_left = get_dp.(i, k)
                    left + dp_left

                  true ->
                    dp_right = get_dp.(k + 1, j)
                    right + dp_right
                end

              if candidate > acc, do: candidate, else: acc
            end)

          :ets.insert(table, {{i, j}, best})
        end
      end

      case :ets.lookup(table, {0, n - 1}) do
        [{_, val}] -> val
        [] -> 0
      end
    end
  end
end
```
