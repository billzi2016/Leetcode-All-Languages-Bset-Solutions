# 1388. Pizza With 3n Slices

## Cpp

```cpp
class Solution {
public:
    int solve(const vector<int>& slices, int l, int r, int pick) {
        int len = r - l + 1;
        vector<int> a(len + 1);
        for (int i = 1; i <= len; ++i) a[i] = slices[l + i - 1];
        const int NEG = -1e9;
        vector<vector<int>> dp(len + 1, vector<int>(pick + 1, NEG));
        for (int i = 0; i <= len; ++i) dp[i][0] = 0;
        for (int i = 1; i <= len; ++i) {
            int maxJ = min(pick, (i + 1) / 2);
            for (int j = 1; j <= maxJ; ++j) {
                int notTake = dp[i - 1][j];
                int take = NEG;
                if (i >= 2) take = dp[i - 2][j - 1] + a[i];
                else if (j == 1) take = a[i]; // i == 1 case
                dp[i][j] = max(notTake, take);
            }
        }
        return dp[len][pick];
    }

    int maxSizeSlices(vector<int>& slices) {
        int n = slices.size() / 3;
        int m = slices.size();
        int ans1 = solve(slices, 0, m - 2, n); // exclude last
        int ans2 = solve(slices, 1, m - 1, n); // exclude first
        return max(ans1, ans2);
    }
};
```

## Java

```java
class Solution {
    public int maxSizeSlices(int[] slices) {
        int total = slices.length;
        int n = total / 3; // number of slices to pick
        // case 1: exclude last slice
        int[] case1 = java.util.Arrays.copyOfRange(slices, 0, total - 1);
        // case 2: exclude first slice
        int[] case2 = java.util.Arrays.copyOfRange(slices, 1, total);
        return Math.max(dp(case1, n), dp(case2, n));
    }

    private int dp(int[] arr, int pick) {
        int m = arr.length;
        // dp[i][k]: max sum using first i elements (0..i-1) picking k slices
        int[][] dp = new int[m + 1][pick + 1];
        final int NEG_INF = Integer.MIN_VALUE / 2; // safe negative infinity

        for (int i = 0; i <= m; i++) {
            java.util.Arrays.fill(dp[i], NEG_INF);
        }
        dp[0][0] = 0;

        for (int i = 1; i <= m; i++) {
            dp[i][0] = 0; // picking zero slices yields sum 0
            int maxK = Math.min(pick, (i + 1) / 2);
            for (int k = 1; k <= maxK; k++) {
                // option 1: skip current slice
                int notTake = dp[i - 1][k];
                // option 2: take current slice, so previous must be i-2
                int takePrev = (i >= 2) ? dp[i - 2][k - 1] : (k == 1 ? 0 : NEG_INF);
                int take = (takePrev == NEG_INF) ? NEG_INF : takePrev + arr[i - 1];
                dp[i][k] = Math.max(notTake, take);
            }
        }
        return dp[m][pick];
    }
}
```

## Python

```python
class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        def solve(arr):
            m = len(arr)
            pick = m // 3
            # dp[i][k]: max sum using first i elements (0..i-1) picking k slices
            dp = [[0] * (pick + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                cur = arr[i - 1]
                # maximum possible picks up to position i is limited by (i+1)//2
                max_k = min(pick, (i + 1) // 2)
                for k in range(1, max_k + 1):
                    # skip current slice
                    option1 = dp[i - 1][k]
                    # take current slice, so previous must be i-2
                    option2 = cur + (dp[i - 2][k - 1] if i >= 2 else 0)
                    dp[i][k] = max(option1, option2)
            return dp[m][pick]

        # circular constraint: either exclude first or exclude last slice
        case1 = solve(slices[:-1])   # exclude last
        case2 = solve(slices[1:])    # exclude first
        return max(case1, case2)
```

## Python3

```python
from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def solve(arr: List[int]) -> int:
            m = len(arr)
            k = m // 3
            NEG = -10**9
            dp = [[NEG] * (k + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                dp[i][0] = 0
            for i in range(1, m + 1):
                maxj = min(k, (i + 1) // 2)
                for j in range(1, maxj + 1):
                    not_take = dp[i - 1][j]
                    take_prev = dp[i - 2][j - 1] if i >= 2 else 0
                    take = arr[i - 1] + take_prev
                    dp[i][j] = not_take if not_take > take else take
            return dp[m][k]

        # case 1: exclude last slice
        ans1 = solve(slices[:-1])
        # case 2: exclude first slice
        ans2 = solve(slices[1:])
        return max(ans1, ans2)
```

## C

```c
int maxSizeSlices(int* slices, int slicesSize) {
    int n = slicesSize / 3;
    int len = slicesSize;

    // helper DP function for linear case
    auto solve = [&](int *a, int l, int k) -> int {
        static int dp[502][168];
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= l; ++i) {
            int maxj = (i + 1) / 2;
            if (maxj > k) maxj = k;
            for (int j = 1; j <= maxj; ++j) {
                int notTake = dp[i - 1][j];
                int take = a[i - 1] + ((i >= 2) ? dp[i - 2][j - 1] : 0);
                dp[i][j] = (notTake > take) ? notTake : take;
            }
        }
        return dp[l][k];
    };

    int res1 = solve(slices, len - 1, n);          // exclude last slice
    int res2 = solve(slices + 1, len - 1, n);      // exclude first slice

    return (res1 > res2) ? res1 : res2;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxSizeSlices(int[] slices)
    {
        int m = slices.Length;
        int n = m / 3;
        return Math.Max(Helper(slices, 0, m - 2, n), Helper(slices, 1, m - 1, n));
    }

    private int Helper(int[] slices, int start, int end, int pick)
    {
        int len = end - start + 1;
        const int NEG = int.MinValue / 2;
        int[,] dp = new int[len + 1, pick + 1];

        for (int i = 0; i <= len; i++)
            for (int j = 0; j <= pick; j++)
                dp[i, j] = NEG;

        dp[0, 0] = 0;

        for (int i = 1; i <= len; i++)
        {
            dp[i, 0] = 0; // picking zero slices yields sum 0
            for (int j = 1; j <= pick; j++)
            {
                int notTake = dp[i - 1, j];
                int take = NEG;
                if (i >= 2)
                {
                    take = dp[i - 2, j - 1] + slices[start + i - 1];
                }
                dp[i, j] = Math.Max(notTake, take);
            }
        }

        return dp[len, pick];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} slices
 * @return {number}
 */
var maxSizeSlices = function(slices) {
    const n = slices.length / 3;
    
    // helper for linear case
    const solve = (arr, picks) => {
        const L = arr.length;
        const K = picks;
        const dp = Array.from({length: L + 1}, () => new Array(K + 1).fill(-Infinity));
        dp[0][0] = 0;
        for (let i = 1; i <= L; i++) {
            dp[i][0] = 0;
        }
        for (let i = 1; i <= L; i++) {
            const maxJ = Math.min(K, Math.floor((i + 1) / 2));
            for (let j = 1; j <= maxJ; j++) {
                const notTake = dp[i - 1][j];
                let take = -Infinity;
                if (i >= 2) {
                    take = dp[i - 2][j - 1] + arr[i - 1];
                } else if (j === 1) { // i == 1
                    take = arr[0];
                }
                dp[i][j] = Math.max(notTake, take);
            }
        }
        return dp[L][K];
    };
    
    const case1 = solve(slices.slice(1), n);               // exclude first slice
    const case2 = solve(slices.slice(0, slices.length - 1), n); // exclude last slice
    return Math.max(case1, case2);
};
```

## Typescript

```typescript
function maxSizeSlices(slices: number[]): number {
    const m = slices.length;
    const pick = Math.floor(m / 3);

    function solve(arr: number[]): number {
        const len = arr.length;
        const dp: number[][] = Array.from({ length: len + 1 }, () => new Array(pick + 1).fill(Number.NEGATIVE_INFINITY));
        for (let i = 0; i <= len; i++) dp[i][0] = 0;

        for (let i = 1; i <= len; i++) {
            const val = arr[i - 1];
            for (let k = 1; k <= pick; k++) {
                // skip current slice
                dp[i][k] = Math.max(dp[i][k], dp[i - 1][k]);
                // take current slice
                if (i >= 2 && dp[i - 2][k - 1] !== Number.NEGATIVE_INFINITY) {
                    dp[i][k] = Math.max(dp[i][k], dp[i - 2][k - 1] + val);
                } else if (i === 1 && k === 1) { // first element can be taken directly
                    dp[i][k] = Math.max(dp[i][k], val);
                }
            }
        }
        return dp[len][pick];
    }

    const case1 = solve(slices.slice(0, m - 1)); // exclude last slice
    const case2 = solve(slices.slice(1));       // exclude first slice

    return Math.max(case1, case2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $slices
     * @return Integer
     */
    function maxSizeSlices($slices) {
        $len = count($slices);
        $pick = intdiv($len, 3); // need to pick n slices

        // helper DP for linear case
        $solve = function($arr) use ($pick) {
            $n = count($arr);
            $negInf = -1000000000; // sufficiently small
            // dp[i][k]: max sum using first i elements (0..i-1) picking k slices
            $dp = array_fill(0, $n + 1, array_fill(0, $pick + 1, $negInf));
            $dp[0][0] = 0;
            for ($i = 1; $i <= $n; $i++) {
                $maxK = min($pick, intdiv($i + 1, 2)); // cannot pick more than ceil(i/2)
                for ($k = 0; $k <= $maxK; $k++) {
                    // not take current slice
                    $dp[$i][$k] = $dp[$i - 1][$k];
                    if ($k > 0) {
                        if ($i == 1) {
                            $prev = 0; // picking the first element directly
                        } else {
                            $prev = $dp[$i - 2][$k - 1];
                        }
                        if ($prev != $negInf) {
                            $cand = $prev + $arr[$i - 1];
                            if ($cand > $dp[$i][$k]) {
                                $dp[$i][$k] = $cand;
                            }
                        }
                    }
                }
            }
            return $dp[$n][$pick];
        };

        // Case 1: exclude last slice
        $case1 = $solve(array_slice($slices, 0, $len - 1));
        // Case 2: exclude first slice
        $case2 = $solve(array_slice($slices, 1));

        return max($case1, $case2);
    }
}
```

## Swift

```swift
class Solution {
    func maxSizeSlices(_ slices: [Int]) -> Int {
        let total = slices.count
        let n = total / 3
        
        func solve(_ arr: [Int], _ k: Int) -> Int {
            let m = arr.count
            if k == 0 { return 0 }
            var dp = Array(repeating: Array(repeating: -1_000_000_000, count: k + 1), count: m + 1)
            for i in 0...m {
                dp[i][0] = 0
            }
            for i in 1...m {
                let maxJ = min(k, (i + 1) / 2)
                for j in 1...maxJ {
                    let notTake = dp[i - 1][j]
                    var take: Int
                    if i >= 2 {
                        take = dp[i - 2][j - 1] + arr[i - 1]
                    } else { // i == 1
                        take = (j == 1) ? arr[0] : -1_000_000_000
                    }
                    dp[i][j] = max(notTake, take)
                }
            }
            return dp[m][k]
        }
        
        let case1 = solve(Array(slices[0..<(total - 1)]), n)
        let case2 = solve(Array(slices[1..<total]), n)
        return max(case1, case2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSizeSlices(slices: IntArray): Int {
        val m = slices.size
        val n = m / 3
        // Exclude last slice
        val case1 = dp(slices.sliceArray(0 until m - 1), n)
        // Exclude first slice
        val case2 = dp(slices.sliceArray(1 until m), n)
        return maxOf(case1, case2)
    }

    private fun dp(arr: IntArray, pick: Int): Int {
        val len = arr.size
        val NEG = -1_000_000_000
        val dp = Array(len + 1) { IntArray(pick + 1) { NEG } }
        for (i in 0..len) dp[i][0] = 0

        for (i in 1..len) {
            for (k in 1..pick) {
                var best = dp[i - 1][k] // not take current
                val take = if (i >= 2 && dp[i - 2][k - 1] != NEG) {
                    dp[i - 2][k - 1] + arr[i - 1]
                } else if (i == 1 && k == 1) {
                    arr[0]
                } else {
                    NEG
                }
                if (take > best) best = take
                dp[i][k] = best
            }
        }
        return dp[len][pick]
    }
}
```

## Dart

```dart
class Solution {
  int maxSizeSlices(List<int> slices) {
    int m = slices.length;
    int n = m ~/ 3;

    int solve(List<int> arr) {
      int len = arr.length;
      List<List<int>> dp = List.generate(len + 1, (_) => List.filled(n + 1, 0));
      for (int i = 1; i <= len; ++i) {
        for (int j = 1; j <= n && j <= (i + 1) ~/ 2; ++j) {
          int notTake = dp[i - 1][j];
          int take;
          if (i == 1) {
            take = (j == 1) ? arr[0] : 0;
          } else {
            take = dp[i - 2][j - 1] + arr[i - 1];
          }
          dp[i][j] = notTake > take ? notTake : take;
        }
      }
      return dp[len][n];
    }

    int case1 = solve(slices.sublist(0, m - 1));
    int case2 = solve(slices.sublist(1));
    return case1 > case2 ? case1 : case2;
  }
}
```

## Golang

```go
func maxSizeSlices(slices []int) int {
	n := len(slices) / 3
	case1 := solve(slices[:len(slices)-1], n)
	case2 := solve(slices[1:], n)
	if case1 > case2 {
		return case1
	}
	return case2
}

func solve(arr []int, picks int) int {
	m := len(arr)
	const INF = -1 << 60
	dp := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([]int, picks+1)
		for j := 0; j <= picks; j++ {
			dp[i][j] = INF
		}
		dp[i][0] = 0
	}

	for i := 1; i <= m; i++ {
		val := arr[i-1]
		maxK := picks
		if 2*maxK-1 > i {
			maxK = (i + 1) / 2
		}
		for k := 1; k <= maxK; k++ {
			notTake := dp[i-1][k]
			take := INF
			if i >= 2 {
				if dp[i-2][k-1] != INF {
					take = dp[i-2][k-1] + val
				}
			} else if i == 1 && k == 1 {
				take = val
			}
			if notTake > take {
				dp[i][k] = notTake
			} else {
				dp[i][k] = take
			}
		}
	}
	return dp[m][picks]
}
```

## Ruby

```ruby
def max_size_slices(slices)
  m = slices.length
  n = m / 3

  solve = lambda do |arr|
    len = arr.length
    dp = Array.new(len + 1) { Array.new(n + 1, 0) }

    (1..len).each do |i|
      max_k = [n, (i + 1) / 2].min
      (1..max_k).each do |k|
        not_take = dp[i - 1][k]
        take = arr[i - 1] + (i >= 2 ? dp[i - 2][k - 1] : 0)
        dp[i][k] = not_take > take ? not_take : take
      end
    end

    dp[len][n]
  end

  case1 = solve.call(slices[0...-1])   # exclude last slice
  case2 = solve.call(slices[1..-1])    # exclude first slice
  case1 > case2 ? case1 : case2
end
```

## Scala

```scala
object Solution {
    def maxSizeSlices(slices: Array[Int]): Int = {
        val n = slices.length / 3

        def solve(arr: Array[Int]): Int = {
            val L = arr.length
            val dp = Array.ofDim[Int](L + 1, n + 1)

            for (i <- 1 to L) {
                val cur = arr(i - 1)
                val maxJ = math.min(n, (i + 1) / 2)
                var j = 1
                while (j <= maxJ) {
                    val notTake = dp(i - 1)(j)
                    val take =
                        if (i >= 2) dp(i - 2)(j - 1) + cur
                        else if (j == 1) cur
                        else Int.MinValue
                    dp(i)(j) = math.max(notTake, take)
                    j += 1
                }
            }
            dp(L)(n)
        }

        val case1 = solve(slices.slice(0, slices.length - 1))
        val case2 = solve(slices.slice(1, slices.length))
        math.max(case1, case2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_size_slices(slices: Vec<i32>) -> i32 {
        fn solve(arr: &[i32], k: usize) -> i32 {
            let m = arr.len();
            if k == 0 || m == 0 {
                return 0;
            }
            const NEG: i32 = -1_000_000_000;
            let mut dp = vec![vec![NEG; k + 1]; m + 1];
            dp[0][0] = 0;
            if m >= 1 {
                dp[1][0] = 0;
                if k >= 1 {
                    dp[1][1] = arr[0];
                }
            }
            for i in 2..=m {
                dp[i][0] = 0;
                let max_j = std::cmp::min(k, (i + 1) / 2);
                for j in 1..=max_j {
                    let not_take = dp[i - 1][j];
                    let take = if dp[i - 2][j - 1] != NEG {
                        dp[i - 2][j - 1] + arr[i - 1]
                    } else {
                        NEG
                    };
                    dp[i][j] = if not_take > take { not_take } else { take };
                }
            }
            dp[m][k]
        }

        let n = slices.len() / 3;
        let case1 = solve(&slices[0..slices.len() - 1], n);
        let case2 = solve(&slices[1..], n);
        if case1 > case2 { case1 } else { case2 }
    }
}
```

## Racket

```racket
(define/contract (max-size-slices slices)
  (-> (listof exact-integer?) exact-integer?)
  (letrec
      ((solve
        (lambda (vec start end k)
          (let* ((m (- end start))
                 (INF -1000000000)
                 (dp (make-vector (+ m 1) #f)))
            ;; initialise inner vectors
            (for ([i (in-range (+ m 1))])
              (vector-set! dp i (make-vector (+ k 1) INF)))
            ;; base: pick 0 slices -> sum 0
            (for ([i (in-range (+ m 1))])
              (vector-set! (vector-ref dp i) 0 0))
            ;; DP transition
            (for ([i (in-range 1 (add1 m))])
              (let* ((idx (+ start (- i 1)))
                     (val (vector-ref vec idx))
                     (maxj (min k (quotient (+ i 1) 2))))
                (for ([j (in-range 1 (add1 maxj))])
                  (define not-pick (vector-ref (vector-ref dp (- i 1)) j))
                  (define pick-prev
                    (cond [(>= i 2)
                           (vector-ref (vector-ref dp (- i 2)) (- j 1))]
                          [(and (= i 1) (= j 1)) 0]
                          [else INF]))
                  (define pick-val (+ val pick-prev))
                  (define best (max not-pick pick-val))
                  (vector-set! (vector-ref dp i) j best))))
            (vector-ref (vector-ref dp m) k)))))
    (let* ((len (length slices))
           (n   (quotient len 3))
           (vec (list->vector slices))
           (case1 (solve vec 0 (- len 1) n)) ; exclude last slice
           (case2 (solve vec 1 len       n))) ; exclude first slice
      (if (> case1 case2) case1 case2))))
```

## Erlang

```erlang
-spec max_size_slices(Slices :: [integer()]) -> integer().
max_size_slices(Slices) ->
    Len = length(Slices),
    N = Len div 3,
    % case: exclude first slice
    S1 = tl(Slices),
    Res1 = solve_linear(S1, N),
    % case: exclude last slice
    S2 = lists:sublist(Slices, 1, Len - 1),
    Res2 = solve_linear(S2, N),
    max(Res1, Res2).

-spec solve_linear([integer()], integer()) -> integer().
solve_linear(Arr, Pick) ->
    DPPrev2 = init_dp(Pick),
    DPPrev = init_dp(Pick),
    solve_loop(Arr, Pick, DPPrev2, DPPrev).

-spec solve_loop([integer()], integer(), [integer()], [integer()]) -> integer().
solve_loop([], Pick, _DPPrev2, DPPrev) ->
    lists:nth(Pick + 1, DPPrev);
solve_loop([Val | Rest], Pick, DPPrev2, DPPrev) ->
    NewDP = [dp_k(K, Val, DPPrev, DPPrev2) || K <- lists:seq(0, Pick)],
    solve_loop(Rest, Pick, DPPrev, NewDP).

-spec dp_k(integer(), integer(), [integer()], [integer()]) -> integer().
dp_k(K, Val, DPPrev, DPPrev2) ->
    NotTake = lists:nth(K + 1, DPPrev),
    Take = if
        K > 0 -> Val + lists:nth(K, DPPrev2);
        true   -> -1000000000
    end,
    max(NotTake, Take).

-spec init_dp(integer()) -> [integer()].
init_dp(Pick) ->
    [0 | lists:duplicate(Pick, -1000000000)].

-spec max(integer(), integer()) -> integer().
max(A, B) when A >= B -> A;
max(_A, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_size_slices(slices :: [integer]) :: integer
  def max_size_slices(slices) do
    n = div(length(slices), 3)

    arr1 = Enum.slice(slices, 0, length(slices) - 1)
    arr2 = Enum.slice(slices, 1, length(slices) - 1)

    max1 = solve(arr1, n)
    max2 = solve(arr2, n)

    if max1 > max2, do: max1, else: max2
  end

  defp solve(arr, pick) do
    len = length(arr)

    dp =
      Enum.reduce(0..len - 1, [], fn i, acc ->
        row =
          Enum.map(0..pick, fn k ->
            cond do
              k == 0 ->
                0

              i == 0 and k == 1 ->
                Enum.at(arr, 0)

              i == 0 ->
                0

              true ->
                not_pick = Enum.at(acc, -1) |> Enum.at(k)

                pick_val =
                  if i >= 2 do
                    prev2 = Enum.at(acc, -2) |> Enum.at(k - 1)
                    prev2 + Enum.at(arr, i)
                  else
                    if k == 1 do
                      Enum.at(arr, i)
                    else
                      -1_000_000_000
                    end
                  end

                if not_pick > pick_val, do: not_pick, else: pick_val
            end
          end)

        acc ++ [row]
      end)

    List.last(dp) |> Enum.at(pick)
  end
end
```
