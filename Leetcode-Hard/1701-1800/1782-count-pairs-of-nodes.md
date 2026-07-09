# 1782. Count Pairs Of Nodes

## Cpp

```cpp
class Solution {
public:
    vector<int> countPairs(int n, vector<vector<int>>& edges, vector<int>& queries) {
        vector<int> deg(n + 1, 0);
        unordered_map<long long, int> pairCnt;
        pairCnt.reserve(edges.size() * 2);
        const long long SHIFT = (1LL << 32);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            ++deg[u];
            ++deg[v];
            if (u > v) swap(u, v);
            long long key = ((long long)u << 32) | v;
            ++pairCnt[key];
        }
        vector<int> sortedDeg(n);
        for (int i = 1; i <= n; ++i) sortedDeg[i - 1] = deg[i];
        sort(sortedDeg.begin(), sortedDeg.end());
        
        vector<int> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            long long total = 0;
            // count pairs with degree sum > q
            for (int i = 0; i < n; ++i) {
                int need = q - sortedDeg[i];
                auto it = upper_bound(sortedDeg.begin() + i + 1, sortedDeg.end(), need);
                total += (long long)(sortedDeg.end() - it);
            }
            // subtract overcounted pairs where actual incident count <= q
            for (auto &kv : pairCnt) {
                int u = (int)(kv.first >> 32);
                int v = (int)(kv.first & 0xffffffffLL);
                int cnt = kv.second;
                int sumDeg = deg[u] + deg[v];
                if (sumDeg > q && sumDeg - cnt <= q) {
                    --total;
                }
            }
            ans.push_back((int)total);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] countPairs(int n, int[][] edges, int[] queries) {
        int[] degree = new int[n + 1];
        java.util.HashMap<Long, Integer> pairCount = new java.util.HashMap<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            degree[u]++;
            degree[v]++;
            if (u > v) {
                int tmp = u;
                u = v;
                v = tmp;
            }
            long key = ((long) u << 32) | (v & 0xffffffffL);
            pairCount.put(key, pairCount.getOrDefault(key, 0) + 1);
        }

        int[] sortedDeg = new int[n];
        for (int i = 1; i <= n; i++) {
            sortedDeg[i - 1] = degree[i];
        }
        java.util.Arrays.sort(sortedDeg);

        int m = queries.length;
        int[] answers = new int[m];

        for (int qi = 0; qi < m; qi++) {
            int k = queries[qi];
            long total = 0;
            int i = 0, j = n - 1;
            while (i < j) {
                if (sortedDeg[i] + sortedDeg[j] > k) {
                    total += (j - i);
                    j--;
                } else {
                    i++;
                }
            }

            for (java.util.Map.Entry<Long, Integer> entry : pairCount.entrySet()) {
                long key = entry.getKey();
                int u = (int) (key >> 32);
                int v = (int) key;
                int cnt = entry.getValue();
                int sum = degree[u] + degree[v];
                if (sum > k && sum - cnt <= k) {
                    total--;
                }
            }

            answers[qi] = (int) total;
        }

        return answers;
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        deg = [0] * (n + 1)
        pair_cnt = {}
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            key = (u, v)
            pair_cnt[key] = pair_cnt.get(key, 0) + 1

        sorted_deg = sorted(deg[1:])  # ignore index 0
        m = len(sorted_deg)

        res = []
        for k in queries:
            # count pairs with deg[u] + deg[v] > k ignoring shared edges
            cnt = 0
            l, r = 0, m - 1
            while l < r:
                if sorted_deg[l] + sorted_deg[r] > k:
                    cnt += (r - l)
                    r -= 1
                else:
                    l += 1

            # subtract pairs where after removing shared edges condition fails
            for (u, v), c in pair_cnt.items():
                total = deg[u] + deg[v]
                if total > k and total - c <= k:
                    cnt -= 1
            res.append(cnt)
        return res
```

## Python3

```python
from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        deg = [0] * (n + 1)
        pair_cnt = defaultdict(int)

        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            a, b = (u, v) if u < v else (v, u)
            pair_cnt[(a, b)] += 1

        sorted_deg = sorted(deg[1:])  # degrees of nodes 1..n
        res = []

        for k in queries:
            total = 0
            # count pairs with deg[u] + deg[v] > k ignoring shared edges
            for i in range(n):
                need = k - sorted_deg[i] + 1
                idx = bisect.bisect_left(sorted_deg, need, i + 1)
                total += n - idx

            # correct overcounted pairs where shared edges reduce the sum to <=k
            for (u, v), c in pair_cnt.items():
                if deg[u] + deg[v] > k and deg[u] + deg[v] - c <= k:
                    total -= 1

            res.append(total)

        return res
```

## C

```c
#include <stdlib.h>

typedef struct {
    int u;
    int v;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->u != pb->u) return pa->u - pb->u;
    return pa->v - pb->v;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countPairs(int n, int** edges, int edgesSize, int* edgesColSize,
                int* queries, int queriesSize, int* returnSize) {
    (void)edgesColSize; // unused, each edge has size 2

    int *degree = (int *)calloc(n + 1, sizeof(int));
    Pair *pairs = (Pair *)malloc(sizeof(Pair) * edgesSize);
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        degree[a]++;
        degree[b]++;
        if (a > b) { int tmp = a; a = b; b = tmp; }
        pairs[i].u = a;
        pairs[i].v = b;
    }

    qsort(pairs, edgesSize, sizeof(Pair), cmpPair);

    // compress duplicate unordered pairs
    int *upU = (int *)malloc(sizeof(int) * edgesSize);
    int *upV = (int *)malloc(sizeof(int) * edgesSize);
    int *upCnt = (int *)malloc(sizeof(int) * edgesSize);
    int upSize = 0;
    for (int i = 0; i < edgesSize; ++i) {
        if (i == 0 || pairs[i].u != pairs[i-1].u || pairs[i].v != pairs[i-1].v) {
            upU[upSize] = pairs[i].u;
            upV[upSize] = pairs[i].v;
            upCnt[upSize] = 1;
            ++upSize;
        } else {
            ++upCnt[upSize - 1];
        }
    }

    // sorted degrees array (excluding index 0)
    int *degSorted = (int *)malloc(sizeof(int) * n);
    for (int i = 1; i <= n; ++i) degSorted[i-1] = degree[i];
    qsort(degSorted, n, sizeof(int), cmpPair); // reuse comparator (works for ints)

    int *answers = (int *)malloc(sizeof(int) * queriesSize);
    for (int qi = 0; qi < queriesSize; ++qi) {
        int k = queries[qi];
        long long ans = 0;
        int left = 0, right = n - 1;
        while (left < right) {
            if ((long long)degSorted[left] + degSorted[right] > k) {
                ans += (right - left);
                --right;
            } else {
                ++left;
            }
        }

        // adjust for pairs with multiple edges
        for (int idx = 0; idx < upSize; ++idx) {
            int u = upU[idx];
            int v = upV[idx];
            int cnt = upCnt[idx];
            long long total = (long long)degree[u] + degree[v];
            if (total > k && total - cnt <= k) {
                --ans;
            }
        }

        answers[qi] = (int)ans;
    }

    *returnSize = queriesSize;

    free(degree);
    free(pairs);
    free(upU);
    free(upV);
    free(upCnt);
    free(degSorted);

    return answers;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] CountPairs(int n, int[][] edges, int[] queries) {
        int[] deg = new int[n];
        int offset = n + 1; // for encoding pair keys
        var pairCount = new Dictionary<long, int>();
        
        foreach (var e in edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            deg[u]++;
            deg[v]++;
            if (u > v) { int tmp = u; u = v; v = tmp; }
            long key = ((long)u) * offset + v;
            if (pairCount.TryGetValue(key, out int cnt)) {
                pairCount[key] = cnt + 1;
            } else {
                pairCount[key] = 1;
            }
        }

        int[] sortedDeg = new int[n];
        Array.Copy(deg, sortedDeg, n);
        Array.Sort(sortedDeg);

        int qLen = queries.Length;
        int[] answers = new int[qLen];

        for (int qi = 0; qi < qLen; ++qi) {
            int k = queries[qi];
            long total = 0;
            int r = n - 1;
            for (int i = 0; i < n; ++i) {
                while (r > i && sortedDeg[i] + sortedDeg[r] > k) {
                    r--;
                }
                int first = Math.Max(r + 1, i + 1);
                total += n - first;
            }

            foreach (var kvp in pairCount) {
                long key = kvp.Key;
                int u = (int)(key / offset);
                int v = (int)(key % offset);
                int sum = deg[u] + deg[v];
                int cnt = kvp.Value;
                if (sum > k && sum - cnt <= k) {
                    total--;
                }
            }

            answers[qi] = (int)total;
        }

        return answers;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} queries
 * @return {number[]}
 */
var countPairs = function(n, edges, queries) {
    const deg = new Array(n + 1).fill(0);
    const pairMap = new Map(); // key: "u,v" where u < v
    
    for (const [a, b] of edges) {
        deg[a]++;
        deg[b]++;
        const u = a < b ? a : b;
        const v = a < b ? b : a;
        const key = u + ',' + v;
        pairMap.set(key, (pairMap.get(key) || 0) + 1);
    }
    
    // sorted degrees for two‑pointer counting
    const sortedDeg = deg.slice(1).sort((x, y) => x - y);
    
    // store unique pairs with their multiplicity
    const pairList = [];
    for (const [key, cnt] of pairMap.entries()) {
        const [uStr, vStr] = key.split(',');
        const u = Number(uStr), v = Number(vStr);
        pairList.push({u, v, c: cnt});
    }
    
    const answers = [];
    for (const k of queries) {
        // count pairs with deg[a] + deg[b] > k
        let total = 0;
        let i = 0, j = n - 1;
        while (i < j) {
            if (sortedDeg[i] + sortedDeg[j] > k) {
                total += (j - i);
                j--;
            } else {
                i++;
            }
        }
        // correct overcount where subtraction of common edges invalidates the pair
        for (const p of pairList) {
            const sum = deg[p.u] + deg[p.v];
            if (sum > k && sum - p.c <= k) {
                total--;
            }
        }
        answers.push(total);
    }
    
    return answers;
};
```

## Typescript

```typescript
function countPairs(n: number, edges: number[][], queries: number[]): number[] {
    const deg = new Array(n + 1).fill(0);
    const pairMap = new Map<string, number>();
    for (const [uRaw, vRaw] of edges) {
        const u = uRaw;
        const v = vRaw;
        deg[u]++;
        deg[v]++;
        const a = Math.min(u, v);
        const b = Math.max(u, v);
        const key = `${a},${b}`;
        pairMap.set(key, (pairMap.get(key) ?? 0) + 1);
    }
    const sortedDeg = deg.slice(1).sort((a, b) => a - b);
    const answers: number[] = [];
    for (const k of queries) {
        let cnt = 0;
        let l = 0, r = n - 1;
        while (l < r) {
            if (sortedDeg[l] + sortedDeg[r] > k) {
                cnt += r - l;
                r--;
            } else {
                l++;
            }
        }
        for (const [key, c] of pairMap.entries()) {
            const comma = key.indexOf(',');
            const a = parseInt(key.substring(0, comma), 10);
            const b = parseInt(key.substring(comma + 1), 10);
            const sum = deg[a] + deg[b];
            if (sum > k && sum - c <= k) cnt--;
        }
        answers.push(cnt);
    }
    return answers;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $queries
     * @return Integer[]
     */
    function countPairs($n, $edges, $queries) {
        // degree of each node (1-indexed)
        $deg = array_fill(0, $n + 1, 0);
        // count multiple edges between same unordered pair
        $pairCnt = [];

        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            if ($u > $v) {
                $tmp = $u; $u = $v; $v = $tmp;
            }
            $deg[$u]++;
            $deg[$v]++;

            $key = $u . ':' . $v;
            if (!isset($pairCnt[$key])) {
                $pairCnt[$key] = 0;
            }
            $pairCnt[$key]++;
        }

        // sorted degrees for binary search / two-pointer
        $sortedDeg = array_slice($deg, 1); // remove index 0
        sort($sortedDeg);
        $answers = [];

        foreach ($queries as $k) {
            // count pairs with deg[i] + deg[j] > k using two pointers
            $cnt = 0;
            $i = 0;
            $j = $n - 1;
            while ($i < $j) {
                if ($sortedDeg[$i] + $sortedDeg[$j] > $k) {
                    $cnt += $j - $i;
                    $j--;
                } else {
                    $i++;
                }
            }

            // adjust for pairs where multiple edges reduce the effective sum
            foreach ($pairCnt as $key => $c) {
                [$u, $v] = array_map('intval', explode(':', $key));
                $sum = $deg[$u] + $deg[$v];
                if ($sum > $k && $sum - $c <= $k) {
                    $cnt--;
                }
            }

            $answers[] = $cnt;
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    func countPairs(_ n: Int, _ edges: [[Int]], _ queries: [Int]) -> [Int] {
        var degree = Array(repeating: 0, count: n + 1)
        var pairCount = [Int64:Int]()
        for e in edges {
            let u = e[0]
            let v = e[1]
            degree[u] += 1
            degree[v] += 1
            let a = min(u, v)
            let b = max(u, v)
            let key = (Int64(a) << 32) | Int64(b)
            pairCount[key, default: 0] += 1
        }
        var degList = [Int]()
        degList.reserveCapacity(n)
        for i in 1...n {
            degList.append(degree[i])
        }
        let sortedDeg = degList.sorted()
        let m = n
        var result = [Int]()
        for q in queries {
            var ans = 0
            // count pairs with degree sum > q using binary search
            for i in 0..<m {
                var lo = i + 1
                var hi = m - 1
                var pos = m
                while lo <= hi {
                    let mid = (lo + hi) >> 1
                    if sortedDeg[i] + sortedDeg[mid] > q {
                        pos = mid
                        hi = mid - 1
                    } else {
                        lo = mid + 1
                    }
                }
                ans += m - pos
            }
            // adjust for pairs where shared edges reduce the count
            for (key, cnt) in pairCount {
                let a = Int(key >> 32)
                let b = Int(key & 0xffffffff)
                if degree[a] + degree[b] > q && degree[a] + degree[b] - cnt <= q {
                    ans -= 1
                }
            }
            result.append(ans)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(n: Int, edges: Array<IntArray>, queries: IntArray): IntArray {
        val deg = IntArray(n + 1)
        val pairCount = HashMap<Long, Int>()
        for (e in edges) {
            var u = e[0]
            var v = e[1]
            deg[u]++
            deg[v]++
            if (u > v) {
                val tmp = u
                u = v
                v = tmp
            }
            val key = (u.toLong() shl 32) or v.toLong()
            pairCount[key] = (pairCount[key] ?: 0) + 1
        }

        // sorted degrees for two‑pointer counting
        val sortedDeg = IntArray(n)
        for (i in 1..n) {
            sortedDeg[i - 1] = deg[i]
        }
        java.util.Arrays.sort(sortedDeg)

        // store pair info to adjust answers later
        data class PairInfo(val u: Int, val v: Int, val cnt: Int)
        val pairs = ArrayList<PairInfo>(pairCount.size)
        for ((key, cnt) in pairCount) {
            val u = (key shr 32).toInt()
            val v = (key and 0xffffffffL).toInt()
            pairs.add(PairInfo(u, v, cnt))
        }

        val res = IntArray(queries.size)
        for (qi in queries.indices) {
            val k = queries[qi]
            var total = 0L
            var l = 0
            var r = n - 1
            while (l < r) {
                if (sortedDeg[l] + sortedDeg[r] > k) {
                    total += (r - l).toLong()
                    r--
                } else {
                    l++
                }
            }

            // adjust for pairs with multiple edges
            for (p in pairs) {
                val sum = deg[p.u] + deg[p.v]
                if (sum > k && sum - p.cnt <= k) {
                    total--
                }
            }
            res[qi] = total.toInt()
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> countPairs(int n, List<List<int>> edges, List<int> queries) {
    // degree of each node (1-indexed)
    List<int> deg = List.filled(n + 1, 0);
    // map to store number of parallel edges between unordered pair (u<v)
    Map<int, int> pairCnt = {};

    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      deg[u]++;
      deg[v]++;

      if (u > v) {
        int tmp = u;
        u = v;
        v = tmp;
      }
      int key = u * (n + 1) + v; // unique encoding
      pairCnt[key] = (pairCnt[key] ?? 0) + 1;
    }

    // sorted degrees for binary search (exclude index 0)
    List<int> sortedDeg = deg.sublist(1);
    sortedDeg.sort();

    int lowerBound(List<int> arr, int target) {
      int l = 0, r = arr.length;
      while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] >= target) {
          r = m;
        } else {
          l = m + 1;
        }
      }
      return l;
    }

    List<int> answers = [];

    for (int k in queries) {
      int ans = 0;
      // count pairs based on degree sum > k
      for (int i = 0; i < n; ++i) {
        int need = k - sortedDeg[i] + 1; // we need other degree >= need
        int idx = lowerBound(sortedDeg, need);
        if (idx <= i) idx = i + 1;
        ans += n - idx;
      }

      // correct for pairs with parallel edges
      pairCnt.forEach((key, cnt) {
        int u = key ~/ (n + 1);
        int v = key % (n + 1);
        int sumDeg = deg[u] + deg[v];
        if (sumDeg > k && sumDeg - cnt <= k) {
          ans--;
        }
      });

      answers.add(ans);
    }

    return answers;
  }
}
```

## Golang

```go
package main

import "sort"

func countPairs(n int, edges [][]int, queries []int) []int {
	deg := make([]int, n)
	pairCnt := make(map[int]int)

	for _, e := range edges {
		u := e[0] - 1
		v := e[1] - 1
		deg[u]++
		deg[v]++
		if u > v {
			u, v = v, u
		}
		key := u*n + v
		pairCnt[key]++
	}

	sortedDeg := make([]int, n)
	copy(sortedDeg, deg)
	sort.Ints(sortedDeg)

	ansArr := make([]int, len(queries))
	for qi, k := range queries {
		total := 0
		for i := 0; i < n; i++ {
			idx := sort.Search(n, func(j int) bool { return sortedDeg[i]+sortedDeg[j] > k })
			start := idx
			if start <= i {
				start = i + 1
			}
			total += n - start
		}

		for key, cnt := range pairCnt {
			u := key / n
			v := key % n
			sum := deg[u] + deg[v]
			if sum > k && sum-cnt <= k {
				total--
			}
		}
		ansArr[qi] = total
	}
	return ansArr
}
```

## Ruby

```ruby
def count_pairs(n, edges, queries)
  deg = Array.new(n + 1, 0)
  pair_cnt = Hash.new(0)

  edges.each do |u, v|
    deg[u] += 1
    deg[v] += 1
    a, b = u < v ? [u, v] : [v, u]
    pair_cnt[[a, b]] += 1
  end

  sorted_deg = deg[1..n].sort
  m = n
  answers = []

  queries.each do |k|
    total = 0
    sorted_deg.each_with_index do |d, i|
      lo = i + 1
      hi = m - 1
      pos = m
      while lo <= hi
        mid = (lo + hi) / 2
        if d + sorted_deg[mid] > k
          pos = mid
          hi = mid - 1
        else
          lo = mid + 1
        end
      end
      total += m - pos if pos < m
    end

    pair_cnt.each do |(a, b), cnt|
      sum = deg[a] + deg[b]
      if sum > k && sum - cnt <= k
        total -= 1
      end
    end

    answers << total
  end

  answers
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def countPairs(n: Int, edges: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
        val degree = new Array[Int](n + 1)
        val pairCnt = mutable.HashMap[Long, Int]()
        for (e <- edges) {
            var u = e(0)
            var v = e(1)
            degree(u) += 1
            degree(v) += 1
            if (u > v) { val tmp = u; u = v; v = tmp }
            val key = (u.toLong << 32) | v.toLong
            pairCnt.put(key, pairCnt.getOrElse(key, 0) + 1)
        }

        // sorted degrees for two‑pointer counting
        val degSorted = degree.slice(1, n + 1).clone()
        java.util.Arrays.sort(degSorted)

        val answers = new Array[Int](queries.length)

        for (qi <- queries.indices) {
            val k = queries(qi)
            var total: Long = 0L
            var l = 0
            var r = n - 1
            while (l < r) {
                if (degSorted(l).toLong + degSorted(r).toLong > k) {
                    total += (r - l)
                    r -= 1
                } else {
                    l += 1
                }
            }

            // correct over‑counted pairs where the shared edges reduce the sum
            for ((key, cntEdges) <- pairCnt) {
                val u = (key >> 32).toInt
                val v = (key & 0xffffffffL).toInt
                val sum = degree(u) + degree(v)
                if (sum > k && sum - cntEdges <= k) {
                    total -= 1
                }
            }

            answers(qi) = total.toInt
        }

        answers
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut deg = vec![0i32; n_usize + 1];
        use std::collections::HashMap;
        let mut pair_cnt: HashMap<(i32, i32), i32> = HashMap::new();

        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            deg[u] += 1;
            deg[v] += 1;
            let (a, b) = if e[0] < e[1] { (e[0], e[1]) } else { (e[1], e[0]) };
            *pair_cnt.entry((a, b)).or_insert(0) += 1;
        }

        // sorted degrees without the dummy zero index
        let mut deg_sorted: Vec<i32> = deg.iter().skip(1).cloned().collect();
        deg_sorted.sort_unstable();

        let mut answers = Vec::with_capacity(queries.len());

        for &q in queries.iter() {
            let mut cnt_pairs: i64 = 0;
            let len = deg_sorted.len();

            // count pairs ignoring multiple edges
            for i in 0..len {
                let need = q - deg_sorted[i];
                // find first index > i where degree > need
                let mut l = i + 1;
                let mut r = len;
                while l < r {
                    let mid = (l + r) / 2;
                    if deg_sorted[mid] <= need {
                        l = mid + 1;
                    } else {
                        r = mid;
                    }
                }
                cnt_pairs += (len - l) as i64;
            }

            // correct for pairs with multiple edges
            for (&(a, b), &c) in pair_cnt.iter() {
                let sum = deg[a as usize] + deg[b as usize];
                if sum > q && sum - c <= q {
                    cnt_pairs -= 1;
                }
            }

            answers.push(cnt_pairs as i32);
        }

        answers
    }
}
```

## Racket

```racket
(define/contract (count-pairs n edges queries)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof exact-integer?)
      (listof exact-integer?))
  (let* ((deg (make-vector (+ n 1) 0))
         ;; compute degrees and edge multiplicities
         (pair-count (make-hash)))
    (for ([e edges])
      (let* ((u (list-ref e 0))
             (v (list-ref e 1)))
        (vector-set! deg u (+ (vector-ref deg u) 1))
        (vector-set! deg v (+ (vector-ref deg v) 1))
        (define a (min u v))
        (define b (max u v))
        (define key (cons a b))
        (hash-set! pair-count key (+ (hash-ref pair-count key 0) 1))))
    ;; sorted degree list
    (define sorted-deg
      (sort (for/list ([i (in-range 1 (+ n 1))]) (vector-ref deg i)) <))
    (define m (vector-length deg)) ; = n+1, not used directly
    (define answers '())
    (for ([k queries])
      ;; base count using two‑pointer
      (let loop ((l 0) (r (- (length sorted-deg) 1)) (cnt 0))
        (if (>= l r)
            (set! cnt cnt)
            (if (> (+ (list-ref sorted-deg l) (list-ref sorted-deg r)) k)
                (loop l (- r 1) (+ cnt (- r l)))
                (loop (+ l 1) r cnt))))
      ;; adjust for over‑counted pairs with multiple edges
      (let ((base cnt))
        (for ([kv (in-hash pair-count)])
          (define a (car kv))
          (define b (cdr kv))
          (define c (hash-ref pair-count kv))
          (when (and (> (+ (vector-ref deg a) (vector-ref deg b)) k)
                     (<= (- (+ (vector-ref deg a) (vector-ref deg b)) c) k))
            (set! base (- base 1))))
        (set! answers (cons base answers))))
    (reverse answers)))
```

## Erlang

```erlang
-spec count_pairs(N :: integer(), Edges :: [[integer()]], Queries :: [integer()]) -> [integer()].
count_pairs(N, Edges, Queries) ->
    {DegArr, EdgeCntMap} = lists:foldl(
        fun([U, V], {DegA, EC}) ->
            DegU = array:get(U, DegA),
            DegA1 = array:set(U, DegU + 1, DegA),
            DegV = array:get(V, DegA1),
            DegA2 = array:set(V, DegV + 1, DegA1),
            {A, B} = if U < V -> {U, V}; true -> {V, U} end,
            EC1 = maps:update_with({A, B}, fun(C) -> C + 1 end, 1, EC),
            {DegA2, EC1}
        end,
        {array:new(N + 1, {default, 0}), #{}},
        Edges),

    DegList = [array:get(I, DegArr) || I <- lists:seq(1, N)],
    SortedTuple = list_to_tuple(lists:sort(DegList)),

    lists:map(
        fun(K) ->
            Total = count_pairs_sum_gt(K, SortedTuple, N),
            Adj = maps:fold(
                fun({U, V}, Cnt, Acc) ->
                    Du = array:get(U, DegArr),
                    Dv = array:get(V, DegArr),
                    if Du + Dv > K andalso Du + Dv - Cnt =< K -> Acc - 1;
                       true -> Acc
                    end
                end,
                Total,
                EdgeCntMap),
            Adj
        end,
        Queries).

-spec count_pairs_sum_gt(K :: integer(), Tuple :: tuple(), N :: integer()) -> integer().
count_pairs_sum_gt(K, Tuple, N) ->
    loop(1, N, 0, K, Tuple).

-spec loop(L :: integer(), R :: integer(), Acc :: integer(), K :: integer(), Tuple :: tuple()) -> integer().
loop(L, R, Acc, _K, _Tuple) when L >= R ->
    Acc;
loop(L, R, Acc, K, Tuple) ->
    Sum = erlang:element(L, Tuple) + erlang:element(R, Tuple),
    if
        Sum > K ->
            NewAcc = Acc + (R - L),
            loop(L, R - 1, NewAcc, K, Tuple);
        true ->
            loop(L + 1, R, Acc, K, Tuple)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(n :: integer, edges :: [[integer]], queries :: [integer]) :: [integer]
  def count_pairs(n, edges, queries) do
    {deg_map, edge_counts} = build_maps(edges, %{}, %{})
    degrees = Enum.map(1..n, fn i -> Map.get(deg_map, i, 0) end)
    sorted = Enum.sort(degrees)
    sorted_t = List.to_tuple(sorted)

    Enum.map(queries, fn k ->
      base = count_pairs_sorted(sorted_t, length(sorted), k)
      adjust(base, edge_counts, deg_map, k)
    end)
  end

  defp build_maps([], deg_map, edge_counts), do: {deg_map, edge_counts}
  defp build_maps([[u, v] | rest], deg_map, edge_counts) do
    deg_map = Map.update(deg_map, u, 1, &(&1 + 1))
    deg_map = Map.update(deg_map, v, 1, &(&1 + 1))

    key = if u < v, do: {u, v}, else: {v, u}
    edge_counts = Map.update(edge_counts, key, 1, &(&1 + 1))
    build_maps(rest, deg_map, edge_counts)
  end

  defp count_pairs_sorted(sorted_t, n, k) do
    do_count(sorted_t, k, 0, n - 1, 0)
  end

  defp do_count(_sorted_t, _k, i, j, acc) when i >= j, do: acc
  defp do_count(sorted_t, k, i, j, acc) do
    if elem(sorted_t, i) + elem(sorted_t, j) > k do
      do_count(sorted_t, k, i, j - 1, acc + (j - i))
    else
      do_count(sorted_t, k, i + 1, j, acc)
    end
  end

  defp adjust(ans, edge_counts, deg_map, k) do
    Enum.reduce(edge_counts, ans, fn {{u, v}, cnt}, acc ->
      sum = Map.get(deg_map, u, 0) + Map.get(deg_map, v, 0)

      if sum > k and sum - cnt <= k do
        acc - 1
      else
        acc
      end
    end)
  end
end
```
