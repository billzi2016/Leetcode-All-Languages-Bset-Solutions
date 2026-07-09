# 3389. Minimum Operations to Make Character Frequencies Equal

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int makeStringGood(string s) {
        const int ALPH = 26;
        vector<int> cnt(ALPH,0);
        for(char ch: s) cnt[ch-'a']++;
        vector<long long> pref(ALPH,0);
        long long sum=0;
        for(int i=0;i<ALPH;i++){
            sum+=cnt[i];
            pref[i]=sum;
        }
        int n = s.size();
        const long long INF = (1LL<<60);
        long long answer = INF;
        // enumerate possible target frequency c
        for(int c=1;c<=n;c++){
            vector<long long> dp(ALPH+1, INF), ndp(ALPH+1, INF);
            dp[0]=0; // before any letters, 0 selected
            for(int i=0;i<ALPH;i++){
                fill(ndp.begin(), ndp.end(), INF);
                for(int k=0;k<=i+1;k++){
                    long long add = llabs(pref[i] - 1LL*k*c);
                    // not select current letter -> keep same k
                    if(dp[k]!=INF){
                        ndp[k]=min(ndp[k], dp[k]+add);
                    }
                    // select current letter -> increase selected count
                    if(k>0 && dp[k-1]!=INF){
                        ndp[k]=min(ndp[k], dp[k-1]+add);
                    }
                }
                dp.swap(ndp);
            }
            for(int k=1;k<=ALPH;k++){
                answer = min(answer, dp[k]);
            }
        }
        return (int)answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int makeStringGood(String s) {
        int n = s.length();
        int[] occ = new int[26];
        for (char ch : s.toCharArray()) occ[ch - 'a']++;
        int maxFreq = 0;
        for (int v : occ) if (v > maxFreq) maxFreq = v;

        long INF = Long.MAX_VALUE / 4;
        int limitCarry = n; // maximum possible carry cannot exceed original length

        long answer = INF;

        // try every possible target frequency c from 1 to maxFreq
        for (int c = 1; c <= maxFreq; ++c) {
            long[] dp = new long[limitCarry + 1];
            Arrays.fill(dp, INF);
            dp[0] = 0;

            for (int i = 0; i < 26; ++i) {
                int curOcc = occ[i];

                // precompute suffix minima of dp[x] + x
                long[] sufPlus = new long[limitCarry + 2];
                sufPlus[limitCarry + 1] = INF;
                for (int x = limitCarry; x >= 0; --x) {
                    long val = dp[x] == INF ? INF : dp[x] + x;
                    sufPlus[x] = Math.min(val, sufPlus[x + 1]);
                }

                // precompute prefix minima of dp[x] - x
                long[] prefMinus = new long[limitCarry + 1];
                long curMin = INF;
                for (int x = 0; x <= limitCarry; ++x) {
                    long val = dp[x] == INF ? INF : dp[x] - x;
                    if (val < curMin) curMin = val;
                    prefMinus[x] = curMin;
                }

                long[] ndp = new long[limitCarry + 1];
                Arrays.fill(ndp, INF);

                // option f = 0 (make this letter count zero)
                for (int k = 0; k <= limitCarry; ++k) {
                    int needIdx = Math.max(0, k - curOcc);
                    if (needIdx <= limitCarry) {
                        long cand = (long)curOcc + sufPlus[needIdx];
                        if (cand < ndp[k]) ndp[k] = cand;
                    }
                }

                // option f = c
                // case total >= c
                for (int k = 0; k <= limitCarry; ++k) {
                    int idx = Math.max(0, k + c - curOcc);
                    if (idx <= limitCarry) {
                        long cand = (long)curOcc - c + sufPlus[idx];
                        if (cand < ndp[k]) ndp[k] = cand;
                    }
                }

                // case total < c : only k == 0
                if (c > curOcc) {
                    int maxCarryForLess = Math.min(limitCarry, c - curOcc - 1);
                    if (maxCarryForLess >= 0) {
                        long cand = (long)(c - curOcc) + prefMinus[maxCarryForLess];
                        if (cand < ndp[0]) ndp[0] = cand;
                    }
                }

                dp = ndp;
            }

            // after processing all letters, delete remaining carry
            for (int k = 0; k <= limitCarry; ++k) {
                if (dp[k] == INF) continue;
                long totalCost = dp[k] + k; // delete leftover characters
                if (totalCost < answer) answer = totalCost;
            }
        }

        return (int)answer;
    }
}
```

## Python

```python
class Solution(object):
    def makeStringGood(self, s):
        """
        :type s: str
        :rtype: int
        """
        from math import inf

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        n = len(s)
        ans = inf

        # DP over possible target frequency f (1..n)
        # dp[i][c] = minimal cost after processing first i letters,
        # with c characters carried to the next letter (0 <= c <= f)
        for f in range(1, n + 1):
            # maximum carry we ever need is at most f
            max_carry = f
            dp = [inf] * (max_carry + 1)
            dp[0] = 0
            for i in range(26):
                ndp = [inf] * (max_carry + 1)
                a = cnt[i]
                for carry in range(max_carry + 1):
                    if dp[carry] == inf:
                        continue
                    # move previous carry one step forward (cost = carry)
                    cur_cost = dp[carry] + carry
                    avail = a + carry

                    # option 1: do not keep this letter (target count 0)
                    # we may delete all or shift some to next
                    # shifting x characters costs nothing now, they become new carry
                    # deleting the rest costs 1 per character
                    # Since moving more than one step never helps, we only need to consider
                    # keeping at most max_carry characters for the next position.
                    keep = min(avail, max_carry)
                    del_cost = avail - keep
                    if cur_cost + del_cost < ndp[keep]:
                        ndp[keep] = cur_cost + del_cost

                    # option 2: make this letter have exactly f occurrences
                    if avail >= f:
                        new_carry = min(avail - f, max_carry)
                        add_cost = 0
                    else:
                        new_carry = 0
                        add_cost = f - avail
                    total = cur_cost + add_cost
                    if total < ndp[new_carry]:
                        ndp[new_carry] = total
                dp = ndp
            # after last letter, any remaining carry must be deleted (cost per char)
            final_cost = min(dp[c] + c for c in range(max_carry + 1))
            ans = min(ans, final_cost)

        return int(ans)
```

## Python3

```python
class Solution:
    def makeStringGood(self, s: str) -> int:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        pref = [0] * 27
        for i in range(26):
            pref[i + 1] = pref[i] + freq[i]

        INF = 10 ** 9
        answer = n  # delete all characters

        for c in range(1, n + 1):
            dp = [INF] * 27
            dp[0] = 0
            for i in range(27):
                cur = dp[i]
                if cur == INF:
                    continue
                # delete all remaining letters (make them zero)
                tail = pref[26] - pref[i]
                if cur + tail < dp[26]:
                    dp[26] = cur + tail
                # try to keep a letter at position j (segment i..j)
                for j in range(i, 26):
                    seg_sum = pref[j + 1] - pref[i]
                    cost = abs(seg_sum - c)
                    nd = cur + cost
                    if nd < dp[j + 1]:
                        dp[j + 1] = nd
            if dp[26] < answer:
                answer = dp[26]

        return answer
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <limits.h>

int makeStringGood(char* s) {
    int n = strlen(s);
    int cnt[26] = {0};
    for (int i = 0; i < n; ++i) cnt[s[i] - 'a']++;

    int pref[26];
    int sum = 0;
    for (int i = 0; i < 26; ++i) {
        sum += cnt[i];
        pref[i] = sum;
    }

    int maxC = n; // no need to consider larger frequencies
    int answer = INT_MAX;

    const int INF = 1e9;
    int prev[27], cur[27];

    for (int c = 0; c <= maxC; ++c) {
        for (int k = 0; k <= 26; ++k) prev[k] = INF;
        prev[0] = 0;

        for (int i = 0; i < 26; ++i) {
            int limit = i + 1;
            for (int k = 0; k <= limit; ++k) cur[k] = INF;

            for (int k = 0; k <= limit; ++k) {
                int best = prev[k];
                if (k > 0 && prev[k - 1] < best) best = prev[k - 1];
                if (best == INF) continue;
                int cost = abs(pref[i] - c * k);
                cur[k] = best + cost;
            }
            for (int k = 0; k <= limit; ++k) prev[k] = cur[k];
        }

        for (int k = 0; k <= 26; ++k) {
            if (prev[k] < answer) answer = prev[k];
        }
    }

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MakeStringGood(string s) {
        int n = s.Length;
        int[] freq = new int[26];
        foreach (char ch in s) {
            freq[ch - 'a']++;
        }

        int answer = n; // delete all characters

        for (int c = 1; c <= n; c++) {
            int[] vals = new int[26];
            for (int i = 0; i < 26; i++) {
                vals[i] = Math.Min(freq[i], c);
            }
            Array.Sort(vals);
            // sort descending by iterating from end
            int sum = 0;
            for (int m = 1; m <= 26; m++) {
                sum += vals[26 - m]; // take the m largest values
                int ops = Math.Max(n - sum, m * c - sum);
                if (ops < answer) answer = ops;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var makeStringGood = function(s) {
    const n = s.length;
    // count occurrences of each letter
    const occ = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) occ[s.charCodeAt(i) - 97]++;

    // if already good (only one distinct char or all counts equal)
    let distinct = 0;
    let firstCount = -1;
    let alreadyGood = true;
    for (let i = 0; i < 26; ++i) {
        if (occ[i] > 0) {
            distinct++;
            if (firstCount === -1) firstCount = occ[i];
            else if (occ[i] !== firstCount) alreadyGood = false;
        }
    }
    if (alreadyGood) return 0;

    const maxOcc = Math.max(...occ);
    const INF = 1e15;
    let answer = INF;

    // DP for a given target frequency c
    const solveForC = (c) => {
        // dpPrev[s] = min cost with surplus s before processing current letter
        let dpPrev = new Array(n + 1).fill(INF);
        dpPrev[0] = 0;
        for (let i = 0; i < 26; ++i) {
            const curOcc = occ[i];
            const dpCurr = new Array(n + 1).fill(INF);
            for (let s = 0; s <= n; ++s) {
                const prevCost = dpPrev[s];
                if (prevCost === INF) continue;
                const total = curOcc + s;

                // option 1: delete all at this position
                let costDel = prevCost + total; // delete each unit
                if (costDel < dpCurr[0]) dpCurr[0] = costDel;

                // option 2: keep with frequency c
                if (total >= c) {
                    const excess = total - c;
                    const newSurplus = excess;
                    const costKeep = prevCost + excess; // move excess one step right
                    if (costKeep < dpCurr[newSurplus]) dpCurr[newSurplus] = costKeep;
                } else {
                    const need = c - total;
                    const costKeep = prevCost + need; // insert needed units
                    if (costKeep < dpCurr[0]) dpCurr[0] = costKeep;
                }
            }
            dpPrev = dpCurr;
        }
        // after last letter, any remaining surplus must be deleted
        let best = INF;
        for (let s = 0; s <= n; ++s) {
            const val = dpPrev[s];
            if (val === INF) continue;
            const totalCost = val + s; // delete leftover surplus
            if (totalCost < best) best = totalCost;
        }
        return best;
    };

    for (let c = 1; c <= maxOcc; ++c) {
        const curAns = solveForC(c);
        if (curAns < answer) answer = curAns;
    }

    // also consider deleting everything (empty string is good)
    answer = Math.min(answer, n); // delete all characters

    return answer;
};
```

## Typescript

```typescript
function makeStringGood(s: string): number {
    const occ = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        occ[s.charCodeAt(i) - 97]++;
    }
    const n = s.length;
    let answer = n; // delete all characters

    const maxC = n; // no need to consider larger target count

    for (let l = 0; l < 26; ++l) {
        for (let r = l; r < 26; ++r) {
            for (let c = 0; c <= maxC; ++c) {
                let surplus = 0;
                let cost = 0;
                for (let i = 0; i < 26; ++i) {
                    const total = occ[i] + surplus;
                    const target = (i >= l && i <= r) ? c : 0;
                    if (total >= target) {
                        const excess = total - target;
                        cost += excess; // move forward one step
                        surplus = excess;
                    } else {
                        const deficit = target - total;
                        cost += deficit; // insert needed characters
                        surplus = 0;
                    }
                }
                cost += surplus; // delete remaining surplus after 'z'
                if (cost < answer) answer = cost;
            }
        }
    }

    return answer;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function makeStringGood($s) {
        $n = strlen($s);
        $cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $cnt[ord($s[$i]) - 97]++;
        }
        $maxCnt = max($cnt);
        $INF = PHP_INT_MAX >> 1;
        $answer = $n; // delete all

        for ($c = 1; $c <= $maxCnt; $c++) {
            // dp[carry] = minimal cost after processing previous letters
            $dp = array_fill(0, $n + 1, $INF);
            $dp[0] = 0;
            $totalSeen = 0;

            for ($i = 0; $i < 26; $i++) {
                $occ = $cnt[$i];
                $newDp = array_fill(0, $n + 1, $INF);
                for ($carry = 0; $carry <= $totalSeen; $carry++) {
                    if ($dp[$carry] == $INF) continue;
                    // cost to move current carry across edge (except before first letter)
                    $moveCost = ($i == 0) ? 0 : $carry;

                    $base = $dp[$carry] + $moveCost;
                    $total = $carry + $occ;

                    // Option 1: do not keep this character type
                    // we may delete any number d (0..$total), leaving newCarry = $total - $d
                    // The optimal is to consider all possible newCarry values.
                    // Since cost = $base + ($total - $newCarry)
                    // This is linear decreasing in $newCarry, so the minimal for each $newCarry
                    // can be obtained by scanning carries in increasing order.
                    // We'll update directly:
                    for ($newCarry = 0; $newCarry <= $total; $newCarry++) {
                        $cost = $base + ($total - $newCarry);
                        if ($cost < $newDp[$newCarry]) $newDp[$newCarry] = $cost;
                    }

                    // Option 2: keep this character type (final frequency = c)
                    if ($total >= $c) {
                        // no additions needed
                        $newCarry = $total - $c;
                        $cost = $base; // all chars used, no extra cost
                        if ($cost < $newDp[$newCarry]) $newDp[$newCarry] = $cost;
                    } else {
                        // need to add (c - $total) characters
                        $add = $c - $total;
                        $newCarry = 0;
                        $cost = $base + $add;
                        if ($cost < $newDp[$newCarry]) $newDp[$newCarry] = $cost;
                    }
                }
                $dp = $newDp;
                $totalSeen += $occ;
            }

            // after processing all letters, delete remaining carry
            for ($carry = 0; $carry <= $n; $carry++) {
                if ($dp[$carry] == $INF) continue;
                $finalCost = $dp[$carry] + $carry; // delete leftover
                if ($finalCost < $answer) $answer = $finalCost;
            }
        }

        return $answer;
    }
}
?>
```

## Swift

```swift
class Solution {
    func makeStringGood(_ s: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for byte in s.utf8 {
            let idx = Int(byte - 97)
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        let n = s.count
        var maxFreq = 0
        for f in freq { if f > maxFreq { maxFreq = f } }
        var answer = n
        if maxFreq == 0 { return 0 }
        for c in 1...maxFreq {
            var cnt = 0
            for f in freq where f >= c {
                cnt += 1
            }
            let deletions = n - c * cnt
            if deletions < answer {
                answer = deletions
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeStringGood(s: String): Int {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        val nonZero = mutableListOf<Int>()
        var maxFreq = 0
        for (f in freq) {
            if (f > 0) {
                nonZero.add(f)
                if (f > maxFreq) maxFreq = f
            }
        }
        // If the string is already good (all non-zero frequencies equal), answer will be 0.
        var best = Int.MAX_VALUE
        for (c in 1..maxFreq) {
            var ops = 0
            for (f in nonZero) {
                ops += kotlin.math.abs(f - c)
                if (ops >= best) break // early stop
            }
            if (ops < best) best = ops
        }
        return if (best == Int.MAX_VALUE) 0 else best
    }
}
```

## Dart

```dart
class Solution {
  int makeStringGood(String s) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      freq[s.codeUnitAt(i) - 97]++;
    }
    int maxFreq = freq.reduce((a, b) => a > b ? a : b);
    int ans = s.length;
    for (int c = 1; c <= maxFreq; c++) {
      int cost = 0;
      for (int f in freq) {
        int diff = (f - c).abs();
        cost += f < diff ? f : diff;
      }
      if (cost < ans) ans = cost;
    }
    return ans;
  }
}
```

## Golang

```go
func makeStringGood(s string) int {
    const INF = int(1e9)
    occ := [26]int{}
    for _, ch := range s {
        occ[ch-'a']++
    }
    maxOcc := 0
    total := len(s)
    for _, v := range occ[:] {
        if v > maxOcc {
            maxOcc = v
        }
    }
    answer := total // delete all characters as worst case

    // try all possible common frequency c (1 .. maxOcc+2)
    for c := 1; c <= maxOcc+2; c++ {
        // precompute excess, deficit and node cost for each letter and state
        var excess [26][2]int
        var deficit [26][2]int
        var nodeCost [26][2]int
        for i := 0; i < 26; i++ {
            cnt := occ[i]
            // state 0 -> target 0
            excess[i][0] = cnt
            deficit[i][0] = 0
            nodeCost[i][0] = cnt

            // state 1 -> target c
            if cnt >= c {
                excess[i][1] = cnt - c
                deficit[i][1] = 0
                nodeCost[i][1] = cnt - c
            } else {
                excess[i][1] = 0
                deficit[i][1] = c - cnt
                nodeCost[i][1] = c - cnt
            }
        }

        dpPrev := [2]int{INF, INF}
        dpPrev[0] = nodeCost[0][0]
        dpPrev[1] = nodeCost[0][1]

        for i := 1; i < 26; i++ {
            var dpCurr [2]int
            dpCurr[0], dpCurr[1] = INF, INF
            for curState := 0; curState <= 1; curState++ {
                curNode := nodeCost[i][curState]
                curDef := deficit[i][curState]
                best := INF
                for prevState := 0; prevState <= 1; prevState++ {
                    red := excess[i-1][prevState]
                    if curDef < red {
                        red = curDef
                    }
                    cand := dpPrev[prevState] + curNode - red
                    if cand < best {
                        best = cand
                    }
                }
                dpCurr[curState] = best
            }
            dpPrev = dpCurr
        }

        curAns := dpPrev[0]
        if dpPrev[1] < curAns {
            curAns = dpPrev[1]
        }
        if curAns < answer {
            answer = curAns
        }
    }
    return answer
}
```

## Ruby

```ruby
def make_string_good(s)
  n = s.length
  cnt = Array.new(26, 0)
  s.each_byte { |b| cnt[b - 97] += 1 }
  pref = Array.new(27, 0)
  26.times { |i| pref[i + 1] = pref[i] + cnt[i] }

  max_c = cnt.max
  ans = n # delete all characters

  (1..max_c).each do |c|
    dp = [Float::INFINITY]
    dp[0] = 0
    26.times do |i|
      new_dp = Array.new(dp.size + 1, Float::INFINITY)
      cnt_i = cnt[i]
      pref_i = pref[i]
      dp.each_with_index do |cost, k|
        next if cost == Float::INFINITY
        prev_surplus = pref_i - k * c

        # option: not keep this character
        ns = prev_surplus + cnt_i
        new_cost = cost + ns.abs
        new_dp[k] = new_cost if new_cost < new_dp[k]

        # option: keep this character with frequency c
        ns2 = ns - c
        new_cost2 = cost + ns2.abs
        new_dp[k + 1] = new_cost2 if new_cost2 < new_dp[k + 1]
      end
      dp = new_dp
    end

    dp.each_with_index do |cost, k|
      next if cost == Float::INFINITY
      final_surplus = n - k * c
      total_cost = cost + final_surplus.abs
      ans = total_cost if total_cost < ans
    end
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
    def makeStringGood(s: String): Int = {
        val n = s.length
        val occ = new Array[Int](26)
        for (ch <- s) occ(ch - 'a') += 1

        var answer = n // worst case delete all characters

        // maximum possible target frequency is n (inserting more would be useless)
        val maxC = n
        val pref = new Array[Int](27)
        for (i <- 0 until 26) pref(i + 1) = pref(i) + occ(i)

        // DP arrays reused for each c
        val INF = Int.MaxValue / 2
        var dpPrev = new Array[Int](n + 1)
        var dpCurr = new Array[Int](n + 1)

        for (c <- 1 to maxC) {
            java.util.Arrays.fill(dpPrev, INF)
            dpPrev(0) = 0

            for (i <- 0 until 26) {
                java.util.Arrays.fill(dpCurr, INF)
                val a = occ(i)
                var s = 0
                while (s <= n) {
                    val cur = dpPrev(s)
                    if (cur < INF) {
                        // cost to move existing surplus across edge i-1 -> i
                        val moveCost = s

                        // option 1: do not keep this character (target 0)
                        var surplusOut = a + s
                        var cost1 = cur + moveCost
                        if (cost1 < dpCurr(surplusOut)) dpCurr(surplusOut) = cost1

                        // option 2: keep this character with frequency c
                        val need = c - (a + s)
                        if (need <= 0) {
                            surplusOut = -(need) // a+s - c
                            val cost2 = cur + moveCost
                            if (cost2 < dpCurr(surplusOut)) dpCurr(surplusOut) = cost2
                        } else {
                            // need insertions
                            surplusOut = 0
                            val cost2 = cur + moveCost + need
                            if (cost2 < dpCurr(0)) dpCurr(0) = cost2
                        }
                    }
                    s += 1
                }
                // swap arrays
                val tmp = dpPrev
                dpPrev = dpCurr
                dpCurr = tmp
            }

            // after processing all letters, delete remaining surplus
            var s = 0
            while (s <= n) {
                val cur = dpPrev(s)
                if (cur < INF) {
                    val totalCost = cur + s // delete leftover surplus
                    if (totalCost < answer) answer = totalCost
                }
                s += 1
            }
        }

        answer
    }
}
```

## Rust

```rust
use std::cmp::{min};

impl Solution {
    pub fn make_string_good(s: String) -> i32 {
        // Count occurrences of each character.
        let mut occ = [0i32; 26];
        for ch in s.bytes() {
            occ[(ch - b'a') as usize] += 1;
        }

        // The maximum possible frequency we need to consider is the length of the string,
        // because any larger target would only require extra insertions which are never optimal.
        let n = s.len() as i32;
        let mut answer = i32::MAX;

        // Try every possible target frequency c (1 ..= n).
        for c in 1..=n {
            // dp[i] = minimal cost after processing first i letters,
            // with some surplus characters carried to the next letter.
            // The surplus can be at most n, so we keep a vector of size n+1.
            let mut dp_prev = vec![i32::MAX; (n + 1) as usize];
            dp_prev[0] = 0;

            for i in 0..26 {
                let cur_occ = occ[i];
                // next dp
                let mut dp_next = vec![i32::MAX; (n + 1) as usize];

                for surplus in 0..=n {
                    let prev_cost = dp_prev[surplus as usize];
                    if prev_cost == i32::MAX { continue; }

                    // total characters available at this position:
                    // original ones plus those moved from previous letters.
                    let avail = cur_occ + surplus;

                    // Option 1: make this letter inactive (final count 0).
                    // All available characters become surplus for the next letter,
                    // each moved one step costs 1 per character.
                    if avail <= n {
                        let cost = prev_cost + avail; // move all forward
                        let idx = avail as usize;
                        dp_next[idx] = min(dp_next[idx], cost);
                    }

                    // Option 2: make this letter active with exactly c occurrences.
                    if avail >= c {
                        // Use c characters here, excess becomes new surplus.
                        let excess = avail - c;
                        let cost = prev_cost + excess; // move excess forward
                        let idx = excess as usize;
                        dp_next[idx] = min(dp_next[idx], cost);
                    } else {
                        // Need (c - avail) insertions.
                        let need = c - avail;
                        // No surplus left after this letter.
                        let cost = prev_cost + need; // insert needed chars
                        dp_next[0] = min(dp_next[0], cost);
                    }
                }

                dp_prev = dp_next;
            }

            // After processing all letters, any remaining surplus must be deleted.
            for surplus in 0..=n {
                let total_cost = dp_prev[surplus as usize] + surplus; // delete leftovers
                answer = min(answer, total_cost);
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (make-string-good s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [occ (make-vector 26 0)])
    ;; count occurrences
    (for ([ch (in-string s)])
      (vector-set! occ (- (char->integer ch) (char->integer #\a))
                   (+ 1 (vector-ref occ (- (char->integer ch) (char->integer #\a))))))
    (define max-n n)
    ;; DP for each possible target frequency c
    (define best max-n) ; upper bound: delete all characters
    (for ([c (in-range 1 (+ max-n 1))])
      ;; dp[i][bal] = minimal cost after processing first i letters with balance bal
      (let* ([dp (make-vector 27 (make-vector (+ max-n 1) +inf.0))]
             [_ (vector-set! (vector-ref dp 0) 0 0)])
        (for ([i (in-range 26)])
          (let ([cur-occ (vector-ref occ i)])
            (for ([bal (in-range (+ max-n 1))])
              (define cur-cost (vector-ref (vector-ref dp i) bal))
              (when (< cur-cost +inf.0)
                ;; option 1: make this letter count 0
                (let* ([total (+ cur-occ bal)]
                       [new-bal total]
                       [add-cost total]) ; each moved one step forward
                  (define prev (vector-ref (vector-ref dp (+ i 1)) new-bal))
                  (when (< (+ cur-cost add-cost) prev)
                    (vector-set! (vector-ref dp (+ i 1)) new_bal (+ cur-cost add-cost))))
                ;; option 2: make this letter count c
                (let* ([total (+ cur-occ bal)])
                  (if (>= total c)
                      (let* ([surplus (- total c)]
                             [new-bal surplus]
                             [add-cost surplus]) ; move surplus one step forward
                        (define prev (vector-ref (vector-ref dp (+ i 1)) new_bal))
                        (when (< (+ cur-cost add-cost) prev)
                          (vector-set! (vector-ref dp (+ i 1)) new_bal (+ cur-cost add-cost))))
                      (let* ([need (- c total)]
                             [new-bal 0]
                             [add-cost need]) ; insert needed characters
                        (define prev (vector-ref (vector-ref dp (+ i 1)) new_bal))
                        (when (< (+ cur-cost add-cost) prev)
                          (vector-set! (vector-ref dp (+ i 1)) new_bal (+ cur-cost add-cost)))))))))
        ;; after processing all letters, delete remaining balance
        (for ([bal (in-range (+ max-n 1))])
          (define cost (+ (vector-ref (vector-ref dp 26) bal) bal))
          (when (< cost best)
            (set! best cost)))))
    best)))
```

## Erlang

```erlang
-spec make_string_good(S :: unicode:unicode_binary()) -> integer().
make_string_good(S) ->
    N = byte_size(S),
    OccTuple = count_occurrences(S, list_to_tuple(lists:duplicate(26, 0))),
    MaxOps = N,
    lists:foldl(
      fun(C, Best) ->
          Ops = min_ops_for_c(C, OccTuple),
          if Ops < Best -> Ops; true -> Best end
      end,
      MaxOps,
      lists:seq(1, N)
    ).

count_occurrences(<<>>, Tuple) -> Tuple;
count_occurrences(<<Char, Rest/binary>>, Tuple) ->
    Index = Char - $a + 1,
    Old = element(Index, Tuple),
    NewTuple = setelement(Index, Tuple, Old + 1),
    count_occurrences(Rest, NewTuple).

min_ops_for_c(C, OccTuple) ->
    Big = 1000000,
    % dpPrev0: previous character not selected
    % dpPrev1: previous character selected
    DP0 = 0,
    DP1 = Big,
    loop(1, 26, C, OccTuple, DP0, DP1, 0, false, Big).

loop(I, MaxI, _C, _OccTuple, DP0, DP1, _PrevOcc, false, _Big) when I > MaxI ->
    min(DP0, DP1);
loop(I, MaxI, C, OccTuple, DP0, DP1, PrevOcc, true, Big) when I > MaxI ->
    min(DP0, DP1);
loop(I, MaxI, C, OccTuple, DP0Prev, DP1Prev, PrevOcc, PrevExists, _Big) when I =< MaxI ->
    OccI = element(I, OccTuple),

    % Surplus from previous character
    SurplusPrev0 = if PrevExists -> PrevOcc else 0 end,
    SurplusPrev1 = if PrevExists -> max(0, PrevOcc - C) else 0 end,

    %% Current not selected (sel=0)
    Cost0 = OccI,
    NewDP0 = min(DP0Prev + Cost0, DP1Prev + Cost0),

    %% Current selected (sel=1)
    Diff1 = OccI - C,
    Cost1 = if Diff1 >= 0 -> Diff1; true -> -Diff1 end,
    Deficit1 = if Diff1 < 0 -> -Diff1; true -> 0 end,
    PairFromPrev0 = min(SurplusPrev0, Deficit1),
    PairFromPrev1 = min(SurplusPrev1, Deficit1),

    Cand01 = DP0Prev + Cost1 - PairFromPrev0,
    Cand11 = DP1Prev + Cost1 - PairFromPrev1,
    NewDP1 = min(Cand01, Cand11),

    loop(I + 1, MaxI, C, OccTuple, NewDP0, NewDP1, OccI, true, Big).

min(A, B) when A =< B -> A;
min(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec make_string_good(s :: String.t()) :: integer
  def make_string_good(s) do
    freqs =
      :binary.bin_to_list(s)
      |> Enum.reduce(List.duplicate(0, 26), fn ch, acc ->
        idx = ch - ?a
        List.update_at(acc, idx, &(&1 + 1))
      end)

    max_freq = Enum.max(freqs)

    1..max_freq
    |> Enum.map(fn c ->
      Enum.reduce(freqs, 0, fn f, sum -> sum + min(f, abs(f - c)) end)
    end)
    |> Enum.min()
  end
end
```
