# 3579. Minimum Steps to Convert String with Operations

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.size();
        const int INF = 1e9;
        static int dp[2][101][101];
        for (int d = 0; d < 2; ++d)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    dp[d][i][j] = INF;

        for (int len = 1; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                for (int d = 0; d < 2; ++d) {
                    if (len == 1) {
                        int srcIdx = (d == 0 ? l : l); // same when length is 1
                        dp[d][l][r] = (word1[srcIdx] == word2[l]) ? 0 : 1;
                        continue;
                    }
                    int best = INF;
                    // split
                    for (int k = l; k < r; ++k) {
                        best = min(best, dp[d][l][k] + dp[d][k+1][r]);
                    }
                    // swap pairs
                    for (int i = l; i <= r; ++i) {
                        int src_i = (d == 0 ? i : l + r - i);
                        if (word1[src_i] == word2[i]) continue; // already correct, swapping would break
                        for (int j = i + 1; j <= r; ++j) {
                            int src_j = (d == 0 ? j : l + r - j);
                            if (word1[src_i] == word2[j] && word1[src_j] == word2[i]) {
                                int cost = 1;
                                if (i > l) cost += dp[d][l][i-1];
                                if (i + 1 <= j - 1) cost += dp[d][i+1][j-1];
                                if (j < r) cost += dp[d][j+1][r];
                                best = min(best, cost);
                            }
                        }
                    }
                    dp[d][l][r] = best;
                }
                // apply reverse operation
                for (int d = 0; d < 2; ++d) {
                    dp[d][l][r] = min(dp[d][l][r], 1 + dp[1-d][l][r]);
                }
            }
        }
        return dp[0][0][n-1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minOperations(String word1, String word2) {
        int n = word1.length();
        final int INF = 1_000_000;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int cost = calc(word1, word2, j, i - 1, false);
                dp[i] = Math.min(dp[i], dp[j] + cost);
                int revCost = calc(word1, word2, j, i - 1, true);
                dp[i] = Math.min(dp[i], dp[j] + revCost);
            }
        }
        return dp[n];
    }

    private int calc(String w1, String w2, int l, int r, boolean rev) {
        int mismatches = 0;
        int[][] cnt = new int[26][26];
        int len = r - l + 1;
        for (int k = 0; k < len; k++) {
            int idx = rev ? (r - k) : (l + k);
            char a = w1.charAt(idx);
            char b = w2.charAt(l + k);
            if (a != b) {
                mismatches++;
                cnt[a - 'a'][b - 'a']++;
            }
        }
        int swaps = 0;
        for (int x = 0; x < 26; x++) {
            for (int y = x + 1; y < 26; y++) {
                swaps += Math.min(cnt[x][y], cnt[y][x]);
            }
        }
        return mismatches - swaps + (rev ? 1 : 0);
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            # accumulate counts incrementally to avoid recomputing from scratch for each j
            cnt_norm = [0] * 676   # 26*26
            cnt_rev = [0] * 676
            mism_norm = 0
            mism_rev = 0
            for j in range(i, n):
                # normal orientation update
                a = word1[j]
                b = word2[j]
                if a != b:
                    mism_norm += 1
                    cnt_norm[(ord(a) - 97) * 26 + (ord(b) - 97)] += 1

                # reversed orientation update: compare word1[j] with word2[i + (j-i)] after reversal,
                # which is equivalent to comparing word1[i + (j-i_rev)] where j_rev = i + (j-i)
                # Simpler: the character from word1 that will be at position j after reversing
                # substring [i..j] is word1[i + (j - k)] for original index k.
                # When extending j by one, the new reversed pair is:
                #   a_rev = word1[i + (j - i) - (j - i)]? Actually easier to recompute each time:
                # We'll compute using offset from start.
                offset = j - i
                a_rev = word1[i + (j - i) - offset]  # which simplifies to word1[j]
                # The above is wrong; we need the character that will appear at position i+offset after reversal,
                # which is original word1[j - offset].
                a_rev = word1[j - offset]
                b_rev = word2[i + offset]
                if a_rev != b_rev:
                    mism_rev += 1
                    cnt_rev[(ord(a_rev) - 97) * 26 + (ord(b_rev) - 97)] += 1

                # compute swaps for normal
                swaps_norm = 0
                for x in range(26):
                    base_x = x * 26
                    for y in range(x + 1, 26):
                        cnt_xy = cnt_norm[base_x + y]
                        cnt_yx = cnt_norm[y * 26 + x]
                        if cnt_xy and cnt_yx:
                            swaps_norm += min(cnt_xy, cnt_yx)
                cost_norm = mism_norm - swaps_norm

                # compute swaps for reversed
                swaps_rev = 0
                for x in range(26):
                    base_x = x * 26
                    for y in range(x + 1, 26):
                        cnt_xy = cnt_rev[base_x + y]
                        cnt_yx = cnt_rev[y * 26 + x]
                        if cnt_xy and cnt_yx:
                            swaps_rev += min(cnt_xy, cnt_yx)
                cost_rev = 1 + (mism_rev - swaps_rev)

                best = cost_norm if cost_norm < cost_rev else cost_rev
                if dp[i] + best < dp[j + 1]:
                    dp[j + 1] = dp[i] + best
        return dp[n]
```

## Python3

```python
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)

        # Precompute costs for each interval [l, r)
        cost_direct = [[0] * (n + 1) for _ in range(n)]
        cost_rev = [[0] * (n + 1) for _ in range(n)]

        def compute(a: str, b: str) -> int:
            m = 0
            cnt = {}
            for ca, cb in zip(a, b):
                if ca != cb:
                    m += 1
                    key = (ca, cb)
                    cnt[key] = cnt.get(key, 0) + 1
            swaps = 0
            visited = set()
            for (c1, c2), v in cnt.items():
                if (c1, c2) in visited:
                    continue
                rev_key = (c2, c1)
                if rev_key in cnt:
                    swaps += min(v, cnt[rev_key])
                visited.add((c1, c2))
                visited.add(rev_key)
            return m - swaps

        for l in range(n):
            for r in range(l + 1, n + 1):
                sub1 = word1[l:r]
                sub2 = word2[l:r]
                cost_direct[l][r] = compute(sub1, sub2)
                rev_sub1 = sub1[::-1]
                cost_rev[l][r] = compute(rev_sub1, sub2)

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        INF = 10 ** 9
        for length in range(1, n + 1):
            for l in range(0, n - length + 1):
                r = l + length
                best = INF
                # partition
                for k in range(l + 1, r):
                    val = dp[l][k] + dp[k][r]
                    if val < best:
                        best = val
                # whole segment as one group
                whole = cost_direct[l][r]
                rev_whole = 1 + cost_rev[l][r]
                if whole < best:
                    best = whole
                if rev_whole < best:
                    best = rev_whole
                dp[l][r] = best

        return dp[0][n]
```

## C

```c
#include <string.h>
#include <limits.h>

static int segCost(const char *w1, const char *w2, int l, int r) {
    int cnt[26][26] = {0};
    int mism = 0;
    for (int i = l; i < r; ++i) {
        int a = w1[i] - 'a';
        int b = w2[i] - 'a';
        if (a != b) {
            ++mism;
            ++cnt[a][b];
        }
    }
    int swaps = 0;
    for (int x = 0; x < 26; ++x)
        for (int y = x + 1; y < 26; ++y)
            swaps += cnt[x][y] < cnt[y][x] ? cnt[x][y] : cnt[y][x];
    return mism - swaps;
}

static int revSegCost(const char *w1, const char *w2, int l, int r) {
    int cnt[26][26] = {0};
    int mism = 0;
    for (int i = l; i < r; ++i) {
        int a = w1[r - 1 - (i - l)] - 'a'; // reversed index
        int b = w2[i] - 'a';
        if (a != b) {
            ++mism;
            ++cnt[a][b];
        }
    }
    int swaps = 0;
    for (int x = 0; x < 26; ++x)
        for (int y = x + 1; y < 26; ++y)
            swaps += cnt[x][y] < cnt[y][x] ? cnt[x][y] : cnt[y][x];
    return mism - swaps;
}

int minOperations(char* word1, char* word2) {
    int n = strlen(word1);
    const int INF = INT_MAX / 4;
    int dp[101];
    for (int i = 0; i <= n; ++i) dp[i] = INF;
    dp[0] = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            int cost = segCost(word1, word2, j, i);
            if (dp[j] + cost < dp[i]) dp[i] = dp[j] + cost;
            int revCost = 1 + revSegCost(word1, word2, j, i);
            if (dp[j] + revCost < dp[i]) dp[i] = dp[j] + revCost;
        }
    }
    return dp[n];
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinOperations(string word1, string word2) {
        int n = word1.Length;
        const int INF = 1_000_000;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int costNormal = SegmentCost(word1, word2, j, i - 1);
                int costReversed = SegmentCostReversed(word1, word2, j, i - 1);
                int segCost = Math.Min(costNormal, 1 + costReversed); // optional reverse operation
                dp[i] = Math.Min(dp[i], dp[j] + segCost);
            }
        }

        return dp[n];
    }

    private int SegmentCost(string s1, string s2, int l, int r) {
        int mismatches = 0;
        int[,] cnt = new int[26, 26];
        for (int i = l; i <= r; i++) {
            char c1 = s1[i];
            char c2 = s2[i];
            if (c1 != c2) {
                mismatches++;
                cnt[c1 - 'a', c2 - 'a']++;
            }
        }
        int swaps = 0;
        for (int x = 0; x < 26; x++) {
            for (int y = x + 1; y < 26; y++) {
                swaps += Math.Min(cnt[x, y], cnt[y, x]);
            }
        }
        return mismatches - swaps;
    }

    private int SegmentCostReversed(string s1, string s2, int l, int r) {
        int mismatches = 0;
        int[,] cnt = new int[26, 26];
        int len = r - l + 1;
        for (int idx = 0; idx < len; idx++) {
            int i = l + idx;               // position in word2
            char c1 = s1[r - idx];         // reversed character from word1
            char c2 = s2[i];
            if (c1 != c2) {
                mismatches++;
                cnt[c1 - 'a', c2 - 'a']++;
            }
        }
        int swaps = 0;
        for (int x = 0; x < 26; x++) {
            for (int y = x + 1; y < 26; y++) {
                swaps += Math.Min(cnt[x, y], cnt[y, x]);
            }
        }
        return mismatches - swaps;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minOperations = function(word1, word2) {
    const n = word1.length;
    const INF = 1e9;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    // helper to compute cost for segment [l, r)
    const segCost = (l, r) => {
        const cnt = Array.from({ length: 26 }, () => Array(26).fill(0));
        let totalMis = 0;
        for (let i = l; i < r; ++i) {
            const a = word1.charCodeAt(i) - 97;
            const b = word2.charCodeAt(i) - 97;
            if (a !== b) {
                cnt[a][b]++;
                totalMis++;
            }
        }
        let swaps = 0;
        for (let a = 0; a < 26; ++a) {
            for (let b = a + 1; b < 26; ++b) {
                const s = Math.min(cnt[a][b], cnt[b][a]);
                swaps += s;
            }
        }
        const costNormal = totalMis - swaps;

        // reversed version
        const len = r - l;
        const cntR = Array.from({ length: 26 }, () => Array(26).fill(0));
        let totalMisR = 0;
        for (let k = 0; k < len; ++k) {
            const idx = l + (len - 1 - k); // index in word1 after reversal
            const a = word1.charCodeAt(idx) - 97;
            const b = word2.charCodeAt(l + k) - 97;
            if (a !== b) {
                cntR[a][b]++;
                totalMisR++;
            }
        }
        let swapsR = 0;
        for (let a = 0; a < 26; ++a) {
            for (let b = a + 1; b < 26; ++b) {
                const s = Math.min(cntR[a][b], cntR[b][a]);
                swapsR += s;
            }
        }
        const costReversed = 1 + (totalMisR - swapsR);

        return Math.min(costNormal, costReversed);
    };

    for (let i = 1; i <= n; ++i) {
        for (let j = 0; j < i; ++j) {
            const c = segCost(j, i);
            if (dp[j] + c < dp[i]) dp[i] = dp[j] + c;
        }
    }

    return dp[n];
};
```

## Typescript

```typescript
function minOperations(word1: string, word2: string): number {
    const n = word1.length;
    const w1 = word1.split('');
    const w2 = word2.split('');
    const INF = 1e9;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    const code = (c: string) => c.charCodeAt(0) - 97;

    for (let l = 0; l < n; ++l) {
        // counts for normal orientation
        const cnt = Array.from({ length: 26 }, () => new Array(26).fill(0));
        let mismatches = 0;
        for (let r = l; r < n; ++r) {
            if (w1[r] !== w2[r]) {
                mismatches++;
                cnt[code(w1[r])][code(w2[r])]++;
            }

            // swaps without reversal
            let swaps = 0;
            for (let a = 0; a < 26; ++a) {
                for (let b = a + 1; b < 26; ++b) {
                    swaps += Math.min(cnt[a][b], cnt[b][a]);
                }
            }
            const costNoRev = mismatches - swaps;

            // compute cost with reversal
            let mismR = 0;
            const cntR = Array.from({ length: 26 }, () => new Array(26).fill(0));
            for (let p = l; p <= r; ++p) {
                const q = l + r - p; // mirrored index after reverse
                if (w1[p] !== w2[q]) {
                    mismR++;
                    cntR[code(w1[p])][code(w2[q])]++;
                }
            }
            let swapsR = 0;
            for (let a = 0; a < 26; ++a) {
                for (let b = a + 1; b < 26; ++b) {
                    swapsR += Math.min(cntR[a][b], cntR[b][a]);
                }
            }
            const costRev = 1 + (mismR - swapsR);

            const intervalCost = Math.min(costNoRev, costRev);
            dp[r + 1] = Math.min(dp[r + 1], dp[l] + intervalCost);
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function minOperations($word1, $word2) {
        $n = strlen($word1);
        $INF = 1 << 30;
        // dp[l][r] minimal operations for substring [l..r]
        $dp = array_fill(0, $n, array_fill(0, $n, $INF));

        for ($len = 1; $len <= $n; ++$len) {
            for ($l = 0; $l + $len - 1 < $n; ++$l) {
                $r = $l + $len - 1;

                // count mismatches and ordered pair frequencies
                $mismatch = 0;
                $cnt = array_fill(0, 26, array_fill(0, 26, 0));
                for ($i = $l; $i <= $r; ++$i) {
                    if ($word1[$i] !== $word2[$i]) {
                        ++$mismatch;
                        $a = ord($word1[$i]) - 97;
                        $b = ord($word2[$i]) - 97;
                        ++$cnt[$a][$b];
                    }
                }

                // maximum number of beneficial swaps
                $maxSwaps = 0;
                for ($a = 0; $a < 26; ++$a) {
                    for ($b = $a + 1; $b < 26; ++$b) {
                        $maxSwaps += min($cnt[$a][$b], $cnt[$b][$a]);
                    }
                }

                $costNoReverse = $mismatch - $maxSwaps;

                // cost if we reverse the whole segment
                $revMismatch = 0;
                for ($i = $l; $i <= $r; ++$i) {
                    $j = $r - ($i - $l); // corresponding index after reversal
                    if ($word1[$i] !== $word2[$j]) {
                        ++$revMismatch;
                    }
                }
                $costReverse = 1 + $revMismatch;

                $best = min($costNoReverse, $costReverse);

                // try splitting the segment
                for ($k = $l; $k < $r; ++$k) {
                    $candidate = $dp[$l][$k] + $dp[$k + 1][$r];
                    if ($candidate < $best) {
                        $best = $candidate;
                    }
                }

                $dp[$l][$r] = $best;
            }
        }

        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ word1: String, _ word2: String) -> Int {
        let n = word1.count
        var w1 = [Int]()
        var w2 = [Int]()
        for c in word1.utf8 { w1.append(Int(c - 97)) }
        for c in word2.utf8 { w2.append(Int(c - 97)) }

        var costNormal = Array(repeating: Array(repeating: 0, count: n), count: n)
        for l in 0..<n {
            var cnt = Array(repeating: Array(repeating: 0, count: 26), count: 26)
            var mismatches = 0
            for r in l..<n {
                let a = w1[r]
                let b = w2[r]
                if a != b {
                    mismatches += 1
                    cnt[a][b] += 1
                }
                var swaps = 0
                for x in 0..<26 {
                    for y in (x + 1)..<26 {
                        swaps += min(cnt[x][y], cnt[y][x])
                    }
                }
                costNormal[l][r] = mismatches - swaps
            }
        }

        var costReversed = Array(repeating: Array(repeating: 0, count: n), count: n)
        for l in 0..<n {
            for r in l..<n {
                let len = r - l + 1
                var cnt = Array(repeating: Array(repeating: 0, count: 26), count: 26)
                var mismatches = 0
                for offset in 0..<len {
                    let a = w1[r - offset]          // reversed segment of word1
                    let b = w2[l + offset]
                    if a != b {
                        mismatches += 1
                        cnt[a][b] += 1
                    }
                }
                var swaps = 0
                for x in 0..<26 {
                    for y in (x + 1)..<26 {
                        swaps += min(cnt[x][y], cnt[y][x])
                    }
                }
                costReversed[l][r] = mismatches - swaps
            }
        }

        let INF = Int.max / 4
        var dp = Array(repeating: INF, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            if dp[i] == INF { continue }
            for j in i..<n {
                let normal = costNormal[i][j]
                let rev = costReversed[i][j] + 1   // one extra operation to reverse
                let best = min(normal, rev)
                dp[j + 1] = min(dp[j + 1], dp[i] + best)
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(word1: String, word2: String): Int {
        val n = word1.length
        val INF = 1_000_000
        val dp = IntArray(n + 1) { INF }
        dp[0] = 0
        for (i in 1..n) {
            var best = INF
            for (j in 0 until i) {
                val len = i - j

                // without reversal
                val cnt = Array(26) { IntArray(26) }
                var total = 0
                var idx = j
                while (idx < i) {
                    val a = word1[idx] - 'a'
                    val b = word2[idx] - 'a'
                    if (a != b) {
                        cnt[a][b]++
                        total++
                    }
                    idx++
                }
                var swaps = 0
                for (x in 0 until 26) {
                    for (y in x + 1 until 26) {
                        swaps += kotlin.math.min(cnt[x][y], cnt[y][x])
                    }
                }
                val costNoRev = total - swaps
                best = kotlin.math.min(best, dp[j] + costNoRev)

                // with reversal
                val cntR = Array(26) { IntArray(26) }
                var totalR = 0
                for (offset in 0 until len) {
                    val a = word1[j + len - 1 - offset] - 'a'
                    val b = word2[j + offset] - 'a'
                    if (a != b) {
                        cntR[a][b]++
                        totalR++
                    }
                }
                var swapsR = 0
                for (x in 0 until 26) {
                    for (y in x + 1 until 26) {
                        swapsR += kotlin.math.min(cntR[x][y], cntR[y][x])
                    }
                }
                val costRev = 1 + (totalR - swapsR)
                best = kotlin.math.min(best, dp[j] + costRev)
            }
            dp[i] = best
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(String word1, String word2) {
    int n = word1.length;
    const int INF = 1 << 30;
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j <= n; ++j) {
        String s1 = word1.substring(i, j);
        String s2 = word2.substring(i, j);

        int cost = _cost(s1, s2);
        if (dp[i] + cost < dp[j]) dp[j] = dp[i] + cost;

        String revS2 = _reverse(s2);
        int costRev = _cost(s1, revS2) + 1; // one extra operation for reversal
        if (dp[i] + costRev < dp[j]) dp[j] = dp[i] + costRev;
      }
    }

    return dp[n];
  }

  int _cost(String a, String b) {
    int len = a.length;
    int mismatches = 0;
    for (int i = 0; i < len; ++i) {
      if (a[i] != b[i]) mismatches++;
    }

    List<bool> used = List.filled(len, false);
    int swaps = 0;
    for (int i = 0; i < len; ++i) {
      if (a[i] == b[i] || used[i]) continue;
      for (int j = i + 1; j < len; ++j) {
        if (used[j]) continue;
        if (a[i] == b[j] && a[j] == b[i]) {
          swaps++;
          used[i] = true;
          used[j] = true;
          break;
        }
      }
    }

    return mismatches - swaps;
  }

  String _reverse(String s) => s.split('').reversed.join();
}
```

## Golang

```go
func minOperations(word1 string, word2 string) int {
    n := len(word1)
    const INF = 1 << 30
    dp := make([]int, n+1)
    for i := range dp {
        dp[i] = INF
    }
    dp[0] = 0

    w1 := []byte(word1)
    w2 := []byte(word2)

    // compute minimal operations for substring [l..r] (inclusive)
    cost := func(l, r int) int {
        length := r - l + 1

        // without reversal
        mismatches := 0
        var cnt [26][26]int
        for i := 0; i < length; i++ {
            a := w1[l+i]
            b := w2[l+i]
            if a != b {
                mismatches++
                cnt[a-'a'][b-'a']++
            }
        }
        swaps := 0
        for x := 0; x < 26; x++ {
            for y := x + 1; y < 26; y++ {
                if cnt[x][y] < cnt[y][x] {
                    swaps += cnt[x][y]
                } else {
                    swaps += cnt[y][x]
                }
            }
        }
        best := mismatches - swaps // cost without reverse

        // with reversal (cost +1)
        mismatches = 0
        var cntR [26][26]int
        for i := 0; i < length; i++ {
            a := w1[l+length-1-i] // reversed position in word1
            b := w2[l+i]
            if a != b {
                mismatches++
                cntR[a-'a'][b-'a']++
            }
        }
        swaps = 0
        for x := 0; x < 26; x++ {
            for y := x + 1; y < 26; y++ {
                if cntR[x][y] < cntR[y][x] {
                    swaps += cntR[x][y]
                } else {
                    swaps += cntR[y][x]
                }
            }
        }
        revCost := 1 + mismatches - swaps
        if revCost < best {
            best = revCost
        }
        return best
    }

    for i := 1; i <= n; i++ {
        for j := 0; j < i; j++ {
            c := cost(j, i-1)
            if dp[j]+c < dp[i] {
                dp[i] = dp[j] + c
            }
        }
    }
    return dp[n]
}
```

## Ruby

```ruby
def min_operations(word1, word2)
  n = word1.length
  w1 = word1.chars
  w2 = word2.chars

  # compute minimal cost for substring [l..r] (inclusive)
  cost_sub = lambda do |l, r|
    mismatches = 0
    cnt = Array.new(26) { Array.new(26, 0) }

    (l..r).each do |idx|
      a = w1[idx].ord - 97
      b = w2[idx].ord - 97
      next if a == b
      mismatches += 1
      cnt[a][b] += 1
    end

    swaps = 0
    (0...26).each do |x|
      ((x + 1)...26).each do |y|
        s = [cnt[x][y], cnt[y][x]].min
        swaps += s
      end
    end
    cost_no_rev = mismatches - swaps

    # reversed version
    mismatches_r = 0
    cnt_r = Array.new(26) { Array.new(26, 0) }
    len = r - l + 1
    (0...len).each do |offset|
      a = w1[r - offset].ord - 97          # reversed char from word1 substring
      b = w2[l + offset].ord - 97           # corresponding target position
      next if a == b
      mismatches_r += 1
      cnt_r[a][b] += 1
    end

    swaps_r = 0
    (0...26).each do |x|
      ((x + 1)...26).each do |y|
        s = [cnt_r[x][y], cnt_r[y][x]].min
        swaps_r += s
      end
    end
    cost_rev = 1 + mismatches_r - swaps_r

    [cost_no_rev, cost_rev].min
  end

  dp = Array.new(n + 1, Float::INFINITY)
  dp[0] = 0
  (1..n).each do |i|
    (0...i).each do |j|
      c = cost_sub.call(j, i - 1)
      val = dp[j] + c
      dp[i] = val if val < dp[i]
    end
  end
  dp[n].to_i
end
```

## Scala

```scala
object Solution {
    def minOperations(word1: String, word2: String): Int = {
        val n = word1.length
        val a = word1.toCharArray
        val b = word2.toCharArray
        val INF = 1 << 30
        val dp = Array.fill(n + 1)(INF)
        dp(0) = 0

        for (i <- 1 to n) {
            var j = 0
            while (j < i) {
                val costNoRev = segmentCost(a, b, j, i, rev = false)
                if (dp(j) + costNoRev < dp(i)) dp(i) = dp(j) + costNoRev

                val costWithRev = segmentCost(a, b, j, i, rev = true) + 1
                if (dp(j) + costWithRev < dp(i)) dp(i) = dp(j) + costWithRev

                j += 1
            }
        }
        dp(n)
    }

    private def segmentCost(s1: Array[Char], s2: Array[Char], l: Int, r: Int, rev: Boolean): Int = {
        val cnt = Array.ofDim[Int](26, 26)
        var mismatches = 0
        if (!rev) {
            var k = l
            while (k < r) {
                val a = s1(k) - 'a'
                val b = s2(k) - 'a'
                if (a != b) {
                    cnt(a)(b) += 1
                    mismatches += 1
                }
                k += 1
            }
        } else {
            var pos = l
            while (pos < r) {
                val a = s1(r - 1 - (pos - l)) - 'a'
                val b = s2(pos) - 'a'
                if (a != b) {
                    cnt(a)(b) += 1
                    mismatches += 1
                }
                pos += 1
            }
        }

        var swaps = 0
        var c1 = 0
        while (c1 < 26) {
            var c2 = c1 + 1
            while (c2 < 26) {
                val s = math.min(cnt(c1)(c2), cnt(c2)(c1))
                swaps += s
                c2 += 1
            }
            c1 += 1
        }

        mismatches - swaps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(word1: String, word2: String) -> i32 {
        let w1 = word1.as_bytes();
        let w2 = word2.as_bytes();
        let n = w1.len();
        // cost[l][r]: minimal operations to transform substring [l..=r] as a single block
        let mut cost = vec![vec![0i32; n]; n];
        for l in 0..n {
            for r in l..n {
                let len = r - l + 1;
                // original orientation
                let mut mismatches = 0usize;
                let mut cnt = [[0usize; 26]; 26];
                for idx in 0..len {
                    let pos = l + idx;
                    let a = (w1[pos] - b'a') as usize;
                    let b = (w2[l + idx] - b'a') as usize;
                    if a != b {
                        mismatches += 1;
                        cnt[a][b] += 1;
                    }
                }
                let mut swaps = 0usize;
                for x in 0..26 {
                    for y in (x + 1)..26 {
                        swaps += std::cmp::min(cnt[x][y], cnt[y][x]);
                    }
                }
                let cost_orig = mismatches - swaps;

                // reversed orientation (includes one reverse operation)
                let mut mismatches_r = 0usize;
                let mut cnt_r = [[0usize; 26]; 26];
                for idx in 0..len {
                    let pos = r - idx;
                    let a = (w1[pos] - b'a') as usize;
                    let b = (w2[l + idx] - b'a') as usize;
                    if a != b {
                        mismatches_r += 1;
                        cnt_r[a][b] += 1;
                    }
                }
                let mut swaps_r = 0usize;
                for x in 0..26 {
                    for y in (x + 1)..26 {
                        swaps_r += std::cmp::min(cnt_r[x][y], cnt_r[y][x]);
                    }
                }
                let cost_rev = 1 + (mismatches_r - swaps_r);

                cost[l][r] = std::cmp::min(cost_orig, cost_rev) as i32;
            }
        }

        // DP over partitions
        let mut dp = vec![i32::MAX / 2; n + 1];
        dp[0] = 0;
        for i in 1..=n {
            for j in 0..i {
                let cur = dp[j] + cost[j][i - 1];
                if cur < dp[i] {
                    dp[i] = cur;
                }
            }
        }
        dp[n]
    }
}
```

## Racket

```racket
(define (min-operations word1 word2)
  (let* ([n (string-length word1)]
         [v1 (make-vector n)]
         [v2 (make-vector n)])
    (for ([i (in-range n)])
      (vector-set! v1 i (string-ref word1 i))
      (vector-set! v2 i (string-ref word2 i)))
    ;; prefix mismatches
    (define pref (make-vector (+ n 1) 0))
    (for ([i (in-range n)])
      (let* ([prev (vector-ref pref i)]
             [add (if (char=? (vector-ref v1 i) (vector-ref v2 i)) 0 1)])
        (vector-set! pref (+ i 1) (+ prev add))))
    (define (mismatch l r)
      (- (vector-ref pref (+ r 1)) (vector-ref pref l)))
    ;; precompute swapable pairs
    (define swap-pairs '())
    (for ([i (in-range n)])
      (for ([j (in-range (+ i 1) n)])
        (when (and (char=? (vector-ref v1 i) (vector-ref v2 j))
                   (char=? (vector-ref v1 j) (vector-ref v2 i)))
          (set! swap-pairs (cons (list i j) swap-pairs)))))
    ;; dp matrix
    (define dp (make-vector n))
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector n 0)))
    (define (reverse-match? l r)
      (let loop ((k 0) (len (+ 1 (- r l))))
        (if (= k len)
            #t
            (and (char=? (vector-ref v1 (- r k)) (vector-ref v2 (+ l k)))
                 (loop (+ k 1) len)))))
    ;; DP over intervals
    (for ([len (in-range 1 (+ n 1))])
      (for ([l (in-range 0 (+ 1 (- n len)))])
        (let* ([r (+ l (- len 1))]
               [row (vector-ref dp l)]
               [initial (mismatch l r)])
          ;; start with replace-all cost
          (define best initial)
          ;; reverse operation
          (when (reverse-match? l r)
            (set! best (min best 1)))
          ;; split into two parts
          (for ([k (in-range l r)])
            (let* ([left (vector-ref (vector-ref dp l) k)]
                   [right (vector-ref (vector-ref dp (+ k 1)) r)]
                   [cand (+ left right)])
              (when (< cand best)
                (set! best cand))))
          ;; swap pairs
          (for ([pair swap-pairs])
            (define i (first pair))
            (define j (second pair))
            (when (and (>= i l) (<= j r))
              (let* ([left (if (> i l) (vector-ref (vector-ref dp l) (- i 1)) 0)]
                     [mid (if (< (+ i 1) j) (vector-ref (vector-ref dp (+ i 1)) (- j 1)) 0)]
                     [right (if (< j r) (vector-ref (vector-ref dp (+ j 1)) r) 0)]
                     [cand (+ 1 left mid right)])
                (when (< cand best)
                  (set! best cand)))))
          (vector-set! row r best))))
    (vector-ref (vector-ref dp 0) (- n 1))))
```

## Erlang

```erlang
-spec min_operations(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
min_operations(Word1, Word2) ->
    W1List = unicode:characters_to_list(Word1),
    W2List = unicode:characters_to_list(Word2),
    W1T = list_to_tuple(W1List),
    W2T = list_to_tuple(W2List),
    N = tuple_size(W1T),
    Max = 1 bsl 30,
    DP0 = array:new(N + 1, [{default, Max}]),
    DP1 = array:set(0, 0, DP0),
    DP = fill_dp(1, N, W1T, W2T, DP1, Max),
    array:get(N, DP).

fill_dp(I, N, _W1T, _W2T, DP, _Max) when I > N ->
    DP;
fill_dp(I, N, W1T, W2T, DPAcc, Max) ->
    Best = best_for_i(0, I - 1, I - 1, W1T, W2T, DPAcc, Max),
    DPNext = array:set(I, Best, DPAcc),
    fill_dp(I + 1, N, W1T, W2T, DPNext, Max).

best_for_i(J, EndJ, R, _W1T, _W2T, _DP, Best) when J > EndJ ->
    Best;
best_for_i(J, EndJ, R, W1T, W2T, DP, Best) ->
    Cost = interval_cost(J, R, W1T, W2T),
    Prev = array:get(J, DP),
    NewVal = Prev + Cost,
    NewBest = if NewVal < Best -> NewVal; true -> Best end,
    best_for_i(J + 1, EndJ, R, W1T, W2T, DP, NewBest).

interval_cost(L, R, W1T, W2T) ->
    Len = R - L + 1,
    {Mis, CntMap} = mismatches_and_counts(L, R, W1T, W2T, #{}, 0),
    Swaps = count_swaps(CntMap),
    CostNoRev = Mis - Swaps,
    {MisR, CntMapR} = mismatches_and_counts_rev(L, R, W1T, W2T, #{}, 0),
    SwapsR = count_swaps(CntMapR),
    CostRev = 1 + MisR - SwapsR,
    erlang:min(CostNoRev, CostRev).

mismatches_and_counts(PosL, PosR, W1T, W2T, Map, AccMis) when PosL > PosR ->
    {AccMis, Map};
mismatches_and_counts(PosL, PosR, W1T, W2T, Map, AccMis) ->
    X = element(PosL + 1, W1T),
    Y = element(PosL + 1, W2T),
    case X =:= Y of
        true -> mismatches_and_counts(PosL + 1, PosR, W1T, W2T, Map, AccMis);
        false ->
            NewMap = maps:update_with({X, Y},
                                      fun(C) -> C + 1 end,
                                      1,
                                      Map),
            mismatches_and_counts(PosL + 1, PosR, W1T, W2T, NewMap, AccMis + 1)
    end.

mismatches_and_counts_rev(L, R, W1T, W2T, Map, AccMis) ->
    mismatches_and_counts_rev_loop(0, R - L, L, R, W1T, W2T, Map, AccMis).

mismatches_and_counts_rev_loop(I, LenMinusOne, L, R, _W1T, _W2T, Map, AccMis) when I > LenMinusOne ->
    {AccMis, Map};
mismatches_and_counts_rev_loop(I, LenMinusOne, L, R, W1T, W2T, Map, AccMis) ->
    X = element(R - I + 1, W1T),
    Y = element(L + I + 1, W2T),
    case X =:= Y of
        true -> mismatches_and_counts_rev_loop(I + 1, LenMinusOne, L, R, W1T, W2T, Map, AccMis);
        false ->
            NewMap = maps:update_with({X, Y},
                                      fun(C) -> C + 1 end,
                                      1,
                                      Map),
            mismatches_and_counts_rev_loop(I + 1, LenMinusOne, L, R, W1T, W2T, NewMap, AccMis + 1)
    end.

count_swaps(Map) ->
    count_swaps(0, 25, Map, 0).

count_swaps(X, MaxX, _Map, Sw) when X > MaxX ->
    Sw;
count_swaps(X, MaxX, Map, Sw) ->
    Sw1 = count_swaps_y(X, X + 1, 25, Map, Sw),
    count_swaps(X + 1, MaxX, Map, Sw1).

count_swaps_y(_X, Y, MaxY, _Map, Sw) when Y > MaxY ->
    Sw;
count_swaps_y(X, Y, MaxY, Map, Sw) ->
    Cxy = maps:get({X, Y}, Map, 0),
    Cyx = maps:get({Y, X}, Map, 0),
    NewSw = Sw + erlang:min(Cxy, Cyx),
    count_swaps_y(X, Y + 1, MaxY, Map, NewSw).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(word1 :: String.t(), word2 :: String.t()) :: integer()
  def min_operations(word1, word2) do
    a = String.graphemes(word1) |> List.to_tuple()
    b = String.graphemes(word2) |> List.to_tuple()
    n = tuple_size(a)

    # prefix mismatches
    pref_list =
      Enum.reduce(0..(n - 1), [0], fn i, acc ->
        mismatch = if elem(a, i) != elem(b, i), do: 1, else: 0
        [hd(acc) + mismatch | acc]
      end)
      |> Enum.reverse()

    pref = List.to_tuple(pref_list)

    # DP for max swaps on original strings
    dp_swap_orig = build_max_swaps(a, b, n)

    # reversed strings
    a_rev = a |> Tuple.to_list() |> :lists.reverse() |> List.to_tuple()
    b_rev = b |> Tuple.to_list() |> :lists.reverse() |> List.to_tuple()
    dp_swap_rev = build_max_swaps(a_rev, b_rev, n)

    # Main DP for minimal operations with possible splits
    dp =
      Enum.reduce(1..n, %{}, fn len, acc ->
        Enum.reduce(0..(n - len), acc, fn l, acc2 ->
          r = l + len - 1

          mismatches = elem(pref, r + 1) - elem(pref, l)

          swaps = Map.get(dp_swap_orig, {l, r}, 0)
          remaining = mismatches - 2 * swaps
          cost_direct = swaps + if remaining > 0, do: 1, else: 0

          # corresponding interval in reversed strings
          rl = n - 1 - r
          rr = n - 1 - l
          swaps_rev = Map.get(dp_swap_rev, {rl, rr}, 0)
          remaining_rev = mismatches - 2 * swaps_rev
          cost_rev = 1 + swaps_rev + if remaining_rev > 0, do: 1, else: 0

          best = min(cost_direct, cost_rev)

          # try all possible splits
          best =
            Enum.reduce(l..(r - 1), best, fn k, cur_best ->
              left = Map.get(acc2, {l, k})
              right = Map.get(acc2, {k + 1, r})
              cand = left + right
              if cand < cur_best, do: cand, else: cur_best
            end)

          Map.put(acc2, {l, r}, best)
        end)
      end)

    Map.get(dp, {0, n - 1})
  end

  # Helper to compute maximum number of disjoint swap pairs for all intervals
  defp build_max_swaps(a, b, n) do
    Enum.reduce(1..n, %{}, fn len, acc ->
      Enum.reduce(0..(n - len), acc, fn l, acc2 ->
        r = l + len - 1

        # option: skip position l
        best =
          if l + 1 <= r do
            Map.get(acc2, {l + 1, r}, 0)
          else
            0
          end

        best =
          Enum.reduce((l + 1)..r, best, fn j, cur_best ->
            if elem(a, l) == elem(b, j) and elem(a, j) == elem(b, l) do
              left = if l + 1 <= j - 1, do: Map.get(acc2, {l + 1, j - 1}, 0), else: 0
              right = if j + 1 <= r, do: Map.get(acc2, {j + 1, r}, 0), else: 0
              cand = 1 + left + right
              if cand > cur_best, do: cand, else: cur_best
            else
              cur_best
            end
          end)

        Map.put(acc2, {l, r}, best)
      end)
    end)
  end
end
```
