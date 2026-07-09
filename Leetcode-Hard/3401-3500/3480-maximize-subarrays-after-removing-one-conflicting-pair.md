# 3480. Maximize Subarrays After Removing One Conflicting Pair

## Cpp

```cpp
class Solution {
public:
    long long maxSubarrays(int n, vector<vector<int>>& conflictingPairs) {
        int m = conflictingPairs.size();
        vector<vector<pair<int,int>>> atPos(n + 2);
        for (int i = 0; i < m; ++i) {
            int a = conflictingPairs[i][0];
            int b = conflictingPairs[i][1];
            if (a > b) swap(a, b);
            atPos[a].push_back({b, i});
        }
        const int INF = n + 1;
        map<int,int> cnt;                     // b -> frequency
        unordered_map<int,int> singleId;      // b -> id when freq == 1
        vector<long long> gain(m, 0);
        long long sumF = 0;
        for (int i = n; i >= 1; --i) {
            for (auto &pr : atPos[i]) {
                int b = pr.first;
                int id = pr.second;
                auto it = cnt.find(b);
                if (it == cnt.end()) {
                    cnt[b] = 1;
                    singleId[b] = id;
                } else {
                    ++(it->second);
                    singleId.erase(b); // now count >=2
                }
            }
            if (!cnt.empty()) {
                int min1 = cnt.begin()->first;
                int c1 = cnt.begin()->second;
                if (c1 == 1) {
                    int pid = singleId[min1];
                    auto it2 = std::next(cnt.begin());
                    int min2 = (it2 == cnt.end()) ? INF : it2->first;
                    long long delta = (long long)min2 - min1;
                    if (delta > 0) gain[pid] += delta;
                }
                sumF += (long long)(min1 - 1);
            } else {
                sumF += n; // no restriction
            }
        }
        long long maxGain = 0;
        for (auto g : gain) if (g > maxGain) maxGain = g;
        long long totalSubarrays = sumF + maxGain - (long long)n * (n + 1) / 2 + n;
        return totalSubarrays;
    }
};
```

## Java

```java
class Solution {
    public long maxSubarrays(int n, int[][] conflictingPairs) {
        int m = conflictingPairs.length;
        int[] a = new int[m];
        int[] b = new int[m];
        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] atA = new ArrayList[n + 2];
        for (int i = 0; i < m; i++) {
            int x = conflictingPairs[i][0];
            int y = conflictingPairs[i][1];
            if (x > y) { // ensure a < b
                int tmp = x;
                x = y;
                y = tmp;
            }
            a[i] = x;
            b[i] = y;
            if (atA[x] == null) atA[x] = new ArrayList<>();
            atA[x].add(i);
        }

        long[] gain = new long[m];
        java.util.TreeMap<Integer, Integer> cnt = new java.util.TreeMap<>();
        java.util.HashMap<Integer, Integer> soleId = new java.util.HashMap<>();

        long total0 = 0;
        for (int i = n; i >= 1; i--) {
            if (atA[i] != null) {
                for (int id : atA[i]) {
                    int bi = b[id];
                    int c = cnt.getOrDefault(bi, 0);
                    if (c == 0) {
                        cnt.put(bi, 1);
                        soleId.put(bi, id);
                    } else if (c == 1) {
                        cnt.put(bi, 2);
                        soleId.remove(bi);
                    } else {
                        cnt.put(bi, c + 1);
                    }
                }
            }

            Integer minKey = cnt.isEmpty() ? null : cnt.firstKey();
            int limit = (minKey == null) ? n + 1 : minKey;
            total0 += (long) (limit - i);

            if (minKey != null && cnt.get(minKey) == 1) {
                int pairId = soleId.get(minKey);
                Integer secondKey = cnt.higherKey(minKey);
                int newLimit = (secondKey == null) ? n + 1 : secondKey;
                long delta = (long) (newLimit - minKey);
                if (delta > 0) {
                    gain[pairId] += delta;
                }
            }
        }

        long maxGain = 0;
        for (long g : gain) {
            if (g > maxGain) maxGain = g;
        }
        return total0 + maxGain;
    }
}
```

## Python

```python
class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        m = len(conflictingPairs)
        pairs_by_a = [[] for _ in range(n + 2)]
        for idx, (a, b) in enumerate(conflictingPairs):
            if a > b:
                a, b = b, a
            pairs_by_a[a].append((b, idx))

        INF = n + 2  # greater than any possible b or n+1
        cur_min1 = INF
        cur_min2 = INF
        cnt_min1 = 0
        unique_min_id = -1

        freq = {}
        contrib = [0] * m
        base = 0

        for i in range(n, 0, -1):
            # add pairs whose left endpoint is i
            for b, idx in pairs_by_a[i]:
                prev = freq.get(b, 0)
                freq[b] = prev + 1
                if b < cur_min1:
                    # shift current minimum to second minimum
                    cur_min2 = cur_min1
                    cur_min1 = b
                    cnt_min1 = freq[b]
                    unique_min_id = idx if cnt_min1 == 1 else -1
                elif b == cur_min1:
                    cnt_min1 = freq[b]
                    unique_min_id = -1  # not unique anymore
                elif b < cur_min2:
                    cur_min2 = b

            if cur_min1 == INF:
                g = n + 1
            else:
                g = cur_min1
            base += (g - i)

            if cur_min1 != INF and cnt_min1 == 1:
                new_g = cur_min2 if cur_min2 != INF else n + 1
                delta = new_g - cur_min1
                if delta > 0:
                    contrib[unique_min_id] += delta

        return base + max(contrib)
```

## Python3

```python
from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        m = len(conflictingPairs)
        adj = [[] for _ in range(n + 1)]
        for idx, (a, b) in enumerate(conflictingPairs):
            if a > b:
                a, b = b, a
            adj[a].append((b, idx))

        INF = n + 2  # larger than any possible b
        best1_b = INF
        best1_id = -1
        best2_b = INF
        best2_id = -1

        gain = [0] * m
        total_base = 0

        for i in range(n, 0, -1):
            for b, pid in adj[i]:
                if b < best1_b:
                    best2_b, best2_id = best1_b, best1_id
                    best1_b, best1_id = b, pid
                elif b == best1_b:
                    # same minimal b, removal of one does not affect min
                    continue
                elif b < best2_b:
                    best2_b, best2_id = b, pid

            cur_min = best1_b if best1_b != INF else n + 1
            total_base += cur_min - i

            next_min = best2_b if best2_b != INF else n + 1
            delta = next_min - cur_min if next_min > cur_min else 0
            if best1_id != -1:
                gain[best1_id] += delta

        max_gain = max(gain) if gain else 0
        return total_base + max_gain
```

## C

```c
#include <stddef.h>
#include <stdlib.h>

typedef struct {
    int a;
    int b;
} Pair;

long long maxSubarrays(int n, int** conflictingPairs, int conflictingPairsSize, int* conflictingPairsColSize) {
    int m = conflictingPairsSize;
    Pair *pairs = (Pair*)malloc(sizeof(Pair) * m);
    for (int i = 0; i < m; ++i) {
        int a = conflictingPairs[i][0];
        int b = conflictingPairs[i][1];
        if (a > b) { int t = a; a = b; b = t; }
        pairs[i].a = a;
        pairs[i].b = b;
    }

    /* adjacency list: for each position a, store indices of pairs with that a */
    int *first = (int*)malloc(sizeof(int) * (n + 2));
    int *next = (int*)malloc(sizeof(int) * m);
    for (int i = 0; i <= n + 1; ++i) first[i] = -1;
    for (int i = 0; i < m; ++i) {
        int a = pairs[i].a;
        next[i] = first[a];
        first[a] = i;
    }

    long long *gain = (long long*)calloc(m, sizeof(long long));

    const int INF = n + 2;          // greater than any possible b
    int min1 = INF, idx1 = -1, cntMin = 0, min2 = INF;
    long long base = 0;

    for (int i = n; i >= 1; --i) {
        for (int e = first[i]; e != -1; e = next[e]) {
            int b = pairs[e].b;
            if (b < min1) {
                min2 = min1;
                min1 = b;
                idx1 = e;
                cntMin = 1;
            } else if (b == min1) {
                ++cntMin;
            } else if (b < min2) {
                min2 = b;
            }
        }

        int limit_i = (cntMin > 0 ? min1 : n + 1);
        base += (long long)(limit_i - i);

        if (cntMin == 1) {
            int newLimit = (min2 < INF ? min2 : n + 1);
            long long delta = (long long)newLimit - min1;
            if (delta > 0) gain[idx1] += delta;
        }
    }

    long long maxGain = 0;
    for (int i = 0; i < m; ++i) {
        if (gain[i] > maxGain) maxGain = gain[i];
    }

    free(pairs);
    free(first);
    free(next);
    free(gain);

    return base + maxGain;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxSubarrays(int n, int[][] conflictingPairs) {
        int m = conflictingPairs.Length;
        var starts = new List<(int b, int id)>[n + 2];
        for (int i = 0; i < m; i++) {
            int a = conflictingPairs[i][0];
            int b = conflictingPairs[i][1];
            if (a > b) { int tmp = a; a = b; b = tmp; }
            if (starts[a] == null) starts[a] = new List<(int, int)>();
            starts[a].Add((b, i));
        }

        int INF = n + 1;
        int[] firstB = new int[n + 2];
        int[] firstId = new int[n + 2];
        int[] secondB = new int[n + 2];

        firstB[n + 1] = INF;
        firstId[n + 1] = -1;
        secondB[n + 1] = INF;

        for (int i = n; i >= 1; i--) {
            int fb = firstB[i + 1];
            int fid = firstId[i + 1];
            int sb = secondB[i + 1];

            var list = starts[i];
            if (list != null) {
                foreach (var (b, id) in list) {
                    if (b < fb) {
                        sb = fb;
                        fb = b;
                        fid = id;
                    } else if (b == fb) {
                        sb = fb; // now at least two minima with same value
                    } else if (b < sb) {
                        sb = b;
                    }
                }
            }

            firstB[i] = fb;
            firstId[i] = fid;
            secondB[i] = sb;
        }

        long[] gain = new long[m];
        long total = 0;

        for (int i = 1; i <= n; i++) {
            int fb = firstB[i];
            int limit = (fb == INF) ? n : fb - 1;
            total += (long)(limit - i + 1);

            int fid = firstId[i];
            if (fid != -1) {
                int sb = secondB[i];
                int delta = Math.Min(sb, INF) - fb;
                if (delta > 0) gain[fid] += delta;
            }
        }

        long maxGain = 0;
        foreach (var g in gain) if (g > maxGain) maxGain = g;

        return total + maxGain;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} conflictingPairs
 * @return {number}
 */
var maxSubarrays = function(n, conflictingPairs) {
    const m = conflictingPairs.length;
    const buckets = Array.from({length: n + 2}, () => []);
    for (let i = 0; i < m; ++i) {
        let a = conflictingPairs[i][0];
        let b = conflictingPairs[i][1];
        if (a > b) { const t = a; a = b; b = t; }
        buckets[a].push({b: b, id: i});
    }

    const gain = new Array(m).fill(0);
    const INF = Number.MAX_SAFE_INTEGER;
    let min1B = INF, min2B = INF;
    let cntMin1 = 0;
    let min1Id = -1;

    let base = 0;
    for (let i = n; i >= 1; --i) {
        const list = buckets[i];
        for (let k = 0; k < list.length; ++k) {
            const b = list[k].b;
            const id = list[k].id;
            if (b < min1B) {
                // previous smallest becomes second smallest
                min2B = min1B;
                min1B = b;
                cntMin1 = 1;
                min1Id = id;
            } else if (b === min1B) {
                cntMin1++;
            } else if (b < min2B) {
                min2B = b;
            }
        }

        const curB1 = (min1B === INF ? n + 1 : min1B);
        const curB2 = (min2B === INF ? n + 1 : min2B);

        const fi = (curB1 <= n) ? curB1 - 1 : n;
        base += fi - i + 1;

        if (cntMin1 === 1 && min1Id !== -1) {
            const delta = curB2 - curB1; // non‑negative
            gain[min1Id] += delta;
        }
    }

    let maxGain = 0;
    for (let i = 0; i < m; ++i) {
        if (gain[i] > maxGain) maxGain = gain[i];
    }
    return base + maxGain;
};
```

## Typescript

```typescript
function maxSubarrays(n: number, conflictingPairs: number[][]): number {
    const m = conflictingPairs.length;
    const INF = n + 1;

    // adjacency list per left position
    const adj: [number, number][][] = Array.from({ length: n + 2 }, () => []);
    for (let id = 0; id < m; ++id) {
        let a = conflictingPairs[id][0];
        let b = conflictingPairs[id][1];
        if (a > b) { const t = a; a = b; b = t; }
        adj[a].push([b, id]);
    }

    // per position data
    const first = new Array(n + 2).fill(INF);      // smallest b
    const cntFirst = new Array(n + 2).fill(0);    // how many pairs achieve that smallest b
    const minIdPos = new Array(n + 2).fill(-1);   // id if unique, else -1
    const second = new Array(n + 2).fill(INF);    // second distinct smallest b

    for (let i = 1; i <= n; ++i) {
        const list = adj[i];
        if (list.length === 0) continue;
        let minB = INF, cntMin = 0, uniqId = -1;
        for (const [b, id] of list) {
            if (b < minB) {
                minB = b;
                cntMin = 1;
                uniqId = id;
            } else if (b === minB) {
                ++cntMin;
                uniqId = -1;
            }
        }
        first[i] = minB;
        cntFirst[i] = cntMin;
        minIdPos[i] = uniqId;

        let secB = INF;
        for (const [b] of list) {
            if (b > minB && b < secB) secB = b;
        }
        second[i] = secB;
    }

    const gainArr = new Array(m).fill(0);
    let baseSum = 0;

    let best1 = INF, cntBest1 = 0, best2 = INF;
    let uniqueId = -1; // id of the unique pair providing best1 when cntBest1==1

    for (let i = n; i >= 1; --i) {
        // incorporate first[i]
        const val = first[i];
        if (val < best1) {
            // shift old best1 to second
            if (best1 < best2) best2 = best1;
            else best2 = Math.min(best2, best1);
            best1 = val;
            cntBest1 = cntFirst[i];
            uniqueId = (cntFirst[i] === 1 && minIdPos[i] !== -1) ? minIdPos[i] : -1;
        } else if (val === best1) {
            cntBest1 += cntFirst[i];
            uniqueId = -1;
        } else if (val < best2) {
            best2 = val;
        }

        // incorporate second[i] (single occurrence, not tied to a pair)
        const v2 = second[i];
        if (v2 < best1) {
            if (best1 < best2) best2 = best1;
            else best2 = Math.min(best2, best1);
            best1 = v2;
            cntBest1 = 1;
            uniqueId = -1;
        } else if (v2 === best1) {
            cntBest1 += 1;
            uniqueId = -1;
        } else if (v2 < best2) {
            best2 = v2;
        }

        const curMin = best1; // may be INF
        const oldLimit = curMin === INF ? n : curMin - 1;
        baseSum += Math.max(0, oldLimit - i + 1);

        if (cntBest1 === 1 && uniqueId !== -1) {
            const newMin = best2 < INF ? best2 : INF;
            const add = newMin - curMin;
            if (add > 0) gainArr[uniqueId] += add;
        }
    }

    let maxGain = 0;
    for (const g of gainArr) if (g > maxGain) maxGain = g;

    return baseSum + maxGain;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $conflictingPairs
     * @return Integer
     */
    function maxSubarrays($n, $conflictingPairs) {
        $m = count($conflictingPairs);
        // adjacency list for each left endpoint a
        $pairsAtA = array_fill(0, $n + 2, []);
        foreach ($conflictingPairs as $idx => $p) {
            $a = $p[0];
            $b = $p[1];
            if ($a > $b) {
                $tmp = $a; $a = $b; $b = $tmp;
            }
            $pairsAtA[$a][] = [$b, $idx];
        }

        $INF = $n + 1;
        // arrays indexed from 1..n
        $firstB   = array_fill(0, $n + 2, $INF);
        $secondB  = array_fill(0, $n + 2, $INF);
        $firstId  = array_fill(0, $n + 2, -1);

        // variables for suffix processing
        $minB   = $INF;
        $cntMin = 0;
        $secondVal = $INF;
        $minId  = -1;

        for ($i = $n; $i >= 1; --$i) {
            foreach ($pairsAtA[$i] as $pair) {
                [$b, $id] = $pair;
                if ($b < $minB) {
                    // previous min becomes second best
                    $secondVal = $minB;
                    $minB = $b;
                    $cntMin = 1;
                    $minId = $id;
                } elseif ($b == $minB) {
                    $cntMin++;
                    $minId = -1; // not unique anymore
                } elseif ($b < $secondVal) {
                    $secondVal = $b;
                }
            }

            $firstB[$i] = $minB;
            if ($cntMin == 1) {
                $firstId[$i] = $minId;
                $secondB[$i] = $secondVal;
            } else { // cntMin==0 or >=2
                $firstId[$i] = -1;
                // if there are at least two minima, removing one leaves the same min value
                $secondB[$i] = ($cntMin >= 2) ? $minB : $INF;
            }
        }

        $gain = array_fill(0, $m, 0);
        $base = 0;
        for ($i = 1; $i <= $n; ++$i) {
            $base += $firstB[$i] - $i;
            $owner = $firstId[$i];
            if ($owner != -1) {
                $delta = $secondB[$i] - $firstB[$i];
                if ($delta > 0) {
                    $gain[$owner] += $delta;
                }
            }
        }

        $maxGain = max($gain);
        return $base + $maxGain;
    }
}
```

## Swift

```swift
class Solution {
    func maxSubarrays(_ n: Int, _ conflictingPairs: [[Int]]) -> Int {
        let m = conflictingPairs.count
        if m == 0 { return n * (n + 1) / 2 }
        
        var leftPairs = Array(repeating: [(b: Int, id: Int)](), count: n + 2)
        for (idx, pair) in conflictingPairs.enumerated() {
            var a = pair[0]
            var b = pair[1]
            if a > b { swap(&a, &b) }
            leftPairs[a].append((b, idx))
        }
        
        // Fenwick Tree
        final class Fenwick {
            let size: Int
            var tree: [Int]
            init(_ n: Int) {
                size = n
                tree = Array(repeating: 0, count: n + 2)
            }
            func add(_ index: Int, _ delta: Int) {
                var i = index
                while i <= size {
                    tree[i] += delta
                    i += i & -i
                }
            }
            func sum(_ index: Int) -> Int {
                var res = 0
                var i = index
                while i > 0 {
                    res += tree[i]
                    i -= i & -i
                }
                return res
            }
            func total() -> Int { sum(size) }
            // smallest idx such that prefix sum >= k (k >= 1)
            func kth(_ k: Int) -> Int {
                var idx = 0
                var bit = 1
                while bit <= size { bit <<= 1 }
                var need = k
                var step = bit
                while step > 0 {
                    let next = idx + step
                    if next <= size && tree[next] < need {
                        need -= tree[next]
                        idx = next
                    }
                    step >>= 1
                }
                return idx + 1
            }
        }
        
        var fenwick = Fenwick(n)
        var cntPerB = Array(repeating: 0, count: n + 2)
        var bucket = Array(repeating: [Int](), count: n + 2)
        var gain = Array(repeating: 0, count: m)
        var baseSum: Int64 = 0
        
        for i in stride(from: n, through: 1, by: -1) {
            // add conflicts whose left endpoint is i
            for (b, id) in leftPairs[i] {
                fenwick.add(b, 1)
                cntPerB[b] += 1
                bucket[b].append(id)
            }
            
            let total = fenwick.total()
            if total == 0 {
                // no constraints, can extend to n
                let f_i = n
                let cnt = f_i - i + 1
                baseSum += Int64(cnt)
                continue
            }
            
            let minB = fenwick.kth(1)
            let countMin = cntPerB[minB]
            var secondBound = n + 1
            if total > countMin {
                // there exists another distinct b after consuming all at minB
                let k = countMin + 1
                secondBound = fenwick.kth(k)
            }
            
            let f_i = minB - 1
            let cnt = f_i - i + 1
            baseSum += Int64(cnt)
            
            if countMin == 1 {
                let delta = max(0, secondBound - minB)
                if delta > 0 {
                    // unique minimal conflict id
                    let uniqId = bucket[minB][0]
                    gain[uniqId] += delta
                }
            }
        }
        
        var maxGain = 0
        for g in gain { if g > maxGain { maxGain = g } }
        let answer = baseSum + Int64(maxGain)
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
import java.util.TreeMap
import kotlin.math.max

class Solution {
    fun maxSubarrays(n: Int, conflictingPairs: Array<IntArray>): Long {
        val m = conflictingPairs.size
        // store pairs by left endpoint
        val byA = Array(n + 2) { mutableListOf<PairInfo>() }
        // map (a,b) -> id
        val pairIdMap = HashMap<Long, Int>(m * 2)
        for (idx in 0 until m) {
            var a = conflictingPairs[idx][0]
            var b = conflictingPairs[idx][1]
            if (a > b) {
                val tmp = a; a = b; b = tmp
            }
            byA[a].add(PairInfo(idx, b))
            val key = a.toLong() * (n + 1L) + b
            pairIdMap[key] = idx
        }

        val cntMap = TreeMap<Int, Int>()
        val uniqueLeft = HashMap<Int, Int>() // b -> left when count == 1
        val gain = LongArray(m)

        var base: Long = 0
        for (i in n downTo 1) {
            // add pairs starting at i
            for (p in byA[i]) {
                val b = p.b
                val newCnt = (cntMap[b] ?: 0) + 1
                cntMap[b] = newCnt
                if (newCnt == 1) {
                    uniqueLeft[b] = i
                } else {
                    uniqueLeft.remove(b)
                }
            }

            var minB = n + 1
            var cntMin = 0
            var secondMin = n + 1

            val firstEntry = cntMap.firstEntry()
            if (firstEntry != null) {
                minB = firstEntry.key
                cntMin = firstEntry.value
                val higher = cntMap.higherKey(minB)
                if (higher != null) secondMin = higher else secondMin = n + 1
            }

            base += (minB - i).toLong()

            if (cntMin == 1) {
                val leftIdx = uniqueLeft[minB]!!
                val key = leftIdx.toLong() * (n + 1L) + minB
                val pid = pairIdMap[key]!!
                gain[pid] += (secondMin - minB).toLong()
            }
        }

        var maxGain: Long = 0
        for (g in gain) {
            if (g > maxGain) maxGain = g
        }
        return base + maxGain
    }

    private data class PairInfo(val id: Int, val b: Int)
}
```

## Dart

```dart
class Solution {
  int maxSubarrays(int n, List<List<int>> conflictingPairs) {
    final int INF = n + 1;
    final List<int> firstMin = List.filled(n + 2, INF);
    final List<int> secondMin = List.filled(n + 2, INF);

    for (var pair in conflictingPairs) {
      int a = pair[0];
      int b = pair[1];
      if (a > b) {
        int tmp = a;
        a = b;
        b = tmp;
      }
      if (b < firstMin[a]) {
        secondMin[a] = firstMin[a];
        firstMin[a] = b;
      } else if (b < secondMin[a]) {
        secondMin[a] = b;
      }
    }

    final List<int> val = List.filled(n + 2, INF);
    for (int i = 1; i <= n; ++i) {
      val[i] = firstMin[i];
    }

    // base sum of suffix minima
    int cur = INF;
    int baseSum = 0;
    for (int i = n; i >= 1; --i) {
      if (val[i] < cur) cur = val[i];
      baseSum += cur;
    }

    // next minimum to the right for each position
    final List<int> nextMin = List.filled(n + 2, INF);
    cur = INF;
    for (int i = n; i >= 1; --i) {
      nextMin[i] = cur;
      if (val[i] < cur) cur = val[i];
    }

    // previous smaller element to the left
    final List<int> leftSmaller = List.filled(n + 2, 0);
    final List<int> stack = [];
    for (int i = 1; i <= n; ++i) {
      while (stack.isNotEmpty && val[stack.last] >= val[i]) {
        stack.removeLast();
      }
      leftSmaller[i] = stack.isEmpty ? 0 : stack.last;
      stack.add(i);
    }

    int maxGain = 0;

    for (int i = n; i >= 1; --i) {
      if (nextMin[i] > val[i]) { // critical position
        int left = leftSmaller[i] + 1;
        int right = i;
        int curNew = secondMin[i];
        if (nextMin[i] < curNew) curNew = nextMin[i];

        int gain = curNew - val[i]; // for i == right
        for (int j = right - 1; j >= left; --j) {
          if (val[j] < curNew) curNew = val[j];
          gain += curNew - val[i];
        }
        if (gain > maxGain) maxGain = gain;
      }
    }

    int totalSubarrays = baseSum - n * (n + 1) ~/ 2 + maxGain;
    return totalSubarrays;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type item struct {
	b  int
	id int
}

type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { if h[i].b == h[j].b { return h[i].id < h[j].id }; return h[i].b < h[j].b }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func maxSubarrays(n int, conflictingPairs [][]int) int64 {
	m := len(conflictingPairs)
	left := make([][]item, n+2)

	for idx, p := range conflictingPairs {
		a, b := p[0], p[1]
		if a > b {
			a, b = b, a
		}
		left[a] = append(left[a], item{b: b, id: idx})
	}

	inc := make([]int64, m)
	var total int64

	h := &minHeap{}
	heap.Init(h)

	for i := n; i >= 1; i-- {
		for _, it := range left[i] {
			heap.Push(h, it)
		}
		if h.Len() == 0 {
			total += int64(n - i + 1)
			continue
		}
		top := (*h)[0]
		firstB, firstID := top.b, top.id

		baseCnt := firstB - i
		total += int64(baseCnt)

		// pop to get second minimum
		heap.Pop(h)
		var secondB int
		if h.Len() > 0 {
			secondB = (*h)[0].b
		} else {
			secondB = n + 1
		}
		heap.Push(h, item{b: firstB, id: firstID})

		if delta := secondB - firstB; delta > 0 {
			inc[firstID] += int64(delta)
		}
	}

	var maxInc int64
	for _, v := range inc {
		if v > maxInc {
			maxInc = v
		}
	}
	return total + maxInc
}
```

## Ruby

```ruby
def max_subarrays(n, conflicting_pairs)
  inf = n + 2
  first_b = Array.new(n + 2, inf)
  second_b = Array.new(n + 2, inf)

  conflicting_pairs.each do |pair|
    a, b = pair[0], pair[1]
    if a > b
      a, b = b, a
    end
    if b < first_b[a]
      second_b[a] = first_b[a]
      first_b[a] = b
    elsif b < second_b[a]
      second_b[a] = b
    end
  end

  count_map = Hash.new(0)
  cur_min = inf
  cnt = 0
  second_min_global = inf
  provider = -1
  gain = Array.new(n + 2, 0)
  base = 0

  i = n
  while i >= 1
    b = first_b[i]
    if b != inf
      c = count_map[b] + 1
      count_map[b] = c
      if b < cur_min
        second_min_global = cur_min
        cur_min = b
        cnt = 1
        provider = i
      elsif b == cur_min
        cnt = c
        provider = -1
      else
        second_min_global = b if b < second_min_global
      end
    end

    min_b = cur_min
    f = (min_b == inf) ? n : (min_b - 1)
    base += f - i + 1

    if cnt == 1 && provider != -1
      next_candidate = second_min_global
      sb = second_b[provider]
      next_candidate = sb if sb < next_candidate
      nxt = (next_candidate == inf) ? (n + 1) : next_candidate
      gain[provider] += nxt - cur_min
    end

    i -= 1
  end

  max_gain = gain.max || 0
  base + max_gain
end
```

## Scala

```scala
object Solution {
  import java.util.{PriorityQueue, Comparator}
  case class Pair(b: Int, id: Int)

  def maxSubarrays(n: Int, conflictingPairs: Array[Array[Int]]): Long = {
    val m = conflictingPairs.length
    // adjacency list for pairs by left endpoint a (1-indexed)
    val atA = Array.fill(n + 2)(new java.util.ArrayList[Pair]())
    for (idx <- 0 until m) {
      var a = conflictingPairs(idx)(0)
      var b = conflictingPairs(idx)(1)
      if (a > b) { val tmp = a; a = b; b = tmp }
      atA(a).add(Pair(b, idx))
    }

    // min-heap based on b
    val cmp = new Comparator[Pair] {
      override def compare(p1: Pair, p2: Pair): Int = Integer.compare(p1.b, p2.b)
    }
    val pq = new PriorityQueue[Pair](cmp)

    val contrib = Array.fill[Long](m)(0L)
    var baseTotal: Long = 0L
    val INF = n + 1

    for (i <- n to 1 by -1) {
      // add pairs whose left endpoint is i
      val list = atA(i)
      val it = list.iterator()
      while (it.hasNext) {
        pq.add(it.next())
      }

      var minFirst = INF
      var firstId = -1
      if (!pq.isEmpty) {
        val first = pq.peek()
        minFirst = Math.min(first.b, INF)
        firstId = first.id
      }
      baseTotal += (minFirst - i).toLong

      // compute second smallest b
      var secondB = Int.MaxValue
      if (pq.size() >= 2) {
        val firstTmp = pq.poll()
        val sec = if (!pq.isEmpty) pq.peek().b else Int.MaxValue
        secondB = sec
        pq.add(firstTmp)
      }
      val minSecond = Math.min(secondB, INF)
      val delta = minSecond - minFirst
      if (delta > 0 && firstId != -1) {
        contrib(firstId) += delta.toLong
      }
    }

    var maxGain: Long = 0L
    for (v <- contrib) {
      if (v > maxGain) maxGain = v
    }
    baseTotal + maxGain
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_subarrays(n: i32, conflicting_pairs: Vec<Vec<i32>>) -> i64 {
        let n_usize = n as usize;
        let m = conflicting_pairs.len();
        // add_at[a] stores (b, id) for pairs with left endpoint a
        let mut add_at: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n_usize + 2];
        for (idx, pair) in conflicting_pairs.iter().enumerate() {
            let mut a = pair[0] as usize;
            let mut b = pair[1] as usize;
            if a > b {
                let tmp = a;
                a = b;
                b = tmp;
            }
            add_at[a].push((b, idx));
        }

        let inf = n_usize + 2; // greater than any possible b and n+1
        let mut best1 = inf;   // smallest b in current suffix
        let mut best2 = inf;   // second smallest distinct b
        let mut cnt_best1: i32 = 0;
        let mut best_id: isize = -1; // id of unique minimal pair, -1 if not unique

        let mut base_total: i64 = 0;
        let mut gain: Vec<i64> = vec![0; m];

        for i in (1..=n_usize).rev() {
            // add pairs whose left endpoint equals i
            for &(b, id) in &add_at[i] {
                if b < best1 {
                    best2 = best1;
                    best1 = b;
                    cnt_best1 = 1;
                    best_id = id as isize;
                } else if b == best1 {
                    cnt_best1 += 1;
                    best_id = -1; // not unique anymore
                } else if b < best2 {
                    best2 = b;
                }
            }

            let limit = if best1 <= n_usize { best1 - 1 } else { n_usize };
            base_total += (limit as i64) - (i as i64) + 1;

            if cnt_best1 == 1 && best_id >= 0 {
                let next_min = if best2 <= n_usize + 1 { best2 } else { n_usize + 1 };
                let delta = (next_min as i64) - (best1 as i64);
                gain[best_id as usize] += delta;
            }
        }

        let max_gain = gain.into_iter().max().unwrap_or(0);
        base_total + max_gain
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-subarrays n conflictingPairs)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length conflictingPairs)]
         [arr (make-vector (+ n 1) '())] ; index 0 unused
         [extra (make-vector m 0)])
    ;; store each pair (b, id) at position a (with a < b)
    (for ([pair conflictingPairs] [idx (in-naturals)])
      (define a (first pair))
      (define b (second pair))
      (when (> a b) (let ((tmp a)) (set! a b) (set! b tmp)))
      (vector-set! arr a (cons (list b idx) (vector-ref arr a))))
    ;; initialize minima
    (define INF (+ n 2))
    (define min1Val INF)
    (define min1Id -1)
    (define cntMin 0)
    (define min2Val INF)
    (define totalBase 0)
    ;; iterate left endpoint i from n down to 1
    (for ([i (in-range n 0 -1)])
      (for ([pr (in-list (vector-ref arr i))])
        (define b (first pr))
        (define pid (second pr))
        (cond
          [(< b min1Val)
           (set! min2Val min1Val)
           (set! min1Val b)
           (set! min1Id pid)
           (set! cntMin 1)]
          [(= b min1Val)
           (set! cntMin (+ cntMin 1))]
          [(< b min2Val)
           (set! min2Val b)]))
      (define limit (if (<= min1Val (+ n 1)) min1Val (+ n 1)))
      (set! totalBase (+ totalBase (- limit i)))
      (when (= cntMin 1)
        (define newLimit (if (<= min2Val (+ n 1)) min2Val (+ n 1)))
        (define inc (- newLimit limit))
        (when (> inc 0)
          (vector-set! extra min1Id (+ (vector-ref extra min1Id) inc)))))
    ;; maximum additional subarrays by deleting one pair
    (let ([maxExtra (apply max (vector->list extra))])
      (+ totalBase maxExtra))))
```

## Erlang

```erlang
-spec max_subarrays(N :: integer(), ConflictingPairs :: [[integer()]]) -> integer().
max_subarrays(N, ConflictingPairs) ->
    INF = N + 2,
    % Initialize arrays for smallest and second smallest b per a
    Min1Arr0 = array:new(N + 1, INF),
    Min2Arr0 = array:new(N + 1, INF),

    % Process all pairs to fill Min1Arr and Min2Arr
    {Min1Arr, Min2Arr} =
        lists:foldl(
          fun([A0, B0], {M1, M2}) ->
                  {A, B} = if A0 > B0 -> {B0, A0}; true -> {A0, B0} end,
                  CurMin1 = array:get(A, M1),
                  CurMin2 = array:get(A, M2),
                  case B < CurMin1 of
                      true ->
                          NewM2 = array:set(A, CurMin1, M2),
                          NewM1 = array:set(A, B, M1),
                          {NewM1, NewM2};
                      false when B == CurMin1 ->
                          % duplicate minimal value, ignore (does not affect result)
                          {M1, M2};
                      false ->
                          case B < CurMin2 of
                              true ->
                                  NewM2 = array:set(A, B, M2),
                                  {M1, NewM2};
                              false ->
                                  {M1, M2}
                          end
                  end
          end,
          {Min1Arr0, Min2Arr0},
          ConflictingPairs),

    % Suffix scan from N down to 1
    LoopFun = fun
        (0, _Best1Val, _Best1Pos, _Best2Val, BaseAcc, GainMap) ->
            {BaseAcc, GainMap};
        (I, Best1Val, Best1Pos, Best2Val, BaseAcc, GainMap) ->
            Min1 = array:get(I, Min1Arr),
            Min2 = array:get(I, Min2Arr),

            % Build candidate list (value, source position)
            Cand0 = [{Best1Val, Best1Pos},
                     {Best2Val, -1},
                     {Min1, I},
                     {Min2, I}],
            Cand = [C || C = {V,_} <- Cand0, V =/= INF],

            % Find smallest and second smallest values
            {NewBest1Val, NewBest1Pos, NewBest2Val} =
                lists:foldl(
                  fun({V,P}, {B1,V1,B2}) ->
                          if V < B1 ->
                                 {V, P, B1};
                             V < B2 ->
                                 {B1, V1, V};
                             true ->
                                 {B1, V1, B2}
                          end
                  end,
                  {INF, -1, INF},
                  Cand),

            % Compute limit for current left endpoint I
            Limit = case NewBest1Val of
                        INF -> N;
                        _   -> min(NewBest1Val - 1, N)
                    end,
            NewBaseAcc = BaseAcc + (Limit - I + 1),

            % Gain contributed by removing the pair that gives NewBest1Val
            B1 = case NewBest1Val of INF -> N + 1; _ -> NewBest1Val end,
            B2 = case NewBest2Val of INF -> N + 1; _ -> NewBest2Val end,
            Delta = if B2 > B1 -> B2 - B1; true -> 0 end,

            NewGainMap =
                if Delta > 0, NewBest1Pos =/= -1 ->
                        PairKey = {NewBest1Pos, B1},
                        Prev = maps:get(PairKey, GainMap, 0),
                        maps:put(PairKey, Prev + Delta, GainMap);
                   true -> GainMap
                end,

            LoopFun(I - 1, NewBest1Val, NewBest1Pos, NewBest2Val, NewBaseAcc, NewGainMap)
    end,

    {BaseCount, Gains} = LoopFun(N, INF, -1, INF, 0, #{}),

    MaxGain =
        case maps:values(Gains) of
            [] -> 0;
            Vs -> lists:max(Vs)
        end,
    BaseCount + MaxGain.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_subarrays(n :: integer, conflicting_pairs :: [[integer]]) :: integer
  def max_subarrays(n, conflicting_pairs) do
    m = length(conflicting_pairs)

    # Build adjacency map: for each smaller element a, store list of {b, pair_id}
    adj =
      Enum.with_index(conflicting_pairs, fn [a, b], idx ->
        if a < b, do: {a, b, idx}, else: {b, a, idx}
      end)
      |> Enum.reduce(%{}, fn {a, b, idx}, acc ->
        Map.update(acc, a, [{b, idx}], fn list -> [{b, idx} | list] end)
      end)

    inf = n + 1

    # Reduce over positions from n down to 1
    {base, gains, _cf, _cntf, _idf, _cs, _cnts} =
      Enum.reduce(n..1, {0, %{}, inf, 0, -1, inf, 0}, fn i,
                                                       {base_acc, gains_acc,
                                                        cur_first, cnt_first,
                                                        id_first, cur_second,
                                                        cnt_second} ->
        list = Map.get(adj, i, [])

        # Process all pairs whose smaller element is i
        {new_first, new_cnt_f, new_id_f, new_second, new_cnt_s} =
          Enum.reduce(list, {cur_first, cnt_first, id_first, cur_second, cnt_second},
            fn {b, pid},
               {cf, ctf, idf, cs, cts} ->
              cond do
                b < cf ->
                  # shift current first to second
                  {b, 1, pid, cf, ctf}

                b == cf ->
                  new_cnt = ctf + 1
                  new_id = if new_cnt > 1, do: -1, else: idf
                  {cf, new_cnt, new_id, cs, cts}

                b < cs ->
                  {cf, ctf, idf, b, 1}

                b == cs ->
                  {cf, ctf, idf, cs, cts + 1}

                true ->
                  {cf, ctf, idf, cs, cts}
              end
            end)

        limit = new_first
        new_base = base_acc + (limit - i)

        new_gains =
          if new_cnt_f == 1 and new_id_f != -1 do
            inc = new_second - new_first
            Map.update(gains_acc, new_id_f, inc, &(&1 + inc))
          else
            gains_acc
          end

        {new_base, new_gains, new_first, new_cnt_f, new_id_f,
         new_second, new_cnt_s}
      end)

    max_gain =
      case Map.values(gains) do
        [] -> 0
        vals -> Enum.max(vals)
      end

    base + max_gain
  end
end
```
