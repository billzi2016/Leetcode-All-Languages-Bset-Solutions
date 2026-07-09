# 1900. The Earliest and Latest Rounds Where Players Compete

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int earliestRound(int n, int a, int b) {
        int round = 0;
        while (a != b) {
            ++round;
            a = (a + 1) / 2;
            b = (b + 1) / 2;
        }
        return round;
    }

    unordered_map<long long,int> memo;

    long long encode(int n, int a, int b) {
        return ((long long)n << 16) | (a << 8) | b;
    }

    int latestRound(int n, int a, int b) {
        if (a > b) swap(a, b);
        long long key = encode(n, a, b);
        auto it = memo.find(key);
        if (it != memo.end()) return it->second;

        // they meet this round
        if (a + b == n + 1) {
            memo[key] = 1;
            return 1;
        }

        // ensure a+b <= n+1 using symmetry
        if (a + b > n + 1) {
            int na = n + 1 - b;
            int nb = n + 1 - a;
            int res = latestRound(n, na, nb);
            memo[key] = res;
            return res;
        }

        int next_n = (n + 1) / 2;
        int best = 0;
        for (int i = 0; i <= a - 1; ++i) {
            for (int j = 0; j <= b - a - 1; ++j) {
                int nxt_a = i + 1;
                int nxt_b = i + j + 2;
                best = max(best, latestRound(next_n, nxt_a, nxt_b));
            }
        }
        memo[key] = best + 1;
        return best + 1;
    }

    vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        int early = earliestRound(n, firstPlayer, secondPlayer);
        int late = latestRound(n, firstPlayer, secondPlayer);
        return {early, late};
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class PairResult {
        int min, max;
        PairResult(int min, int max) { this.min = min; this.max = max; }
    }

    private final Map<Integer, PairResult> memo = new HashMap<>();

    public int[] earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        if (firstPlayer > secondPlayer) {
            int tmp = firstPlayer;
            firstPlayer = secondPlayer;
            secondPlayer = tmp;
        }
        PairResult res = dfs(n, firstPlayer, secondPlayer);
        return new int[]{res.min, res.max};
    }

    private PairResult dfs(int n, int a, int b) {
        // a < b guaranteed
        if (a + b == n + 1) {
            return new PairResult(1, 1);
        }
        int key = (n << 16) | (a << 8) | b;
        if (memo.containsKey(key)) return memo.get(key);

        int pairs = n / 2;
        int[] left = new int[pairs];
        int[] right = new int[pairs];
        for (int i = 0; i < pairs; i++) {
            left[i] = i + 1;
            right[i] = n - i;
        }
        boolean hasMiddle = (n % 2 == 1);
        int middle = hasMiddle ? (n + 1) / 2 : -1;

        int nextN = (n + 1) / 2; // number of survivors after this round

        int bestMin = Integer.MAX_VALUE;
        int bestMax = Integer.MIN_VALUE;

        int totalMasks = 1 << pairs;
        for (int mask = 0; mask < totalMasks; mask++) {
            boolean valid = true;
            List<Integer> survivors = new ArrayList<>(nextN);
            for (int i = 0; i < pairs; i++) {
                int l = left[i];
                int r = right[i];
                if (l == a || l == b) {
                    // must pick left side
                    if ((mask >> i & 1) != 0) { valid = false; break; }
                    survivors.add(l);
                } else if (r == a || r == b) {
                    // must pick right side
                    if ((mask >> i & 1) == 0) { valid = false; break; }
                    survivors.add(r);
                } else {
                    int win = ((mask >> i) & 1) == 0 ? l : r;
                    survivors.add(win);
                }
            }
            if (!valid) continue;

            if (hasMiddle) {
                // middle player always advances
                survivors.add(middle);
            }

            Collections.sort(survivors);
            int aPos = -1, bPos = -1;
            for (int i = 0; i < survivors.size(); i++) {
                int val = survivors.get(i);
                if (val == a) aPos = i + 1;
                else if (val == b) bPos = i + 1;
            }
            // both must be present
            PairResult sub = dfs(nextN, aPos, bPos);
            bestMin = Math.min(bestMin, 1 + sub.min);
            bestMax = Math.max(bestMax, 1 + sub.max);
        }

        PairResult ans = new PairResult(bestMin, bestMax);
        memo.put(key, ans);
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        from functools import lru_cache

        @lru_cache(None)
        def dp(cur_n, f, s):
            if f > s:
                f, s = s, f
            # meet this round
            if f + s == cur_n + 1:
                return (1, 1)

            # use symmetry to keep f on the left side
            if f + s > cur_n + 1:
                nf = cur_n + 1 - s
                ns = cur_n + 1 - f
                if nf > ns:
                    nf, ns = ns, nf
                return dp(cur_n, nf, ns)

            nxt_n = (cur_n + 1) // 2
            INF = 10 ** 9
            best_min = INF
            best_max = -INF

            # s is on the left side or middle
            if s <= (cur_n + 1) // 2:
                for i in range(f):                     # survivors before f
                    for j in range(s - f):             # survivors between f and s
                        e, l = dp(nxt_n, i + 1, i + j + 2)
                        if e < best_min:
                            best_min = e
                        if l > best_max:
                            best_max = l
            else:
                # s is on the right side
                sp = cur_n + 1 - s          # opponent of s
                if f > sp:
                    f, sp = sp, f
                offset = (cur_n - 2 * sp + 1) // 2
                for i in range(f):
                    for j in range(sp - f):
                        e, l = dp(nxt_n, i + 1, i + j + offset + 2)
                        if e < best_min:
                            best_min = e
                        if l > best_max:
                            best_max = l

            return (best_min + 1, best_max + 1)

        early, late = dp(n, firstPlayer, secondPlayer)
        return [early, late]
```

## Python3

```python
import sys
from functools import lru_cache
from typing import List

def _normalize(n: int, f: int, s: int):
    if f > s:
        f, s = s, f
    if f + s > n + 1:
        f, s = n + 1 - s, n + 1 - f
    return f, s

@lru_cache(None)
def _min_round(n: int, f: int, s: int) -> int:
    # f < s and f+s <= n+1 guaranteed
    if f + s == n + 1:
        return 1
    nxt_n = (n + 1) // 2
    best = sys.maxsize
    left_cnt = f - 1
    mid_cnt = s - f - 1
    for i in range(left_cnt + 1):
        for j in range(mid_cnt + 1):
            nf, ns = i + 1, i + j + 2
            nf, ns = _normalize(nxt_n, nf, ns)
            cur = _min_round(nxt_n, nf, ns) + 1
            if cur < best:
                best = cur
    return best

@lru_cache(None)
def _max_round(n: int, f: int, s: int) -> int:
    # f < s and f+s <= n+1 guaranteed
    if f + s == n + 1:
        return 1
    nxt_n = (n + 1) // 2
    worst = -1
    left_cnt = f - 1
    mid_cnt = s - f - 1
    for i in range(left_cnt + 1):
        for j in range(mid_cnt + 1):
            nf, ns = i + 1, i + j + 2
            nf, ns = _normalize(nxt_n, nf, ns)
            cur = _max_round(nxt_n, nf, ns) + 1
            if cur > worst:
                worst = cur
    return worst

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        f, s = _normalize(n, firstPlayer, secondPlayer)
        early = _min_round(n, f, s)
        late = _max_round(n, f, s)
        return [early, late]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int memoMin[29][29][29];
static int memoMax[29][29][29];

static int earliestRec(int n, int f, int s) {
    if (f > s) { int t = f; f = s; s = t; }
    int *mem = &memoMin[n][f][s];
    if (*mem != -1) return *mem;

    if (f + s > n + 1) {
        int nf = n + 1 - s;
        int ns = n + 1 - f;
        *mem = earliestRec(n, nf, ns);
        return *mem;
    }
    if (s == n + 1 - f) {
        *mem = 1;
        return 1;
    }

    int nextN = (n + 1) / 2;
    int best = INT_MAX;
    for (int i = 0; i <= f - 1; ++i) {
        for (int j = 0; j <= s - f - 1; ++j) {
            int nfPos = i + 1;
            int nsPos = i + j + 2;
            int cand = earliestRec(nextN, nfPos, nsPos);
            if (cand < best) best = cand;
        }
    }
    *mem = best + 1;
    return *mem;
}

static int latestRec(int n, int f, int s) {
    if (f > s) { int t = f; f = s; s = t; }
    int *mem = &memoMax[n][f][s];
    if (*mem != -1) return *mem;

    if (f + s > n + 1) {
        int nf = n + 1 - s;
        int ns = n + 1 - f;
        *mem = latestRec(n, nf, ns);
        return *mem;
    }
    if (s == n + 1 - f) {
        *mem = 1;
        return 1;
    }

    int nextN = (n + 1) / 2;
    int best = 0;
    for (int i = 0; i <= f - 1; ++i) {
        for (int j = 0; j <= s - f - 1; ++j) {
            int nfPos = i + 1;
            int nsPos = i + j + 2;
            int cand = latestRec(nextN, nfPos, nsPos);
            if (cand > best) best = cand;
        }
    }
    *mem = best + 1;
    return *mem;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* earliestAndLatest(int n, int firstPlayer, int secondPlayer, int* returnSize){
    memset(memoMin, -1, sizeof(memoMin));
    memset(memoMax, -1, sizeof(memoMax));

    int f = firstPlayer;
    int s = secondPlayer;
    if (f > s) { int t = f; f = s; s = t; }

    int early = earliestRec(n, f, s);
    int late  = latestRec(n, f, s);

    int *ans = (int*)malloc(2 * sizeof(int));
    ans[0] = early;
    ans[1] = late;
    *returnSize = 2;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] EarliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        var memo = new Dictionary<(int, int, int), (int min, int max)>();

        (int min, int max) Dfs(int curN, int f, int s) {
            if (f > s) { var tmp = f; f = s; s = tmp; }

            // Base case: they meet this round
            if (f + s == curN + 1) return (1, 1);

            // Reflect if they are on the right side
            if (f + s > curN + 1) {
                int nf = curN + 1 - s;
                int ns = curN + 1 - f;
                if (nf > ns) { var tmp = nf; nf = ns; ns = tmp; }
                return Dfs(curN, nf, ns);
            }

            var key = (curN, f, s);
            if (memo.TryGetValue(key, out var cached)) return cached;

            int nextN = (curN + 1) / 2;
            int bestMin = int.MaxValue;
            int bestMax = 0;

            for (int i = 0; i <= f - 1; i++) {
                for (int j = 0; j <= s - f - 1; j++) {
                    var sub = Dfs(nextN, i + 1, i + j + 2);
                    bestMin = Math.Min(bestMin, sub.min + 1);
                    bestMax = Math.Max(bestMax, sub.max + 1);
                }
            }

            var result = (bestMin, bestMax);
            memo[key] = result;
            return result;
        }

        var ans = Dfs(n, firstPlayer, secondPlayer);
        return new int[] { ans.min, ans.max };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} firstPlayer
 * @param {number} secondPlayer
 * @return {number[]}
 */
var earliestAndLatest = function(n, firstPlayer, secondPlayer) {
    if (firstPlayer > secondPlayer) [firstPlayer, secondPlayer] = [secondPlayer, firstPlayer];
    const memo = new Map();

    function dfs(curN, f, s) {
        // ensure f < s
        if (f > s) [f, s] = [s, f];
        const key = curN + "#" + f + "#" + s;
        if (memo.has(key)) return memo.get(key);

        let ans;
        // they meet this round
        if (f + s === curN + 1) {
            ans = [1, 1];
        } else if (f + s > curN + 1) {
            // reflect positions
            const nf = curN + 1 - s;
            const ns = curN + 1 - f;
            ans = dfs(curN, nf, ns);
        } else {
            const nextN = Math.floor((curN + 1) / 2);
            let minRound = Infinity;
            let maxRound = -Infinity;
            for (let i = 0; i <= f - 1; ++i) {
                for (let j = 0; j <= s - f - 1; ++j) {
                    const [subMin, subMax] = dfs(nextN, i + 1, i + j + 2);
                    if (subMin + 1 < minRound) minRound = subMin + 1;
                    if (subMax + 1 > maxRound) maxRound = subMax + 1;
                }
            }
            ans = [minRound, maxRound];
        }

        memo.set(key, ans);
        return ans;
    }

    return dfs(n, firstPlayer, secondPlayer);
};
```

## Typescript

```typescript
function earliestAndLatest(n: number, firstPlayer: number, secondPlayer: number): number[] {
    const memo = new Map<string, [number, number]>();

    function dfs(curN: number, f: number, s: number): [number, number] {
        if (f > s) {
            const tmp = f;
            f = s;
            s = tmp;
        }
        const key = `${curN},${f},${s}`;
        const cached = memo.get(key);
        if (cached) return cached;

        // they meet this round
        if (f + s === curN + 1) {
            memo.set(key, [1, 1]);
            return [1, 1];
        }

        // flip when both are on the right side
        if (f + s > curN + 1) {
            const nf = curN + 1 - s;
            const ns = curN + 1 - f;
            const res = dfs(curN, nf, ns);
            memo.set(key, res);
            return res;
        }

        const half = Math.floor((curN + 1) / 2);
        let minRound = Infinity;
        let maxRound = -Infinity;

        if (s <= half) {
            // both on the left side (or middle)
            for (let i = 0; i <= f - 1; ++i) {
                for (let j = 0; j <= s - f - 1; ++j) {
                    const [subMin, subMax] = dfs(half, i + 1, i + j + 2);
                    if (subMin + 1 < minRound) minRound = subMin + 1;
                    if (subMax + 1 > maxRound) maxRound = subMax + 1;
                }
            }
        } else {
            // s is on the right side
            const sOpp = curN + 1 - s; // opponent of s on the left
            const gap = Math.floor((curN - 2 * sOpp + 1) / 2);
            for (let i = 0; i <= f - 1; ++i) {
                for (let j = 0; j <= sOpp - f - 1; ++j) {
                    const [subMin, subMax] = dfs(half, i + 1, i + j + gap + 2);
                    if (subMin + 1 < minRound) minRound = subMin + 1;
                    if (subMax + 1 > maxRound) maxRound = subMax + 1;
                }
            }
        }

        const result: [number, number] = [minRound, maxRound];
        memo.set(key, result);
        return result;
    }

    return dfs(n, firstPlayer, secondPlayer);
}
```

## Php

```php
class Solution {
    private $memo = [];

    /**
     * @param Integer $n
     * @param Integer $firstPlayer
     * @param Integer $secondPlayer
     * @return Integer[]
     */
    function earliestAndLatest($n, $firstPlayer, $secondPlayer) {
        if ($firstPlayer > $secondPlayer) {
            $tmp = $firstPlayer;
            $firstPlayer = $secondPlayer;
            $secondPlayer = $tmp;
        }
        [$minRound, $maxRound] = $this->dfs($n, $firstPlayer, $secondPlayer);
        return [$minRound, $maxRound];
    }

    private function dfs($n, $a, $b) {
        if ($a > $b) {
            $tmp = $a;
            $a = $b;
            $b = $tmp;
        }
        $key = "$n,$a,$b";
        if (isset($this->memo[$key])) {
            return $this->memo[$key];
        }

        // They meet this round
        if ($a + $b == $n + 1) {
            $this->memo[$key] = [1, 1];
            return $this->memo[$key];
        }

        // Reflect to keep them on the left side
        if ($a + $b > $n + 1) {
            $na = $n + 1 - $b;
            $nb = $n + 1 - $a;
            $res = $this->dfs($n, $na, $nb);
            $this->memo[$key] = $res;
            return $res;
        }

        $nextN = intdiv($n + 1, 2);
        $minRounds = PHP_INT_MAX;
        $maxRounds = 0;

        for ($i = 0; $i <= $a - 1; $i++) {
            for ($j = 0; $j <= $b - $a - 1; $j++) {
                $na = $i + 1;
                $nb = $i + $j + 2;
                [$cmin, $cmax] = $this->dfs($nextN, $na, $nb);
                $minRounds = min($minRounds, $cmin + 1);
                $maxRounds = max($maxRounds, $cmax + 1);
            }
        }

        $this->memo[$key] = [$minRounds, $maxRounds];
        return $this->memo[$key];
    }
}
```

## Swift

```swift
class Solution {
    struct Key: Hashable {
        let n: Int
        let f: Int
        let s: Int
    }
    
    var memoEarliest = [Key: Int]()
    var memoLatest = [Key: Int]()
    
    private func earliest(_ n: Int, _ f: Int, _ s: Int) -> Int {
        if f + s == n + 1 { return 1 }
        let key = Key(n: n, f: f, s: s)
        if let v = memoEarliest[key] { return v }
        var ans = Int.max
        if f + s > n + 1 {
            // symmetry transformation
            let nf = n + 1 - s
            let ns = n + 1 - f
            ans = earliest(n, nf, ns)
        } else {
            let nextN = (n + 1) / 2
            for i in 0..<f {                 // keep i players from left segment
                for j in 0..<(s - f) {       // keep j players from middle segment
                    let nfPos = i + 1
                    let nsPos = i + j + 2
                    let cand = earliest(nextN, nfPos, nsPos) + 1
                    if cand < ans { ans = cand }
                }
            }
        }
        memoEarliest[key] = ans
        return ans
    }
    
    private func latest(_ n: Int, _ f: Int, _ s: Int) -> Int {
        if f + s == n + 1 { return 1 }
        let key = Key(n: n, f: f, s: s)
        if let v = memoLatest[key] { return v }
        var ans = Int.min
        if f + s > n + 1 {
            // symmetry transformation
            let nf = n + 1 - s
            let ns = n + 1 - f
            ans = latest(n, nf, ns)
        } else {
            let nextN = (n + 1) / 2
            for i in 0..<f {
                for j in 0..<(s - f) {
                    let nfPos = i + 1
                    let nsPos = i + j + 2
                    let cand = latest(nextN, nfPos, nsPos) + 1
                    if cand > ans { ans = cand }
                }
            }
        }
        memoLatest[key] = ans
        return ans
    }
    
    func earliestAndLatest(_ n: Int, _ firstPlayer: Int, _ secondPlayer: Int) -> [Int] {
        var a = firstPlayer
        var b = secondPlayer
        if a > b { swap(&a, &b) }
        let e = earliest(n, a, b)
        let l = latest(n, a, b)
        return [e, l]
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap

class Solution {
    private val memo = HashMap<Triple<Int, Int, Int>, Int>()

    fun earliestAndLatest(n: Int, firstPlayer: Int, secondPlayer: Int): IntArray {
        val earliest = computeEarliest(n, firstPlayer, secondPlayer)
        val latest = computeLatest(n, firstPlayer, secondPlayer)
        return intArrayOf(earliest, latest)
    }

    private fun computeEarliest(n: Int, f0: Int, s0: Int): Int {
        if (f0 + s0 == n + 1) return 1
        var f = f0
        var s = s0
        var rounds = 0
        while (f != s) {
            f = (f + 1) / 2
            s = (s + 1) / 2
            rounds++
        }
        return rounds + 1
    }

    private fun computeLatest(n: Int, f0: Int, s0: Int): Int {
        var f = f0
        var s = s0
        if (f > s) {
            val tmp = f; f = s; s = tmp
        }
        return latestRec(n, f, s)
    }

    private fun latestRec(n: Int, f0: Int, s0: Int): Int {
        var f = f0
        var s = s0
        if (f > s) {
            val tmp = f; f = s; s = tmp
        }
        val key = Triple(n, f, s)
        memo[key]?.let { return it }

        // direct meeting this round
        if (f + s == n + 1) {
            memo[key] = 1
            return 1
        }

        var result: Int

        // If they are on opposite sides beyond the middle, mirror them
        if (f + s > n + 1) {
            val nf = n + 1 - s
            val ns = n + 1 - f
            result = latestRec(n, nf, ns)
        } else {
            val nextN = (n + 1) / 2
            var best = 0
            if (s <= nextN) { // both on the left side (including middle)
                val maxI = f - 1
                val maxJ = if (s - f - 1 >= 0) s - f - 1 else 0
                for (i in 0..maxI) {
                    for (j in 0..maxJ) {
                        val nfPos = i + 1
                        val nsPos = i + j + 2
                        val cur = latestRec(nextN, nfPos, nsPos)
                        if (cur > best) best = cur
                    }
                }
            } else { // s on the right side
                val sp = n + 1 - s          // mirror of s, now on left
                val mid = (n - 2 * sp + 1) / 2   // survivors between sp and s after this round
                val maxI = f - 1
                val maxJ = if (sp - f - 1 >= 0) sp - f - 1 else 0
                for (i in 0..maxI) {
                    for (j in 0..maxJ) {
                        val nfPos = i + 1
                        val nsPos = i + j + mid + 2
                        val cur = latestRec(nextN, nfPos, nsPos)
                        if (cur > best) best = cur
                    }
                }
            }
            result = best + 1
        }

        memo[key] = result
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
    final Map<String, int> memoMin = {};
    final Map<String, int> memoMax = {};

    int dfs(int curN, int f, int s, bool isMin) {
      if (f > s) {
        int tmp = f;
        f = s;
        s = tmp;
      }
      String key = '$curN,$f,$s';
      final memo = isMin ? memoMin : memoMax;
      if (memo.containsKey(key)) return memo[key]!;

      // They meet this round
      if (f + s == curN + 1) {
        memo[key] = 1;
        return 1;
      }

      // Mirror when they are on the right side of each other
      if (f + s > curN + 1) {
        int nf = curN + 1 - s;
        int ns = curN + 1 - f;
        int res = dfs(curN, nf, ns, isMin);
        memo[key] = res;
        return res;
      }

      int nextN = (curN + 1) ~/ 2;
      int best = isMin ? 1 << 30 : 0;

      // s on the left side or middle
      if (s <= (curN + 1) ~/ 2) {
        for (int i = 0; i <= f - 1; ++i) {
          for (int j = 0; j <= s - f - 1; ++j) {
            int res = dfs(nextN, i + 1, i + j + 2, isMin);
            if (isMin) {
              if (res < best) best = res;
            } else {
              if (res > best) best = res;
            }
          }
        }
      } else {
        // s on the right side
        int sPrime = curN + 1 - s; // counterpart on left
        int extra = (curN - 2 * sPrime + 1) ~/ 2;
        for (int i = 0; i <= f - 1; ++i) {
          for (int j = 0; j <= sPrime - f - 1; ++j) {
            int res = dfs(nextN, i + 1, i + j + extra + 2, isMin);
            if (isMin) {
              if (res < best) best = res;
            } else {
              if (res > best) best = res;
            }
          }
        }
      }

      int ans = best + 1;
      memo[key] = ans;
      return ans;
    }

    int earliest = dfs(n, firstPlayer, secondPlayer, true);
    int latest = dfs(n, firstPlayer, secondPlayer, false);
    return [earliest, latest];
  }
}
```

## Golang

```go
package main

func earliestAndLatest(n int, firstPlayer int, secondPlayer int) []int {
	type key struct{ n, f, s int }
	memo := make(map[key][2]int)

	var dfs func(int, int, int) (int, int)
	dfs = func(nn, ff, ss int) (int, int) {
		if ff > ss {
			ff, ss = ss, ff
		}
		// direct match this round
		if ff+ss == nn+1 {
			return 1, 1
		}
		// transform when they are on opposite sides
		if ff+ss > nn+1 {
			nf := nn + 1 - ss
			ns := nn + 1 - ff
			return dfs(nn, nf, ns)
		}
		k := key{nn, ff, ss}
		if v, ok := memo[k]; ok {
			return v[0], v[1]
		}
		nextN := (nn + 1) / 2

		minRound := int(^uint(0) >> 1) // max int
		maxRound := 0

		for i := 0; i <= ff-1; i++ {
			for j := 0; j <= ss-ff-1; j++ {
				nf := i + 1
				ns := i + j + 2
				e, l := dfs(nextN, nf, ns)
				if e < minRound {
					minRound = e
				}
				if l > maxRound {
					maxRound = l
				}
			}
		}

		earliest := minRound + 1
		latest := maxRound + 1
		memo[k] = [2]int{earliest, latest}
		return earliest, latest
	}

	e, l := dfs(n, firstPlayer, secondPlayer)
	return []int{e, l}
}
```

## Ruby

```ruby
def earliest_and_latest(n, first_player, second_player)
  @memo = {}

  solve = lambda do |cur_n, f, s|
    if f > s
      f, s = s, f
    end

    if f + s > cur_n + 1
      nf = cur_n + 1 - s
      ns = cur_n + 1 - f
      f, s = nf, ns
      f, s = s, f if f > s
    end

    key = [cur_n, f, s]
    return @memo[key] if @memo.key?(key)

    # they meet this round
    if f + s == cur_n + 1
      @memo[key] = [1, 1]
      return @memo[key]
    end

    next_n = (cur_n + 1) / 2
    earliest = Float::INFINITY
    latest   = -Float::INFINITY

    if s <= (cur_n + 1) / 2
      max_left = f - 1
      between = s - f - 1
      (0..max_left).each do |i|
        (0..between).each do |j|
          sub = solve.call(next_n, i + 1, i + j + 2)
          earliest = [earliest, sub[0] + 1].min
          latest   = [latest,   sub[1] + 1].max
        end
      end
    else
      s_prime = cur_n + 1 - s
      max_left = f - 1
      between_prime = s_prime - f - 1
      rem_between = (cur_n - 2 * s_prime + 1) / 2
      (0..max_left).each do |i|
        (0..between_prime).each do |j|
          sub = solve.call(next_n, i + 1, i + j + rem_between + 2)
          earliest = [earliest, sub[0] + 1].min
          latest   = [latest,   sub[1] + 1].max
        end
      end
    end

    @memo[key] = [earliest, latest]
  end

  solve.call(n, first_player, second_player)
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  private val earlyMemo = mutable.Map[(Int, Int, Int), Int]()
  private val lateMemo = mutable.Map[(Int, Int, Int), Int]()

  private def normalize(n: Int, f0: Int, s0: Int): (Int, Int, Int) = {
    var f = f0
    var s = s0
    if (f > s) { val t = f; f = s; s = t }
    if (f + s > n + 1) {
      val nf = n + 1 - s
      val ns = n + 1 - f
      f = nf
      s = ns
    }
    (n, f, s)
  }

  private def earliest(n: Int, f0: Int, s0: Int): Int = {
    val (nn, f, s) = normalize(n, f0, s0)
    earlyMemo.getOrElseUpdate((nn, f, s), {
      if (f + s == nn + 1) 1
      else {
        var best = Int.MaxValue
        val nextN = (nn + 1) / 2
        for (i <- 0 to f - 1) {
          for (j <- 0 to (s - f - 1)) {
            val cand = earliest(nextN, i + 1, i + j + 2) + 1
            if (cand < best) best = cand
          }
        }
        best
      }
    })
  }

  private def latest(n: Int, f0: Int, s0: Int): Int = {
    val (nn, f, s) = normalize(n, f0, s0)
    lateMemo.getOrElseUpdate((nn, f, s), {
      if (f + s == nn + 1) 1
      else {
        var worst = 0
        val nextN = (nn + 1) / 2
        for (i <- 0 to f - 1) {
          for (j <- 0 to (s - f - 1)) {
            val cand = latest(nextN, i + 1, i + j + 2) + 1
            if (cand > worst) worst = cand
          }
        }
        worst
      }
    })
  }

  def earliestAndLatest(n: Int, firstPlayer: Int, secondPlayer: Int): Array[Int] = {
    val e = earliest(n, firstPlayer, secondPlayer)
    val l = latest(n, firstPlayer, secondPlayer)
    Array(e, l)
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn earliest_and_latest(n: i32, first_player: i32, second_player: i32) -> Vec<i32> {
        fn dfs(
            n: i32,
            f: i32,
            s: i32,
            memo: &mut HashMap<(i32, i32, i32), (i32, i32)>,
        ) -> (i32, i32) {
            // ensure f < s
            let (f, s) = if f < s { (f, s) } else { (s, f) };
            if let Some(&res) = memo.get(&(n, f, s)) {
                return res;
            }

            // they meet this round
            if f + s == n + 1 {
                memo.insert((n, f, s), (1, 1));
                return (1, 1);
            }

            // reflect if both are on the right side
            let (f, s) = if f + s > n + 1 {
                (n + 1 - s, n + 1 - f)
            } else {
                (f, s)
            };

            // after possible reflection, they must be on the left/middle side
            let m = (n + 1) / 2; // number of players in next round
            let mut min_round = i32::MAX;
            let mut max_round = i32::MIN;

            for i in 0..f {
                for j in 0..(s - f) {
                    let (e, l) = dfs(m, i + 1, i + j + 2, memo);
                    if e < min_round {
                        min_round = e;
                    }
                    if l > max_round {
                        max_round = l;
                    }
                }
            }

            let res = (min_round + 1, max_round + 1);
            memo.insert((n, f, s), res);
            res
        }

        let mut memo: HashMap<(i32, i32, i32), (i32, i32)> = HashMap::new();
        let (earliest, latest) = dfs(n, first_player, second_player, &mut memo);
        vec![earliest, latest]
    }
}
```

## Racket

```racket
(define memo (make-hash))

;; solve returns a cons where car = earliest round, cdr = latest round
(define (solve n f s)
  ;; ensure f <= s
  (if (> f s)
      (solve n s f)
      (let ((key (list n f s)))
        (cond
          [(hash-has-key? memo key) (hash-ref memo key)]
          [else
           (define result
             (cond
               ;; they meet this round
               [(= (+ f s) (add1 n)) (cons 1 1)]
               ;; use symmetry if they are on the right side
               [(> (+ f s) (add1 n))
                (let* ((nf (- (add1 n) s))
                       (ns (- (add1 n) f)))
                  (solve n nf ns))]
               [else
                (let* ((n' (quotient (+ n 1) 2))
                       (left-count (- f 1))
                       (mid-count (- s f 1))
                       (min-round 1000)
                       (max-round -1))
                  (for ([i (in-range 0 (add1 left-count))])
                    (for ([j (in-range 0 (add1 mid-count))])
                      (let* ((newf (+ i 1))
                             (news (+ i j 2))
                             (rec (solve n' newf news))
                             (ear (car rec))
                             (lat (cdr rec)))
                        (set! min-round (min min-round (+ ear 1)))
                        (set! max-round (max max-round (+ lat 1))))))
                  (cons min-round max-round)))])
           (hash-set! memo key result)
           result)]))))

(define/contract (earliest-and-latest n firstPlayer secondPlayer)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  (let* ((f (min firstPlayer secondPlayer))
         (s (max firstPlayer secondPlayer))
         (res (solve n f s)))
    (list (car res) (cdr res))))
```

## Erlang

```erlang
-spec earliest_and_latest(N :: integer(), FirstPlayer :: integer(), SecondPlayer :: integer()) -> [integer()].
earliest_and_latest(N, FirstPlayer, SecondPlayer) ->
    {Earliest, _Cache1} = min_round(N, FirstPlayer, SecondPlayer, #{}),
    {Latest,   _Cache2} = max_round(N, FirstPlayer, SecondPlayer, #{}),
    [Earliest, Latest].

%%------------------------------------------------------------
%% Minimum (earliest) round DP with memoization
%% Returns {Result, UpdatedCache}
%%------------------------------------------------------------
min_round(N, F, S, Cache) ->
    %% Ensure F <= S
    case F =< S of
        true -> ok;
        false -> min_round(N, S, F, Cache)
    end,
    Key = {N, F, S},
    case maps:find(Key, Cache) of
        {ok, Val} ->
            {Val, Cache};
        error ->
            Res =
                if
                    F + S == N + 1 ->
                        1;
                    F + S > N + 1 ->
                        NewF = N + 1 - S,
                        NewS = N + 1 - F,
                        {Tmp, C1} = min_round(N, NewF, NewS, Cache),
                        Tmp;
                    true ->
                        N2 = (N + 1) div 2,
                        %% iterate over possible survivors
                        MinInit = 1000,
                        {MinVal, FinalCache} =
                            iter_i(F - 1, F, S, N2, MinInit, Cache, fun min_iter/7),
                        MinVal
                end,
            UpdatedCache = maps:put(Key, Res, FinalCache),
            {Res, UpdatedCache}
    end.

%% Helper to iterate over i values
iter_i(-1, _F, _S, _N2, AccMin, Cache, _Fun) ->
    {AccMin, Cache};
iter_i(I, F, S, N2, AccMin, Cache, Fun) ->
    {NewAccMin, NewCache} = Fun(I, F, S, N2, AccMin, Cache),
    iter_i(I - 1, F, S, N2, NewAccMin, NewCache, Fun).

%% For each i, iterate over j and compute min
min_iter(I, F, S, N2, AccMin, Cache) ->
    MaxJ = S - F - 1,
    iter_j(MaxJ, I, F, S, N2, AccMin, Cache, fun(Ii, Jj, _F,_S,N2c,AccM,Cc) ->
        {R, CNew} = min_round(N2c, Ii + 1, Ii + Jj + 2, Cc),
        NewMin = if R < AccM -> R; true -> AccM end,
        {NewMin, CNew}
    end).

%% Helper to iterate over j values
iter_j(-1, _I, _F, _S, _N2, Acc, Cache, _Fun) ->
    {Acc, Cache};
iter_j(J, I, F, S, N2, Acc, Cache, Fun) ->
    {NewAcc, NewCache} = Fun(I, J, F, S, N2, Acc, Cache),
    iter_j(J - 1, I, F, S, N2, NewAcc, NewCache, Fun).

%%------------------------------------------------------------
%% Maximum (latest) round DP with memoization
%% Returns {Result, UpdatedCache}
%%------------------------------------------------------------
max_round(N, F, S, Cache) ->
    %% Ensure F <= S
    case F =< S of
        true -> ok;
        false -> max_round(N, S, F, Cache)
    end,
    Key = {N, F, S},
    case maps:find(Key, Cache) of
        {ok, Val} ->
            {Val, Cache};
        error ->
            Res =
                if
                    F + S == N + 1 ->
                        1;
                    F + S > N + 1 ->
                        NewF = N + 1 - S,
                        NewS = N + 1 - F,
                        {Tmp, C1} = max_round(N, NewF, NewS, Cache),
                        Tmp;
                    true ->
                        N2 = (N + 1) div 2,
                        MaxInit = 0,
                        {MaxVal, FinalCache} =
                            iter_i(F - 1, F, S, N2, MaxInit, Cache, fun max_iter/7),
                        MaxVal
                end,
            UpdatedCache = maps:put(Key, Res, FinalCache),
            {Res, UpdatedCache}
    end.

%% For each i, iterate over j and compute max
max_iter(I, F, S, N2, AccMax, Cache) ->
    MaxJ = S - F - 1,
    iter_j(MaxJ, I, F, S, N2, AccMax, Cache, fun(Ii, Jj, _F,_S,N2c,AccM,Cc) ->
        {R, CNew} = max_round(N2c, Ii + 1, Ii + Jj + 2, Cc),
        NewMax = if R > AccM -> R; true -> AccM end,
        {NewMax, CNew}
    end).
```

## Elixir

```elixir
defmodule Solution do
  @spec earliest_and_latest(n :: integer, first_player :: integer, second_player :: integer) :: [integer]
  def earliest_and_latest(n, first_player, second_player) do
    {f, s} = if first_player < second_player, do: {first_player, second_player}, else: {second_player, first_player}

    :ets.new(:earliest_cache, [:named_table, :public, read_concurrency: true])
    :ets.new(:latest_cache, [:named_table, :public, read_concurrency: true])

    earliest = compute_earliest(n, f, s)
    latest = compute_latest(n, f, s)

    :ets.delete(:earliest_cache)
    :ets.delete(:latest_cache)

    [earliest, latest]
  end

  # ---------- Earliest (minimum rounds) ----------
  defp compute_earliest(n, f, s) do
    case :ets.lookup(:earliest_cache, {n, f, s}) do
      [{_, val}] -> val
      [] ->
        res = cond do
          f + s == n + 1 ->
            1

          true ->
            next_n = div(n + 1, 2)

            if s <= div(n, 2) do
              # both on the left side (or middle case handled here)
              min_val = 1_000_000

              for i <- 0..(f - 1), reduce: min_val do
                acc_i ->
                  for j <- 0..(s - f - 1), reduce: acc_i do
                    acc_j ->
                      v = compute_earliest(next_n, i + 1, i + j + 2)
                      if v < acc_j, do: v, else: acc_j
                  end
              end
              min_val + 1
            else
              # s on the right side
              s_prime = n + 1 - s
              mid = div(n - 2 * s_prime + 1, 2)

              min_val = 1_000_000

              for i <- 0..(f - 1), reduce: min_val do
                acc_i ->
                  for j <- 0..(s_prime - f - 1), reduce: acc_i do
                    acc_j ->
                      v = compute_earliest(next_n, i + 1, i + j + mid + 2)
                      if v < acc_j, do: v, else: acc_j
                  end
              end
              min_val + 1
            end
        end

        :ets.insert(:earliest_cache, {{n, f, s}, res})
        res
    end
  end

  # ---------- Latest (maximum rounds) ----------
  defp compute_latest(n, f, s) do
    case :ets.lookup(:latest_cache, {n, f, s}) do
      [{_, val}] -> val
      [] ->
        res = cond do
          f + s == n + 1 ->
            1

          true ->
            next_n = div(n + 1, 2)

            if s <= div(n, 2) do
              max_val = -1_000_000

              for i <- 0..(f - 1), reduce: max_val do
                acc_i ->
                  for j <- 0..(s - f - 1), reduce: acc_i do
                    acc_j ->
                      v = compute_latest(next_n, i + 1, i + j + 2)
                      if v > acc_j, do: v, else: acc_j
                  end
              end
              max_val + 1
            else
              s_prime = n + 1 - s
              mid = div(n - 2 * s_prime + 1, 2)

              max_val = -1_000_000

              for i <- 0..(f - 1), reduce: max_val do
                acc_i ->
                  for j <- 0..(s_prime - f - 1), reduce: acc_i do
                    acc_j ->
                      v = compute_latest(next_n, i + 1, i + j + mid + 2)
                      if v > acc_j, do: v, else: acc_j
                  end
              end
              max_val + 1
            end
        end

        :ets.insert(:latest_cache, {{n, f, s}, res})
        res
    end
  end
end
```
