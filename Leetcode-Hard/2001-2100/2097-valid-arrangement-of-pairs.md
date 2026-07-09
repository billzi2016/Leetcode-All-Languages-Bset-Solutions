# 2097. Valid Arrangement of Pairs

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        unordered_map<int, vector<int>> adj;
        unordered_map<int, int> outDeg, inDeg;
        for (auto& p : pairs) {
            int u = p[0], v = p[1];
            adj[u].push_back(v);
            ++outDeg[u];
            ++inDeg[v];
        }
        int start = pairs[0][0];
        for (const auto& kv : outDeg) {
            int node = kv.first;
            if (outDeg[node] - inDeg[node] == 1) {
                start = node;
                break;
            }
        }
        // Hierholzer's algorithm (iterative)
        vector<int> path;
        stack<int> st;
        st.push(start);
        while (!st.empty()) {
            int u = st.top();
            auto& vec = adj[u];
            if (!vec.empty()) {
                int v = vec.back();
                vec.pop_back();
                st.push(v);
            } else {
                path.push_back(u);
                st.pop();
            }
        }
        reverse(path.begin(), path.end());
        vector<vector<int>> res;
        for (size_t i = 1; i < path.size(); ++i) {
            res.push_back({path[i-1], path[i]});
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] validArrangement(int[][] pairs) {
        java.util.Map<Integer, java.util.Deque<Integer>> adj = new java.util.HashMap<>();
        java.util.Map<Integer, Integer> outDeg = new java.util.HashMap<>();
        java.util.Map<Integer, Integer> inDeg = new java.util.HashMap<>();

        for (int[] p : pairs) {
            int u = p[0], v = p[1];
            adj.computeIfAbsent(u, k -> new java.util.ArrayDeque<>()).add(v);
            outDeg.put(u, outDeg.getOrDefault(u, 0) + 1);
            inDeg.put(v, inDeg.getOrDefault(v, 0) + 1);
        }

        int start = pairs[0][0];
        for (int node : outDeg.keySet()) {
            int out = outDeg.get(node);
            int in = inDeg.getOrDefault(node, 0);
            if (out - in == 1) {
                start = node;
                break;
            }
        }

        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        java.util.List<Integer> path = new java.util.ArrayList<>();
        stack.push(start);
        while (!stack.isEmpty()) {
            int v = stack.peek();
            java.util.Deque<Integer> nbrs = adj.get(v);
            if (nbrs != null && !nbrs.isEmpty()) {
                int u = nbrs.pollFirst();
                stack.push(u);
            } else {
                path.add(stack.pop());
            }
        }

        java.util.Collections.reverse(path);
        int m = pairs.length;
        int[][] res = new int[m][2];
        for (int i = 1; i < path.size(); i++) {
            res[i - 1][0] = path.get(i - 1);
            res[i - 1][1] = path.get(i);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        graph = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        for a, b in pairs:
            graph[a].append(b)
            outdeg[a] += 1
            indeg[b] += 1

        start = None
        for node in outdeg:
            if outdeg[node] - indeg.get(node, 0) == 1:
                start = node
                break
        if start is None:
            start = pairs[0][0]

        stack = [start]
        path = []
        while stack:
            v = stack[-1]
            if graph[v]:
                nxt = graph[v].pop()
                stack.append(nxt)
            else:
                path.append(stack.pop())

        path.reverse()
        res = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
        return res
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        for a, b in pairs:
            adj[a].append(b)
            outdeg[a] += 1
            indeg[b] += 1

        start = None
        for node in outdeg:
            if outdeg[node] - indeg.get(node, 0) == 1:
                start = node
                break
        if start is None:
            start = pairs[0][0]

        stack = [start]
        path = []
        while stack:
            v = stack[-1]
            if adj[v]:
                nxt = adj[v].pop()
                stack.append(nxt)
            else:
                path.append(stack.pop())

        path.reverse()
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

/* lower_bound: first index where arr[idx] >= target */
static int lower_bound(int *arr, int size, int target) {
    int l = 0, r = size;
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] < target)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** validArrangement(int** pairs, int pairsSize, int* pairsColSize,
                       int* returnSize, int*** returnColumnSizes) {
    (void)pairsColSize;  // unused

    int n = pairsSize;
    if (n == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    /* 1. Collect all vertex values */
    int totalVals = 2 * n;
    int *vals = (int *)malloc(totalVals * sizeof(int));
    for (int i = 0; i < n; ++i) {
        vals[2*i]   = pairs[i][0];
        vals[2*i+1] = pairs[i][1];
    }

    /* 2. Sort and deduplicate */
    qsort(vals, totalVals, sizeof(int), cmp_int);
    int m = 0;
    for (int i = 0; i < totalVals; ++i) {
        if (i == 0 || vals[i] != vals[i-1]) {
            vals[m++] = vals[i];
        }
    }

    /* 3. Map edges to compressed indices */
    int *edgeStart = (int *)malloc(n * sizeof(int));
    int *edgeEnd   = (int *)malloc(n * sizeof(int));

    int *outDeg = (int *)calloc(m, sizeof(int));
    int *inDeg  = (int *)calloc(m, sizeof(int));

    for (int i = 0; i < n; ++i) {
        int s = lower_bound(vals, m, pairs[i][0]);
        int e = lower_bound(vals, m, pairs[i][1]);
        edgeStart[i] = s;
        edgeEnd[i]   = e;
        outDeg[s]++;
        inDeg[e]++;
    }

    /* 4. Build adjacency lists (as stacks) */
    int **adj = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        if (outDeg[i] > 0)
            adj[i] = (int *)malloc(outDeg[i] * sizeof(int));
        else
            adj[i] = NULL;
    }

    int *curPos = (int *)calloc(m, sizeof(int));
    for (int i = 0; i < n; ++i) {
        int s = edgeStart[i];
        int e = edgeEnd[i];
        adj[s][curPos[s]++] = e;   // fill forward
    }

    /* remaining edges counter per vertex */
    int *rem = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) rem[i] = outDeg[i];

    /* 5. Determine start vertex */
    int start = -1;
    for (int i = 0; i < m; ++i) {
        if (outDeg[i] == inDeg[i] + 1) {
            start = i;
            break;
        }
    }
    if (start == -1) start = edgeStart[0];

    /* 6. Hierholzer's algorithm (iterative) */
    int *stack = (int *)malloc((n + 5) * sizeof(int));
    int top = 0;
    stack[top++] = start;

    int *path = (int *)malloc((n + 5) * sizeof(int));
    int pathLen = 0;

    while (top > 0) {
        int v = stack[top - 1];
        if (rem[v] > 0) {
            int u = adj[v][--rem[v]];
            stack[top++] = u;
        } else {
            path[pathLen++] = v;
            top--;
        }
    }

    /* 7. Build result */
    *returnSize = n;
    int **ans = (int **)malloc(n * sizeof(int *));
    int *colSizes = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) {
        ans[i] = (int *)malloc(2 * sizeof(int));
        int fromIdx = path[pathLen - 1 - i];
        int toIdx   = path[pathLen - 1 - (i + 1)];
        ans[i][0] = vals[fromIdx];
        ans[i][1] = vals[toIdx];
        colSizes[i] = 2;
    }

    *returnColumnSizes = &colSizes;

    /* Cleanup temporary allocations (optional, LeetCode ignores) */
    free(vals);
    free(edgeStart);
    free(edgeEnd);
    free(outDeg);
    free(inDeg);
    for (int i = 0; i < m; ++i) {
        if (adj[i]) free(adj[i]);
    }
    free(adj);
    free(curPos);
    free(rem);
    free(stack);
    free(path);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] ValidArrangement(int[][] pairs) {
        var adj = new Dictionary<int, Stack<int>>();
        var outDeg = new Dictionary<int, int>();
        var inDeg = new Dictionary<int, int>();

        foreach (var p in pairs) {
            int u = p[0];
            int v = p[1];

            if (!adj.ContainsKey(u)) adj[u] = new Stack<int>();
            adj[u].Push(v);

            outDeg[u] = outDeg.GetValueOrDefault(u) + 1;
            inDeg[v] = inDeg.GetValueOrDefault(v) + 1;
        }

        int start = pairs[0][0];
        foreach (var kvp in outDeg) {
            int node = kvp.Key;
            int outd = kvp.Value;
            int ind = inDeg.GetValueOrDefault(node);
            if (outd - ind == 1) {
                start = node;
                break;
            }
        }

        var stack = new Stack<int>();
        var path = new List<int>();
        stack.Push(start);

        while (stack.Count > 0) {
            int v = stack.Peek();
            if (adj.ContainsKey(v) && adj[v].Count > 0) {
                int nxt = adj[v].Pop();
                stack.Push(nxt);
            } else {
                path.Add(v);
                stack.Pop();
            }
        }

        path.Reverse();

        var result = new int[path.Count - 1][];
        for (int i = 1; i < path.Count; i++) {
            result[i - 1] = new int[] { path[i - 1], path[i] };
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} pairs
 * @return {number[][]}
 */
var validArrangement = function(pairs) {
    const adj = new Map();          // start -> array of ends
    const outDeg = Object.create(null);
    const inDeg = Object.create(null);

    for (const [u, v] of pairs) {
        if (!adj.has(u)) adj.set(u, []);
        adj.get(u).push(v);
        outDeg[u] = (outDeg[u] || 0) + 1;
        inDeg[v] = (inDeg[v] || 0) + 1;
    }

    // find start node: out - in == 1, else any start
    let start = pairs[0][0];
    for (const u of Object.keys(outDeg)) {
        const o = outDeg[u];
        const i = inDeg[u] || 0;
        if (o === i + 1) {
            start = Number(u);
            break;
        }
    }

    // Hierholzer's algorithm (iterative)
    const stack = [start];
    const path = [];

    while (stack.length) {
        let v = stack[stack.length - 1];
        const edges = adj.get(v);
        if (edges && edges.length) {
            const nxt = edges.pop(); // O(1)
            stack.push(nxt);
        } else {
            path.push(stack.pop());
        }
    }

    path.reverse();

    const res = [];
    for (let i = 1; i < path.length; ++i) {
        res.push([path[i - 1], path[i]]);
    }
    return res;
};
```

## Typescript

```typescript
function validArrangement(pairs: number[][]): number[][] {
    const adj = new Map<number, number[]>();
    const outDeg = new Map<number, number>();
    const inDeg = new Map<number, number>();

    for (const [u, v] of pairs) {
        if (!adj.has(u)) adj.set(u, []);
        adj.get(u)!.push(v);
        outDeg.set(u, (outDeg.get(u) ?? 0) + 1);
        inDeg.set(v, (inDeg.get(v) ?? 0) + 1);
    }

    let start: number | undefined;
    for (const [node, out] of outDeg.entries()) {
        const indeg = inDeg.get(node) ?? 0;
        if (out === indeg + 1) {
            start = node;
            break;
        }
    }
    if (start === undefined) start = pairs[0][0];

    const stack: number[] = [start];
    const path: number[] = [];

    while (stack.length) {
        const v = stack[stack.length - 1];
        const edges = adj.get(v);
        if (edges && edges.length > 0) {
            const to = edges.pop()!;
            stack.push(to);
        } else {
            path.push(stack.pop()!);
        }
    }

    path.reverse();

    const result: number[][] = [];
    for (let i = 1; i < path.length; ++i) {
        result.push([path[i - 1], path[i]]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $pairs
     * @return Integer[][]
     */
    function validArrangement($pairs) {
        $adj = [];
        $out = [];
        $in  = [];

        foreach ($pairs as $pair) {
            $s = $pair[0];
            $e = $pair[1];

            $adj[$s][] = $e;               // store edge
            $out[$s] = ($out[$s] ?? 0) + 1;
            $in[$e]  = ($in[$e]  ?? 0) + 1;
        }

        // find start node: out-degree = in-degree + 1, if exists
        $start = null;
        foreach ($out as $node => $deg) {
            $indeg = $in[$node] ?? 0;
            if ($deg == $indeg + 1) {
                $start = $node;
                break;
            }
        }
        if ($start === null) {
            $start = $pairs[0][0];
        }

        // Hierholzer's algorithm (iterative)
        $stack = [];
        $path  = [];

        array_push($stack, $start);
        while (!empty($stack)) {
            $v = end($stack); // peek top
            if (isset($adj[$v]) && count($adj[$v]) > 0) {
                $next = array_pop($adj[$v]); // take an outgoing edge
                array_push($stack, $next);
            } else {
                $path[] = array_pop($stack); // backtrack
            }
        }

        $path = array_reverse($path);

        $result = [];
        for ($i = 1; $i < count($path); $i++) {
            $result[] = [$path[$i - 1], $path[$i]];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func validArrangement(_ pairs: [[Int]]) -> [[Int]] {
        var adj = [Int: [Int]]()
        var outDeg = [Int: Int]()
        var inDeg = [Int: Int]()
        
        for p in pairs {
            let u = p[0]
            let v = p[1]
            adj[u, default: []].append(v)
            outDeg[u, default: 0] += 1
            inDeg[v, default: 0] += 1
        }
        
        var start = pairs[0][0]
        for (node, out) in outDeg {
            let indeg = inDeg[node] ?? 0
            if out == indeg + 1 {
                start = node
                break
            }
        }
        
        var stack = [Int]()
        var path = [Int]()
        stack.append(start)
        
        while !stack.isEmpty {
            let v = stack.last!
            if var neighbors = adj[v], !neighbors.isEmpty {
                let next = neighbors.removeLast()
                adj[v] = neighbors
                stack.append(next)
            } else {
                path.append(v)
                stack.removeLast()
            }
        }
        
        path.reverse()
        var result = [[Int]]()
        for i in 1..<path.count {
            result.append([path[i - 1], path[i]])
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import java.util.Collections

class Solution {
    fun validArrangement(pairs: Array<IntArray>): Array<IntArray> {
        val adj = HashMap<Int, ArrayDeque<Int>>()
        val outDeg = HashMap<Int, Int>()
        val inDeg = HashMap<Int, Int>()

        for (p in pairs) {
            val u = p[0]
            val v = p[1]
            adj.getOrPut(u) { ArrayDeque() }.add(v)
            outDeg[u] = outDeg.getOrDefault(u, 0) + 1
            inDeg[v] = inDeg.getOrDefault(v, 0) + 1
        }

        var start = pairs[0][0]
        for (node in outDeg.keys) {
            val out = outDeg[node] ?: 0
            val inn = inDeg[node] ?: 0
            if (out == inn + 1) {
                start = node
                break
            }
        }

        val stack: ArrayDeque<Int> = ArrayDeque()
        val path = mutableListOf<Int>()
        stack.push(start)

        while (!stack.isEmpty()) {
            val v = stack.peek()
            val deque = adj[v]
            if (deque != null && !deque.isEmpty()) {
                val nxt = deque.pollFirst()
                stack.push(nxt)
            } else {
                path.add(stack.pop())
            }
        }

        Collections.reverse(path)

        val result = Array(path.size - 1) { IntArray(2) }
        for (i in 0 until path.size - 1) {
            result[i][0] = path[i]
            result[i][1] = path[i + 1]
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> validArrangement(List<List<int>> pairs) {
    // Build adjacency list and degree maps
    final Map<int, List<int>> adj = {};
    final Map<int, int> outDeg = {};
    final Map<int, int> inDeg = {};

    for (var p in pairs) {
      int u = p[0];
      int v = p[1];
      adj.putIfAbsent(u, () => []).add(v);
      outDeg[u] = (outDeg[u] ?? 0) + 1;
      inDeg[v] = (inDeg[v] ?? 0) + 1;
    }

    // Find start node
    int? start;
    for (var entry in outDeg.entries) {
      int node = entry.key;
      int out = entry.value;
      int inn = inDeg[node] ?? 0;
      if (out == inn + 1) {
        start = node;
        break;
      }
    }
    start ??= pairs[0][0];

    // Hierholzer's algorithm (iterative)
    final List<int> stack = [start];
    final List<int> path = [];

    while (stack.isNotEmpty) {
      int v = stack.last;
      var edges = adj[v];
      if (edges != null && edges.isNotEmpty) {
        int to = edges.removeLast();
        stack.add(to);
      } else {
        path.add(v);
        stack.removeLast();
      }
    }

    // Reverse the path to get correct order
    final List<int> revPath = path.reversed.toList();

    // Build result pairs
    final List<List<int>> res = [];
    for (int i = 1; i < revPath.length; ++i) {
      res.add([revPath[i - 1], revPath[i]]);
    }
    return res;
  }
}
```

## Golang

```go
func validArrangement(pairs [][]int) [][]int {
	adj := make(map[int][]int)
	indeg := make(map[int]int)
	outdeg := make(map[int]int)

	for _, p := range pairs {
		u, v := p[0], p[1]
		adj[u] = append(adj[u], v)
		outdeg[u]++
		indeg[v]++
	}

	start := -1
	for node, od := range outdeg {
		if od-indeg[node] == 1 {
			start = node
			break
		}
	}
	if start == -1 {
		start = pairs[0][0]
	}

	stack := []int{start}
	path := []int{}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		if len(adj[v]) > 0 {
			nxt := adj[v][len(adj[v])-1]
			adj[v] = adj[v][:len(adj[v])-1]
			stack = append(stack, nxt)
		} else {
			path = append(path, v)
			stack = stack[:len(stack)-1]
		}
	}

	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}

	ans := make([][]int, 0, len(pairs))
	for i := 0; i+1 < len(path); i++ {
		ans = append(ans, []int{path[i], path[i+1]})
	}
	return ans
}
```

## Ruby

```ruby
def valid_arrangement(pairs)
  adj = Hash.new { |h, k| h[k] = [] }
  indeg = Hash.new(0)
  outdeg = Hash.new(0)

  pairs.each do |u, v|
    adj[u] << v
    outdeg[u] += 1
    indeg[v] += 1
  end

  start_node = nil
  outdeg.each_key do |node|
    if outdeg[node] - indeg[node] == 1
      start_node = node
      break
    end
  end
  start_node ||= pairs[0][0]

  stack = [start_node]
  path = []

  while !stack.empty?
    v = stack[-1]
    if adj[v].empty?
      path << stack.pop
    else
      stack << adj[v].pop
    end
  end

  path.reverse!
  result = []
  (1...path.size).each do |i|
    result << [path[i - 1], path[i]]
  end
  result
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayDeque, Stack, ArrayBuffer, Map}

object Solution {
  def validArrangement(pairs: Array[Array[Int]]): Array[Array[Int]] = {
    val adj: Map[Int, ArrayDeque[Int]] = Map()
    val indeg: Map[Int, Int] = Map()
    val outdeg: Map[Int, Int] = Map()

    for (p <- pairs) {
      val u = p(0)
      val v = p(1)

      adj.getOrElseUpdate(u, ArrayDeque()).append(v)

      outdeg.update(u, outdeg.getOrElse(u, 0) + 1)
      indeg.update(v, indeg.getOrElse(v, 0) + 1)
    }

    // Find start node: a node with outdegree = indegree + 1, otherwise any start
    val startNode: Int = outdeg.keys.find(node => outdeg(node) == indeg.getOrElse(node, 0) + 1)
      .getOrElse(pairs(0)(0))

    val stack = Stack[Int]()
    val path = ArrayBuffer[Int]()

    stack.push(startNode)

    while (stack.nonEmpty) {
      val v = stack.top
      adj.get(v) match {
        case Some(deq) if deq.nonEmpty =>
          val nxt = deq.removeHead()
          stack.push(nxt)
        case _ =>
          path.append(stack.pop())
      }
    }

    val revPath = path.reverse

    val result = new Array[Array[Int]](revPath.length - 1)
    for (i <- 1 until revPath.length) {
      result(i - 1) = Array(revPath(i - 1), revPath(i))
    }
    result
  }
}
```

## Rust

```rust
use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn valid_arrangement(pairs: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut adj: HashMap<i32, VecDeque<i32>> = HashMap::new();
        let mut out_deg: HashMap<i32, i32> = HashMap::new();
        let mut in_deg: HashMap<i32, i32> = HashMap::new();

        for p in pairs.iter() {
            let u = p[0];
            let v = p[1];
            adj.entry(u).or_insert_with(VecDeque::new).push_back(v);
            *out_deg.entry(u).or_insert(0) += 1;
            *in_deg.entry(v).or_insert(0) += 1;
        }

        // Find start node
        let mut start = pairs[0][0];
        for (&node, &out) in out_deg.iter() {
            let indeg = *in_deg.get(&node).unwrap_or(&0);
            if out == indeg + 1 {
                start = node;
                break;
            }
        }

        // Hierholzer's algorithm (iterative)
        let mut stack: Vec<i32> = vec![start];
        let mut path: Vec<i32> = Vec::new();

        while let Some(&v) = stack.last() {
            if let Some(nei) = adj.get_mut(&v) {
                if let Some(next) = nei.pop_front() {
                    stack.push(next);
                    continue;
                }
            }
            // No more outgoing edges from v
            path.push(v);
            stack.pop();
        }

        path.reverse();

        let mut result: Vec<Vec<i32>> = Vec::new();
        for i in 1..path.len() {
            result.push(vec![path[i - 1], path[i]]);
        }
        result
    }
}
```

## Racket

```racket
(require racket/queue)

(define/contract (valid-arrangement pairs)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((adj   (make-hash))
         (indeg (make-hash))
         (outdeg (make-hash))
         (first-pair (car pairs)))
    ;; build graph and degree maps
    (for ([p pairs])
      (define start (list-ref p 0))
      (define end   (list-ref p 1))
      (let ((q (hash-ref adj start (lambda () (make-queue)))))
        (enqueue! q end)
        (hash-set! adj start q))
      (hash-set! outdeg start (+ 1 (hash-ref outdeg start 0)))
      (hash-set! indeg   end   (+ 1 (hash-ref indeg   end 0))))
    ;; find start node (out = in + 1) if exists
    (define start-node
      (let loop ((keys (hash-keys outdeg)))
        (cond [(null? keys) #f]
              [else (let* ((node (car keys))
                           (out (hash-ref outdeg node 0))
                           (in  (hash-ref indeg   node 0)))
                      (if (= out (+ in 1))
                          node
                          (loop (cdr keys))))])))
    (define start (or start-node (list-ref first-pair 0)))
    ;; Hierholzer's algorithm (iterative)
    (define (hierholzer start adj)
      (let loop ((stack (list start)) (circuit '()))
        (if (null? stack)
            (reverse circuit)
            (let* ((v (car stack))
                   (q (hash-ref adj v #f)))
              (if (and q (not (queue-empty? q)))
                  (let ((next (dequeue! q)))
                    (loop (cons next stack) circuit))
                  (loop (cdr stack) (cons v circuit)))))))
    (define vertices (hierholzer start adj))
    ;; build result pairs from vertex sequence
    (let build ((prev (car vertices)) (rest (cdr vertices)) (acc '()))
      (if (null? rest)
          (reverse acc)
          (build (car rest) (cdr rest) (cons (list prev (car rest)) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([valid_arrangement/1]).

-spec valid_arrangement(Pairs :: [[integer()]]) -> [[integer()]].
valid_arrangement(Pairs) ->
    {Adj, InDeg, OutDeg} = build_maps(Pairs, #{}, #{}, #{}),
    StartNode = find_start_node(Pairs, InDeg, OutDeg),
    PathRev = dfs([StartNode], Adj, []),
    Nodes = lists:reverse(PathRev),
    build_pairs(Nodes, []).

%% Build adjacency list and degree maps
build_maps([], Adj, InDeg, OutDeg) ->
    {Adj, InDeg, OutDeg};
build_maps([[U, V] | Rest], Adj, InDeg, OutDeg) ->
    Adj1 = case maps:find(U, Adj) of
        {ok, List} -> maps:put(U, [V | List], Adj);
        error      -> maps:put(U, [V], Adj)
    end,
    InDeg1  = maps:update_with(V, fun(C) -> C + 1 end, 1, InDeg),
    OutDeg1 = maps:update_with(U, fun(C) -> C + 1 end, 1, OutDeg),
    build_maps(Rest, Adj1, InDeg1, OutDeg1).

%% Determine start node for Eulerian path
find_start_node(Pairs, InDeg, OutDeg) ->
    Candidates = [Node ||
        {Node, Out} <- maps:to_list(OutDeg),
        (maps:get(Node, InDeg, 0) + 1) =:= Out],
    case Candidates of
        [S | _] -> S;
        [] ->
            [[First | _] | _] = Pairs,
            First
    end.

%% Hierholzer's algorithm (iterative using stack)
dfs([], _Adj, Path) ->
    Path;
dfs([Curr | RestStack] = Stack, Adj, Path) ->
    case maps:get(Curr, Adj, []) of
        [] ->
            dfs(RestStack, Adj, [Curr | Path]);
        [Next | Remaining] ->
            NewAdj = maps:put(Curr, Remaining, Adj),
            dfs([Next | Stack], NewAdj, Path)
    end.

%% Convert node list to pair list
build_pairs([_], Acc) ->
    lists:reverse(Acc);
build_pairs([A, B | Rest], Acc) ->
    build_pairs([B | Rest], [[A, B] | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_arrangement(pairs :: [[integer]]) :: [[integer]]
  def valid_arrangement(pairs) do
    {adj, outdeg, indeg} = build_graph(pairs)
    start = find_start(pairs, outdeg, indeg)
    path = hierholzer(start, adj, [])
    build_pairs(path, [])
  end

  # Build adjacency list and degree maps
  defp build_graph(pairs) do
    Enum.reduce(pairs, {%{}, %{}, %{}}, fn [u, v], {adj, outd, ind} ->
      adj = Map.update(adj, u, [v], fn lst -> [v | lst] end)
      outd = Map.update(outd, u, 1, &(&1 + 1))
      ind = Map.update(ind, v, 1, &(&1 + 1))
      {adj, outd, ind}
    end)
  end

  # Determine starting node for Eulerian path
  defp find_start(pairs, outdeg, indeg) do
    start =
      Enum.find(Map.keys(outdeg), fn node ->
        out = Map.get(outdeg, node, 0)
        inn = Map.get(indeg, node, 0)
        out == inn + 1
      end)

    case start do
      nil -> hd(pairs) |> List.first()
      _ -> start
    end
  end

  # Hierholzer's algorithm (iterative)
  defp hierholzer(start, adj, path) do
    loop([start], adj, path)
  end

  defp loop([], _adj, path), do: path

  defp loop([v | rest_stack] = stack, adj, path) do
    case Map.get(adj, v, []) do
      [] ->
        # no outgoing edges, add to result and pop from stack
        loop(rest_stack, adj, [v | path])

      [next | remaining] ->
        new_adj = Map.put(adj, v, remaining)
        loop([next | stack], new_adj, path)
    end
  end

  # Convert vertex path to list of pairs
  defp build_pairs([_], acc), do: Enum.reverse(acc)

  defp build_pairs([a, b | rest], acc) do
    build_pairs([b | rest], [[a, b] | acc])
  end
end
```
