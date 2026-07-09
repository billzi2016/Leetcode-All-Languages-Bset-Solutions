# 3599. Partition Array to Minimize XOR

## Cpp

```cpp
class Solution {
public:
    int minXor(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) pre[i + 1] = pre[i] ^ nums[i];
        
        const int INF = INT_MAX;
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, INF));
        dp[0][0] = 0;
        
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= min(i, k); ++j) {
                int best = INF;
                for (int t = j - 1; t < i; ++t) { // previous split point
                    if (dp[t][j - 1] == INF) continue;
                    int curXor = pre[i] ^ pre[t];
                    int cand = max(dp[t][j - 1], curXor);
                    if (cand < best) best = cand;
                }
                dp[i][j] = best;
            }
        }
        return dp[n][k];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minXor(int[] nums, int k) {
        int n = nums.length;
        int[] pre = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            pre[i] = pre[i - 1] ^ nums[i - 1];
        }
        int INF = Integer.MAX_VALUE;
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], INF);
        }
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i][1] = pre[i];
        }
        for (int parts = 2; parts <= k; parts++) {
            for (int i = parts; i <= n; i++) {
                int best = INF;
                for (int t = parts - 1; t <= i - 1; t++) {
                    int cur = Math.max(dp[t][parts - 1], pre[i] ^ pre[t]);
                    if (cur < best) {
                        best = cur;
                    }
                }
                dp[i][parts] = best;
            }
        }
        return dp[n][k];
    }
}
```

## Python

```python
class Solution(object):
    def minXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # prefix xor, pre[0]=0, pre[i] is xor of first i elements (nums[0..i-1])
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ nums[i]

        INF = 10 ** 18
        # dp[j][i]: min possible max xor when splitting first i elements into j parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            # at least j elements needed to form j non‑empty parts
            for i in range(j, n + 1):
                if j == 1:
                    dp[j][i] = pre[i]
                else:
                    best = INF
                    # split point t: first t elements into j-1 parts, last part is (t,i)
                    for t in range(j - 1, i):
                        cur = max(dp[j - 1][t], pre[i] ^ pre[t])
                        if cur < best:
                            best = cur
                    dp[j][i] = best

        return dp[k][n]
```

## Python3

```python
from typing import List

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] ^ nums[i - 1]

        INF = 10 ** 18
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(parts, n + 1):
                best = INF
                # t is the split point: first 't' elements form (parts-1) groups,
                # and segment [t, i) forms the last group.
                for t in range(parts - 1, i):
                    cur = max(dp[t][parts - 1], pre[i] ^ pre[t])
                    if cur < best:
                        best = cur
                dp[i][parts] = best

        return dp[n][k]
```

## C

```c
int minXor(int* nums, int numsSize, int k) {
    const int INF = 0x3f3f3f3f;
    int pre[251];
    pre[0] = 0;
    for (int i = 1; i <= numsSize; ++i) {
        pre[i] = pre[i - 1] ^ nums[i - 1];
    }
    static int dp[251][251];
    for (int i = 0; i <= numsSize; ++i) {
        for (int j = 0; j <= k; ++j) {
            dp[i][j] = INF;
        }
    }
    dp[0][0] = 0;
    for (int i = 1; i <= numsSize; ++i) {
        int maxJ = i < k ? i : k;
        for (int j = 1; j <= maxJ; ++j) {
            int best = INF;
            // t is the split point: first t elements form j-1 parts
            for (int t = j - 1; t <= i - 1; ++t) {
                int curXor = pre[i] ^ pre[t];
                int cand = dp[t][j - 1];
                if (cand > curXor) cand = curXor;
                else if (curXor > cand) cand = curXor; // max(dp, curXor)
                // above is just max, but we can use conditional
                // simpler:
                // int cand = dp[t][j-1] > curXor ? dp[t][j-1] : curXor;
                if (cand < best) best = cand;
            }
            dp[i][j] = best;
        }
    }
    return dp[numsSize][k];
}
```

## Csharp

```csharp
public class Solution {
    public int MinXor(int[] nums, int k) {
        int n = nums.Length;
        int[] pre = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pre[i + 1] = pre[i] ^ nums[i];
        }

        const int INF = int.MaxValue / 2;
        int[,] dp = new int[n + 1, k + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i, j] = INF;
            }
        }
        dp[0, 0] = 0;

        for (int parts = 1; parts <= k; parts++) {
            for (int i = parts; i <= n; i++) { // need at least 'parts' elements
                int best = INF;
                for (int t = parts - 1; t < i; t++) {
                    int curXor = pre[i] ^ pre[t];
                    int cur = Math.Max(dp[t, parts - 1], curXor);
                    if (cur < best) best = cur;
                }
                dp[i, parts] = best;
            }
        }

        return dp[n, k];
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
var minXor = function(nums, k) {
    const n = nums.length;
    const pre = new Array(n + 1);
    pre[0] = 0;
    for (let i = 0; i < n; ++i) {
        pre[i + 1] = pre[i] ^ nums[i];
    }

    // dp[i][j]: min possible max XOR for first i elements split into j parts
    const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(Infinity));
    dp[0][0] = 0;

    for (let i = 1; i <= n; ++i) {
        dp[1][i] = pre[i]; // one part -> XOR of whole prefix
    }

    for (let parts = 2; parts <= k; ++parts) {
        for (let i = parts; i <= n; ++i) { // need at least 'parts' elements
            let best = Infinity;
            for (let t = parts - 1; t < i; ++t) {
                const cur = Math.max(dp[parts - 1][t], pre[i] ^ pre[t]);
                if (cur < best) best = cur;
            }
            dp[parts][i] = best;
        }
    }

    return dp[k][n];
};
```

## Typescript

```typescript
function minXor(nums: number[], k: number): number {
    const n = nums.length;
    const pre = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        pre[i + 1] = pre[i] ^ nums[i];
    }
    const INF = Number.MAX_SAFE_INTEGER;
    const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(k + 1).fill(INF));
    dp[0][0] = 0;

    for (let i = 1; i <= n; i++) {
        const maxJ = Math.min(k, i);
        for (let j = 1; j <= maxJ; j++) {
            let best = INF;
            // previous split point t must leave at least j-1 elements before it
            for (let t = j - 1; t <= i - 1; t++) {
                const curXor = pre[i] ^ pre[t];
                const candidate = Math.max(dp[t][j - 1], curXor);
                if (candidate < best) best = candidate;
            }
            dp[i][j] = best;
        }
    }

    return dp[n][k];
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
    function minXor($nums, $k) {
        $n = count($nums);
        // prefix xor
        $pre = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $pre[$i] = $pre[$i - 1] ^ $nums[$i - 1];
        }

        // dp[i][j]: min possible max xor for first i elements into j parts
        $dp = array_fill(0, $n + 1, array_fill(0, $k + 1, PHP_INT_MAX));

        // base case: one part
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i][1] = $pre[$i];
        }

        for ($j = 2; $j <= $k; $j++) {
            for ($i = $j; $i <= $n; $i++) { // need at least j elements
                $best = PHP_INT_MAX;
                for ($t = $j - 1; $t <= $i - 1; $t++) {
                    $candidate = max($dp[$t][$j - 1], $pre[$i] ^ $pre[$t]);
                    if ($candidate < $best) {
                        $best = $candidate;
                    }
                }
                $dp[$i][$j] = $best;
            }
        }

        return $dp[$n][$k];
    }
}
```

## Swift

```swift
class Solution {
    func minXor(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pre = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            pre[i + 1] = pre[i] ^ nums[i]
        }
        let INF = Int.max / 2
        var dp = Array(repeating: Array(repeating: INF, count: k + 1), count: n + 1)
        dp[0][0] = 0
        if n > 0 {
            for i in 1...n {
                dp[i][1] = pre[i]
            }
        }
        if k >= 2 {
            for parts in 2...k {
                for i in parts...n {
                    var best = INF
                    var t = parts - 1
                    while t <= i - 1 {
                        let candidate = max(dp[t][parts - 1], pre[i] ^ pre[t])
                        if candidate < best { best = candidate }
                        t += 1
                    }
                    dp[i][parts] = best
                }
            }
        }
        return dp[n][k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minXor(nums: IntArray, k: Int): Int {
        val n = nums.size
        val pre = IntArray(n + 1)
        for (i in 1..n) {
            pre[i] = pre[i - 1] xor nums[i - 1]
        }
        // dp[j][i]: min possible max XOR for first i elements split into j parts
        val dp = Array(k + 1) { IntArray(n + 1) { Int.MAX_VALUE } }

        // base: one part
        for (i in 1..n) {
            dp[1][i] = pre[i]
        }

        for (j in 2..k) {
            for (i in j..n) { // need at least j elements to have j parts
                var best = Int.MAX_VALUE
                var t = j - 1
                while (t <= i - 1) {
                    val cur = maxOf(dp[j - 1][t], pre[i] xor pre[t])
                    if (cur < best) best = cur
                    // early exit if we reach zero, cannot improve further
                    if (best == 0) break
                    t++
                }
                dp[j][i] = best
            }
        }

        return dp[k][n]
    }
}
```

## Dart

```dart
class Solution {
  int minXor(List<int> nums, int k) {
    int n = nums.length;
    List<int> pre = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pre[i + 1] = pre[i] ^ nums[i];
    }
    const int INF = 1 << 60;
    List<List<int>> dp = List.generate(
        n + 1, (_) => List.filled(k + 1, INF),
        growable: false);
    dp[0][0] = 0;

    for (int i = 1; i <= n; ++i) {
      int maxJ = i < k ? i : k;
      for (int j = 1; j <= maxJ; ++j) {
        int best = INF;
        // t is the split point, first t elements form j-1 groups
        for (int t = j - 1; t <= i - 1; ++t) {
          int prev = dp[t][j - 1];
          if (prev == INF) continue;
          int subXor = pre[i] ^ pre[t];
          int candidate = prev > subXor ? prev : subXor;
          if (candidate < best) best = candidate;
        }
        dp[i][j] = best;
      }
    }

    return dp[n][k];
  }
}
```

## Golang

```go
func minXor(nums []int, k int) int {
    n := len(nums)
    pre := make([]int, n+1)
    for i := 0; i < n; i++ {
        pre[i+1] = pre[i] ^ nums[i]
    }
    const INF = int(^uint(0) >> 1)

    dp := make([][]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([]int, k+1)
        for j := 0; j <= k; j++ {
            dp[i][j] = INF
        }
    }
    dp[0][0] = 0

    for i := 1; i <= n; i++ {
        maxJ := k
        if i < maxJ {
            maxJ = i
        }
        for j := 1; j <= maxJ; j++ {
            best := INF
            for t := j - 1; t <= i-1; t++ {
                if dp[t][j-1] == INF {
                    continue
                }
                curXor := pre[i] ^ pre[t]
                cand := dp[t][j-1]
                if curXor > cand {
                    cand = curXor
                }
                if cand < best {
                    best = cand
                }
            }
            dp[i][j] = best
        }
    }
    return dp[n][k]
}
```

## Ruby

```ruby
def min_xor(nums, k)
  n = nums.length
  pre = Array.new(n + 1, 0)
  (0...n).each { |i| pre[i + 1] = pre[i] ^ nums[i] }

  inf = 1 << 60
  dp = Array.new(k + 1) { Array.new(n + 1, inf) }

  (1..n).each { |i| dp[1][i] = pre[i] }

  (2..k).each do |p|
    (p..n).each do |i|
      best = inf
      ((p - 1)..(i - 1)).each do |t|
        cur = [dp[p - 1][t], pre[i] ^ pre[t]].max
        best = cur if cur < best
      end
      dp[p][i] = best
    end
  end

  dp[k][n]
end
```

## Scala

```scala
object Solution {
    def minXor(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val pre = new Array[Int](n + 1)
        for (i <- 0 until n) {
            pre(i + 1) = pre(i) ^ nums(i)
        }
        val INF = Int.MaxValue
        val dp = Array.ofDim[Int](n + 1, k + 1)
        for (i <- 0 to n) {
            java.util.Arrays.fill(dp(i), INF)
        }
        for (i <- 1 to n) {
            dp(i)(1) = pre(i)
        }
        for (parts <- 2 to k) {
            for (i <- parts to n) {
                var best = INF
                var t = parts - 1
                while (t <= i - 1) {
                    val cur = Math.max(dp(t)(parts - 1), pre(i) ^ pre(t))
                    if (cur < best) best = cur
                    t += 1
                }
                dp(i)(parts) = best
            }
        }
        dp(n)(k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_xor(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut pre = vec![0i32; n + 1];
        for i in 0..n {
            pre[i + 1] = pre[i] ^ nums[i];
        }
        let k_usize = k as usize;
        const INF: i32 = i32::MAX;
        let mut dp = vec![vec![INF; k_usize + 1]; n + 1];
        dp[0][0] = 0;
        for j in 1..=k_usize {
            for i in j..=n {
                let mut best = INF;
                for t in (j - 1)..i {
                    let prev = dp[t][j - 1];
                    if prev == INF {
                        continue;
                    }
                    let subxor = pre[i] ^ pre[t];
                    let cand = if prev > subxor { prev } else { subxor };
                    if cand < best {
                        best = cand;
                    }
                }
                dp[i][j] = best;
            }
        }
        dp[n][k_usize]
    }
}
```

## Racket

```racket
(define/contract (min-xor nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (pre (make-vector (+ n 1) 0))
         (INF (expt 2 60))
         (dp (make-vector (+ n 1) #f)))
    ;; prefix xor
    (for ([i (in-range 1 (+ n 1))])
      (vector-set! pre i
                   (bitwise-xor (vector-ref pre (- i 1))
                                (vector-ref nums-vec (- i 1)))))
    ;; dp initialization
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ k 1) INF)))
    (vector-set! (vector-ref dp 0) 0 0)
    ;; DP computation
    (for ([i (in-range 1 (+ n 1))])
      (let ((maxj (min i k)))
        (for ([j (in-range 1 (add1 maxj))])
          (let ((best INF))
            (for ([t (in-range (- j 1) i)]) ; t from j-1 to i-1
              (let* ((prev (vector-ref (vector-ref dp t) (- j 1)))
                     (xorval (bitwise-xor (vector-ref pre i)
                                          (vector-ref pre t)))
                     (cur (max prev xorval)))
                (when (< cur best)
                  (set! best cur))))
            (vector-set! (vector-ref dp i) j best)))))
    (vector-ref (vector-ref dp n) k)))
```

## Erlang

```erlang
-spec min_xor([integer()], integer()) -> integer().
min_xor(Nums, K) ->
    N = length(Nums),
    PreList = build_prefix(Nums),               % [Pre0=0, Pre1, ..., Pren]
    PreArray = array:from_list(PreList),        % index 0..N
    INF = 1 bsl 60,
    DP1Vals = [array:get(I, PreArray) || I <- lists:seq(0, N)],
    DP1 = array:from_list(DP1Vals),
    DPs = loop_j(2, K, N, PreArray, DP1, INF, [DP1]),
    FinalDP = lists:nth(K, DPs),
    array:get(N, FinalDP).

build_prefix(Nums) ->
    {RevList, _} =
        lists:foldl(
            fun (X, {Acc, Xor}) ->
                {[Xor bxor X | Acc], Xor bxor X}
            end,
            {[], 0},
            Nums),
    Prefix = lists:reverse(RevList),
    [0 | Prefix].

loop_j(CurJ, MaxJ, N, PreArray, PrevDP, INF, Acc) when CurJ =< MaxJ ->
    CurrDP = compute_curr_dp(CurJ, N, PreArray, PrevDP, INF),
    loop_j(CurJ + 1, MaxJ, N, PreArray, CurrDP, INF, [CurrDP | Acc]);
loop_j(_CurJ, _MaxJ, _N, _PreArray, _PrevDP, _INF, Acc) ->
    lists:reverse(Acc).

compute_curr_dp(J, N, PreArray, PrevDP, INF) ->
    Curr0 = array:new(N + 1, {default, INF}),
    compute_i(J, N, J - 1, PreArray, PrevDP, Curr0).

compute_i(I, N, _MinT, _PreArray, _PrevDP, Curr) when I > N ->
    Curr;
compute_i(I, N, MinT, PreArray, PrevDP, Curr) ->
    Best = find_best(I, MinT, PrevDP, PreArray),
    NewCurr = array:set(I, Best, Curr),
    compute_i(I + 1, N, MinT, PreArray, PrevDP, NewCurr).

find_best(I, MinT, PrevDP, PreArray) ->
    find_t(I, MinT, I - 1, PrevDP, PreArray, 1 bsl 60).

find_t(_I, T, MaxT, _PrevDP, _PreArray, Best) when T > MaxT ->
    Best;
find_t(I, T, MaxT, PrevDP, PreArray, Best) ->
    PrevVal = array:get(T, PrevDP),
    SubXor = (array:get(I, PreArray)) bxor (array:get(T, PreArray)),
    Cur = if PrevVal > SubXor -> PrevVal; true -> SubXor end,
    NewBest = if Cur < Best -> Cur; true -> Best end,
    find_t(I, T + 1, MaxT, PrevDP, PreArray, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_xor(nums :: [integer], k :: integer) :: integer
  def min_xor(nums, k) do
    n = length(nums)
    # prefix xor as tuple for O(1) access: pre[0] = 0
    pre_list =
      Enum.scan(nums, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
      |> List.insert_at(0, 0)

    pre = List.to_tuple(pre_list)

    inf = 1 <<< 60

    # dp map: {i, j} => minimal possible maximal xor for first i elements into j parts
    dp_initial = %{{0, 0} => 0}

    dp_final =
      1..k
      |> Enum.reduce(dp_initial, fn j, dp_acc ->
        Enum.reduce(j..n, dp_acc, fn i, dp_map ->
          best =
            ((j - 1)..(i - 1))
            |> Enum.map(fn t ->
              prev = Map.get(dp_map, {t, j - 1}, inf)
              cur = max(prev, Bitwise.bxor(elem(pre, i), elem(pre, t)))
              cur
            end)
            |> Enum.min()

          Map.put(dp_map, {i, j}, best)
        end)
      end)

    Map.get(dp_final, {n, k}, 0)
  end
end
```
