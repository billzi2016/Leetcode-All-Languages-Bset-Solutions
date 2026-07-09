# 0399. Evaluate Division

## Cpp

```cpp
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string,int> idx;
        int n = 0;
        for (auto& eq : equations) {
            if (!idx.count(eq[0])) idx[eq[0]] = n++;
            if (!idx.count(eq[1])) idx[eq[1]] = n++;
        }
        vector<int> parent(n);
        vector<double> weight(n, 1.0);
        for (int i = 0; i < n; ++i) parent[i] = i;
        
        function<int(int)> find = [&](int x) -> int {
            if (parent[x] == x) return x;
            int p = parent[x];
            int root = find(p);
            weight[x] *= weight[p];
            parent[x] = root;
            return root;
        };
        
        auto unite = [&](int a, int b, double value) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            // set parent of ra to rb
            // weight[ra] = value * weight[b] / weight[a]
            weight[ra] = value * weight[b] / weight[a];
            parent[ra] = rb;
        };
        
        for (size_t i = 0; i < equations.size(); ++i) {
            int a = idx[equations[i][0]];
            int b = idx[equations[i][1]];
            unite(a, b, values[i]);
        }
        
        vector<double> ans;
        for (auto& q : queries) {
            if (!idx.count(q[0]) || !idx.count(q[1])) {
                ans.push_back(-1.0);
                continue;
            }
            int a = idx[q[0]];
            int b = idx[q[1]];
            int ra = find(a);
            int rb = find(b);
            if (ra != rb) {
                ans.push_back(-1.0);
            } else {
                ans.push_back(weight[a] / weight[b]);
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Integer> idMap = new HashMap<>();
        int idx = 0;
        for (List<String> eq : equations) {
            String a = eq.get(0);
            String b = eq.get(1);
            if (!idMap.containsKey(a)) idMap.put(a, idx++);
            if (!idMap.containsKey(b)) idMap.put(b, idx++);
        }
        UnionFind uf = new UnionFind(idx);
        for (int i = 0; i < equations.size(); i++) {
            List<String> eq = equations.get(i);
            int a = idMap.get(eq.get(0));
            int b = idMap.get(eq.get(1));
            uf.union(a, b, values[i]);
        }
        double[] ans = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            List<String> q = queries.get(i);
            String c = q.get(0), d = q.get(1);
            if (!idMap.containsKey(c) || !idMap.containsKey(d)) {
                ans[i] = -1.0;
            } else {
                int a = idMap.get(c);
                int b = idMap.get(d);
                ans[i] = uf.getRatio(a, b);
            }
        }
        return ans;
    }

    private static class UnionFind {
        int[] parent;
        double[] weight; // weight[x] = x / parent[x]

        UnionFind(int n) {
            parent = new int[n];
            weight = new double[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                weight[i] = 1.0;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                int origParent = parent[x];
                int root = find(origParent);
                weight[x] *= weight[origParent];
                parent[x] = root;
            }
            return parent[x];
        }

        void union(int a, int b, double value) { // a / b = value
            int rootA = find(a);
            int rootB = find(b);
            if (rootA == rootB) return;
            // weight[a] = a / rootA, weight[b] = b / rootB
            // need to set parent[rootA] = rootB and adjust weight[rootA]
            double ratio = value * weight[b] / weight[a];
            parent[rootA] = rootB;
            weight[rootA] = ratio;
        }

        double getRatio(int a, int b) {
            if (find(a) != find(b)) return -1.0;
            // after find, weight[x] = x / root
            return weight[a] / weight[b];
        }
    }
}
```

## Python

```python
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        parent = {}
        weight = {}

        def find(x):
            if parent[x] != x:
                orig_parent = parent[x]
                root = find(orig_parent)
                weight[x] *= weight[orig_parent]
                parent[x] = root
            return parent[x]

        def union(x, y, val):
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
            if y not in parent:
                parent[y] = y
                weight[y] = 1.0
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            # set root_x's parent to root_y and adjust weight
            ratio = val * weight[y] / weight[x]
            parent[root_x] = root_y
            weight[root_x] = ratio

        for (a, b), v in zip(equations, values):
            union(a, b, v)

        res = []
        for a, b in queries:
            if a not in parent or b not in parent:
                res.append(-1.0)
                continue
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                res.append(-1.0)
            else:
                res.append(weight[a] / weight[b])
        return res
```

## Python3

```python
from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1.0 / v))

        def bfs(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited = {src}
            q = deque([(src, 1.0)])
            while q:
                node, prod = q.popleft()
                for nei, w in graph[node]:
                    if nei in visited:
                        continue
                    cur = prod * w
                    if nei == dst:
                        return cur
                    visited.add(nei)
                    q.append((nei, cur))
            return -1.0

        return [bfs(a, b) for a, b in queries]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAXN 100

static int getOrAdd(const char *s, char **vars, int *cnt) {
    for (int i = 0; i < *cnt; ++i) {
        if (strcmp(vars[i], s) == 0) return i;
    }
    vars[*cnt] = (char *)malloc(strlen(s) + 1);
    strcpy(vars[*cnt], s);
    (*cnt)++;
    return *cnt - 1;
}

static bool dfs(int src, int dst, double cur, bool *vis, double graph[][MAXN], int n, double *res) {
    if (src == dst) {
        *res = cur;
        return true;
    }
    vis[src] = true;
    for (int i = 0; i < n; ++i) {
        if (!vis[i] && graph[src][i] > 0.0) {
            if (dfs(i, dst, cur * graph[src][i], vis, graph, n, res)) return true;
        }
    }
    return false;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* calcEquation(char*** equations, int equationsSize, int* equationsColSize,
                     double* values, int valuesSize,
                     char*** queries, int queriesSize, int* queriesColSize,
                     int* returnSize) {
    char *vars[MAXN];
    int varCnt = 0;
    double graph[MAXN][MAXN];
    for (int i = 0; i < MAXN; ++i)
        for (int j = 0; j < MAXN; ++j)
            graph[i][j] = -1.0;

    // Build graph from equations
    for (int i = 0; i < equationsSize; ++i) {
        char *a = equations[i][0];
        char *b = equations[i][1];
        int idA = getOrAdd(a, vars, &varCnt);
        int idB = getOrAdd(b, vars, &varCnt);
        double v = values[i];
        graph[idA][idB] = v;
        graph[idB][idA] = 1.0 / v;
    }

    double *ans = (double *)malloc(sizeof(double) * queriesSize);
    *returnSize = queriesSize;

    for (int i = 0; i < queriesSize; ++i) {
        char *c = queries[i][0];
        char *d = queries[i][1];
        int idC = -1, idD = -1;
        for (int j = 0; j < varCnt; ++j) {
            if (strcmp(vars[j], c) == 0) idC = j;
            if (strcmp(vars[j], d) == 0) idD = j;
        }
        if (idC == -1 || idD == -1) {
            ans[i] = -1.0;
            continue;
        }
        bool visited[MAXN] = {false};
        double result = -1.0;
        if (!dfs(idC, idD, 1.0, visited, graph, varCnt, &result))
            result = -1.0;
        ans[i] = result;
    }

    // free variable strings
    for (int i = 0; i < varCnt; ++i) {
        free(vars[i]);
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries) {
        var index = new Dictionary<string, int>();
        int id = 0;
        foreach (var eq in equations) {
            string a = eq[0], b = eq[1];
            if (!index.ContainsKey(a)) index[a] = id++;
            if (!index.ContainsKey(b)) index[b] = id++;
        }

        int n = id;
        var parent = new int[n];
        var weight = new double[n]; // weight[x] = x / parent[x]
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            weight[i] = 1.0;
        }

        int Find(int x) {
            if (parent[x] != x) {
                int p = parent[x];
                int root = Find(p);
                weight[x] *= weight[p];
                parent[x] = root;
            }
            return parent[x];
        }

        void Union(int aIdx, int bIdx, double value) {
            int rootA = Find(aIdx);
            int rootB = Find(bIdx);
            if (rootA == rootB) return;

            // weight[aIdx] = a / rootA, weight[bIdx] = b / rootB
            double ratio = value * weight[bIdx] / weight[aIdx]; // rootA / rootB
            parent[rootA] = rootB;
            weight[rootA] = ratio; // rootA / rootB
        }

        for (int i = 0; i < equations.Count; i++) {
            var eq = equations[i];
            int aIdx = index[eq[0]];
            int bIdx = index[eq[1]];
            Union(aIdx, bIdx, values[i]);
        }

        double[] answer = new double[queries.Count];
        for (int i = 0; i < queries.Count; i++) {
            var q = queries[i];
            string c = q[0], d = q[1];
            if (!index.ContainsKey(c) || !index.ContainsKey(d)) {
                answer[i] = -1.0;
                continue;
            }
            int cIdx = index[c];
            int dIdx = index[d];
            int rootC = Find(cIdx);
            int rootD = Find(dIdx);
            if (rootC != rootD) {
                answer[i] = -1.0;
            } else {
                answer[i] = weight[cIdx] / weight[dIdx];
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    const indexMap = new Map();
    let idx = 0;
    // assign indices to variables
    for (const [a, b] of equations) {
        if (!indexMap.has(a)) indexMap.set(a, idx++);
        if (!indexMap.has(b)) indexMap.set(b, idx++);
    }
    const parent = new Array(idx);
    const weight = new Array(idx).fill(1.0); // weight[x] = x / parent[x]
    for (let i = 0; i < idx; i++) {
        parent[i] = i;
    }

    function find(x) {
        if (parent[x] !== x) {
            const origParent = parent[x];
            const root = find(origParent);
            weight[x] *= weight[origParent]; // x/root = (x/origParent)*(origParent/root)
            parent[x] = root;
        }
        return parent[x];
    }

    function union(x, y, value) {
        const rootX = find(x);
        const rootY = find(y);
        if (rootX === rootY) return;
        // weight[x] = x / rootX, weight[y] = y / rootY
        // we need to set parent[rootX] = rootY and weight[rootX] = (value * weight[y]) / weight[x]
        const ratio = value * weight[y] / weight[x];
        parent[rootX] = rootY;
        weight[rootX] = ratio; // rootX / rootY
    }

    // build union-find structure
    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i];
        const val = values[i];
        const idxA = indexMap.get(a);
        const idxB = indexMap.get(b);
        union(idxA, idxB, val);
    }

    const result = [];
    for (const [c, d] of queries) {
        if (!indexMap.has(c) || !indexMap.has(d)) {
            result.push(-1.0);
            continue;
        }
        const idxC = indexMap.get(c);
        const idxD = indexMap.get(d);
        const rootC = find(idxC);
        const rootD = find(idxD);
        if (rootC !== rootD) {
            result.push(-1.0);
        } else {
            // c/d = (c/root) / (d/root) = weight[c] / weight[d]
            result.push(weight[idxC] / weight[idxD]);
        }
    }
    return result;
};
```

## Typescript

```typescript
function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    const graph = new Map<string, Array<[string, number]>>();
    for (let i = 0; i < equations.length; i++) {
        const [a, b] = equations[i];
        const v = values[i];
        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);
        graph.get(a)!.push([b, v]);
        graph.get(b)!.push([a, 1 / v]);
    }

    const res: number[] = [];
    for (const [src, dst] of queries) {
        if (!graph.has(src) || !graph.has(dst)) {
            res.push(-1.0);
            continue;
        }
        if (src === dst) {
            res.push(1.0);
            continue;
        }

        const visited = new Set<string>();
        const queue: Array<[string, number]> = [[src, 1]];
        visited.add(src);
        let ans = -1.0;

        while (queue.length) {
            const [node, prod] = queue.shift()!;
            if (node === dst) {
                ans = prod;
                break;
            }
            for (const [nei, w] of graph.get(node)!) {
                if (!visited.has(nei)) {
                    visited.add(nei);
                    queue.push([nei, prod * w]);
                }
            }
        }

        res.push(ans);
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $equations
     * @param Float[] $values
     * @param String[][] $queries
     * @return Float[]
     */
    function calcEquation($equations, $values, $queries) {
        $graph = [];

        foreach ($equations as $i => $pair) {
            $a = $pair[0];
            $b = $pair[1];
            $val = $values[$i];

            if (!isset($graph[$a])) {
                $graph[$a] = [];
            }
            if (!isset($graph[$b])) {
                $graph[$b] = [];
            }

            $graph[$a][$b] = $val;
            $graph[$b][$a] = 1.0 / $val;
        }

        $result = [];

        foreach ($queries as $q) {
            $src = $q[0];
            $dst = $q[1];

            if (!isset($graph[$src]) || !isset($graph[$dst])) {
                $result[] = -1.0;
                continue;
            }

            if ($src === $dst) {
                $result[] = 1.0;
                continue;
            }

            $queue = new SplQueue();
            $queue->enqueue([$src, 1.0]);
            $visited = [$src => true];
            $answer = -1.0;

            while (!$queue->isEmpty()) {
                list($node, $prod) = $queue->dequeue();

                if ($node === $dst) {
                    $answer = $prod;
                    break;
                }

                foreach ($graph[$node] as $neighbor => $weight) {
                    if (!isset($visited[$neighbor])) {
                        $visited[$neighbor] = true;
                        $queue->enqueue([$neighbor, $prod * $weight]);
                    }
                }
            }

            $result[] = $answer;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func calcEquation(_ equations: [[String]], _ values: [Double], _ queries: [[String]]) -> [Double] {
        var graph = [String: [(String, Double)]]()
        
        for i in 0..<equations.count {
            let a = equations[i][0]
            let b = equations[i][1]
            let val = values[i]
            graph[a, default: []].append((b, val))
            graph[b, default: []].append((a, 1.0 / val))
        }
        
        func dfs(_ current: String, _ target: String, _ acc: Double, _ visited: inout Set<String>) -> Double? {
            if current == target { return acc }
            visited.insert(current)
            guard let neighbors = graph[current] else { return nil }
            for (next, weight) in neighbors {
                if visited.contains(next) { continue }
                if let result = dfs(next, target, acc * weight, &visited) {
                    return result
                }
            }
            return nil
        }
        
        var results = [Double]()
        for q in queries {
            let src = q[0]
            let dst = q[1]
            if graph[src] == nil || graph[dst] == nil {
                results.append(-1.0)
            } else if src == dst {
                results.append(1.0)
            } else {
                var visited = Set<String>()
                if let value = dfs(src, dst, 1.0, &visited) {
                    results.append(value)
                } else {
                    results.append(-1.0)
                }
            }
        }
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calcEquation(
        equations: List<List<String>>,
        values: DoubleArray,
        queries: List<List<String>>
    ): DoubleArray {
        val idMap = HashMap<String, Int>()
        var idx = 0
        for (eq in equations) {
            for (v in eq) {
                if (!idMap.containsKey(v)) {
                    idMap[v] = idx++
                }
            }
        }

        val parent = IntArray(idx) { it }
        val weight = DoubleArray(idx) { 1.0 }

        fun find(x: Int): Int {
            if (parent[x] != x) {
                val origParent = parent[x]
                parent[x] = find(origParent)
                weight[x] *= weight[origParent]
            }
            return parent[x]
        }

        fun union(a: Int, b: Int, value: Double) {
            val rootA = find(a)
            val rootB = find(b)
            if (rootA == rootB) return
            // Set rootA's parent to rootB and adjust weight
            parent[rootA] = rootB
            weight[rootA] = value * weight[b] / weight[a]
        }

        for (i in equations.indices) {
            val a = equations[i][0]
            val b = equations[i][1]
            val idA = idMap[a]!!
            val idB = idMap[b]!!
            union(idA, idB, values[i])
        }

        val result = DoubleArray(queries.size)
        for (i in queries.indices) {
            val a = queries[i][0]
            val b = queries[i][1]
            if (!idMap.containsKey(a) || !idMap.containsKey(b)) {
                result[i] = -1.0
                continue
            }
            val idA = idMap[a]!!
            val idB = idMap[b]!!
            val rootA = find(idA)
            val rootB = find(idB)
            if (rootA != rootB) {
                result[i] = -1.0
            } else {
                result[i] = weight[idA] / weight[idB]
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  List<double> calcEquation(
      List<List<String>> equations, List<double> values, List<List<String>> queries) {
    // Map each variable to a unique id
    final Map<String, int> id = {};
    int idx = 0;
    for (var eq in equations) {
      for (var v in eq) {
        if (!id.containsKey(v)) {
          id[v] = idx++;
        }
      }
    }

    // Union-Find structures
    final List<int> parent = List.filled(idx, 0);
    final List<double> weight = List.filled(idx, 1.0); // weight[x] = x / parent[x]
    for (int i = 0; i < idx; ++i) {
      parent[i] = i;
    }

    int find(int x) {
      if (parent[x] != x) {
        final int origParent = parent[x];
        final int root = find(origParent);
        weight[x] *= weight[origParent];
        parent[x] = root;
      }
      return parent[x];
    }

    void union(String a, String b, double value) {
      final int ia = id[a]!;
      final int ib = id[b]!;
      final int ra = find(ia);
      final int rb = find(ib);
      if (ra == rb) return;
      // weight[ia] = a / ra, weight[ib] = b / rb
      // Need to set parent[ra] = rb and maintain ratio: a/b = value
      final double ratio = value * weight[ib] / weight[ia];
      parent[ra] = rb;
      weight[ra] = ratio; // now ra / rb = ratio
    }

    for (int i = 0; i < equations.length; ++i) {
      union(equations[i][0], equations[i][1], values[i]);
    }

    final List<double> result = [];
    for (var q in queries) {
      final String a = q[0];
      final String b = q[1];
      if (!id.containsKey(a) || !id.containsKey(b)) {
        result.add(-1.0);
        continue;
      }
      final int ia = id[a]!;
      final int ib = id[b]!;
      final int ra = find(ia);
      final int rb = find(ib);
      if (ra != rb) {
        result.add(-1.0);
      } else {
        result.add(weight[ia] / weight[ib]);
      }
    }

    return result;
  }
}
```

## Golang

```go
type Edge struct {
	to     string
	weight float64
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	graph := make(map[string][]Edge)

	for i, eq := range equations {
		a, b := eq[0], eq[1]
		val := values[i]

		graph[a] = append(graph[a], Edge{to: b, weight: val})
		graph[b] = append(graph[b], Edge{to: a, weight: 1.0 / val})
	}

	results := make([]float64, len(queries))
	for i, q := range queries {
		start, end := q[0], q[1]

		if _, ok := graph[start]; !ok {
			results[i] = -1.0
			continue
		}
		if _, ok := graph[end]; !ok {
			results[i] = -1.0
			continue
		}
		if start == end {
			results[i] = 1.0
			continue
		}

		results[i] = bfs(start, end, graph)
	}
	return results
}

func bfs(start, end string, graph map[string][]Edge) float64 {
	type Node struct {
		name string
		prod float64
	}
	queue := []Node{{name: start, prod: 1.0}}
	visited := make(map[string]bool)
	visited[start] = true

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.name == end {
			return cur.prod
		}
		for _, e := range graph[cur.name] {
			if !visited[e.to] {
				visited[e.to] = true
				queue = append(queue, Node{name: e.to, prod: cur.prod * e.weight})
			}
		}
	}
	return -1.0
}
```

## Ruby

```ruby
def calc_equation(equations, values, queries)
  graph = Hash.new { |h, k| h[k] = [] }
  equations.each_with_index do |(a, b), i|
    v = values[i]
    graph[a] << [b, v]
    graph[b] << [a, 1.0 / v]
  end

  dfs = lambda do |src, dst|
    return nil unless graph.key?(src) && graph.key?(dst)
    stack = [[src, 1.0]]
    visited = {}
    until stack.empty?
      node, prod = stack.pop
      return prod if node == dst
      next if visited[node]
      visited[node] = true
      graph[node].each do |nbr, w|
        stack << [nbr, prod * w] unless visited[nbr]
      end
    end
    nil
  end

  queries.map do |c, d|
    if !graph.key?(c) || !graph.key?(d)
      -1.0
    elsif c == d
      1.0
    else
      res = dfs.call(c, d)
      res ? res : -1.0
    end
  end
end
```

## Scala

```scala
object Solution {
  def calcEquation(equations: List[List[String]], values: Array[Double], queries: List[List[String]]): Array[Double] = {
    val graph = scala.collection.mutable.Map[String, List[(String, Double)]]().withDefaultValue(Nil)

    for (i <- equations.indices) {
      val a = equations(i)(0)
      val b = equations(i)(1)
      val v = values(i)
      graph(a) = (b, v) :: graph(a)
      graph(b) = (a, 1.0 / v) :: graph(b)
    }

    def dfs(cur: String, target: String, visited: Set[String]): Double = {
      if (cur == target) return 1.0
      for ((next, weight) <- graph(cur)) {
        if (!visited.contains(next)) {
          val sub = dfs(next, target, visited + cur)
          if (sub != -1.0) return sub * weight
        }
      }
      -1.0
    }

    queries.map { q =>
      val src = q(0)
      val dst = q(1)
      if (!graph.contains(src) || !graph.contains(dst)) -1.0
      else dfs(src, dst, Set.empty)
    }.toArray
  }
}
```

## Rust

```rust
use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn calc_equation(equations: Vec<Vec<String>>, values: Vec<f64>, queries: Vec<Vec<String>>) -> Vec<f64> {
        // Assign an index to each variable
        let mut id: HashMap<String, usize> = HashMap::new();
        let mut idx: usize = 0;
        for eq in &equations {
            for var in eq {
                if !id.contains_key(var) {
                    id.insert(var.clone(), idx);
                    idx += 1;
                }
            }
        }

        // Build adjacency list with weights
        let n = idx;
        let mut graph: Vec<Vec<(usize, f64)>> = vec![Vec::new(); n];
        for (eq, &val) in equations.iter().zip(values.iter()) {
            let a = &eq[0];
            let b = &eq[1];
            let i = id[a];
            let j = id[b];
            graph[i].push((j, val));
            graph[j].push((i, 1.0 / val));
        }

        // Process each query
        let mut results: Vec<f64> = Vec::with_capacity(queries.len());
        for q in queries {
            if q[0] == q[1] && id.contains_key(&q[0]) {
                results.push(1.0);
                continue;
            }
            let start_opt = id.get(&q[0]);
            let end_opt = id.get(&q[1]);
            if start_opt.is_none() || end_opt.is_none() {
                results.push(-1.0);
                continue;
            }
            let start = *start_opt.unwrap();
            let target = *end_opt.unwrap();

            // BFS to find product along a path
            let mut visited = vec![false; n];
            let mut queue: VecDeque<(usize, f64)> = VecDeque::new();
            visited[start] = true;
            queue.push_back((start, 1.0));
            let mut answer = -1.0;

            while let Some((node, prod)) = queue.pop_front() {
                if node == target {
                    answer = prod;
                    break;
                }
                for &(nei, weight) in &graph[node] {
                    if !visited[nei] {
                        visited[nei] = true;
                        queue.push_back((nei, prod * weight));
                    }
                }
            }

            results.push(answer);
        }

        results
    }
}
```

## Racket

```racket
(define/contract (calc-equation equations values queries)
  (-> (listof (listof string?)) (listof flonum?) (listof (listof string?)) (listof flonum?))
  (let ((graph (make-hash)))
    ;; build adjacency list
    (for ([eq equations] [val values])
      (match-define (list a b) eq)
      (hash-update! graph a (lambda (lst) (cons (cons b val) lst)) '())
      (hash-update! graph b (lambda (lst) (cons (cons a (/ 1.0 val)) lst)) '()))
    ;; depth‑first search returning product or #f if unreachable
    (define (dfs cur target visited prod)
      (if (string=? cur target)
          prod
          (let loop ((nbrs (hash-ref graph cur)))
            (cond
              [(null? nbrs) #f]
              [else
               (define nb (car nbrs))
               (define nxt (car nb))
               (define w   (cdr nb))
               (if (member nxt visited)
                   (loop (cdr nbrs))
                   (let ((res (dfs nxt target (cons nxt visited) (* prod w))))
                     (if res
                         res
                         (loop (cdr nbrs)))))]))))
    ;; answer each query
    (map (lambda (q)
           (match-define (list a b) q)
           (cond
             [(not (and (hash-has-key? graph a) (hash-has-key? graph b))) -1.0]
             [(string=? a b) 1.0]
             [else
              (let ((ans (dfs a b (list a) 1.0)))
                (if ans ans -1.0))]))
         queries)))
```

## Erlang

```erlang
-module(solution).
-export([calc_equation/3]).

-spec calc_equation(Equations :: [[unicode:unicode_binary()]],
                    Values :: [float()],
                    Queries :: [[unicode:unicode_binary()]]) -> [float()].
calc_equation(Equations, Values, Queries) ->
    Graph = build_graph(Equations, Values, #{}),
    lists:map(fun(Q) -> eval_query(Q, Graph) end, Queries).

%% Build adjacency map: #{Var => [{Neighbor,Weight}...]}
build_graph([], [], G) -> G;
build_graph([[A,B]|RestEqs], [V|RestVals], G) ->
    G1 = add_edge(G, A, B, V),
    G2 = add_edge(G1, B, A, 1.0 / V),
    build_graph(RestEqs, RestVals, G2).

add_edge(G, From, To, Weight) ->
    case maps:find(From, G) of
        {ok, List} -> maps:put(From, [{To,Weight}|List], G);
        error      -> maps:put(From, [{To,Weight}], G)
    end.

eval_query([C,D], Graph) ->
    case {maps:is_key(C, Graph), maps:is_key(D, Graph)} of
        {false,_} -> -1.0;
        {_,false} -> -1.0;
        {true,true} ->
            if C =:= D -> 1.0;
               true   -> bfs(C, D, Graph)
            end
    end.

bfs(Start, Target, Graph) ->
    bfs_queue([{Start,1.0}], #{}, Target, Graph).

bfs_queue([], _Visited, _Target, _Graph) ->
    -1.0;
bfs_queue([{Node,Prod}|RestQueue], Visited, Target, Graph) ->
    case maps:is_key(Node, Visited) of
        true ->
            bfs_queue(RestQueue, Visited, Target, Graph);
        false ->
            NewVisited = maps:put(Node, true, Visited),
            if Node =:= Target ->
                    Prod;
               true ->
                    Neighbors = maps:get(Node, Graph, []),
                    Next = [{N,Prod*W} || {N,W} <- Neighbors],
                    bfs_queue(RestQueue ++ Next, NewVisited, Target, Graph)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec calc_equation(equations :: [[String.t]], values :: [float], queries :: [[String.t]]) :: [float]
  def calc_equation(equations, values, queries) do
    graph = build_graph(equations, values)

    Enum.map(queries, fn [src, dst] ->
      cond do
        not Map.has_key?(graph, src) or not Map.has_key?(graph, dst) -> -1.0
        src == dst -> 1.0
        true ->
          case dfs(graph, src, dst, MapSet.new([src])) do
            {:ok, val} -> val
            :error -> -1.0
          end
      end
    end)
  end

  defp build_graph(equations, values) do
    Enum.reduce(Enum.zip(equations, values), %{}, fn { [a, b], v }, acc ->
      acc
      |> Map.update(a, [{b, v}], fn list -> [{b, v} | list] end)
      |> Map.update(b, [{a, 1.0 / v}], fn list -> [{a, 1.0 / v} | list] end)
    end)
  end

  defp dfs(_graph, current, target, _visited) when current == target do
    {:ok, 1.0}
  end

  defp dfs(graph, current, target, visited) do
    neighbors = Map.get(graph, current, [])

    Enum.reduce_while(neighbors, :error, fn {nbr, weight}, _acc ->
      if MapSet.member?(visited, nbr) do
        {:cont, :error}
      else
        case dfs(graph, nbr, target, MapSet.put(visited, nbr)) do
          {:ok, val} -> {:halt, {:ok, val * weight}}
          :error -> {:cont, :error}
        end
      end
    end)
  end
end
```
