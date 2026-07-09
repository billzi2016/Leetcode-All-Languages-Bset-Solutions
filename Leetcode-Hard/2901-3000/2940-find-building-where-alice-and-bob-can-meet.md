# 2940. Find Building Where Alice and Bob Can Meet

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        int n = heights.size();
        int m = queries.size();
        vector<int> ans(m, -1);
        vector<vector<pair<int,int>>> bucket(n); // for each b store (a, queryId)

        for (int id = 0; id < m; ++id) {
            int a = queries[id][0];
            int b = queries[id][1];
            if (a == b) {
                ans[id] = a;
                continue;
            }
            if (a > b) swap(a, b); // ensure a < b
            if (heights[a] < heights[b]) {
                ans[id] = b; // Alice can move directly to Bob's building
            } else {
                bucket[b].push_back({a, id}); // need to search for t > b with height > heights[a]
            }
        }

        vector<pair<int,int>> st; // (height, index), decreasing heights
        for (int i = n - 1; i >= 0; --i) {
            // answer queries whose larger index is i
            for (auto &pr : bucket[i]) {
                int aIdx = pr.first;
                int qid = pr.second;
                int need = heights[aIdx];
                if (!st.empty()) {
                    int l = 0, r = (int)st.size() - 1;
                    while (l < r) {
                        int mid = (l + r) / 2;
                        if (st[mid].first > need) r = mid;
                        else l = mid + 1;
                    }
                    if (st[l].first > need) ans[qid] = st[l].second;
                }
            }
            // maintain monotonic decreasing stack
            while (!st.empty() && st.back().first <= heights[i]) st.pop_back();
            st.push_back({heights[i], i});
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] leftmostBuildingQueries(int[] heights, int[][] queries) {
        int n = heights.length;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<int[]>[] bucket = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) bucket[i] = new java.util.ArrayList<>();
        int m = queries.length;
        int[] ans = new int[m];
        java.util.Arrays.fill(ans, -1);
        for (int idx = 0; idx < m; idx++) {
            int a = queries[idx][0];
            int b = queries[idx][1];
            if (a > b) { int tmp = a; a = b; b = tmp; }
            if (a == b) {
                ans[idx] = a;
            } else if (heights[a] < heights[b]) {
                ans[idx] = b;
            } else {
                bucket[b].add(new int[]{heights[a], idx});
            }
        }
        java.util.ArrayList<Integer> stack = new java.util.ArrayList<>();
        for (int i = n - 1; i >= 0; i--) {
            // answer queries whose right endpoint is i
            for (int[] qinfo : bucket[i]) {
                int thresh = qinfo[0];
                int qid = qinfo[1];
                if (!stack.isEmpty() && heights[stack.get(0)] > thresh) {
                    ans[qid] = stack.get(0);
                } else {
                    ans[qid] = -1;
                }
            }
            // maintain monotonic decreasing stack of heights
            while (!stack.isEmpty() && heights[stack.get(stack.size() - 1)] <= heights[i]) {
                stack.remove(stack.size() - 1);
            }
            stack.add(i);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(heights)
        # build segment tree for range maximum
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2 * size)
        for i in range(n):
            seg[size + i] = heights[i]
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        import sys
        sys.setrecursionlimit(1000000)

        def find_first(pos, val):
            # first index >= pos with height > val
            return _find(1, 0, size - 1, pos, val)

        def _find(node, l, r, pos, val):
            if r < pos or seg[node] <= val:
                return -1
            if l == r:
                return l
            mid = (l + r) // 2
            left_res = _find(node * 2, l, mid, pos, val)
            if left_res != -1:
                return left_res
            return _find(node * 2 + 1, mid + 1, r, pos, val)

        ans = []
        for a, b in queries:
            if a == b:
                ans.append(a)
                continue
            if a > b:
                a, b = b, a  # ensure a < b
            if heights[a] < heights[b]:
                ans.append(b)
                continue
            idx = find_first(b + 1, heights[a])
            if idx == -1 or idx >= n:
                ans.append(-1)
            else:
                ans.append(idx)
        return ans
```

## Python3

```python
class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        m = len(queries)
        ans = [-1] * m
        # bucket queries by right index b where we need to search
        buckets = [[] for _ in range(n)]
        for idx, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[idx] = b
            else:
                # need smallest t > b with height > heights[a]
                buckets[b].append((heights[a], idx))

        stack_h = []   # decreasing heights
        stack_i = []   # corresponding indices

        for i in range(n - 1, -1, -1):
            # answer queries whose right endpoint is i
            if buckets[i]:
                # binary search on decreasing height list
                for thresh, qid in buckets[i]:
                    lo, hi = 0, len(stack_h) - 1
                    best = -1
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        if stack_h[mid] > thresh:
                            best = stack_i[mid]
                            lo = mid + 1   # look for later (smaller index) still > thresh
                        else:
                            hi = mid - 1
                    ans[qid] = best if best != -1 else -1

            # maintain monotonic decreasing stack
            while stack_h and stack_h[-1] <= heights[i]:
                stack_h.pop()
                stack_i.pop()
            stack_h.append(heights[i])
            stack_i.append(i)

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int h;
    int pos;
} HeightPos;

typedef struct {
    int thresh;
    int y;
    int idx;
} QueryProc;

/* Comparator for descending height */
static int cmpHeightDesc(const void *a, const void *b) {
    const HeightPos *ha = (const HeightPos *)a;
    const HeightPos *hb = (const HeightPos *)b;
    return hb->h - ha->h;
}

/* Comparator for descending threshold */
static int cmpQueryDesc(const void *a, const void *b) {
    const QueryProc *qa = (const QueryProc *)a;
    const QueryProc *qb = (const QueryProc *)b;
    return qb->thresh - qa->thresh;
}

/* Fenwick Tree */
typedef struct {
    int n;
    int *bit;
} BIT;

static BIT *bitCreate(int n) {
    BIT *t = (BIT *)malloc(sizeof(BIT));
    t->n = n;
    t->bit = (int *)calloc(n + 1, sizeof(int)); /* 1-indexed */
    return t;
}

static void bitAdd(BIT *t, int idx, int val) {   /* idx: 0‑based */
    for (idx++; idx <= t->n; idx += idx & -idx)
        t->bit[idx] += val;
}

static int bitSumPrefix(BIT *t, int idx) {      /* sum of [0, idx) , idx 0‑based */
    int res = 0;
    for (; idx > 0; idx -= idx & -idx)
        res += t->bit[idx];
    return res;
}

/* find smallest index >= start (0‑based) that has a value in BIT.
   assumes there is at least one such element. */
static int bitFindFirstAfter(BIT *t, int start) {
    int sumBefore = bitSumPrefix(t, start + 1);          /* include start */
    int target = sumBefore + 1;                          /* next element */
    int idx = 0;
    int mask = 1;
    while ((mask << 1) <= t->n) mask <<= 1;
    for (int k = mask; k > 0; k >>= 1) {
        int nxt = idx + k;
        if (nxt <= t->n && t->bit[nxt] < target) {
            idx = nxt;
            target -= t->bit[nxt];
        }
    }
    return idx;   /* zero‑based index of the found position */
}

/* Main function */
int* leftmostBuildingQueries(int* heights, int heightsSize,
                             int** queries, int queriesSize,
                             int* queriesColSize, int* returnSize) {
    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) ans[i] = -1;

    /* Prepare height array */
    HeightPos *hp = (HeightPos *)malloc(sizeof(HeightPos) * heightsSize);
    for (int i = 0; i < heightsSize; ++i) {
        hp[i].h = heights[i];
        hp[i].pos = i;
    }
    qsort(hp, heightsSize, sizeof(HeightPos), cmpHeightDesc);

    /* Collect queries that need searching */
    QueryProc *proc = (QueryProc *)malloc(sizeof(QueryProc) * queriesSize);
    int procCnt = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int a = queries[i][0];
        int b = queries[i][1];
        if (a > b) { int tmp = a; a = b; b = tmp; }
        if (a == b || heights[a] < heights[b]) {
            ans[i] = b;
        } else {
            proc[procCnt].thresh = heights[a];
            proc[procCnt].y = b;
            proc[procCnt].idx = i;
            ++procCnt;
        }
    }

    if (procCnt > 0) {
        qsort(proc, procCnt, sizeof(QueryProc), cmpQueryDesc);
        BIT *bit = bitCreate(heightsSize);
        int p = 0;   /* pointer in hp */

        for (int i = 0; i < procCnt; ++i) {
            int th = proc[i].thresh;
            while (p < heightsSize && hp[p].h > th) {
                bitAdd(bit, hp[p].pos, 1);
                ++p;
            }
            /* check if any index > y exists */
            int totalAfterY = bitSumPrefix(bit, heightsSize) - bitSumPrefix(bit, proc[i].y + 1);
            if (totalAfterY == 0) {
                ans[proc[i].idx] = -1;
            } else {
                int pos = bitFindFirstAfter(bit, proc[i].y);
                ans[proc[i].idx] = pos;
            }
        }
        free(bit->bit);
        free(bit);
    }

    free(hp);
    free(proc);

    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private struct QueryInfo {
        public int Threshold;
        public int Index;
    }

    public int[] LeftmostBuildingQueries(int[] heights, int[][] queries) {
        int n = heights.Length;
        int q = queries.Length;
        int[] answer = new int[q];
        for (int i = 0; i < q; i++) answer[i] = -1;

        // bucket each query by its larger index (after ordering)
        List<QueryInfo>[] bucket = new List<QueryInfo>[n];
        for (int i = 0; i < n; i++) bucket[i] = new List<QueryInfo>();

        for (int i = 0; i < q; i++) {
            int a = queries[i][0];
            int b = queries[i][1];
            if (a > b) { int tmp = a; a = b; b = tmp; }

            if (a == b) {
                answer[i] = a;
                continue;
            }
            if (heights[a] < heights[b]) {
                answer[i] = b;
                continue;
            }
            // need to find first index > b with height > heights[a]
            bucket[b].Add(new QueryInfo { Threshold = heights[a], Index = i });
        }

        List<int> stack = new List<int>(); // indices with decreasing heights

        for (int i = n - 1; i >= 0; i--) {
            // answer queries whose max index is i
            foreach (var qi in bucket[i]) {
                int pos = -1;
                int l = 0, r = stack.Count - 1;
                while (l <= r) {
                    int m = (l + r) >> 1;
                    if (heights[stack[m]] > qi.Threshold) {
                        pos = m;          // candidate, look for later (smaller index) still > threshold
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
                answer[qi.Index] = (pos == -1) ? -1 : stack[pos];
            }

            // maintain monotonic decreasing heights in the stack
            while (stack.Count > 0 && heights[stack[stack.Count - 1]] <= heights[i]) {
                stack.RemoveAt(stack.Count - 1);
            }
            stack.Add(i);
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} heights
 * @param {number[][]} queries
 * @return {number[]}
 */
var leftmostBuildingQueries = function(heights, queries) {
    const n = heights.length;
    const ans = new Array(queries.length).fill(-1);
    // buckets for queries that need processing at position y (max index)
    const bucket = Array.from({length: n}, () => []);
    
    for (let i = 0; i < queries.length; ++i) {
        let [a, b] = queries[i];
        if (a > b) { const tmp = a; a = b; b = tmp; }
        if (a === b) {
            ans[i] = a;
        } else if (heights[a] < heights[b]) {
            // Alice can move directly to Bob's building
            ans[i] = b;
        } else {
            // need to find t > b with height > heights[a]
            bucket[b].push({threshold: heights[a], idx: i});
        }
    }

    const stack = []; // will store indices, heights decreasing from bottom to top

    for (let pos = n - 1; pos >= 0; --pos) {
        // answer queries whose max index is current pos
        if (bucket[pos].length) {
            for (const q of bucket[pos]) {
                const th = q.threshold;
                // binary search rightmost position in stack with height > th
                let l = 0, r = stack.length - 1, best = -1;
                while (l <= r) {
                    const mid = (l + r) >> 1;
                    if (heights[stack[mid]] > th) {
                        best = mid;
                        l = mid + 1; // look for later (closer to top) occurrence
                    } else {
                        r = mid - 1;
                    }
                }
                ans[q.idx] = best === -1 ? -1 : stack[best];
            }
        }

        // maintain monotonic decreasing height stack
        while (stack.length && heights[stack[stack.length - 1]] <= heights[pos]) {
            stack.pop();
        }
        stack.push(pos);
    }

    return ans;
};
```

## Typescript

```typescript
function leftmostBuildingQueries(heights: number[], queries: number[][]): number[] {
    const n = heights.length;
    let size = 1;
    while (size < n) size <<= 1;
    const seg = new Array(2 * size).fill(-Infinity);
    for (let i = 0; i < n; i++) seg[size + i] = heights[i];
    for (let i = size - 1; i > 0; --i) {
        seg[i] = Math.max(seg[2 * i], seg[2 * i + 1]);
    }

    function findFirst(l: number, thresh: number): number {
        const dfs = (node: number, nl: number, nr: number): number => {
            if (nr < l || seg[node] <= thresh) return -1;
            if (nl === nr) return nl;
            const mid = (nl + nr) >> 1;
            const leftRes = dfs(node * 2, nl, mid);
            if (leftRes !== -1) return leftRes;
            return dfs(node * 2 + 1, mid + 1, nr);
        };
        return dfs(1, 0, size - 1);
    }

    const ans: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        let a = queries[i][0];
        let b = queries[i][1];
        if (a > b) { const t = a; a = b; b = t; }
        if (a === b) {
            ans[i] = a;
        } else if (heights[a] < heights[b]) {
            ans[i] = b;
        } else {
            const t = findFirst(b + 1, heights[a]);
            ans[i] = t === -1 ? -1 : t;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function leftmostBuildingQueries($heights, $queries) {
        $n = count($heights);
        $m = count($queries);
        $ans = array_fill(0, $m, -1);
        // buckets for queries grouped by right index (y)
        $buckets = array_fill(0, $n, []);
        
        foreach ($queries as $qid => $pair) {
            $a = $pair[0];
            $b = $pair[1];
            if ($a > $b) {
                $tmp = $a; $a = $b; $b = $tmp;
            }
            if ($a == $b) {
                $ans[$qid] = $a;
                continue;
            }
            if ($heights[$a] < $heights[$b]) {
                $ans[$qid] = $b;
                continue;
            }
            // need first index > b with height > heights[a]
            $threshold = $heights[$a];
            $buckets[$b][] = [$threshold, $qid];
        }

        $stackIdx = [];
        $stackHeight = [];

        for ($i = $n - 1; $i >= 0; --$i) {
            // answer queries whose right endpoint is i
            foreach ($buckets[$i] as $item) {
                [$threshold, $qid] = $item;
                $l = 0;
                $r = count($stackIdx) - 1;
                $pos = -1;
                while ($l <= $r) {
                    $mid = intdiv($l + $r, 2);
                    if ($stackHeight[$mid] > $threshold) {
                        $pos = $mid;
                        $r = $mid - 1; // look for earlier (smaller index)
                    } else {
                        $l = $mid + 1;
                    }
                }
                if ($pos != -1) {
                    $ans[$qid] = $stackIdx[$pos];
                }
            }

            // maintain monotonic decreasing stack of heights
            while (!empty($stackIdx) && $heights[$i] >= $stackHeight[count($stackIdx) - 1]) {
                array_pop($stackIdx);
                array_pop($stackHeight);
            }
            $stackIdx[] = $i;
            $stackHeight[] = $heights[$i];
        }

        return $ans;
    }
}
```

## Swift

```swift
class BIT {
    private var n: Int
    private var tree: [Int]
    init(_ n: Int) {
        self.n = n
        self.tree = Array(repeating: 0, count: n + 2)
    }
    func add(_ idx: Int, _ delta: Int) {
        var i = idx
        while i <= n {
            tree[i] += delta
            i += i & -i
        }
    }
    func sum(_ idx: Int) -> Int {
        var res = 0
        var i = idx
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
    // smallest index such that prefix sum >= target (1-indexed)
    func lowerBound(_ target: Int) -> Int {
        var idx = 0
        var bitMask = 1
        while (bitMask << 1) <= n { bitMask <<= 1 }
        var mask = bitMask
        var cur = 0
        while mask != 0 {
            let next = idx + mask
            if next <= n && cur + tree[next] < target {
                idx = next
                cur += tree[next]
            }
            mask >>= 1
        }
        return idx + 1
    }
}

class Solution {
    func leftmostBuildingQueries(_ heights: [Int], _ queries: [[Int]]) -> [Int] {
        let n = heights.count
        var answer = Array(repeating: -1, count: queries.count)
        var pending: [(threshold: Int, b: Int, idx: Int)] = []
        
        for (i, q) in queries.enumerated() {
            var a = q[0]
            var b = q[1]
            if a > b { swap(&a, &b) }
            if a == b || heights[a] < heights[b] {
                answer[i] = b
            } else {
                pending.append((threshold: heights[a], b: b, idx: i))
            }
        }
        
        // sort buildings by height descending
        var buildingList: [(h: Int, idx: Int)] = []
        buildingList.reserveCapacity(n)
        for i in 0..<n {
            buildingList.append((heights[i], i))
        }
        buildingList.sort { $0.h > $1.h }
        
        // sort pending queries by threshold descending
        pending.sort { $0.threshold > $1.threshold }
        
        let bit = BIT(n)
        var p = 0
        
        for q in pending {
            while p < n && buildingList[p].h > q.threshold {
                bit.add(buildingList[p].idx + 1, 1)
                p += 1
            }
            let sumUpToB = bit.sum(q.b + 1) // inclusive of b (0-indexed)
            let totalActive = bit.sum(n)
            if totalActive - sumUpToB == 0 {
                answer[q.idx] = -1
            } else {
                let target = sumUpToB + 1
                let pos = bit.lowerBound(target) // 1-indexed
                answer[q.idx] = pos - 1
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun leftmostBuildingQueries(heights: IntArray, queries: Array<IntArray>): IntArray {
        val n = heights.size
        val m = queries.size
        val ans = IntArray(m) { -1 }
        val bucket = Array(n) { mutableListOf<Pair<Int, Int>>() } // (threshold, queryIdx)

        for (i in 0 until m) {
            var a = queries[i][0]
            var b = queries[i][1]
            if (a > b) {
                val tmp = a
                a = b
                b = tmp
            }
            if (a == b || heights[a] < heights[b]) {
                ans[i] = b
            } else {
                bucket[b].add(Pair(heights[a], i))
            }
        }

        val stack = mutableListOf<Int>()
        for (i in n - 1 downTo 0) {
            // answer queries whose right endpoint is i
            for ((threshold, qIdx) in bucket[i]) {
                var l = 0
                var r = stack.size - 1
                var pos = -1
                while (l <= r) {
                    val mid = (l + r) ushr 1
                    if (heights[stack[mid]] > threshold) {
                        pos = mid
                        r = mid - 1
                    } else {
                        l = mid + 1
                    }
                }
                if (pos != -1) ans[qIdx] = stack[pos]
            }

            // maintain monotonic decreasing heights stack (heights increase in the list)
            while (stack.isNotEmpty() && heights[stack.last()] <= heights[i]) {
                stack.removeAt(stack.size - 1)
            }
            stack.add(i)
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> leftmostBuildingQueries(List<int> heights, List<List<int>> queries) {
    int n = heights.length;
    int size = 1;
    while (size < n) size <<= 1;
    List<int> seg = List.filled(2 * size, 0);
    for (int i = 0; i < n; i++) seg[size + i] = heights[i];
    for (int i = size - 1; i >= 1; i--) {
      seg[i] = seg[2 * i] > seg[2 * i + 1] ? seg[2 * i] : seg[2 * i + 1];
    }

    int findFirst(int l, int h) {
      if (l >= n) return -1;
      int dfs(int idx, int left, int right) {
        if (right < l || seg[idx] <= h) return -1;
        if (left == right) {
          return left < n ? left : -1;
        }
        int mid = (left + right) >> 1;
        int res = dfs(idx * 2, left, mid);
        if (res != -1) return res;
        return dfs(idx * 2 + 1, mid + 1, right);
      }

      return dfs(1, 0, size - 1);
    }

    List<int> ans = List.filled(queries.length, -1);
    for (int i = 0; i < queries.length; i++) {
      int a = queries[i][0];
      int b = queries[i][1];
      if (a == b) {
        ans[i] = a;
        continue;
      }
      if (a > b) {
        int tmp = a;
        a = b;
        b = tmp;
      }
      // now a < b
      if (heights[a] < heights[b]) {
        ans[i] = b;
      } else {
        int t = findFirst(b + 1, heights[a]);
        ans[i] = t;
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

func leftmostBuildingQueries(heights []int, queries [][]int) []int {
	n := len(heights)
	m := len(queries)
	ans := make([]int, m)
	for i := range ans {
		ans[i] = -1
	}

	type qInfo struct {
		th int // threshold height (heights[x])
		id int // original query index
	}
	buckets := make([][]qInfo, n)

	for idx, q := range queries {
		x, y := q[0], q[1]
		if x > y {
			x, y = y, x
		}
		if x == y || heights[x] < heights[y] {
			ans[idx] = y
			continue
		}
		buckets[y] = append(buckets[y], qInfo{th: heights[x], id: idx})
	}

	stack := make([]int, 0) // stores indices with decreasing heights

	for i := n - 1; i >= 0; i-- {
		// answer queries whose right endpoint is i
		if len(buckets[i]) > 0 {
			for _, q := range buckets[i] {
				lo, hi := 0, len(stack)-1
				pos := -1
				for lo <= hi {
					mid := (lo + hi) >> 1
					if heights[stack[mid]] > q.th {
						pos = mid
						lo = mid + 1 // look for rightmost true
					} else {
						hi = mid - 1
					}
				}
				if pos != -1 {
					ans[q.id] = stack[pos]
				}
			}
		}
		// maintain monotonic decreasing stack of heights
		for len(stack) > 0 && heights[i] >= heights[stack[len(stack)-1]] {
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}

	return ans
}
```

## Ruby

```ruby
def leftmost_building_queries(heights, queries)
  n = heights.length
  q = queries.length
  ans = Array.new(q, -1)
  bucket = Array.new(n) { [] }

  queries.each_with_index do |pair, idx|
    a, b = pair[0], pair[1]
    if a > b
      a, b = b, a
    end
    if a == b
      ans[idx] = a
    elsif heights[a] < heights[b]
      ans[idx] = b
    else
      bucket[b] << [heights[a], idx]
    end
  end

  stack = [] # indices with strictly decreasing heights
  (n - 1).downto(0) do |i|
    bucket[i].each do |thresh, qidx|
      pos = -1
      l = 0
      r = stack.size - 1
      while l <= r
        m = (l + r) / 2
        if heights[stack[m]] > thresh
          pos = m
          l = m + 1
        else
          r = m - 1
        end
      end
      ans[qidx] = pos == -1 ? -1 : stack[pos]
    end

    while !stack.empty? && heights[stack[-1]] <= heights[i]
      stack.pop
    end
    stack << i
  end

  ans
end
```

## Scala

```scala
import java.util.Arrays
import scala.collection.mutable.ArrayBuffer

object Solution {
  def leftmostBuildingQueries(heights: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = heights.length
    val q = queries.length
    val ans = Array.fill(q)(-1)

    // pending queries grouped by y (right index)
    val pending = Array.fill(n)(new ArrayBuffer[(Int, Int)]())

    for (idx <- 0 until q) {
      var a = queries(idx)(0)
      var b = queries(idx)(1)
      if (a > b) { val tmp = a; a = b; b = tmp }
      if (a == b) {
        ans(idx) = a
      } else if (heights(a) < heights(b)) {
        ans(idx) = b
      } else {
        // need to find t > b with height > heights(a)
        pending(b).append((heights(a), idx))
      }
    }

    // coordinate compression of heights
    val uniq = heights.distinct.sorted
    val m = uniq.length
    val heightToIdx = new java.util.HashMap[Int, Int]()
    var i = 0
    while (i < m) {
      heightToIdx.put(uniq(i), i)
      i += 1
    }

    // segment tree for range minimum index
    var size = 1
    while (size < m) size <<= 1
    val seg = Array.fill(2 * size)(Int.MaxValue)

    def update(pos: Int, value: Int): Unit = {
      var p = pos + size
      if (value < seg(p)) {
        seg(p) = value
        p >>= 1
        while (p > 0) {
          val newVal = math.min(seg(p << 1), seg((p << 1) | 1))
          if (newVal == seg(p)) {
            // no change upwards
          } else {
            seg(p) = newVal
          }
          p >>= 1
        }
      }
    }

    def query(l: Int, r: Int): Int = {
      var left = l + size
      var right = r + size
      var res = Int.MaxValue
      while (left <= right) {
        if ((left & 1) == 1) {
          res = math.min(res, seg(left))
          left += 1
        }
        if ((right & 1) == 0) {
          res = math.min(res, seg(right))
          right -= 1
        }
        left >>= 1
        right >>= 1
      }
      res
    }

    // process from right to left
    var idxPos = n - 1
    while (idxPos >= 0) {
      val hIdx = heightToIdx.get(heights(idxPos))
      update(hIdx, idxPos)

      for ((thresholdHeight, qid) <- pending(idxPos)) {
        // find first compressed height > thresholdHeight
        var pos = Arrays.binarySearch(uniq, thresholdHeight)
        if (pos >= 0) pos += 1 else pos = -pos - 1
        if (pos >= m) {
          ans(qid) = -1
        } else {
          val resIdx = query(pos, m - 1)
          ans(qid) = if (resIdx == Int.MaxValue) -1 else resIdx
        }
      }

      idxPos -= 1
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn leftmost_building_queries(heights: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = heights.len();
        let q = queries.len();
        let mut ans = vec![-1i32; q];
        // group queries that need searching by their larger index y
        let mut by_y: Vec<Vec<(usize, i32, usize)>> = vec![Vec::new(); n];
        for (idx, query) in queries.iter().enumerate() {
            let mut a = query[0] as usize;
            let mut b = query[1] as usize;
            if a > b {
                std::mem::swap(&mut a, &mut b);
            }
            if a == b || heights[a] < heights[b] {
                ans[idx] = b as i32;
            } else {
                // need to find first t > b with height > heights[a]
                by_y[b].push((a, heights[a], idx));
            }
        }

        // monotonic stack: (height, index) with strictly increasing heights,
        // indices decreasing (since we process from right to left)
        let mut stack: Vec<(i32, usize)> = Vec::new();

        for i in (0..n).rev() {
            // answer queries whose y == i
            for &(x, hx, qid) in by_y[i].iter() {
                // binary search first element with height > hx
                let mut l = 0usize;
                let mut r = stack.len();
                while l < r {
                    let m = (l + r) / 2;
                    if stack[m].0 <= hx {
                        l = m + 1;
                    } else {
                        r = m;
                    }
                }
                if l < stack.len() {
                    ans[qid] = stack[l].1 as i32;
                }
            }

            // maintain monotonic decreasing heights in stack (pop <= current)
            while let Some(&(h, _)) = stack.last() {
                if h <= heights[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push((heights[i], i));
        }

        ans
    }
}
```

## Racket

```racket
(define (leftmost-building-queries heights queries)
  (define INF 1000000000) ; larger than any possible answer
  (define n (length heights))
  (define hv (list->vector heights))

  ;; segment tree for range minimum query of active indices
  (define size
    (let loop ((s 1))
      (if (>= s n) s (loop (* s 2)))))
  (define seg (make-vector (* 2 size) INF))

  (define (seg-update pos)
    (let ((i (+ pos size)))
      (vector-set! seg i pos)
      (let loop ((i (quotient i 2)))
        (when (> i 0)
          (vector-set! seg i
                       (min (vector-ref seg (* i 2))
                            (vector-ref seg (+ (* i 2) 1))))
          (loop (quotient i 2))))))

  (define (seg-query l r) ; inclusive range, returns INF if none
    (let ((l0 (+ l size))
          (r0 (+ r size)))
      (let loop ((l l0) (r r0) (res INF))
        (if (> l r)
            res
            (begin
              (when (odd? l)
                (set! res (min res (vector-ref seg l)))
                (set! l (+ l 1)))
              (when (even? r)
                (set! res (min res (vector-ref seg r)))
                (set! r (- r 1)))
              (loop (quotient l 2) (quotient r 2) res))))))

  ;; prepare sorted heights list: each element is (list height index)
  (define height-pairs
    (let loop ((i 0) (acc '()))
      (if (= i n)
          acc
          (loop (+ i 1) (cons (list (vector-ref hv i) i) acc)))))
  (define sorted-heights
    (sort height-pairs (lambda (a b) (> (first a) (first b))))) ; descending by height

  ;; process queries, separate easy ones and pending hard ones
  (define qlen (length queries))
  (define result (make-vector qlen -1))

  (define pending '())
  (let loop ((idx 0) (qs queries))
    (if (null? qs)
        (void)
        (let* ((pair (car qs))
               (a (first pair))
               (b (second pair)))
          (when (> a b) (let ((tmp a)) (set! a b) (set! b tmp))) ; ensure a <= b
          (cond
            [(= a b)
             (vector-set! result idx a)]
            [(< (vector-ref hv a) (vector-ref hv b))
             (vector-set! result idx b)]
            [else
             (set! pending (cons (list (vector-ref hv a) b idx) pending))])
          (loop (+ idx 1) (cdr qs)))))


  ;; sort pending queries by threshold descending
  (define sorted-pending
    (sort pending (lambda (x y) (> (first x) (first y)))))

  ;; offline processing
  (let loop ((p 0) (ph sorted-heights) (pq sorted-pending))
    (if (null? pq)
        (void)
        (let* ((thresh (first (car pq))) ; threshold = heights[a]
               (left   (second (car pq))) ; left = b
               (orig   (third (car pq))))
          ;; activate all positions with height > thresh
          (let inner ((ph ph) (p p))
            (if (or (null? ph)
                    (<= (first (car ph)) thresh))
                (begin
                  (set! ph ph) ; keep unchanged for next iteration
                  (set! p p))
                (begin
                  (seg-update (second (car ph)))
                  (inner (cdr ph) (+ p 1)))))
          ;; query range left+1 .. n-1
          (let ((ans
                 (if (= left (- n 1))
                     INF
                     (seg-query (+ left 1) (- n 1)))))
            (when (< ans INF)
              (vector-set! result orig ans)))
          (loop p ph (cdr pq))))))

  (vector->list result))
```

## Erlang

```erlang
-module(solution).
-export([leftmost_building_queries/2]).

-spec leftmost_building_queries(Heights :: [integer()], Queries :: [[integer()]]) -> [integer()].
leftmost_building_queries(Heights, Queries) ->
    N = length(Heights),
    HeightTuple = list_to_tuple([0 | Heights]),               % 1‑based indexing
    NGArray = build_next_greater(N, HeightTuple),
    Log = ceil_log2(N) + 1,
    UpList = build_up_arrays(N, Log, NGArray),
    [process_query(Q, HeightTuple, UpList) || Q <- Queries].

%% ---------- helpers ----------
ceil_log2(0) -> 0;
ceil_log2(N) ->
    ceil_log2(N, 0).

ceil_log2(N, Acc) when (1 bsl Acc) < N ->
    ceil_log2(N, Acc + 1);
ceil_log2(_, Acc) -> Acc.

%% build next greater array using a monotonic stack
build_next_greater(0, _HeightTuple) -> array:new(1, {default, -1});
build_next_greater(N, HeightTuple) ->
    NG0 = array:new(N + 1, {default, -1}),
    build_ng(N, HeightTuple, [], NG0).

build_ng(0, _HeightTuple, _Stack, NGArray) -> NGArray;
build_ng(I, HeightTuple, Stack, NGArray) ->
    Hi = element(HeightTuple, I),
    NewStack = pop_while(Stack, HeightTuple, Hi),
    NextIdx = case NewStack of
                  [] -> -1;
                  [H|_] -> H
              end,
    NGArray2 = array:set(I, NextIdx, NGArray),
    build_ng(I - 1, HeightTuple, [I | NewStack], NGArray2).

pop_while([], _HeightTuple, _Hi) -> [];
pop_while([Top|Rest], HeightTuple, Hi) ->
    Htop = element(HeightTuple, Top),
    if
        Htop =< Hi -> pop_while(Rest, HeightTuple, Hi);
        true -> [Top|Rest]
    end.

%% build binary lifting tables
build_up_arrays(_N, 0, UpList) -> lists:reverse(UpList);
build_up_arrays(N, Levels, [Prev|Rest]) ->
    NewLevel = array:new(N + 1, {default, -1}),
    Filled = fill_up_level(N, Prev, NewLevel),
    build_up_arrays(N, Levels - 1, [Filled, Prev | Rest]).

fill_up_level(0, _Prev, UpArray) -> UpArray;
fill_up_level(I, Prev, UpArray) when I > 0 ->
    Mid = array:get(I, Prev),
    Next = case Mid of
               -1 -> -1;
               _ -> array:get(Mid, Prev)
           end,
    UpArray2 = array:set(I, Next, UpArray),
    fill_up_level(I - 1, Prev, UpArray2).

%% process a single query
process_query([A0, B0], HeightTuple, UpList) ->
    {AIdx, BIdx} = if A0 =< B0 -> {A0, B0}; true -> {B0, A0} end,
    A = AIdx + 1,
    B = BIdx + 1,
    HA = element(HeightTuple, A),
    HB = element(HeightTuple, B),
    if
        AIdx == BIdx orelse HA < HB ->
            BIdx;                                   % meet at Bob's building
        true ->
            Threshold = HA,
            find_meeting(B, Threshold, UpList, HeightTuple)
    end.

find_meeting(Curr, Thresh, UpList, HeightTuple) ->
    MaxK = length(UpList) - 1,
    Curr2 = binary_lift(Curr, Thresh, UpList, HeightTuple, MaxK),
    Up0 = hd(UpList),                               % level 0 (next greater)
    NextIdx = array:get(Curr2, Up0),
    case NextIdx of
        -1 -> -1;
        _ -> NextIdx - 1                              % convert back to 0‑based index
    end.

binary_lift(Curr, _Thresh, _UpList, _HeightTuple, K) when K < 0 ->
    Curr;
binary_lift(Curr, Thresh, UpList, HeightTuple, K) ->
    UpK = lists:nth(K + 1, UpList),                 % list is 1‑based
    NextIdx = array:get(Curr, UpK),
    case NextIdx of
        -1 ->
            binary_lift(Curr, Thresh, UpList, HeightTuple, K - 1);
        _ ->
            Hnext = element(HeightTuple, NextIdx),
            if
                Hnext =< Thresh ->
                    binary_lift(NextIdx, Thresh, UpList, HeightTuple, K - 1);
                true ->
                    binary_lift(Curr, Thresh, UpList, HeightTuple, K - 1)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec leftmost_building_queries(heights :: [integer], queries :: [[integer]]) :: [integer]
  def leftmost_building_queries(heights, queries) do
    n = length(heights)
    heights_arr = :array.from_list(heights)

    seg_tree = build_seg(0, n - 1, 1, heights_arr, %{})

    Enum.map(queries, fn [a, b] ->
      {x, y} = if a <= b, do: {a, b}, else: {b, a}
      cond do
        x == y ->
          y

        :array.get(x, heights_arr) < :array.get(y, heights_arr) ->
          y

        true ->
          thresh = :array.get(x, heights_arr)

          if y + 1 > n - 1 do
            -1
          else
            case query_leftmost(0, n - 1, 1, y + 1, n - 1, thresh, seg_tree) do
              nil -> -1
              idx -> idx
            end
          end
      end
    end)
  end

  # Build segment tree storing maximum height in each node.
  defp build_seg(l, r, idx, heights_arr, map) when l == r do
    val = :array.get(l, heights_arr)
    Map.put(map, idx, val)
  end

  defp build_seg(l, r, idx, heights_arr, map) do
    mid = div(l + r, 2)

    map1 = build_seg(l, mid, idx * 2, heights_arr, map)
    map2 = build_seg(mid + 1, r, idx * 2 + 1, heights_arr, map1)

    left_max = Map.get(map2, idx * 2)
    right_max = Map.get(map2, idx * 2 + 1)
    max_val = if left_max > right_max, do: left_max, else: right_max

    Map.put(map2, idx, max_val)
  end

  # Query for the leftmost index in [ql, qr] with height > thresh.
  defp query_leftmost(l, r, idx, ql, qr, thresh, map) do
    cond do
      ql > r or qr < l ->
        nil

      Map.get(map, idx) <= thresh ->
        nil

      l == r ->
        l

      true ->
        mid = div(l + r, 2)

        left_res = query_leftmost(l, mid, idx * 2, ql, qr, thresh, map)

        if left_res != nil do
          left_res
        else
          query_leftmost(mid + 1, r, idx * 2 + 1, ql, qr, thresh, map)
        end
    end
  end
end
```
