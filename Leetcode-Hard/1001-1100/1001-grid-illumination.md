# 1001. Grid Illumination

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> gridIllumination(int n, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
        unordered_map<int,int> rowCnt, colCnt;
        unordered_map<long long,int> diagCnt, antiDiagCnt;
        unordered_set<long long> active;
        auto encode = [&](int r, int c)->long long{
            return (static_cast<long long>(r) << 32) | static_cast<unsigned int>(c);
        };
        
        for (auto &lamp : lamps) {
            int r = lamp[0], c = lamp[1];
            long long key = encode(r,c);
            if (active.count(key)) continue;
            active.insert(key);
            ++rowCnt[r];
            ++colCnt[c];
            ++diagCnt[static_cast<long long>(r) - c];
            ++antiDiagCnt[static_cast<long long>(r) + c];
        }
        
        vector<int> ans;
        const int dirs[3] = {-1,0,1};
        for (auto &q : queries) {
            int r = q[0], c = q[1];
            bool lit = rowCnt[r] > 0 || colCnt[c] > 0 ||
                       diagCnt[static_cast<long long>(r) - c] > 0 ||
                       antiDiagCnt[static_cast<long long>(r) + c] > 0;
            ans.push_back(lit ? 1 : 0);
            
            for (int dr : dirs) {
                for (int dc : dirs) {
                    int nr = r + dr, nc = c + dc;
                    if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                    long long key = encode(nr,nc);
                    auto it = active.find(key);
                    if (it != active.end()) {
                        active.erase(it);
                        if (--rowCnt[nr] == 0) rowCnt.erase(nr);
                        if (--colCnt[nc] == 0) colCnt.erase(nc);
                        long long d1 = static_cast<long long>(nr) - nc;
                        long long d2 = static_cast<long long>(nr) + nc;
                        if (--diagCnt[d1] == 0) diagCnt.erase(d1);
                        if (--antiDiagCnt[d2] == 0) antiDiagCnt.erase(d2);
                    }
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] gridIllumination(int n, int[][] lamps, int[][] queries) {
        java.util.HashMap<Integer, Integer> row = new java.util.HashMap<>();
        java.util.HashMap<Integer, Integer> col = new java.util.HashMap<>();
        java.util.HashMap<Integer, Integer> diag = new java.util.HashMap<>();      // r - c
        java.util.HashMap<Integer, Integer> antiDiag = new java.util.HashMap<>(); // r + c
        java.util.HashSet<Long> active = new java.util.HashSet<>();

        for (int[] lamp : lamps) {
            int r = lamp[0], c = lamp[1];
            long key = ((long) r << 32) | (c & 0xffffffffL);
            if (active.add(key)) { // only count once per unique lamp
                row.put(r, row.getOrDefault(r, 0) + 1);
                col.put(c, col.getOrDefault(c, 0) + 1);
                diag.put(r - c, diag.getOrDefault(r - c, 0) + 1);
                antiDiag.put(r + c, antiDiag.getOrDefault(r + c, 0) + 1);
            }
        }

        int m = queries.length;
        int[] ans = new int[m];
        int idx = 0;
        for (int[] q : queries) {
            int r = q[0], c = q[1];
            if (row.getOrDefault(r, 0) > 0 ||
                col.getOrDefault(c, 0) > 0 ||
                diag.getOrDefault(r - c, 0) > 0 ||
                antiDiag.getOrDefault(r + c, 0) > 0) {
                ans[idx++] = 1;
            } else {
                ans[idx++] = 0;
            }

            // turn off lamps in the 3x3 area centered at (r,c)
            for (int dr = -1; dr <= 1; ++dr) {
                int nr = r + dr;
                if (nr < 0 || nr >= n) continue;
                for (int dc = -1; dc <= 1; ++dc) {
                    int nc = c + dc;
                    if (nc < 0 || nc >= n) continue;
                    long key = ((long) nr << 32) | (nc & 0xffffffffL);
                    if (active.remove(key)) {
                        // decrement counts
                        row.put(nr, row.get(nr) - 1);
                        if (row.get(nr) == 0) row.remove(nr);
                        col.put(nc, col.get(nc) - 1);
                        if (col.get(nc) == 0) col.remove(nc);
                        int d = nr - nc;
                        diag.put(d, diag.get(d) - 1);
                        if (diag.get(d) == 0) diag.remove(d);
                        int ad = nr + nc;
                        antiDiag.put(ad, antiDiag.get(ad) - 1);
                        if (antiDiag.get(ad) == 0) antiDiag.remove(ad);
                    }
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lamp_set = set()
        row_cnt = {}
        col_cnt = {}
        diag_cnt = {}
        anti_cnt = {}

        for r, c in lamps:
            if (r, c) in lamp_set:
                continue
            lamp_set.add((r, c))
            row_cnt[r] = row_cnt.get(r, 0) + 1
            col_cnt[c] = col_cnt.get(c, 0) + 1
            d = r - c
            diag_cnt[d] = diag_cnt.get(d, 0) + 1
            a = r + c
            anti_cnt[a] = anti_cnt.get(a, 0) + 1

        ans = []
        for r, c in queries:
            if (row_cnt.get(r, 0) > 0 or
                col_cnt.get(c, 0) > 0 or
                diag_cnt.get(r - c, 0) > 0 or
                anti_cnt.get(r + c, 0) > 0):
                ans.append(1)
            else:
                ans.append(0)

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in lamp_set:
                        lamp_set.remove((nr, nc))
                        row_cnt[nr] -= 1
                        if row_cnt[nr] == 0:
                            del row_cnt[nr]
                        col_cnt[nc] -= 1
                        if col_cnt[nc] == 0:
                            del col_cnt[nc]
                        d = nr - nc
                        diag_cnt[d] -= 1
                        if diag_cnt[d] == 0:
                            del diag_cnt[d]
                        a = nr + nc
                        anti_cnt[a] -= 1
                        if anti_cnt[a] == 0:
                            del anti_cnt[a]

        return ans
```

## Python3

```python
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict

        # Counters for rows, columns, diagonals, anti-diagonals
        row_cnt = defaultdict(int)
        col_cnt = defaultdict(int)
        diag_cnt = defaultdict(int)      # r - c
        adiag_cnt = defaultdict(int)     # r + c

        # Set of active lamps
        active = set()

        for r, c in lamps:
            if (r, c) in active:
                continue
            active.add((r, c))
            row_cnt[r] += 1
            col_cnt[c] += 1
            diag_cnt[r - c] += 1
            adiag_cnt[r + c] += 1

        ans = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),  (0, 0),  (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for r, c in queries:
            # Check illumination
            if row_cnt[r] > 0 or col_cnt[c] > 0 or diag_cnt[r - c] > 0 or adiag_cnt[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)

            # Turn off lamp at (r,c) and adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in active:
                    active.remove((nr, nc))
                    row_cnt[nr] -= 1
                    col_cnt[nc] -= 1
                    diag_cnt[nr - nc] -= 1
                    adiag_cnt[nr + nc] -= 1

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef struct {
    long long *keys;
    int *vals;
    char *used;
    int cap;
} HashMap;

/* simple 64-bit mix hash */
static inline uint64_t mix_hash(uint64_t x) {
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    x *= 0xc4ceb9fe1a85ec53ULL;
    x ^= x >> 33;
    return x;
}

static HashMap* hm_create(int cap) {
    HashMap *hm = (HashMap*)malloc(sizeof(HashMap));
    hm->cap = cap;
    hm->keys = (long long*)calloc(cap, sizeof(long long));
    hm->vals = (int*)calloc(cap, sizeof(int));
    hm->used = (char*)calloc(cap, sizeof(char));
    return hm;
}

/* find slot for key, returns index where key is or should be inserted */
static int hm_find_slot(HashMap *hm, long long key) {
    uint64_t h = mix_hash((uint64_t)key);
    int idx = (int)(h & (uint64_t)(hm->cap - 1));
    while (hm->used[idx]) {
        if (hm->keys[idx] == key) break;
        idx = (idx + 1) & (hm->cap - 1);
    }
    return idx;
}

/* increment value for key, inserting with value 1 if absent */
static void hm_inc(HashMap *hm, long long key) {
    int idx = hm_find_slot(hm, key);
    if (hm->used[idx]) {
        hm->vals[idx] += 1;
    } else {
        hm->used[idx] = 1;
        hm->keys[idx] = key;
        hm->vals[idx] = 1;
    }
}

/* decrement value for key; remove entry when it reaches zero */
static void hm_dec(HashMap *hm, long long key) {
    int idx = hm_find_slot(hm, key);
    if (!hm->used[idx]) return;          // not present
    hm->vals[idx] -= 1;
    if (hm->vals[idx] > 0) return;

    /* delete and rehash subsequent cluster */
    hm->used[idx] = 0;
    int nxt = (idx + 1) & (hm->cap - 1);
    while (hm->used[nxt]) {
        long long k = hm->keys[nxt];
        int v = hm->vals[nxt];
        hm->used[nxt] = 0;
        int j = hm_find_slot(hm, k);
        hm->used[j] = 1;
        hm->keys[j] = k;
        hm->vals[j] = v;
        nxt = (nxt + 1) & (hm->cap - 1);
    }
}

/* get value for key; returns 0 if absent */
static int hm_get(HashMap *hm, long long key) {
    int idx = hm_find_slot(hm, key);
    return hm->used[idx] ? hm->vals[idx] : 0;
}

/* check presence (value >0) */
static int hm_contains(HashMap *hm, long long key) {
    int idx = hm_find_slot(hm, key);
    return hm->used[idx];
}

/* add key with dummy value 1 if not present */
static void hm_add(HashMap *hm, long long key) {
    int idx = hm_find_slot(hm, key);
    if (!hm->used[idx]) {
        hm->used[idx] = 1;
        hm->keys[idx] = key;
        hm->vals[idx] = 1;
    }
}

/* remove key (if present) */
static void hm_remove(HashMap *hm, long long key) {
    int idx = hm_find_slot(hm, key);
    if (!hm->used[idx]) return;
    hm->used[idx] = 0;
    int nxt = (idx + 1) & (hm->cap - 1);
    while (hm->used[nxt]) {
        long long k = hm->keys[nxt];
        int v = hm->vals[nxt];
        hm->used[nxt] = 0;
        int j = hm_find_slot(hm, k);
        hm->used[j] = 1;
        hm->keys[j] = k;
        hm->vals[j] = v;
        nxt = (nxt + 1) & (hm->cap - 1);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* gridIllumination(int n, int** lamps, int lampsSize, int* lampsColSize,
                      int** queries, int queriesSize, int* queriesColSize,
                      int* returnSize) {
    /* capacity as power of two larger than expected entries */
    const int CAP = 1 << 18;   // 262144
    HashMap *lampSet = hm_create(CAP);
    HashMap *rowCnt  = hm_create(CAP);
    HashMap *colCnt  = hm_create(CAP);
    HashMap *diagCnt = hm_create(CAP);   // key = row - col
    HashMap *antiCnt = hm_create(CAP);   // key = row + col

    for (int i = 0; i < lampsSize; ++i) {
        int r = lamps[i][0];
        int c = lamps[i][1];
        long long posKey = ((long long)r << 32) | (unsigned int)c;
        if (!hm_contains(lampSet, posKey)) {
            hm_add(lampSet, posKey);
            hm_inc(rowCnt, r);
            hm_inc(colCnt, c);
            hm_inc(diagCnt, (long long)r - (long long)c);
            hm_inc(antiCnt, (long long)r + (long long)c);
        }
    }

    int *ans = (int*)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;

    const int dirs[3] = {-1, 0, 1};

    for (int i = 0; i < queriesSize; ++i) {
        int r = queries[i][0];
        int c = queries[i][1];

        int illuminated = hm_get(rowCnt, r) > 0 ||
                          hm_get(colCnt, c) > 0 ||
                          hm_get(diagCnt, (long long)r - (long long)c) > 0 ||
                          hm_get(antiCnt, (long long)r + (long long)c) > 0;
        ans[i] = illuminated ? 1 : 0;

        /* turn off lamp at (r,c) and its adjacent cells */
        for (int dr = 0; dr < 3; ++dr) {
            for (int dc = 0; dc < 3; ++dc) {
                long long nr = (long long)r + dirs[dr];
                long long nc = (long long)c + dirs[dc];
                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                long long posKey = (nr << 32) | (unsigned int)nc;
                if (hm_contains(lampSet, posKey)) {
                    hm_remove(lampSet, posKey);
                    hm_dec(rowCnt, nr);
                    hm_dec(colCnt, nc);
                    hm_dec(diagCnt, nr - nc);
                    hm_dec(antiCnt, nr + nc);
                }
            }
        }
    }

    /* free hash maps (optional for LeetCode) */
    free(lampSet->keys); free(lampSet->vals); free(lampSet->used); free(lampSet);
    free(rowCnt->keys);  free(rowCnt->vals);  free(rowCnt->used);  free(rowCnt);
    free(colCnt->keys);  free(colCnt->vals);  free(colCnt->used);  free(colCnt);
    free(diagCnt->keys); free(diagCnt->vals); free(diagCnt->used); free(diagCnt);
    free(antiCnt->keys); free(antiCnt->vals); free(antiCnt->used); free(antiCnt);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] GridIllumination(int n, int[][] lamps, int[][] queries) {
        var lampSet = new HashSet<long>();
        var rowCount = new Dictionary<int, int>();
        var colCount = new Dictionary<int, int>();
        var diagCount = new Dictionary<long, int>();      // r - c
        var antiDiagCount = new Dictionary<long, int>();  // r + c

        void AddOne<TKey>(Dictionary<TKey, int> dict, TKey key) {
            if (dict.TryGetValue(key, out int v)) dict[key] = v + 1;
            else dict[key] = 1;
        }

        foreach (var lamp in lamps) {
            int r = lamp[0];
            int c = lamp[1];
            long key = ((long)r << 32) | (uint)c;
            if (!lampSet.Add(key)) continue; // duplicate lamp, ignore
            AddOne(rowCount, r);
            AddOne(colCount, c);
            AddOne(diagCount, (long)r - c);
            AddOne(antiDiagCount, (long)r + c);
        }

        void Dec<TKey>(Dictionary<TKey, int> dict, TKey key) {
            if (!dict.TryGetValue(key, out int v)) return;
            if (v == 1) dict.Remove(key);
            else dict[key] = v - 1;
        }

        var answer = new List<int>(queries.Length);

        foreach (var q in queries) {
            int r = q[0];
            int c = q[1];

            bool illuminated = rowCount.ContainsKey(r) ||
                               colCount.ContainsKey(c) ||
                               diagCount.ContainsKey((long)r - c) ||
                               antiDiagCount.ContainsKey((long)r + c);
            answer.Add(illuminated ? 1 : 0);

            for (int dr = -1; dr <= 1; dr++) {
                int nr = r + dr;
                if (nr < 0 || nr >= n) continue;
                for (int dc = -1; dc <= 1; dc++) {
                    int nc = c + dc;
                    if (nc < 0 || nc >= n) continue;
                    long key = ((long)nr << 32) | (uint)nc;
                    if (!lampSet.Remove(key)) continue;

                    Dec(rowCount, nr);
                    Dec(colCount, nc);
                    Dec(diagCount, (long)nr - nc);
                    Dec(antiDiagCount, (long)nr + nc);
                }
            }
        }

        return answer.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} lamps
 * @param {number[][]} queries
 * @return {number[]}
 */
var gridIllumination = function(n, lamps, queries) {
    const rowMap = new Map();
    const colMap = new Map();
    const diagMap = new Map();      // r - c
    const antiDiagMap = new Map();  // r + c
    const lampSet = new Set();

    const inc = (map, key) => map.set(key, (map.get(key) || 0) + 1);
    const dec = (map, key) => {
        const cnt = map.get(key);
        if (cnt === 1) map.delete(key);
        else map.set(key, cnt - 1);
    };

    for (const [r, c] of lamps) {
        const posKey = r + ',' + c;
        if (lampSet.has(posKey)) continue;
        lampSet.add(posKey);
        inc(rowMap, r);
        inc(colMap, c);
        inc(diagMap, r - c);
        inc(antiDiagMap, r + c);
    }

    const ans = [];
    for (const [r, c] of queries) {
        if (rowMap.has(r) || colMap.has(c) || diagMap.has(r - c) || antiDiagMap.has(r + c)) {
            ans.push(1);
        } else {
            ans.push(0);
        }

        for (let dr = -1; dr <= 1; dr++) {
            const nr = r + dr;
            if (nr < 0 || nr >= n) continue;
            for (let dc = -1; dc <= 1; dc++) {
                const nc = c + dc;
                if (nc < 0 || nc >= n) continue;
                const key = nr + ',' + nc;
                if (!lampSet.has(key)) continue;
                lampSet.delete(key);
                dec(rowMap, nr);
                dec(colMap, nc);
                dec(diagMap, nr - nc);
                dec(antiDiagMap, nr + nc);
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function gridIllumination(n: number, lamps: number[][], queries: number[][]): number[] {
    const lampSet = new Set<string>();
    const rowMap = new Map<number, number>();
    const colMap = new Map<number, number>();
    const diagMap = new Map<number, number>(); // r - c
    const antiDiagMap = new Map<number, number>(); // r + c

    const addCount = (map: Map<number, number>, key: number) => {
        map.set(key, (map.get(key) ?? 0) + 1);
    };
    const subCount = (map: Map<number, number>, key: number) => {
        const cnt = map.get(key);
        if (cnt === undefined) return;
        if (cnt === 1) map.delete(key);
        else map.set(key, cnt - 1);
    };

    for (const [r, c] of lamps) {
        const posKey = `${r},${c}`;
        if (lampSet.has(posKey)) continue;
        lampSet.add(posKey);
        addCount(rowMap, r);
        addCount(colMap, c);
        addCount(diagMap, r - c);
        addCount(antiDiagMap, r + c);
    }

    const ans: number[] = [];
    for (const [r, c] of queries) {
        if (
            rowMap.has(r) ||
            colMap.has(c) ||
            diagMap.has(r - c) ||
            antiDiagMap.has(r + c)
        ) {
            ans.push(1);
        } else {
            ans.push(0);
        }

        for (let dr = -1; dr <= 1; dr++) {
            const nr = r + dr;
            if (nr < 0 || nr >= n) continue;
            for (let dc = -1; dc <= 1; dc++) {
                const nc = c + dc;
                if (nc < 0 || nc >= n) continue;
                const key = `${nr},${nc}`;
                if (!lampSet.has(key)) continue;
                lampSet.delete(key);
                subCount(rowMap, nr);
                subCount(colMap, nc);
                subCount(diagMap, nr - nc);
                subCount(antiDiagMap, nr + nc);
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $lamps
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function gridIllumination($n, $lamps, $queries) {
        $lampSet = [];
        $row = [];
        $col = [];
        $diag = [];
        $anti = [];

        foreach ($lamps as $pos) {
            $r = $pos[0];
            $c = $pos[1];
            $key = $r . ':' . $c;
            if (isset($lampSet[$key])) {
                continue;
            }
            $lampSet[$key] = true;

            $row[$r] = ($row[$r] ?? 0) + 1;
            $col[$c] = ($col[$c] ?? 0) + 1;
            $diag[$r - $c] = ($diag[$r - $c] ?? 0) + 1;
            $anti[$r + $c] = ($anti[$r + $c] ?? 0) + 1;
        }

        $ans = [];

        foreach ($queries as $q) {
            $r = $q[0];
            $c = $q[1];

            if (isset($row[$r]) || isset($col[$c]) || isset($diag[$r - $c]) || isset($anti[$r + $c])) {
                $ans[] = 1;
            } else {
                $ans[] = 0;
            }

            for ($dr = -1; $dr <= 1; $dr++) {
                $nr = $r + $dr;
                if ($nr < 0 || $nr >= $n) {
                    continue;
                }
                for ($dc = -1; $dc <= 1; $dc++) {
                    $nc = $c + $dc;
                    if ($nc < 0 || $nc >= $n) {
                        continue;
                    }
                    $key = $nr . ':' . $nc;
                    if (!isset($lampSet[$key])) {
                        continue;
                    }

                    unset($lampSet[$key]);

                    $row[$nr]--;
                    if ($row[$nr] == 0) {
                        unset($row[$nr]);
                    }
                    $col[$nc]--;
                    if ($col[$nc] == 0) {
                        unset($col[$nc]);
                    }
                    $diagKey = $nr - $nc;
                    $diag[$diagKey]--;
                    if ($diag[$diagKey] == 0) {
                        unset($diag[$diagKey]);
                    }
                    $antiKey = $nr + $nc;
                    $anti[$antiKey]--;
                    if ($anti[$antiKey] == 0) {
                        unset($anti[$antiKey]);
                    }
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func gridIllumination(_ n: Int, _ lamps: [[Int]], _ queries: [[Int]]) -> [Int] {
        var lampSet = Set<Int64>()
        var rowCount = [Int:Int]()
        var colCount = [Int:Int]()
        var diagCount = [Int:Int]()      // r - c
        var antiDiagCount = [Int:Int]()  // r + c
        
        for lamp in lamps {
            let r = lamp[0]
            let c = lamp[1]
            let key = (Int64(r) << 32) | Int64(c)
            if lampSet.contains(key) { continue }
            lampSet.insert(key)
            rowCount[r, default: 0] += 1
            colCount[c, default: 0] += 1
            diagCount[r - c, default: 0] += 1
            antiDiagCount[r + c, default: 0] += 1
        }
        
        var result = [Int]()
        let dirs = [-1, 0, 1]
        
        for query in queries {
            let r = query[0]
            let c = query[1]
            
            if (rowCount[r] ?? 0) > 0 ||
               (colCount[c] ?? 0) > 0 ||
               (diagCount[r - c] ?? 0) > 0 ||
               (antiDiagCount[r + c] ?? 0) > 0 {
                result.append(1)
            } else {
                result.append(0)
            }
            
            for dr in dirs {
                let nr = r + dr
                if nr < 0 || nr >= n { continue }
                for dc in dirs {
                    let nc = c + dc
                    if nc < 0 || nc >= n { continue }
                    let key = (Int64(nr) << 32) | Int64(nc)
                    if lampSet.contains(key) {
                        lampSet.remove(key)
                        
                        if let cnt = rowCount[nr] {
                            if cnt == 1 { rowCount.removeValue(forKey: nr) } else { rowCount[nr] = cnt - 1 }
                        }
                        if let cnt = colCount[nc] {
                            if cnt == 1 { colCount.removeValue(forKey: nc) } else { colCount[nc] = cnt - 1 }
                        }
                        let d = nr - nc
                        if let cnt = diagCount[d] {
                            if cnt == 1 { diagCount.removeValue(forKey: d) } else { diagCount[d] = cnt - 1 }
                        }
                        let ad = nr + nc
                        if let cnt = antiDiagCount[ad] {
                            if cnt == 1 { antiDiagCount.removeValue(forKey: ad) } else { antiDiagCount[ad] = cnt - 1 }
                        }
                    }
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun gridIllumination(n: Int, lamps: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val lampSet = HashSet<Long>()
        val rowMap = HashMap<Int, Int>()
        val colMap = HashMap<Int, Int>()
        val diagMap = HashMap<Int, Int>()
        val antiDiagMap = HashMap<Int, Int>()

        fun encode(r: Int, c: Int): Long = (r.toLong() shl 32) or (c.toLong() and 0xffffffffL)

        for (lamp in lamps) {
            val r = lamp[0]
            val c = lamp[1]
            val key = encode(r, c)
            if (!lampSet.add(key)) continue
            rowMap[r] = (rowMap[r] ?: 0) + 1
            colMap[c] = (colMap[c] ?: 0) + 1
            diagMap[r - c] = (diagMap[r - c] ?: 0) + 1
            antiDiagMap[r + c] = (antiDiagMap[r + c] ?: 0) + 1
        }

        val ans = IntArray(queries.size)
        var idx = 0
        for (q in queries) {
            val r = q[0]
            val c = q[1]

            if ((rowMap[r] ?: 0) > 0 ||
                (colMap[c] ?: 0) > 0 ||
                (diagMap[r - c] ?: 0) > 0 ||
                (antiDiagMap[r + c] ?: 0) > 0) {
                ans[idx] = 1
            }

            for (dr in -1..1) {
                val nr = r + dr
                if (nr < 0 || nr >= n) continue
                for (dc in -1..1) {
                    val nc = c + dc
                    if (nc < 0 || nc >= n) continue
                    val key = encode(nr, nc)
                    if (lampSet.remove(key)) {
                        rowMap[nr]?.let { cnt ->
                            if (cnt == 1) rowMap.remove(nr) else rowMap[nr] = cnt - 1
                        }
                        colMap[nc]?.let { cnt ->
                            if (cnt == 1) colMap.remove(nc) else colMap[nc] = cnt - 1
                        }
                        val dKey = nr - nc
                        diagMap[dKey]?.let { cnt ->
                            if (cnt == 1) diagMap.remove(dKey) else diagMap[dKey] = cnt - 1
                        }
                        val aKey = nr + nc
                        antiDiagMap[aKey]?.let { cnt ->
                            if (cnt == 1) antiDiagMap.remove(aKey) else antiDiagMap[aKey] = cnt - 1
                        }
                    }
                }
            }

            idx++
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> gridIllumination(int n, List<List<int>> lamps, List<List<int>> queries) {
    final Map<int, int> rows = {};
    final Map<int, int> cols = {};
    final Map<int, int> diag = {}; // row - col
    final Map<int, int> anti = {}; // row + col
    final Set<int> active = {};

    for (final lamp in lamps) {
      final int r = lamp[0];
      final int c = lamp[1];
      final int key = r * n + c;
      if (active.contains(key)) continue;
      active.add(key);
      rows[r] = (rows[r] ?? 0) + 1;
      cols[c] = (cols[c] ?? 0) + 1;
      diag[r - c] = (diag[r - c] ?? 0) + 1;
      anti[r + c] = (anti[r + c] ?? 0) + 1;
    }

    final List<int> ans = [];

    for (final query in queries) {
      final int r = query[0];
      final int c = query[1];

      if ((rows[r] != null && rows[r]! > 0) ||
          (cols[c] != null && cols[c]! > 0) ||
          (diag[r - c] != null && diag[r - c]! > 0) ||
          (anti[r + c] != null && anti[r + c]! > 0)) {
        ans.add(1);
      } else {
        ans.add(0);
      }

      for (int dr = -1; dr <= 1; dr++) {
        for (int dc = -1; dc <= 1; dc++) {
          final int nr = r + dr;
          final int nc = c + dc;
          if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
          final int key = nr * n + nc;
          if (!active.contains(key)) continue;
          active.remove(key);

          rows[nr] = rows[nr]! - 1;
          if (rows[nr] == 0) rows.remove(nr);
          cols[nc] = cols[nc]! - 1;
          if (cols[nc] == 0) cols.remove(nc);
          final int dKey = nr - nc;
          diag[dKey] = diag[dKey]! - 1;
          if (diag[dKey] == 0) diag.remove(dKey);
          final int aKey = nr + nc;
          anti[aKey] = anti[aKey]! - 1;
          if (anti[aKey] == 0) anti.remove(aKey);
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func gridIllumination(n int, lamps [][]int, queries [][]int) []int {
	rowCnt := make(map[int]int)
	colCnt := make(map[int]int)
	diagCnt := make(map[int]int)   // r - c
	antiCnt := make(map[int]int)   // r + c
	lampSet := make(map[int64]bool)

	for _, p := range lamps {
		r, c := p[0], p[1]
		key := (int64(r) << 32) | int64(c)
		if lampSet[key] {
			continue
		}
		lampSet[key] = true
		rowCnt[r]++
		colCnt[c]++
		diagCnt[r-c]++
		antiCnt[r+c]++
	}

	dirs := []int{-1, 0, 1}
	ans := make([]int, len(queries))

	for i, q := range queries {
		r, c := q[0], q[1]
		if rowCnt[r] > 0 || colCnt[c] > 0 || diagCnt[r-c] > 0 || antiCnt[r+c] > 0 {
			ans[i] = 1
		} else {
			ans[i] = 0
		}
		for _, dr := range dirs {
			nr := r + dr
			if nr < 0 || nr >= n {
				continue
			}
			for _, dc := range dirs {
				nc := c + dc
				if nc < 0 || nc >= n {
					continue
				}
				key := (int64(nr) << 32) | int64(nc)
				if lampSet[key] {
					delete(lampSet, key)

					rowCnt[nr]--
					if rowCnt[nr] == 0 {
						delete(rowCnt, nr)
					}
					colCnt[nc]--
					if colCnt[nc] == 0 {
						delete(colCnt, nc)
					}
					diagCnt[nr-nc]--
					if diagCnt[nr-nc] == 0 {
						delete(diagCnt, nr-nc)
					}
					antiCnt[nr+nc]--
					if antiCnt[nr+nc] == 0 {
						delete(antiCnt, nr+nc)
					}
				}
			}
		}
	}

	return ans
}
```

## Ruby

```ruby
def grid_illumination(n, lamps, queries)
  rows = Hash.new(0)
  cols = Hash.new(0)
  diag = Hash.new(0)   # r - c
  anti = Hash.new(0)   # r + c
  lamp_set = {}

  lamps.each do |lamp|
    r, c = lamp
    key = (r << 32) + c
    next if lamp_set[key]
    lamp_set[key] = true
    rows[r] += 1
    cols[c] += 1
    diag[r - c] += 1
    anti[r + c] += 1
  end

  result = []

  queries.each do |query|
    r, c = query
    if rows[r] > 0 || cols[c] > 0 || diag[r - c] > 0 || anti[r + c] > 0
      result << 1
    else
      result << 0
    end

    (-1..1).each do |dr|
      nr = r + dr
      next if nr < 0 || nr >= n
      (-1..1).each do |dc|
        nc = c + dc
        next if nc < 0 || nc >= n
        key = (nr << 32) + nc
        if lamp_set[key]
          lamp_set.delete(key)
          rows[nr] -= 1
          cols[nc] -= 1
          diag[nr - nc] -= 1
          anti[nr + nc] -= 1
        end
      end
    end
  end

  result
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def gridIllumination(n: Int, lamps: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val lampSet = mutable.HashSet[Long]()
    val rowCnt = mutable.HashMap[Int, Int]().withDefaultValue(0)
    val colCnt = mutable.HashMap[Int, Int]().withDefaultValue(0)
    val diagCnt = mutable.HashMap[Int, Int]().withDefaultValue(0)      // r - c
    val antiDiagCnt = mutable.HashMap[Int, Int]().withDefaultValue(0) // r + c

    def encode(r: Int, c: Int): Long = (r.toLong << 32) | (c & 0xffffffffL)

    for (lamp <- lamps) {
      val r = lamp(0)
      val c = lamp(1)
      val key = encode(r, c)
      if (!lampSet.contains(key)) {
        lampSet.add(key)
        rowCnt(r) += 1
        colCnt(c) += 1
        diagCnt(r - c) += 1
        antiDiagCnt(r + c) += 1
      }
    }

    val ans = new Array[Int](queries.length)

    def dec(map: mutable.HashMap[Int, Int], k: Int): Unit = {
      map.get(k) match {
        case Some(v) if v > 1 => map.update(k, v - 1)
        case Some(_)          => map -= k
        case None             => ()
      }
    }

    var i = 0
    for (q <- queries) {
      val r = q(0)
      val c = q(1)

      if (rowCnt.getOrElse(r, 0) > 0 ||
          colCnt.getOrElse(c, 0) > 0 ||
          diagCnt.getOrElse(r - c, 0) > 0 ||
          antiDiagCnt.getOrElse(r + c, 0) > 0) {
        ans(i) = 1
      } else {
        ans(i) = 0
      }

      for (dr <- -1 to 1; dc <- -1 to 1) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
          val key = encode(nr, nc)
          if (lampSet.contains(key)) {
            lampSet.remove(key)
            dec(rowCnt, nr)
            dec(colCnt, nc)
            dec(diagCnt, nr - nc)
            dec(antiDiagCnt, nr + nc)
          }
        }
      }

      i += 1
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn grid_illumination(n: i32, lamps: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        use std::collections::{HashMap, HashSet};

        let mut lamp_set: HashSet<i64> = HashSet::new();
        let mut row_cnt: HashMap<i32, i32> = HashMap::new();
        let mut col_cnt: HashMap<i32, i32> = HashMap::new();
        let mut diag_cnt: HashMap<i32, i32> = HashMap::new();   // r + c
        let mut anti_cnt: HashMap<i32, i32> = HashMap::new();   // r - c

        for l in lamps.iter() {
            let r = l[0];
            let c = l[1];
            let key = ((r as i64) << 32) | (c as i64 & 0xffffffff);
            if lamp_set.insert(key) {
                *row_cnt.entry(r).or_insert(0) += 1;
                *col_cnt.entry(c).or_insert(0) += 1;
                *diag_cnt.entry(r + c).or_insert(0) += 1;
                *anti_cnt.entry(r - c).or_insert(0) += 1;
            }
        }

        let mut ans = Vec::with_capacity(queries.len());

        for q in queries.iter() {
            let r = q[0];
            let c = q[1];

            let illuminated = row_cnt.get(&r).copied().unwrap_or(0) > 0
                || col_cnt.get(&c).copied().unwrap_or(0) > 0
                || diag_cnt.get(&(r + c)).copied().unwrap_or(0) > 0
                || anti_cnt.get(&(r - c)).copied().unwrap_or(0) > 0;
            ans.push(if illuminated { 1 } else { 0 });

            for dr in -1i32..=1 {
                for dc in -1i32..=1 {
                    let nr = r + dr;
                    let nc = c + dc;
                    if nr < 0 || nr >= n || nc < 0 || nc >= n {
                        continue;
                    }
                    let key = ((nr as i64) << 32) | (nc as i64 & 0xffffffff);
                    if lamp_set.remove(&key) {
                        if let Some(cnt) = row_cnt.get_mut(&nr) {
                            *cnt -= 1;
                            if *cnt == 0 {
                                row_cnt.remove(&nr);
                            }
                        }
                        if let Some(cnt) = col_cnt.get_mut(&nc) {
                            *cnt -= 1;
                            if *cnt == 0 {
                                col_cnt.remove(&nc);
                            }
                        }
                        let d = nr + nc;
                        if let Some(cnt) = diag_cnt.get_mut(&d) {
                            *cnt -= 1;
                            if *cnt == 0 {
                                diag_cnt.remove(&d);
                            }
                        }
                        let a = nr - nc;
                        if let Some(cnt) = anti_cnt.get_mut(&a) {
                            *cnt -= 1;
                            if *cnt == 0 {
                                anti_cnt.remove(&a);
                            }
                        }
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (grid-illumination n lamps queries)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((lamp-set   (make-hash))
         (row-count  (make-hash))
         (col-count  (make-hash))
         (diag-count (make-hash))   ; r - c
         (anti-count (make-hash)))  ; r + c

    ;; helpers to increment / decrement hash counters
    (define (inc! ht key)
      (hash-update! ht key (lambda (v) (+ v 1)) 0))
    (define (dec! ht key)
      (let ((new-val (- (hash-ref ht key) 1)))
        (if (= new-val 0)
            (hash-remove! ht key)
            (hash-set! ht key new-val))))

    ;; add initial lamps
    (for ([lamp lamps])
      (let* ((r (first lamp))
             (c (second lamp))
             (pos (cons r c)))
        (unless (hash-has-key? lamp-set pos)
          (hash-set! lamp-set pos #t)
          (inc! row-count r)
          (inc! col-count c)
          (inc! diag-count (- r c))
          (inc! anti-count (+ r c)))))

    ;; process queries
    (let loop ((qs queries) (ans '()))
      (if (null? qs)
          (reverse ans)
          (let* ((q (first qs))
                 (r (first q))
                 (c (second q))
                 (illuminated (or (> (hash-ref row-count r 0) 0)
                                  (> (hash-ref col-count c 0) 0)
                                  (> (hash-ref diag-count (- r c) 0) 0)
                                  (> (hash-ref anti-count (+ r c) 0) 0))))
            ;; turn off lamp at (r,c) and its 8 neighbours
            (for ([dx (list -1 0 1)])
              (for ([dy (list -1 0 1)])
                (let ((nr (+ r dx))
                      (nc (+ c dy)))
                  (when (and (>= nr 0) (< nr n)
                             (>= nc 0) (< nc n))
                    (let ((pos (cons nr nc)))
                      (when (hash-has-key? lamp-set pos)
                        (hash-remove! lamp-set pos)
                        (dec! row-count nr)
                        (dec! col-count nc)
                        (dec! diag-count (- nr nc))
                        (dec! anti-count (+ nr nc))))))))
            (loop (rest qs) (cons (if illuminated 1 0) ans)))))))
```

## Erlang

```erlang
-spec grid_illumination(integer(), [[integer()]], [[integer()]]) -> [integer()].
grid_illumination(N, Lamps, Queries) ->
    {LampSet, RowMap, ColMap, DiagMap, AntiDiagMap} = build_maps(Lamps, #{}, #{}, #{}, #{}, #{}),
    Answers = process_queries(Queries, N, LampSet, RowMap, ColMap, DiagMap, AntiDiagMap, []),
    lists:reverse(Answers).

%% Build initial maps from lamp list
build_maps([], Set, Row, Col, Diag, Anti) ->
    {Set, Row, Col, Diag, Anti};
build_maps([[R, C] | Rest], Set, Row, Col, Diag, Anti) ->
    Key = {R, C},
    case maps:is_key(Key, Set) of
        true ->
            build_maps(Rest, Set, Row, Col, Diag, Anti);
        false ->
            Set1   = maps:put(Key, true, Set),
            Row1   = inc(R, Row),
            Col1   = inc(C, Col),
            DKey   = R - C,
            Diag1  = inc(DKey, Diag),
            AKey   = R + C,
            Anti1  = inc(AKey, Anti),
            build_maps(Rest, Set1, Row1, Col1, Diag1, Anti1)
    end.

inc(Key, Map) ->
    Count = maps:get(Key, Map, 0) + 1,
    maps:put(Key, Count, Map).

dec(Key, Map) ->
    case maps:get(Key, Map) of
        1 -> maps:remove(Key, Map);
        C -> maps:put(Key, C - 1, Map)
    end.

process_queries([], _N, _Set, _Row, _Col, _Diag, _Anti, Acc) ->
    Acc;
process_queries([[R, C] | Rest], N, Set, Row, Col, Diag, Anti, Acc) ->
    Illuminated =
        (maps:get(R, Row, 0) > 0) orelse
        (maps:get(C, Col, 0) > 0) orelse
        (maps:get(R - C, Diag, 0) > 0) orelse
        (maps:get(R + C, Anti, 0) > 0),
    Ans = if Illuminated -> 1; true -> 0 end,
    {Set1, Row1, Col1, Diag1, Anti1} =
        turn_off_adjacent(R, C, N, Set, Row, Col, Diag, Anti),
    process_queries(Rest, N, Set1, Row1, Col1, Diag1, Anti1, [Ans | Acc]).

turn_off_adjacent(R, C, N, Set, Row, Col, Diag, Anti) ->
    Offsets = [{-1,-1},{-1,0},{-1,1},
               {0,-1}, {0,0}, {0,1},
               {1,-1},{1,0},{1,1}],
    lists:foldl(
      fun({DR, DC},
          {S, RMap, CMap, DMap, AMap}) ->
          Nr = R + DR,
          Nc = C + DC,
          if
              Nr < 0; Nr >= N; Nc < 0; Nc >= N ->
                  {S, RMap, CMap, DMap, AMap};
              true ->
                  Key = {Nr, Nc},
                  case maps:is_key(Key, S) of
                      false -> {S, RMap, CMap, DMap, AMap};
                      true ->
                          S1   = maps:remove(Key, S),
                          RMap1= dec(Nr, RMap),
                          CMap1= dec(Nc, CMap),
                          DKey = Nr - Nc,
                          DMap1= dec(DKey, DMap),
                          AKey = Nr + Nc,
                          AMap1= dec(AKey, AMap),
                          {S1, RMap1, CMap1, DMap1, AMap1}
                  end
          end
      end,
      {Set, Row, Col, Diag, Anti},
      Offsets).
```

## Elixir

```elixir
defmodule Solution do
  @spec grid_illumination(integer, [[integer]], [[integer]]) :: [integer]
  def grid_illumination(n, lamps, queries) do
    {row_counts, col_counts, diag_counts, anti_counts, lamp_set} =
      Enum.reduce(lamps, {%{}, %{}, %{}, %{}, MapSet.new()}, fn [r, c],
                                                               {rc, cc, dc, ac, set} ->
        key = {r, c}

        if MapSet.member?(set, key) do
          {rc, cc, dc, ac, set}
        else
          rc2 = Map.update(rc, r, 1, &(&1 + 1))
          cc2 = Map.update(cc, c, 1, &(&1 + 1))
          d = r - c
          dc2 = Map.update(dc, d, 1, &(&1 + 1))
          a = r + c
          ac2 = Map.update(ac, a, 1, &(&1 + 1))

          {rc2, cc2, dc2, ac2, MapSet.put(set, key)}
        end
      end)

    {answers_rev, _, _, _, _, _} =
      Enum.reduce(queries, {[], row_counts, col_counts, diag_counts, anti_counts, lamp_set},
        fn [r, c],
           {ans_acc, rc, cc, dc, ac, set} ->
          illuminated =
            Map.has_key?(rc, r) or
              Map.has_key?(cc, c) or
              Map.has_key?(dc, r - c) or
              Map.has_key?(ac, r + c)

          ans_val = if illuminated, do: 1, else: 0

          {rc2, cc2, dc2, ac2, set2} =
            Enum.reduce(-1..1, {rc, cc, dc, ac, set}, fn dr,
                                                       {racc, cacc, dacc, aacc, sacc} ->
              nr = r + dr

              if nr < 0 or nr >= n do
                {racc, cacc, dacc, aacc, sacc}
              else
                Enum.reduce(-1..1, {racc, cacc, dacc, aacc, sacc}, fn dc_off,
                                                                   {rrc, ccc, ddd, aaa, sss} ->
                  nc = c + dc_off

                  if nc < 0 or nc >= n do
                    {rrc, ccc, ddd, aaa, sss}
                  else
                    key = {nr, nc}

                    if MapSet.member?(sss, key) do
                      sss2 = MapSet.delete(sss, key)
                      rrc2 = dec_count(rrc, nr)
                      ccc2 = dec_count(ccc, nc)
                      ddd2 = dec_count(ddd, nr - nc)
                      aaa2 = dec_count(aaa, nr + nc)

                      {rrc2, ccc2, ddd2, aaa2, sss2}
                    else
                      {rrc, ccc, ddd, aaa, sss}
                    end
                  end
                end)
              end
            end)

          {[ans_val | ans_acc], rc2, cc2, dc2, ac2, set2}
        end)

    Enum.reverse(answers_rev)
  end

  defp dec_count(map, key) do
    case Map.get(map, key) do
      nil -> map
      1 -> Map.delete(map, key)
      v when v > 1 -> Map.put(map, key, v - 1)
    end
  end
end
```
