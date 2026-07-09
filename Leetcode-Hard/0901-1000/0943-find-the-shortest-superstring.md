# 0943. Find the Shortest Superstring

## Cpp

```cpp
class Solution {
public:
    string shortestSuperstring(vector<string>& words) {
        int n = words.size();
        if (n == 0) return "";
        // compute overlap lengths
        vector<vector<int>> overlap(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) if (i != j) {
                int max_ol = min(words[i].size(), words[j].size());
                for (int k = max_ol; k > 0; --k) {
                    if (words[i].compare(words[i].size() - k, k, words[j], 0, k) == 0) {
                        overlap[i][j] = k;
                        break;
                    }
                }
            }
        }
        int N = 1 << n;
        const int INF = 1e9;
        vector<vector<int>> dp(N, vector<int>(n, INF));
        vector<vector<int>> parent(N, vector<int>(n, -1));
        for (int i = 0; i < n; ++i) {
            dp[1 << i][i] = words[i].size();
        }
        for (int mask = 0; mask < N; ++mask) {
            for (int last = 0; last < n; ++last) if (mask & (1 << last)) {
                int curLen = dp[mask][last];
                if (curLen == INF) continue;
                for (int nxt = 0; nxt < n; ++nxt) if (!(mask & (1 << nxt))) {
                    int nextMask = mask | (1 << nxt);
                    int cand = curLen + (int)words[nxt].size() - overlap[last][nxt];
                    if (cand < dp[nextMask][nxt]) {
                        dp[nextMask][nxt] = cand;
                        parent[nextMask][nxt] = last;
                    }
                }
            }
        }
        int fullMask = N - 1;
        int bestLen = INF, lastIdx = -1;
        for (int i = 0; i < n; ++i) {
            if (dp[fullMask][i] < bestLen) {
                bestLen = dp[fullMask][i];
                lastIdx = i;
            }
        }
        // reconstruct path
        vector<int> order;
        int mask = fullMask, cur = lastIdx;
        while (cur != -1) {
            order.push_back(cur);
            int prev = parent[mask][cur];
            mask ^= (1 << cur);
            cur = prev;
        }
        reverse(order.begin(), order.end());
        // build result string
        string res = words[order[0]];
        for (size_t i = 1; i < order.size(); ++i) {
            int o = overlap[order[i-1]][order[i]];
            res += words[order[i]].substr(o);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String shortestSuperstring(String[] words) {
        int n = words.length;
        if (n == 1) return words[0];
        
        // Compute overlaps
        int[][] overlap = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                overlap[i][j] = calcOverlap(words[i], words[j]);
            }
        }
        
        int N = 1 << n;
        int INF = Integer.MAX_VALUE / 2;
        int[][] dp = new int[N][n];
        int[][] parent = new int[N][n];
        for (int[] row : dp) Arrays.fill(row, INF);
        for (int i = 0; i < n; i++) {
            dp[1 << i][i] = words[i].length();
            parent[1 << i][i] = -1;
        }
        
        for (int mask = 0; mask < N; mask++) {
            for (int last = 0; last < n; last++) {
                if ((mask & (1 << last)) == 0) continue;
                int curLen = dp[mask][last];
                if (curLen == INF) continue;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((mask & (1 << nxt)) != 0) continue;
                    int nextMask = mask | (1 << nxt);
                    int cand = curLen + words[nxt].length() - overlap[last][nxt];
                    if (cand < dp[nextMask][nxt]) {
                        dp[nextMask][nxt] = cand;
                        parent[nextMask][nxt] = last;
                    }
                }
            }
        }
        
        // Find best ending word
        int fullMask = N - 1;
        int minLen = INF;
        int lastWord = -1;
        for (int i = 0; i < n; i++) {
            if (dp[fullMask][i] < minLen) {
                minLen = dp[fullMask][i];
                lastWord = i;
            }
        }
        
        // Reconstruct path
        List<Integer> order = new ArrayList<>();
        int mask = fullMask;
        int cur = lastWord;
        while (cur != -1) {
            order.add(cur);
            int prev = parent[mask][cur];
            mask ^= (1 << cur);
            cur = prev;
        }
        Collections.reverse(order);
        
        // Build result string
        StringBuilder sb = new StringBuilder(words[order.get(0)]);
        for (int i = 1; i < order.size(); i++) {
            int a = order.get(i - 1);
            int b = order.get(i);
            sb.append(words[b].substring(overlap[a][b]));
        }
        return sb.toString();
    }
    
    private int calcOverlap(String a, String b) {
        int max = Math.min(a.length(), b.length());
        for (int k = max; k >= 0; k--) {
            if (a.endsWith(b.substring(0, k))) {
                return k;
            }
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        # compute overlap[i][j]: max length that suffix of i matches prefix of j
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = words[i], words[j]
                max_olap = min(len(a), len(b))
                # find largest k where a[-k:] == b[:k]
                for k in range(max_olap, 0, -1):
                    if a.endswith(b[:k]):
                        overlap[i][j] = k
                        break

        full_mask = (1 << n) - 1
        INF = float('inf')
        dp = [[INF] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = len(words[i])

        for mask in range(1 << n):
            for last in range(n):
                if not (mask & (1 << last)):
                    continue
                cur_len = dp[mask][last]
                if cur_len == INF:
                    continue
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    next_mask = mask | (1 << nxt)
                    cand = cur_len + len(words[nxt]) - overlap[last][nxt]
                    if cand < dp[next_mask][nxt]:
                        dp[next_mask][nxt] = cand
                        parent[next_mask][nxt] = last

        # find end word giving minimal length
        min_len = INF
        last = -1
        for i in range(n):
            if dp[full_mask][i] < min_len:
                min_len = dp[full_mask][i]
                last = i

        # reconstruct order
        mask = full_mask
        order = []
        while last != -1:
            order.append(last)
            prev = parent[mask][last]
            mask ^= (1 << last)
            last = prev
        order.reverse()

        # build result string using overlaps
        res = words[order[0]]
        for i in range(1, len(order)):
            o = overlap[order[i-1]][order[i]]
            res += words[order[i]][o:]
        return res
```

## Python3

```python
import sys
from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        # compute overlap lengths
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = words[i], words[j]
                max_olap = min(len(a), len(b))
                # find maximum k where suffix of a matches prefix of b
                for k in range(max_olap, 0, -1):
                    if a[-k:] == b[:k]:
                        overlap[i][j] = k
                        break

        # cost to add j after i
        add_len = [[len(words[j]) - overlap[i][j] for j in range(n)] for i in range(n)]

        INF = sys.maxsize
        dp = [[INF] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = len(words[i])

        for mask in range(1, 1 << n):
            for last in range(n):
                if not (mask & (1 << last)):
                    continue
                prev_mask = mask ^ (1 << last)
                if prev_mask == 0:
                    continue
                # try all possible previous words
                best_prev = -1
                best_val = INF
                for k in range(n):
                    if not (prev_mask & (1 << k)):
                        continue
                    val = dp[prev_mask][k] + add_len[k][last]
                    if val < best_val:
                        best_val = val
                        best_prev = k
                if best_val < dp[mask][last]:
                    dp[mask][last] = best_val
                    parent[mask][last] = best_prev

        # find end word with minimal total length
        full_mask = (1 << n) - 1
        min_len = INF
        last_word = -1
        for i in range(n):
            if dp[full_mask][i] < min_len:
                min_len = dp[full_mask][i]
                last_word = i

        # reconstruct path
        order = []
        mask = full_mask
        cur = last_word
        while cur != -1:
            order.append(cur)
            prev = parent[mask][cur]
            mask ^= (1 << cur)
            cur = prev
        order.reverse()

        # build superstring from order
        res = words[order[0]]
        for i in range(1, len(order)):
            o = overlap[order[i-1]][order[i]]
            res += words[order[i]][o:]
        return res
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

char* shortestSuperstring(char** words, int wordsSize) {
    int n = wordsSize;
    if (n == 0) return NULL;

    int len[12];
    for (int i = 0; i < n; ++i) len[i] = strlen(words[i]);

    // compute overlaps
    int ov[12][12];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) { ov[i][j] = 0; continue; }
            int maxk = len[i] < len[j] ? len[i] : len[j];
            int k;
            for (k = maxk; k > 0; --k) {
                if (strncmp(words[i] + len[i] - k, words[j], k) == 0) break;
            }
            ov[i][j] = k;
        }
    }

    int fullMask = (1 << n) - 1;
    static int dp[1 << 12][12];
    static int parent[1 << 12][12];

    for (int mask = 0; mask <= fullMask; ++mask)
        for (int i = 0; i < n; ++i)
            dp[mask][i] = INT_MAX / 2, parent[mask][i] = -1;

    // DP over subsets
    for (int mask = 1; mask <= fullMask; ++mask) {
        for (int i = 0; i < n; ++i) if (mask & (1 << i)) {
            int prevMask = mask ^ (1 << i);
            if (prevMask == 0) {
                dp[mask][i] = len[i];
                parent[mask][i] = -1;
            } else {
                for (int j = 0; j < n; ++j) if (prevMask & (1 << j)) {
                    int cand = dp[prevMask][j] + len[i] - ov[j][i];
                    if (cand < dp[mask][i]) {
                        dp[mask][i] = cand;
                        parent[mask][i] = j;
                    }
                }
            }
        }
    }

    // find best ending word
    int minLen = INT_MAX, last = -1;
    for (int i = 0; i < n; ++i) {
        if (dp[fullMask][i] < minLen) {
            minLen = dp[fullMask][i];
            last = i;
        }
    }

    // reconstruct order
    int order[12];
    int idx = n - 1;
    int mask = fullMask;
    int cur = last;
    while (cur != -1) {
        order[idx--] = cur;
        int prev = parent[mask][cur];
        mask ^= (1 << cur);
        cur = prev;
    }

    // build result string
    char* res = (char*)malloc(minLen + 1);
    int pos = 0;
    strcpy(res, words[order[0]]);
    pos = len[order[0]];
    for (int k = 1; k < n; ++k) {
        int iPrev = order[k - 1];
        int iCurr = order[k];
        int o = ov[iPrev][iCurr];
        const char* w = words[iCurr];
        int l = len[iCurr];
        memcpy(res + pos, w + o, l - o);
        pos += l - o;
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ShortestSuperstring(string[] words) {
        int n = words.Length;
        if (n == 1) return words[0];

        // Compute overlaps
        int[,] overlap = new int[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int maxLen = Math.Min(words[i].Length, words[j].Length);
                for (int k = maxLen; k > 0; k--) {
                    if (words[i].EndsWith(words[j].Substring(0, k))) {
                        overlap[i, j] = k;
                        break;
                    }
                }
            }
        }

        int size = 1 << n;
        int[,] dp = new int[size, n];
        int[,] parent = new int[size, n];
        for (int mask = 0; mask < size; mask++) {
            for (int i = 0; i < n; i++) {
                dp[mask, i] = -1;
                parent[mask, i] = -1;
            }
        }

        // Initialize DP
        for (int i = 0; i < n; i++) {
            dp[1 << i, i] = 0;
        }

        // DP over subsets
        for (int mask = 0; mask < size; mask++) {
            for (int last = 0; last < n; last++) {
                if ((mask & (1 << last)) == 0) continue;
                int curVal = dp[mask, last];
                if (curVal < 0) continue;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((mask & (1 << nxt)) != 0) continue;
                    int nextMask = mask | (1 << nxt);
                    int val = curVal + overlap[last, nxt];
                    if (val > dp[nextMask, nxt]) {
                        dp[nextMask, nxt] = val;
                        parent[nextMask, nxt] = last;
                    }
                }
            }
        }

        // Find best ending word
        int finalMask = size - 1;
        int bestEnd = -1;
        int bestOverlap = -1;
        for (int i = 0; i < n; i++) {
            if (dp[finalMask, i] > bestOverlap) {
                bestOverlap = dp[finalMask, i];
                bestEnd = i;
            }
        }

        // Reconstruct path
        List<int> path = new List<int>();
        int maskCur = finalMask;
        int cur = bestEnd;
        while (cur != -1) {
            path.Add(cur);
            int prev = parent[maskCur, cur];
            maskCur ^= 1 << cur;
            cur = prev;
        }
        path.Reverse();

        // Build result string
        StringBuilder sb = new StringBuilder();
        sb.Append(words[path[0]]);
        for (int i = 1; i < path.Count; i++) {
            int a = path[i - 1];
            int b = path[i];
            sb.Append(words[b].Substring(overlap[a, b]));
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var shortestSuperstring = function(words) {
    const n = words.length;
    // compute overlap[i][j]: max suffix of words[i] that matches prefix of words[j]
    const overlap = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            const a = words[i];
            const b = words[j];
            const maxLen = Math.min(a.length, b.length);
            let best = 0;
            for (let k = maxLen; k > 0; --k) {
                if (a.slice(a.length - k) === b.slice(0, k)) {
                    best = k;
                    break;
                }
            }
            overlap[i][j] = best;
        }
    }

    const size = 1 << n;
    const dp = Array.from({ length: size }, () => Array(n).fill(Infinity));
    const parent = Array.from({ length: size }, () => Array(n).fill(-1));

    // initialize
    for (let i = 0; i < n; ++i) {
        dp[1 << i][i] = words[i].length;
    }

    for (let mask = 0; mask < size; ++mask) {
        for (let last = 0; last < n; ++last) {
            if (!(mask & (1 << last))) continue;
            const curLen = dp[mask][last];
            if (curLen === Infinity) continue;
            for (let nxt = 0; nxt < n; ++nxt) {
                if (mask & (1 << nxt)) continue;
                const nextMask = mask | (1 << nxt);
                const candLen = curLen + words[nxt].length - overlap[last][nxt];
                if (candLen < dp[nextMask][nxt]) {
                    dp[nextMask][nxt] = candLen;
                    parent[nextMask][nxt] = last;
                }
            }
        }
    }

    // find best ending word
    let finalMask = size - 1;
    let end = 0;
    let minLen = Infinity;
    for (let i = 0; i < n; ++i) {
        if (dp[finalMask][i] < minLen) {
            minLen = dp[finalMask][i];
            end = i;
        }
    }

    // reconstruct path
    const path = [];
    let mask = finalMask;
    let cur = end;
    while (cur !== -1) {
        path.push(cur);
        const prev = parent[mask][cur];
        mask ^= (1 << cur);
        cur = prev;
    }
    path.reverse();

    // build superstring
    let result = words[path[0]];
    for (let i = 1; i < path.length; ++i) {
        const a = path[i - 1];
        const b = path[i];
        const ov = overlap[a][b];
        result += words[b].substring(ov);
    }
    return result;
};
```

## Typescript

```typescript
function shortestSuperstring(words: string[]): string {
    const n = words.length;
    if (n === 0) return "";
    // compute overlap
    const overlap: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            const a = words[i];
            const b = words[j];
            const maxLen = Math.min(a.length, b.length);
            for (let k = maxLen; k >= 0; --k) {
                if (a.endsWith(b.substring(0, k))) {
                    overlap[i][j] = k;
                    break;
                }
            }
        }
    }

    const size = 1 << n;
    const dp: number[][] = Array.from({ length: size }, () => Array(n).fill(-Infinity));
    const parent: number[][] = Array.from({ length: size }, () => Array(n).fill(-1));

    for (let i = 0; i < n; ++i) {
        dp[1 << i][i] = 0;
    }

    for (let mask = 0; mask < size; ++mask) {
        for (let last = 0; last < n; ++last) {
            if ((mask & (1 << last)) === 0) continue;
            const curVal = dp[mask][last];
            if (curVal === -Infinity) continue;
            for (let nxt = 0; nxt < n; ++nxt) {
                if (mask & (1 << nxt)) continue;
                const nextMask = mask | (1 << nxt);
                const val = curVal + overlap[last][nxt];
                if (val > dp[nextMask][nxt]) {
                    dp[nextMask][nxt] = val;
                    parent[nextMask][nxt] = last;
                }
            }
        }
    }

    let fullMask = size - 1;
    let bestEnd = 0;
    let bestOverlap = -Infinity;
    for (let i = 0; i < n; ++i) {
        if (dp[fullMask][i] > bestOverlap) {
            bestOverlap = dp[fullMask][i];
            bestEnd = i;
        }
    }

    // reconstruct path
    const order: number[] = [];
    let mask = fullMask;
    let cur = bestEnd;
    while (cur !== -1) {
        order.push(cur);
        const prev = parent[mask][cur];
        mask ^= 1 << cur;
        cur = prev;
    }
    order.reverse();

    // build result string
    let res = words[order[0]];
    for (let i = 1; i < order.length; ++i) {
        const a = order[i - 1];
        const b = order[i];
        res += words[b].substring(overlap[a][b]);
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function shortestSuperstring($words) {
        $n = count($words);
        // Precompute overlaps and costs
        $overlap = array_fill(0, $n, array_fill(0, $n, 0));
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i == $j) continue;
                $a = $words[$i];
                $b = $words[$j];
                $max = min(strlen($a), strlen($b));
                $ov = 0;
                for ($k = $max; $k > 0; $k--) {
                    if (substr($a, -$k) === substr($b, 0, $k)) {
                        $ov = $k;
                        break;
                    }
                }
                $overlap[$i][$j] = $ov;
                $cost[$i][$j] = strlen($b) - $ov;
            }
        }

        $fullMask = (1 << $n) - 1;
        $INF = PHP_INT_MAX;

        // dp[mask][last] = minimal length
        $dp = array_fill(0, $fullMask + 1, array_fill(0, $n, $INF));
        $parent = array_fill(0, $fullMask + 1, array_fill(0, $n, -1));

        for ($i = 0; $i < $n; $i++) {
            $mask = 1 << $i;
            $dp[$mask][$i] = strlen($words[$i]);
        }

        for ($mask = 1; $mask <= $fullMask; $mask++) {
            for ($last = 0; $last < $n; $last++) {
                if (!($mask & (1 << $last))) continue;
                $curLen = $dp[$mask][$last];
                if ($curLen == $INF) continue;
                for ($next = 0; $next < $n; $next++) {
                    if ($mask & (1 << $next)) continue;
                    $nextMask = $mask | (1 << $next);
                    $newLen = $curLen + $cost[$last][$next];
                    if ($newLen < $dp[$nextMask][$next]) {
                        $dp[$nextMask][$next] = $newLen;
                        $parent[$nextMask][$next] = $last;
                    }
                }
            }
        }

        // Find best ending word
        $minLen = $INF;
        $lastWord = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$fullMask][$i] < $minLen) {
                $minLen = $dp[$fullMask][$i];
                $lastWord = $i;
            }
        }

        // Reconstruct order
        $order = [];
        $mask = $fullMask;
        $cur = $lastWord;
        while ($cur != -1) {
            array_unshift($order, $cur);
            $prev = $parent[$mask][$cur];
            $mask ^= (1 << $cur);
            $cur = $prev;
        }

        // Build result string
        $result = $words[$order[0]];
        for ($i = 1; $i < count($order); $i++) {
            $prevIdx = $order[$i - 1];
            $currIdx = $order[$i];
            $ov = $overlap[$prevIdx][$currIdx];
            $result .= substr($words[$currIdx], $ov);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func shortestSuperstring(_ words: [String]) -> String {
        let n = words.count
        if n == 0 { return "" }
        if n == 1 { return words[0] }

        // Convert words to character arrays for fast indexing
        let wordChars = words.map { Array($0) }

        // Precompute extra characters needed when appending j after i
        var extra = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n where i != j {
                let a = wordChars[i]
                let b = wordChars[j]
                let maxOverlap = computeMaxOverlap(a, b)
                extra[i][j] = b.count - maxOverlap
            }
        }

        let fullMask = (1 << n) - 1
        let INF = Int.max / 4

        var dp = Array(repeating: Array(repeating: INF, count: n), count: 1 << n)
        var parent = Array(repeating: Array(repeating: -1, count: n), count: 1 << n)

        for i in 0..<n {
            dp[1 << i][i] = wordChars[i].count
        }

        if n > 1 {
            for mask in 0...fullMask {
                for last in 0..<n where (mask & (1 << last)) != 0 {
                    let curLen = dp[mask][last]
                    if curLen == INF { continue }
                    for nxt in 0..<n where (mask & (1 << nxt)) == 0 {
                        let nextMask = mask | (1 << nxt)
                        let cand = curLen + extra[last][nxt]
                        if cand < dp[nextMask][nxt] {
                            dp[nextMask][nxt] = cand
                            parent[nextMask][nxt] = last
                        }
                    }
                }
            }
        }

        // Find the ending word with minimal total length
        var minLen = INF
        var lastIdx = -1
        for i in 0..<n {
            if dp[fullMask][i] < minLen {
                minLen = dp[fullMask][i]
                lastIdx = i
            }
        }

        // Reconstruct order of words
        var mask = fullMask
        var cur = lastIdx
        var order: [Int] = []
        while cur != -1 {
            order.append(cur)
            let prev = parent[mask][cur]
            mask ^= (1 << cur)
            cur = prev
        }
        order.reverse()

        // Build the final superstring using the computed overlaps
        var result = words[order[0]]
        for k in 1..<order.count {
            let iPrev = order[k - 1]
            let j = order[k]
            let overlapLen = wordChars[j].count - extra[iPrev][j]   // length of overlapping part
            let suffix = String(words[j].dropFirst(overlapLen))
            result += suffix
        }
        return result
    }

    private func computeMaxOverlap(_ a: [Character], _ b: [Character]) -> Int {
        let maxPossible = min(a.count, b.count)
        if maxPossible == 0 { return 0 }
        for k in stride(from: maxPossible, through: 1, by: -1) {
            var match = true
            for i in 0..<k {
                if a[a.count - k + i] != b[i] {
                    match = false
                    break
                }
            }
            if match { return k }
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestSuperstring(words: Array<String>): String {
        val n = words.size
        if (n == 1) return words[0]

        // Compute overlap lengths
        val overlap = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i == j) continue
                val a = words[i]
                val b = words[j]
                val maxLen = minOf(a.length, b.length)
                var best = 0
                for (k in maxLen downTo 1) {
                    if (a.endsWith(b.substring(0, k))) {
                        best = k
                        break
                    }
                }
                overlap[i][j] = best
            }
        }

        val totalMask = 1 shl n
        val INF = Int.MAX_VALUE / 4
        val dp = Array(totalMask) { IntArray(n) { INF } }
        val parent = Array(totalMask) { IntArray(n) { -1 } }

        // Initialize DP with single words
        for (i in 0 until n) {
            dp[1 shl i][i] = words[i].length
        }

        // DP over subsets
        for (mask in 1 until totalMask) {
            for (last in 0 until n) {
                if ((mask and (1 shl last)) == 0) continue
                val curLen = dp[mask][last]
                if (curLen == INF) continue
                for (next in 0 until n) {
                    if ((mask and (1 shl next)) != 0) continue
                    val nextMask = mask or (1 shl next)
                    val cand = curLen + words[next].length - overlap[last][next]
                    if (cand < dp[nextMask][next]) {
                        dp[nextMask][next] = cand
                        parent[nextMask][next] = last
                    }
                }
            }
        }

        // Find best ending word
        var minLen = INF
        var lastWord = -1
        val fullMask = totalMask - 1
        for (i in 0 until n) {
            if (dp[fullMask][i] < minLen) {
                minLen = dp[fullMask][i]
                lastWord = i
            }
        }

        // Reconstruct order
        val order = mutableListOf<Int>()
        var mask = fullMask
        var cur = lastWord
        while (cur != -1) {
            order.add(cur)
            val prev = parent[mask][cur]
            mask = mask xor (1 shl cur)
            cur = prev
        }
        order.reverse()

        // Build result string using overlaps
        val sb = StringBuilder()
        sb.append(words[order[0]])
        for (k in 1 until order.size) {
            val iPrev = order[k - 1]
            val iCurr = order[k]
            val ov = overlap[iPrev][iCurr]
            sb.append(words[iCurr].substring(ov))
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String shortestSuperstring(List<String> words) {
    int n = words.length;
    // Precompute overlap lengths and the string to add
    List<List<int>> overlap = List.generate(n, (_) => List.filled(n, 0));
    List<List<String>> addStr = List.generate(n, (_) => List.filled(n, ''));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        int maxOl = 0;
        int limit = words[i].length < words[j].length ? words[i].length : words[j].length;
        for (int k = limit; k > 0; --k) {
          if (words[i].substring(words[i].length - k) == words[j].substring(0, k)) {
            maxOl = k;
            break;
          }
        }
        overlap[i][j] = maxOl;
        addStr[i][j] = words[j].substring(maxOl);
      }
    }

    int totalMask = 1 << n;
    List<List<String?>> dp = List.generate(totalMask, (_) => List.filled(n, null));

    // Initialize DP with each single word
    for (int i = 0; i < n; ++i) {
      dp[1 << i][i] = words[i];
    }

    for (int mask = 1; mask < totalMask; ++mask) {
      for (int last = 0; last < n; ++last) {
        String? cur = dp[mask][last];
        if (cur == null) continue;
        for (int nxt = 0; nxt < n; ++nxt) {
          if ((mask & (1 << nxt)) != 0) continue;
          int nextMask = mask | (1 << nxt);
          String candidate = cur + addStr[last][nxt];
          String? existing = dp[nextMask][nxt];
          if (existing == null || candidate.length < existing.length) {
            dp[nextMask][nxt] = candidate;
          }
        }
      }
    }

    int fullMask = totalMask - 1;
    String? answer;
    for (int i = 0; i < n; ++i) {
      String? cand = dp[fullMask][i];
      if (cand == null) continue;
      if (answer == null || cand.length < answer.length) {
        answer = cand;
      }
    }

    return answer ?? '';
  }
}
```

## Golang

```go
package main

import (
	"math"
	"strings"
)

func shortestSuperstring(words []string) string {
	n := len(words)
	if n == 0 {
		return ""
	}
	// overlap[i][j] = length of longest suffix of words[i] that matches prefix of words[j]
	overlap := make([][]int, n)
	add := make([][]int, n)
	for i := 0; i < n; i++ {
		overlap[i] = make([]int, n)
		add[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			maxK := min(len(words[i]), len(words[j]))
			best := 0
			for k := maxK; k > 0; k-- {
				if strings.HasSuffix(words[i], words[j][:k]) {
					best = k
					break
				}
			}
			overlap[i][j] = best
			add[i][j] = len(words[j]) - best
		}
	}

	size := 1 << n
	const INF = math.MaxInt32 / 2
	dp := make([][]int, size)
	parent := make([][]int, size)
	for mask := 0; mask < size; mask++ {
		dp[mask] = make([]int, n)
		parent[mask] = make([]int, n)
		for i := 0; i < n; i++ {
			dp[mask][i] = INF
			parent[mask][i] = -1
		}
	}
	for i := 0; i < n; i++ {
		dp[1<<i][i] = len(words[i])
	}

	for mask := 1; mask < size; mask++ {
		for last := 0; last < n; last++ {
			if (mask>>last)&1 == 0 {
				continue
			}
			curLen := dp[mask][last]
			if curLen >= INF {
				continue
			}
			for nxt := 0; nxt < n; nxt++ {
				if (mask>>nxt)&1 == 1 {
					continue
				}
				nextMask := mask | (1 << nxt)
				cand := curLen + add[last][nxt]
				if cand < dp[nextMask][nxt] {
					dp[nextMask][nxt] = cand
					parent[nextMask][nxt] = last
				}
			}
		}
	}

	fullMask := size - 1
	bestLen := INF
	lastIdx := -1
	for i := 0; i < n; i++ {
		if dp[fullMask][i] < bestLen {
			bestLen = dp[fullMask][i]
			lastIdx = i
		}
	}

	// reconstruct order
	order := []int{}
	mask := fullMask
	cur := lastIdx
	for cur != -1 {
		order = append(order, cur)
		prev := parent[mask][cur]
		mask ^= 1 << cur
		cur = prev
	}
	// reverse order
	for i, j := 0, len(order)-1; i < j; i, j = i+1, j-1 {
		order[i], order[j] = order[j], order[i]
	}

	// build result string
	res := words[order[0]]
	for i := 1; i < len(order); i++ {
		o := overlap[order[i-1]][order[i]]
		res += words[order[i]][o:]
	}
	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def shortest_superstring(words)
  n = words.size
  overlap = Array.new(n) { Array.new(n, 0) }

  (0...n).each do |i|
    (0...n).each do |j|
      next if i == j
      max_ol = [words[i].length, words[j].length].min
      max_ol.downto(1) do |k|
        if words[i][-k..-1] == words[j][0, k]
          overlap[i][j] = k
          break
        end
      end
    end
  end

  dp = Array.new(1 << n) { Array.new(n) }

  (0...n).each do |i|
    dp[1 << i][i] = words[i]
  end

  (0...(1 << n)).each do |mask|
    (0...n).each do |last|
      cur = dp[mask][last]
      next if cur.nil?
      (0...n).each do |next_idx|
        next if (mask & (1 << next_idx)) != 0
        new_mask = mask | (1 << next_idx)
        extra = words[next_idx][overlap[last][next_idx]..-1] || ""
        candidate = cur + extra
        existing = dp[new_mask][next_idx]
        if existing.nil? || candidate.length < existing.length
          dp[new_mask][next_idx] = candidate
        end
      end
    end
  end

  full = (1 << n) - 1
  ans = nil
  (0...n).each do |i|
    s = dp[full][i]
    next if s.nil?
    ans = s if ans.nil? || s.length < ans.length
  end
  ans
end
```

## Scala

```scala
object Solution {
  def shortestSupergraph(words: Array[String]): String = {
    val n = words.length
    if (n == 0) return ""
    if (n == 1) return words(0)

    // compute overlaps
    val overlap = Array.ofDim[Int](n, n)
    for (i <- 0 until n; j <- 0 until n if i != j) {
      val a = words(i)
      val b = words(j)
      var maxOv = Math.min(a.length, b.length)
      while (maxOv > 0 && !a.endsWith(b.substring(0, maxOv))) {
        maxOv -= 1
      }
      overlap(i)(j) = maxOv
    }

    val fullMask = (1 << n) - 1
    val INF = Int.MaxValue / 4
    val dp = Array.fill(1 << n, n)(INF)
    val parent = Array.ofDim[Int](1 << n, n)

    for (i <- 0 until n) {
      dp(1 << i)(i) = words(i).length
      parent(1 << i)(i) = -1
    }

    for (mask <- 0 to fullMask) {
      for (last <- 0 until n if (mask & (1 << last)) != 0 && dp(mask)(last) < INF) {
        for (next <- 0 until n if (mask & (1 << next)) == 0) {
          val newMask = mask | (1 << next)
          val cand = dp(mask)(last) + words(next).length - overlap(last)(next)
          if (cand < dp(newMask)(next)) {
            dp(newMask)(next) = cand
            parent(newMask)(next) = last
          }
        }
      }
    }

    var minLen = INF
    var lastIdx = -1
    for (i <- 0 until n) {
      if (dp(fullMask)(i) < minLen) {
        minLen = dp(fullMask)(i)
        lastIdx = i
      }
    }

    // reconstruct order
    val orderBuffer = scala.collection.mutable.ArrayBuffer[Int]()
    var mask = fullMask
    var cur = lastIdx
    while (cur != -1) {
      orderBuffer += cur
      val prev = parent(mask)(cur)
      mask ^= (1 << cur)
      cur = prev
    }
    val order = orderBuffer.reverse

    // build result string using overlaps
    val sb = new StringBuilder()
    sb.append(words(order.head))
    for (k <- 1 until order.length) {
      val i = order(k - 1)
      val j = order(k)
      sb.append(words(j).substring(overlap(i)(j)))
    }
    sb.toString()
  }

  // LeetCode expects the method name `shortestSuperstring`
  def shortestSuperstring(words: Array[String]): String = shortestSupergraph(words)
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_superstring(words: Vec<String>) -> String {
        let n = words.len();
        if n == 0 {
            return "".to_string();
        }
        // compute overlaps
        let mut overlap = vec![vec![0usize; n]; n];
        for i in 0..n {
            for j in 0..n {
                if i == j {
                    continue;
                }
                let a = &words[i];
                let b = &words[j];
                let max_olap = std::cmp::min(a.len(), b.len());
                for k in (0..=max_olap).rev() {
                    if &a[a.len() - k..] == &b[0..k] {
                        overlap[i][j] = k;
                        break;
                    }
                }
            }
        }

        let size = 1usize << n;
        let mut dp: Vec<Vec<Option<String>>> = vec![vec![None; n]; size];
        for i in 0..n {
            dp[1 << i][i] = Some(words[i].clone());
        }

        for mask in 1..size {
            for last in 0..n {
                if let Some(ref cur) = dp[mask][last] {
                    for nxt in 0..n {
                        if (mask >> nxt) & 1 == 1 {
                            continue;
                        }
                        let new_mask = mask | (1 << nxt);
                        let mut cand = cur.clone();
                        let add_part = &words[nxt][overlap[last][nxt]..];
                        cand.push_str(add_part);
                        match &dp[new_mask][nxt] {
                            Some(existing) => {
                                if cand.len() < existing.len() {
                                    dp[new_mask][nxt] = Some(cand);
                                }
                            }
                            None => {
                                dp[new_mask][nxt] = Some(cand);
                            }
                        }
                    }
                }
            }
        }

        let full_mask = size - 1;
        let mut answer: Option<String> = None;
        for i in 0..n {
            if let Some(ref s) = dp[full_mask][i] {
                match &answer {
                    Some(best) => {
                        if s.len() < best.len() {
                            answer = Some(s.clone());
                        }
                    }
                    None => {
                        answer = Some(s.clone());
                    }
                }
            }
        }

        answer.unwrap_or_default()
    }
}
```

## Racket

```racket
(define/contract (shortest-superstring words)
  (-> (listof string?) string?)
  (let* ((n (length words))
         (total (arithmetic-shift 1 n)) ; 2^n
         (word-vec (list->vector words))
         ;; compute overlap matrix
         (ov (make-vector n (lambda () (make-vector n 0))))
         (calc-overlap
          (lambda (a b)
            (let* ((la (string-length a))
                   (lb (string-length b))
                   (maxk (min la lb)))
              (let loop ((k maxk))
                (if (= k 0)
                    0
                    (if (string=? (substring a (- la k)) (substring b 0 k))
                        k
                        (loop (- k 1)))))))))
    ;; fill overlap matrix
    (for ([i (in-range n)])
      (for ([j (in-range n)])
        (when (not (= i j))
          (vector-set! (vector-ref ov i) j (calc-overlap (vector-ref word-vec i)
                                                         (vector-ref word-vec j))))))
    ;; dp tables: dp[mask][i] = max total overlap ending with i, parent[mask][i] = previous index
    (define dp (make-vector total))
    (define parent (make-vector total))
    (for ([mask (in-range total)])
      (vector-set! dp mask (make-vector n -1))
      (vector-set! parent mask (make-vector n -1)))
    ;; initialization for single-word masks
    (for ([i (in-range n)])
      (let ((mask (arithmetic-shift 1 i)))
        (vector-set! (vector-ref dp mask) i 0)
        (vector-set! (vector-ref parent mask) i -1)))
    ;; DP over subsets
    (for ([mask (in-range total)])
      (for ([i (in-range n)])
        (when (and (> (bitwise-and mask (arithmetic-shift 1 i)) 0)
                   (> (vector-ref (vector-ref dp mask) i) -1))
          (let ((cur (vector-ref (vector-ref dp mask) i)))
            (for ([j (in-range n)])
              (when (= (bitwise-and mask (arithmetic-shift 1 j)) 0)
                (let* ((newMask (bitwise-ior mask (arithmetic-shift 1 j)))
                       (val (+ cur (vector-ref (vector-ref ov i) j))))
                  (when (> val (vector-ref (vector-ref dp newMask) j))
                    (vector-set! (vector-ref dp newMask) j val)
                    (vector-set! (vector-ref parent newMask) j i)))))))))
    ;; find best ending word
    (let* ((fullMask (- total 1))
           (best-i -1)
           (best-val -1))
      (for ([i (in-range n)])
        (when (> (vector-ref (vector-ref dp fullMask) i) best-val)
          (set! best-val (vector-ref (vector-ref dp fullMask) i))
          (set! best-i i)))
      ;; reconstruct order
      (define order '())
      (let loop ((mask fullMask) (i best-i))
        (when (>= i 0)
          (set! order (cons i order))
          (let ((prev (vector-ref (vector-ref parent mask) i)))
            (loop (bitwise-xor mask (arithmetic-shift 1 i)) prev))))
      ;; build final superstring
      (define result (vector-ref word-vec (car order)))
      (for ([idx (in-range 1 (length order))])
        (let* ((prev (list-ref order (- idx 1)))
               (curr (list-ref order idx))
               (overlap (vector-ref (vector-ref ov prev) curr))
               (add (substring (vector-ref word-vec curr) overlap)))
          (set! result (string-append result add))))
      result)))
```

## Erlang

```erlang
-module(solution).
-export([shortest_superstring/1]).

-spec shortest_superstring(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
shortest_superstring(Words) ->
    N = length(Words),
    LenList = [byte_size(W) || W <- Words],
    Overlap = compute_overlap_matrix(Words, N),

    Size = 1 bsl N,
    %% Initialize DP and Parent maps
    {DP0, Parent0} =
        lists:foldl(
          fun(I, {DPAcc, ParAcc}) ->
                  Mask = 1 bsl I,
                  {maps:put({Mask, I}, lists:nth(I + 1, LenList), DPAcc),
                   maps:put({Mask, I}, -1, ParAcc)}
          end,
          {maps:new(), maps:new()},
          lists:seq(0, N - 1)),

    %% Main DP loop over masks
    {DPFinal, ParentFinal} =
        lists:foldl(
          fun(Mask, {DPMap, ParMap}) ->
                  lists:foldl(
                    fun(I, {DPIn, ParIn}) ->
                            case (Mask band (1 bsl I)) =/= 0 of
                                true ->
                                    CurLen = maps:get({Mask, I}, DPIn),
                                    lists:foldl(
                                      fun(J, {DPOut, ParOut}) ->
                                              case (Mask band (1 bsl J)) =:= 0 of
                                                  true ->
                                                      NewMask = Mask bor (1 bsl J),
                                                      Add = lists:nth(J + 1, LenList) -
                                                            get_overlap(I, J, Overlap),
                                                      NewLen = CurLen + Add,
                                                      case maps:find({NewMask, J}, DPOut) of
                                                          error ->
                                                              {maps:put({NewMask, J}, NewLen, DPOut),
                                                               maps:put({NewMask, J}, I, ParOut)};
                                                          {ok, Existing} when NewLen < Existing ->
                                                              {maps:put({NewMask, J}, NewLen, DPOut),
                                                               maps:put({NewMask, J}, I, ParOut)};
                                                          _ ->
                                                              {DPOut, ParOut}
                                                      end;
                                                  false -> {DPOut, ParOut}
                                              end
                                      end,
                                      {DPIn, ParIn},
                                      lists:seq(0, N - 1))
                            ; false -> {DPIn, ParIn}
                            end
                    end,
                    {DPMap, ParMap},
                    lists:seq(0, N - 1))
          end,
          {DP0, Parent0},
          lists:seq(1, Size - 1)),

    FullMask = Size - 1,
    %% Find best ending word
    {_, EndIdx} =
        lists:foldl(
          fun(I, {BestLen, BestIdx}) ->
                  case maps:find({FullMask, I}, DPFinal) of
                      {ok, Len} when Len < BestLen -> {Len, I};
                      _ -> {BestLen, BestIdx}
                  end
          end,
          {1000000, -1},
          lists:seq(0, N - 1)),

    %% Reconstruct path
    PathRev = build_path(FullMask, EndIdx, ParentFinal, []),
    Order = lists:reverse(PathRev),

    %% Build final superstring
    case Order of
        [FirstIdx | Rest] ->
            Bin0 = get_word(FirstIdx, Words),
            {_, Result} =
                lists:foldl(
                  fun(CurrIdx, {PrevIdx, Acc}) ->
                          Over = get_overlap(PrevIdx, CurrIdx, Overlap),
                          WordBin = get_word(CurrIdx, Words),
                          Suffix = binary:part(WordBin, {Over, byte_size(WordBin) - Over}),
                          {CurrIdx, <<Acc/binary, Suffix/binary>>}
                  end,
                  {FirstIdx, Bin0},
                  Rest),
            Result;
        [] -> <<>>
    end.

%% Compute overlap matrix where element (i,j) is the maximum overlap length
compute_overlap_matrix(Words, N) ->
    lists:map(
      fun(IWord) ->
              lists:map(
                fun(JWord) ->
                        compute_overlap(IWord, JWord)
                end,
                Words)
      end,
      Words).

%% Compute maximum overlap where suffix of A matches prefix of B
compute_overlap(A, B) ->
    MaxK = min(byte_size(A), byte_size(B)),
    compute_overlap(A, B, MaxK).

compute_overlap(_A, _B, 0) -> 0;
compute_overlap(A, B, K) ->
    StartA = byte_size(A) - K,
    case binary:part(A, {StartA, K}) == binary:part(B, {0, K}) of
        true -> K;
        false -> compute_overlap(A, B, K - 1)
    end.

%% Retrieve word by index (0‑based)
get_word(Index, Words) ->
    lists:nth(Index + 1, Words).

%% Get overlap length from precomputed matrix
get_overlap(I, J, Overlap) ->
    Row = lists:nth(I + 1, Overlap),
    lists:nth(J + 1, Row).

%% Reconstruct path from DP parent map
build_path(_Mask, -1, _Parent, Acc) -> Acc;
build_path(Mask, Curr, Parent, Acc) ->
    Prev = maps:get({Mask, Curr}, Parent),
    NewMask = Mask bxor (1 bsl Curr),
    build_path(NewMask, Prev, Parent, [Curr | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_superstring(words :: [String.t]) :: String.t
  def shortest_superstring(words) do
    import Bitwise

    n = length(words)
    lens = Enum.map(words, &String.length/1)

    # compute extra characters needed when appending j after i
    add_map =
      for i <- 0..n - 1, into: %{} do
        wi = Enum.at(words, i)

        for j <- 0..n - 1, into: %{} do
          if i == j do
            {{i, j}, 0}
          else
            wj = Enum.at(words, j)
            olap = overlap(wi, wj)
            {{i, j}, String.length(wj) - olap}
          end
        end
      end

    get_add = fn i, j -> Map.fetch!(add_map, {i, j}) end

    max_mask = 1 <<< n

    # dp map: {mask, last} => length
    dp0 =
      Enum.reduce(0..n - 1, %{}, fn i, acc ->
        mask = 1 <<< i
        Map.put(acc, {mask, i}, Enum.at(lens, i))
      end)

    parent0 = %{}

    {dp_final, parent_final} =
      Enum.reduce(1..max_mask - 1, {dp0, parent0}, fn mask, {dp_acc, par_acc} ->
        dp_next = dp_acc
        par_next = par_acc

        for i <- 0..n - 1 do
          if (mask &&& (1 <<< i)) != 0 do
            cur_len = Map.get(dp_acc, {mask, i})

            if cur_len != nil do
              for j <- 0..n - 1 do
                if (mask &&& (1 <<< j)) == 0 do
                  new_mask = mask ||| (1 <<< j)
                  add_ij = get_add.(i, j)
                  new_len = cur_len + add_ij
                  key = {new_mask, j}
                  existing = Map.get(dp_next, key)

                  if existing == nil or new_len < existing do
                    dp_next = Map.put(dp_next, key, new_len)
                    par_next = Map.put(par_next, key, {mask, i})
                  end
                end
              end
            end
          end
        end

        {dp_next, par_next}
      end)

    final_mask = max_mask - 1

    {best_last, _} =
      Enum.reduce(0..n - 1, {nil, :infinity}, fn i, {bl, blen} ->
        case Map.get(dp_final, {final_mask, i}) do
          nil -> {bl, blen}
          len when len < blen -> {i, len}
          _ -> {bl, blen}
        end
      end)

    order = build_path(final_mask, best_last, parent_final)

    # construct superstring from order
    [first_idx | rest] = order
    result = Enum.at(words, first_idx)
    prev = first_idx

    final_str =
      Enum.reduce(rest, result, fn idx, acc ->
        add_len = get_add.(prev, idx)
        overlap_len = String.length(Enum.at(words, idx)) - add_len
        suffix = String.slice(Enum.at(words, idx), overlap_len..-1)
        new_acc = acc <> suffix
        prev = idx
        new_acc
      end)

    final_str
  end

  defp overlap(a, b) do
    max = min(String.length(a), String.length(b))

    Enum.reduce_while(max..1, 0, fn k, _acc ->
      if String.slice(a, -k, k) == String.slice(b, 0, k) do
        {:halt, k}
      else
        {:cont, nil}
      end
    end)
  end

  defp build_path(mask, last, parent) do
    case Map.get(parent, {mask, last}) do
      nil -> [last]
      {pm, pl} -> build_path(pm, pl, parent) ++ [last]
    end
  end
end
```
