# 3302. Find the Lexicographically Smallest Valid Sequence

## Cpp

```cpp
class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        // dpExact[i]: longest suffix of word2 that is a subsequence of word1[i..]
        vector<int> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            if (dp[i + 1] < m && word1[i] == word2[m - dp[i + 1] - 1])
                dp[i] = dp[i + 1] + 1;
            else
                dp[i] = dp[i + 1];
        }
        // earliest positions for each prefix of word2 (exact match)
        vector<int> prefPos(m, -1);
        int p = 0;
        for (int i = 0; i < n && p < m; ++i) {
            if (word1[i] == word2[p]) {
                prefPos[p] = i;
                ++p;
            }
        }
        // next occurrence table
        const int ALPH = 26;
        vector<array<int, ALPH>> nxt(n + 2);
        for (int c = 0; c < ALPH; ++c) nxt[n][c] = n;
        for (int i = n - 1; i >= 0; --i) {
            nxt[i] = nxt[i + 1];
            nxt[i][word1[i] - 'a'] = i;
        }
        // try to place mismatch at position k (number of exact prefix chars before it)
        for (int k = 0; k < m; ++k) {
            if (k > 0 && prefPos[k - 1] == -1) continue;          // prefix not possible
            int leftIdx = (k == 0 ? -1 : prefPos[k - 1]);
            int startPos = leftIdx + 1;
            if (startPos >= n) continue;
            int needLen = m - k - 1;                               // characters after mismatch
            if (dp[startPos] < needLen) continue;                 // cannot match remaining suffix
            // construct answer
            vector<int> ans;
            for (int i = 0; i < k; ++i) ans.push_back(prefPos[i]);
            ans.push_back(startPos);                               // mismatch index
            int cur = startPos + 1;
            bool ok = true;
            for (int idx = k + 1; idx < m; ++idx) {
                int c = word2[idx] - 'a';
                int pos = nxt[cur][c];
                if (pos >= n) { ok = false; break; }
                ans.push_back(pos);
                cur = pos + 1;
            }
            if (ok) return ans;
        }
        // no mismatch needed, exact match possible?
        if (prefPos[m - 1] != -1) {
            vector<int> ans(m);
            for (int i = 0; i < m; ++i) ans[i] = prefPos[i];
            return ans;
        }
        return {};
    }
};
```

## Java

```java
class Solution {
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        char[] w1 = word1.toCharArray();
        char[] w2 = word2.toCharArray();

        int[] dp0 = new int[n + 1]; // exact match suffix length
        int[] dp1 = new int[n + 1]; // at most one mismatch suffix length

        for (int i = n - 1; i >= 0; --i) {
            // dp0 transition
            if (dp0[i + 1] < m && w1[i] == w2[m - dp0[i + 1] - 1]) {
                dp0[i] = dp0[i + 1] + 1;
            } else {
                dp0[i] = dp0[i + 1];
            }

            // dp1 transition
            int best = dp1[i + 1]; // skip current character
            if (dp1[i + 1] < m && w1[i] == w2[m - dp1[i + 1] - 1]) {
                best = Math.max(best, dp1[i + 1] + 1); // match without using mismatch
            }
            best = Math.max(best, 1 + dp0[i + 1]); // use mismatch at this position
            dp1[i] = best;
        }

        if (dp1[0] < m) {
            return new int[0];
        }

        int[] ans = new int[m];
        int ansPos = 0;
        int curIdx = 0;          // next searchable index in word1
        boolean usedMismatch = false;

        for (int k = 0; k < m; ++k) {
            int remaining = m - k - 1;
            int i = curIdx;
            while (i < n) {
                char c1 = w1[i];
                char c2 = w2[k];
                if (!usedMismatch) {
                    if (c1 == c2) {
                        // keep mismatch for later if needed
                        if (dp1[i + 1] >= remaining) {
                            ans[ansPos++] = i;
                            curIdx = i + 1;
                            break;
                        }
                    } else {
                        // use the single allowed mismatch now
                        if (dp0[i + 1] >= remaining) {
                            ans[ansPos++] = i;
                            usedMismatch = true;
                            curIdx = i + 1;
                            break;
                        }
                    }
                } else {
                    // mismatch already used, must match exactly
                    if (c1 == c2 && dp0[i + 1] >= remaining) {
                        ans[ansPos++] = i;
                        curIdx = i + 1;
                        break;
                    }
                }
                ++i;
            }
            if (i == n) { // no feasible index found
                return new int[0];
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n = len(word1)
        m = len(word2)
        # dp[i]: longest suffix of word2 that can be matched as subsequence in word1[i:]
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if dp[i + 1] < m and word1[i] == word2[m - dp[i + 1] - 1]:
                dp[i] = dp[i + 1] + 1
            else:
                dp[i] = dp[i + 1]

        ans = []
        i = 0
        mismatch_used = False

        while i < n and len(ans) < m:
            j = len(ans)          # current position in word2 we need to fill
            rem = m - (j + 1)     # characters remaining after this one

            # Try to take this index as an exact match
            if word1[i] == word2[j]:
                allowed_mismatch = 0 if mismatch_used else 1
                if (rem - dp[i + 1]) <= allowed_mismatch:
                    ans.append(i)
                    i += 1
                    continue

            # Try to take this index as the single allowed mismatch
            if not mismatch_used and dp[i + 1] >= rem:
                ans.append(i)
                mismatch_used = True
                i += 1
                continue

            i += 1

        return ans if len(ans) == m else []
```

## Python3

```python
from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        # dp[i]: longest suffix of word2 that is a subsequence of word1[i:]
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if dp[i + 1] < m and word1[i] == word2[m - dp[i + 1] - 1]:
                dp[i] = dp[i + 1] + 1
            else:
                dp[i] = dp[i + 1]

        # best[i]: longest suffix of word2 that can be matched from i: with at most one mismatch
        best = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            cand = 1 + dp[i + 1]          # use the allowed mismatch at position i
            best[i] = best[i + 1] if best[i + 1] > cand else cand

        ans = []
        pos = 0               # how many characters of word2 have been matched so far
        cur = 0               # current index in word1 to consider
        used_mismatch = False

        while len(ans) < m:
            need = m - len(ans) - 1   # remaining characters after we pick the next one
            found = False
            while cur < n:
                if word1[cur] == word2[pos]:
                    feasible = (best[cur + 1] >= need) if not used_mismatch else (dp[cur + 1] >= need)
                    if feasible:
                        ans.append(cur)
                        pos += 1
                        cur += 1
                        found = True
                        break
                else:
                    if not used_mismatch and dp[cur + 1] >= need:
                        ans.append(cur)
                        pos += 1
                        cur += 1
                        used_mismatch = True
                        found = True
                        break
                cur += 1
            if not found:
                return []
        return ans
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>

int* validSequence(char* word1, char* word2, int* returnSize) {
    int n = (int)strlen(word1);
    int m = (int)strlen(word2);
    *returnSize = 0;
    if (m == 0) return NULL;

    // dp[i] = longest suffix of word2 that can be matched as subsequence in word1[i..]
    int *dp = (int *)malloc((n + 1) * sizeof(int));
    dp[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (dp[i + 1] < m && word1[i] == word2[m - dp[i + 1] - 1])
            dp[i] = dp[i + 1] + 1;
        else
            dp[i] = dp[i + 1];
    }

    int *ans = (int *)malloc(m * sizeof(int));
    int pos = 0;          // position in word2 we are trying to fill
    int i = 0;            // current index in word1
    int used = 0;         // whether the allowed mismatch has been used

    while (pos < m && i < n) {
        int rem = m - pos - 1;   // characters left after taking current position
        if (!used) {
            /* Try to take an exact match */
            if (word1[i] == word2[pos]) {
                if (rem == 0 || dp[i + 1] >= rem - 1) {
                    ans[pos++] = i;
                    ++i;
                    continue;
                }
            }
            /* Use the mismatch at this position */
            if (dp[i + 1] >= rem) {
                ans[pos++] = i;
                used = 1;
                ++i;
                continue;
            }
        } else {
            /* Mismatch already used, must match exactly */
            if (word1[i] == word2[pos] && dp[i + 1] >= rem) {
                ans[pos++] = i;
                ++i;
                continue;
            }
        }
        ++i;
    }

    free(dp);

    if (pos == m) {
        *returnSize = m;
        return ans;
    } else {
        free(ans);
        *returnSize = 0;
        return NULL;
    }
}
```

## Csharp

```csharp
using System;
public class Solution {
    public int[] ValidSequence(string word1, string word2) {
        int n = word1.Length;
        int m = word2.Length;
        char[] w1 = word1.ToCharArray();
        char[] w2 = word2.ToCharArray();

        // exact suffix match DP
        int[] exact = new int[n + 1];
        exact[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (exact[i + 1] < m && w1[i] == w2[m - exact[i + 1] - 1]) {
                exact[i] = exact[i + 1] + 1;
            } else {
                exact[i] = exact[i + 1];
            }
        }

        // at most one mismatch suffix match DP
        int[] one = new int[n + 1];
        one[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (one[i + 1] < m && w1[i] == w2[m - one[i + 1] - 1]) {
                one[i] = one[i + 1] + 1;
            } else {
                int useMismatch = 1 + exact[i + 1];
                if (useMismatch > m) useMismatch = m;
                int skip = one[i + 1];
                one[i] = Math.Max(skip, useMismatch);
                if (one[i] > m) one[i] = m;
            }
        }

        int[] res = new int[m];
        int pos = 0;
        bool used = false;

        for (int i = 0; i < m; i++) {
            int needed = m - (i + 1);
            while (true) {
                if (pos >= n) return new int[0];
                bool matchExact = w1[pos] == w2[i];

                if (!used) {
                    // try exact match first
                    if (matchExact && one[pos + 1] >= needed) {
                        res[i] = pos;
                        pos++;
                        break;
                    }
                    // try using mismatch now
                    if (!matchExact && exact[pos + 1] >= needed) {
                        res[i] = pos;
                        used = true;
                        pos++;
                        break;
                    }
                } else {
                    // mismatch already used, need exact match
                    if (matchExact && exact[pos + 1] >= needed) {
                        res[i] = pos;
                        pos++;
                        break;
                    }
                }
                pos++;
            }
        }

        return res;
    }
}
```

## Javascript

```javascript
/ **
 * @param {string} word1
 * @param {string} word2
 * @return {number[]}
 */
var validSequence = function(word1, word2) {
    const n = word1.length;
    const m = word2.length;
    const INF = n; // sentinel for not found

    // nextPos[c][i] = smallest index >= i where char c appears, or INF
    const nextPos = Array.from({length: 26}, () => new Int32Array(n + 1));
    for (let c = 0; c < 26; ++c) {
        nextPos[c][n] = INF;
    }
    for (let i = n - 1; i >= 0; --i) {
        const chIdx = word1.charCodeAt(i) - 97;
        for (let c = 0; c < 26; ++c) {
            nextPos[c][i] = nextPos[c][i + 1];
        }
        nextPos[chIdx][i] = i;
    }

    // dp[i]: longest suffix of word2 that is a subsequence of word1[i..]
    const dp = new Int32Array(n + 1);
    dp[n] = 0;
    for (let i = n - 1; i >= 0; --i) {
        if (dp[i + 1] < m) {
            const needIdx = m - dp[i + 1] - 1;
            if (word1.charCodeAt(i) === word2.charCodeAt(needIdx)) {
                dp[i] = dp[i + 1] + 1;
                continue;
            }
        }
        dp[i] = dp[i + 1];
    }

    // earliest exact match indices for each prefix of word2
    const preIdx = new Int32Array(m);
    preIdx.fill(-1);
    let pos = 0;
    for (let k = 0; k < m; ++k) {
        const c = word2.charCodeAt(k) - 97;
        const idx = nextPos[c][pos];
        if (idx === INF) break;
        preIdx[k] = idx;
        pos = idx + 1;
    }

    // check full exact match
    let allMatched = true;
    for (let k = 0; k < m; ++k) {
        if (preIdx[k] === -1) { allMatched = false; break; }
    }
    if (allMatched) return Array.from(preIdx);

    // try to place the single mismatch at earliest possible position
    for (let p = 0; p < m; ++p) {
        if (p > 0 && preIdx[p - 1] === -1) break; // prefix not possible
        const lastIdx = p === 0 ? -1 : preIdx[p - 1];
        const mismatchIdx = lastIdx + 1;
        if (mismatchIdx >= n) continue; // no room for mismatch

        const startPos = mismatchIdx + 1; // dp index after taking mismatch
        const remaining = m - p - 1; // length of suffix to match exactly
        if (dp[startPos] < remaining) continue; // cannot complete

        // construct answer
        const ans = new Array(m);
        let cur = 0;
        for (let k = 0; k < p; ++k) ans[cur++] = preIdx[k];
        ans[cur++] = mismatchIdx;

        let curPos = mismatchIdx + 1;
        for (let k = p + 1; k < m; ++k) {
            const c = word2.charCodeAt(k) - 97;
            const idx = nextPos[c][curPos];
            // guaranteed to exist due to dp condition
            ans[cur++] = idx;
            curPos = idx + 1;
        }
        return ans;
    }

    // no valid sequence
    return [];
};
```

## Typescript

```typescript
function validSequence(word1: string, word2: string): number[] {
    const n = word1.length;
    const m = word2.length;
    const dp = new Int32Array(n + 1);
    dp[n] = 0;
    for (let i = n - 1; i >= 0; --i) {
        const nxt = dp[i + 1];
        if (nxt < m && word1.charAt(i) === word2.charAt(m - nxt - 1)) {
            dp[i] = nxt + 1;
        } else {
            dp[i] = nxt;
        }
    }

    const res: number[] = [];
    let j = 0;          // index in word2
    let used = false;   // whether we already used the allowed mismatch

    for (let i = 0; i < n && j < m; ++i) {
        if (word1.charAt(i) === word2.charAt(j)) {
            const need = m - (j + 1);
            if (dp[i + 1] >= need) {
                res.push(i);
                ++j;
                continue;
            }
        } else if (!used) {
            const need = m - (j + 1);
            if (dp[i + 1] >= need) {
                res.push(i);
                ++j;
                used = true;
                continue;
            }
        }
    }

    return j === m ? res : [];
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer[]
     */
    function validSequence($word1, $word2) {
        $n = strlen($word1);
        $m = strlen($word2);
        if ($m == 0) return [];

        // dp[i] = longest suffix of word2 that is a subsequence of word1[i..]
        $dp = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            if ($dp[$i + 1] < $m && $word1[$i] === $word2[$m - $dp[$i + 1] - 1]) {
                $dp[$i] = $dp[$i + 1] + 1;
            } else {
                $dp[$i] = $dp[$i + 1];
            }
        }

        // positions of each character in word1
        $posList = array_fill(0, 26, []);
        for ($i = 0; $i < $n; ++$i) {
            $cIdx = ord($word1[$i]) - 97;
            $posList[$cIdx][] = $i;
        }

        // helper lower bound
        $lowerBound = function(array $arr, int $target): int {
            $l = 0;
            $r = count($arr);
            while ($l < $r) {
                $mid = ($l + $r) >> 1;
                if ($arr[$mid] < $target) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }
            return $l;
        };

        $ans = [];
        $iPos = 0;      // current start index in word1
        $j = 0;         // index in word2
        $used = false; // mismatch used?

        while ($j < $m) {
            $remainingAfter = $m - $j - 1;

            // earliest position where the remaining suffix can be matched
            $candidatePos = $iPos;
            while ($candidatePos < $n && $dp[$candidatePos + 1] < $remainingAfter) {
                ++$candidatePos;
            }
            if ($candidatePos >= $n) {
                return [];
            }

            if (!$used) {
                // try to match exactly
                $cIdx = ord($word2[$j]) - 97;
                $list = $posList[$cIdx];
                $idx = $lowerBound($list, $iPos);
                $posExact = null;
                $lenList = count($list);
                for ($k = $idx; $k < $lenList; ++$k) {
                    $p = $list[$k];
                    if ($dp[$p + 1] >= $remainingAfter) {
                        $posExact = $p;
                        break;
                    }
                }

                // decide
                if ($posExact !== null && $posExact <= $candidatePos) {
                    // exact match gives lexicographically smaller or equal index
                    $ans[] = $posExact;
                    $iPos = $posExact + 1;
                    ++$j;
                    continue;
                } else {
                    // use mismatch at candidatePos
                    $ans[] = $candidatePos;
                    $iPos = $candidatePos + 1;
                    $used = true;
                    ++$j; // consumed this character via mismatch
                    continue;
                }
            } else {
                // mismatch already used, must match exactly
                $cIdx = ord($word2[$j]) - 97;
                $list = $posList[$cIdx];
                $idx = $lowerBound($list, $iPos);
                $posExact = null;
                $lenList = count($list);
                for ($k = $idx; $k < $lenList; ++$k) {
                    $p = $list[$k];
                    if ($dp[$p + 1] >= $remainingAfter) {
                        $posExact = $p;
                        break;
                    }
                }
                if ($posExact === null) {
                    return [];
                }
                $ans[] = $posExact;
                $iPos = $posExact + 1;
                ++$j;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func validSequence(_ word1: String, _ word2: String) -> [Int] {
        let w1 = Array(word1.utf8)
        let w2 = Array(word2.utf8)
        let n = w1.count
        let m = w2.count
        if m == 0 { return [] }
        
        // dp[i]: longest suffix of word2 that is a subsequence of w1[i...]
        var dp = Array(repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let cur = dp[i + 1]
            if cur < m && w1[i] == w2[m - cur - 1] {
                dp[i] = cur + 1
            } else {
                dp[i] = cur
            }
        }
        
        var ans = [Int]()
        var iPos = 0          // current index in word1
        var idx = 0           // current index in word2
        var usedMismatch = false
        
        while idx < m {
            let remainingAfterPick = m - idx - 1   // characters left after we pick one now
            var found = false
            
            while iPos < n {
                if !usedMismatch {
                    if w1[iPos] == w2[idx] {
                        // try to match exactly; we may still use a mismatch later
                        let needExact = remainingAfterPick > 0 ? remainingAfterPick - 1 : 0
                        if dp[iPos + 1] >= needExact {
                            ans.append(iPos)
                            iPos += 1
                            idx += 1
                            found = true
                            break
                        }
                    } else {
                        // use the allowed mismatch now
                        if dp[iPos + 1] >= remainingAfterPick {
                            ans.append(iPos)
                            iPos += 1
                            idx += 1
                            usedMismatch = true
                            found = true
                            break
                        }
                    }
                } else {
                    // mismatch already used; must match exactly
                    if w1[iPos] == w2[idx] && dp[iPos + 1] >= remainingAfterPick {
                        ans.append(iPos)
                        iPos += 1
                        idx += 1
                        found = true
                        break
                    }
                }
                iPos += 1
            }
            
            if !found { return [] }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validSequence(word1: String, word2: String): IntArray {
        val n = word1.length
        val m = word2.length
        if (m == 0) return intArrayOf()
        // next occurrence array
        val nxt = Array(n + 1) { IntArray(26) }
        for (c in 0 until 26) nxt[n][c] = n
        for (i in n - 1 downTo 0) {
            for (c in 0 until 26) {
                nxt[i][c] = nxt[i + 1][c]
            }
            nxt[i][word1[i] - 'a'] = i
        }
        // dp suffix: longest suffix of word2 that can be matched exactly from position i
        val dp = IntArray(n + 1)
        dp[n] = 0
        for (i in n - 1 downTo 0) {
            var v = dp[i + 1]
            if (v < m && word1[i] == word2[m - v - 1]) {
                v++
            }
            dp[i] = v
        }
        // pref positions for exact prefix matches
        val pref = IntArray(m + 1)
        pref[0] = -1
        var curIdx = 0
        var matched = 0
        while (matched < m) {
            if (curIdx >= n) break
            val c = word2[matched] - 'a'
            val nxtPos = nxt[curIdx][c]
            if (nxtPos == n) break
            pref[matched + 1] = nxtPos
            curIdx = nxtPos + 1
            matched++
        }
        val matchedLen = matched
        // exact match possible
        if (matchedLen == m) {
            val res = IntArray(m)
            for (i in 0 until m) res[i] = pref[i + 1]
            return res
        }
        // find best position to place the single mismatch (largest prefix length that works)
        var bestP = -1
        for (p in matchedLen downTo 0) {
            val startIdx = pref[p]          // index of last exact match before mismatch, -1 if p==0
            val mismPos = startIdx + 1      // position we would use as the mismatching character
            if (mismPos >= n) continue     // cannot place mismatch outside string
            val remaining = m - p - 1       // characters after the mismatch that must match exactly
            if (dp[mismPos + 1] >= remaining) {
                bestP = p
                break
            }
        }
        if (bestP == -1) return intArrayOf()
        // build result
        val res = IntArray(m)
        for (i in 0 until bestP) {
            res[i] = pref[i + 1]
        }
        val startIdx = pref[bestP]
        val mismPos = startIdx + 1
        res[bestP] = mismPos
        var cur = mismPos + 1
        for (j in bestP + 1 until m) {
            val c = word2[j] - 'a'
            if (cur > n) return intArrayOf()
            val nxtPos = nxt[cur][c]
            if (nxtPos == n) return intArrayOf()
            res[j] = nxtPos
            cur = nxtPos + 1
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> validSequence(String word1, String word2) {
    int n = word1.length;
    int m = word2.length;
    List<int> dpExact = List.filled(n + 1, 0);
    List<int> dpAllow = List.filled(n + 1, 0);

    for (int i = n - 1; i >= 0; --i) {
      int exNext = dpExact[i + 1];
      if (exNext < m &&
          word1.codeUnitAt(i) == word2.codeUnitAt(m - exNext - 1)) {
        dpExact[i] = exNext + 1;
      } else {
        dpExact[i] = exNext;
      }

      int alNext = dpAllow[i + 1];
      int best = alNext; // skip current character
      if (alNext < m &&
          word1.codeUnitAt(i) == word2.codeUnitAt(m - alNext - 1)) {
        int cand = alNext + 1;
        if (cand > best) best = cand;
      }
      if (exNext < m) {
        int cand = exNext + 1; // use mismatch here
        if (cand > best) best = cand;
      }
      dpAllow[i] = best;
    }

    int iPos = 0;
    bool used = false;
    List<int> ans = [];

    for (int pos = 0; pos < m; ++pos) {
      int rem = m - pos; // characters left including current
      while (true) {
        if (iPos > n) return [];
        bool possible =
            used ? dpExact[iPos] >= rem : dpAllow[iPos] >= rem;
        if (!possible) return [];

        int c1 = word1.codeUnitAt(iPos);
        int c2 = word2.codeUnitAt(pos);

        if (c1 == c2) {
          ans.add(iPos);
          iPos++;
          break;
        } else if (!used && dpExact[iPos + 1] >= rem - 1) {
          // use mismatch here
          ans.add(iPos);
          used = true;
          iPos++;
          break;
        }
        iPos++;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func validSequence(word1 string, word2 string) []int {
    n := len(word1)
    m := len(word2)

    // pre[i]: number of characters of word2 that can be matched using word1[0..i-1]
    pre := make([]int, n+1)
    cur := 0
    for i := 0; i < n; i++ {
        pre[i] = cur
        if cur < m && word1[i] == word2[cur] {
            cur++
        }
    }
    pre[n] = cur

    // If exact subsequence exists, build the lexicographically smallest one.
    if cur == m {
        res := make([]int, 0, m)
        idx := 0
        for j := 0; j < m; j++ {
            for word1[idx] != word2[j] {
                idx++
            }
            res = append(res, idx)
            idx++
        }
        return res
    }

    // dp[i]: longest suffix of word2 that is a subsequence of word1[i..]
    dp := make([]int, n+1) // dp[n] = 0 by default
    for i := n - 1; i >= 0; i-- {
        if dp[i+1] < m && word1[i] == word2[m-dp[i+1]-1] {
            dp[i] = dp[i+1] + 1
        } else {
            dp[i] = dp[i+1]
        }
    }

    // Find earliest position to place the single mismatch.
    missIdx, missPos := -1, -1
    for i := 0; i < n; i++ {
        j := pre[i] // matched before i
        if j < m && dp[i+1] >= m-(j+1) {
            missIdx = i
            missPos = j
            break
        }
    }

    if missIdx == -1 {
        return []int{}
    }

    // Construct the answer using the found mismatch position.
    res := make([]int, 0, m)
    pos := 0
    usedMismatch := false
    for j := 0; j < m; j++ {
        if !usedMismatch && j == missPos {
            // Move to the mismatched index.
            for pos < missIdx {
                pos++
            }
            res = append(res, missIdx)
            usedMismatch = true
            pos = missIdx + 1
            continue
        }
        // Need exact match for word2[j].
        for pos < n && word1[pos] != word2[j] {
            pos++
        }
        if pos >= n {
            return []int{}
        }
        res = append(res, pos)
        pos++
    }

    return res
}
```

## Ruby

```ruby
def valid_sequence(word1, word2)
  n = word1.length
  m = word2.length
  a = word1.bytes
  b = word2.bytes

  # dp[i]: longest suffix of word2 that can be matched as subsequence in a[i..]
  dp = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    if dp[i + 1] < m && a[i] == b[m - dp[i + 1] - 1]
      dp[i] = dp[i + 1] + 1
    else
      dp[i] = dp[i + 1]
    end
  end

  # suffix_max[i]: maximum dp[t] for t >= i
  suffix_max = Array.new(n + 2, -1)
  suffix_max[n] = dp[n]
  (n - 1).downto(0) do |i|
    suffix_max[i] = dp[i] > suffix_max[i + 1] ? dp[i] : suffix_max[i + 1]
  end

  res = []
  i = 0
  j = 0
  mismatch_used = false

  while j < m
    found = false
    while i < n
      remaining_needed = m - (j + 1) # characters left after taking current one
      if a[i] == b[j]
        feasible_exact = dp[i + 1] >= remaining_needed
        feasible_future_mismatch = (!mismatch_used && remaining_needed > 0 && suffix_max[i + 2] >= remaining_needed - 1)
        if feasible_exact || feasible_future_mismatch
          res << i
          i += 1
          j += 1
          found = true
          break
        end
      else
        unless mismatch_used
          if dp[i + 1] >= remaining_needed
            # use the allowed mismatch here
            res << i
            i += 1
            j += 1
            mismatch_used = true
            found = true
            break
          end
        end
      end
      i += 1
    end
    return [] unless found
  end

  res
end
```

## Scala

```scala
object Solution {
    def validSequence(word1: String, word2: String): Array[Int] = {
        val n = word1.length
        val m = word2.length
        if (m == 0) return Array.emptyIntArray

        // dp[i]: longest suffix of word2 that can be matched as subsequence in word1[i..]
        val dp = new Array[Int](n + 1)
        var i = n - 1
        while (i >= 0) {
            if (dp(i + 1) < m && word1.charAt(i) == word2.charAt(m - dp(i + 1) - 1)) {
                dp(i) = dp(i + 1) + 1
            } else {
                dp(i) = dp(i + 1)
            }
            i -= 1
        }

        val res = new Array[Int](m)
        var idx = 0               // position in word2 to fill next
        var usedMismatch = false // whether we already used the allowed mismatch
        var pos = 0               // current index in word1

        while (pos < n && idx < m) {
            val remainingAfterTake = m - idx - 1   // characters left after taking this one
            if (word1.charAt(pos) == word2.charAt(idx)) {
                // exact match candidate
                val feasible = dp(pos + 1) + (if (usedMismatch) 0 else 1) >= remainingAfterTake
                if (feasible) {
                    res(idx) = pos
                    idx += 1
                }
            } else {
                // mismatched character, can be taken only if mismatch not used yet
                if (!usedMismatch) {
                    val feasible = dp(pos + 1) >= remainingAfterTake
                    if (feasible) {
                        res(idx) = pos
                        idx += 1
                        usedMismatch = true
                    }
                }
            }
            pos += 1
        }

        if (idx == m) res else Array.emptyIntArray
    }
}
```

## Rust

```rust
use std::cmp::max;

impl Solution {
    pub fn valid_sequence(word1: String, word2: String) -> Vec<i32> {
        let w1 = word1.as_bytes();
        let w2 = word2.as_bytes();
        let n = w1.len();
        let m = w2.len();

        // dp0[i]: longest suffix of word2 that can be matched exactly from w1[i..]
        // dp1[i]: longest suffix that can be matched with at most one mismatch from w1[i..]
        let mut dp0 = vec![0usize; n + 1];
        let mut dp1 = vec![0usize; n + 1];

        for i in (0..n).rev() {
            // dp0 transition
            let cur0 = dp0[i + 1];
            if cur0 < m && w1[i] == w2[m - cur0 - 1] {
                dp0[i] = cur0 + 1;
            } else {
                dp0[i] = cur0;
            }

            // dp1 transition
            let mut best = dp1[i + 1]; // skip current character

            // exact match extension while still having at most one mismatch allowed
            let cur1 = dp1[i + 1];
            if cur1 < m && w1[i] == w2[m - cur1 - 1] {
                best = max(best, cur1 + 1);
            }

            // use the mismatch now (if not used yet)
            let cand = 1 + dp0[i + 1];
            best = max(best, if cand > m { m } else { cand });

            dp1[i] = if best > m { m } else { best };
        }

        let mut ans: Vec<i32> = Vec::with_capacity(m);
        let mut i_idx: usize = 0;
        let mut j_idx: usize = 0;
        let mut used_mismatch = false;

        while j_idx < m {
            let mut found = false;
            while i_idx < n {
                if w1[i_idx] == w2[j_idx] {
                    // exact match
                    let remaining = m - j_idx - 1;
                    let feasible = if used_mismatch {
                        dp0[i_idx + 1] >= remaining
                    } else {
                        dp1[i_idx + 1] >= remaining
                    };
                    if feasible {
                        ans.push(i_idx as i32);
                        i_idx += 1;
                        j_idx += 1;
                        found = true;
                        break;
                    }
                } else if !used_mismatch {
                    // use mismatch here
                    let remaining = m - j_idx - 1;
                    if dp0[i_idx + 1] >= remaining {
                        ans.push(i_idx as i32);
                        used_mismatch = true;
                        i_idx += 1;
                        j_idx += 1;
                        found = true;
                        break;
                    }
                }
                i_idx += 1;
            }
            if !found {
                return Vec::new();
            }
        }

        ans
    }
}
```

## Racket

```racket
(define (valid-sequence word1 word2)
  (let* ((n (string-length word1))
         (m (string-length word2))
         ;; next-pos[i][c] = smallest index >= i where word1[index] == c, or n if none
         (next-pos (make-vector (+ n 1)))
         ;; dp[i] = length of longest suffix of word2 that is a subsequence of word1[i..]
         (dp (make-vector (+ n 1) 0)))
    ;; initialise next-pos at position n (sentinel)
    (vector-set! next-pos n
                 (let ((v (make-vector 26 n))) v))
    ;; fill next-pos backwards
    (for ([i (in-range (- n 1) -1 -1)])
      (define prev (vector-ref next-pos (+ i 1)))
      (define cur (make-vector 26))
      (for ([c (in-range 26)])
        (vector-set! cur c (vector-ref prev c)))
      (let ((ch-index
             (- (char->integer (string-ref word1 i))
                (char->integer #\a))))
        (vector-set! cur ch-index i))
      (vector-set! next-pos i cur))
    ;; compute dp suffix array
    (for ([i (in-range (- n 1) -1 -1)])
      (define nxt (vector-ref dp (+ i 1)))
      (if (and (< nxt m)
               (= (string-ref word1 i)
                  (string-ref word2 (- m nxt 1))))
          (vector-set! dp i (+ nxt 1))
          (vector-set! dp i nxt)))
    ;; greedy construction
    (let ((res (make-vector m -1))
          (j 0) (cur 0) (used #f) (failed #f))
      (let loop ()
        (if (or (= j m) failed)
            (void)
            (begin
              (define rem (- m j))
              (define c2 (string-ref word2 j))
              (define cidx
                (- (char->integer c2) (char->integer #\a)))
              ;; exact match candidate
              (define idxExact
                (let ((vec (vector-ref next-pos cur))) (vector-ref vec cidx)))
              (define feasExact
                (and (< idxExact n)
                     (>= (vector-ref dp (+ idxExact 1)) (- rem 1))))
              ;; mismatch candidate (if still allowed)
              (define idxMis
                (if used
                    n
                    (let loop2 ((p cur))
                      (if (or (>= p n)
                              (>= (vector-ref dp (+ p 1)) (- rem 1)))
                          p
                          (loop2 (+ p 1))))))
              (define feasMis (and (not used) (< idxMis n)))
              (cond
                [(and feasExact (or (not feasMis) (<= idxExact idxMis)))
                 (vector-set! res j idxExact)
                 (set! cur (+ idxExact 1))
                 (set! j (+ j 1))]
                [feasMis
                 (vector-set! res j idxMis)
                 (set! cur (+ idxMis 1))
                 (set! used #t)
                 (set! j (+ j 1))]
                [else
                 (set! failed #t)]))
              (unless failed (loop)))))
      (if (or failed (for/or ([k (in-range m)]) (= (vector-ref res k) -1)))
          '()
          (let ((out '()))
            (for ([k (in-range m)])
              (set! out (cons (vector-ref res k) out)))
            (reverse out))))))
```

## Erlang

```erlang
-spec valid_sequence(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> [integer()].
valid_sequence(Word1, Word2) ->
    N = byte_size(Word1),
    M = byte_size(Word2),
    DP = build_dp(Word1, Word2, N, M, []),
    case select_seq(DP, Word1, Word2, N, M) of
        {ok, Res} -> Res;
        error -> []
    end.

%% Build dp tuple where dp[i] is the longest suffix length of Word2 that can be matched as subsequence in Word1[i..]
build_dp(_Word1, _Word2, 0, _M, Acc) ->
    list_to_tuple(lists:reverse([0 | Acc])); % dp[0] will be at position 1
build_dp(Word1, Word2, N, M, Acc) ->
    %% start from i = N-1 down to 0, with Next being dp[i+1]
    build_dp_rev(N - 1, Word1, Word2, N, M, [0], Acc).

build_dp_rev(-1, _Word1, _Word2, _N, _M, DPList, Acc) ->
    list_to_tuple(lists:reverse(DPList ++ Acc));
build_dp_rev(I, Word1, Word2, N, M, [Next | Rest] = DPList, Acc) ->
    Char1 = binary:at(Word1, I),
    Cur =
        if
            Next < M,
            Char1 == binary:at(Word2, M - Next - 1) -> Next + 1;
            true -> Next
        end,
    build_dp_rev(I - 1, Word1, Word2, N, M, [Cur | DPList], Acc).

%% Greedy selection of indices
select_seq(DP, Word1, Word2, N, M) ->
    select_seq(0, 0, false, [], DP, Word1, Word2, N, M).

select_seq(_J, _Pos, _MismatchUsed, Acc, _DP, _Word1, _Word2, _N, M) when length(Acc) =:= M ->
    {ok, lists:reverse(Acc)};
select_seq(J, Pos, MismatchUsed, Acc, DP, Word1, Word2, N, M) ->
    NeedChar = binary:at(Word2, J),
    RemainingLen = M - (J + 1),
    case find_index(Pos, NeedChar, RemainingLen, MismatchUsed, DP, Word1, N) of
        {found, Index, NewMismatch} ->
            select_seq(J + 1, Index + 1, NewMismatch, [Index | Acc], DP, Word1, Word2, N, M);
        not_found ->
            error
    end.

%% Find the smallest index >= Start satisfying conditions
find_index(Start, NeedChar, RemLen, MismatchUsed, DP, Word1, N) ->
    find_index_loop(Start, NeedChar, RemLen, MismatchUsed, DP, Word1, N).

find_index_loop(I, _NeedChar, _RemLen, _MismatchUsed, _DP, _Word1, N) when I >= N ->
    not_found;
find_index_loop(I, NeedChar, RemLen, MismatchUsed, DP, Word1, N) ->
    RestOk = element(I + 2, DP) >= RemLen, % DP tuple is 1‑based, dp[i+1] at position i+2
    if
        not RestOk ->
            find_index_loop(I + 1, NeedChar, RemLen, MismatchUsed, DP, Word1, N);
        true ->
            Char = binary:at(Word1, I),
            case MismatchUsed of
                true ->
                    if Char == NeedChar ->
                        {found, I, true};
                       true ->
                        find_index_loop(I + 1, NeedChar, RemLen, MismatchUsed, DP, Word1, N)
                    end;
                false ->
                    if Char == NeedChar ->
                        {found, I, false};
                       true ->
                        % use mismatch here
                        {found, I, true}
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_sequence(word1 :: String.t(), word2 :: String.t()) :: [integer]
  def valid_sequence(word1, word2) do
    n = byte_size(word1)
    m = byte_size(word2)

    # helper to get byte at index
    get_byte = fn bin, idx -> :binary.at(bin, idx) end

    # positions of each character in word1
    pos_map =
      0..(n - 1)
      |> Enum.reduce(%{}, fn i, acc ->
        c = get_byte.(word1, i) - ?a
        Map.update(acc, c, [i], &[i | &1])
      end)
      |> Enum.map(fn {k, v} -> {k, Enum.reverse(v)} end)
      |> Enum.into(%{})

    # binary search for first element > value in a sorted list
    next_greater = fn list, val ->
      :lists.foldl(
        fn x, acc ->
          if x > val and (acc == nil or x < elem(acc, 0)), do: {x, true}, else: acc
        end,
        nil,
        list
      )
      |> case do
        nil -> nil
        {idx, _} -> idx
      end
    end

    # compute dp: longest suffix of word2 that can be matched exactly from i
    dp = :array.new(n + 1, default: 0)
    dp = :array.set(dp, n, 0)

    dp =
      Enum.reduce((n - 1)..0, dp, fn i, arr ->
        cur_len = :array.get(arr, i + 1)

        if cur_len < m and get_byte.(word1, i) == get_byte.(word2, m - cur_len - 1) do
          :array.set(arr, i, cur_len + 1)
        else
          :array.set(arr, i, cur_len)
        end
      end)

    # earliest exact match positions (pref)
    pref =
      Enum.reduce(0..(m - 1), {[], 0}, fn idx, {list, pos} ->
        ch = get_byte.(word2, idx) - ?a

        case Map.get(pos_map, ch) do
          nil -> {[nil | list], n}
          lst ->
            nxt =
              Enum.find(lst, fn x -> x >= pos end)

            if nxt == nil do
              {[nil | list], n}
            else
              {[nxt | list], nxt + 1}
            end
        end
      end)
      |> elem(0)
      |> Enum.reverse()

    # latest exact match positions (suff)
    suff = List.duplicate(nil, m)

    {suff, _} =
      Enum.reduce((n - 1)..0, {suff, m - 1}, fn i, {arr, j} ->
        if j >= 0 and get_byte.(word1, i) == get_byte.(word2, j) do
          arr = List.replace_at(arr, j, i)
          {arr, j - 1}
        else
          {arr, j}
        end
      end)

    # helper to compare two sequences lexicographically
    less_seq = fn a, b ->
      Enum.zip(a, b)
      |> Enum.reduce_while(:eq, fn
        {x, y}, :eq when x < y -> {:halt, true}
        {x, y}, :eq when x > y -> {:halt, false}
        _, :eq -> {:cont, :eq}
      end) == true
    end

    best = nil

    # case without mismatch
    if Enum.all?(pref, &(&1 != nil)) do
      best = pref
    end

    # iterate possible mismatch positions
    0..(m - 1)
    |> Enum.reduce_while(nil, fn k, _acc ->
      # prefix must exist up to k-1
      if k > 0 and Enum.at(pref, k - 1) == nil do
        {:halt, best}
      else
        pre_idx = if k == 0, do: -1, else: Enum.at(pref, k - 1)
        next_limit =
          if k == m - 1 do
            n
          else
            Enum.at(suff, k + 1) || -1
          end

        i_candidate = pre_idx + 1

        cond do
          i_candidate >= next_limit or i_candidate >= n ->
            {:cont, best}

          true ->
            # build sequence
            prefix_part = if k == 0, do: [], else: Enum.slice(pref, 0, k)
            seq_start = prefix_part ++ [i_candidate]

            # build suffix using binary search lists
            start_pos = i_candidate + 1

            suffix_seq =
              Enum.reduce_while((k + 1)..(m - 1), {start_pos, []}, fn idx, {cur, acc} ->
                ch = get_byte.(word2, idx) - ?a
                lst = Map.get(pos_map, ch, [])

                nxt = next_greater.(lst, cur - 1)

                if nxt == nil do
                  {:halt, :fail}
                else
                  {:cont, {nxt + 1, acc ++ [nxt]}}
                end
              end)

            case suffix_seq do
              :fail ->
                {:cont, best}

              {_pos_end, suffix_part} ->
                candidate = seq_start ++ suffix_part

                new_best =
                  cond do
                    best == nil -> candidate
                    less_seq.(candidate, best) -> candidate
                    true -> best
                  end

                {:cont, new_best}
            end
        end
      end
    end)

    case best do
      nil -> []
      seq -> seq
    end
  end
end
```
