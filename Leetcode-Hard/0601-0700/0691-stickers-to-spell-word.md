# 0691. Stickers to Spell Word

## Cpp

```cpp
class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        int m = target.size();
        int fullMask = (1 << m) - 1;
        const int INF = 1e9;
        
        // Preprocess sticker counts limited to letters in target
        vector<array<int,26>> cnts;
        for (const string& s : stickers) {
            array<int,26> cnt{};
            cnt.fill(0);
            bool useful = false;
            for (char ch : s) {
                int idx = ch - 'a';
                cnt[idx]++;
                // check if this letter appears in target
                if (target.find(ch) != string::npos) useful = true;
            }
            if (useful) cnts.push_back(cnt);
        }
        if (cnts.empty()) return -1;
        
        vector<int> dp(1 << m, INF);
        dp[0] = 0;
        for (int mask = 0; mask <= fullMask; ++mask) {
            if (dp[mask] == INF) continue;
            // try each sticker
            for (const auto& cnt : cnts) {
                int newMask = mask;
                array<int,26> remain = cnt; // copy
                // fill uncovered positions greedily
                for (int i = 0; i < m; ++i) {
                    if ((newMask >> i) & 1) continue; // already covered
                    int idx = target[i] - 'a';
                    if (remain[idx] > 0) {
                        remain[idx]--;
                        newMask |= (1 << i);
                    }
                }
                if (dp[newMask] > dp[mask] + 1) {
                    dp[newMask] = dp[mask] + 1;
                }
            }
        }
        return dp[fullMask] == INF ? -1 : dp[fullMask];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minStickers(String[] stickers, String target) {
        int m = target.length();
        char[] tChars = target.toCharArray();
        boolean[] need = new boolean[26];
        for (char c : tChars) need[c - 'a'] = true;

        // Count letters in each sticker, only needed ones
        int n = stickers.length;
        int[][] cnts = new int[n][26];
        int[] totalAvail = new int[26];
        for (int i = 0; i < n; i++) {
            String s = stickers[i];
            int[] cur = new int[26];
            for (char c : s.toCharArray()) {
                int idx = c - 'a';
                if (need[idx]) {
                    cur[idx]++;
                    totalAvail[idx]++;
                }
            }
            cnts[i] = cur;
        }

        // If any needed letter is unavailable, impossible
        for (int i = 0; i < 26; i++) {
            if (need[i] && totalAvail[i] == 0) return -1;
        }

        // Remove dominated stickers
        boolean[] remove = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (remove[i]) continue;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (dominates(cnts[j], cnts[i])) {
                    remove[i] = true;
                    break;
                }
            }
        }

        List<int[]> stickerList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!remove[i]) stickerList.add(cnts[i]);
        }
        int[][] stickersCnt = stickerList.toArray(new int[0][]);

        int fullMask = (1 << m) - 1;
        int[] dp = new int[1 << m];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int mask = 0; mask <= fullMask; mask++) {
            if (dp[mask] == Integer.MAX_VALUE) continue;
            for (int[] sc : stickersCnt) {
                int next = applySticker(mask, sc, tChars);
                if (next != mask && dp[next] > dp[mask] + 1) {
                    dp[next] = dp[mask] + 1;
                }
            }
        }

        return dp[fullMask] == Integer.MAX_VALUE ? -1 : dp[fullMask];
    }

    private boolean dominates(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] < b[i]) return false;
        }
        return true;
    }

    private int applySticker(int mask, int[] cnt, char[] target) {
        int m = target.length;
        int next = mask;
        for (int c = 0; c < 26; c++) {
            int remain = cnt[c];
            if (remain == 0) continue;
            for (int i = 0; i < m && remain > 0; i++) {
                if (((next >> i) & 1) == 0 && target[i] - 'a' == c) {
                    next |= 1 << i;
                    remain--;
                }
            }
        }
        return next;
    }
}
```

## Python

```python
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        m = len(target)
        full_mask = (1 << m) - 1

        # Preprocess sticker counts limited to letters in target
        target_counts = [0] * 26
        for ch in target:
            target_counts[ord(ch) - 97] += 1

        processed = []
        for s in stickers:
            cnt = [0] * 26
            for ch in s:
                idx = ord(ch) - 97
                if target_counts[idx]:
                    cnt[idx] += 1
            # keep only stickers that contribute at least one needed letter
            if any(cnt):
                processed.append(cnt)

        # Early impossibility check
        overall = [0] * 26
        for cnt in processed:
            for i in range(26):
                if cnt[i]:
                    overall[i] = 1
        for ch in target:
            if not overall[ord(ch) - 97]:
                return -1

        # DP over masks
        INF = float('inf')
        dp = [INF] * (full_mask + 1)
        dp[0] = 0

        def apply(mask, sticker_cnt):
            new_mask = mask
            cnt = sticker_cnt[:]  # copy to modify locally
            for i in range(m):
                if not (new_mask >> i) & 1:
                    idx = ord(target[i]) - 97
                    if cnt[idx]:
                        cnt[idx] -= 1
                        new_mask |= 1 << i
            return new_mask

        for mask in range(full_mask + 1):
            if dp[mask] == INF:
                continue
            for scnt in processed:
                nxt = apply(mask, scnt)
                if nxt != mask and dp[nxt] > dp[mask] + 1:
                    dp[nxt] = dp[mask] + 1

        return -1 if dp[full_mask] == INF else dp[full_mask]
```

## Python3

```python
class Solution:
    def minStickers(self, stickers, target):
        from collections import Counter
        m = len(target)
        full_mask = (1 << m) - 1
        # preprocess sticker counts limited to letters in target
        target_set = set(target)
        sticker_counts = []
        for s in stickers:
            cnt = [0] * 26
            for ch in s:
                if ch in target_set:
                    cnt[ord(ch) - 97] += 1
            if any(cnt):
                sticker_counts.append(cnt)

        # early impossible check
        total_available = [0] * 26
        for cnt in sticker_counts:
            for i in range(26):
                total_available[i] += cnt[i]
        for ch in target:
            if total_available[ord(ch) - 97] == 0:
                return -1

        # remove dominated stickers
        filtered = []
        n = len(sticker_counts)
        for i in range(n):
            dominate = False
            for j in range(n):
                if i == j:
                    continue
                ci, cj = sticker_counts[i], sticker_counts[j]
                if all(ci[k] <= cj[k] for k in range(26)) and any(ci[k] < cj[k] for k in range(26)):
                    dominate = True
                    break
            if not dominate:
                filtered.append(sticker_counts[i])
        sticker_counts = filtered

        dp = [float('inf')] * (1 << m)
        dp[0] = 0

        # helper to apply a sticker on a mask
        def apply(mask, cnt):
            new_mask = mask
            remain = cnt[:]  # copy
            for i in range(m):
                if not (mask >> i) & 1:
                    idx = ord(target[i]) - 97
                    if remain[idx] > 0:
                        remain[idx] -= 1
                        new_mask |= (1 << i)
            return new_mask

        for mask in range(1 << m):
            if dp[mask] == float('inf'):
                continue
            for cnt in sticker_counts:
                nxt = apply(mask, cnt)
                if dp[nxt] > dp[mask] + 1:
                    dp[nxt] = dp[mask] + 1

        return -1 if dp[full_mask] == float('inf') else dp[full_mask]
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int applySticker(int mask, const int *cnt, const char *target, int m) {
    int newMask = mask;
    int rem[26];
    memcpy(rem, cnt, 26 * sizeof(int));
    for (int i = 0; i < m; ++i) {
        if ((mask >> i) & 1) continue;               // already covered
        int c = target[i] - 'a';
        if (rem[c] > 0) {
            rem[c]--;
            newMask |= (1 << i);
        }
    }
    return newMask;
}

int minStickers(char** stickers, int stickersSize, char* target) {
    int m = strlen(target);
    if (m == 0) return 0;
    int fullMask = (1 << m) - 1;

    // Preprocess sticker character counts
    int **stickerCnt = (int **)malloc(stickersSize * sizeof(int *));
    for (int i = 0; i < stickersSize; ++i) {
        stickerCnt[i] = (int *)calloc(26, sizeof(int));
        for (char *p = stickers[i]; *p; ++p)
            stickerCnt[i][*p - 'a']++;
    }

    // Quick impossibility check
    int have[26] = {0};
    for (int i = 0; i < stickersSize; ++i) {
        for (int c = 0; c < 26; ++c)
            if (stickerCnt[i][c]) have[c] = 1;
    }
    for (int i = 0; i < m; ++i) {
        if (!have[target[i] - 'a']) {
            // clean up
            for (int k = 0; k < stickersSize; ++k) free(stickerCnt[k]);
            free(stickerCnt);
            return -1;
        }
    }

    int INF = m + 1;                     // maximum needed cannot exceed m
    int dpSize = 1 << m;
    int *dp = (int *)malloc(dpSize * sizeof(int));
    for (int i = 0; i < dpSize; ++i) dp[i] = INF;
    dp[0] = 0;

    for (int mask = 0; mask <= fullMask; ++mask) {
        if (dp[mask] == INF) continue;
        for (int s = 0; s < stickersSize; ++s) {
            int newMask = applySticker(mask, stickerCnt[s], target, m);
            if (newMask != mask && dp[newMask] > dp[mask] + 1)
                dp[newMask] = dp[mask] + 1;
        }
    }

    int ans = dp[fullMask];
    // clean up
    for (int i = 0; i < stickersSize; ++i) free(stickerCnt[i]);
    free(stickerCnt);
    free(dp);

    return (ans == INF) ? -1 : ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinStickers(string[] stickers, string target) {
        int m = target.Length;
        int fullMask = (1 << m) - 1;
        bool[] needed = new bool[26];
        foreach (char c in target) needed[c - 'a'] = true;

        List<int[]> filtered = new List<int[]>();
        foreach (var s in stickers) {
            int[] cnt = new int[26];
            foreach (char c in s) {
                int idx = c - 'a';
                if (needed[idx]) cnt[idx]++;
            }
            bool any = false;
            for (int i = 0; i < 26; i++) {
                if (cnt[i] > 0) { any = true; break; }
            }
            if (any) filtered.Add(cnt);
        }

        const int INF = 1000000;
        int[] dp = new int[1 << m];
        for (int i = 0; i < dp.Length; i++) dp[i] = INF;
        dp[0] = 0;

        for (int mask = 0; mask <= fullMask; mask++) {
            if (dp[mask] == INF) continue;
            foreach (var sticker in filtered) {
                int[] cnt = (int[])sticker.Clone();
                int newMask = mask;
                for (int i = 0; i < m; i++) {
                    if (((newMask >> i) & 1) == 0) {
                        int idx = target[i] - 'a';
                        if (cnt[idx] > 0) {
                            cnt[idx]--;
                            newMask |= 1 << i;
                        }
                    }
                }
                if (dp[newMask] > dp[mask] + 1) {
                    dp[newMask] = dp[mask] + 1;
                }
            }
        }

        return dp[fullMask] == INF ? -1 : dp[fullMask];
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} stickers
 * @param {string} target
 * @return {number}
 */
var minStickers = function(stickers, target) {
    const m = target.length;
    const fullMask = (1 << m) - 1;
    const tIdx = new Array(m);
    for (let i = 0; i < m; i++) tIdx[i] = target.charCodeAt(i) - 97;

    // preprocess stickers into count arrays, keep only useful ones
    const stickerCounts = [];
    for (const s of stickers) {
        const cnt = new Array(26).fill(0);
        for (let ch of s) {
            cnt[ch.charCodeAt(0) - 97]++;
        }
        // discard if it doesn't contain any needed character
        let useful = false;
        for (let i = 0; i < m; i++) {
            if (cnt[tIdx[i]] > 0) { useful = true; break; }
        }
        if (useful) stickerCounts.push(cnt);
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dp = new Array(1 << m).fill(INF);
    dp[0] = 0;

    for (let mask = 0; mask <= fullMask; mask++) {
        if (dp[mask] === INF) continue;
        for (const cnt of stickerCounts) {
            const cur = cnt.slice(); // mutable copy
            let newMask = mask;
            for (let i = 0; i < m; i++) {
                if (((newMask >> i) & 1) === 0) {
                    const idx = tIdx[i];
                    if (cur[idx] > 0) {
                        cur[idx]--;
                        newMask |= (1 << i);
                    }
                }
            }
            if (newMask === mask) continue; // sticker adds nothing
            if (dp[newMask] > dp[mask] + 1) {
                dp[newMask] = dp[mask] + 1;
            }
        }
    }

    return dp[fullMask] === INF ? -1 : dp[fullMask];
};
```

## Typescript

```typescript
function minStickers(stickers: string[], target: string): number {
    const n = stickers.length;
    const m = target.length;
    const targetArr = target.split('');
    
    // Count letters in all stickers to quickly detect impossibility
    const totalCnt = new Array(26).fill(0);
    const stickerCounts: number[][] = [];
    for (let s = 0; s < n; ++s) {
        const cnt = new Array(26).fill(0);
        for (const ch of stickers[s]) {
            const idx = ch.charCodeAt(0) - 97;
            cnt[idx]++;
            totalCnt[idx]++;
        }
        stickerCounts.push(cnt);
    }
    for (const ch of targetArr) {
        if (totalCnt[ch.charCodeAt(0) - 97] === 0) return -1;
    }

    const size = 1 << m;
    const INF = Number.MAX_SAFE_INTEGER;
    const dp = new Array(size).fill(INF);
    dp[0] = 0;

    for (let state = 0; state < size; ++state) {
        if (dp[state] === INF) continue;
        for (let s = 0; s < n; ++s) {
            const cnt = stickerCounts[s].slice(); // mutable copy
            let newState = state;
            for (let i = 0; i < m; ++i) {
                if ((newState >> i) & 1) continue; // already covered
                const idx = targetArr[i].charCodeAt(0) - 97;
                if (cnt[idx] > 0) {
                    cnt[idx]--;
                    newState |= (1 << i);
                }
            }
            if (newState !== state && dp[newState] > dp[state] + 1) {
                dp[newState] = dp[state] + 1;
            }
        }
    }

    const ans = dp[size - 1];
    return ans === INF ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $stickers
     * @param String $target
     * @return Integer
     */
    function minStickers($stickers, $target) {
        $m = strlen($target);
        if ($m == 0) return 0;
        $tChars = str_split($target);

        // characters that appear in target
        $needChar = array_fill(0, 26, false);
        for ($i = 0; $i < $m; $i++) {
            $idx = ord($tChars[$i]) - 97;
            $needChar[$idx] = true;
        }

        // preprocess stickers: count only needed letters, discard useless stickers
        $stickerCounts = [];
        foreach ($stickers as $s) {
            $cnt = array_fill(0, 26, 0);
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $cIdx = ord($s[$i]) - 97;
                if ($needChar[$cIdx]) {
                    $cnt[$cIdx]++;
                }
            }
            // keep only stickers that contribute at least one needed letter
            $has = false;
            foreach ($cnt as $v) {
                if ($v > 0) { $has = true; break; }
            }
            if ($has) {
                $stickerCounts[] = $cnt;
            }
        }

        // If no sticker can contribute, impossible
        if (empty($stickerCounts)) return -1;

        $size = 1 << $m;
        $INF = PHP_INT_MAX;
        $dp = array_fill(0, $size, $INF);
        $dp[0] = 0;
        $fullMask = $size - 1;

        for ($state = 0; $state < $size; $state++) {
            if ($dp[$state] == $INF) continue;
            foreach ($stickerCounts as $cnt) {
                $newState = $state;
                // copy counts to use this sticker once
                $remain = $cnt;
                for ($i = 0; $i < $m; $i++) {
                    if ((($state >> $i) & 1) == 0) { // not yet covered
                        $cIdx = ord($tChars[$i]) - 97;
                        if ($remain[$cIdx] > 0) {
                            $remain[$cIdx]--;
                            $newState |= (1 << $i);
                        }
                    }
                }
                if ($newState == $state) continue; // this sticker adds nothing
                if ($dp[$newState] > $dp[$state] + 1) {
                    $dp[$newState] = $dp[$state] + 1;
                }
            }
        }

        return $dp[$fullMask] == $INF ? -1 : $dp[$fullMask];
    }
}
```

## Swift

```swift
class Solution {
    func minStickers(_ stickers: [String], _ target: String) -> Int {
        // Count letters in target
        var targetCount = [Int](repeating: 0, count: 26)
        for ch in target {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            targetCount[idx] += 1
        }
        
        // Preprocess stickers: keep only letters that appear in target
        var stickerCounts = [[Int]]()
        for s in stickers {
            var cnt = [Int](repeating: 0, count: 26)
            var hasRelevant = false
            for ch in s {
                let idx = Int(ch.unicodeScalars.first!.value - 97)
                if targetCount[idx] > 0 {
                    cnt[idx] += 1
                    hasRelevant = true
                }
            }
            if hasRelevant { stickerCounts.append(cnt) }
        }
        
        // Remove dominated stickers
        var keep = [Bool](repeating: true, count: stickerCounts.count)
        for i in 0..<stickerCounts.count where keep[i] {
            for j in 0..<stickerCounts.count where i != j && keep[j] {
                var iDominated = true
                var jDominated = true
                for k in 0..<26 {
                    if stickerCounts[i][k] > stickerCounts[j][k] { iDominated = false }
                    if stickerCounts[i][k] < stickerCounts[j][k] { jDominated = false }
                }
                // i is dominated by j
                if iDominated && !jDominated {
                    keep[i] = false
                    break
                }
            }
        }
        var filteredStickers = [[Int]]()
        for (idx, flag) in keep.enumerated() where flag {
            filteredStickers.append(stickerCounts[idx])
        }
        
        // Early impossibility check
        for i in 0..<26 where targetCount[i] > 0 {
            var ok = false
            for cnt in filteredStickers where cnt[i] > 0 {
                ok = true
                break
            }
            if !ok { return -1 }
        }
        
        var memo = [String: Int]()
        func dfs(_ need: [Int]) -> Int {
            // All satisfied?
            var finished = true
            for v in need where v > 0 {
                finished = false
                break
            }
            if finished { return 0 }
            
            let key = need.map { String($0) }.joined(separator: ",")
            if let cached = memo[key] { return cached }
            
            // Choose a needed letter to guide pruning
            var firstIdx = -1
            for i in 0..<26 where need[i] > 0 {
                firstIdx = i
                break
            }
            
            var best = Int.max
            for sticker in filteredStickers {
                if sticker[firstIdx] == 0 { continue } // cannot help with this needed letter
                var newNeed = need
                for k in 0..<26 where newNeed[k] > 0 && sticker[k] > 0 {
                    newNeed[k] = max(0, newNeed[k] - sticker[k])
                }
                let sub = dfs(newNeed)
                if sub != -1 {
                    best = min(best, 1 + sub)
                }
            }
            
            let result = (best == Int.max) ? -1 : best
            memo[key] = result
            return result
        }
        
        return dfs(targetCount)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minStickers(stickers: Array<String>, target: String): Int {
        val n = stickers.size
        val m = target.length
        val targetChars = target.toCharArray()
        // Count letters for each sticker
        val stickerCounts = Array(n) { IntArray(26) }
        for (i in 0 until n) {
            for (ch in stickers[i]) {
                stickerCounts[i][ch - 'a']++
            }
        }
        // Remove dominated stickers
        val useful = mutableListOf<IntArray>()
        outer@ for (i in 0 until n) {
            val cur = stickerCounts[i]
            for (j in 0 until n) {
                if (i == j) continue
                val other = stickerCounts[j]
                var dominates = true
                for (c in 0..25) {
                    if (other[c] < cur[c]) { dominates = false; break }
                }
                if (dominates) continue@outer // cur is dominated, skip it
            }
            useful.add(cur)
        }
        val stickersList = useful.toTypedArray()
        val sz = stickersList.size

        val fullMask = (1 shl m) - 1
        val INF = Int.MAX_VALUE / 2
        val dp = IntArray(1 shl m) { INF }
        dp[0] = 0

        for (mask in 0..fullMask) {
            if (dp[mask] == INF) continue
            for (stIdx in 0 until sz) {
                val cntCopy = stickersList[stIdx].clone()
                var newMask = mask
                for (pos in 0 until m) {
                    if ((newMask shr pos) and 1 == 0) {
                        val cIdx = targetChars[pos] - 'a'
                        if (cntCopy[cIdx] > 0) {
                            cntCopy[cIdx]--
                            newMask = newMask or (1 shl pos)
                        }
                    }
                }
                if (newMask != mask && dp[newMask] > dp[mask] + 1) {
                    dp[newMask] = dp[mask] + 1
                }
            }
        }

        return if (dp[fullMask] == INF) -1 else dp[fullMask]
    }
}
```

## Dart

```dart
class Solution {
  int minStickers(List<String> stickers, String target) {
    int m = target.length;
    if (m == 0) return 0;

    // Convert target to list of character indices
    List<int> targetChars = List.filled(m, 0);
    for (int i = 0; i < m; ++i) {
      targetChars[i] = target.codeUnitAt(i) - 97;
    }

    // Count letters in each sticker
    List<List<int>> stickerCounts = [];
    // Also track which letters appear in any sticker
    List<bool> letterAvailable = List.filled(26, false);
    for (String s in stickers) {
      List<int> cnt = List.filled(26, 0);
      for (int i = 0; i < s.length; ++i) {
        int c = s.codeUnitAt(i) - 97;
        cnt[c]++;
        letterAvailable[c] = true;
      }
      stickerCounts.add(cnt);
    }

    // Quick impossibility check
    for (int c in targetChars) {
      if (!letterAvailable[c]) return -1;
    }

    int fullMask = (1 << m) - 1;
    const int INF = 1 << 30;
    List<int> dp = List.filled(1 << m, INF);
    dp[0] = 0;

    for (int mask = 0; mask <= fullMask; ++mask) {
      if (dp[mask] == INF) continue;
      for (List<int> sticker in stickerCounts) {
        // Apply this sticker
        List<int> cnt = List.from(sticker);
        int newMask = mask;

        for (int i = 0; i < m; ++i) {
          if ((newMask >> i & 1) == 1) continue;
          int c = targetChars[i];
          if (cnt[c] > 0) {
            cnt[c]--;
            newMask |= (1 << i);
          }
        }

        if (newMask == mask) continue; // sticker adds nothing
        if (dp[newMask] > dp[mask] + 1) {
          dp[newMask] = dp[mask] + 1;
        }
      }
    }

    return dp[fullMask] == INF ? -1 : dp[fullMask];
  }
}
```

## Golang

```go
func minStickers(stickers []string, target string) int {
	m := len(target)
	if m == 0 {
		return 0
	}
	fullMask := (1 << m) - 1

	// quick impossibility check
	var have [26]bool
	for _, s := range stickers {
		for i := 0; i < len(s); i++ {
			have[s[i]-'a'] = true
		}
	}
	for i := 0; i < m; i++ {
		if !have[target[i]-'a'] {
			return -1
		}
	}

	// preprocess sticker letter counts
	type cntArr [26]int
	stickerCnts := make([]cntArr, 0, len(stickers))
	for _, s := range stickers {
		var arr cntArr
		for i := 0; i < len(s); i++ {
			arr[s[i]-'a']++
		}
		stickerCnts = append(stickerCnts, arr)
	}

	const INF = int(1e9)
	dp := make([]int, 1<<m)
	for i := range dp {
		dp[i] = INF
	}
	dp[0] = 0

	for mask := 0; mask <= fullMask; mask++ {
		if dp[mask] == INF {
			continue
		}
		for _, cnt := range stickerCnts {
			newMask := mask
			var cur cntArr = cnt
			// try to cover uncovered positions
			for i := 0; i < m; i++ {
				if (newMask>>i)&1 == 1 {
					continue
				}
				c := target[i] - 'a'
				if cur[c] > 0 {
					cur[c]--
					newMask |= 1 << i
				}
			}
			if dp[newMask] > dp[mask]+1 {
				dp[newMask] = dp[mask] + 1
			}
		}
	}

	if dp[fullMask] == INF {
		return -1
	}
	return dp[fullMask]
}
```

## Ruby

```ruby
def min_stickers(stickers, target)
  m = target.length
  return 0 if m == 0

  # count letters in all stickers for quick impossibility check
  total = Array.new(26, 0)
  sticker_counts = stickers.map do |s|
    cnt = Array.new(26, 0)
    s.each_char { |c| idx = c.ord - 97; cnt[idx] += 1; total[idx] += 1 }
    cnt
  end

  target.each_char { |c| return -1 if total[c.ord - 97] == 0 }

  full_mask = (1 << m) - 1
  inf = 1 << 30
  dp = Array.new(1 << m, inf)
  dp[0] = 0

  (0...(1 << m)).each do |mask|
    next if dp[mask] == inf
    sticker_counts.each do |cnt|
      new_mask = mask
      cnt_copy = cnt.clone
      (0...m).each do |i|
        next if (new_mask >> i) & 1 == 1
        idx = target[i].ord - 97
        if cnt_copy[idx] > 0
          cnt_copy[idx] -= 1
          new_mask |= (1 << i)
        end
      end
      dp[new_mask] = dp[mask] + 1 if dp[new_mask] > dp[mask] + 1
    end
  end

  ans = dp[full_mask]
  ans == inf ? -1 : ans
end
```

## Scala

```scala
object Solution {
    def minStickers(stickers: Array[String], target: String): Int = {
        val m = target.length
        if (m == 0) return 0
        val fullMask = (1 << m) - 1
        val INF = Int.MaxValue / 2

        val dp = Array.fill(1 << m)(INF)
        dp(0) = 0

        val targetChars = target.toCharArray

        // Preprocess sticker letter counts
        val stickerCounts: Array[Array[Int]] = stickers.map { s =>
            val cnt = new Array[Int](26)
            for (ch <- s) {
                cnt(ch - 'a') += 1
            }
            cnt
        }

        for (mask <- 0 to fullMask) {
            if (dp(mask) != INF) {
                for (sticker <- stickerCounts) {
                    var cnt = sticker.clone()
                    var newMask = mask
                    var i = 0
                    while (i < m) {
                        if (((newMask >> i) & 1) == 0) {
                            val idx = targetChars(i) - 'a'
                            if (cnt(idx) > 0) {
                                cnt(idx) -= 1
                                newMask |= (1 << i)
                            }
                        }
                        i += 1
                    }
                    if (dp(newMask) > dp(mask) + 1) {
                        dp(newMask) = dp(mask) + 1
                    }
                }
            }
        }

        val ans = dp(fullMask)
        if (ans >= INF) -1 else ans
    }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn min_stickers(stickers: Vec<String>, target: String) -> i32 {
        let m = target.len();
        if m == 0 {
            return 0;
        }
        let t_bytes = target.as_bytes();

        // preprocess stickers into count arrays
        let mut sticker_counts: Vec<[i32; 26]> = Vec::new();
        for s in &stickers {
            let mut cnt = [0i32; 26];
            for &b in s.as_bytes() {
                cnt[(b - b'a') as usize] += 1;
            }
            sticker_counts.push(cnt);
        }

        // early impossibility check
        let mut have = [false; 26];
        for cnt in &sticker_counts {
            for i in 0..26 {
                if cnt[i] > 0 {
                    have[i] = true;
                }
            }
        }
        for &b in t_bytes {
            if !have[(b - b'a') as usize] {
                return -1;
            }
        }

        let full_mask: usize = (1usize << m) - 1;
        const INF: i32 = 1_000_000;
        let mut dp = vec![INF; full_mask + 1];
        dp[0] = 0;

        for mask in 0..=full_mask {
            if dp[mask] == INF {
                continue;
            }
            for sticker in &sticker_counts {
                let mut new_mask = mask;
                let mut cnt = *sticker; // copy
                for i in 0..m {
                    if (new_mask >> i) & 1 == 0 {
                        let idx = (t_bytes[i] - b'a') as usize;
                        if cnt[idx] > 0 {
                            cnt[idx] -= 1;
                            new_mask |= 1 << i;
                        }
                    }
                }
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1);
            }
        }

        let ans = dp[full_mask];
        if ans == INF { -1 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (min-stickers stickers target)
  (-> (listof string?) string? exact-integer?)
  (let* ((m (string-length target))
         (full-mask (sub1 (arithmetic-shift 1 m))) ; 2^m - 1
         (INF 1000)                               ; larger than any possible answer
         
         ;; check if every character of target appears in at least one sticker
         (available (make-vector 26 #f)))
    ;; populate available letters
    (for ([s stickers])
      (for ([ch (in-string s)])
        (vector-set! available
                     (- (char->integer ch) (char->integer #\a))
                     #t)))
    (let loop ((i 0) (possible? #t))
      (if (or (not possible?) (= i m))
          (if (not possible?)
              -1
              ;; proceed with DP
              (let* ((sticker-chars-list (map string->list stickers))
                     (dp (make-vector (+ full-mask 1) INF)))
                (vector-set! dp 0 0)
                
                ;; apply a sticker to current mask, returning new mask
                (define (apply-sticker mask chars)
                  (let inner ((cs chars) (newMask mask))
                    (if (null? cs)
                        newMask
                        (let* ((ch (car cs))
                               (pos (let find ((idx 0))
                                      (cond [(>= idx m) #f]
                                            [(and (char=? ch (string-ref target idx))
                                                  (= 0 (bitwise-and newMask (arithmetic-shift 1 idx))))
                                             idx]
                                            [else (find (+ idx 1))]))))
                          (if pos
                              (inner (cdr cs)
                                     (bitwise-ior newMask (arithmetic-shift 1 pos)))
                              (inner (cdr cs) newMask))))))

                ;; DP over all subsets of target positions
                (for ([mask (in-range 0 (+ full-mask 1))])
                  (let ((cur (vector-ref dp mask)))
                    (when (< cur INF)
                      (for ([sch sticker-chars-list])
                        (define newMask (apply-sticker mask sch))
                        (when (< (+ cur 1) (vector-ref dp newMask))
                          (vector-set! dp newMask (+ cur 1)))))))

                (let ((ans (vector-ref dp full-mask)))
                  (if (= ans INF) -1 ans))))
          ;; continue checking feasibility
          (let* ((ch (string-ref target i))
                 (idx (- (char->integer ch) (char->integer #\a))))
            (loop (+ i 1)
                  (and possible? (vector-ref available idx)))))))))
```

## Erlang

```erlang
-spec min_stickers([unicode:unicode_binary()], unicode:unicode_binary()) -> integer().
min_stickers(Stickers, Target) ->
    TargetChars = unicode:characters_to_list(Target),
    TLen = length(TargetChars),
    FullMask = (1 bsl TLen) - 1,
    TargetSet = lists:foldl(fun(C, Acc) -> maps:put(C - $a, true, Acc) end, #{}, TargetChars),

    StickerMaps0 = [make_counts(unicode:characters_to_list(S), TargetSet) || S <- Stickers],
    StickerMaps = [M || M <- StickerMaps0, maps:size(M) > 0],

    case bfs(StickerMaps, TargetChars, FullMask) of
        {ok, Steps} -> Steps;
        not_found -> -1
    end.

make_counts(Chars, TargetSet) ->
    lists:foldl(fun(C, Acc) ->
        Idx = C - $a,
        case maps:is_key(Idx, TargetSet) of
            true ->
                case maps:get(Idx, Acc, 0) of
                    0 -> maps:put(Idx, 1, Acc);
                    V -> maps:put(Idx, V + 1, Acc)
                end;
            false -> Acc
        end
    end, #{}, Chars).

bfs(Stickers, TargetChars, FullMask) ->
    Queue0 = queue:new(),
    Queue1 = queue:in({0, 0}, Queue0),
    Visited0 = maps:put(0, true, #{}),
    bfs_loop(Queue1, Visited0, Stickers, TargetChars, FullMask).

bfs_loop(Queue, Visited, Stickers, TargetChars, FullMask) ->
    case queue:out(Queue) of
        {empty, _} -> not_found;
        {{value, {Mask, Steps}}, RestQueue} ->
            if Mask =:= FullMask ->
                    {ok, Steps};
               true ->
                    {NewQueue, NewVisited} =
                        lists:foldl(
                            fun(StickerMap, {QAcc, VAcc}) ->
                                NewMask = apply_sticker(Mask, StickerMap, TargetChars),
                                case (NewMask =/= Mask) andalso (maps:is_key(NewMask, VAcc) =:= false) of
                                    true ->
                                        Q1 = queue:in({NewMask, Steps + 1}, QAcc),
                                        V1 = maps:put(NewMask, true, VAcc),
                                        {Q1, V1};
                                    false -> {QAcc, VAcc}
                                end
                            end,
                            {RestQueue, Visited},
                            Stickers),
                    bfs_loop(NewQueue, NewVisited, Stickers, TargetChars, FullMask)
            end
    end.

apply_sticker(Mask, StickerMap, TargetChars) ->
    apply_sticker_chars(0, Mask, StickerMap, TargetChars).

apply_sticker_chars(_Idx, Mask, _Counts, []) -> Mask;
apply_sticker_chars(Idx, Mask, Counts, [Char | Rest]) ->
    Bit = 1 bsl Idx,
    case (Mask band Bit) of
        0 ->
            IdxLetter = Char - $a,
            C = maps:get(IdxLetter, Counts, 0),
            if C > 0 ->
                    NewCounts = maps:put(IdxLetter, C - 1, Counts),
                    NewMask = Mask bor Bit,
                    apply_sticker_chars(Idx + 1, NewMask, NewCounts, Rest);
               true ->
                    apply_sticker_chars(Idx + 1, Mask, Counts, Rest)
            end;
        _Other -> % already covered
            apply_sticker_chars(Idx + 1, Mask, Counts, Rest)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec min_stickers(stickers :: [String.t()], target :: String.t()) :: integer()
  def min_stickers(stickers, target) do
    t_chars = String.graphemes(target)
    n = length(t_chars)

    all_mask = (1 <<< n) - 1
    stickers_lists = Enum.map(stickers, &String.graphemes/1)

    {ans, _memo} = dfs(0, all_mask, t_chars, stickers_lists, %{})
    if ans == :infinity, do: -1, else: ans
  end

  defp dfs(mask, all_mask, t_chars, stickers, memo) do
    cond do
      mask == all_mask ->
        {0, memo}

      Map.has_key?(memo, mask) ->
        {Map.get(memo, mask), memo}

      true ->
        {best, new_memo} =
          Enum.reduce(stickers, {:infinity, memo}, fn sticker, {cur_best, cur_memo} ->
            new_mask = apply_sticker(mask, t_chars, sticker)

            if new_mask == mask do
              {cur_best, cur_memo}
            else
              {sub_res, sub_memo} = dfs(new_mask, all_mask, t_chars, stickers, cur_memo)

              if sub_res != :infinity and sub_res + 1 < cur_best do
                {sub_res + 1, sub_memo}
              else
                {cur_best, sub_memo}
              end
            end
          end)

        memo2 = Map.put(new_memo, mask, best)
        {best, memo2}
    end
  end

  defp apply_sticker(mask, t_chars, sticker) do
    Enum.reduce(sticker, mask, fn ch, cur_mask ->
      case find_uncovered_index(t_chars, ch, cur_mask) do
        nil -> cur_mask
        idx -> cur_mask ||| (1 <<< idx)
      end
    end)
  end

  defp find_uncovered_index(t_chars, ch, mask) do
    t_chars
    |> Enum.with_index()
    |> Enum.find(fn {c, i} ->
      c == ch and ((mask &&& (1 <<< i)) == 0)
    end)
    |> case do
      nil -> nil
      {_c, i} -> i
    end
  end
end
```
