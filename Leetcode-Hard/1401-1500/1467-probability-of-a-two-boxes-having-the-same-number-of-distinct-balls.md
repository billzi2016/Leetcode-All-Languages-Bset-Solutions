# 1467. Probability of a Two Boxes Having The Same Number of Distinct Balls

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double getProbability(vector<int>& balls) {
        int k = balls.size();
        int total = 0;
        for (int c : balls) total += c;
        int n = total / 2; // balls per box
        
        // precompute small combinations C(cnt, x) where cnt <=6
        unsigned long long combSmall[7][7] = {};
        for (int i = 0; i <= 6; ++i) {
            combSmall[i][0] = combSmall[i][i] = 1;
            for (int j = 1; j < i; ++j)
                combSmall[i][j] = combSmall[i-1][j-1] + combSmall[i-1][j];
        }
        
        int offset = k; // diff range [-k, k]
        vector<vector<long double>> dp(n+1, vector<long double>(2*k+1, 0.0L));
        dp[0][offset] = 1.0L;
        
        for (int cnt : balls) {
            vector<vector<long double>> ndp(n+1, vector<long double>(2*k+1, 0.0L));
            for (int used = 0; used <= n; ++used) {
                for (int d = -k; d <= k; ++d) {
                    long double cur = dp[used][d + offset];
                    if (cur == 0.0L) continue;
                    for (int x = 0; x <= cnt; ++x) { // balls of this color to box1
                        int nused = used + x;
                        if (nused > n) break;
                        int ndiff = d;
                        if (x == cnt) ndiff += 1;          // all to box1
                        else if (x == 0) ndiff -= 1;       // all to box2
                        // else split, diff unchanged
                        ndp[nused][ndiff + offset] += cur * (long double)combSmall[cnt][x];
                    }
                }
            }
            dp.swap(ndp);
        }
        
        long double favorable = dp[n][offset]; // diff == 0
        
        // compute total ways C(total, n)
        long double totalWays = 1.0L;
        for (int i = 1; i <= n; ++i) {
            totalWays *= (total - n + i);
            totalWays /= i;
        }
        
        return (double)(favorable / totalWays);
    }
};
```

## Java

```java
class Solution {
    public double getProbability(int[] balls) {
        int k = balls.length;
        int total = 0;
        for (int b : balls) total += b;
        int n = total / 2;

        // precompute combinations up to total
        long[][] comb = new long[total + 1][total + 1];
        for (int i = 0; i <= total; i++) {
            comb[i][0] = comb[i][i] = 1L;
            for (int j = 1; j < i; j++) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            }
        }

        int offset = k; // diff range [-k, k]
        int size = 2 * k + 1;
        long[][] dp = new long[n + 1][size];
        dp[0][offset] = 1L;

        for (int idx = 0; idx < k; idx++) {
            int cnt = balls[idx];
            long[][] ndp = new long[n + 1][size];
            for (int sel = 0; sel <= n; sel++) {
                for (int d = 0; d < size; d++) {
                    long cur = dp[sel][d];
                    if (cur == 0) continue;
                    for (int take = 0; take <= cnt; take++) {
                        int nSel = sel + take;
                        if (nSel > n) break;
                        int diffChange = (take > 0 ? 1 : 0) - (take < cnt ? 1 : 0);
                        int nd = d + diffChange;
                        if (nd < 0 || nd >= size) continue;
                        ndp[nSel][nd] += cur * comb[cnt][take];
                    }
                }
            }
            dp = ndp;
        }

        long favorable = dp[n][offset];
        double probability = (double) favorable / (double) comb[total][n];
        return probability;
    }
}
```

## Python

```python
class Solution(object):
    def getProbability(self, balls):
        """
        :type balls: List[int]
        :rtype: float
        """
        from math import comb

        k = len(balls)
        total = sum(balls)
        n = total // 2  # balls per box

        offset = k  # to shift diff index to non‑negative
        size_diff = 2 * k + 1

        dp = [[0] * size_diff for _ in range(n + 1)]
        dp[0][offset] = 1  # no balls selected, zero diff

        for cnt in balls:
            ndp = [[0] * size_diff for _ in range(n + 1)]
            for sel in range(n + 1):
                row = dp[sel]
                for d_idx in range(size_diff):
                    cur = row[d_idx]
                    if cur == 0:
                        continue
                    for x in range(cnt + 1):          # balls of this colour to box1
                        new_sel = sel + x
                        if new_sel > n:
                            continue
                        d1 = 1 if x > 0 else 0               # distinct in box1?
                        d2 = 1 if cnt - x > 0 else 0         # distinct in box2?
                        nd_idx = d_idx + (d1 - d2)
                        if 0 <= nd_idx < size_diff:
                            ndp[new_sel][nd_idx] += cur * comb(cnt, x)
            dp = ndp

        favorable = dp[n][offset]
        total_ways = comb(total, n)

        return favorable / total_ways
```

## Python3

```python
import math
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        total = sum(balls)
        n = total // 2
        k = len(balls)
        offset = k  # to shift delta range [-k, k] to [0, 2k]
        dp = [[0] * (2 * k + 1) for _ in range(n + 1)]
        dp[0][offset] = 1

        for c in balls:
            ndp = [[0] * (2 * k + 1) for _ in range(n + 1)]
            for s in range(n + 1):
                row = dp[s]
                for d_idx, val in enumerate(row):
                    if not val:
                        continue
                    for x in range(c + 1):
                        ns = s + x
                        if ns > n:
                            break
                        comb = math.comb(c, x)
                        if x == 0:
                            delta = -1
                        elif x == c:
                            delta = 1
                        else:
                            delta = 0
                        nd = d_idx + delta
                        if 0 <= nd < 2 * k + 1:
                            ndp[ns][nd] += val * comb
            dp = ndp

        favorable = dp[n][offset]
        denominator = math.comb(total, n)
        return favorable / denominator
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static long double combCache[55][55];
static bool combInit = false;

static void initComb(int N) {
    for (int i = 0; i <= N; ++i) {
        combCache[i][0] = combCache[i][i] = 1.0L;
        for (int j = 1; j < i; ++j)
            combCache[i][j] = combCache[i-1][j-1] + combCache[i-1][j];
    }
    combInit = true;
}

static long double C(int n, int k) {
    if (!combInit) initComb(50);
    return combCache[n][k];
}

double getProbability(int* balls, int ballsSize) {
    vector<int> b(balls, balls + ballsSize);
    int total = 0;
    for (int v : b) total += v;
    int half = total / 2;

    // total ways to choose half balls
    long double totalWays = C(total, half);

    long double favorable = 0.0L;
    function<void(int,int,int,int,long double)> dfs = [&](int idx, int selected,
                                                          int distinct1, int distinct2,
                                                          long double ways) {
        if (idx == ballsSize) {
            if (selected == half && distinct1 == distinct2)
                favorable += ways;
            return;
        }
        int cnt = b[idx];
        for (int x = 0; x <= cnt; ++x) { // x taken to box1
            int newSel = selected + x;
            if (newSel > half) continue;
            int d1 = distinct1 + (x > 0);
            int d2 = distinct2 + ((cnt - x) > 0);
            long double w = ways * C(cnt, x);
            dfs(idx + 1, newSel, d1, d2, w);
        }
    };

    dfs(0, 0, 0, 0, 1.0L);

    double ans = (double)(favorable / totalWays);
    return ans;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public double GetProbability(int[] balls) {
        int k = balls.Length;
        int total = 0;
        foreach (int b in balls) total += b;
        int n = total / 2;

        // precompute combinations up to 6 (max balls[i]) using double
        double[,] combSmall = new double[7, 7];
        for (int i = 0; i <= 6; i++) {
            combSmall[i, 0] = combSmall[i, i] = 1.0;
            for (int j = 1; j < i; j++) {
                combSmall[i, j] = combSmall[i - 1, j - 1] + combSmall[i - 1, j];
            }
        }

        // factorials up to total for denominator
        double[] fact = new double[total + 1];
        fact[0] = 1.0;
        for (int i = 1; i <= total; i++) fact[i] = fact[i - 1] * i;

        double Denominator = fact[total] / (fact[n] * fact[total - n]);

        // dp[s, d1, d2]
        double[,,] dp = new double[n + 1, k + 1, k + 1];
        dp[0, 0, 0] = 1.0;

        foreach (int cnt in balls) {
            double[,,] next = new double[n + 1, k + 1, k + 1];
            for (int s = 0; s <= n; s++) {
                for (int d1 = 0; d1 <= k; d1++) {
                    for (int d2 = 0; d2 <= k; d2++) {
                        double cur = dp[s, d1, d2];
                        if (cur == 0.0) continue;
                        for (int x = 0; x <= cnt; x++) {
                            int ns = s + x;
                            if (ns > n) break;
                            int nd1 = d1 + (x > 0 ? 1 : 0);
                            int nd2 = d2 + ((cnt - x) > 0 ? 1 : 0);
                            double ways = combSmall[cnt, x];
                            next[ns, nd1, nd2] += cur * ways;
                        }
                    }
                }
            }
            dp = next;
        }

        double numerator = 0.0;
        for (int c = 0; c <= k; c++) {
            numerator += dp[n, c, c];
        }

        return numerator / Denominator;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} balls
 * @return {number}
 */
var getProbability = function(balls) {
    const k = balls.length;
    const total = balls.reduce((a, b) => a + b, 0);
    const n = total >> 1; // total / 2
    
    // factorials for combinations
    const fact = new Float64Array(total + 1);
    fact[0] = 1;
    for (let i = 1; i <= total; ++i) {
        fact[i] = fact[i - 1] * i;
    }
    const comb = (a, b) => {
        if (b < 0 || b > a) return 0;
        return fact[a] / (fact[b] * fact[a - b]);
    };
    
    const diffSize = 2 * k + 1; // possible diff range [-k, k]
    const offset = k;
    
    let dp = Array.from({ length: n + 1 }, () => new Float64Array(diffSize));
    dp[0][offset] = 1; // no balls taken, zero difference
    
    for (let idx = 0; idx < k; ++idx) {
        const c = balls[idx];
        let next = Array.from({ length: n + 1 }, () => new Float64Array(diffSize));
        for (let taken = 0; taken <= n; ++taken) {
            const curRow = dp[taken];
            if (!curRow) continue;
            for (let dIdx = 0; dIdx < diffSize; ++dIdx) {
                const curWays = curRow[dIdx];
                if (curWays === 0) continue;
                for (let x = 0; x <= c; ++x) { // balls of this color to box1
                    const ntaken = taken + x;
                    if (ntaken > n) continue;
                    const delta = (x > 0 ? 1 : 0) - ((c - x) > 0 ? 1 : 0);
                    const ndIdx = dIdx + delta;
                    // ndIdx stays within [0, diffSize)
                    next[ntaken][ndIdx] += curWays * comb(c, x);
                }
            }
        }
        dp = next;
    }
    
    const numerator = dp[n][offset];
    const denominator = comb(total, n);
    return numerator / denominator;
};
```

## Typescript

```typescript
function getProbability(balls: number[]): number {
    const total = balls.reduce((a, b) => a + b, 0);
    const n = total >> 1;
    const k = balls.length;

    // precompute combinations up to total
    const C: number[][] = Array.from({ length: total + 1 }, () => Array(total + 1).fill(0));
    for (let i = 0; i <= total; i++) {
        C[i][0] = C[i][i] = 1;
        for (let j = 1; j < i; j++) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }

    const offset = k; // diff range [-k, k]
    let dp: number[][] = Array.from({ length: n + 1 }, () => Array(2 * k + 1).fill(0));
    dp[0][offset] = 1;

    for (const cnt of balls) {
        const ndp: number[][] = Array.from({ length: n + 1 }, () => Array(2 * k + 1).fill(0));
        for (let s = 0; s <= n; s++) {
            for (let diff = -k; diff <= k; diff++) {
                const cur = dp[s][diff + offset];
                if (cur === 0) continue;
                for (let x = 0; x <= cnt; x++) {
                    const ns = s + x;
                    if (ns > n) continue;
                    let ndiff = diff;
                    if (x === 0) ndiff -= 1;
                    else if (x === cnt) ndiff += 1;
                    ndp[ns][ndiff + offset] += cur * C[cnt][x];
                }
            }
        }
        dp = ndp;
    }

    const numerator = dp[n][offset];
    const denominator = C[total][n];
    return numerator / denominator;
}
```

## Php

```php
class Solution {
    private $balls;
    private $k;
    private $n;
    private $C;
    private $suffix;

    /**
     * @param Integer[] $balls
     * @return Float
     */
    function getProbability($balls) {
        $this->balls = $balls;
        $this->k = count($balls);
        $total = array_sum($balls);
        $this->n = intdiv($total, 2);

        // precompute binomial coefficients up to total
        $max = $total;
        $C = array_fill(0, $max + 1, []);
        for ($i = 0; $i <= $max; $i++) {
            $C[$i][0] = 1.0;
            $C[$i][$i] = 1.0;
        }
        for ($i = 2; $i <= $max; $i++) {
            for ($j = 1; $j < $i; $j++) {
                $C[$i][$j] = $C[$i - 1][$j - 1] + $C[$i - 1][$j];
            }
        }
        $this->C = $C;

        // suffix sums for pruning
        $suffix = array_fill(0, $this->k + 1, 0);
        for ($i = $this->k - 1; $i >= 0; $i--) {
            $suffix[$i] = $suffix[$i + 1] + $balls[$i];
        }
        $this->suffix = $suffix;

        $denom = $C[$total][$this->n];
        $numerator = $this->dfs(0, 0, 0, 0, 1.0);
        return $numerator / $denom;
    }

    private function dfs($idx, $selected, $d1, $d2, $ways) {
        if ($idx == $this->k) {
            if ($selected == $this->n && $d1 == $d2) {
                return $ways;
            }
            return 0.0;
        }

        $cnt = $this->balls[$idx];
        $totalWays = 0.0;

        for ($x = 0; $x <= $cnt; $x++) {
            if ($selected + $x > $this->n) continue;
            // check if we can still reach n with remaining colors
            $maxPossible = $selected + $x + $this->suffix[$idx + 1];
            if ($maxPossible < $this->n) continue;

            $newWays = $ways * $this->C[$cnt][$x];
            $newD1 = $d1 + ($x > 0 ? 1 : 0);
            $newD2 = $d2 + (($cnt - $x) > 0 ? 1 : 0);
            $totalWays += $this->dfs($idx + 1, $selected + $x, $newD1, $newD2, $newWays);
        }

        return $totalWays;
    }
}
```

## Swift

```swift
class Solution {
    func getProbability(_ balls: [Int]) -> Double {
        let k = balls.count
        let total = balls.reduce(0, +)
        let half = total / 2
        
        // factorials for combinations
        var fact = [Double](repeating: 1.0, count: total + 1)
        if total > 0 {
            for i in 1...total {
                fact[i] = fact[i - 1] * Double(i)
            }
        }
        func comb(_ n: Int, _ r: Int) -> Double {
            if r < 0 || r > n { return 0.0 }
            return fact[n] / (fact[r] * fact[n - r])
        }
        
        let offset = k                     // to shift negative diffs to non‑negative indices
        var dp = Array(repeating: Array(repeating: 0.0, count: 2 * k + 1), count: half + 1)
        dp[0][offset] = 1.0                // no balls taken, diff = 0
        
        for cnt in balls {
            var ndp = Array(repeating: Array(repeating: 0.0, count: 2 * k + 1), count: half + 1)
            for s in 0...half {
                for dIdx in 0..<(2 * k + 1) {
                    let cur = dp[s][dIdx]
                    if cur == 0 { continue }
                    for x in 0...cnt {
                        let ns = s + x
                        if ns > half { continue }
                        var delta = 0
                        if x > 0 { delta += 1 }               // color appears in first box
                        if cnt - x > 0 { delta -= 1 }          // color appears in second box
                        let nd = (dIdx - offset) + delta
                        let ndIdx = nd + offset
                        if ndIdx < 0 || ndIdx >= 2 * k + 1 { continue }
                        ndp[ns][ndIdx] += cur * comb(cnt, x)
                    }
                }
            }
            dp = ndp
        }
        
        let favorable = dp[half][offset]
        let totalWays = comb(total, half)
        return favorable / totalWays
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getProbability(balls: IntArray): Double {
        val k = balls.size
        val totalBalls = balls.sum()
        val n = totalBalls / 2

        // Precompute combinations up to totalBalls
        val comb = Array(totalBalls + 1) { LongArray(totalBalls + 1) }
        for (i in 0..totalBalls) {
            comb[i][0] = 1L
            comb[i][i] = 1L
            for (j in 1 until i) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
            }
        }

        val totalWays = comb[totalBalls][n].toDouble()
        var favorable = 0.0

        fun dfs(idx: Int, selected: Int, distinctA: Int, distinctB: Int, prod: Double) {
            if (idx == k) {
                if (selected == n && distinctA == distinctB) {
                    favorable += prod
                }
                return
            }
            val cnt = balls[idx]
            for (x in 0..cnt) {
                val newSelected = selected + x
                if (newSelected > n) continue
                val dA = distinctA + if (x > 0) 1 else 0
                val remain = cnt - x
                val dB = distinctB + if (remain > 0) 1 else 0
                val newProd = prod * comb[cnt][x].toDouble()
                dfs(idx + 1, newSelected, dA, dB, newProd)
            }
        }

        dfs(0, 0, 0, 0, 1.0)

        return favorable / totalWays
    }
}
```

## Dart

```dart
class Solution {
  double getProbability(List<int> balls) {
    int total = balls.reduce((a, b) => a + b);
    int n = total ~/ 2;
    int k = balls.length;
    int offset = k; // to shift negative diff indices

    // factorials up to total
    List<int> fact = List.filled(total + 1, 1);
    for (int i = 1; i <= total; ++i) {
      fact[i] = fact[i - 1] * i;
    }

    int comb(int N, int R) {
      if (R < 0 || R > N) return 0;
      return fact[N] ~/ (fact[R] * fact[N - R]);
    }

    // dp[selected][diff+offset] = ways
    List<List<int>> dp = List.generate(
        n + 1, (_) => List.filled(2 * k + 1, 0));
    dp[0][offset] = 1;

    for (int c in balls) {
      List<List<int>> ndp = List.generate(
          n + 1, (_) => List.filled(2 * k + 1, 0));
      for (int sel = 0; sel <= n; ++sel) {
        for (int dIdx = 0; dIdx < 2 * k + 1; ++dIdx) {
          int curWays = dp[sel][dIdx];
          if (curWays == 0) continue;
          for (int x = 0; x <= c; ++x) {
            int newSel = sel + x;
            if (newSel > n) continue;
            int deltaDiff;
            if (x == 0) {
              deltaDiff = -1; // only box2 gets this colour
            } else if (x == c) {
              deltaDiff = 1; // only box1 gets this colour
            } else {
              deltaDiff = 0; // both boxes get the colour
            }
            int newDIdx = dIdx + deltaDiff;
            ndp[newSel][newDIdx] += curWays * comb(c, x);
          }
        }
      }
      dp = ndp;
    }

    int numerator = dp[n][offset];
    int denominator = comb(total, n);
    return numerator.toDouble() / denominator.toDouble();
  }
}
```

## Golang

```go
func getProbability(balls []int) float64 {
    total := 0
    for _, c := range balls {
        total += c
    }
    n := total / 2

    // precompute combinations up to total
    comb := make([][]float64, total+1)
    for i := 0; i <= total; i++ {
        comb[i] = make([]float64, i+1)
        comb[i][0] = 1.0
        comb[i][i] = 1.0
        for j := 1; j < i; j++ {
            comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
        }
    }

    k := len(balls)
    offset := k // diff range [-k, k]
    dp := make([][]float64, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([]float64, 2*k+1)
    }
    dp[0][offset] = 1.0

    for _, c := range balls {
        ndp := make([][]float64, n+1)
        for i := 0; i <= n; i++ {
            ndp[i] = make([]float64, 2*k+1)
        }
        for taken := 0; taken <= n; taken++ {
            for diffIdx := 0; diffIdx < 2*k+1; diffIdx++ {
                val := dp[taken][diffIdx]
                if val == 0 {
                    continue
                }
                for x := 0; x <= c; x++ {
                    nt := taken + x
                    if nt > n {
                        break
                    }
                    delta := 0
                    if x > 0 {
                        delta++
                    }
                    if x < c {
                        delta--
                    }
                    ndiffIdx := diffIdx + delta
                    if ndiffIdx < 0 || ndiffIdx >= 2*k+1 {
                        continue
                    }
                    ndp[nt][ndiffIdx] += val * comb[c][x]
                }
            }
        }
        dp = ndp
    }

    favorable := dp[n][offset]
    totalWays := comb[total][n]

    return favorable / totalWays
}
```

## Ruby

```ruby
def get_probability(balls)
  total = balls.sum
  n = total / 2
  k = balls.length

  # precompute combinations up to total
  comb = Array.new(total + 1) { Array.new(total + 1, 0.0) }
  (0..total).each do |i|
    comb[i][0] = comb[i][i] = 1.0
    (1...i).each do |j|
      comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
    end
  end

  # dp[chosen balls][distinct in box1][distinct in box2] = ways
  dp = Array.new(n + 1) { Array.new(k + 1) { Array.new(k + 1, 0.0) } }
  dp[0][0][0] = 1.0

  balls.each do |c|
    newdp = Array.new(n + 1) { Array.new(k + 1) { Array.new(k + 1, 0.0) } }
    (0..n).each do |chosen|
      (0..k).each do |d1|
        (0..k).each do |d2|
          cur = dp[chosen][d1][d2]
          next if cur == 0.0
          (0..c).each do |x|
            nxt_chosen = chosen + x
            next if nxt_chosen > n
            nd1 = d1 + (x > 0 ? 1 : 0)
            nd2 = d2 + ((c - x) > 0 ? 1 : 0)
            newdp[nxt_chosen][nd1][nd2] += cur * comb[c][x]
          end
        end
      end
    end
    dp = newdp
  end

  favorable = 0.0
  (0..k).each do |d|
    favorable += dp[n][d][d]
  end

  total_ways = comb[total][n]
  favorable / total_ways
end
```

## Scala

```scala
object Solution {
    def getProbability(balls: Array[Int]): Double = {
        val k = balls.length
        val totalBalls = balls.sum
        val n = totalBalls / 2

        // factorials as double
        val fact = new Array[Double](totalBalls + 1)
        fact(0) = 1.0
        for (i <- 1 to totalBalls) {
            fact(i) = fact(i - 1) * i
        }
        def comb(a: Int, b: Int): Double = {
            if (b < 0 || b > a) 0.0 else fact(a) / (fact(b) * fact(a - b))
        }

        // precompute combinations for each colour count
        val combCache = Array.ofDim[Double](k, 7) // balls[i] <= 6
        for (i <- 0 until k) {
            val c = balls(i)
            for (x <- 0 to c) {
                combCache(i)(x) = comb(c, x)
            }
        }

        var favorable: Double = 0.0

        def dfs(idx: Int, remaining: Int, distinct1: Int, distinct2: Int, prod: Double): Unit = {
            if (idx == k) {
                if (remaining == 0 && distinct1 == distinct2) {
                    favorable += prod
                }
                return
            }
            val c = balls(idx)
            for (x <- 0 to c) {
                if (x <= remaining) {
                    val newRem = remaining - x
                    val nd1 = distinct1 + (if (x > 0) 1 else 0)
                    val nd2 = distinct2 + (if ((c - x) > 0) 1 else 0)
                    dfs(idx + 1, newRem, nd1, nd2, prod * combCache(idx)(x))
                }
            }
        }

        dfs(0, n, 0, 0, 1.0)

        val totalWays = comb(totalBalls, n)
        favorable / totalWays
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_probability(balls: Vec<i32>) -> f64 {
        let k = balls.len() as i32;
        let total: usize = balls.iter().map(|&x| x as usize).sum();
        let n = total / 2;

        fn comb(n: i32, k: i32) -> f64 {
            if k < 0 || k > n {
                return 0.0;
            }
            let mut k = k;
            if k > n - k {
                k = n - k;
            }
            let mut res = 1.0_f64;
            for i in 1..=k {
                res *= (n - k + i) as f64 / i as f64;
            }
            res
        }

        let offset = k as usize;
        let diff_size = (2 * k + 1) as usize;
        let mut dp = vec![vec![0.0_f64; diff_size]; n + 1];
        dp[0][offset] = 1.0;

        for &c_i in balls.iter() {
            let c = c_i as usize;
            let mut ndp = vec![vec![0.0_f64; diff_size]; n + 1];
            for sel in 0..=n {
                for d_idx in 0..diff_size {
                    let cur = dp[sel][d_idx];
                    if cur == 0.0 {
                        continue;
                    }
                    for xi in 0..=c {
                        let new_sel = sel + xi;
                        if new_sel > n {
                            continue;
                        }
                        let ways = comb(c_i, xi as i32);
                        let delta = (if xi > 0 { 1 } else { 0 }) - (if c - xi > 0 { 1 } else { 0 });
                        let nd_idx = d_idx as i32 + delta;
                        if nd_idx < 0 || nd_idx >= diff_size as i32 {
                            continue;
                        }
                        ndp[new_sel][nd_idx as usize] += cur * ways;
                    }
                }
            }
            dp = ndp;
        }

        let numerator = dp[n][offset];
        let denominator = comb(total as i32, n as i32);
        numerator / denominator
    }
}
```

## Racket

```racket
(define/contract (get-probability balls)
  (-> (listof exact-integer?) flonum?)
  (let* ((sum-balls (apply + balls))          ; total number of balls = 2n
         (n (/ sum-balls 2))
         (max-n sum-balls)
         ;; factorials up to max-n
         (fact (let ((v (make-vector (+ max-n 1) 1)))
                 (for ([i (in-range 1 (add1 max-n))])
                   (vector-set! v i (* (vector-ref v (- i 1)) i)))
                 v))
         ;; binomial coefficient as exact integer
         (binom (lambda (nn kk)
                  (if (or (< kk 0) (> kk nn))
                      0
                      (/ (vector-ref fact nn)
                         (* (vector-ref fact kk)
                            (vector-ref fact (- nn kk)))))))
         (denominator (binom sum-balls n))
         ;; DP: map from (list total diff) -> ways (exact integer)
         (dp (let ((h (make-hash)))
               (hash-set! h (list 0 0) 1)
               h)))
    (for ([m balls])
      (let ((next (make-hash)))
        (hash-for-each dp
                       (lambda (key val)
                         (define total-so-far (first key))
                         (define diff-so-far (second key))
                         (for ([x (in-range 0 (add1 m))])
                           (define new-total (+ total-so-far x))
                           (when (<= new-total n)          ; we only need totals up to n
                             (define ways (* val (binom m x)))   ; exact integer
                             (define diff-change
                               (cond [(= x 0) -1]
                                     [(= x m) 1]
                                     [else 0]))
                             (define new-diff (+ diff-so-far diff-change))
                             (define existing (hash-ref next (list new-total new-diff) 0))
                             (hash-set! next (list new-total new-diff) (+ existing ways))))))
        (set! dp next)))
    (define numerator (hash-ref dp (list n 0) 0))
    (/ (exact->inexact numerator) (exact->inexact denominator))))
```

## Erlang

```erlang
-module(solution).
-export([get_probability/1]).

-spec get_probability(Balls :: [integer()]) -> float().
get_probability(Balls) ->
    Total = lists:sum(Balls),
    N = Total div 2,
    FactMap = precompute_factorials(Total),
    Favorable = dfs(Balls, N, 0, 0, 0, 1, FactMap),
    TotalWays = binom(Total, N, FactMap),
    Favorable / TotalWays.

%% Depth‑first search over possible allocations to the first box
-spec dfs([integer()], integer(), integer(), integer(), integer(), integer(), map()) -> integer().
dfs([], N, SumX, Dist1, Dist2, Ways, _FactMap) ->
    if SumX =:= N andalso Dist1 =:= Dist2 -> Ways;
       true -> 0
    end;
dfs([Count|Rest], N, SumX, Dist1, Dist2, Ways, FactMap) ->
    MaxTake = erlang:min(Count, N - SumX),
    lists:foldl(
        fun(Take, Acc) ->
            NewSum   = SumX + Take,
            NewDist1 = if Take > 0 -> Dist1 + 1; true -> Dist1 end,
            Rem      = Count - Take,
            NewDist2 = if Rem > 0 -> Dist2 + 1; true -> Dist2 end,
            Comb     = binom(Count, Take, FactMap),
            Acc + dfs(Rest, N, NewSum, NewDist1, NewDist2, Ways * Comb, FactMap)
        end,
        0,
        lists:seq(0, MaxTake)
    ).

%% Binomial coefficient using pre‑computed factorials
-spec binom(N :: integer(), K :: integer(), map()) -> integer().
binom(N, K, _FactMap) when K < 0; K > N ->
    0;
binom(N, K, FactMap) ->
    FactN  = maps:get(N, FactMap),
    FactK  = maps:get(K, FactMap),
    FactNK = maps:get(N - K, FactMap),
    FactN div (FactK * FactNK).

%% Pre‑compute factorials up to Max
-spec precompute_factorials(Max :: integer()) -> map().
precompute_factorials(Max) ->
    lists:foldl(
        fun(I, Acc) ->
            Prev = maps:get(I - 1, Acc),
            maps:put(I, Prev * I, Acc)
        end,
        #{0 => 1},
        lists:seq(1, Max)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_probability(balls :: [integer]) :: float
  def get_probability(balls) do
    total = Enum.sum(balls)
    n = div(total, 2)

    fact = build_fact_map(total)

    comb = fn a, b ->
      if b < 0 or b > a do
        0
      else
        div(Map.get(fact, a), Map.get(fact, b) * Map.get(fact, a - b))
      end
    end

    combos =
      Enum.map(balls, fn cnt ->
        Enum.map(0..cnt, fn xi -> comb.(cnt, xi) end)
      end)

    dp_initial = %{{0, 0, 0} => 1}

    dp_final =
      Enum.reduce(Enum.with_index(balls), dp_initial, fn {cnt, idx}, acc_dp ->
        combo_row = Enum.at(combos, idx)

        Enum.reduce(acc_dp, %{}, fn {{rem, d1, d2}, val}, ndp ->
          Enum.reduce(0..cnt, ndp, fn xi, ndp2 ->
            nrem = rem + xi
            nd1 = d1 + if xi > 0, do: 1, else: 0
            nd2 = d2 + if cnt - xi > 0, do: 1, else: 0
            add_val = val * Enum.at(combo_row, xi)
            key = {nrem, nd1, nd2}
            Map.update(ndp2, key, add_val, &(&1 + add_val))
          end)
        end)
      end)

    favorable =
      dp_final
      |> Enum.filter(fn {{rem, d1, d2}, _} -> rem == n and d1 == d2 end)
      |> Enum.reduce(0, fn {_, v}, acc -> acc + v end)

    total_comb = comb.(total, n)
    favorable / total_comb
  end

  defp build_fact_map(max) do
    Enum.reduce(0..max, %{0 => 1}, fn i, acc ->
      if i == 0 do
        acc
      else
        Map.put(acc, i, Map.get(acc, i - 1) * i)
      end
    end)
  end
end
```
