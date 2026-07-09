# 0546. Remove Boxes

## Cpp

```cpp
class Solution {
public:
    int n;
    vector<int> a;
    vector<vector<vector<int>>> dp;

    int dfs(int l, int r, int k) {
        if (l > r) return 0;
        if (dp[l][r][k] != -1) return dp[l][r][k];
        // Merge same-colored boxes at the end
        while (r > l && a[r] == a[r - 1]) {
            --r;
            ++k;
        }
        int res = dfs(l, r - 1, 0) + (k + 1) * (k + 1);
        for (int i = l; i < r; ++i) {
            if (a[i] == a[r]) {
                int temp = dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0);
                if (temp > res) res = temp;
            }
        }
        dp[l][r][k] = res;
        return res;
    }

    int removeBoxes(vector<int>& boxes) {
        a = boxes;
        n = a.size();
        dp.assign(n, vector<vector<int>>(n, vector<int>(n + 1, -1)));
        return dfs(0, n - 1, 0);
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    private int[] boxes;
    private int[][][] memo;

    public int removeBoxes(int[] boxes) {
        this.boxes = boxes;
        int n = boxes.length;
        memo = new int[n][n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(memo[i][j], -1);
            }
        }
        return dfs(0, n - 1, 0);
    }

    private int dfs(int l, int r, int k) {
        if (l > r) return 0;
        if (memo[l][r][k] != -1) return memo[l][r][k];

        int origR = r, origK = k;

        // Merge boxes of the same color at the end
        while (r > l && boxes[r] == boxes[r - 1]) {
            r--;
            k++;
        }

        // Option 1: remove the group ending at position r now
        int best = dfs(l, r - 1, 0) + (k + 1) * (k + 1);

        // Option 2: try to merge non‑contiguous boxes of the same color
        for (int i = l; i < r; i++) {
            if (boxes[i] == boxes[r]) {
                int candidate = dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0);
                if (candidate > best) best = candidate;
            }
        }

        memo[l][origR][origK] = best;
        return best;
    }
}
```

## Python

```python
import sys
from functools import lru_cache

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        sys.setrecursionlimit(10000)
        n = len(boxes)

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            # merge boxes of the same color at the end
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            # option 1: remove the last group now
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            # option 2: merge with a previous same-colored box
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            return res

        return dp(0, n - 1, 0)
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            # Merge boxes of the same color as boxes[r] that are contiguous to its left
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            # Option 1: remove the group ending at r now
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            # Option 2: try to merge non‑contiguous same‑colored boxes
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            return res

        return dp(0, n - 1, 0)
```

## C

```c
#include <string.h>

static int boxesArr[105];
static int dp[105][105][105];

int solve(int l, int r, int k) {
    if (l > r) return 0;
    while (r > l && boxesArr[r] == boxesArr[r - 1]) {
        r--;
        k++;
    }
    int *memo = &dp[l][r][k];
    if (*memo != -1) return *memo;

    int res = solve(l, r - 1, 0) + (k + 1) * (k + 1);
    for (int i = l; i < r; ++i) {
        if (boxesArr[i] == boxesArr[r]) {
            int temp = solve(l, i, k + 1) + solve(i + 1, r - 1, 0);
            if (temp > res) res = temp;
        }
    }
    *memo = res;
    return res;
}

int removeBoxes(int* boxes, int boxesSize) {
    memcpy(boxesArr, boxes, boxesSize * sizeof(int));
    memset(dp, -1, sizeof(dp));
    return solve(0, boxesSize - 1, 0);
}
```

## Csharp

```csharp
public class Solution
{
    private int[,,] memo;
    private int[] boxes;
    private int n;

    public int RemoveBoxes(int[] boxes)
    {
        this.boxes = boxes;
        n = boxes.Length;
        memo = new int[n, n, n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++)
                    memo[i, j, k] = -1;
        return Dp(0, n - 1, 0);
    }

    private int Dp(int l, int r, int k)
    {
        if (l > r) return 0;
        if (memo[l, r, k] != -1) return memo[l, r, k];

        // Merge boxes of the same color at the end
        while (r > l && boxes[r] == boxes[r - 1])
        {
            r--;
            k++;
        }

        int result = Dp(l, r - 1, 0) + (k + 1) * (k + 1);

        for (int i = l; i < r; i++)
        {
            if (boxes[i] == boxes[r])
            {
                int temp = Dp(l, i, k + 1) + Dp(i + 1, r - 1, 0);
                if (temp > result) result = temp;
            }
        }

        memo[l, r, k] = result;
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} boxes
 * @return {number}
 */
var removeBoxes = function(boxes) {
    const n = boxes.length;
    // memo[l][r][k] => max points for subarray [l..r] with k extra boxes equal to boxes[r] appended on the right
    const memo = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => Array(n).fill(undefined))
    );

    function dfs(l, r, k) {
        if (l > r) return 0;
        if (memo[l][r][k] !== undefined) return memo[l][r][k];

        // Merge consecutive boxes of the same color at the end into k
        while (r > l && boxes[r] === boxes[r - 1]) {
            r--;
            k++;
        }

        // Option 1: remove the group ending at r now
        let best = dfs(l, r - 1, 0) + (k + 1) * (k + 1);

        // Option 2: try to merge with a previous same-colored box
        for (let i = l; i < r; i++) {
            if (boxes[i] === boxes[r]) {
                const candidate = dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0);
                if (candidate > best) best = candidate;
            }
        }

        memo[l][r][k] = best;
        return best;
    }

    return dfs(0, n - 1, 0);
};
```

## Typescript

```typescript
function removeBoxes(boxes: number[]): number {
    const n = boxes.length;
    const memo: number[][][] = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => Array(n + 1).fill(-1))
    );

    function dfs(l: number, r: number, k: number): number {
        if (l > r) return 0;

        while (r > l && boxes[r] === boxes[r - 1]) {
            r--;
            k++;
        }

        if (memo[l][r][k] !== -1) return memo[l][r][k];

        let best = dfs(l, r - 1, 0) + (k + 1) * (k + 1);

        for (let i = l; i < r; i++) {
            if (boxes[i] === boxes[r]) {
                const candidate = dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0);
                if (candidate > best) best = candidate;
            }
        }

        memo[l][r][k] = best;
        return best;
    }

    return dfs(0, n - 1, 0);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $boxes
     * @return Integer
     */
    function removeBoxes($boxes) {
        $n = count($boxes);
        $memo = [];

        $dfs = function ($l, $r, $k) use (&$boxes, &$memo, &$dfs) {
            if ($l > $r) {
                return 0;
            }

            // Merge consecutive boxes of the same color at the end
            while ($r > $l && $boxes[$r] == $boxes[$r - 1]) {
                $r--;
                $k++;
            }

            $key = $l . ',' . $r . ',' . $k;
            if (isset($memo[$key])) {
                return $memo[$key];
            }

            // Base case: only one box left
            if ($l == $r) {
                $res = ($k + 1) * ($k + 1);
                $memo[$key] = $res;
                return $res;
            }

            // Option 1: remove the last group now
            $res = $dfs($l, $r - 1, 0) + ($k + 1) * ($k + 1);

            // Option 2: try to merge with a previous box of the same color
            for ($i = $l; $i < $r; $i++) {
                if ($boxes[$i] == $boxes[$r]) {
                    $temp = $dfs($l, $i, $k + 1) + $dfs($i + 1, $r - 1, 0);
                    if ($temp > $res) {
                        $res = $temp;
                    }
                }
            }

            $memo[$key] = $res;
            return $res;
        };

        return $dfs(0, $n - 1, 0);
    }
}
```

## Swift

```swift
class Solution {
    func removeBoxes(_ boxes: [Int]) -> Int {
        let n = boxes.count
        var dp = Array(repeating: Array(repeating: Array(repeating: -1, count: n + 1), count: n), repeatCount: n)
        
        func dfs(_ l: Int, _ r: Int, _ k: Int) -> Int {
            if l > r { return 0 }
            var r = r
            var k = k
            // Merge boxes of the same color at the end
            while r > l && boxes[r] == boxes[r - 1] {
                r -= 1
                k += 1
            }
            if dp[l][r][k] != -1 { return dp[l][r][k] }
            
            // Option 1: remove the group at position r (with k extra)
            var best = dfs(l, r - 1, 0) + (k + 1) * (k + 1)
            
            // Option 2: try to merge non‑contiguous same colors
            if l < r {
                for i in l..<r {
                    if boxes[i] == boxes[r] {
                        let temp = dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0)
                        if temp > best { best = temp }
                    }
                }
            }
            
            dp[l][r][k] = best
            return best
        }
        
        return dfs(0, n - 1, 0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeBoxes(boxes: IntArray): Int {
        val n = boxes.size
        val dp = Array(n) { Array(n) { IntArray(n) } }
        for (i in 0 until n) {
            for (j in 0 until n) {
                java.util.Arrays.fill(dp[i][j], -1)
            }
        }

        fun dfs(l: Int, r: Int, k: Int): Int {
            if (l > r) return 0
            var rr = r
            var kk = k
            while (rr > l && boxes[rr] == boxes[rr - 1]) {
                rr--
                kk++
            }
            if (dp[l][rr][kk] != -1) return dp[l][rr][kk]
            var res = dfs(l, rr - 1, 0) + (kk + 1) * (kk + 1)
            for (i in l until rr) {
                if (boxes[i] == boxes[rr]) {
                    val temp = dfs(l, i, kk + 1) + dfs(i + 1, rr - 1, 0)
                    if (temp > res) res = temp
                }
            }
            dp[l][rr][kk] = res
            return res
        }

        return dfs(0, n - 1, 0)
    }
}
```

## Dart

```dart
class Solution {
  int removeBoxes(List<int> boxes) {
    final int n = boxes.length;
    // memo[l][r][k] where k is the count of same-colored boxes appended to the right of r
    final List<List<List<int>>> memo = List.generate(
        n, (_) => List.generate(n, (_) => List.filled(n, -1)));

    int dfs(int l, int r, int k) {
      if (l > r) return 0;

      // Merge consecutive boxes of the same color at the end into k
      while (r > l && boxes[r] == boxes[r - 1]) {
        r--;
        k++;
      }

      if (memo[l][r][k] != -1) return memo[l][r][k];

      // Option 1: remove the group ending at r now
      int best = dfs(l, r - 1, 0) + (k + 1) * (k + 1);

      // Option 2: try to merge with a previous box of same color
      for (int i = l; i < r; ++i) {
        if (boxes[i] == boxes[r]) {
          int candidate =
              dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0);
          if (candidate > best) best = candidate;
        }
      }

      memo[l][r][k] = best;
      return best;
    }

    return dfs(0, n - 1, 0);
  }
}
```

## Golang

```go
func removeBoxes(boxes []int) int {
    n := len(boxes)
    if n == 0 {
        return 0
    }
    // dp[l][r][k] = max points for boxes[l..r] with k extra boxes equal to boxes[r] appended on the right
    dp := make([][][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([][]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = make([]int, n+1)
            for k := 0; k <= n; k++ {
                dp[i][j][k] = -1
            }
        }
    }

    var dfs func(l, r, k int) int
    dfs = func(l, r, k int) int {
        if l > r {
            return 0
        }
        if dp[l][r][k] != -1 {
            return dp[l][r][k]
        }

        origR, origK := r, k

        // Merge consecutive boxes of the same color at the end into k
        for r > l && boxes[r] == boxes[r-1] {
            r--
            k++
        }

        // Now boxes[r] is the last box of its color group, with (k+1) boxes total
        if l == r {
            dp[l][origR][origK] = (k + 1) * (k + 1)
            return dp[l][origR][origK]
        }

        // Option 1: remove the last group now
        best := dfs(l, r-1, 0) + (k+1)*(k+1)

        // Option 2: try to merge with a previous box of the same color
        for i := l; i < r; i++ {
            if boxes[i] == boxes[r] {
                temp := dfs(l, i, k+1) + dfs(i+1, r-1, 0)
                if temp > best {
                    best = temp
                }
            }
        }

        dp[l][origR][origK] = best
        return best
    }

    return dfs(0, n-1, 0)
}
```

## Ruby

```ruby
def remove_boxes(boxes)
  n = boxes.length
  dp = Array.new(n) { Array.new(n) { Array.new(n + 1) } }

  dfs = nil
  dfs = ->(l, r, k) {
    return 0 if l > r
    cached = dp[l][r][k]
    return cached unless cached.nil?

    # Merge consecutive boxes of the same color at the start
    while l < r && boxes[l] == boxes[l + 1]
      l += 1
      k += 1
    end

    # Option 1: remove the group starting at l now
    best = (k + 1) * (k + 1) + dfs.call(l + 1, r, 0)

    # Option 2: try to merge non‑adjacent boxes of the same color
    i = l + 1
    while i <= r
      if boxes[i] == boxes[l]
        temp = dfs.call(l + 1, i - 1, 0) + dfs.call(i, r, k + 1)
        best = [best, temp].max
      end
      i += 1
    end

    dp[l][r][k] = best
    best
  }

  dfs.call(0, n - 1, 0)
end
```

## Scala

```scala
object Solution {
    def removeBoxes(boxes: Array[Int]): Int = {
        val n = boxes.length
        val memo = Array.ofDim[Int](n, n, n)

        def dfs(l: Int, r: Int, k: Int): Int = {
            if (l > r) return 0
            var rr = r
            var kk = k
            while (rr > l && boxes(rr) == boxes(rr - 1)) {
                rr -= 1
                kk += 1
            }
            if (memo(l)(rr)(kk) != 0) return memo(l)(rr)(kk)

            val result =
                if (l == rr) {
                    (kk + 1) * (kk + 1)
                } else {
                    var best = dfs(l, rr - 1, 0) + (kk + 1) * (kk + 1)
                    var i = l
                    while (i < rr) {
                        if (boxes(i) == boxes(rr)) {
                            val temp = dfs(l, i, kk + 1) + dfs(i + 1, rr - 1, 0)
                            if (temp > best) best = temp
                        }
                        i += 1
                    }
                    best
                }

            memo(l)(rr)(kk) = result
            result
        }

        dfs(0, n - 1, 0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_boxes(boxes: Vec<i32>) -> i32 {
        let n = boxes.len();
        if n == 0 {
            return 0;
        }
        let mut memo = vec![vec![vec![-1i32; n + 1]; n]; n];
        fn dfs(
            l: usize,
            r: usize,
            k: usize,
            boxes: &Vec<i32>,
            memo: &mut Vec<Vec<Vec<i32>>>,
        ) -> i32 {
            if l > r {
                return 0;
            }
            if memo[l][r][k] != -1 {
                return memo[l][r][k];
            }

            let mut ll = l;
            let mut kk = k;
            while ll + 1 <= r && boxes[ll] == boxes[ll + 1] {
                ll += 1;
                kk += 1;
            }

            // Remove the group at position ll (with kk extra same-colored boxes)
            let mut res =
                ((kk + 1) * (kk + 1)) as i32 + dfs(ll + 1, r, 0, boxes, memo);

            // Try to merge with later boxes of the same color
            for m in (ll + 1)..=r {
                if boxes[m] == boxes[ll] {
                    let temp = dfs(ll + 1, m - 1, 0, boxes, memo)
                        + dfs(m, r, kk + 1, boxes, memo);
                    if temp > res {
                        res = temp;
                    }
                }
            }

            memo[l][r][k] = res;
            res
        }

        dfs(0, n - 1, 0, &boxes, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (remove-boxes boxes)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector boxes)]
         [n (vector-length v)])
    (define memo (make-hash))
    (letrec ((dp (lambda (l r k)
                   (if (> l r)
                       0
                       (let ([key (list l r k)])
                         (let ([cached (hash-ref memo key #f)])
                           (if cached
                               cached
                               (let loop ((l l) (r r) (k k))
                                 (if (and (> r l)
                                          (= (vector-ref v r)
                                             (vector-ref v (- r 1))))
                                     (loop l (- r 1) (+ k 1))
                                     (begin
                                       (define base (+ (* (+ k 1) (+ k 1))
                                                       (dp l (- r 1) 0)))
                                       (define best base)
                                       (for ([i (in-range l r)])
                                         (when (= (vector-ref v i)
                                                  (vector-ref v r))
                                           (let ((temp (+ (dp l i (+ k 1))
                                                          (dp (+ i 1) (- r 1) 0))))
                                             (when (> temp best)
                                               (set! best temp)))))
                                       (hash-set! memo key best)
                                       best))))))))))
      (if (= n 0)
          0
          (dp 0 (- n 1) 0)))))
```

## Erlang

```erlang
-module(solution).
-export([remove_boxes/1]).

-spec remove_boxes(Boxes :: [integer()]) -> integer().
remove_boxes(Boxes) ->
    BoxT = list_to_tuple(Boxes),
    N = tuple_size(BoxT),
    {Res, _} = dp(0, N - 1, 0, BoxT, #{}),
    Res.

dp(L, R, K, BoxT, Memo) when L > R ->
    {0, Memo};
dp(L, R, K, BoxT, Memo) ->
    case maps:get({L,R,K}, Memo, undefined) of
        undefined ->
            ColorL = element(L+1, BoxT),
            {Val1, Memo1} = dp(L+1, R, 0, BoxT, Memo),
            Opt1 = (K+1)*(K+1) + Val1,
            {Best, Memo2} = loop(L+1, R, L, ColorL, K, Opt1, BoxT, Memo1),
            NewMemo = maps:put({L,R,K}, Best, Memo2),
            {Best, NewMemo};
        Value ->
            {Value, Memo}
    end.

loop(I, R, _L, _ColorL, _K, CurrentBest, _BoxT, Memo) when I > R ->
    {CurrentBest, Memo};
loop(I, R, L, ColorL, K, CurrentBest, BoxT, Memo) ->
    case element(I+1, BoxT) of
        ColorL ->
            {Mid, MemoMid} = dp(L+1, I-1, 0, BoxT, Memo),
            {Right, MemoRight} = dp(I, R, K+1, BoxT, MemoMid),
            Total = Mid + Right,
            NewBest = if Total > CurrentBest -> Total; true -> CurrentBest end,
            loop(I+1, R, L, ColorL, K, NewBest, BoxT, MemoRight);
        _ ->
            loop(I+1, R, L, ColorL, K, CurrentBest, BoxT, Memo)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_boxes(boxes :: [integer]) :: integer
  def remove_boxes(boxes) do
    n = length(boxes)
    {res, _} = dfs(0, n - 1, 0, boxes, %{})
    res
  end

  defp dfs(l, r, k, _boxes, memo) when l > r, do: {0, memo}

  defp dfs(l, r, k, boxes, memo) do
    key = {l, r, k}
    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        {r2, k2} = compress(l, r, k, boxes)

        {temp1, memo1} = dfs(l, r2 - 1, 0, boxes, memo)
        best_initial = temp1 + (k2 + 1) * (k2 + 1)

        {best, final_memo} =
          Enum.reduce(l..(r2 - 1), {best_initial, memo1}, fn i, {cur_best, cur_memo} ->
            if Enum.at(boxes, i) == Enum.at(boxes, r2) do
              {left_val, memo_left} = dfs(l, i, k2 + 1, boxes, cur_memo)
              {mid_val, memo_mid} = dfs(i + 1, r2 - 1, 0, boxes, memo_left)
              val = left_val + mid_val

              if val > cur_best do
                {val, memo_mid}
              else
                {cur_best, memo_mid}
              end
            else
              {cur_best, cur_memo}
            end
          end)

        new_memo = Map.put(final_memo, key, best)
        {best, new_memo}
    end
  end

  defp compress(l, r, k, boxes) do
    if r > l && Enum.at(boxes, r) == Enum.at(boxes, r - 1) do
      compress(l, r - 1, k + 1, boxes)
    else
      {r, k}
    end
  end
end
```
