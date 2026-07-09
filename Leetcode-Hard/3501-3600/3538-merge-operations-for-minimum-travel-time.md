# 3538. Merge Operations for Minimum Travel Time

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        const long long INF = (1LL<<60);
        // prefix sum of time
        vector<long long> pref(n+1,0);
        for(int i=0;i<n;i++) pref[i+1]=pref[i]+time[i];
        
        vector<vector<long long>> dp(n, vector<long long>(k+1, INF));
        dp[0][0]=0; // start at position 0
        
        for(int i=1;i<n;i++){
            for(int j=0;j<=k;j++){
                for(int p=0;p<i;p++){
                    int del = i-p-1;
                    if(del>j) continue;
                    long long prev = dp[p][j-del];
                    if(prev==INF) continue;
                    long long sumDel = pref[i] - pref[p+1]; // times of deleted signs between p and i
                    long long effTime = (long long)time[i] + sumDel;
                    long long cost = prev + (long long)(position[i]-position[p]) * effTime;
                    dp[i][j]=min(dp[i][j], cost);
                }
            }
        }
        return (int)dp[n-1][k];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minTravelTime(int l, int n, int k, int[] position, int[] time) {
        long INF = Long.MAX_VALUE / 4;
        // prefix sum of time
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + time[i];
        }

        long[][][] dp = new long[n][k + 1][k + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                Arrays.fill(dp[i][j], INF);
            }
        }
        dp[0][0][0] = 0;

        for (int i = 0; i < n; i++) {
            for (int used = 0; used <= k; used++) {
                for (int s = 0; s <= k; s++) {
                    long cur = dp[i][used][s];
                    if (cur == INF) continue;

                    // effective time at sign i
                    long addedBefore = 0;
                    if (i > 0) {
                        int prevIdx = i - s - 1; // previous kept index
                        addedBefore = pref[i] - pref[prevIdx + 1];
                    }
                    long effTime = time[i] + addedBefore;

                    for (int nxt = i + 1; nxt < n; nxt++) {
                        int delBetween = nxt - i - 1;
                        int newUsed = used + delBetween;
                        if (newUsed > k) continue;
                        long cost = cur + (long) (position[nxt] - position[i]) * effTime;
                        if (cost < dp[nxt][newUsed][delBetween]) {
                            dp[nxt][newUsed][delBetween] = cost;
                        }
                    }
                }
            }
        }

        long ans = INF;
        for (int s = 0; s <= k; s++) {
            ans = Math.min(ans, dp[n - 1][k][s]);
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def minTravelTime(self, l, n, k, position, time):
        """
        :type l: int
        :type n: int
        :type k: int
        :type position: List[int]
        :type time: List[int]
        :rtype: int
        """
        INF = 10**18
        total_sum = sum(time)
        # prefix sums of time
        pref = [0] * n
        cur = 0
        for i in range(n):
            cur += time[i]
            pref[i] = cur

        # dp[idx][del][extra] = min cost up to idx (kept) with del deletions,
        # where extra is sum of times transferred to this sign from previous deletions
        dp = [[[INF] * (total_sum + 1) for _ in range(k + 1)] for __ in range(n)]
        dp[0][0][0] = 0

        for p in range(n - 1):
            for d in range(k + 1):
                row = dp[p][d]
                if all(v == INF for v in row):
                    continue
                for ep, cur_cost in enumerate(row):
                    if cur_cost == INF:
                        continue
                    # try next kept sign i > p
                    for i in range(p + 1, n):
                        cnt = i - p - 1
                        nd = d + cnt
                        if nd > k:
                            break
                        ei = pref[i - 1] - (pref[p] if p >= 0 else 0)
                        cost = (position[i] - position[p]) * (time[p] + ep)
                        new_val = cur_cost + cost
                        if new_val < dp[i][nd][ei]:
                            dp[i][nd][ei] = new_val

        ans = min(dp[n - 1][k])
        return ans
```

## Python3

```python
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        INF = 10**18
        # prefix sum of time
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + time[i]

        def block_sum(idx: int, s: int) -> int:
            # sum of time from idx-s to idx inclusive
            return pre[idx + 1] - pre[idx - s]

        # dp[i][d][s]: min cost reaching sign i (kept), using d deletions total,
        # and exactly s consecutive deletions just before i.
        dp = [[[INF] * (k + 1) for _ in range(k + 1)] for __ in range(n)]
        dp[0][0][0] = 0

        for i in range(1, n):
            for p in range(i):
                del_cnt = i - p - 1
                if del_cnt > k:
                    continue
                for d_prev in range(k + 1 - del_cnt):
                    for s_prev in range(k + 1):
                        cur = dp[p][d_prev][s_prev]
                        if cur == INF:
                            continue
                        new_d = d_prev + del_cnt
                        cost = cur + (position[i] - position[p]) * block_sum(p, s_prev)
                        if cost < dp[i][new_d][del_cnt]:
                            dp[i][new_d][del_cnt] = cost

        ans = min(dp[n - 1][k])
        return ans
```

## C

```c
#include <limits.h>
#include <stddef.h>

int minTravelTime(int l, int n, int k, int* position, int positionSize, int* time, int timeSize){
    const long long INF = 1LL<<60;
    static long long dp[55][12][12];
    for (int i=0;i<n;i++)
        for (int j=0;j<=k;j++)
            for (int s=0;s<=k;s++) dp[i][j][s]=INF;

    // prefix sum of time
    long long pref[55];
    pref[0]=time[0];
    for (int i=1;i<n;i++) pref[i]=pref[i-1]+time[i];

    dp[0][0][0]=0; // first sign kept, no deletions

    for (int p=0;p<n-1;p++){
        for (int used=0;used<=k;used++){
            for (int sPrev=0;sPrev<=k;sPrev++){
                long long cur = dp[p][used][sPrev];
                if (cur==INF) continue;
                // effective time at p
                long long effTime = time[p];
                if (sPrev>0){
                    int leftIdx = p - sPrev; // first deleted index before p
                    long long sumDel = pref[p-1] - (leftIdx-1>=0 ? pref[leftIdx-1] : 0);
                    effTime += sumDel;
                }
                for (int i=p+1;i<n;i++){
                    int delBetween = i - p - 1;
                    int newUsed = used + delBetween;
                    if (newUsed>k) break;
                    long long addCost = (long long)(position[i] - position[p]) * effTime;
                    int newS = delBetween; // deletions immediately before i
                    long long &dest = dp[i][newUsed][newS];
                    long long cand = cur + addCost;
                    if (cand < dest) dest = cand;
                }
            }
        }
    }

    long long ans = INF;
    for (int s=0;s<=k;s++){
        if (dp[n-1][k][s] < ans) ans = dp[n-1][k][s];
    }
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinTravelTime(int l, int n, int k, int[] position, int[] time) {
        int N = n;
        int K = k;
        long INF = (1L << 60);
        // prefix sum of time (excluding the last unused element)
        long[] pref = new long[N];
        pref[0] = 0;
        for (int i = 0; i < N - 1; i++) {
            pref[i + 1] = pref[i] + time[i];
        }

        long[,,] dp = new long[N, K + 1, K + 1];
        for (int i = 0; i < N; i++)
            for (int j = 0; j <= K; j++)
                for (int s = 0; s <= K; s++)
                    dp[i, j, s] = INF;

        dp[0, 0, 0] = 0;

        for (int p = 0; p < N - 1; p++) {
            for (int used = 0; used <= K; used++) {
                for (int consec = 0; consec <= used; consec++) {
                    long cur = dp[p, used, consec];
                    if (cur == INF) continue;

                    // sum of times of the 'consec' deleted signs before p
                    long added = 0;
                    if (consec > 0) {
                        int startIdx = p - consec; // first deleted sign index
                        added = pref[p] - pref[startIdx];
                    }
                    long effectiveRate = time[p] + added;

                    for (int q = p + 1; q < N; q++) {
                        int delBetween = q - p - 1;
                        int newUsed = used + delBetween;
                        if (newUsed > K) continue;
                        int newConsec = delBetween; // deletions before q
                        long cost = cur + (long)(position[q] - position[p]) * effectiveRate;
                        if (cost < dp[q, newUsed, newConsec]) {
                            dp[q, newUsed, newConsec] = cost;
                        }
                    }
                }
            }
        }

        long ans = INF;
        for (int s = 0; s <= K; s++) {
            if (dp[N - 1, K, s] < ans) ans = dp[N - 1, K, s];
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number} l
 * @param {number} n
 * @param {number} k
 * @param {number[]} position
 * @param {number[]} time
 * @return {number}
 * /
var minTravelTime = function(l, n, k, position, time) {
    const INF = Number.MAX_SAFE_INTEGER;
    // prefix sum of time: pref[i] = sum_{0..i-1} time
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + time[i];

    // dp[i][j][s] = min travel time up to sign i (kept), using j deletions total,
    // with s consecutive deletions immediately before i.
    const dp = Array.from({ length: n }, () =>
        Array.from({ length: k + 1 }, () => new Array(k + 1).fill(INF))
    );
    dp[0][0][0] = 0; // start sign

    for (let i = 0; i < n - 1; ++i) {
        for (let j = 0; j <= k; ++j) {
            for (let s = 0; s <= k; ++s) {
                const cur = dp[i][j][s];
                if (cur === INF) continue;
                if (s > i) continue; // cannot have more deletions than available signs before i
                const sumDeleted = pref[i] - pref[i - s]; // times of the s deleted signs before i
                const effective = time[i] + sumDeleted;   // per km time for segment starting at i

                for (let t = 0; t <= k - j; ++t) {
                    const nxt = i + t + 1;
                    if (nxt >= n) break;
                    const newJ = j + t;
                    const cost = cur + effective * (position[nxt] - position[i]);
                    if (cost < dp[nxt][newJ][t]) dp[nxt][newJ][t] = cost;
                }
            }
        }
    }

    let ans = INF;
    for (let s = 0; s <= k; ++s) {
        if (dp[n - 1][k][s] < ans) ans = dp[n - 1][k][s];
    }
    return ans;
};
```

## Typescript

```typescript
function minTravelTime(l: number, n: number, k: number, position: number[], time: number[]): number {
    const INF = Number.MAX_SAFE_INTEGER;
    const totalSum = time.reduce((a, b) => a + b, 0);
    // prefix sums of time
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + time[i];

    // dp[i][j][e] = min cost up to sign i kept, using j deletions, extra e added to time[i]
    const dp: number[][][] = Array.from({ length: n }, () =>
        Array.from({ length: k + 1 }, () => new Array(totalSum + 1).fill(INF))
    );
    dp[0][0][0] = 0;

    for (let i = 0; i < n; ++i) {
        for (let j = 0; j <= k; ++j) {
            for (let e = 0; e <= totalSum; ++e) {
                const cur = dp[i][j][e];
                if (cur === INF) continue;
                // try next kept sign
                for (let nxt = i + 1; nxt < n; ++nxt) {
                    const delCnt = nxt - i - 1;
                    const nj = j + delCnt;
                    if (nj > k) break; // further nxt will only increase deletions
                    const sumDel = pref[nxt] - pref[i + 1]; // times of deleted signs between i and nxt
                    const ne = sumDel; // extra for nxt
                    const cost = cur + (time[i] + e) * (position[nxt] - position[i]);
                    if (cost < dp[nxt][nj][ne]) {
                        dp[nxt][nj][ne] = cost;
                    }
                }
            }
        }
    }

    let ans = INF;
    for (let e = 0; e <= totalSum; ++e) {
        if (dp[n - 1][k][e] < ans) ans = dp[n - 1][k][e];
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $l
     * @param Integer $n
     * @param Integer $k
     * @param Integer[] $position
     * @param Integer[] $time
     * @return Integer
     */
    function minTravelTime($l, $n, $k, $position, $time) {
        $INF = PHP_INT_MAX;
        // prefix sum of time for quick range sums
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] + $time[$i];
        }

        // dp[i][j][s] = min cost up to sign i (kept), j deletions total, s consecutive deletions before i
        $dp = array_fill(0, $n, null);
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = array_fill(0, $k + 1, null);
            for ($j = 0; $j <= $k; $j++) {
                $dp[$i][$j] = array_fill(0, $k + 1, $INF);
            }
        }
        // start sign 0, no deletions before it
        $dp[0][0][0] = 0;

        for ($i = 1; $i < $n; $i++) {
            $maxS = min($k, $i); // cannot have more consecutive deletions than i
            for ($s = 0; $s <= $maxS; $s++) {
                $p = $i - $s - 1; // previous kept sign index
                if ($p < 0) continue;
                for ($j = $s; $j <= $k; $j++) {
                    $prevDel = $j - $s;
                    $maxPrevS = min($k, $p);
                    for ($sp = 0; $sp <= $maxPrevS; $sp++) {
                        $prevCost = $dp[$p][$prevDel][$sp];
                        if ($prevCost === $INF) continue;
                        // extra time accumulated before p
                        $extraPrev = ($sp == 0) ? 0 : ($pref[$p] - $pref[$p - $sp]);
                        $effectiveTimePrev = $time[$p] + $extraPrev;
                        $segmentLen = $position[$i] - $position[$p];
                        $newCost = $prevCost + $effectiveTimePrev * $segmentLen;
                        if ($newCost < $dp[$i][$j][$s]) {
                            $dp[$i][$j][$s] = $newCost;
                        }
                    }
                }
            }
        }

        // answer is min over possible s at the last sign with exactly k deletions
        $ans = $INF;
        for ($s = 0; $s <= $k; $s++) {
            if ($dp[$n - 1][$k][$s] < $ans) {
                $ans = $dp[$n - 1][$k][$s];
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minTravelTime(_ l: Int, _ n: Int, _ k: Int, _ position: [Int], _ time: [Int]) -> Int {
        let N = n
        let K = k
        var prefix = [Int64](repeating: 0, count: N + 1)
        for i in 0..<N {
            prefix[i + 1] = prefix[i] + Int64(time[i])
        }
        let INF = Int64.max / 4
        // dp[i][j][s] = min cost reaching sign i (kept), using j deletions total, with s consecutive deletions just before i
        var dp = Array(repeating: Array(repeating: Array(repeating: INF, count: K + 1), count: K + 1), count: N)
        dp[0][0][0] = 0
        for i in 0..<N {
            for j in 0...K {
                for s in 0...K where s <= i && dp[i][j][s] < INF {
                    let extraTime = prefix[i] - prefix[i - s]
                    let curTime = Int64(time[i]) + extraTime
                    for nxt in (i + 1)..<N {
                        let del = nxt - i - 1
                        let newJ = j + del
                        if newJ > K { continue }
                        let dist = Int64(position[nxt] - position[i])
                        let cost = dp[i][j][s] + curTime * dist
                        if cost < dp[nxt][newJ][del] {
                            dp[nxt][newJ][del] = cost
                        }
                    }
                }
            }
        }
        var answer = INF
        for s in 0...K {
            let val = dp[N - 1][K][s]
            if val < answer { answer = val }
        }
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
import kotlin.math.min

class Solution {
    fun minTravelTime(l: Int, n: Int, k: Int, position: IntArray, time: IntArray): Int {
        val INF = Int.MAX_VALUE / 4
        // prefix sum of times (including dummy last element)
        val pref = IntArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + time[i]
        }
        val maxBase = pref[n] + 100   // safe upper bound
        // dp[sign][deletions][baseTime] = min cost up to this sign (kept)
        val dp = Array(n) { Array(k + 1) { IntArray(maxBase + 1) { INF } } }
        if (time[0] > maxBase) return -1
        dp[0][0][time[0]] = 0
        var answer = INF

        for (p in 0 until n) {
            for (del in 0..k) {
                val row = dp[p][del]
                for (base in 0..maxBase) {
                    val curCost = row[base]
                    if (curCost == INF) continue
                    // try next kept sign i
                    var i = p + 1
                    while (i < n) {
                        val deletionsNeeded = i - p - 1
                        val newDel = del + deletionsNeeded
                        if (newDel > k) break
                        val dist = position[i] - position[p]
                        val newCost = curCost + dist * base
                        if (i == n - 1) {
                            answer = min(answer, newCost)
                        } else {
                            val sumDeleted = pref[i] - pref[p + 1]
                            val newBase = time[i] + sumDeleted
                            if (newBase <= maxBase && newCost < dp[i][newDel][newBase]) {
                                dp[i][newDel][newBase] = newCost
                            }
                        }
                        i++
                    }
                }
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minTravelTime(int l, int n, int k, List<int> position, List<int> time) {
    const int INF = 1 << 60;
    // prefix sum of time for quick interval sums
    List<int> pref = List.filled(n, 0);
    pref[0] = time[0];
    for (int i = 1; i < n; ++i) pref[i] = pref[i - 1] + time[i];

    // dp[i][j][s]: min cost up to sign i kept,
    // j deletions used, s consecutive deletions just before i
    List<List<List<int>>> dp = List.generate(
        n, (_) => List.generate(k + 1, (_) => List.filled(k + 1, INF)));
    dp[0][0][0] = 0; // start sign

    for (int i = 1; i < n; ++i) {
      int maxS = i - 1;
      if (maxS > k) maxS = k;
      for (int s = 0; s <= maxS; ++s) { // deletions just before i
        int p = i - s - 1; // previous kept sign index
        if (p < 0) continue;
        for (int jPrev = 0; jPrev + s <= k; ++jPrev) {
          for (int sPrev = 0; sPrev <= k && sPrev <= p; ++sPrev) {
            int prevCost = dp[p][jPrev][sPrev];
            if (prevCost == INF) continue;
            // cumulative time of sign p (including its preceding deletions)
            int leftIdx = p - sPrev;
            int cumTimePrev = pref[p] -
                (leftIdx > 0 ? pref[leftIdx - 1] : 0);
            int segCost =
                (position[i] - position[p]) * cumTimePrev;
            int newJ = jPrev + s;
            int val = prevCost + segCost;
            if (val < dp[i][newJ][s]) dp[i][newJ][s] = val;
          }
        }
      }
    }

    int ans = INF;
    for (int s = 0; s <= k; ++s) {
      if (dp[n - 1][k][s] < ans) ans = dp[n - 1][k][s];
    }
    return ans;
  }
}
```

## Golang

```go
func minTravelTime(l int, n int, k int, position []int, time []int) int {
    const INF = int(1e9)
    // prefix sums of distances and times
    dist := make([]int, n-1)
    for i := 0; i < n-1; i++ {
        dist[i] = position[i+1] - position[i]
    }
    prefTime := make([]int, n)
    prefDist := make([]int, n)
    prefDT := make([]int, n) // sum of dist[t]*prefTime[t]
    for i := 0; i < n; i++ {
        if i > 0 {
            prefDist[i] = prefDist[i-1] + dist[i-1]
        }
        prefTime[i] = time[i]
        if i > 0 {
            prefTime[i] += prefTime[i-1]
        }
        if i < n-1 {
            val := dist[i] * prefTime[i]
            prefDT[i] = val
            if i > 0 {
                prefDT[i] += prefDT[i-1]
            }
        }
    }

    // dp[i][j]: min travel time to reach sign i (kept) using j deletions
    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, k+1)
        for j := 0; j <= k; j++ {
            dp[i][j] = INF
        }
    }
    dp[0][0] = 0

    // helper to get sum of dist from a to b-1 (positions[a]..positions[b])
    sumDist := func(a, b int) int { return position[b] - position[a] }

    // helper to get original cost without merges between a and b (a<b)
    origCost := func(a, b int) int {
        if a == b {
            return 0
        }
        left := prefDT[b-1]
        if a > 0 {
            left -= prefDT[a-1]
        }
        return left
    }

    for i := 1; i < n; i++ {
        for j := 0; j <= k; j++ {
            // try previous kept sign p
            for p := 0; p < i; p++ {
                del := i - p - 1
                if del > j {
                    continue
                }
                // sum of times of deleted signs between p and i
                sumDel := prefTime[i-1] - prefTime[p]
                cost := origCost(p, i) + sumDist(p, i)*sumDel
                if dp[p][j-del]+cost < dp[i][j] {
                    dp[i][j] = dp[p][j-del] + cost
                }
            }
        }
    }

    return dp[n-1][k]
}
```

## Ruby

```ruby
def min_travel_time(l, n, k, position, time)
  # use only the first n-1 times (the last one is irrelevant)
  t = time[0, n - 1]
  max_k = k
  inf = 1 << 60

  # dp[i][r] => hash { [p, s] => cost }
  # i: current index being processed (1..n-1), where signs before i are decided.
  dp = Array.new(n) { Array.new(max_k + 1) { {} } }

  # start before processing sign 1, last kept is 0, accumulated removed sum s = 0
  dp[1][0][[0, 0]] = 0

  (1...n - 1).each do |i|
    (0..max_k).each do |r|
      cur_hash = dp[i][r]
      next if cur_hash.empty?
      cur_hash.each do |key, cost|
        p, s = key
        # option 1: remove sign i
        if r < max_k
          new_s = s + t[i]
          new_key = [p, new_s]
          prev = dp[i + 1][r + 1][new_key] || inf
          dp[i + 1][r + 1][new_key] = cost < prev ? cost : prev
        end
        # option 2: keep sign i
        effective_time = t[p] + s
        add = (position[i] - position[p]) * effective_time
        new_key = [i, 0]
        prev = dp[i + 1][r][new_key] || inf
        new_cost = cost + add
        dp[i + 1][r][new_key] = new_cost < prev ? new_cost : prev
      end
    end
  end

  ans = inf
  (0..max_k).each do |r|
    next unless r == k
    dp[n - 1][r].each do |key, cost|
      p, s = key
      effective_time = t[p] + s
      total = cost + (position[n - 1] - position[p]) * effective_time
      ans = total if total < ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def minTravelTime(l: Int, n: Int, k: Int, position: Array[Int], time: Array[Int]): Int = {
    val keptNeeded = n - k
    val INF: Long = Long.MaxValue / 4
    val dp = Array.fill(n)(Array.fill(keptNeeded + 1)(INF))
    dp(0)(1) = 0L

    for (i <- 1 until n) {
      // j is number of kept signs up to i, must be at least 2 and at most keptNeeded
      val maxJ = math.min(i + 1, keptNeeded)
      for (j <- 2 to maxJ) {
        var best = INF
        var p = 0
        while (p < i) {
          if (dp(p)(j - 1) != INF) {
            val cost = dp(p)(j - 1) + (position(i).toLong - position(p).toLong) * time(p).toLong
            if (cost < best) best = cost
          }
          p += 1
        }
        dp(i)(j) = best
      }
    }

    dp(n - 1)(keptNeeded).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_travel_time(l: i32, n: i32, k: i32, position: Vec<i32>, time: Vec<i32>) -> i32 {
        let n_usize = n as usize;
        let keep_needed = (n - k) as usize; // number of signs to keep
        // prefix sum of time
        let mut pref_time = vec![0i64; n_usize + 1];
        for i in 0..n_usize {
            pref_time[i + 1] = pref_time[i] + time[i] as i64;
        }
        const INF: i64 = i64::MAX / 4;
        // dp[j][c]: min cost to reach sign j (kept) with c kept signs total (including start and j)
        let mut dp = vec![vec![INF; keep_needed + 1]; n_usize];
        dp[0][1] = 0;
        for j in 1..n_usize {
            // cnt ranges from 2 to keep_needed
            for cnt in 2..=keep_needed.min(j + 1) {
                let mut best = INF;
                for i in 0..j {
                    if dp[i][cnt - 1] == INF {
                        continue;
                    }
                    let dist = (position[j] - position[i]) as i64;
                    let time_sum = pref_time[j] - pref_time[i];
                    let cost = dist * time_sum;
                    let cand = dp[i][cnt - 1] + cost;
                    if cand < best {
                        best = cand;
                    }
                }
                dp[j][cnt] = best;
            }
        }
        let ans = dp[n_usize - 1][keep_needed];
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-travel-time l n k position time)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((m (- n k))                         ; number of signs to keep
         (INF (expt 2 60))
         (pos-vec (list->vector position))
         (time-vec (list->vector time))
         (dp (make-vector n)))
    ;; initialize dp table with INF
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector (+ m 1) INF)))
    ;; start at sign 0, count = 1, cost = 0
    (vector-set! (vector-ref dp 0) 1 0)
    ;; DP transitions
    (for ([i (in-range 1 n)])
      (let ((pos-i (vector-ref pos-vec i)))
        (for ([p (in-range 0 i)])
          (let* ((pos-p (vector-ref pos-vec p))
                 (dist (- pos-i pos-p))
                 (t (if (< p (sub1 n)) (vector-ref time-vec p) 0))) ; time[p]
            (when (> t -inf)                     ; always true, keep for symmetry
              (for ([c (in-range 1 m)])          ; previous kept count
                (let ((prev-cost (vector-ref (vector-ref dp p) c)))
                  (when (< prev-cost INF)
                    (let* ((newcnt (+ c 1))
                           (newcost (+ prev-cost (* t dist))))
                      (when (< newcost (vector-ref (vector-ref dp i) newcnt))
                        (vector-set! (vector-ref dp i) newcnt newcost))))))))))
    ;; answer: cost to reach last sign with exactly m kept signs
    (vector-ref (vector-ref dp (- n 1)) m)))
```

## Erlang

```erlang
-spec min_travel_time(L :: integer(), N :: integer(), K :: integer(),
                       Position :: [integer()], Time :: [integer()]) -> integer().
min_travel_time(_L, N, K, Position, Time) ->
    %% prefix sum of Time
    Pref = build_prefix(Time, 0, []),
    DPAll0 = maps:put(0, #{ {0,0} => 0 }, #{}),
    DPAll = loop_i(0, N-1, K, Position, Time, Pref, DPAll0),
    FinalMap = maps:get(N-1, DPAll, #{}),
    find_min(K, FinalMap).

%% build prefix sums: returns list where element i is sum of first i elements (i from 0..len)
build_prefix([], Acc, AccList) ->
    lists:reverse([Acc | AccList]);
build_prefix([H|T], Acc, AccList) ->
    NewAcc = Acc + H,
    build_prefix(T, NewAcc, [Acc | AccList]).

%% get prefix sum up to index i (0‑based, exclusive)
pref_at(Pref, I) ->
    lists:nth(I+1, Pref).   % because Pref list is 1‑based after reverse

loop_i(I, NMinusOne, K, Position, Time, Pref, DPAll) when I < NMinusOne ->
    MapI = maps:get(I, DPAll, #{}),
    DPAll2 = maps:fold(
        fun({J,S}, Val, AccDP) ->
            EffectiveTime = get_time(Time, I) + (pref_at(Pref, I) - pref_at(Pref, I - S)),
            lists:foldl(
                fun(Nxt, AccDP2) ->
                    D = Nxt - I - 1,
                    NewJ = J + D,
                    if NewJ =< K ->
                        CostAdd = (get_pos(Position, Nxt) - get_pos(Position, I)) * EffectiveTime,
                        NewVal = Val + CostAdd,
                        MapNxt0 = maps:get(Nxt, AccDP2, #{}),
                        Old = maps:get({NewJ,D}, MapNxt0, 1 bsl 60),
                        UpdatedMapNxt =
                            if NewVal < Old ->
                                maps:put({NewJ,D}, NewVal, MapNxt0);
                               true -> MapNxt0
                            end,
                        maps:put(Nxt, UpdatedMapNxt, AccDP2);
                       true -> AccDP2
                    end
                end,
                AccDP,
                lists:seq(I+1, NMinusOne)
            )
        end,
        DPAll,
        MapI),
    loop_i(I+1, NMinusOne, K, Position, Time, Pref, DPAll2);
loop_i(_, _, _, _, _, _, DPAll) -> DPAll.

get_pos(List, Index) ->
    lists:nth(Index+1, List).

get_time(List, Index) ->
    lists:nth(Index+1, List).

find_min(K, Map) ->
    maps:fold(
        fun({J,_S}, Val, Min) ->
            if J =:= K, Val < Min -> Val; true -> Min end
        end,
        1 bsl 60,
        Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_travel_time(l :: integer, n :: integer, k :: integer, position :: [integer], time :: [integer]) :: integer
  def min_travel_time(_l, n, k, position, time) do
    # prefix sum of time for quick range sums
    pref = Enum.reduce(0..(n - 1), [0], fn idx, acc ->
      [Enum.at(time, idx) + hd(acc) | acc]
    end) |> Enum.reverse()

    # dp[i] is a map %{ {j, effective_time} => min_cost } for sign i being kept
    empty_dp = List.duplicate(%{}, n)
    dp0 = %{{0, Enum.at(time, 0)} => 0}
    dp = List.replace_at(empty_dp, 0, dp0)

    dp =
      Enum.reduce(0..(n - 2), dp, fn i, dp_acc ->
        cur_map = Enum.at(dp_acc, i)

        Enum.reduce(cur_map, dp_acc, fn {{j, e}, cur_cost}, dp_inner ->
          # try all next kept signs t > i
          Enum.reduce((i + 1)..(n - 1), dp_inner, fn t, dp_mid ->
            del = t - i - 1
            new_j = j + del

            if new_j <= k do
              sum_del = Enum.at(pref, t) - Enum.at(pref, i + 1)
              e_t = Enum.at(time, t) + sum_del
              dist = Enum.at(position, t) - Enum.at(position, i)
              add_cost = dist * e
              total = cur_cost + add_cost

              old_map = Enum.at(dp_mid, t)
              prev = Map.get(old_map, {new_j, e_t}, :infinity)

              new_map =
                if total < prev do
                  Map.put(old_map, {new_j, e_t}, total)
                else
                  old_map
                end

              List.replace_at(dp_mid, t, new_map)
            else
              dp_mid
            end
          end)
        end)
      end)

    final_map = Enum.at(dp, n - 1)

    final_map
    |> Enum.filter(fn {{j, _e}, _cost} -> j == k end)
    |> Enum.map(fn {_key, cost} -> cost end)
    |> Enum.min()
  end
end
```
