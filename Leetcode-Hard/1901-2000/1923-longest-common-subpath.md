# 1923. Longest Common Subpath

## Cpp

```cpp
class Solution {
public:
    using ull = unsigned long long;
    
    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        int m = paths.size();
        int minLen = INT_MAX, maxLen = 0;
        for (auto &p : paths) {
            minLen = min(minLen, (int)p.size());
            maxLen = max(maxLen, (int)p.size());
        }
        if (minLen == 0) return 0;
        
        const ull BASE = 1000003ULL; // a prime larger than n
        vector<ull> powBase(maxLen + 1);
        powBase[0] = 1;
        for (int i = 1; i <= maxLen; ++i) powBase[i] = powBase[i - 1] * BASE;
        
        // prefix hashes for each path
        vector<vector<ull>> pref(m);
        for (int i = 0; i < m; ++i) {
            int sz = paths[i].size();
            pref[i].resize(sz + 1, 0);
            for (int j = 0; j < sz; ++j) {
                // add 1 to value to avoid zero issues
                pref[i][j + 1] = pref[i][j] * BASE + (ull)(paths[i][j] + 1);
            }
        }
        
        auto getHash = [&](int idx, int l, int r) -> ull {
            // hash of subarray [l, r)
            return pref[idx][r] - pref[idx][l] * powBase[r - l];
        };
        
        auto ok = [&](int L) -> bool {
            if (L == 0) return true;
            unordered_set<ull> common;
            // first path
            int sz0 = paths[0].size();
            for (int i = 0; i + L <= sz0; ++i) {
                common.insert(getHash(0, i, i + L));
            }
            if (common.empty()) return false;
            
            // intersect with other paths
            for (int p = 1; p < m; ++p) {
                unordered_set<ull> nxt;
                int sz = paths[p].size();
                for (int i = 0; i + L <= sz; ++i) {
                    ull h = getHash(p, i, i + L);
                    if (common.find(h) != common.end()) {
                        nxt.insert(h);
                    }
                }
                common.swap(nxt);
                if (common.empty()) return false;
            }
            return !common.empty();
        };
        
        int lo = 0, hi = minLen;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD1 = 1_000_000_007L;
    private static final long MOD2 = 1_000_000_009L;
    private static final long BASE = 91138233L;

    public int longestCommonSubpath(int n, int[][] paths) {
        int m = paths.length;
        int minLen = Integer.MAX_VALUE;
        for (int[] p : paths) {
            minLen = Math.min(minLen, p.length);
        }
        if (minLen == 0) return 0;

        // precompute powers up to minLen
        long[] pow1 = new long[minLen + 1];
        long[] pow2 = new long[minLen + 1];
        pow1[0] = pow2[0] = 1;
        for (int i = 1; i <= minLen; i++) {
            pow1[i] = (pow1[i - 1] * BASE) % MOD1;
            pow2[i] = (pow2[i - 1] * BASE) % MOD2;
        }

        int low = 0, high = minLen + 1; // exclusive upper bound
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (existsCommon(paths, mid, pow1, pow2)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low - 1;
    }

    private boolean existsCommon(int[][] paths, int len,
                                 long[] pow1, long[] pow2) {
        if (len == 0) return true;
        HashSet<Long> common = null;

        for (int[] path : paths) {
            if (path.length < len) return false;

            // prefix hashes
            int L = path.length;
            long[] pref1 = new long[L + 1];
            long[] pref2 = new long[L + 1];
            for (int i = 0; i < L; i++) {
                pref1[i + 1] = (pref1[i] * BASE + path[i]) % MOD1;
                pref2[i + 1] = (pref2[i] * BASE + path[i]) % MOD2;
            }

            HashSet<Long> cur = new HashSet<>();
            for (int i = 0; i + len <= L; i++) {
                long h1 = (pref1[i + len] - pref1[i] * pow1[len]) % MOD1;
                if (h1 < 0) h1 += MOD1;
                long h2 = (pref2[i + len] - pref2[i] * pow2[len]) % MOD2;
                if (h2 < 0) h2 += MOD2;
                long key = (h1 << 32) | h2;
                cur.add(key);
            }

            if (common == null) {
                common = cur;
            } else {
                // intersect common with cur
                HashSet<Long> next = new HashSet<>();
                // iterate over smaller set for efficiency
                if (common.size() <= cur.size()) {
                    for (Long h : common) {
                        if (cur.contains(h)) next.add(h);
                    }
                } else {
                    for (Long h : cur) {
                        if (common.contains(h)) next.add(h);
                    }
                }
                common = next;
                if (common.isEmpty()) return false;
            }
        }
        return !common.isEmpty();
    }
}
```

## Python

```python
class Solution(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        if not paths:
            return 0

        min_len = min(len(p) for p in paths)
        max_len = max(len(p) for p in paths)

        MOD1 = 1000000007
        MOD2 = 1000000009
        BASE = 100007  # a prime larger than n

        # precompute powers
        pow1 = [1] * (max_len + 1)
        pow2 = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow1[i] = (pow1[i - 1] * BASE) % MOD1
            pow2[i] = (pow2[i - 1] * BASE) % MOD2

        def has_common(L):
            if L == 0:
                return True
            common_hashes = None
            for path in paths:
                if len(path) < L:
                    return False
                cur_set = set()
                h1 = 0
                h2 = 0
                # initial window
                for i in range(L):
                    h1 = (h1 * BASE + path[i]) % MOD1
                    h2 = (h2 * BASE + path[i]) % MOD2
                cur_set.add((h1 << 32) ^ h2)
                powL1 = pow1[L]
                powL2 = pow2[L]
                for i in range(L, len(path)):
                    # slide window: remove path[i-L], add path[i]
                    h1 = (h1 * BASE + path[i] - path[i - L] * powL1) % MOD1
                    h2 = (h2 * BASE + path[i] - path[i - L] * powL2) % MOD2
                    cur_set.add((h1 << 32) ^ h2)
                if common_hashes is None:
                    common_hashes = cur_set
                else:
                    # intersect
                    common_hashes &= cur_set
                    if not common_hashes:
                        return False
            return bool(common_hashes)

        low, high = 0, min_len + 1  # [low, high)
        while low < high:
            mid = (low + high) // 2
            if has_common(mid):
                low = mid + 1
            else:
                high = mid
        return low - 1
```

## Python3

```python
import sys
import random
from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        if not paths:
            return 0
        m = len(paths)
        min_len = min(len(p) for p in paths)
        max_len = max(len(p) for p in paths)

        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE = random.randint(100000, 200000)

        # precompute powers
        pow1 = [1] * (max_len + 1)
        pow2 = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow1[i] = (pow1[i-1] * BASE) % MOD1
            pow2[i] = (pow2[i-1] * BASE) % MOD2

        # prefix hashes for each path
        prefixes = []
        for arr in paths:
            pre1 = [0]
            pre2 = [0]
            for v in arr:
                # add 1 to value to avoid leading zeros effect
                x = v + 1
                pre1.append((pre1[-1] * BASE + x) % MOD1)
                pre2.append((pre2[-1] * BASE + x) % MOD2)
            prefixes.append((pre1, pre2))

        def possible(L: int) -> bool:
            if L == 0:
                return True
            common = None
            powL1 = pow1[L]
            powL2 = pow2[L]
            for arr, (pre1, pre2) in zip(paths, prefixes):
                if len(arr) < L:
                    return False
                cur = set()
                limit = len(arr) - L + 1
                for i in range(limit):
                    h1 = (pre1[i+L] - pre1[i] * powL1) % MOD1
                    h2 = (pre2[i+L] - pre2[i] * powL2) % MOD2
                    cur.add((h1, h2))
                if common is None:
                    common = cur
                else:
                    common.intersection_update(cur)
                    if not common:
                        return False
            return True

        low, high = 0, min_len + 1
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                low = mid + 1
            else:
                high = mid
        return low - 1
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static const uint32_t MOD1 = 1000000007U;
static const uint32_t MOD2 = 1000000009U;
static const uint32_t BASE = 100007U;

int compare_uint64(const void *a, const void *b) {
    uint64_t va = *(const uint64_t *)a;
    uint64_t vb = *(const uint64_t *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

/* check whether there exists a common subpath of length L */
static int hasCommon(int n, int **paths, int pathsSize, int *pathsColSize,
                     uint32_t *pow1, uint32_t *pow2, int L) {
    if (L == 0) return 1;
    uint64_t *common = NULL;
    int commonSize = 0;

    for (int i = 0; i < pathsSize; ++i) {
        int len = pathsColSize[i];
        if (len < L) {               // impossible
            free(common);
            return 0;
        }
        int cnt = len - L + 1;
        uint64_t *hashes = (uint64_t *)malloc(cnt * sizeof(uint64_t));
        if (!hashes) exit(1);

        /* compute rolling hashes for this path */
        uint32_t h1 = 0, h2 = 0;
        for (int j = 0; j < L; ++j) {
            uint32_t val = (uint32_t)(paths[i][j] + 1);
            h1 = ( (uint64_t)h1 * BASE + val ) % MOD1;
            h2 = ( (uint64_t)h2 * BASE + val ) % MOD2;
        }
        hashes[0] = ((uint64_t)h1 << 32) ^ h2;

        for (int start = 1; start < cnt; ++start) {
            uint32_t oldVal = (uint32_t)(paths[i][start - 1] + 1);
            uint32_t newVal = (uint32_t)(paths[i][start + L - 1] + 1);

            // remove old contribution
            uint64_t sub = ((uint64_t)oldVal * pow1[L]) % MOD1;
            h1 = (h1 + MOD1 - sub) % MOD1;
            // add new char
            h1 = ( (uint64_t)h1 * BASE + newVal ) % MOD1;

            sub = ((uint64_t)oldVal * pow2[L]) % MOD2;
            h2 = (h2 + MOD2 - sub) % MOD2;
            h2 = ( (uint64_t)h2 * BASE + newVal ) % MOD2;

            hashes[start] = ((uint64_t)h1 << 32) ^ h2;
        }

        /* sort and deduplicate */
        qsort(hashes, cnt, sizeof(uint64_t), compare_uint64);
        int uniq = 0;
        for (int j = 0; j < cnt; ++j) {
            if (j == 0 || hashes[j] != hashes[uniq - 1])
                hashes[uniq++] = hashes[j];
        }

        if (i == 0) {
            common = (uint64_t *)malloc(uniq * sizeof(uint64_t));
            memcpy(common, hashes, uniq * sizeof(uint64_t));
            commonSize = uniq;
        } else {
            int newSize = (commonSize < uniq) ? commonSize : uniq;
            uint64_t *inter = (uint64_t *)malloc(newSize * sizeof(uint64_t));
            int p1 = 0, p2 = 0, k = 0;
            while (p1 < commonSize && p2 < uniq) {
                if (common[p1] == hashes[p2]) {
                    inter[k++] = common[p1];
                    ++p1; ++p2;
                } else if (common[p1] < hashes[p2]) {
                    ++p1;
                } else {
                    ++p2;
                }
            }
            free(common);
            common = inter;
            commonSize = k;
        }

        free(hashes);
        if (commonSize == 0) {
            return 0;
        }
    }

    free(common);
    return 1;
}

int longestCommonSubpath(int n, int** paths, int pathsSize, int* pathsColSize){
    int minLen = INT_MAX, maxLen = 0;
    for (int i = 0; i < pathsSize; ++i) {
        if (pathsColSize[i] < minLen) minLen = pathsColSize[i];
        if (pathsColSize[i] > maxLen) maxLen = pathsColSize[i];
    }
    /* precompute powers */
    uint32_t *pow1 = (uint32_t *)malloc((maxLen + 1) * sizeof(uint32_t));
    uint32_t *pow2 = (uint32_t *)malloc((maxLen + 1) * sizeof(uint32_t));
    pow1[0] = pow2[0] = 1;
    for (int i = 1; i <= maxLen; ++i) {
        pow1[i] = ((uint64_t)pow1[i-1] * BASE) % MOD1;
        pow2[i] = ((uint64_t)pow2[i-1] * BASE) % MOD2;
    }

    int lo = 0, hi = minLen;
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (hasCommon(n, paths, pathsSize, pathsColSize, pow1, pow2, mid))
            lo = mid;
        else
            hi = mid - 1;
    }

    free(pow1);
    free(pow2);
    return lo;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestCommonSubpath(int n, int[][] paths) {
        int m = paths.Length;
        int minLen = int.MaxValue;
        foreach (var p in paths) if (p.Length < minLen) minLen = p.Length;

        const ulong BASE = 1000003UL;
        ulong[] pow = new ulong[minLen + 1];
        pow[0] = 1;
        for (int i = 1; i <= minLen; i++) pow[i] = pow[i - 1] * BASE;

        var prefixes = new List<ulong[]>(m);
        foreach (var arr in paths) {
            int len = arr.Length;
            ulong[] pref = new ulong[len + 1];
            for (int i = 0; i < len; i++) {
                pref[i + 1] = pref[i] * BASE + (ulong)(arr[i] + 1);
            }
            prefixes.Add(pref);
        }

        bool Check(int L) {
            if (L == 0) return true;
            HashSet<ulong> common = null;
            for (int idx = 0; idx < m; idx++) {
                int len = paths[idx].Length;
                if (len < L) return false;
                var pref = prefixes[idx];
                var curSet = new HashSet<ulong>();
                for (int start = 0; start <= len - L; ++start) {
                    ulong hash = pref[start + L] - pref[start] * pow[L];
                    if (common == null || common.Contains(hash)) {
                        curSet.Add(hash);
                    }
                }
                common = curSet;
                if (common.Count == 0) return false;
            }
            return true;
        }

        int lo = 0, hi = minLen + 1;
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (Check(mid)) lo = mid;
            else hi = mid;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} paths
 * @return {number}
 */
var longestCommonSubpath = function(n, paths) {
    const MOD1 = 1000000007;
    const MOD2 = 1000000009;
    const BASE = 100007;

    // find min and max path lengths
    let minLen = Infinity, maxLen = 0;
    for (const p of paths) {
        if (p.length < minLen) minLen = p.length;
        if (p.length > maxLen) maxLen = p.length;
    }
    if (minLen === 0) return 0;

    // precompute powers
    const pow1 = new Array(maxLen + 1);
    const pow2 = new Array(maxLen + 1);
    pow1[0] = 1; pow2[0] = 1;
    for (let i = 1; i <= maxLen; ++i) {
        pow1[i] = (pow1[i - 1] * BASE) % MOD1;
        pow2[i] = (pow2[i - 1] * BASE) % MOD2;
    }

    // compute prefix hashes for each path once
    const pref = paths.map(arr => {
        const pre1 = new Array(arr.length + 1);
        const pre2 = new Array(arr.length + 1);
        pre1[0] = 0; pre2[0] = 0;
        for (let i = 0; i < arr.length; ++i) {
            // add 1 to avoid leading zeros effect
            const val = arr[i] + 1;
            pre1[i + 1] = (pre1[i] * BASE + val) % MOD1;
            pre2[i + 1] = (pre2[i] * BASE + val) % MOD2;
        }
        return [pre1, pre2];
    });

    const check = (len) => {
        if (len === 0) return true;
        const countMap = new Map(); // key -> number of paths containing it
        for (let idx = 0; idx < paths.length; ++idx) {
            const arr = paths[idx];
            if (arr.length < len) return false;
            const [pre1, pre2] = pref[idx];
            const localSet = new Set();
            for (let i = 0; i + len <= arr.length; ++i) {
                const j = i + len;
                let h1 = (pre1[j] - (pre1[i] * pow1[len]) % MOD1);
                if (h1 < 0) h1 += MOD1;
                let h2 = (pre2[j] - (pre2[i] * pow2[len]) % MOD2);
                if (h2 < 0) h2 += MOD2;
                const key = h1 + ',' + h2;
                localSet.add(key);
            }
            // update global counts
            for (const key of localSet) {
                const prev = countMap.get(key) || 0;
                countMap.set(key, prev + 1);
            }
        }
        // check if any hash appears in all paths
        for (const cnt of countMap.values()) {
            if (cnt === paths.length) return true;
        }
        return false;
    };

    let low = 0, high = minLen;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (check(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function longestCommonSubpath(n: number, paths: number[][]): number {
    const m = paths.length;
    let minLen = Infinity;
    for (const p of paths) if (p.length < minLen) minLen = p.length;

    const maxLen = Math.max(...paths.map(p => p.length));
    const BASE = 91138233n;
    const MOD1 = 1000000007n;
    const MOD2 = 1000000009n;

    const pow1: bigint[] = new Array(maxLen + 1);
    const pow2: bigint[] = new Array(maxLen + 1);
    pow1[0] = 1n;
    pow2[0] = 1n;
    for (let i = 1; i <= maxLen; i++) {
        pow1[i] = (pow1[i - 1] * BASE) % MOD1;
        pow2[i] = (pow2[i - 1] * BASE) % MOD2;
    }

    const prefixes = paths.map(p => {
        const h1: bigint[] = new Array(p.length + 1);
        const h2: bigint[] = new Array(p.length + 1);
        h1[0] = 0n;
        h2[0] = 0n;
        for (let i = 0; i < p.length; i++) {
            h1[i + 1] = (h1[i] * BASE + BigInt(p[i])) % MOD1;
            h2[i + 1] = (h2[i] * BASE + BigInt(p[i])) % MOD2;
        }
        return { h1, h2 };
    });

    function hasCommon(L: number): boolean {
        if (L === 0) return true;
        const countMap = new Map<string, number>();
        for (let idx = 0; idx < m; idx++) {
            const p = paths[idx];
            if (p.length < L) return false;
            const { h1, h2 } = prefixes[idx];
            const seen = new Set<string>();
            for (let i = 0; i <= p.length - L; i++) {
                let cur1 = (h1[i + L] - (h1[i] * pow1[L]) % MOD1) % MOD1;
                if (cur1 < 0) cur1 += MOD1;
                let cur2 = (h2[i + L] - (h2[i] * pow2[L]) % MOD2) % MOD2;
                if (cur2 < 0) cur2 += MOD2;
                const key = cur1.toString() + '_' + cur2.toString();
                seen.add(key);
            }
            for (const key of seen) {
                const cnt = countMap.get(key) ?? 0;
                if (cnt === idx) {
                    countMap.set(key, cnt + 1);
                }
            }
        }
        for (const cnt of countMap.values()) {
            if (cnt === m) return true;
        }
        return false;
    }

    let low = 0, high = minLen;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (hasCommon(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $paths
     * @return Integer
     */
    function longestCommonSubpath($n, $paths) {
        $mod1 = 1000000007;
        $mod2 = 1000000009;
        $base = 91138233; // large random base

        $minLen = PHP_INT_MAX;
        $maxLen = 0;
        foreach ($paths as $p) {
            $len = count($p);
            if ($len < $minLen) $minLen = $len;
            if ($len > $maxLen) $maxLen = $len;
        }

        // pre‑compute powers
        $pow1 = [1];
        $pow2 = [1];
        for ($i = 1; $i <= $maxLen; $i++) {
            $pow1[$i] = (int)(($pow1[$i-1] * $base) % $mod1);
            $pow2[$i] = (int)(($pow2[$i-1] * $base) % $mod2);
        }

        // binary search on answer length
        $lo = 0;
        $hi = $minLen;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->hasCommon($paths, $mid, $base, $mod1, $mod2, $pow1, $pow2)) {
                $lo = $mid;
            } else {
                $hi = $mid - 1;
            }
        }
        return $lo;
    }

    private function hasCommon($paths, $len, $base, $mod1, $mod2, &$pow1, &$pow2) {
        if ($len == 0) return true;

        $common = null; // associative array of hashes present in all processed paths

        foreach ($paths as $path) {
            $m = count($path);
            if ($len > $m) return false;

            // prefix hashes
            $pref1 = [0];
            $pref2 = [0];
            foreach ($path as $v) {
                $last1 = end($pref1);
                $last2 = end($pref2);
                $pref1[] = (int)((($last1 * $base) + $v + 1) % $mod1);
                $pref2[] = (int)((($last2 * $base) + $v + 1) % $mod2);
            }

            // collect all subpath hashes of length $len
            $set = [];
            for ($i = 0; $i <= $m - $len; $i++) {
                $h1 = $pref1[$i + $len] - (int)(($pref1[$i] * $pow1[$len]) % $mod1);
                if ($h1 < 0) $h1 += $mod1;
                $h2 = $pref2[$i + $len] - (int)(($pref2[$i] * $pow2[$len]) % $mod2);
                if ($h2 < 0) $h2 += $mod2;
                $key = $h1 . ':' . $h2;
                $set[$key] = true;
            }

            if ($common === null) {
                $common = $set;
            } else {
                // intersect with previous common set
                foreach ($common as $k => $_) {
                    if (!isset($set[$k])) {
                        unset($common[$k]);
                    }
                }
                if (empty($common)) return false;
            }
        }

        return !empty($common);
    }
}
```

## Swift

```swift
class Solution {
    func longestCommonSubpath(_ n: Int, _ paths: [[Int]]) -> Int {
        let base: UInt64 = 1000003
        let minLen = paths.map { $0.count }.min() ?? 0
        var low = 0
        var high = minLen

        func hasCommon(_ length: Int) -> Bool {
            if length == 0 { return true }
            var pow: UInt64 = 1
            for _ in 0..<length {
                pow = pow &* base
            }
            var commonSet: Set<UInt64>? = nil

            for path in paths {
                let m = path.count
                if m < length { return false }
                var pref = [UInt64](repeating: 0, count: m + 1)
                for i in 0..<m {
                    pref[i + 1] = (pref[i] &* base) &+ UInt64(path[i])
                }
                var curSet = Set<UInt64>()
                let limit = m - length
                for i in 0...limit {
                    let h = pref[i + length] &- (pref[i] &* pow)
                    curSet.insert(h)
                }
                if commonSet == nil {
                    commonSet = curSet
                } else {
                    var newCommon = Set<UInt64>()
                    if curSet.count < commonSet!.count {
                        for h in curSet where commonSet!.contains(h) {
                            newCommon.insert(h)
                        }
                    } else {
                        for h in commonSet! where curSet.contains(h) {
                            newCommon.insert(h)
                        }
                    }
                    commonSet = newCommon
                    if commonSet!.isEmpty { return false }
                }
            }
            return !(commonSet?.isEmpty ?? true)
        }

        while low < high {
            let mid = (low + high + 1) / 2
            if hasCommon(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
import java.util.HashSet

class Solution {
    private val MOD1 = 1_000_000_007L
    private val MOD2 = 1_000_000_009L
    private val BASE = 100_007L

    fun longestCommonSubpath(n: Int, paths: Array<IntArray>): Int {
        var minLen = Int.MAX_VALUE
        for (p in paths) if (p.size < minLen) minLen = p.size
        // precompute powers up to minLen
        val pow1 = LongArray(minLen + 1)
        val pow2 = LongArray(minLen + 1)
        pow1[0] = 1L
        pow2[0] = 1L
        for (i in 1..minLen) {
            pow1[i] = (pow1[i - 1] * BASE) % MOD1
            pow2[i] = (pow2[i - 1] * BASE) % MOD2
        }

        fun check(len: Int): Boolean {
            if (len == 0) return true
            var common: HashSet<Long>? = null
            for (path in paths) {
                val sz = path.size
                if (len > sz) return false
                // prefix hashes
                val pref1 = LongArray(sz + 1)
                val pref2 = LongArray(sz + 1)
                for (i in 0 until sz) {
                    pref1[i + 1] = (pref1[i] * BASE + path[i]) % MOD1
                    pref2[i + 1] = (pref2[i] * BASE + path[i]) % MOD2
                }
                val curSet = HashSet<Long>()
                for (i in 0..sz - len) {
                    var h1 = (pref1[i + len] - (pref1[i] * pow1[len]) % MOD1)
                    if (h1 < 0) h1 += MOD1
                    var h2 = (pref2[i + len] - (pref2[i] * pow2[len]) % MOD2)
                    if (h2 < 0) h2 += MOD2
                    val combined = (h1 shl 32) xor h2
                    if (common == null) {
                        curSet.add(combined)
                    } else if (common.contains(combined)) {
                        curSet.add(combined)
                    }
                }
                if (curSet.isEmpty()) return false
                common = curSet
            }
            return true
        }

        var low = 0
        var high = minLen
        while (low < high) {
            val mid = (low + high + 1) ushr 1
            if (check(mid)) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod1 = 1000000007;
  static const int _mod2 = 1000000009;
  static const int _base = 100007;

  int longestCommonSubpath(int n, List<List<int>> paths) {
    if (paths.isEmpty) return 0;
    int minLen = paths[0].length;
    for (var p in paths) {
      if (p.length < minLen) minLen = p.length;
    }

    // precompute powers up to minLen
    List<int> pow1 = List.filled(minLen + 1, 0);
    List<int> pow2 = List.filled(minLen + 1, 0);
    pow1[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i <= minLen; ++i) {
      pow1[i] = (pow1[i - 1] * _base) % _mod1;
      pow2[i] = (pow2[i - 1] * _base) % _mod2;
    }

    bool check(int L) {
      if (L == 0) return true;
      Set<int> common = {};
      bool firstPath = true;

      for (var path in paths) {
        int len = path.length;
        if (len < L) return false;

        // prefix hashes
        List<int> pre1 = List.filled(len + 1, 0);
        List<int> pre2 = List.filled(len + 1, 0);
        for (int i = 0; i < len; ++i) {
          pre1[i + 1] = ((pre1[i] * _base) + path[i]) % _mod1;
          pre2[i + 1] = ((pre2[i] * _base) + path[i]) % _mod2;
        }

        Set<int> curSet = {};
        for (int i = 0; i <= len - L; ++i) {
          int h1 = pre1[i + L] -
              ((pre1[i] * pow1[L]) % _mod1);
          if (h1 < 0) h1 += _mod1;
          int h2 = pre2[i + L] -
              ((pre2[i] * pow2[L]) % _mod2);
          if (h2 < 0) h2 += _mod2;
          int combined = (h1 << 32) ^ h2;
          curSet.add(combined);
        }

        if (firstPath) {
          common = curSet;
          firstPath = false;
        } else {
          Set<int> newCommon = {};
          for (int v in common) {
            if (curSet.contains(v)) newCommon.add(v);
          }
          common = newCommon;
          if (common.isEmpty) return false;
        }
      }

      return common.isNotEmpty;
    }

    int low = 0, high = minLen;
    while (low < high) {
      int mid = (low + high + 1) >> 1;
      if (check(mid)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
package main

import (
	// no imports needed beyond builtins
)

const (
	mod1 uint64 = 1000000007
	mod2 uint64 = 1000000009
	base uint64 = 91138233
)

func longestCommonSubpath(n int, paths [][]int) int {
	m := len(paths)
	if m == 0 {
		return 0
	}
	minLen := int(^uint(0) >> 1) // max int
	maxLen := 0

	type PathData struct {
		arr   []int
		pref1 []uint64
		pref2 []uint64
	}
	data := make([]PathData, m)

	for i, p := range paths {
		l := len(p)
		if l < minLen {
			minLen = l
		}
		if l > maxLen {
			maxLen = l
		}
		pref1 := make([]uint64, l+1)
		pref2 := make([]uint64, l+1)
		for j, v := range p {
			val := uint64(v + 1) // shift to avoid zero
			pref1[j+1] = (pref1[j]*base + val) % mod1
			pref2[j+1] = (pref2[j]*base + val) % mod2
		}
		data[i] = PathData{arr: p, pref1: pref1, pref2: pref2}
	}

	// precompute powers
	pow1 := make([]uint64, maxLen+1)
	pow2 := make([]uint64, maxLen+1)
	pow1[0], pow2[0] = 1, 1
	for i := 1; i <= maxLen; i++ {
		pow1[i] = (pow1[i-1] * base) % mod1
		pow2[i] = (pow2[i-1] * base) % mod2
	}

	check := func(L int) bool {
		if L == 0 {
			return true
		}
		counts := make(map[uint64]int)
		for _, pd := range data {
			if len(pd.arr) < L {
				return false
			}
			local := make(map[uint64]struct{})
			for i := 0; i+L <= len(pd.arr); i++ {
				h1 := (pd.pref1[i+L] + mod1 - (pd.pref1[i]*pow1[L])%mod1) % mod1
				h2 := (pd.pref2[i+L] + mod2 - (pd.pref2[i]*pow2[L])%mod2) % mod2
				key := (h1 << 32) | h2
				local[key] = struct{}{}
			}
			for k := range local {
				counts[k]++
			}
		}
		for _, c := range counts {
			if c == m {
				return true
			}
		}
		return false
	}

	low, high := 0, minLen
	for low < high {
		mid := (low + high + 1) / 2
		if check(mid) {
			low = mid
		} else {
			high = mid - 1
		}
	}
	return low
}
```

## Ruby

```ruby
def longest_common_subpath(n, paths)
  m = paths.size
  min_len = paths.map(&:length).min
  return 0 if min_len == 0

  base = 100_007
  mod1 = 1_000_000_007
  mod2 = 1_000_000_009

  max_len = paths.map(&:length).max
  pow1 = Array.new(max_len + 1, 0)
  pow2 = Array.new(max_len + 1, 0)
  pow1[0] = 1
  pow2[0] = 1
  (1..max_len).each do |i|
    pow1[i] = (pow1[i - 1] * base) % mod1
    pow2[i] = (pow2[i - 1] * base) % mod2
  end

  low = 0
  high = min_len
  while low < high
    mid = (low + high + 1) / 2
    if common_subpath?(mid, paths, pow1, pow2, base, mod1, mod2)
      low = mid
    else
      high = mid - 1
    end
  end
  low
end

def common_subpath?(len, paths, pow1, pow2, base, mod1, mod2)
  return true if len == 0
  counts = Hash.new(0)
  m = paths.size

  paths.each do |path|
    n = path.length
    h1 = Array.new(n + 1, 0)
    h2 = Array.new(n + 1, 0)

    path.each_with_index do |v, i|
      h1[i + 1] = (h1[i] * base + v) % mod1
      h2[i + 1] = (h2[i] * base + v) % mod2
    end

    seen = {}
    (0..n - len).each do |i|
      j = i + len
      cur1 = (h1[j] - (h1[i] * pow1[len]) % mod1)
      cur1 += mod1 if cur1 < 0
      cur2 = (h2[j] - (h2[i] * pow2[len]) % mod2)
      cur2 += mod2 if cur2 < 0
      key = [cur1, cur2]
      next if seen[key]

      seen[key] = true
      cnt = counts[key] + 1
      return true if cnt == m

      counts[key] = cnt
    end
  end
  false
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.HashSet

  def longestCommonSubpath(n: Int, paths: Array[Array[Int]]): Int = {
    if (paths.isEmpty) return 0
    val m = paths.length
    val minLen = paths.map(_.length).min
    val maxLen = paths.map(_.length).max

    // random odd base > n to reduce collisions
    val rand = new scala.util.Random()
    var base: Long = (rand.nextInt(1 << 30) | 1).toLong
    if (base <= n) base += n + 1
    // precompute powers
    val pow = new Array[Long](maxLen + 1)
    pow(0) = 1L
    var i = 1
    while (i <= maxLen) {
      pow(i) = pow(i - 1) * base
      i += 1
    }

    // prefix hashes for each path
    val prefArr = new Array[Array[Long]](m)
    var idx = 0
    while (idx < m) {
      val arr = paths(idx)
      val pref = new Array[Long](arr.length + 1)
      var h: Long = 0L
      var j = 0
      while (j < arr.length) {
        h = h * base + (arr(j).toLong + 1L) // shift by 1 to avoid zero
        pref(j + 1) = h
        j += 1
      }
      prefArr(idx) = pref
      idx += 1
    }

    def check(k: Int): Boolean = {
      if (k == 0) return true
      var common = new HashSet[Long]()
      // first path hashes
      val pref0 = prefArr(0)
      val len0 = paths(0).length
      var start = 0
      while (start <= len0 - k) {
        val h = pref0(start + k) - pref0(start) * pow(k)
        common.add(h)
        start += 1
      }
      // intersect with other paths
      var pIdx = 1
      while (pIdx < m && common.nonEmpty) {
        val curSet = new HashSet[Long]()
        val pref = prefArr(pIdx)
        val plen = paths(pIdx).length
        var s = 0
        while (s <= plen - k) {
          val h = pref(s + k) - pref(s) * pow(k)
          if (common.contains(h)) curSet.add(h)
          s += 1
        }
        common = curSet
        pIdx += 1
      }
      common.nonEmpty
    }

    var lo = 0
    var hi = minLen + 1 // exclusive upper bound
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (check(mid)) lo = mid + 1 else hi = mid
    }
    lo - 1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_common_subpath(n: i32, paths: Vec<Vec<i32>>) -> i32 {
        use std::collections::{HashMap, HashSet};

        let m = paths.len();
        if m == 0 {
            return 0;
        }
        // minimum length among all paths
        let min_len = paths.iter().map(|p| p.len()).min().unwrap_or(0);
        if min_len == 0 {
            return 0;
        }

        // maximum possible substring length needed for powers
        let max_path_len = paths.iter().map(|p| p.len()).max().unwrap();

        // rolling hash base (random odd)
        const BASE: u64 = 1_000_003;

        // precompute powers of base modulo 2^64 (overflow)
        let mut pow: Vec<u64> = vec![0; max_path_len + 1];
        pow[0] = 1;
        for i in 1..=max_path_len {
            pow[i] = pow[i - 1].wrapping_mul(BASE);
        }

        // helper to compute all substring hashes of length `len` for a path
        fn substr_hashes(path: &Vec<i32>, len: usize, pow: &Vec<u64>) -> Vec<u64> {
            let n = path.len();
            if len == 0 || n < len {
                return vec![];
            }
            let mut pref: Vec<u64> = vec![0; n + 1];
            for i in 0..n {
                // add 1 to avoid zero values affecting hash
                pref[i + 1] = pref[i]
                    .wrapping_mul(BASE)
                    .wrapping_add((path[i] as u64).wrapping_add(1));
            }
            let mut res: Vec<u64> = Vec::with_capacity(n - len + 1);
            for i in 0..=n - len {
                let hash = pref[i + len]
                    .wrapping_sub(pref[i].wrapping_mul(pow[len]));
                res.push(hash);
            }
            res
        }

        // check if there exists a common subpath of length `len`
        fn ok(
            len: usize,
            paths: &Vec<Vec<i32>>,
            pow: &Vec<u64>,
            m: usize,
        ) -> bool {
            if len == 0 {
                return true;
            }
            let mut cnt: HashMap<u64, i32> = HashMap::new();
            for path in paths.iter() {
                if path.len() < len {
                    return false;
                }
                let hashes = substr_hashes(path, len, pow);
                let mut seen: HashSet<u64> = HashSet::new();
                for h in hashes {
                    seen.insert(h);
                }
                for h in seen {
                    *cnt.entry(h).or_insert(0) += 1;
                }
            }
            cnt.values().any(|&v| v as usize == m)
        }

        // binary search on answer
        let mut lo: usize = 0;
        let mut hi: usize = min_len;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid, &paths, &pow, m) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
```

## Racket

```racket
(define base1 1000003)
(define base2 1000033)
(define mod1 1000000007)
(define mod2 1000000009)

(define (precompute-powers maxlen)
  (let ((p1 (make-vector (+ maxlen 1) 0))
        (p2 (make-vector (+ maxlen 1) 0)))
    (vector-set! p1 0 1)
    (vector-set! p2 0 1)
    (for ([i (in-range 1 (+ maxlen 1))])
      (vector-set! p1 i (modulo (* (vector-ref p1 (- i 1)) base1) mod1))
      (vector-set! p2 i (modulo (* (vector-ref p2 (- i 1)) base2) mod2)))
    (values p1 p2)))

(define/contract (longest-common-subpath n paths)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((vec-paths (map list->vector paths))
         (minlen   (apply min (map vector-length vec-paths)))
         (maxlen   (apply max (map vector-length vec-paths))))
    (if (= minlen 0)
        0
        (let-values (((pow1 pow2) (precompute-powers maxlen)))
          (define (check L)
            (if (= L 0)
                #t
                (let ((candidates (make-hash)))
                  ;; first path
                  (let* ((v (first vec-paths))
                         (len (vector-length v)))
                    (when (>= len L)
                      (let ((pref1 (make-vector (+ len 1) 0))
                            (pref2 (make-vector (+ len 1) 0)))
                        (for ([i (in-range len)])
                          (define val (vector-ref v i))
                          (vector-set! pref1 (add1 i)
                                       (modulo (+ (* (vector-ref pref1 i) base1) val) mod1))
                          (vector-set! pref2 (add1 i)
                                       (modulo (+ (* (vector-ref pref2 i) base2) val) mod2)))
                        (for ([i (in-range 0 (- len L) + 1)])
                          (define h1 (modulo
                                      (- (vector-ref pref1 (+ i L))
                                         (modulo (* (vector-ref pref1 i)
                                                    (vector-ref pow1 L)) mod1))
                                      mod1))
                          (define h2 (modulo
                                      (- (vector-ref pref2 (+ i L))
                                         (modulo (* (vector-ref pref2 i)
                                                    (vector-ref pow2 L)) mod2))
                                      mod2))
                          (hash-set! candidates (cons h1 h2) #t)))))
                  ;; remaining paths
                  (for ([v (in-list (rest vec-paths))])
                    (let ((newc (make-hash)))
                      (define len (vector-length v))
                      (when (>= len L)
                        (define pref1 (make-vector (+ len 1) 0))
                        (define pref2 (make-vector (+ len 1) 0))
                        (for ([i (in-range len)])
                          (define val (vector-ref v i))
                          (vector-set! pref1 (add1 i)
                                       (modulo (+ (* (vector-ref pref1 i) base1) val) mod1))
                          (vector-set! pref2 (add1 i)
                                       (modulo (+ (* (vector-ref pref2 i) base2) val) mod2)))
                        (for ([i (in-range 0 (- len L) + 1)])
                          (define h1 (modulo
                                      (- (vector-ref pref1 (+ i L))
                                         (modulo (* (vector-ref pref1 i)
                                                    (vector-ref pow1 L)) mod1))
                                      mod1))
                          (define h2 (modulo
                                      (- (vector-ref pref2 (+ i L))
                                         (modulo (* (vector-ref pref2 i)
                                                    (vector-ref pow2 L)) mod2))
                                      mod2))
                          (let ((key (cons h1 h2)))
                            (when (hash-has-key? candidates key)
                              (hash-set! newc key #t)))))
                        )
                      (set! candidates newc)))
                  (> (hash-count candidates) 0))))
          ;; binary search for maximum length
          (let loop ((lo 0) (hi minlen))
            (if (= lo hi)
                lo
                (let* ((mid (quotient (+ lo hi) 2))
                       (mid+1 (add1 mid)))
                  (if (check mid+1)
                      (loop mid+1 hi)
                      (loop lo mid)))))))))
```

## Erlang

```erlang
-module(solution).
-export([longest_common_subpath/2]).

-define(MOD1, 1000000007).
-define(MOD2, 1000000009).
-define(BASE, 100007).

-spec longest_common_subpath(N :: integer(), Paths :: [[integer()]]) -> integer().
longest_common_subpath(_N, Paths) ->
    MinLen = min_path_len(Paths),
    Pow1 = make_pow(?BASE, ?MOD1, MinLen),
    Pow2 = make_pow(?BASE, ?MOD2, MinLen),
    binary_search(0, MinLen, Paths, Pow1, Pow2).

%% binary search for maximum length
binary_search(Low, High, _Paths, _Pow1, _Pow2) when Low >= High ->
    Low;
binary_search(Low, High, Paths, Pow1, Pow2) ->
    Mid = (Low + High + 1) div 2,
    case has_common(Mid, Paths, Pow1, Pow2) of
        true -> binary_search(Mid, High, Paths, Pow1, Pow2);
        false -> binary_search(Low, Mid - 1, Paths, Pow1, Pow2)
    end.

%% check if there exists a common subpath of length L
has_common(0, _Paths, _Pow1, _Pow2) ->
    true;
has_common(L, Paths, Pow1, Pow2) when L > 0 ->
    M = length(Paths),
    CountMap0 = #{},
    CountMap = lists:foldl(
        fun(Path, AccMap) ->
            Hashes = subpath_hashes(Path, L, Pow1, Pow2),
            Unique = sets:from_list(Hashes),
            sets:fold(
                fun(H, MapIn) ->
                    case maps:is_key(H, MapIn) of
                        true -> maps:update_with(H, fun(V) -> V + 1 end, MapIn);
                        false -> maps:put(H, 1, MapIn)
                    end
                end,
                AccMap,
                Unique)
        end,
        CountMap0,
        Paths),
    %% any hash appearing in all M paths?
    lists:any(fun({_H, C}) -> C == M end, maps:to_list(CountMap)).

%% compute all subpath hashes of length L for a single path
subpath_hashes(PathList, L, Pow1, Pow2) ->
    Len = length(PathList),
    case Len < L of
        true -> [];
        false ->
            PathT = list_to_tuple(PathList),
            Pref1 = build_prefix(PathT, Len, ?BASE, ?MOD1),
            Pref2 = build_prefix(PathT, Len, ?BASE, ?MOD2),
            compute_hashes(0, Len - L, L, Pref1, Pref2, Pow1, Pow2, [])
    end.

compute_hashes(I, MaxI, L, Pref1, Pref2, Pow1, Pow2, Acc) when I =< MaxI ->
    H1 = sub_hash(Pref1, I, L, Pow1, ?MOD1),
    H2 = sub_hash(Pref2, I, L, Pow2, ?MOD2),
    compute_hashes(I + 1, MaxI, L, Pref1, Pref2, Pow1, Pow2, [{H1, H2} | Acc]);
compute_hashes(_, _, _, _, _, _, _, Acc) ->
    lists:reverse(Acc).

sub_hash(Pref, StartIdx, L, Pow, Mod) ->
    % pref tuple is 1‑based with pref[1] = 0 for empty prefix
    A = element(StartIdx + 1, Pref),          % pref at position start
    B = element(StartIdx + L + 1, Pref),      % pref at position start+L
    PowL = element(L, Pow),
    Raw = (B - (A * PowL) rem Mod) rem Mod,
    if Raw < 0 -> Raw + Mod; true -> Raw end.

%% build prefix hash tuple: size Len+1, index 1 holds 0
build_prefix(PathT, Len, Base, Mod) ->
    PrefList = build_prefix(1, Len, PathT, Base, Mod, [0]),
    list_to_tuple(lists:reverse(PrefList)).

build_prefix(I, Len, _PathT, _Base, _Mod, Acc) when I > Len ->
    Acc;
build_prefix(I, Len, PathT, Base, Mod, Acc) ->
    Prev = hd(Acc),
    Elem = element(I, PathT),
    Cur = ((Prev * Base) + Elem) rem Mod,
    build_prefix(I + 1, Len, PathT, Base, Mod, [Cur | Acc]).

%% pre‑compute powers base^i mod Mod up to Max
make_pow(Base, Mod, Max) ->
    PowList = make_pow(0, Max, Base, Mod, [1]),
    list_to_tuple(lists:reverse(PowList)).

make_pow(I, Max, _Base, _Mod, Acc) when I > Max ->
    Acc;
make_pow(I, Max, Base, Mod, Acc) ->
    Prev = hd(Acc),
    Cur = (Prev * Base) rem Mod,
    make_pow(I + 1, Max, Base, Mod, [Cur | Acc]).

%% minimum length among all paths
min_path_len(Paths) ->
    lists:min([length(P) || P <- Paths]).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod1 1_000_000_007
  @mod2 1_000_000_009
  @base 100_007

  @spec longest_common_subpath(n :: integer, paths :: [[integer]]) :: integer
  def longest_common_subpath(_n, paths) do
    lengths = Enum.map(paths, &length/1)
    min_len = Enum.min(lengths)
    max_len = Enum.max(lengths)

    pow1 = build_powers(max_len, @base, @mod1)
    pow2 = build_powers(max_len, @base, @mod2)

    precomputed =
      Enum.map(paths, fn arr ->
        {build_prefix(arr, @base, @mod1), build_prefix(arr, @base, @mod2), length(arr)}
      end)

    bin_search(0, min_len, precomputed, pow1, pow2)
  end

  defp bin_search(low, high, precomputed, pow1, pow2) do
    if low < high do
      mid = div(low + high + 1, 2)

      if common?(mid, precomputed, pow1, pow2) do
        bin_search(mid, high, precomputed, pow1, pow2)
      else
        bin_search(low, mid - 1, precomputed, pow1, pow2)
      end
    else
      low
    end
  end

  defp common?(0, _precomputed, _pow1, _pow2), do: true

  defp common?(k, precomputed, pow1, pow2) do
    pow_k1 = :erlang.element(k + 1, pow1)
    pow_k2 = :erlang.element(k + 1, pow2)

    Enum.reduce_while(precomputed, nil, fn {pref1, pref2, len}, acc ->
      if k > len do
        {:halt, false}
      else
        cur_set = substr_hashes(pref1, pref2, len, k, pow_k1, pow_k2)

        new_acc =
          case acc do
            nil -> cur_set
            _ -> MapSet.intersection(acc, cur_set)
          end

        if MapSet.size(new_acc) == 0 do
          {:halt, false}
        else
          {:cont, new_acc}
        end
      end
    end) != false
  end

  defp substr_hashes(pref1, pref2, len, k, pow_k1, pow_k2) do
    max_i = len - k

    Enum.reduce(0..max_i, MapSet.new(), fn i, set ->
      h1_end = :erlang.element(i + k + 1, pref1)
      h1_start = :erlang.element(i + 1, pref1)

      hash1 = rem(h1_end - h1_start * pow_k1, @mod1)
      hash1 = if hash1 < 0, do: hash1 + @mod1, else: hash1

      h2_end = :erlang.element(i + k + 1, pref2)
      h2_start = :erlang.element(i + 1, pref2)

      hash2 = rem(h2_end - h2_start * pow_k2, @mod2)
      hash2 = if hash2 < 0, do: hash2 + @mod2, else: hash2

      MapSet.put(set, {hash1, hash2})
    end)
  end

  defp build_prefix(arr, base, mod) do
    {list_rev, _} =
      Enum.reduce(arr, {[0], 0}, fn city, {list, prev_hash} ->
        new_hash = rem(prev_hash * base + city, mod)
        {[new_hash | list], new_hash}
      end)

    List.to_tuple(Enum.reverse(list_rev))
  end

  defp build_powers(max_len, base, mod) do
    0..max_len
    |> Enum.reduce([1], fn _, acc ->
      [rem(List.first(acc) * base, mod) | acc]
    end)
    |> Enum.reverse()
    |> List.to_tuple()
  end
end
```
