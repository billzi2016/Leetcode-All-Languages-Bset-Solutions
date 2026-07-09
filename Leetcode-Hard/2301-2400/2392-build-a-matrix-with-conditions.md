# 2392. Build a Matrix With Conditions

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topoSort(int k, const vector<vector<int>>& cond) {
        vector<vector<int>> adj(k + 1);
        vector<int> indeg(k + 1, 0);
        for (const auto& e : cond) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            ++indeg[v];
        }
        queue<int> q;
        for (int i = 1; i <= k; ++i)
            if (indeg[i] == 0) q.push(i);
        vector<int> order;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (--indeg[v] == 0) q.push(v);
            }
        }
        if ((int)order.size() != k) return {};
        return order;
    }

    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        vector<int> rowOrder = topoSort(k, rowConditions);
        vector<int> colOrder = topoSort(k, colConditions);
        if (rowOrder.empty() || colOrder.empty()) return {};

        vector<int> rowPos(k + 1), colPos(k + 1);
        for (int i = 0; i < k; ++i) rowPos[rowOrder[i]] = i;
        for (int i = 0; i < k; ++i) colPos[colOrder[i]] = i;

        vector<vector<int>> ans(k, vector<int>(k, 0));
        for (int val = 1; val <= k; ++val) {
            ans[rowPos[val]][colPos[val]] = val;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[][] buildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        int[] rowOrder = topologicalSort(k, rowConditions);
        int[] colOrder = topologicalSort(k, colConditions);
        if (rowOrder == null || colOrder == null) {
            return new int[0][0];
        }
        int[] rowPos = new int[k + 1];
        int[] colPos = new int[k + 1];
        for (int i = 0; i < k; i++) {
            rowPos[rowOrder[i]] = i;
            colPos[colOrder[i]] = i;
        }
        int[][] matrix = new int[k][k];
        for (int v = 1; v <= k; v++) {
            matrix[rowPos[v]][colPos[v]] = v;
        }
        return matrix;
    }

    private int[] topologicalSort(int n, int[][] edges) {
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] indegree = new int[n + 1];
        for (int[] e : edges) {
            int from = e[0], to = e[1];
            graph[from].add(to);
            indegree[to]++;
        }
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }
        int[] order = new int[n];
        int idx = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            order[idx++] = node;
            for (int nb : graph[node]) {
                indegree[nb]--;
                if (indegree[nb] == 0) {
                    queue.add(nb);
                }
            }
        }
        return idx == n ? order : null;
    }
}
```

## Python

```python
class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque

        def topo_sort(edges, n):
            adj = [[] for _ in range(n + 1)]
            indeg = [0] * (n + 1)
            for u, v in edges:
                adj[u].append(v)
                indeg[v] += 1
            q = deque([i for i in range(1, n + 1) if indeg[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nb in adj[node]:
                    indeg[nb] -= 1
                    if indeg[nb] == 0:
                        q.append(nb)
            return order if len(order) == n else []

        row_order = topo_sort(rowConditions, k)
        col_order = topo_sort(colConditions, k)

        if not row_order or not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num

        return matrix
```

## Python3

```python
import collections
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges: List[List[int]]) -> List[int]:
            adj = [[] for _ in range(k + 1)]
            indeg = [0] * (k + 1)
            for a, b in edges:
                adj[a].append(b)
                indeg[b] += 1
            q = collections.deque([i for i in range(1, k + 1) if indeg[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nb in adj[node]:
                    indeg[nb] -= 1
                    if indeg[nb] == 0:
                        q.append(nb)
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num

        return matrix
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
static int* topoSort(int k, int** conds, int condSize) {
    int *indeg = calloc(k + 1, sizeof(int));
    int *outCnt = calloc(k + 1, sizeof(int));

    for (int i = 0; i < condSize; ++i) {
        int u = conds[i][0];
        int v = conds[i][1];
        outCnt[u]++;
        indeg[v]++;
    }

    int **adj = malloc((k + 1) * sizeof(int*));
    for (int i = 1; i <= k; ++i) {
        adj[i] = malloc(outCnt[i] * sizeof(int));
    }

    int *fillIdx = calloc(k + 1, sizeof(int));
    for (int i = 0; i < condSize; ++i) {
        int u = conds[i][0];
        int v = conds[i][1];
        adj[u][fillIdx[u]++] = v;
    }

    int *queue = malloc(k * sizeof(int));
    int front = 0, back = 0;
    for (int i = 1; i <= k; ++i) {
        if (indeg[i] == 0) queue[back++] = i;
    }

    int *order = malloc(k * sizeof(int));
    int pos = 0;
    while (front < back) {
        int node = queue[front++];
        order[pos++] = node;
        for (int j = 0; j < outCnt[node]; ++j) {
            int nb = adj[node][j];
            if (--indeg[nb] == 0) queue[back++] = nb;
        }
    }

    // cleanup
    for (int i = 1; i <= k; ++i) free(adj[i]);
    free(adj);
    free(indeg);
    free(outCnt);
    free(fillIdx);
    free(queue);

    if (pos != k) {
        free(order);
        return NULL;
    }
    return order;
}

int** buildMatrix(int k, int** rowConditions, int rowConditionsSize, int* rowConditionsColSize,
                  int** colConditions, int colConditionsSize, int* colConditionsColSize,
                  int* returnSize, int*** returnColumnSizes) {
    (void)rowConditionsColSize; // unused
    (void)colConditionsColSize; // unused

    int *orderRows = topoSort(k, rowConditions, rowConditionsSize);
    int *orderCols = topoSort(k, colConditions, colConditionsSize);

    if (!orderRows || !orderCols) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        free(orderRows);
        free(orderCols);
        return NULL;
    }

    int **ans = malloc(k * sizeof(int*));
    for (int i = 0; i < k; ++i) {
        ans[i] = calloc(k, sizeof(int));
    }

    int *posRow = calloc(k + 1, sizeof(int));
    int *posCol = calloc(k + 1, sizeof(int));
    for (int i = 0; i < k; ++i) {
        posRow[orderRows[i]] = i;
        posCol[orderCols[i]] = i;
    }

    for (int v = 1; v <= k; ++v) {
        ans[posRow[v]][posCol[v]] = v;
    }

    *returnSize = k;
    int **colSizes = malloc(sizeof(int*));
    *colSizes = malloc(k * sizeof(int));
    for (int i = 0; i < k; ++i) (*colSizes)[i] = k;
    *returnColumnSizes = colSizes;

    free(orderRows);
    free(orderCols);
    free(posRow);
    free(posCol);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] BuildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        int[] rowOrder = TopoSort(k, rowConditions);
        int[] colOrder = TopoSort(k, colConditions);
        if (rowOrder == null || colOrder == null) {
            return new int[0][];
        }

        int[][] matrix = new int[k][];
        for (int i = 0; i < k; i++) {
            matrix[i] = new int[k];
        }

        int[] rowPos = new int[k + 1];
        int[] colPos = new int[k + 1];
        for (int i = 0; i < k; i++) {
            rowPos[rowOrder[i]] = i;
            colPos[colOrder[i]] = i;
        }

        for (int num = 1; num <= k; num++) {
            matrix[rowPos[num]][colPos[num]] = num;
        }

        return matrix;
    }

    private int[] TopoSort(int n, int[][] edges) {
        List<int>[] adj = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new List<int>();
        int[] indeg = new int[n + 1];

        foreach (var e in edges) {
            int from = e[0];
            int to = e[1];
            adj[from].Add(to);
            indeg[to]++;
        }

        Queue<int> q = new Queue<int>();
        for (int i = 1; i <= n; i++) {
            if (indeg[i] == 0) q.Enqueue(i);
        }

        int[] order = new int[n];
        int idx = 0;
        while (q.Count > 0) {
            int u = q.Dequeue();
            order[idx++] = u;
            foreach (int v in adj[u]) {
                indeg[v]--;
                if (indeg[v] == 0) q.Enqueue(v);
            }
        }

        return idx == n ? order : null;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number[][]} rowConditions
 * @param {number[][]} colConditions
 * @return {number[][]}
 */
var buildMatrix = function(k, rowConditions, colConditions) {
    const topoSort = (edges) => {
        const adj = Array.from({ length: k + 1 }, () => []);
        const indeg = new Array(k + 1).fill(0);
        const seen = new Set();
        for (const [u, v] of edges) {
            const key = u + ',' + v;
            if (!seen.has(key)) {
                seen.add(key);
                adj[u].push(v);
                indeg[v]++;
            }
        }
        const queue = [];
        for (let i = 1; i <= k; i++) {
            if (indeg[i] === 0) queue.push(i);
        }
        const order = [];
        let qIdx = 0;
        while (qIdx < queue.length) {
            const node = queue[qIdx++];
            order.push(node);
            for (const nb of adj[node]) {
                indeg[nb]--;
                if (indeg[nb] === 0) queue.push(nb);
            }
        }
        return order.length === k ? order : [];
    };

    const rowOrder = topoSort(rowConditions);
    if (rowOrder.length === 0) return [];

    const colOrder = topoSort(colConditions);
    if (colOrder.length === 0) return [];

    const rowPos = new Array(k + 1);
    const colPos = new Array(k + 1);
    for (let i = 0; i < k; i++) {
        rowPos[rowOrder[i]] = i;
        colPos[colOrder[i]] = i;
    }

    const matrix = Array.from({ length: k }, () => Array(k).fill(0));
    for (let num = 1; num <= k; num++) {
        matrix[rowPos[num]][colPos[num]] = num;
    }
    return matrix;
};
```

## Typescript

```typescript
function buildMatrix(k: number, rowConditions: number[][], colConditions: number[][]): number[][] {
    const topoSort = (edges: number[][]): number[] => {
        const adj: number[][] = Array.from({ length: k + 1 }, () => []);
        const indeg = new Array(k + 1).fill(0);
        for (const [u, v] of edges) {
            adj[u].push(v);
            indeg[v]++;
        }
        const queue: number[] = [];
        for (let i = 1; i <= k; i++) {
            if (indeg[i] === 0) queue.push(i);
        }
        const order: number[] = [];
        let qIdx = 0;
        while (qIdx < queue.length) {
            const node = queue[qIdx++];
            order.push(node);
            for (const nb of adj[node]) {
                indeg[nb]--;
                if (indeg[nb] === 0) queue.push(nb);
            }
        }
        return order.length === k ? order : [];
    };

    const rowOrder = topoSort(rowConditions);
    const colOrder = topoSort(colConditions);
    if (rowOrder.length === 0 || colOrder.length === 0) return [];

    const rowPos = new Array(k + 1).fill(0);
    const colPos = new Array(k + 1).fill(0);
    for (let i = 0; i < k; i++) {
        rowPos[rowOrder[i]] = i;
        colPos[colOrder[i]] = i;
    }

    const matrix: number[][] = Array.from({ length: k }, () => Array(k).fill(0));
    for (let v = 1; v <= k; v++) {
        const r = rowPos[v];
        const c = colPos[v];
        matrix[r][c] = v;
    }
    return matrix;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer[][] $rowConditions
     * @param Integer[][] $colConditions
     * @return Integer[][]
     */
    function buildMatrix($k, $rowConditions, $colConditions) {
        $rowOrder = $this->topoSort($k, $rowConditions);
        if (empty($rowOrder)) {
            return [];
        }
        $colOrder = $this->topoSort($k, $colConditions);
        if (empty($colOrder)) {
            return [];
        }

        // map number to its row and column index
        $rowPos = array_fill(0, $k + 1, 0);
        foreach ($rowOrder as $idx => $num) {
            $rowPos[$num] = $idx;
        }
        $colPos = array_fill(0, $k + 1, 0);
        foreach ($colOrder as $idx => $num) {
            $colPos[$num] = $idx;
        }

        // build matrix
        $matrix = array_fill(0, $k, array_fill(0, $k, 0));
        for ($num = 1; $num <= $k; $num++) {
            $r = $rowPos[$num];
            $c = $colPos[$num];
            $matrix[$r][$c] = $num;
        }

        return $matrix;
    }

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]|null
     */
    private function topoSort($n, $edges) {
        $adj = array_fill(0, $n + 1, []);
        $indeg = array_fill(0, $n + 1, 0);

        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $indeg[$b]++;
        }

        $queue = new SplQueue();
        for ($i = 1; $i <= $n; $i++) {
            if ($indeg[$i] == 0) {
                $queue->enqueue($i);
            }
        }

        $order = [];
        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            $order[] = $node;
            foreach ($adj[$node] as $nei) {
                $indeg[$nei]--;
                if ($indeg[$nei] == 0) {
                    $queue->enqueue($nei);
                }
            }
        }

        return count($order) === $n ? $order : [];
    }
}
```

## Swift

```swift
class Solution {
    private func topoSort(_ k: Int, _ conditions: [[Int]]) -> [Int]? {
        var adj = Array(repeating: [Int](), count: k + 1)
        var indeg = Array(repeating: 0, count: k + 1)
        for cond in conditions {
            let a = cond[0]
            let b = cond[1]
            adj[a].append(b)
            indeg[b] += 1
        }
        var queue = [Int]()
        var head = 0
        for i in 1...k where indeg[i] == 0 {
            queue.append(i)
        }
        var order = [Int]()
        while head < queue.count {
            let node = queue[head]
            head += 1
            order.append(node)
            for nb in adj[node] {
                indeg[nb] -= 1
                if indeg[nb] == 0 {
                    queue.append(nb)
                }
            }
        }
        return order.count == k ? order : nil
    }

    func buildMatrix(_ k: Int, _ rowConditions: [[Int]], _ colConditions: [[Int]]) -> [[Int]] {
        guard let rowOrder = topoSort(k, rowConditions),
              let colOrder = topoSort(k, colConditions) else {
            return []
        }
        var rowPos = [Int: Int]()
        for (idx, num) in rowOrder.enumerated() {
            rowPos[num] = idx
        }
        var colPos = [Int: Int]()
        for (idx, num) in colOrder.enumerated() {
            colPos[num] = idx
        }

        var matrix = Array(repeating: Array(repeating: 0, count: k), count: k)
        for num in 1...k {
            if let r = rowPos[num], let c = colPos[num] {
                matrix[r][c] = num
            }
        }
        return matrix
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun buildMatrix(k: Int, rowConditions: Array<IntArray>, colConditions: Array<IntArray>): Array<IntArray> {
        val rowOrder = topoSort(k, rowConditions) ?: return arrayOf()
        val colOrder = topoSort(k, colConditions) ?: return arrayOf()

        val rowPos = IntArray(k + 1)
        val colPos = IntArray(k + 1)

        for (i in 0 until k) {
            rowPos[rowOrder[i]] = i
            colPos[colOrder[i]] = i
        }

        val result = Array(k) { IntArray(k) }
        for (num in 1..k) {
            val r = rowPos[num]
            val c = colPos[num]
            result[r][c] = num
        }
        return result
    }

    private fun topoSort(k: Int, conditions: Array<IntArray>): IntArray? {
        val adj = Array(k + 1) { mutableListOf<Int>() }
        val indeg = IntArray(k + 1)

        for (cond in conditions) {
            val a = cond[0]
            val b = cond[1]
            adj[a].add(b)
            indeg[b]++
        }

        val queue: ArrayDeque<Int> = ArrayDeque()
        for (i in 1..k) {
            if (indeg[i] == 0) queue.add(i)
        }

        val order = IntArray(k)
        var idx = 0
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            order[idx++] = node
            for (nbr in adj[node]) {
                indeg[nbr]--
                if (indeg[nbr] == 0) queue.add(nbr)
            }
        }

        return if (idx == k) order else null
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> buildMatrix(int k, List<List<int>> rowConditions,
      List<List<int>> colConditions) {
    List<int> rowOrder = _topoSort(k, rowConditions);
    List<int> colOrder = _topoSort(k, colConditions);
    if (rowOrder.isEmpty || colOrder.isEmpty) return [];

    // position maps
    List<int> rowPos = List.filled(k + 1, 0);
    for (int i = 0; i < k; i++) {
      rowPos[rowOrder[i]] = i;
    }
    List<int> colPos = List.filled(k + 1, 0);
    for (int i = 0; i < k; i++) {
      colPos[colOrder[i]] = i;
    }

    // build matrix
    List<List<int>> ans =
        List.generate(k, (_) => List.filled(k, 0), growable: false);
    for (int num = 1; num <= k; num++) {
      ans[rowPos[num]][colPos[num]] = num;
    }
    return ans;
  }

  List<int> _topoSort(int n, List<List<int>> edges) {
    List<List<int>> adj = List.generate(n + 1, (_) => []);
    List<int> indeg = List.filled(n + 1, 0);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      adj[a].add(b);
      indeg[b]++;
    }
    List<int> queue = [];
    for (int i = 1; i <= n; i++) {
      if (indeg[i] == 0) queue.add(i);
    }
    List<int> order = [];
    int idx = 0;
    while (idx < queue.length) {
      int node = queue[idx++];
      order.add(node);
      for (int nb in adj[node]) {
        indeg[nb]--;
        if (indeg[nb] == 0) queue.add(nb);
      }
    }
    return order.length == n ? order : [];
  }
}
```

## Golang

```go
func buildMatrix(k int, rowConditions [][]int, colConditions [][]int) [][]int {
    topo := func(edges [][]int) []int {
        adj := make([][]int, k+1)
        indeg := make([]int, k+1)
        for _, e := range edges {
            a, b := e[0], e[1]
            adj[a] = append(adj[a], b)
            indeg[b]++
        }
        q := make([]int, 0, k)
        for i := 1; i <= k; i++ {
            if indeg[i] == 0 {
                q = append(q, i)
            }
        }
        order := make([]int, 0, k)
        for head := 0; head < len(q); head++ {
            node := q[head]
            order = append(order, node)
            for _, nb := range adj[node] {
                indeg[nb]--
                if indeg[nb] == 0 {
                    q = append(q, nb)
                }
            }
        }
        if len(order) != k {
            return nil
        }
        return order
    }

    rowOrder := topo(rowConditions)
    colOrder := topo(colConditions)
    if rowOrder == nil || colOrder == nil {
        return [][]int{}
    }

    rowPos := make([]int, k+1)
    colPos := make([]int, k+1)
    for i, v := range rowOrder {
        rowPos[v] = i
    }
    for i, v := range colOrder {
        colPos[v] = i
    }

    matrix := make([][]int, k)
    for i := 0; i < k; i++ {
        matrix[i] = make([]int, k)
    }
    for v := 1; v <= k; v++ {
        r := rowPos[v]
        c := colPos[v]
        matrix[r][c] = v
    }
    return matrix
}
```

## Ruby

```ruby
def build_matrix(k, row_conditions, col_conditions)
  rows_order = topo_sort(row_conditions, k)
  cols_order = topo_sort(col_conditions, k)
  return [] if rows_order.empty? || cols_order.empty?

  row_pos = {}
  rows_order.each_with_index { |val, idx| row_pos[val] = idx }
  col_pos = {}
  cols_order.each_with_index { |val, idx| col_pos[val] = idx }

  matrix = Array.new(k) { Array.new(k, 0) }
  (1..k).each do |val|
    r = row_pos[val]
    c = col_pos[val]
    matrix[r][c] = val
  end
  matrix
end

def topo_sort(edges, k)
  adj = Array.new(k + 1) { [] }
  indeg = Array.new(k + 1, 0)

  edges.each do |u, v|
    adj[u] << v
    indeg[v] += 1
  end

  queue = []
  (1..k).each { |i| queue << i if indeg[i].zero? }

  order = []
  head = 0
  while head < queue.length
    node = queue[head]
    head += 1
    order << node
    adj[node].each do |nbr|
      indeg[nbr] -= 1
      queue << nbr if indeg[nbr].zero?
    end
  end

  order.size == k ? order : []
end
```

## Scala

```scala
object Solution {
    def buildMatrix(k: Int, rowConditions: Array[Array[Int]], colConditions: Array[Array[Int]]): Array[Array[Int]] = {
        def topoSort(conds: Array[Array[Int]]): Array[Int] = {
            val adj = Array.fill(k + 1)(scala.collection.mutable.ArrayBuffer[Int]())
            val indeg = new Array[Int](k + 1)
            for (c <- conds) {
                val a = c(0)
                val b = c(1)
                adj(a).append(b)
                indeg(b) += 1
            }
            val q = scala.collection.mutable.Queue[Int]()
            for (i <- 1 to k) if (indeg(i) == 0) q.enqueue(i)
            val order = scala.collection.mutable.ArrayBuffer[Int]()
            while (q.nonEmpty) {
                val cur = q.dequeue()
                order.append(cur)
                for (nb <- adj(cur)) {
                    indeg(nb) -= 1
                    if (indeg(nb) == 0) q.enqueue(nb)
                }
            }
            if (order.size != k) Array.empty[Int] else order.toArray
        }

        val rowOrder = topoSort(rowConditions)
        val colOrder = topoSort(colConditions)

        if (rowOrder.isEmpty || colOrder.isEmpty) return Array.empty[Array[Int]]

        val rowPos = new Array[Int](k + 1)
        for (i <- rowOrder.indices) {
            rowPos(rowOrder(i)) = i
        }
        val colPos = new Array[Int](k + 1)
        for (i <- colOrder.indices) {
            colPos(colOrder(i)) = i
        }

        val mat = Array.ofDim[Int](k, k)
        for (v <- 1 to k) {
            mat(rowPos(v))(colPos(v)) = v
        }
        mat
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn build_matrix(k: i32, row_conditions: Vec<Vec<i32>>, col_conditions: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = k as usize;
        // topological sort for rows
        let row_order_opt = Self::topo_sort(n, &row_conditions);
        let col_order_opt = Self::topo_sort(n, &col_conditions);
        if row_order_opt.is_none() || col_order_opt.is_none() {
            return vec![];
        }
        let row_order = row_order_opt.unwrap();
        let col_order = col_order_opt.unwrap();

        // position maps: value -> index
        let mut row_pos = vec![0usize; n + 1];
        let mut col_pos = vec![0usize; n + 1];
        for (idx, &val) in row_order.iter().enumerate() {
            row_pos[val] = idx;
        }
        for (idx, &val) in col_order.iter().enumerate() {
            col_pos[val] = idx;
        }

        let mut matrix = vec![vec![0i32; n]; n];
        for val in 1..=n {
            let r = row_pos[val];
            let c = col_pos[val];
            matrix[r][c] = val as i32;
        }
        matrix
    }

    fn topo_sort(k: usize, edges: &Vec<Vec<i32>>) -> Option<Vec<usize>> {
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); k + 1];
        let mut indeg: Vec<usize> = vec![0; k + 1];

        for e in edges.iter() {
            if e.len() != 2 {
                continue;
            }
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            indeg[b] += 1;
        }

        let mut q: VecDeque<usize> = VecDeque::new();
        for i in 1..=k {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }

        let mut order: Vec<usize> = Vec::with_capacity(k);
        while let Some(u) = q.pop_front() {
            order.push(u);
            for &v in adj[u].iter() {
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    q.push_back(v);
                }
            }
        }

        if order.len() == k { Some(order) } else { None }
    }
}
```

## Racket

```racket
#lang racket

(define (topo-sort edges k)
  (let ([adj   (make-vector (+ k 1) '())]
        [indeg (make-vector (+ k 1) 0)])
    (for ([e edges])
      (let* ((a (first e))
             (b (second e)))
        (vector-set! adj a (cons b (vector-ref adj a)))
        (vector-set! indeg b (+ (vector-ref indeg b) 1))))
    (define q (make-vector (+ k 1) 0))
    (define front 0)
    (define back 0)
    (for ([i (in-range 1 (+ k 1))])
      (when (= (vector-ref indeg i) 0)
        (vector-set! q back i)
        (set! back (+ back 1))))
    (define order '())
    (let loop ()
      (when (< front back)
        (let ((node (vector-ref q front)))
          (set! front (+ front 1))
          (set! order (cons node order))
          (for ([nbr (in-list (vector-ref adj node))])
            (let ((newdeg (- (vector-ref indeg nbr) 1)))
              (vector-set! indeg nbr newdeg)
              (when (= newdeg 0)
                (vector-set! q back nbr)
                (set! back (+ back 1)))))
          (loop))))
    (if (= (length order) k)
        (reverse order)
        '())))

(define/contract (build-matrix k rowConditions colConditions)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let* ([row-order (topo-sort rowConditions k)]
         [col-order (topo-sort colConditions k)])
    (if (or (null? row-order) (null? col-order))
        '()
        (let* ([matrix   (make-vector k (make-vector k 0))]
               [col-pos  (make-vector (+ k 1) -1)])
          ;; column positions
          (for ([idx (in-range k)])
            (let ((val (list-ref col-order idx)))
              (vector-set! col-pos val idx)))
          ;; place numbers according to row and column orders
          (for ([rIdx (in-range k)])
            (let ((val (list-ref row-order rIdx)))
              (let ((cIdx (vector-ref col-pos val)))
                (when (>= cIdx 0)
                  (vector-set! (vector-ref matrix rIdx) cIdx val)))))
          ;; convert to list of lists
          (for/list ([i (in-range k)])
            (vector->list (vector-ref matrix i)))))))
```

## Erlang

```erlang
-spec build_matrix(K :: integer(), RowConditions :: [[integer()]], ColConditions :: [[integer()]]) -> [[integer()]].
build_matrix(K, RowConditions, ColConditions) ->
    RowOrder = topo_sort(K, RowConditions),
    case RowOrder of
        [] -> [];
        _ ->
            ColOrder = topo_sort(K, ColConditions),
            case ColOrder of
                [] -> [];
                _ -> build_from_orders(K, RowOrder, ColOrder)
            end
    end.

%% topological sort using Kahn's algorithm; returns empty list on cycle
-spec topo_sort(integer(), [[integer()]]) -> [integer()].
topo_sort(N, Edges) ->
    Adj0 = maps:from_list([{I, []} || I <- lists:seq(1, N)]),
    Indeg0 = maps:from_list([{I, 0} || I <- lists:seq(1, N)]),
    {Adj, Indeg} = build_graph(Edges, Adj0, Indeg0),
    Queue0 = [V || V <- lists:seq(1, N), maps:get(V, Indeg) =:= 0],
    process_queue(Queue0, Adj, Indeg, []).

build_graph([], Adj, Indeg) -> {Adj, Indeg};
build_graph([[A,B]|Rest], Adj, Indeg) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B|L] end,
            [B],
            Adj),
    Indeg1 = maps:update_with(B,
            fun(V) -> V + 1 end,
            1,
            Indeg),
    build_graph(Rest, Adj1, Indeg1).

process_queue([], _Adj, Indeg, Order) ->
    case length(Order) of
        L when L =:= maps:size(Indeg) -> lists:reverse(Order);
        _ -> []
    end;
process_queue([Node|RestQ], Adj, Indeg, Order) ->
    Neigh = maps:get(Node, Adj),
    {Indeg2, NewZeros} = reduce_neighbors(Neigh, Indeg, []),
    Queue2 = RestQ ++ NewZeros,
    process_queue(Queue2, Adj, Indeg2, [Node|Order]).

reduce_neighbors([], Indeg, Acc) -> {Indeg, lists:reverse(Acc)};
reduce_neighbors([V|Vs], Indeg, Acc) ->
    Cur = maps:get(V, Indeg),
    NewVal = Cur - 1,
    Indeg1 = maps:put(V, NewVal, Indeg),
    Acc1 = if NewVal =:= 0 -> [V|Acc]; true -> Acc end,
    reduce_neighbors(Vs, Indeg1, Acc1).

%% Build matrix from row and column orders
-spec build_from_orders(integer(), [integer()], [integer()]) -> [[integer()]].
build_from_orders(K, RowOrder, ColOrder) ->
    RowPos = maps:from_list(lists:zip(RowOrder, lists:seq(0, K-1))),
    ColPos = maps:from_list(lists:zip(ColOrder, lists:seq(0, K-1))),
    EmptyRows = [lists:duplicate(K, 0) || _ <- lists:seq(1, K)],
    Numbers = lists:seq(1, K),
    lists:foldl(fun(N, AccRows) ->
        R = maps:get(N, RowPos),
        C = maps:get(N, ColPos),
        OldRow = lists:nth(R + 1, AccRows),
        NewRow = set_at(OldRow, C, N),
        update_nth(AccRows, R, NewRow)
    end, EmptyRows, Numbers).

%% Set element at zero‑based index
-spec set_at([integer()], integer(), integer()) -> [integer()].
set_at([_H|T], 0, Val) -> [Val | T];
set_at([H|T], Index, Val) when Index > 0 ->
    [H | set_at(T, Index - 1, Val)].

%% Replace list element at zero‑based index
-spec update_nth([[integer()]], integer(), [integer()]) -> [[integer()]].
update_nth([_H|T], 0, NewElem) -> [NewElem | T];
update_nth([H|T], Index, NewElem) when Index > 0 ->
    [H | update_nth(T, Index - 1, NewElem)].
```

## Elixir

```elixir
defmodule Solution do
  @spec build_matrix(k :: integer, row_conditions :: [[integer]], col_conditions :: [[integer]]) :: [[integer]]
  def build_matrix(k, row_conditions, col_conditions) do
    rows = topo_sort(k, row_conditions)
    cols = topo_sort(k, col_conditions)

    if rows == [] or cols == [] do
      []
    else
      row_pos = Enum.with_index(rows) |> Enum.into(%{}, fn {v, i} -> {v, i} end)
      col_pos = Enum.with_index(cols) |> Enum.into(%{}, fn {v, i} -> {v, i} end)

      empty_row = List.duplicate(0, k)
      matrix = List.duplicate(empty_row, k)

      1..k
      |> Enum.reduce(matrix, fn val, mat ->
        r = Map.fetch!(row_pos, val)
        c = Map.fetch!(col_pos, val)

        updated_row = List.replace_at(Enum.at(mat, r), c, val)
        List.replace_at(mat, r, updated_row)
      end)
    end
  end

  defp topo_sort(k, edges) do
    indeg =
      Enum.reduce(1..k, %{}, fn i, acc -> Map.put(acc, i, 0) end)

    {adj, indeg} =
      Enum.reduce(edges, {%{}, indeg}, fn [a, b], {adj_acc, indeg_acc} ->
        adj_updated = Map.update(adj_acc, a, [b], &[b | &1])
        indeg_updated = Map.update!(indeg_acc, b, &(&1 + 1))
        {adj_updated, indeg_updated}
      end)

    zero_queue =
      :queue.from_list(
        Enum.filter(1..k, fn i -> Map.get(indeg, i) == 0 end)
      )

    order_rev = bfs(zero_queue, adj, indeg, [])

    order = Enum.reverse(order_rev)

    if length(order) == k, do: order, else: []
  end

  defp bfs(queue, adj, indeg, acc) do
    case :queue.out(queue) do
      {:empty, _} ->
        acc

      {{:value, node}, q_rest} ->
        neighbors = Map.get(adj, node, [])

        {indeg_after, q_after} =
          Enum.reduce(neighbors, {indeg, q_rest}, fn nb, {ind_map, q_acc} ->
            new_deg = Map.update!(ind_map, nb, &(&1 - 1))

            if new_deg == 0 do
              {new_deg, :queue.in(nb, q_acc)}
            else
              {new_deg, q_acc}
            end
          end)

        bfs(q_after, adj, indeg_after, [node | acc])
    end
  end
end
```
