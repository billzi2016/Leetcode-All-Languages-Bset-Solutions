# 1707. Maximum XOR With an Element From Array

## Cpp

```cpp
class Solution {
public:
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        const int MAX_BIT = 30; // since nums[i], xi <= 1e9 < 2^30
        struct Node { int child[2]; Node(){ child[0] = child[1] = -1; } };
        vector<Node> trie(1); // root at index 0
        
        auto insert = [&](int val) {
            int node = 0;
            for (int k = MAX_BIT; k >= 0; --k) {
                int b = (val >> k) & 1;
                if (trie[node].child[b] == -1) {
                    trie[node].child[b] = trie.size();
                    trie.emplace_back();
                }
                node = trie[node].child[b];
            }
        };
        
        auto queryMaxXor = [&](int x) -> int {
            int node = 0;
            int res = 0;
            for (int k = MAX_BIT; k >= 0; --k) {
                int b = (x >> k) & 1;
                int want = 1 - b;
                if (trie[node].child[want] != -1) {
                    res |= (1 << k);
                    node = trie[node].child[want];
                } else {
                    node = trie[node].child[b];
                }
            }
            return res;
        };
        
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        struct Q { int m, x, idx; };
        vector<Q> qs;
        qs.reserve(queries.size());
        for (int i = 0; i < (int)queries.size(); ++i) {
            qs.push_back({queries[i][1], queries[i][0], i});
        }
        sort(qs.begin(), qs.end(), [](const Q& a, const Q& b){ return a.m < b.m; });
        
        vector<int> ans(queries.size());
        int ptr = 0;
        for (const auto& q : qs) {
            while (ptr < n && nums[ptr] <= q.m) {
                insert(nums[ptr]);
                ++ptr;
            }
            if (ptr == 0) { // no numbers inserted yet
                ans[q.idx] = -1;
            } else {
                ans[q.idx] = queryMaxXor(q.x);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Query {
        int x, m, idx;
        Query(int x, int m, int idx) {
            this.x = x;
            this.m = m;
            this.idx = idx;
        }
    }

    private static class Trie {
        int[][] child;
        int nodeCnt;

        Trie(int maxNodes) {
            child = new int[maxNodes][2];
            for (int i = 0; i < maxNodes; i++) {
                child[i][0] = -1;
                child[i][1] = -1;
            }
            nodeCnt = 1; // root at 0
        }

        void insert(int num) {
            int node = 0;
            for (int k = 31; k >= 0; k--) {
                int bit = (num >>> k) & 1;
                if (child[node][bit] == -1) {
                    child[node][bit] = nodeCnt++;
                }
                node = child[node][bit];
            }
        }

        int maxXor(int num) {
            int node = 0;
            int res = 0;
            for (int k = 31; k >= 0; k--) {
                int bit = (num >>> k) & 1;
                int want = bit ^ 1;
                if (child[node][want] != -1) {
                    res |= (1 << k);
                    node = child[node][want];
                } else {
                    node = child[node][bit];
                }
            }
            return res;
        }

        boolean isEmpty() {
            return child[0][0] == -1 && child[0][1] == -1;
        }
    }

    public int[] maximizeXor(int[] nums, int[][] queries) {
        int n = nums.length;
        int q = queries.length;

        java.util.Arrays.sort(nums);

        Query[] qs = new Query[q];
        for (int i = 0; i < q; i++) {
            qs[i] = new Query(queries[i][0], queries[i][1], i);
        }
        java.util.Arrays.sort(qs, (a, b) -> Integer.compare(a.m, b.m));

        int maxNodes = (n + 1) * 32;
        Trie trie = new Trie(maxNodes);

        int[] ans = new int[q];
        int ptr = 0;
        for (Query qu : qs) {
            while (ptr < n && nums[ptr] <= qu.m) {
                trie.insert(nums[ptr]);
                ptr++;
            }
            if (trie.isEmpty()) {
                ans[qu.idx] = -1;
            } else {
                ans[qu.idx] = trie.maxXor(qu.x);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums.sort()
        # augment queries with original index and sort by mi
        q = [(mi, xi, i) for i, (xi, mi) in enumerate(queries)]
        q.sort()
        
        trie = [[-1, -1]]  # each node: [child0, child1]
        
        def insert(val):
            node = 0
            for k in range(30, -1, -1):
                b = (val >> k) & 1
                if trie[node][b] == -1:
                    trie[node][b] = len(trie)
                    trie.append([-1, -1])
                node = trie[node][b]
        
        def max_xor(val):
            # assumes at least one number has been inserted
            node = 0
            ans = 0
            for k in range(30, -1, -1):
                b = (val >> k) & 1
                want = 1 - b
                if trie[node][want] != -1:
                    ans |= (1 << k)
                    node = trie[node][want]
                else:
                    node = trie[node][b]
            return ans
        
        res = [0] * len(queries)
        idx = 0
        n = len(nums)
        
        for mi, xi, i in q:
            while idx < n and nums[idx] <= mi:
                insert(nums[idx])
                idx += 1
            if idx == 0:   # no eligible numbers
                res[i] = -1
            else:
                res[i] = max_xor(xi)
        return res
```

## Python3

```python
from typing import List

class Trie:
    def __init__(self):
        self.children = [[-1, -1]]  # root node
        self.size = 0  # number of inserted numbers

    def insert(self, num: int) -> None:
        node = 0
        for k in range(31, -1, -1):
            bit = (num >> k) & 1
            nxt = self.children[node][bit]
            if nxt == -1:
                self.children.append([-1, -1])
                nxt = len(self.children) - 1
                self.children[node][bit] = nxt
            node = nxt
        self.size += 1

    def max_xor(self, num: int) -> int:
        node = 0
        res = 0
        for k in range(31, -1, -1):
            bit = (num >> k) & 1
            toggled = 1 - bit
            if self.children[node][toggled] != -1:
                res |= (1 << k)
                node = self.children[node][toggled]
            else:
                node = self.children[node][bit]
        return res

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        # augment queries with original index
        q_with_idx = [(x, m, i) for i, (x, m) in enumerate(queries)]
        q_with_idx.sort(key=lambda x: x[1])  # sort by mi

        trie = Trie()
        ans = [-1] * len(queries)
        n_ptr = 0
        n_len = len(nums)

        for xi, mi, idx in q_with_idx:
            while n_ptr < n_len and nums[n_ptr] <= mi:
                trie.insert(nums[n_ptr])
                n_ptr += 1
            if trie.size == 0:
                ans[idx] = -1
            else:
                ans[idx] = trie.max_xor(xi)
        return ans
```

## C

```c
#include <stdlib.h>

#define MAX_BITS 31  // enough for numbers up to 2^30

typedef struct {
    int child[2];
} TrieNode;

static int cmpInt(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

typedef struct {
    int x;
    int m;
    int idx;
} Query;

static int cmpQuery(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    return (qa->m > qb->m) - (qa->m < qb->m);
}

static void trieInsert(int num, TrieNode *nodes, int *nodeCnt) {
    int cur = 0;
    for (int i = MAX_BITS - 1; i >= 0; --i) {
        int bit = (num >> i) & 1;
        if (nodes[cur].child[bit] == -1) {
            nodes[*nodeCnt].child[0] = nodes[*nodeCnt].child[1] = -1;
            nodes[cur].child[bit] = (*nodeCnt)++;
        }
        cur = nodes[cur].child[bit];
    }
}

static int trieMaxXor(int num, TrieNode *nodes) {
    int cur = 0;
    int ans = 0;
    for (int i = MAX_BITS - 1; i >= 0; --i) {
        int bit = (num >> i) & 1;
        int want = bit ^ 1;
        if (nodes[cur].child[want] != -1) {
            ans |= (1 << i);
            cur = nodes[cur].child[want];
        } else {
            cur = nodes[cur].child[bit];
        }
    }
    return ans;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximizeXor(int* nums, int numsSize, int** queries, int queriesSize,
                 int* queriesColSize, int* returnSize) {
    // Sort nums
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);

    // Prepare query structures
    Query *qs = (Query *)malloc(sizeof(Query) * (size_t)queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        qs[i].x = queries[i][0];
        qs[i].m = queries[i][1];
        qs[i].idx = i;
    }
    qsort(qs, (size_t)queriesSize, sizeof(Query), cmpQuery);

    // Allocate trie nodes
    int maxNodes = (numsSize + 1) * MAX_BITS + 5;
    TrieNode *nodes = (TrieNode *)malloc(sizeof(TrieNode) * (size_t)maxNodes);
    for (int i = 0; i < maxNodes; ++i) {
        nodes[i].child[0] = nodes[i].child[1] = -1;
    }
    int nodeCnt = 1; // root at index 0

    int *answers = (int *)malloc(sizeof(int) * (size_t)queriesSize);
    int nIdx = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int limit = qs[i].m;
        while (nIdx < numsSize && nums[nIdx] <= limit) {
            trieInsert(nums[nIdx], nodes, &nodeCnt);
            ++nIdx;
        }
        if (nodes[0].child[0] == -1 && nodes[0].child[1] == -1) {
            answers[qs[i].idx] = -1;
        } else {
            answers[qs[i].idx] = trieMaxXor(qs[i].x, nodes);
        }
    }

    free(nodes);
    free(qs);

    *returnSize = queriesSize;
    return answers;
}
```

## Csharp

```csharp
public class Solution {
    private const int HIGH_BIT = 30;
    private class TrieNode {
        public TrieNode[] child = new TrieNode[2];
    }
    private void Insert(TrieNode root, int num) {
        var node = root;
        for (int k = HIGH_BIT; k >= 0; --k) {
            int bit = (num >> k) & 1;
            if (node.child[bit] == null) node.child[bit] = new TrieNode();
            node = node.child[bit];
        }
    }
    private int MaxXor(TrieNode root, int num) {
        var node = root;
        int ans = 0;
        for (int k = HIGH_BIT; k >= 0; --k) {
            int bit = (num >> k) & 1;
            int toggled = bit ^ 1;
            if (node.child[toggled] != null) {
                ans |= (1 << k);
                node = node.child[toggled];
            } else {
                node = node.child[bit];
            }
        }
        return ans;
    }

    public int[] MaximizeXor(int[] nums, int[][] queries) {
        Array.Sort(nums);
        int q = queries.Length;
        var qs = new (int x, int m, int idx)[q];
        for (int i = 0; i < q; ++i) {
            qs[i] = (queries[i][0], queries[i][1], i);
        }
        Array.Sort(qs, (a, b) => a.m.CompareTo(b.m));
        var res = new int[q];
        var root = new TrieNode();
        int nIdx = 0;
        foreach (var (x, m, idx) in qs) {
            while (nIdx < nums.Length && nums[nIdx] <= m) {
                Insert(root, nums[nIdx]);
                ++nIdx;
            }
            if (root.child[0] == null && root.child[1] == null) {
                res[idx] = -1;
            } else {
                res[idx] = MaxXor(root, x);
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var maximizeXor = function(nums, queries) {
    nums.sort((a, b) => a - b);
    const m = queries.length;
    const qWithIdx = queries.map((q, i) => [q[0], q[1], i]);
    qWithIdx.sort((a, b) => a[1] - b[1]); // sort by mi

    const res = new Array(m);
    let nIdx = 0;

    const root = { ch: [null, null] };

    function insert(num) {
        let node = root;
        for (let k = 30; k >= 0; --k) {
            const bit = (num >> k) & 1;
            if (!node.ch[bit]) node.ch[bit] = { ch: [null, null] };
            node = node.ch[bit];
        }
    }

    function queryMaxXor(x) {
        // empty trie check
        if (!root.ch[0] && !root.ch[1]) return -1;
        let node = root;
        let ans = 0;
        for (let k = 30; k >= 0; --k) {
            const bit = (x >> k) & 1;
            const want = bit ^ 1;
            if (node.ch[want]) {
                ans |= (1 << k);
                node = node.ch[want];
            } else {
                node = node.ch[bit];
            }
        }
        return ans;
    }

    for (const [xi, mi, idx] of qWithIdx) {
        while (nIdx < nums.length && nums[nIdx] <= mi) {
            insert(nums[nIdx]);
            nIdx++;
        }
        res[idx] = queryMaxXor(xi);
    }

    return res;
};
```

## Typescript

```typescript
function maximizeXor(nums: number[], queries: number[][]): number[] {
    const sortedNums = nums.slice().sort((a, b) => a - b);
    const qWithIdx = queries.map((q, i) => [q[0], q[1], i] as [number, number, number]);
    qWithIdx.sort((a, b) => a[1] - b[1]); // sort by mi

    const trie: number[][] = [[-1, -1]]; // root node

    function insert(val: number): void {
        let node = 0;
        for (let k = 30; k >= 0; --k) {
            const bit = (val >> k) & 1;
            if (trie[node][bit] === -1) {
                trie[node][bit] = trie.length;
                trie.push([-1, -1]);
            }
            node = trie[node][bit];
        }
    }

    function query(val: number): number {
        let node = 0;
        let ans = 0;
        for (let k = 30; k >= 0; --k) {
            const bit = (val >> k) & 1;
            const toggled = bit ^ 1;
            if (trie[node][toggled] !== -1) {
                ans |= (1 << k);
                node = trie[node][toggled];
            } else {
                node = trie[node][bit];
            }
        }
        return ans;
    }

    const res: number[] = new Array(queries.length).fill(-1);
    let idxNum = 0;

    for (const [xi, mi, origIdx] of qWithIdx) {
        while (idxNum < sortedNums.length && sortedNums[idxNum] <= mi) {
            insert(sortedNums[idxNum]);
            ++idxNum;
        }
        if (idxNum === 0) {
            res[origIdx] = -1;
        } else {
            res[origIdx] = query(xi);
        }
    }

    return res;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maximizeXor($nums, $queries) {
        sort($nums);
        $qCount = count($queries);
        $queriesWithIdx = [];
        foreach ($queries as $idx => $q) {
            $queriesWithIdx[] = [$q[0], $q[1], $idx];
        }
        usort($queriesWithIdx, function($a, $b) {
            if ($a[1] == $b[1]) return 0;
            return ($a[1] < $b[1]) ? -1 : 1;
        });
        $answers = array_fill(0, $qCount, 0);
        // Trie initialization
        $trie = [[-1, -1]];
        $ptr = 0;
        $n = count($nums);
        foreach ($queriesWithIdx as $item) {
            [$x, $m, $origIdx] = $item;
            while ($ptr < $n && $nums[$ptr] <= $m) {
                $num = $nums[$ptr];
                $node = 0;
                for ($i = 30; $i >= 0; $i--) {
                    $b = ($num >> $i) & 1;
                    if ($trie[$node][$b] == -1) {
                        $trie[] = [-1, -1];
                        $trie[$node][$b] = count($trie) - 1;
                    }
                    $node = $trie[$node][$b];
                }
                $ptr++;
            }
            // query
            if ($trie[0][0] == -1 && $trie[0][1] == -1) {
                $answers[$origIdx] = -1;
                continue;
            }
            $node = 0;
            $res = 0;
            for ($i = 30; $i >= 0; $i--) {
                $b = ($x >> $i) & 1;
                $desired = 1 - $b;
                if ($trie[$node][$desired] != -1) {
                    $res |= (1 << $i);
                    $node = $trie[$node][$desired];
                } else {
                    $node = $trie[$node][$b];
                }
            }
            $answers[$origIdx] = $res;
        }
        return $answers;
    }
}
```

## Swift

```swift
class TrieNode {
    var child: [TrieNode?] = [nil, nil]
}

class Solution {
    func maximizeXor(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let sortedNums = nums.sorted()
        var queryInfos: [(x: Int, m: Int, idx: Int)] = []
        for (i, q) in queries.enumerated() {
            queryInfos.append((x: q[0], m: q[1], idx: i))
        }
        queryInfos.sort { $0.m < $1.m }
        
        let root = TrieNode()
        var result = Array(repeating: 0, count: queries.count)
        var nIdx = 0
        let nCount = sortedNums.count
        
        func insert(_ num: Int) {
            var node = root
            for k in stride(from: 30, through: 0, by: -1) {
                let bit = (num >> k) & 1
                if node.child[bit] == nil {
                    node.child[bit] = TrieNode()
                }
                node = node.child[bit]!
            }
        }
        
        func getMaxXor(_ num: Int) -> Int {
            var node = root
            var ans = 0
            for k in stride(from: 30, through: 0, by: -1) {
                let bit = (num >> k) & 1
                let toggled = bit ^ 1
                if let next = node.child[toggled] {
                    ans |= (1 << k)
                    node = next
                } else if let same = node.child[bit] {
                    node = same
                } else {
                    break
                }
            }
            return ans
        }
        
        func isEmpty() -> Bool {
            return root.child[0] == nil && root.child[1] == nil
        }
        
        for q in queryInfos {
            while nIdx < nCount && sortedNums[nIdx] <= q.m {
                insert(sortedNums[nIdx])
                nIdx += 1
            }
            if isEmpty() {
                result[q.idx] = -1
            } else {
                result[q.idx] = getMaxXor(q.x)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeXor(nums: IntArray, queries: Array<IntArray>): IntArray {
        val sortedNums = nums.clone()
        java.util.Arrays.sort(sortedNums)
        data class Q(val x: Int, val m: Int, val idx: Int)
        val qList = ArrayList<Q>(queries.size)
        for (i in queries.indices) {
            qList.add(Q(queries[i][0], queries[i][1], i))
        }
        qList.sortWith(compareBy<Q> { it.m })
        // Trie implementation
        val child = ArrayList<IntArray>()
        fun newNode(): Int {
            child.add(intArrayOf(-1, -1))
            return child.size - 1
        }
        newNode() // root at index 0
        var hasElements = false
        fun insert(num: Int) {
            var node = 0
            for (bit in 30 downTo 0) {
                val b = (num shr bit) and 1
                if (child[node][b] == -1) {
                    child[node][b] = newNode()
                }
                node = child[node][b]
            }
        }
        fun maxXor(x: Int): Int {
            var node = 0
            var ans = 0
            for (bit in 30 downTo 0) {
                val b = (x shr bit) and 1
                val toggled = b xor 1
                if (child[node][toggled] != -1) {
                    ans = ans or (1 shl bit)
                    node = child[node][toggled]
                } else if (child[node][b] != -1) {
                    node = child[node][b]
                } else {
                    break
                }
            }
            return ans
        }
        val res = IntArray(queries.size)
        var iNum = 0
        for (q in qList) {
            while (iNum < sortedNums.size && sortedNums[iNum] <= q.m) {
                insert(sortedNums[iNum])
                hasElements = true
                iNum++
            }
            res[q.idx] = if (!hasElements) -1 else maxXor(q.x)
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> maximizeXor(List<int> nums, List<List<int>> queries) {
    // Sort the numbers
    List<int> sortedNums = List.from(nums);
    sortedNums.sort();
    int n = sortedNums.length;

    // Prepare query objects with original indices
    List<_Query> qs = [];
    for (int i = 0; i < queries.length; i++) {
      qs.add(_Query(queries[i][0], queries[i][1], i));
    }
    qs.sort((a, b) => a.m.compareTo(b.m));

    // Result array
    List<int> ans = List.filled(queries.length, -1);

    // Trie for numbers <= current m
    _Trie trie = _Trie();
    int idx = 0;

    for (var q in qs) {
      while (idx < n && sortedNums[idx] <= q.m) {
        trie.insert(sortedNums[idx]);
        idx++;
      }
      if (trie.count > 0) {
        ans[q.idx] = trie.maxXor(q.x);
      } else {
        ans[q.idx] = -1;
      }
    }

    return ans;
  }
}

class _Query {
  int x;
  int m;
  int idx;
  _Query(this.x, this.m, this.idx);
}

class _Trie {
  // Each node stores two child indices: [0] for bit 0, [1] for bit 1
  final List<List<int>> _nodes = [
    [-1, -1]
  ];
  int _cnt = 0; // number of inserted values

  void insert(int num) {
    int node = 0;
    for (int k = 30; k >= 0; --k) {
      int bit = (num >> k) & 1;
      if (_nodes[node][bit] == -1) {
        _nodes.add([-1, -1]);
        _nodes[node][bit] = _nodes.length - 1;
      }
      node = _nodes[node][bit];
    }
    _cnt++;
  }

  int maxXor(int num) {
    int node = 0;
    int xor = 0;
    for (int k = 30; k >= 0; --k) {
      int bit = (num >> k) & 1;
      int toggled = bit ^ 1;
      if (_nodes[node][toggled] != -1) {
        xor |= (1 << k);
        node = _nodes[node][toggled];
      } else {
        node = _nodes[node][bit];
      }
    }
    return xor;
  }

  int get count => _cnt;
}
```

## Golang

```go
package main

import (
	"sort"
)

type trieNode struct {
	child [2]*trieNode
}

func insert(root *trieNode, num int) {
	node := root
	for i := 30; i >= 0; i-- {
		bit := (num >> i) & 1
		if node.child[bit] == nil {
			node.child[bit] = &trieNode{}
		}
		node = node.child[bit]
	}
}

func maxXor(root *trieNode, x int) int {
	node := root
	ans := 0
	for i := 30; i >= 0; i-- {
		bit := (x >> i) & 1
		want := bit ^ 1 // opposite bit for maximizing xor
		if node.child[want] != nil {
			ans |= 1 << i
			node = node.child[want]
		} else {
			node = node.child[bit]
		}
	}
	return ans
}

type query struct {
	x   int
	m   int
	idx int
}

func maximizeXor(nums []int, queries [][]int) []int {
	sort.Ints(nums)

	qList := make([]query, len(queries))
	for i, q := range queries {
		qList[i] = query{x: q[0], m: q[1], idx: i}
	}
	sort.Slice(qList, func(i, j int) bool { return qList[i].m < qList[j].m })

	ans := make([]int, len(queries))
	root := &trieNode{}
	nIdx := 0
	inserted := false

	for _, qu := range qList {
		for nIdx < len(nums) && nums[nIdx] <= qu.m {
			insert(root, nums[nIdx])
			nIdx++
			inserted = true
		}
		if !inserted {
			ans[qu.idx] = -1
		} else {
			ans[qu.idx] = maxXor(root, qu.x)
		}
	}
	return ans
}
```

## Ruby

```ruby
class Trie
  def initialize
    @nodes = [[-1, -1]] # each node stores indices of children [0-bit, 1-bit]
  end

  def insert(num)
    node = 0
    30.downto(0) do |k|
      bit = (num >> k) & 1
      child = @nodes[node][bit]
      if child == -1
        @nodes << [-1, -1]
        child = @nodes.size - 1
        @nodes[node][bit] = child
      end
      node = child
    end
  end

  def max_xor(num)
    node = 0
    xor_val = 0
    30.downto(0) do |k|
      bit = (num >> k) & 1
      toggled = bit ^ 1
      if @nodes[node][toggled] != -1
        xor_val |= (1 << k)
        node = @nodes[node][toggled]
      else
        node = @nodes[node][bit]
      end
    end
    xor_val
  end

  def empty?
    @nodes.size == 1 && @nodes[0] == [-1, -1]
  end
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximize_xor(nums, queries)
  sorted_nums = nums.sort
  # each query: [mi, xi, original_index]
  q_with_idx = queries.each_with_index.map { |(xi, mi), i| [mi, xi, i] }
  q_with_idx.sort_by! { |arr| arr[0] }

  trie = Trie.new
  ans = Array.new(queries.length)
  n_ptr = 0
  n_len = sorted_nums.length

  q_with_idx.each do |mi, xi, idx|
    while n_ptr < n_len && sorted_nums[n_ptr] <= mi
      trie.insert(sorted_nums[n_ptr])
      n_ptr += 1
    end
    if n_ptr == 0
      ans[idx] = -1
    else
      ans[idx] = trie.max_xor(xi)
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximizeXor(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        val sortedNums = nums.sorted
        case class Q(x: Int, m: Int, idx: Int)
        val qs = queries.zipWithIndex.map { case (arr, i) => Q(arr(0), arr(1), i) }.sortBy(_.m)

        class TrieNode {
            var child: Array[TrieNode] = new Array[TrieNode](2)
        }
        val root = new TrieNode()
        var insertedCount = 0

        def insert(num: Int): Unit = {
            var node = root
            for (k <- 30 to 0 by -1) {
                val bit = (num >> k) & 1
                if (node.child(bit) == null) node.child(bit) = new TrieNode()
                node = node.child(bit)
            }
        }

        def query(x: Int): Int = {
            var node = root
            var ans = 0
            for (k <- 30 to 0 by -1) {
                val bit = (x >> k) & 1
                val toggled = bit ^ 1
                if (node.child(toggled) != null) {
                    ans |= (1 << k)
                    node = node.child(toggled)
                } else {
                    node = node.child(bit)
                }
            }
            ans
        }

        val res = new Array[Int](queries.length)
        var i = 0
        for (q <- qs) {
            while (i < sortedNums.length && sortedNums(i) <= q.m) {
                insert(sortedNums(i))
                insertedCount += 1
                i += 1
            }
            if (insertedCount == 0) res(q.idx) = -1
            else res(q.idx) = query(q.x)
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_xor(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        // Sort numbers
        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();

        // Prepare queries with original indices
        let mut q_with_idx: Vec<(i32, i32, usize)> = queries
            .iter()
            .enumerate()
            .map(|(i, v)| (v[0], v[1], i))
            .collect();
        q_with_idx.sort_unstable_by_key(|k| k.1); // sort by mi

        // Trie structure
        struct Trie {
            nodes: Vec<[i32; 2]>, // children indices, -1 means none
        }
        impl Trie {
            fn new() -> Self {
                Self { nodes: vec![[ -1, -1 ]] } // root at index 0
            }
            fn insert(&mut self, num: i32) {
                let mut node = 0usize;
                for k in (0..=31).rev() {
                    let bit = ((num >> k) & 1) as usize;
                    if self.nodes[node][bit] == -1 {
                        self.nodes.push([ -1, -1 ]);
                        let new_idx = (self.nodes.len() - 1) as i32;
                        self.nodes[node][bit] = new_idx;
                    }
                    node = self.nodes[node][bit] as usize;
                }
            }
            fn max_xor(&self, num: i32) -> i32 {
                if self.nodes.len() == 1 {
                    return -1; // empty trie
                }
                let mut node = 0usize;
                let mut ans = 0i32;
                for k in (0..=31).rev() {
                    let bit = ((num >> k) & 1) as usize;
                    let toggled = 1 - bit;
                    if self.nodes[node][toggled] != -1 {
                        ans |= 1 << k;
                        node = self.nodes[node][toggled] as usize;
                    } else {
                        node = self.nodes[node][bit] as usize;
                    }
                }
                ans
            }
        }

        let mut trie = Trie::new();
        let mut res = vec![-1; queries.len()];
        let mut idx_num = 0usize;

        for (x, m, orig_idx) in q_with_idx {
            while idx_num < sorted_nums.len() && sorted_nums[idx_num] <= m {
                trie.insert(sorted_nums[idx_num]);
                idx_num += 1;
            }
            if trie.nodes.len() > 1 {
                res[orig_idx] = trie.max_xor(x);
            } else {
                res[orig_idx] = -1;
            }
        }

        res
    }
}
```

## Racket

```racket
#lang racket

(define/contract (maximize-xor nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  ;; helper: insert a number into binary trie
  (define (insert root num)
    (let loop ((node root) (bit 30))
      (when (>= bit 0)
        (define b (if (zero? (bitwise-and num (arithmetic-shift 1 bit))) 0 1))
        (define child (vector-ref node b))
        (unless child
          (set! child (make-vector 2 #f))
          (vector-set! node b child))
        (loop child (sub1 bit)))))
  ;; helper: query max xor with x given current trie (assumes at least one number inserted)
  (define (max-xor root x)
    (let loop ((node root) (bit 30) (res 0))
      (if (< bit 0)
          res
          (let* ((b (if (zero? (bitwise-and x (arithmetic-shift 1 bit))) 0 1))
                 (desired (if (= b 0) 1 0))
                 (next (vector-ref node desired)))
            (if next
                (loop next (sub1 bit) (bitwise-ior res (arithmetic-shift 1 bit)))
                (let ((alt (vector-ref node b)))
                  (if alt
                      (loop alt (sub1 bit) res)
                      res)))))))
  ;; sort nums
  (define sorted-nums (list->vector (sort nums <)))
  (define nlen (vector-length sorted-nums))
  ;; index queries and sort by mi
  (define indexed-queries
    (let loop ((qs queries) (i 0) (acc '()))
      (if (null? qs)
          acc
          (loop (cdr qs) (add1 i)
                (cons (list (first (car qs)) (second (car qs)) i) acc)))))
  (define sorted-queries (sort indexed-queries (lambda (a b) (< (second a) (second b)))))
  ;; prepare structures
  (define root (make-vector 2 #f))
  (define ans (make-vector (length queries) -1))
  (define inserted-count 0)
  (define num-pos 0)
  ;; process each query in order of mi
  (for ([q sorted-queries])
    (define xi (first q))
    (define mi (second q))
    (define idx (third q))
    ;; insert all nums <= mi
    (let loop ((pos num-pos))
      (if (and (< pos nlen) (<= (vector-ref sorted-nums pos) mi))
          (begin
            (insert root (vector-ref sorted-nums pos))
            (set! inserted-count (+ inserted-count 1))
            (loop (add1 pos)))
          (set! num-pos pos)))
    ;; answer query
    (if (> inserted-count 0)
        (vector-set! ans idx (max-xor root xi))
        (vector-set! ans idx -1)))
  (vector->list ans))
```

## Erlang

```erlang
-module(solution).
-export([maximize_xor/2]).

-spec maximize_xor(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
maximize_xor(Nums, Queries) ->
    SortedNums = lists:sort(Nums),
    QWithIdx = prepare_queries(Queries, 0, []),
    SortedQueries = lists:keysort(1, QWithIdx),
    % Initialize empty trie with root id 0
    EmptyTrie = #{0 => {-1, -1}},
    {AnsPairs, _} = process_queries(SortedQueries, SortedNums, EmptyTrie, 1, []),
    SortedAns = [Ans || {_Idx, Ans} <- lists:keysort(1, AnsPairs)],
    SortedAns.

prepare_queries([], _Idx, Acc) ->
    lists:reverse(Acc);
prepare_queries([[Xi, Mi] | Rest], Idx, Acc) ->
    prepare_queries(Rest, Idx + 1, [{Mi, Xi, Idx} | Acc]).

process_queries([], NumList, Trie, NextId, Answers) ->
    {Answers, {NumList, Trie, NextId}};
process_queries([{Mi, Xi, Idx} | RestQ], NumList, Trie, NextId, Answers) ->
    {NewNumList, NewTrie, NewNextId} = insert_until(NumList, Mi, Trie, NextId),
    RootNode = maps:get(0, NewTrie),
    Answer =
        case element(1, RootNode) of
            -1 when element(2, RootNode) =:= -1 -> -1;
            _ -> max_xor_query(NewTrie, Xi)
        end,
    process_queries(RestQ, NewNumList, NewTrie, NewNextId, [{Idx, Answer} | Answers]).

insert_until([], _Mi, Trie, NextId) ->
    {[], Trie, NextId};
insert_until([N | Rest] = NumList, Mi, Trie, NextId) when N =< Mi ->
    {TmpTrie, TmpNextId} = insert_num({Trie, NextId}, N, 30),
    insert_until(Rest, Mi, TmpTrie, TmpNextId);
insert_until(NumList, _Mi, Trie, NextId) ->
    {NumList, Trie, NextId}.

%% Insert a number into the trie
insert_num({TrieMap, NextId}, Num, MaxBit) ->
    insert_loop(0, TrieMap, NextId, Num, MaxBit).

insert_loop(_CurId, TrieMap, NextId, _Num, BitIdx) when BitIdx < 0 ->
    {TrieMap, NextId};
insert_loop(CurId, TrieMap, NextId, Num, BitIdx) ->
    Bit = (Num bsr BitIdx) band 1,
    CurNode = maps:get(CurId, TrieMap),
    case Bit of
        0 ->
            ChildId = element(1, CurNode),
            {TrieMap2, NextId2, NewChild} =
                if ChildId == -1 ->
                        NewNode = {-1, -1},
                        TmpTrie = maps:put(NextId, NewNode, TrieMap),
                        UpdatedCur = setelement(1, CurNode, NextId),
                        {maps:put(CurId, UpdatedCur, TmpTrie), NextId + 1, NextId};
                   true ->
                        {TrieMap, NextId, ChildId}
                end,
            insert_loop(NewChild, TrieMap2, NextId2, Num, BitIdx - 1);
        1 ->
            ChildId = element(2, CurNode),
            {TrieMap2, NextId2, NewChild} =
                if ChildId == -1 ->
                        NewNode = {-1, -1},
                        TmpTrie = maps:put(NextId, NewNode, TrieMap),
                        UpdatedCur = setelement(2, CurNode, NextId),
                        {maps:put(CurId, UpdatedCur, TmpTrie), NextId + 1, NextId};
                   true ->
                        {TrieMap, NextId, ChildId}
                end,
            insert_loop(NewChild, TrieMap2, NextId2, Num, BitIdx - 1)
    end.

%% Query maximum xor with Xi
max_xor_query(TrieMap, Xi) ->
    query_loop(0, TrieMap, Xi, 30, 0).

query_loop(_CurId, _TrieMap, _Xi, BitIdx, Acc) when BitIdx < 0 ->
    Acc;
query_loop(CurId, TrieMap, Xi, BitIdx, Acc) ->
    Bit = (Xi bsr BitIdx) band 1,
    CurNode = maps:get(CurId, TrieMap),
    DesiredOpp = 1 - Bit,
    case DesiredOpp of
        0 ->
            OppChild = element(1, CurNode),
            if OppChild =/= -1 ->
                    NewAcc = Acc bor (1 bsl BitIdx),
                    query_loop(OppChild, TrieMap, Xi, BitIdx - 1, NewAcc);
               true ->
                    SameChild = element(2, CurNode),
                    query_loop(SameChild, TrieMap, Xi, BitIdx - 1, Acc)
            end;
        1 ->
            OppChild = element(2, CurNode),
            if OppChild =/= -1 ->
                    NewAcc = Acc bor (1 bsl BitIdx),
                    query_loop(OppChild, TrieMap, Xi, BitIdx - 1, NewAcc);
               true ->
                    SameChild = element(1, CurNode),
                    query_loop(SameChild, TrieMap, Xi, BitIdx - 1, Acc)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec maximize_xor(nums :: [integer], queries :: [[integer]]) :: [integer]
  def maximize_xor(nums, queries) do
    sorted_nums = Enum.sort(nums)

    indexed_queries =
      queries
      |> Enum.with_index()
      |> Enum.map(fn {[x, m], idx} -> %{x: x, m: m, idx: idx} end)
      |> Enum.sort_by(& &1.m)

    {answers_map, _remaining, _trie} =
      Enum.reduce(indexed_queries, {%{}, sorted_nums, %{}}, fn q,
                                                               {ans_map, remaining, trie} ->
        {new_remaining, new_trie} = insert_while(remaining, trie, q.m)

        ans =
          if map_size(new_trie) == 0 do
            -1
          else
            query_max_xor(new_trie, q.x)
          end

        {Map.put(ans_map, q.idx, ans), new_remaining, new_trie}
      end)

    Enum.map(0..(length(queries) - 1), fn i -> Map.fetch!(answers_map, i) end)
  end

  defp insert_while([], trie, _m), do: {[], trie}

  defp insert_while([h | t] = list, trie, m) when h <= m do
    new_trie = insert(trie, h)
    insert_while(t, new_trie, m)
  end

  defp insert_while(list, trie, _m), do: {list, trie}

  # Insert number into binary trie (bits 30..0)
  defp insert(trie, num) do
    do_insert(trie, num, 30)
  end

  defp do_insert(nil, _num, _i), do: %{}
  defp do_insert(node, _num, i) when i < 0, do: node

  defp do_insert(node, num, i) do
    bit = (num >>> i) &&& 1
    child = Map.get(node, bit, %{})
    new_child = do_insert(child, num, i - 1)
    Map.put(node, bit, new_child)
  end

  # Query maximum xor with x using trie; assumes trie non-empty
  defp query_max_xor(trie, x) do
    do_query(trie, x, 30, 0)
  end

  defp do_query(_node, _x, i, acc) when i < 0, do: acc

  defp do_query(node, x, i, acc) do
    bit = (x >>> i) &&& 1
    preferred = 1 - bit

    if Map.has_key?(node, preferred) do
      child = Map.get(node, preferred)
      do_query(child, x, i - 1, acc ||| (1 <<< i))
    else
      child = Map.get(node, bit)
      do_query(child, x, i - 1, acc)
    end
  end
end
```
