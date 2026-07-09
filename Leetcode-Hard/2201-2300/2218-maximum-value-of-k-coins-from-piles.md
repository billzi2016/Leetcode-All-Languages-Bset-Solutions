# 2218. Maximum Value of K Coins From Piles

## Cpp

```cpp
class Solution {
public:
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        const int NEG_INF = -1e9;
        vector<int> dp(k + 1, NEG_INF);
        dp[0] = 0;
        for (const auto& pile : piles) {
            int sz = min((int)pile.size(), k);
            vector<int> pref(sz + 1, 0);
            for (int i = 1; i <= sz; ++i) {
                pref[i] = pref[i - 1] + pile[i - 1];
            }
            vector<int> ndp(k + 1, NEG_INF);
            for (int used = 0; used <= k; ++used) {
                if (dp[used] == NEG_INF) continue;
                // take t coins from current pile
                for (int t = 0; t <= sz && used + t <= k; ++t) {
                    ndp[used + t] = max(ndp[used + t], dp[used] + pref[t]);
                }
            }
            dp.swap(ndp);
        }
        return dp[k];
    }
};
```

## Java

```java
class Solution {
    public int maxValueOfCoins(java.util.List<java.util.List<Integer>> piles, int k) {
        int[] dp = new int[k + 1];
        for (java.util.List<Integer> pile : piles) {
            int m = Math.min(pile.size(), k);
            int[] prefix = new int[m + 1];
            for (int i = 1; i <= m; i++) {
                prefix[i] = prefix[i - 1] + pile.get(i - 1);
            }
            int[] ndp = dp.clone();
            for (int take = 1; take <= m; take++) {
                int val = prefix[take];
                for (int total = take; total <= k; total++) {
                    ndp[total] = Math.max(ndp[total], dp[total - take] + val);
                }
            }
            dp = ndp;
        }
        return dp[k];
    }
}
```

## Python

```python
class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [0] * (k + 1)
        for pile in piles:
            limit = min(len(pile), k)
            prefix = [0]
            s = 0
            for i in range(limit):
                s += pile[i]
                prefix.append(s)
            prev = dp[:]
            for cur in range(1, k + 1):
                max_take = min(limit, cur)
                best = prev[cur]  # taking 0 from this pile
                for take in range(1, max_take + 1):
                    val = prev[cur - take] + prefix[take]
                    if val > best:
                        best = val
                dp[cur] = best
        return dp[k]
```

## Python3

```python
class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        INF_NEG = -10**18
        dp = [INF_NEG] * (k + 1)
        dp[0] = 0

        for pile in piles:
            m = min(len(pile), k)
            prefix = [0] * (m + 1)
            s = 0
            for i in range(m):
                s += pile[i]
                prefix[i + 1] = s

            newdp = [INF_NEG] * (k + 1)
            for used in range(k + 1):
                if dp[used] == INF_NEG:
                    continue
                # take j coins from current pile
                max_take = min(m, k - used)
                for j in range(max_take + 1):
                    val = dp[used] + prefix[j]
                    if val > newdp[used + j]:
                        newdp[used + j] = val
            dp = newdp

        return dp[k]
```

## C

```c
int maxValueOfCoins(int** piles, int pilesSize, int* pilesColSize, int k) {
    const int NEG_INF = -1000000000;
    int *dp = (int*)malloc((k + 1) * sizeof(int));
    for (int i = 0; i <= k; ++i) dp[i] = NEG_INF;
    dp[0] = 0;

    for (int p = 0; p < pilesSize; ++p) {
        int len = pilesColSize[p];
        int maxTake = len < k ? len : k;

        // compute prefix sums up to maxTake
        int *pref = (int*)malloc((maxTake + 1) * sizeof(int));
        pref[0] = 0;
        for (int t = 1; t <= maxTake; ++t) {
            pref[t] = pref[t - 1] + piles[p][t - 1];
        }

        int *ndp = (int*)malloc((k + 1) * sizeof(int));
        for (int j = 0; j <= k; ++j) ndp[j] = dp[j]; // take 0 from this pile

        for (int j = 0; j <= k; ++j) {
            if (dp[j] == NEG_INF) continue;
            int limit = maxTake < (k - j) ? maxTake : (k - j);
            for (int x = 1; x <= limit; ++x) {
                int val = dp[j] + pref[x];
                if (val > ndp[j + x]) ndp[j + x] = val;
            }
        }

        free(dp);
        free(pref);
        dp = ndp;
    }

    int result = dp[k];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxValueOfCoins(IList<IList<int>> piles, int k)
    {
        int[] dp = new int[k + 1];
        foreach (var pile in piles)
        {
            int takeLimit = Math.Min(k, pile.Count);
            int[] prefix = new int[takeLimit + 1];
            for (int i = 1; i <= takeLimit; ++i)
                prefix[i] = prefix[i - 1] + pile[i - 1];

            int[] ndp = new int[k + 1];
            Array.Copy(dp, ndp, k + 1); // taking 0 coins from this pile

            for (int used = 0; used <= k; ++used)
            {
                if (dp[used] == 0 && used != 0) continue; // unreachable state
                for (int t = 1; t <= takeLimit && used + t <= k; ++t)
                {
                    int val = dp[used] + prefix[t];
                    if (val > ndp[used + t])
                        ndp[used + t] = val;
                }
            }

            dp = ndp;
        }
        return dp[k];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} piles
 * @param {number} k
 * @return {number}
 */
var maxValueOfCoins = function(piles, k) {
    let dp = new Array(k + 1).fill(0);
    for (const pile of piles) {
        const m = pile.length;
        const prefix = new Array(m + 1);
        prefix[0] = 0;
        for (let i = 1; i <= m; i++) {
            prefix[i] = prefix[i - 1] + pile[i - 1];
        }
        const ndp = dp.slice(); // copy current dp
        for (let j = 1; j <= k; j++) {
            let best = ndp[j]; // taking 0 coins from this pile
            const limit = Math.min(m, j);
            for (let take = 1; take <= limit; take++) {
                const cand = dp[j - take] + prefix[take];
                if (cand > best) best = cand;
            }
            ndp[j] = best;
        }
        dp = ndp;
    }
    return dp[k];
};
```

## Typescript

```typescript
function maxValueOfCoins(piles: number[][], k: number): number {
    const dp = new Array(k + 1).fill(-Infinity);
    dp[0] = 0;
    for (const pile of piles) {
        const limit = Math.min(pile.length, k);
        const prefix = new Array(limit + 1).fill(0);
        for (let i = 1; i <= limit; ++i) {
            prefix[i] = prefix[i - 1] + pile[i - 1];
        }
        const ndp = dp.slice();
        for (let used = 0; used <= k; ++used) {
            if (dp[used] === -Infinity) continue;
            for (let take = 1; take <= limit && used + take <= k; ++take) {
                const val = dp[used] + prefix[take];
                if (val > ndp[used + take]) ndp[used + take] = val;
            }
        }
        for (let i = 0; i <= k; ++i) dp[i] = ndp[i];
    }
    return dp[k];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $piles
     * @param Integer $k
     * @return Integer
     */
    function maxValueOfCoins($piles, $k) {
        $negInf = -1e18;
        $dp = array_fill(0, $k + 1, $negInf);
        $dp[0] = 0;

        foreach ($piles as $pile) {
            $len = count($pile);
            $maxTake = min($len, $k);

            // prefix sums for this pile
            $prefix = [0];
            $sum = 0;
            for ($i = 0; $i < $maxTake; $i++) {
                $sum += $pile[$i];
                $prefix[] = $sum; // prefix[t] = sum of first t coins
            }

            $newdp = $dp; // copy current dp

            for ($take = 1; $take <= $maxTake; $take++) {
                $val = $prefix[$take];
                for ($j = $take; $j <= $k; $j++) {
                    if ($dp[$j - $take] != $negInf) {
                        $candidate = $dp[$j - $take] + $val;
                        if ($candidate > $newdp[$j]) {
                            $newdp[$j] = $candidate;
                        }
                    }
                }
            }

            $dp = $newdp;
        }

        return $dp[$k];
    }
}
```

## Swift

```swift
class Solution {
    func maxValueOfCoins(_ piles: [[Int]], _ k: Int) -> Int {
        var dp = Array(repeating: 0, count: k + 1)
        for pile in piles {
            let limit = min(pile.count, k)
            var prefix = Array(repeating: 0, count: limit + 1)
            for i in 1...limit {
                prefix[i] = prefix[i - 1] + pile[i - 1]
            }
            var newDP = dp
            if limit > 0 {
                for t in 1...limit {
                    let val = prefix[t]
                    for j in t...k {
                        let candidate = dp[j - t] + val
                        if candidate > newDP[j] {
                            newDP[j] = candidate
                        }
                    }
                }
            }
            dp = newDP
        }
        return dp[k]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxValueOfCoins(piles: List<List<Int>>, k: Int): Int {
        val dp = IntArray(k + 1) { Int.MIN_VALUE / 2 }
        dp[0] = 0
        for (pile in piles) {
            val m = pile.size
            val prefix = IntArray(m + 1)
            for (i in 1..m) {
                prefix[i] = prefix[i - 1] + pile[i - 1]
            }
            val newDp = IntArray(k + 1) { Int.MIN_VALUE / 2 }
            for (used in 0..k) {
                if (dp[used] <= Int.MIN_VALUE / 4) continue
                val maxTake = kotlin.math.min(m, k - used)
                for (t in 0..maxTake) {
                    val total = dp[used] + prefix[t]
                    if (total > newDp[used + t]) {
                        newDp[used + t] = total
                    }
                }
            }
            for (i in 0..k) {
                dp[i] = newDp[i]
            }
        }
        return dp[k]
    }
}
```

## Dart

```dart
class Solution {
  int maxValueOfCoins(List<List<int>> piles, int k) {
    List<int> dp = List.filled(k + 1, 0);
    for (var pile in piles) {
      int m = pile.length;
      int limit = m < k ? m : k;
      // prefix sums: pref[t] = sum of first t coins
      List<int> pref = List.filled(limit + 1, 0);
      for (int i = 1; i <= limit; ++i) {
        pref[i] = pref[i - 1] + pile[i - 1];
      }
      List<int> next = List.from(dp);
      for (int taken = 0; taken <= k; ++taken) {
        int maxTake = limit;
        if (taken + maxTake > k) maxTake = k - taken;
        for (int t = 1; t <= maxTake; ++t) {
          int candidate = dp[taken] + pref[t];
          if (candidate > next[taken + t]) {
            next[taken + t] = candidate;
          }
        }
      }
      dp = next;
    }
    return dp[k];
  }
}
```

## Golang

```go
func maxValueOfCoins(piles [][]int, k int) int {
	const negInf = -1 << 60
	dp := make([]int, k+1)
	for i := 1; i <= k; i++ {
		dp[i] = negInf
	}
	dp[0] = 0

	for _, pile := range piles {
		m := len(pile)
		prefix := make([]int, m+1)
		for i := 1; i <= m; i++ {
			prefix[i] = prefix[i-1] + pile[i-1]
		}
		newDP := make([]int, k+1)
		copy(newDP, dp) // taking 0 coins from this pile
		for taken := 0; taken <= k; taken++ {
			if dp[taken] == negInf {
				continue
			}
			maxTake := m
			if k-taken < maxTake {
				maxTake = k - taken
			}
			for t := 1; t <= maxTake; t++ {
				val := dp[taken] + prefix[t]
				if val > newDP[taken+t] {
					newDP[taken+t] = val
				}
			}
		}
		dp = newDP
	}
	return dp[k]
}
```

## Ruby

```ruby
def max_value_of_coins(piles, k)
  dp = Array.new(k + 1, 0)

  piles.each do |pile|
    limit = [pile.length, k].min
    pref = Array.new(limit + 1, 0)
    (1..limit).each { |i| pref[i] = pref[i - 1] + pile[i - 1] }

    new_dp = dp.clone
    (0..k).each do |j|
      max_take = [limit, j].min
      1.upto(max_take) do |t|
        val = dp[j - t] + pref[t]
        new_dp[j] = val if val > new_dp[j]
      end
    end
    dp = new_dp
  end

  dp[k]
end
```

## Scala

```scala
object Solution {
    def maxValueOfCoins(piles: List[List[Int]], k: Int): Int = {
        val NEG_INF = Int.MinValue / 2
        var dp = Array.fill(k + 1)(NEG_INF)
        dp(0) = 0

        for (pile <- piles) {
            val limit = math.min(pile.length, k)
            val pref = new Array[Int](limit + 1)
            var sum = 0
            var i = 1
            while (i <= limit) {
                sum += pile(i - 1)
                pref(i) = sum
                i += 1
            }

            val ndp = Array.fill(k + 1)(NEG_INF)

            var used = 0
            while (used <= k) {
                if (dp(used) != NEG_INF) {
                    var take = 0
                    while (take <= limit && used + take <= k) {
                        val cand = dp(used) + pref(take)
                        if (cand > ndp(used + take)) ndp(used + take) = cand
                        take += 1
                    }
                }
                used += 1
            }

            dp = ndp
        }

        dp(k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_value_of_coins(piles: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        const NEG_INF: i64 = i64::MIN / 4;
        let mut dp = vec![NEG_INF; k + 1];
        dp[0] = 0;

        for pile in piles.iter() {
            let limit = std::cmp::min(pile.len(), k);
            // prefix sums of taking first x coins from this pile
            let mut pref = vec![0i64; limit + 1];
            for i in 0..limit {
                pref[i + 1] = pref[i] + pile[i] as i64;
            }

            let mut new_dp = vec![NEG_INF; k + 1];
            for used in 0..=k {
                // try taking x coins from current pile
                let max_take = std::cmp::min(limit, used);
                let mut best = NEG_INF;
                for x in 0..=max_take {
                    let candidate = dp[used - x] + pref[x];
                    if candidate > best {
                        best = candidate;
                    }
                }
                new_dp[used] = best;
            }
            dp = new_dp;
        }

        dp[k] as i32
    }
}
```

## Racket

```racket
(define/contract (max-value-of-coins piles k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((neg-inf -1000000000)
         (dp (make-vector (+ k 1) neg-inf)))
    (vector-set! dp 0 0)
    (for ([pile piles])
      (let* ((len (length pile))
             (max-take (min len k))
             (pref (make-vector (+ max-take 1) 0)))
        ;; compute prefix sums for this pile
        (let loop ((i 1) (sum 0))
          (when (<= i max-take)
            (set! sum (+ sum (list-ref pile (- i 1))))
            (vector-set! pref i sum)
            (loop (+ i 1) sum)))
        (let ((newdp (make-vector (+ k 1) neg-inf)))
          (for ([j (in-range 0 (+ k 1))])
            (let ((cur (vector-ref dp j)))
              (when (> cur neg-inf)
                ;; try taking x coins from this pile
                (let loop2 ((x 0))
                  (when (<= x max-take)
                    (define newj (+ j x))
                    (when (<= newj k)
                      (define val (+ cur (vector-ref pref x)))
                      (when (> val (vector-ref newdp newj))
                        (vector-set! newdp newj val)))
                    (loop2 (+ x 1)))))))
          (set! dp newdp))))
    (vector-ref dp k)))
```

## Erlang

```erlang
-spec max_value_of_coins(Piles :: [[integer()]], K :: integer()) -> integer().
max_value_of_coins(Piles, K) ->
    NegInf = -1000000000,
    DP0 = lists:duplicate(K + 1, NegInf),
    [_ | Rest] = DP0,
    DPInit = [0 | Rest],
    FinalDP = lists:foldl(
        fun(Pile, DPPrev) ->
            Pref = prefix_sums(Pile),
            Len = length(Pref) - 1,
            NewDP = [max_take(J, DPPrev, Pref, Len, NegInf) || J <- lists:seq(0, K)],
            NewDP
        end,
        DPInit,
        Piles
    ),
    get_nth(FinalDP, K).

prefix_sums(Pile) ->
    prefix_sums(Pile, [0]).

prefix_sums([], Acc) -> lists:reverse(Acc);
prefix_sums([H | T], [Prev | _] = Acc) ->
    New = Prev + H,
    prefix_sums(T, [New | Acc]).

max_take(J, DPPrev, Pref, Len, NegInf) ->
    MaxT = erlang:min(Len, J),
    max_take_loop(0, MaxT, J, DPPrev, Pref, NegInf).

max_take_loop(T, MaxT, _J, _DPPrev, _Pref, CurMax) when T > MaxT ->
    CurMax;
max_take_loop(T, MaxT, J, DPPrev, Pref, CurMax) ->
    PrevVal = get_nth(DPPrev, J - T),
    Sum = PrevVal + get_nth(Pref, T),
    NewMax = erlang:max(CurMax, Sum),
    max_take_loop(T + 1, MaxT, J, DPPrev, Pref, NewMax).

get_nth(List, Index) ->
    lists:nth(Index + 1, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_value_of_coins(piles :: [[integer]], k :: integer) :: integer
  def max_value_of_coins(piles, k) do
    neg_inf = -1_000_000_000

    init_dp =
      List.duplicate(neg_inf, k + 1)
      |> List.replace_at(0, 0)
      |> List.to_tuple()

    final_dp =
      Enum.reduce(piles, init_dp, fn pile, dp ->
        pref = prefix_sums(pile, k)
        max_take = length(pref) - 1

        new_vals =
          for t <- 0..k do
            limit = min(max_take, t)

            Enum.reduce(0..limit, neg_inf, fn j, acc ->
              prev = elem(dp, (t - j) + 1)
              cand = prev + Enum.at(pref, j)
              if cand > acc, do: cand, else: acc
            end)
          end

        List.to_tuple(new_vals)
      end)

    elem(final_dp, k + 1)
  end

  defp prefix_sums(pile, k) do
    max = min(length(pile), k)

    Enum.reduce(1..max, [0], fn i, acc ->
      sum = hd(acc) + Enum.at(pile, i - 1)
      [sum | acc]
    end)
    |> Enum.reverse()
  end
end
```
