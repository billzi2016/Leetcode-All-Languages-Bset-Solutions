# 0879. Profitable Schemes

## Cpp

```cpp
class Solution {
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        const int MOD = 1'000'000'007;
        int m = group.size();
        vector<vector<int>> dp(n + 1, vector<int>(minProfit + 1, 0));
        dp[0][0] = 1;
        for (int idx = 0; idx < m; ++idx) {
            int g = group[idx];
            int p = profit[idx];
            for (int members = n; members >= g; --members) {
                for (int prof = minProfit; prof >= 0; --prof) {
                    int newProf = prof + p;
                    if (newProf > minProfit) newProf = minProfit;
                    dp[members][newProf] = (dp[members][newProf] + dp[members - g][prof]) % MOD;
                }
            }
        }
        long long ans = 0;
        for (int members = 0; members <= n; ++members) {
            ans += dp[members][minProfit];
        }
        return ans % MOD;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int m = group.length;
        int[][] dp = new int[n + 1][minProfit + 1];
        dp[0][0] = 1; // empty scheme
        
        for (int i = 0; i < m; ++i) {
            int membersNeeded = group[i];
            int profitGain = profit[i];
            for (int g = n; g >= membersNeeded; --g) {
                for (int p = minProfit; p >= 0; --p) {
                    int newP = Math.min(p + profitGain, minProfit);
                    dp[g][newP] = (dp[g][newP] + dp[g - membersNeeded][p]) % MOD;
                }
            }
        }
        
        int ans = 0;
        for (int g = 0; g <= n; ++g) {
            ans = (ans + dp[g][minProfit]) % MOD;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        # dp[m][p] = number of ways using m members to achieve at least p profit (capped)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            # iterate members and profit backwards to avoid reuse within same iteration
            for m in range(n, g - 1, -1):
                prev = dp[m - g]
                cur = dp[m]
                for prof in range(minProfit, -1, -1):
                    new_prof = min(minProfit, prof + p)
                    cur[new_prof] = (cur[new_prof] + prev[prof]) % MOD

        ans = sum(dp[m][minProfit] for m in range(n + 1)) % MOD
        return ans
```

## Python3

```python
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for need, earn in zip(group, profit):
            for g in range(n, need - 1, -1):
                prev = dp[g - need]
                cur = dp[g]
                for p in range(minProfit, -1, -1):
                    np = p + earn
                    if np > minProfit:
                        np = minProfit
                    cur[np] = (cur[np] + prev[p]) % MOD
        return sum(dp[g][minProfit] for g in range(n + 1)) % MOD
```

## C

```c
int profitableSchemes(int n, int minProfit, int* group, int groupSize, int* profit, int profitSize) {
    const int MOD = 1000000007;
    static int dp[101][101];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int idx = 0; idx < groupSize; ++idx) {
        int g = group[idx];
        int p = profit[idx];
        for (int i = n; i >= g; --i) {
            for (int j = minProfit; j >= 0; --j) {
                int newProf = j + p;
                if (newProf > minProfit) newProf = minProfit;
                dp[i][newProf] += dp[i - g][j];
                if (dp[i][newProf] >= MOD) dp[i][newProf] -= MOD;
            }
        }
    }
    long long ans = 0;
    for (int i = 0; i <= n; ++i) {
        ans += dp[i][minProfit];
        if (ans >= MOD) ans -= MOD;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int ProfitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int m = group.Length;
        int[,] dp = new int[n + 1, minProfit + 1];
        dp[0, 0] = 1;

        for (int idx = 0; idx < m; idx++) {
            int g = group[idx];
            int p = profit[idx];
            for (int i = n; i >= g; i--) {
                for (int j = minProfit; j >= 0; j--) {
                    int newProf = j + p;
                    if (newProf > minProfit) newProf = minProfit;
                    long val = dp[i, newProf] + dp[i - g, j];
                    if (val >= MOD) val -= MOD;
                    dp[i, newProf] = (int)val;
                }
            }
        }

        int result = 0;
        for (int i = 0; i <= n; i++) {
            result += dp[i, minProfit];
            if (result >= MOD) result -= MOD;
        }
        return result;
    }
}
```

## Javascript

```javascript
var profitableSchemes = function(n, minProfit, group, profit) {
    const MOD = 1000000007;
    const m = minProfit;
    const dp = Array.from({length: n + 1}, () => new Uint32Array(m + 1));
    dp[0][0] = 1;
    for (let idx = 0; idx < group.length; ++idx) {
        const g = group[idx];
        const p = profit[idx];
        for (let i = n; i >= g; --i) {
            const prev = dp[i - g];
            const cur = dp[i];
            for (let prof = 0; prof <= m; ++prof) {
                const ways = prev[prof];
                if (!ways) continue;
                const newProf = Math.min(m, prof + p);
                let val = cur[newProf] + ways;
                if (val >= MOD) val -= MOD;
                cur[newProf] = val;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i <= n; ++i) {
        ans += dp[i][m];
        if (ans >= MOD) ans -= MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function profitableSchemes(n: number, minProfit: number, group: number[], profit: number[]): number {
    const MOD = 1_000_000_007;
    const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(minProfit + 1).fill(0));
    dp[0][0] = 1;

    for (let i = 0; i < group.length; ++i) {
        const g = group[i];
        const p = profit[i];
        for (let members = n; members >= g; --members) {
            for (let prof = minProfit; prof >= 0; --prof) {
                const ways = dp[members - g][prof];
                if (ways === 0) continue;
                const newProf = Math.min(minProfit, prof + p);
                dp[members][newProf] = (dp[members][newProf] + ways) % MOD;
            }
        }
    }

    let ans = 0;
    for (let members = 0; members <= n; ++members) {
        ans = (ans + dp[members][minProfit]) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $minProfit
     * @param Integer[] $group
     * @param Integer[] $profit
     * @return Integer
     */
    function profitableSchemes($n, $minProfit, $group, $profit) {
        $MOD = 1000000007;
        // dp[i][j] = number of schemes using i members achieving profit j (capped at minProfit)
        $dp = array_fill(0, $n + 1, array_fill(0, $minProfit + 1, 0));
        $dp[0][0] = 1;

        $m = count($group);
        for ($idx = 0; $idx < $m; $idx++) {
            $g = $group[$idx];
            $p = $profit[$idx];
            // iterate members descending to avoid reuse within same crime
            for ($i = $n; $i >= $g; $i--) {
                // profit dimension can be iterated descending as well
                for ($j = $minProfit; $j >= 0; $j--) {
                    if ($dp[$i - $g][$j] == 0) continue;
                    $newProf = $j + $p;
                    if ($newProf > $minProfit) $newProf = $minProfit;
                    $dp[$i][$newProf] = ($dp[$i][$newProf] + $dp[$i - $g][$j]) % $MOD;
                }
            }
        }

        $ans = 0;
        for ($i = 0; $i <= $n; $i++) {
            $ans = ($ans + $dp[$i][$minProfit]) % $MOD;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func profitableSchemes(_ n: Int, _ minProfit: Int, _ group: [Int], _ profit: [Int]) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: minProfit + 1), count: n + 1)
        dp[0][0] = 1
        
        for idx in 0..<group.count {
            let g = group[idx]
            let p = profit[idx]
            if g > n { continue }
            for i in stride(from: n, through: g, by: -1) {
                for j in stride(from: minProfit, through: 0, by: -1) {
                    let newProf = min(minProfit, j + p)
                    dp[i][newProf] += dp[i - g][j]
                    if dp[i][newProf] >= MOD { dp[i][newProf] -= MOD }
                }
            }
        }
        
        var result = 0
        for i in 0...n {
            result += dp[i][minProfit]
            if result >= MOD { result -= MOD }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    fun profitableSchemes(n: Int, minProfit: Int, group: IntArray, profit: IntArray): Int {
        val dp = Array(n + 1) { LongArray(minProfit + 1) }
        dp[0][0] = 1L
        for (i in group.indices) {
            val g = group[i]
            val p = profit[i]
            for (members in n downTo g) {
                for (prof in minProfit downTo 0) {
                    val newProf = if (prof + p >= minProfit) minProfit else prof + p
                    dp[members][newProf] = (dp[members][newProf] + dp[members - g][prof]) % MOD
                }
            }
        }
        var ans = 0L
        for (members in 0..n) {
            ans = (ans + dp[members][minProfit]) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int profitableSchemes(int n, int minProfit, List<int> group, List<int> profit) {
    // dp[people][profit] = number of ways
    List<List<int>> dp = List.generate(
        n + 1, (_) => List.filled(minProfit + 1, 0),
        growable: false);
    dp[0][0] = 1;

    for (int idx = 0; idx < group.length; ++idx) {
      int g = group[idx];
      int p = profit[idx];
      // iterate people in reverse to avoid reuse within same crime
      for (int i = n; i >= g; --i) {
        for (int j = 0; j <= minProfit; ++j) {
          if (dp[i - g][j] == 0) continue;
          int newProf = j + p;
          if (newProf > minProfit) newProf = minProfit;
          dp[i][newProf] = (dp[i][newProf] + dp[i - g][j]) % _mod;
        }
      }
    }

    int ans = 0;
    for (int i = 0; i <= n; ++i) {
      ans = (ans + dp[i][minProfit]) % _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func profitableSchemes(n int, minProfit int, group []int, profit []int) int {
	const MOD = 1000000007
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, minProfit+1)
	}
	dp[0][0] = 1

	for idx := 0; idx < len(group); idx++ {
		g := group[idx]
		p := profit[idx]
		for m := n; m >= g; m-- {
			for prof := minProfit; prof >= 0; prof-- {
				if dp[m-g][prof] == 0 {
					continue
				}
				newProf := prof + p
				if newProf > minProfit {
					newProf = minProfit
				}
				dp[m][newProf] = (dp[m][newProf] + dp[m-g][prof]) % MOD
			}
		}
	}

	ans := 0
	for m := 0; m <= n; m++ {
		ans = (ans + dp[m][minProfit]) % MOD
	}
	return ans
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def profitable_schemes(n, min_profit, group, profit)
  dp = Array.new(n + 1) { Array.new(min_profit + 1, 0) }
  dp[0][0] = 1

  group.each_with_index do |g_needed, idx|
    p_gain = profit[idx]
    n.downto(g_needed) do |g|
      min_profit.downto(0) do |p|
        ways = dp[g - g_needed][p]
        next if ways == 0
        new_p = p + p_gain
        new_p = min_profit if new_p > min_profit
        dp[g][new_p] = (dp[g][new_p] + ways) % MOD
      end
    end
  end

  ans = 0
  (0..n).each { |g| ans = (ans + dp[g][min_profit]) % MOD }
  ans
end
```

## Scala

```scala
object Solution {
  def profitableSchemes(n: Int, minProfit: Int, group: Array[Int], profit: Array[Int]): Int = {
    val MOD = 1000000007
    val dp = Array.ofDim[Int](n + 1, minProfit + 1)
    dp(0)(0) = 1
    for (idx <- group.indices) {
      val g = group(idx)
      val p = profit(idx)
      var i = n
      while (i >= g) {
        var j = minProfit
        while (j >= 0) {
          if (dp(i - g)(j) != 0) {
            val newProf = math.min(minProfit, j + p)
            dp(i)(newProf) = (dp(i)(newProf) + dp(i - g)(j)) % MOD
          }
          j -= 1
        }
        i -= 1
      }
    }
    var ans = 0
    var i = 0
    while (i <= n) {
      ans = (ans + dp(i)(minProfit)) % MOD
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn profitable_schemes(n: i32, min_profit: i32, group: Vec<i32>, profit: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n_usize = n as usize;
        let min_p = min_profit as usize;
        let m = group.len();
        // dp[people][profit] = ways
        let mut dp = vec![vec![0i64; min_p + 1]; n_usize + 1];
        dp[0][0] = 1;
        for i in 0..m {
            let g = group[i] as usize;
            let p = profit[i] as usize;
            if g > n_usize {
                continue;
            }
            for people in (g..=n_usize).rev() {
                for prof in (0..=min_p).rev() {
                    let ways = dp[people - g][prof];
                    if ways == 0 {
                        continue;
                    }
                    let new_prof = std::cmp::min(min_p, prof + p);
                    dp[people][new_prof] = (dp[people][new_prof] + ways) % MOD;
                }
            }
        }
        let mut ans: i64 = 0;
        for people in 0..=n_usize {
            ans = (ans + dp[people][min_p]) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(provide profitable-schemes)

(define MOD 1000000007)

(define/contract (profitable-schemes n minProfit group profit)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((m (length group))
         (dp (make-vector (+ n 1) #f)))
    ;; initialize dp rows
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ minProfit 1) 0)))
    ;; base case: zero members, zero profit
    (let ((row0 (vector-ref dp 0))) (vector-set! row0 0 1))
    ;; process each crime
    (for ([idx (in-range m)])
      (define g (list-ref group idx))
      (define p (list-ref profit idx))
      (when (<= g n)
        (for ([mem (in-range n (sub1 g) -1)]) ; descending members from n to g inclusive
          (let ((rowMem (vector-ref dp mem)))
            (for ([prof (in-range minProfit -1 -1)]) ; descending profit from minProfit to 0
              (define prevVal (vector-ref (vector-ref dp (- mem g)) prof))
              (when (> prevVal 0)
                (define newProf (+ prof p))
                (when (> newProf minProfit) (set! newProf minProfit))
                (define cur (vector-ref rowMem newProf))
                (vector-set! rowMem newProf (modulo (+ cur prevVal) MOD))))))))
    ;; sum up schemes achieving at least minProfit
    (let ((ans 0))
      (for ([mem (in-range (+ n 1))])
        (set! ans (modulo (+ ans (vector-ref (vector-ref dp mem) minProfit)) MOD)))
      ans)))
```

## Erlang

```erlang
-spec profitable_schemes(N :: integer(), MinProfit :: integer(), Group :: [integer()], Profit :: [integer()]) -> integer().
profitable_schemes(N, MinProfit, Group, Profit) ->
    Mod = 1000000007,
    DP0 = #{ {0,0} => 1 },
    DPFinal = lists:foldl(
        fun({G,P}, DPAcc) ->
            maps:fold(
                fun({I,J}, Cnt, DPMap) ->
                    I2 = I + G,
                    if I2 =< N ->
                        J2 = erlang:min(MinProfit, J + P),
                        Old = maps:get({I2,J2}, DPMap, 0),
                        NewVal = (Old + Cnt) rem Mod,
                        maps:put({I2,J2}, NewVal, DPMap);
                       true -> DPMap
                    end
                end,
                DPAcc,
                DPAcc)
        end,
        DP0,
        lists:zip(Group, Profit)),
    maps:fold(
        fun({_I,J}, Cnt, Acc) ->
            if J == MinProfit -> (Acc + Cnt) rem Mod;
               true -> Acc
            end
        end,
        0,
        DPFinal).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec profitable_schemes(n :: integer, min_profit :: integer, group :: [integer], profit :: [integer]) :: integer
  def profitable_schemes(n, min_profit, group, profit) do
    mod = 1_000_007
    initial_dp = %{{0, 0} => 1}

    dp =
      Enum.zip(group, profit)
      |> Enum.reduce(initial_dp, fn {g, p}, dp ->
        prev = dp

        Enum.reduce(prev, dp, fn {{mem, prof}, cnt}, acc ->
          new_mem = mem + g

          if new_mem <= n do
            new_prof = min(min_profit, prof + p)
            key = {new_mem, new_prof}
            new_val = (Map.get(acc, key, 0) + cnt) |> rem(mod)
            Map.put(acc, key, new_val)
          else
            acc
          end
        end)
      end)

    0..n
    |> Enum.reduce(0, fn mem, sum ->
      (sum + Map.get(dp, {mem, min_profit}, 0)) |> rem(mod)
    end)
  end
end
```
