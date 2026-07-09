# 0797. All Paths From Source to Target

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<vector<int>> res;
        vector<int> path;
        dfs(0, graph, n - 1, path, res);
        return res;
    }
private:
    void dfs(int node, const vector<vector<int>>& graph, int target,
             vector<int>& path, vector<vector<int>>& res) {
        path.push_back(node);
        if (node == target) {
            res.push_back(path);
        } else {
            for (int nxt : graph[node]) {
                dfs(nxt, graph, target, path, res);
            }
        }
        path.pop_back();
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(0, graph, path, result);
        return result;
    }
    
    private void dfs(int node, int[][] graph, List<Integer> path, List<List<Integer>> result) {
        if (node == graph.length - 1) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int next : graph[node]) {
            path.add(next);
            dfs(next, graph, path, result);
            path.remove(path.size() - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        res = []
        path = [0]

        def dfs(node):
            if node == target:
                res.append(path[:])
                return
            for nxt in graph[node]:
                path.append(nxt)
                dfs(nxt)
                path.pop()

        dfs(0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result: List[List[int]] = []
        path = [0]

        def dfs(node: int):
            if node == target:
                result.append(path.copy())
                return
            for nxt in graph[node]:
                path.append(nxt)
                dfs(nxt)
                path.pop()

        dfs(0)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int **paths;
    int *colSizes;
    int count;
    int capacity;
} Result;

static void addPath(Result *res, int *path, int len) {
    if (res->count == res->capacity) {
        int newCap = res->capacity ? res->capacity * 2 : 4;
        res->paths = realloc(res->paths, newCap * sizeof(int *));
        res->colSizes = realloc(res->colSizes, newCap * sizeof(int));
        res->capacity = newCap;
    }
    int *copy = malloc(len * sizeof(int));
    memcpy(copy, path, len * sizeof(int));
    res->paths[res->count] = copy;
    res->colSizes[res->count] = len;
    res->count++;
}

static void dfs(int node, int target, int **graph, int *graphColSize,
                int *path, int depth, Result *res) {
    if (node == target) {
        addPath(res, path, depth);
        return;
    }
    for (int i = 0; i < graphColSize[node]; ++i) {
        int nxt = graph[node][i];
        path[depth] = nxt;
        dfs(nxt, target, graph, graphColSize, path, depth + 1, res);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** allPathsSourceTarget(int** graph, int graphSize, int* graphColSize,
                           int* returnSize, int** returnColumnSizes) {
    Result res = {NULL, NULL, 0, 0};
    int *path = malloc(graphSize * sizeof(int));
    path[0] = 0;
    dfs(0, graphSize - 1, graph, graphColSize, path, 1, &res);
    free(path);
    *returnSize = res.count;
    *returnColumnSizes = res.colSizes;
    return res.paths;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<IList<int>> AllPathsSourceTarget(int[][] graph)
    {
        var results = new List<IList<int>>();
        var path = new List<int>();
        DFS(0, graph, path, results);
        return results;
    }

    private void DFS(int node, int[][] graph, List<int> path, List<IList<int>> results)
    {
        path.Add(node);
        if (node == graph.Length - 1)
        {
            results.Add(new List<int>(path));
        }
        else
        {
            foreach (int next in graph[node])
            {
                DFS(next, graph, path, results);
            }
        }
        path.RemoveAt(path.Count - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    const target = graph.length - 1;
    const res = [];
    const path = [0];
    
    const dfs = (node) => {
        if (node === target) {
            res.push([...path]);
            return;
        }
        for (const next of graph[node]) {
            path.push(next);
            dfs(next);
            path.pop();
        }
    };
    
    dfs(0);
    return res;
};
```

## Typescript

```typescript
function allPathsSourceTarget(graph: number[][]): number[][] {
    const target = graph.length - 1;
    const result: number[][] = [];
    const path: number[] = [];

    function dfs(node: number) {
        path.push(node);
        if (node === target) {
            result.push([...path]);
        } else {
            for (const next of graph[node]) {
                dfs(next);
            }
        }
        path.pop();
    }

    dfs(0);
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer[][]
     */
    function allPathsSourceTarget($graph) {
        $n = count($graph);
        $target = $n - 1;
        $res = [];
        $path = [0];
        $dfs = function ($node) use (&$dfs, &$graph, &$res, $target, &$path) {
            if ($node === $target) {
                $res[] = $path;
                return;
            }
            foreach ($graph[$node] as $next) {
                $path[] = $next;
                $dfs($next);
                array_pop($path);
            }
        };
        $dfs(0);
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func allPathsSourceTarget(_ graph: [[Int]]) -> [[Int]] {
        let target = graph.count - 1
        var result = [[Int]]()
        var path = [Int]()
        
        func dfs(_ node: Int) {
            path.append(node)
            if node == target {
                result.append(path)
            } else {
                for next in graph[node] {
                    dfs(next)
                }
            }
            path.removeLast()
        }
        
        dfs(0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun allPathsSourceTarget(graph: Array<IntArray>): List<List<Int>> {
        val target = graph.size - 1
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf(0)

        fun dfs(node: Int) {
            if (node == target) {
                result.add(ArrayList(path))
                return
            }
            for (next in graph[node]) {
                path.add(next)
                dfs(next)
                path.removeAt(path.size - 1)
            }
        }

        dfs(0)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> allPathsSourceTarget(List<List<int>> graph) {
    int target = graph.length - 1;
    List<List<int>> result = [];
    List<int> path = [];

    void dfs(int node) {
      path.add(node);
      if (node == target) {
        result.add(List<int>.from(path));
      } else {
        for (int next in graph[node]) {
          dfs(next);
        }
      }
      path.removeLast();
    }

    dfs(0);
    return result;
  }
}
```

## Golang

```go
func allPathsSourceTarget(graph [][]int) [][]int {
	var res [][]int
	n := len(graph)
	var dfs func(int, []int)
	dfs = func(node int, path []int) {
		if node == n-1 {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		for _, nxt := range graph[node] {
			dfs(nxt, append(path, nxt))
		}
	}
	dfs(0, []int{0})
	return res
}
```

## Ruby

```ruby
def all_paths_source_target(graph)
  target = graph.length - 1
  results = []
  path = [0]

  dfs = lambda do |node|
    if node == target
      results << path.clone
      next
    end

    graph[node].each do |next_node|
      path << next_node
      dfs.call(next_node)
      path.pop
    end
  end

  dfs.call(0)
  results
end
```

## Scala

```scala
object Solution {
    def allPathsSourceTarget(graph: Array[Array[Int]]): List[List[Int]] = {
        val target = graph.length - 1
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val path = scala.collection.mutable.ArrayBuffer[Int](0)

        def dfs(node: Int): Unit = {
            if (node == target) {
                result += path.toList
                return
            }
            for (next <- graph(node)) {
                path.append(next)
                dfs(next)
                path.remove(path.size - 1)
            }
        }

        dfs(0)
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = graph.len();
        let target = n - 1;
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut path: Vec<i32> = vec![0];
        fn dfs(
            node: usize,
            target: usize,
            graph: &Vec<Vec<i32>>,
            path: &mut Vec<i32>,
            res: &mut Vec<Vec<i32>>,
        ) {
            if node == target {
                res.push(path.clone());
                return;
            }
            for &next_i in &graph[node] {
                let next = next_i as usize;
                path.push(next_i);
                dfs(next, target, graph, path, res);
                path.pop();
            }
        }
        dfs(0, target, &graph, &mut path, &mut res);
        res
    }
}
```

## Racket

```racket
(define/contract (all-paths-source-target graph)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((n (length graph))
         (target (- n 1)))
    (letrec ((dfs
              (lambda (node path)
                (let ((new-path (append path (list node))))
                  (if (= node target)
                      (list new-path)
                      (apply append
                             (map (lambda (next) (dfs next new-path))
                                  (list-ref graph node))))))))
      (dfs 0 '()))))
```

## Erlang

```erlang
-module(solution).
-export([all_paths_source_target/1]).

-spec all_paths_source_target(Graph :: [[integer()]]) -> [[integer()]].
all_paths_source_target(Graph) ->
    Target = length(Graph) - 1,
    dfs(0, Graph, Target, [0]).

dfs(Node, _Graph, Node, Acc) ->
    [[lists:reverse(Acc)]];
dfs(Node, Graph, Target, Acc) ->
    Adj = lists:nth(Node + 1, Graph),
    lists:foldl(fun(Next, Paths) ->
        Paths ++ dfs(Next, Graph, Target, [Next | Acc])
    end, [], Adj).
```

## Elixir

```elixir
defmodule Solution do
  @spec all_paths_source_target(graph :: [[integer]]) :: [[integer]]
  def all_paths_source_target(graph) do
    target = length(graph) - 1
    dfs(0, graph, target)
  end

  defp dfs(node, _graph, target) when node == target do
    [[target]]
  end

  defp dfs(node, graph, target) do
    graph[node]
    |> Enum.flat_map(fn nxt ->
      dfs(nxt, graph, target)
      |> Enum.map(&([node | &1]))
    end)
  end
end
```
