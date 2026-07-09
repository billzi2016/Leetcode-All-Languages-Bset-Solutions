# 1458. Max Dot Product of Two Subsequences

## Cpp

```cpp
class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        const int INF_NEG = INT_MIN;
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, INF_NEG));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                int prod = nums1[i] * nums2[j];
                int best = prod;
                if (dp[i + 1][j + 1] != INF_NEG) {
                    best = max(best, prod + dp[i + 1][j + 1]);
                }
                best = max({best, dp[i + 1][j], dp[i][j + 1]});
                dp[i][j] = best;
            }
        }
        return dp[0][0];
    }
};
```

## Java

```java
class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        long NEG = Long.MIN_VALUE / 4;
        long[][] dp = new long[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            java.util.Arrays.fill(dp[i], NEG);
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                long prod = (long) nums1[i - 1] * nums2[j - 1];
                dp[i][j] = Math.max(prod, prod + dp[i - 1][j - 1]);
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j]);
                dp[i][j] = Math.max(dp[i][j], dp[i][j - 1]);
            }
        }
        return (int) dp[n][m];
    }
}
```

## Python

```python
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        # dp[i][j] for first i elements of nums1 and first j elements of nums2
        neg_inf = float('-inf')
        dp = [[neg_inf] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            a = nums1[i - 1]
            for j in range(1, m + 1):
                b = nums2[j - 1]
                pair = a * b
                dp[i][j] = max(
                    pair,                     # start new subsequence with this pair
                    dp[i - 1][j - 1] + pair, # extend previous best
                    dp[i - 1][j],             # skip a
                    dp[i][j - 1]              # skip b
                )
        return dp[n][m]
```

## Python3

```python
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**9
        dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            a = nums1[i - 1]
            for j in range(1, m + 1):
                b = nums2[j - 1]
                prod = a * b
                dp[i][j] = max(
                    prod,
                    dp[i - 1][j - 1] + prod,
                    dp[i - 1][j],
                    dp[i][j - 1]
                )
        return dp[n][m]
```

## C

```c
int maxDotProduct(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size;
    int m = nums2Size;
    const int NEG_INF = -1000000000;  // sufficiently small
    
    int **dp = (int **)malloc((n + 1) * sizeof(int *));
    for (int i = 0; i <= n; ++i) {
        dp[i] = (int *)malloc((m + 1) * sizeof(int));
    }
    
    for (int i = 0; i <= n; ++i) dp[i][0] = NEG_INF;
    for (int j = 0; j <= m; ++j) dp[0][j] = NEG_INF;
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            int prod = nums1[i - 1] * nums2[j - 1];
            int extend = dp[i - 1][j - 1] + prod;
            int start   = prod;
            int skipA   = dp[i - 1][j];
            int skipB   = dp[i][j - 1];
            
            int best = extend;
            if (start > best) best = start;
            if (skipA > best) best = skipA;
            if (skipB > best) best = skipB;
            dp[i][j] = best;
        }
    }
    
    int result = dp[n][m];
    
    for (int i = 0; i <= n; ++i) free(dp[i]);
    free(dp);
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDotProduct(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int m = nums2.Length;
        const int NEG_INF = -1000000000; // sufficiently small
        
        int[,] dp = new int[n + 1, m + 1];
        for (int i = 0; i <= n; i++) dp[i, 0] = NEG_INF;
        for (int j = 0; j <= m; j++) dp[0, j] = NEG_INF;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int prod = nums1[i - 1] * nums2[j - 1];
                int best = prod;
                if (dp[i - 1, j - 1] != NEG_INF) {
                    best = Math.Max(best, dp[i - 1, j - 1] + prod);
                }
                dp[i, j] = Math.Max(Math.Max(dp[i - 1, j], dp[i, j - 1]), best);
            }
        }

        return dp[n, m];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDotProduct = function(nums1, nums2) {
    const n = nums1.length;
    const m = nums2.length;
    const dp = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(Number.NEGATIVE_INFINITY));
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            const prod = nums1[i - 1] * nums2[j - 1];
            dp[i][j] = Math.max(
                prod,
                dp[i - 1][j - 1] + prod,
                dp[i - 1][j],
                dp[i][j - 1]
            );
        }
    }
    
    return dp[n][m];
};
```

## Typescript

```typescript
function maxDotProduct(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const m = nums2.length;
    const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(Number.NEGATIVE_INFINITY));
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            const prod = nums1[i - 1] * nums2[j - 1];
            dp[i][j] = Math.max(
                prod,
                dp[i - 1][j - 1] + prod,
                dp[i - 1][j],
                dp[i][j - 1]
            );
        }
    }
    return dp[n][m];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxDotProduct($nums1, $nums2) {
        $n = count($nums1);
        $m = count($nums2);
        $dp = array_fill(0, $n, array_fill(0, $m, 0));

        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $m; ++$j) {
                $prod = $nums1[$i] * $nums2[$j];
                $best = $prod;

                if ($i > 0 && $j > 0) {
                    $best = max($best, $prod + $dp[$i - 1][$j - 1]);
                }
                if ($i > 0) {
                    $best = max($best, $dp[$i - 1][$j]);
                }
                if ($j > 0) {
                    $best = max($best, $dp[$i][$j - 1]);
                }

                $dp[$i][$j] = $best;
            }
        }

        return $dp[$n - 1][$m - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maxDotProduct(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        let m = nums2.count
        let NEG = -1_000_000_000
        var dp = Array(repeating: Array(repeating: NEG, count: m + 1), count: n + 1)
        for i in 1...n {
            for j in 1...m {
                let prod = nums1[i - 1] * nums2[j - 1]
                var best = max(prod, prod + dp[i - 1][j - 1])
                best = max(best, dp[i - 1][j])
                best = max(best, dp[i][j - 1])
                dp[i][j] = best
            }
        }
        return dp[n][m]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDotProduct(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        val m = nums2.size
        val dp = Array(n + 1) { IntArray(m + 1) { Int.MIN_VALUE } }
        for (i in 1..n) {
            for (j in 1..m) {
                val prod = nums1[i - 1] * nums2[j - 1]
                var best = prod // start new subsequence with this pair
                if (dp[i - 1][j - 1] != Int.MIN_VALUE) {
                    best = maxOf(best, dp[i - 1][j - 1] + prod)
                }
                best = maxOf(best, dp[i - 1][j])
                best = maxOf(best, dp[i][j - 1])
                dp[i][j] = best
            }
        }
        return dp[n][m]
    }
}
```

## Dart

```dart
class Solution {
  int maxDotProduct(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    int m = nums2.length;
    const int NEG_INF = -1000000000; // sufficiently small sentinel
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(m + 1, NEG_INF));
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= m; ++j) {
        int prod = nums1[i - 1] * nums2[j - 1];
        int extend = dp[i - 1][j - 1] + prod;
        int start = prod;
        int skipA = dp[i - 1][j];
        int skipB = dp[i][j - 1];
        int best = extend;
        if (start > best) best = start;
        if (skipA > best) best = skipA;
        if (skipB > best) best = skipB;
        dp[i][j] = best;
      }
    }
    return dp[n][m];
  }
}
```

## Golang

```go
func maxDotProduct(nums1 []int, nums2 []int) int {
    n, m := len(nums1), len(nums2)
    const negInf = -1 << 60

    // dp[i][j] represents the answer for first i elements of nums1 and first j elements of nums2
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
        for j := range dp[i] {
            dp[i][j] = negInf
        }
    }

    max := func(a, b int) int {
        if a > b {
            return a
        }
        return b
    }

    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            prod := nums1[i-1] * nums2[j-1]

            // start new subsequence with this pair or extend previous one
            dp[i][j] = max(prod, dp[i-1][j-1]+prod)

            // skip element from nums1 or nums2
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        }
    }

    return dp[n][m]
}
```

## Ruby

```ruby
def max_dot_product(nums1, nums2)
  n = nums1.length
  m = nums2.length
  neg_inf = -10**15
  dp = Array.new(n + 1) { Array.new(m + 1, neg_inf) }

  (1..n).each do |i|
    (1..m).each do |j|
      prod = nums1[i - 1] * nums2[j - 1]
      dp[i][j] = [
        prod,
        dp[i - 1][j - 1] + prod,
        dp[i - 1][j],
        dp[i][j - 1]
      ].max
    end
  end

  dp[n][m]
end
```

## Scala

```scala
object Solution {
    def maxDotProduct(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        val m = nums2.length
        val NEG = -1000000000 // smaller than any possible answer
        val dp = Array.ofDim[Int](n + 1, m + 1)
        for (i <- 0 to n) java.util.Arrays.fill(dp(i), NEG)

        for (i <- 1 to n) {
            val a = nums1(i - 1)
            for (j <- 1 to m) {
                val b = nums2(j - 1)
                val prod = a * b
                var best = dp(i - 1)(j)               // skip a
                if (dp(i)(j - 1) > best) best = dp(i)(j - 1)   // skip b
                if (prod > best) best = prod           // start new subsequence
                val extend = dp(i - 1)(j - 1) + prod    // extend previous subsequence
                if (extend > best) best = extend
                dp(i)(j) = best
            }
        }
        dp(n)(m)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let m = nums2.len();
        const NEG_INF: i32 = -1_000_000_000;
        let mut dp = vec![vec![NEG_INF; m + 1]; n + 1];
        for i in 1..=n {
            for j in 1..=m {
                let prod = nums1[i - 1] * nums2[j - 1];
                let mut best = prod;
                let ext = dp[i - 1][j - 1] + prod;
                if ext > best {
                    best = ext;
                }
                if dp[i - 1][j] > best {
                    best = dp[i - 1][j];
                }
                if dp[i][j - 1] > best {
                    best = dp[i][j - 1];
                }
                dp[i][j] = best;
            }
        }
        dp[n][m]
    }
}
```

## Racket

```racket
(define/contract (max-dot-product nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (n (vector-length v1))
         (m (vector-length v2))
         (neg-inf -1000000000)
         (dp (make-vector n)))
    ;; initialize dp rows
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector m neg-inf)))
    ;; fill DP bottom‑up
    (for ([i (in-range (sub1 n) -1 -1)])          ; i = n-1 .. 0
      (let ((row (vector-ref dp i))
            (a   (vector-ref v1 i)))
        (for ([j (in-range (sub1 m) -1 -1)])    ; j = m-1 .. 0
          (let* ((b       (vector-ref v2 j))
                 (prod    (* a b))
                 (best    prod)
                 (extend  (if (and (< i (sub1 n)) (< j (sub1 m)))
                              (+ prod (vector-ref (vector-ref dp (+ i 1)) (+ j 1)))
                              neg-inf))
                 (skip1   (if (< i (sub1 n))
                              (vector-ref (vector-ref dp (+ i 1)) j)
                              neg-inf))
                 (skip2   (if (< j (sub1 m))
                              (vector-ref row (+ j 1))
                              neg-inf)))
            (set! best (max best extend skip1 skip2))
            (vector-set! row j best)))))
    (vector-ref (vector-ref dp 0) 0)))
```

## Erlang

```erlang
-spec max_dot_product(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
max_dot_product(Nums1, Nums2) ->
    NegInf = -1000000000,
    N = length(Nums1),
    M = length(Nums2),
    T1 = list_to_tuple(Nums1),
    T2 = list_to_tuple(Nums2),
    InitRowList = lists:duplicate(M + 1, NegInf),          % index 0..M
    PrevTuple = list_to_tuple(InitRowList),
    GlobalMax = loop_i(1, N, T1, T2, M, NegInf, PrevTuple, NegInf),
    GlobalMax.

%% Loop over rows (i from 1 to N)
loop_i(I, N, _T1, _T2, _M, _NegInf, _PrevTuple, GlobalMax) when I > N ->
    GlobalMax;
loop_i(I, N, T1, T2, M, NegInf, PrevTuple, GlobalMax) ->
    A = element(I, T1),
    {CurrAccRev, NewGlobal} = loop_j(1, M, A, T2, NegInf, PrevTuple, [], NegInf, NegInf, GlobalMax),
    RowValues = lists:reverse(CurrAccRev),                % values for j=1..M
    CurrRowList = [NegInf | RowValues],                  % prepend dummy for index 0
    CurrTuple = list_to_tuple(CurrRowList),
    loop_i(I + 1, N, T1, T2, M, NegInf, CurrTuple, NewGlobal).

%% Loop over columns (j from 1 to M)
loop_j(J, M, _A, _T2, _NegInf, _PrevTuple, AccRev, _PrevDiag, _PrevLeft, GlobalMax) when J > M ->
    {AccRev, GlobalMax};
loop_j(J, M, A, T2, NegInf, PrevTuple, AccRev, PrevDiag, PrevLeft, GlobalMax) ->
    B = element(J, T2),
    Prod = A * B,
    Option1 = Prod,
    Option2 = case PrevDiag of
                  X when X > NegInf -> X + Prod;
                  _ -> NegInf
              end,
    Option3 = element(J, PrevTuple),   % dp[i-1][j]
    Option4 = PrevLeft,                % dp[i][j-1]
    Best = max4(Option1, Option2, Option3, Option4),
    NewGlobal = if Best > GlobalMax -> Best; true -> GlobalMax end,
    NextPrevDiag = element(J, PrevTuple),   % becomes dp[i-1][j] for next column
    loop_j(J + 1, M, A, T2, NegInf, PrevTuple, [Best | AccRev], NextPrevDiag, Best, NewGlobal).

max4(A, B, C, D) ->
    max(max(A, B), max(C, D)).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_dot_product(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_dot_product(nums1, nums2) do
    n = length(nums1)
    m = length(nums2)
    neg_inf = -1_000_000_000

    {_final_row, answer} =
      Enum.reduce(0..(n - 1), {List.duplicate(neg_inf, m), neg_inf}, fn i, {prev_row, ans} ->
        a = Enum.at(nums1, i)

        {cur_rev, _} =
          Enum.reduce(0..(m - 1), {[], nil}, fn j, {row_acc, left_val} ->
            b = Enum.at(nums2, j)
            prod = a * b
            best = prod

            if i > 0 and j > 0 do
              diag = Enum.at(prev_row, j - 1) + prod
              best = max(best, diag)
            end

            if i > 0 do
              up = Enum.at(prev_row, j)
              best = max(best, up)
            end

            if j > 0 do
              best = max(best, left_val)
            end

            {[best | row_acc], best}
          end)

        cur_row = Enum.reverse(cur_rev)
        new_ans = max(ans, List.last(cur_row))
        {cur_row, new_ans}
      end)

    answer
  end
end
```
