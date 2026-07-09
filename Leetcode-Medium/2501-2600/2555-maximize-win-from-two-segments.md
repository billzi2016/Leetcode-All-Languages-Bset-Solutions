# 2555. Maximize Win From Two Segments

## Cpp

```cpp
class Solution {
public:
    int maximizeWin(vector<int>& prizePositions, int k) {
        int n = prizePositions.size();
        vector<int> cnt(n);
        int r = 0;
        for (int i = 0; i < n; ++i) {
            while (r < n && prizePositions[r] - prizePositions[i] <= k) {
                ++r;
            }
            cnt[i] = r - i;
        }
        vector<int> suffixBest(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            suffixBest[i] = max(cnt[i], suffixBest[i + 1]);
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int nextIdx = i + cnt[i];
            ans = max(ans, cnt[i] + suffixBest[nextIdx]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximizeWin(int[] prizePositions, int k) {
        int n = prizePositions.length;
        int[] right = new int[n];
        int[] cnt = new int[n];
        int r = 0;
        for (int i = 0; i < n; i++) {
            while (r < n && (long)prizePositions[r] - prizePositions[i] <= k) {
                r++;
            }
            right[i] = r;               // first index outside the interval
            cnt[i] = r - i;
        }

        // suffix max of cnt for non‑overlapping case
        int[] suffixMaxCnt = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixMaxCnt[i] = Math.max(cnt[i], suffixMaxCnt[i + 1]);
        }

        // segment tree for range maximum of right[]
        SegmentTree seg = new SegmentTree(right);

        int ans = 0;
        for (int i = 0; i < n; i++) {
            // overlapping / partially overlapping case
            int maxRightInWindow = seg.query(i, right[i] - 1);
            int totalOverlap = maxRightInWindow - i;
            if (totalOverlap > ans) ans = totalOverlap;

            // non‑overlapping case
            int totalNonOverlap = cnt[i] + suffixMaxCnt[right[i]];
            if (totalNonOverlap > ans) ans = totalNonOverlap;
        }
        return ans;
    }

    private static class SegmentTree {
        private final int n;
        private final int[] tree;

        SegmentTree(int[] arr) {
            this.n = arr.length;
            this.tree = new int[4 * n];
            build(1, 0, n - 1, arr);
        }

        private void build(int node, int l, int r, int[] arr) {
            if (l == r) {
                tree[node] = arr[l];
                return;
            }
            int mid = (l + r) >>> 1;
            build(node << 1, l, mid, arr);
            build(node << 1 | 1, mid + 1, r, arr);
            tree[node] = Math.max(tree[node << 1], tree[node << 1 | 1]);
        }

        int query(int ql, int qr) {
            return query(1, 0, n - 1, ql, qr);
        }

        private int query(int node, int l, int r, int ql, int qr) {
            if (ql <= l && r <= qr) {
                return tree[node];
            }
            int mid = (l + r) >>> 1;
            int res = Integer.MIN_VALUE;
            if (ql <= mid) {
                res = Math.max(res, query(node << 1, l, mid, ql, qr));
            }
            if (qr > mid) {
                res = Math.max(res, query(node << 1 | 1, mid + 1, r, ql, qr));
            }
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prizePositions)
        cnt = [0] * n          # prizes covered when interval starts at i
        nxt = [0] * n          # first index not covered by that interval
        right = 0
        for left in range(n):
            while right < n and prizePositions[right] - prizePositions[left] <= k:
                right += 1
            cnt[left] = right - left
            nxt[left] = right

        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(cnt[i], suffix_max[i + 1])

        ans = 0
        for i in range(n):
            total = cnt[i]
            if nxt[i] < n:
                total += suffix_max[nxt[i]]
            if total > ans:
                ans = total
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        cnt = [0] * n          # prizes covered by interval starting at i
        nxt = [0] * n          # first index not covered by that interval
        
        right = 0
        for left in range(n):
            while right < n and prizePositions[right] - prizePositions[left] <= k:
                right += 1
            cnt[left] = right - left
            nxt[left] = right   # exclusive end
        
        # suffix maximum of cnt
        suff_max = [0] * (n + 1)   # suff_max[i] = max cnt[t] for t >= i
        for i in range(n - 1, -1, -1):
            suff_max[i] = max(cnt[i], suff_max[i + 1])
        
        ans = 0
        for i in range(n):
            total = cnt[i] + suff_max[nxt[i]]
            if total > ans:
                ans = total
        
        return ans
```

## C

```c
int maximizeWin(int* prizePositions, int prizePositionsSize, int k) {
    int n = prizePositionsSize;
    if (n == 0) return 0;

    int *cnt = (int*)malloc(n * sizeof(int));
    int *endIdx = (int*)malloc(n * sizeof(int));

    int r = 0;
    for (int l = 0; l < n; ++l) {
        while (r + 1 < n && prizePositions[r + 1] - prizePositions[l] <= k) {
            ++r;
        }
        cnt[l] = r - l + 1;
        endIdx[l] = r;
        if (r == l) { // move right pointer forward for next iteration
            ++r;
        }
    }

    int *bestRight = (int*)malloc((n + 1) * sizeof(int));
    bestRight[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        bestRight[i] = cnt[i] > bestRight[i + 1] ? cnt[i] : bestRight[i + 1];
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int total = cnt[i];
        int nextIdx = endIdx[i] + 1;
        if (nextIdx < n) {
            total += bestRight[nextIdx];
        }
        if (total > ans) ans = total;
    }

    free(cnt);
    free(endIdx);
    free(bestRight);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximizeWin(int[] prizePositions, int k) {
        int n = prizePositions.Length;
        int[] cnt = new int[n];
        int[] rightIdx = new int[n];
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && prizePositions[j] - prizePositions[i] <= k) {
                j++;
            }
            cnt[i] = j - i;
            rightIdx[i] = j - 1;
        }

        int[] suffixMax = new int[n + 1];
        suffixMax[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            suffixMax[i] = Math.Max(cnt[i], suffixMax[i + 1]);
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            int total = cnt[i];
            int nextIdx = rightIdx[i] + 1;
            if (nextIdx < n) {
                total += suffixMax[nextIdx];
            }
            if (total > ans) ans = total;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prizePositions
 * @param {number} k
 * @return {number}
 */
var maximizeWin = function(prizePositions, k) {
    const n = prizePositions.length;
    const cnt = new Array(n);
    const endIdx = new Array(n);
    
    let r = 0;
    for (let l = 0; l < n; ++l) {
        while (r + 1 < n && prizePositions[r + 1] - prizePositions[l] <= k) {
            ++r;
        }
        cnt[l] = r - l + 1;
        endIdx[l] = r;
        // move left pointer forward, r stays >= l
        if (r === l) ++r; // ensure window moves when l catches up
    }
    
    const suffixMax = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        suffixMax[i] = Math.max(cnt[i], suffixMax[i + 1]);
    }
    
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const nextIdx = endIdx[i] + 1;
        const total = cnt[i] + (nextIdx < n ? suffixMax[nextIdx] : 0);
        if (total > ans) ans = total;
    }
    
    return ans;
};
```

## Typescript

```typescript
function maximizeWin(prizePositions: number[], k: number): number {
    const n = prizePositions.length;
    const cnt = new Array<number>(n);
    const nextIdx = new Array<number>(n);
    let r = 0;
    for (let l = 0; l < n; ++l) {
        while (r < n && prizePositions[r] - prizePositions[l] <= k) {
            r++;
        }
        cnt[l] = r - l;
        nextIdx[l] = r;
    }

    const suffixMax = new Array<number>(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        suffixMax[i] = Math.max(cnt[i], suffixMax[i + 1]);
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const total = cnt[i] + suffixMax[nextIdx[i]];
        if (total > ans) ans = total;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $prizePositions
     * @param Integer $k
     * @return Integer
     */
    function maximizeWin($prizePositions, $k) {
        $n = count($prizePositions);
        if ($n == 0) return 0;
        $cnt = array_fill(0, $n, 0);
        $nextIdx = array_fill(0, $n, 0);
        $r = 0;
        for ($l = 0; $l < $n; $l++) {
            while ($r < $n && $prizePositions[$r] - $prizePositions[$l] <= $k) {
                $r++;
            }
            $cnt[$l] = $r - $l;
            $nextIdx[$l] = $r;
        }
        $suffix = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $suffix[$i] = max($cnt[$i], $suffix[$i + 1]);
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $total = $cnt[$i];
            if ($nextIdx[$i] < $n) {
                $total += $suffix[$nextIdx[$i]];
            }
            if ($total > $ans) $ans = $total;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximizeWin(_ prizePositions: [Int], _ k: Int) -> Int {
        let n = prizePositions.count
        var cnt = Array(repeating: 0, count: n)
        var right = 0
        for left in 0..<n {
            while right < n && prizePositions[right] - prizePositions[left] <= k {
                right += 1
            }
            cnt[left] = right - left
        }
        var suffixBest = Array(repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            suffixBest[i] = max(cnt[i], suffixBest[i + 1])
        }
        var ans = 0
        for left in 0..<n {
            let nextIdx = left + cnt[left]
            let total = cnt[left] + suffixBest[nextIdx]
            if total > ans { ans = total }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeWin(prizePositions: IntArray, k: Int): Int {
        val n = prizePositions.size
        val cnt = IntArray(n)
        var r = 0
        for (l in 0 until n) {
            while (r < n && prizePositions[r] - prizePositions[l] <= k) {
                r++
            }
            cnt[l] = r - l
        }
        val bestFrom = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            bestFrom[i] = maxOf(cnt[i], bestFrom[i + 1])
        }
        var ans = 0
        for (i in 0 until n) {
            val nextIdx = i + cnt[i]
            var total = cnt[i]
            if (nextIdx < n) {
                total += bestFrom[nextIdx]
            }
            if (total > ans) ans = total
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maximizeWin(List<int> prizePositions, int k) {
    int n = prizePositions.length;
    List<int> cnt = List.filled(n, 0);
    int r = 0;
    for (int l = 0; l < n; ++l) {
      while (r < n && prizePositions[r] - prizePositions[l] <= k) {
        r++;
      }
      cnt[l] = r - l;
    }

    List<int> best = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      best[i] = max(cnt[i], best[i + 1]);
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int total = cnt[i];
      int nextIdx = i + cnt[i];
      if (nextIdx < n) {
        total += best[nextIdx];
      }
      if (total > ans) ans = total;
    }

    return ans;
  }
}
```

## Golang

```go
func maximizeWin(prizePositions []int, k int) int {
    n := len(prizePositions)
    cnt := make([]int, n)
    right := 0
    for left := 0; left < n; left++ {
        for right < n && prizePositions[right]-prizePositions[left] <= k {
            right++
        }
        cnt[left] = right - left
    }

    best := make([]int, n+1)
    for i := n - 1; i >= 0; i-- {
        if cnt[i] > best[i+1] {
            best[i] = cnt[i]
        } else {
            best[i] = best[i+1]
        }
    }

    ans := 0
    for i := 0; i < n; i++ {
        total := cnt[i] + best[i+cnt[i]]
        if total > ans {
            ans = total
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximize_win(prize_positions, k)
  n = prize_positions.length
  cnt = Array.new(n, 0)
  nxt = Array.new(n, 0)

  r = 0
  (0...n).each do |l|
    while r < n && prize_positions[r] - prize_positions[l] <= k
      r += 1
    end
    cnt[l] = r - l
    nxt[l] = r
  end

  suff_max = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    suff_max[i] = cnt[i] > suff_max[i + 1] ? cnt[i] : suff_max[i + 1]
  end

  ans = 0
  (0...n).each do |l|
    total = cnt[l] + suff_max[nxt[l]]
    ans = total if total > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maximizeWin(prizePositions: Array[Int], k: Int): Int = {
        val n = prizePositions.length
        val cnt = new Array[Int](n)
        var r = 0
        for (l <- 0 until n) {
            while (r < n && prizePositions(r) - prizePositions(l) <= k) {
                r += 1
            }
            cnt(l) = r - l
        }
        val suffixBest = new Array[Int](n + 1) // extra slot for ease of indexing
        for (i <- n - 1 to 0 by -1) {
            suffixBest(i) = math.max(cnt(i), suffixBest(i + 1))
        }
        var ans = 0
        for (i <- 0 until n) {
            val total = cnt(i) + suffixBest(i + cnt(i))
            if (total > ans) ans = total
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_win(prize_positions: Vec<i32>, k: i32) -> i32 {
        let n = prize_positions.len();
        if n == 0 {
            return 0;
        }
        let mut cnt = vec![0usize; n];
        let mut next_idx = vec![0usize; n];
        let mut right = 0usize;
        for left in 0..n {
            while right < n && prize_positions[right] - prize_positions[left] <= k {
                right += 1;
            }
            cnt[left] = right - left;
            next_idx[left] = right;
        }
        let mut best_from = vec![0usize; n + 1];
        for i in (0..n).rev() {
            best_from[i] = std::cmp::max(cnt[i], best_from[i + 1]);
        }
        let mut ans = 0usize;
        for i in 0..n {
            let total = cnt[i] + best_from[next_idx[i]];
            if total > ans {
                ans = total;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (maximize-win prizePositions k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length prizePositions))
         (arr (list->vector prizePositions)))
    (if (= n 0)
        0
        (let* ((cnt (make-vector n))
               ;; compute cnt[i]: number of prizes in [arr[i], arr[i]+k]
               (r0 0))
          (let ((r r0))
            (for ([l (in-range n)])
              (let loop ()
                (when (and (< r n)
                           (<= (- (vector-ref arr r) (vector-ref arr l)) k))
                  (set! r (+ r 1))
                  (loop)))
              (vector-set! cnt l (- r l))))
          ;; prefix max
          (define pref (make-vector n))
          (let loop ((i 0) (best 0))
            (when (< i n)
              (define cur (vector-ref cnt i))
              (define nb (if (> cur best) cur best))
              (vector-set! pref i nb)
              (loop (+ i 1) nb)))
          ;; suffix max
          (define suff (make-vector n))
          (let loop ((i (- n 1)) (best 0))
            (when (>= i 0)
              (define cur (vector-ref cnt i))
              (define nb (if (> cur best) cur best))
              (vector-set! suff i nb)
              (loop (- i 1) nb)))
          ;; combine two intervals
          (let ((ans (vector-ref pref (- n 1)))) ; at least one interval
            (let loop ((i 0) (best ans))
              (if (< i (- n 1))
                  (let ((cand (+ (vector-ref pref i)
                                 (vector-ref suff (+ i 1)))))
                    (loop (+ i 1) (if (> cand best) cand best)))
                  best)))))))
```

## Erlang

```erlang
-spec maximize_win(PrizePositions :: [integer()], K :: integer()) -> integer().
-maximize_win(PrizePositions, K) ->
    N = length(PrizePositions),
    PosArr = array:from_list(PrizePositions),

    %% Compute count of prizes in each window starting at i and the index after the window
    {CntRev, NextRev} = compute_counts(N, PosArr, K, 0, -1, [], []),
    CntList   = lists:reverse(CntRev),
    NextList  = lists:reverse(NextRev),

    %% Suffix maximum of counts
    RevCnt = lists:reverse(CntList),
    {_, RevSuf} = lists:foldl(
        fun(C, {PrevMax, Acc}) ->
            Max = if C > PrevMax -> C; true -> PrevMax end,
            {Max, [Max|Acc]}
        end,
        {0, []},
        RevCnt
    ),
    SufList = lists:reverse(RevSuf),
    CntArr   = array:from_list(CntList),
    NextArr  = array:from_list(NextList),
    SufArr   = array:from_list(SufList),

    %% Evaluate best combination of two non‑overlapping windows
    compute_answer(N, 0, CntArr, NextArr, SufArr, 0).

%% ------------------------------------------------------------------
%% Sliding window counts
%% ------------------------------------------------------------------
compute_counts(_N, _PosArr, _K, I, _JPrev, AccCntRev, AccNextRev) when I == _N ->
    {AccCntRev, AccNextRev};
compute_counts(N, PosArr, K, I, JPrev, AccCntRev, AccNextRev) ->
    %% Ensure J starts at least I-1
    J0 = if JPrev < I - 1 -> I - 1; true -> JPrev end,
    J = advance(J0, I, N, PosArr, K),
    Cnt = J - I + 1,
    NextIdx = J + 1,
    compute_counts(N, PosArr, K, I + 1, J, [Cnt|AccCntRev], [NextIdx|AccNextRev]).

advance(J, I, N, PosArr, K) ->
    case (J + 1 < N) andalso
         (array:get(J + 1, PosArr) - array:get(I, PosArr) =< K) of
        true -> advance(J + 1, I, N, PosArr, K);
        false -> J
    end.

%% ------------------------------------------------------------------
%% Compute final answer using suffix maxima
%% ------------------------------------------------------------------
compute_answer(N, I, _CntArr, _NextArr, _SufArr, Max) when I == N ->
    Max;
compute_answer(N, I, CntArr, NextArr, SufArr, Max) ->
    Cnt = array:get(I, CntArr),
    NextIdx = array:get(I, NextArr),
    Add = if NextIdx < N -> array:get(NextIdx, SufArr); true -> 0 end,
    Total = Cnt + Add,
    NewMax = if Total > Max -> Total; true -> Max end,
    compute_answer(N, I + 1, CntArr, NextArr, SufArr, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximize_win(prize_positions :: [integer], k :: integer) :: integer
  def maximize_win(prize_positions, k) do
    n = length(prize_positions)
    pos_tuple = List.to_tuple(prize_positions)

    cnt = compute_cnt(pos_tuple, n, k)
    suff = suffix_max(cnt)

    cnt_t = List.to_tuple(cnt)
    suff_t = List.to_tuple(suff)

    Enum.reduce(0..(n - 1), 0, fn i, ans ->
      cnt_i = elem(cnt_t, i)
      r_i = i + cnt_i - 1
      second = if r_i + 1 < n, do: elem(suff_t, r_i + 1), else: 0
      total = cnt_i + second
      if total > ans, do: total, else: ans
    end)
  end

  defp compute_cnt(pos, n, k) do
    {_, rev_cnt} =
      Enum.reduce(0..(n - 1), {0, []}, fn i, {r, acc} ->
        r = if r < i, do: i, else: r
        r = advance_r(r, i, pos, n, k)
        cnt_i = r - i + 1
        {r, [cnt_i | acc]}
      end)

    Enum.reverse(rev_cnt)
  end

  defp advance_r(r, i, pos, n, k) do
    if r + 1 < n and (:erlang.element(r + 2, pos) - :erlang.element(i + 1, pos) <= k) do
      advance_r(r + 1, i, pos, n, k)
    else
      r
    end
  end

  defp suffix_max(cnt_list) do
    rev = Enum.reverse(cnt_list)

    {suff_rev, _} =
      Enum.reduce(rev, {[], 0}, fn val, {acc, cur_max} ->
        new_max = if val > cur_max, do: val, else: cur_max
        {[new_max | acc], new_max}
      end)

    suff_rev
  end
end
```
