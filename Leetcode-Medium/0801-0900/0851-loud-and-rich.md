# 0851. Loud and Rich

## Cpp

```cpp
class Solution {
public:
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int n = quiet.size();
        vector<vector<int>> g(n);
        for (auto& r : richer) {
            int a = r[0], b = r[1];
            g[b].push_back(a); // edge from poorer to richer
        }
        vector<int> ans(n, -1);
        function<int(int)> dfs = [&](int x) -> int {
            if (ans[x] != -1) return ans[x];
            int best = x;
            for (int y : g[x]) {
                int cand = dfs(y);
                if (quiet[cand] < quiet[best]) best = cand;
            }
            ans[x] = best;
            return best;
        };
        for (int i = 0; i < n; ++i) dfs(i);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private List<Integer>[] graph;
    private int[] quiet;
    private int[] memo;

    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        this.quiet = quiet;
        memo = new int[n];
        Arrays.fill(memo, -1);
        graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        // edge from poorer to richer
        for (int[] r : richer) {
            int richerPerson = r[0];
            int poorerPerson = r[1];
            graph[poorerPerson].add(richerPerson);
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = dfs(i);
        }
        return answer;
    }

    private int dfs(int person) {
        if (memo[person] != -1) {
            return memo[person];
        }
        int best = person;
        for (int richer : graph[person]) {
            int candidate = dfs(richer);
            if (quiet[candidate] < quiet[best]) {
                best = candidate;
            }
        }
        memo[person] = best;
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            # edge from poorer (b) to richer (a)
            graph[b].append(a)

        ans = [-1] * n

        def dfs(x):
            if ans[x] != -1:
                return ans[x]
            best = x
            for y in graph[x]:
                cand = dfs(y)
                if quiet[cand] < quiet[best]:
                    best = cand
            ans[x] = best
            return best

        for i in range(n):
            dfs(i)

        return ans
```

## Python3

```python
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)  # edge from poorer to richer

        ans = [-1] * n

        def dfs(x: int) -> int:
            if ans[x] != -1:
                return ans[x]
            best = x
            for y in graph[x]:
                cand = dfs(y)
                if quiet[cand] < quiet[best]:
                    best = cand
            ans[x] = best
            return best

        for i in range(n):
            dfs(i)

        return ans
```

## C

```c
#include <stdlib.h>

/* Global variables for DFS */
static int n;
static int *gQuiet;
static int **gAdj;
static int *gDeg;
static int *gMemo;

/* Depth‑first search with memoization */
static int dfs(int u) {
    if (gMemo[u] != -1) return gMemo[u];
    int best = u;
    for (int i = 0; i < gDeg[u]; ++i) {
        int v = gAdj[u][i];
        int cand = dfs(v);
        if (gQuiet[cand] < gQuiet[best]) best = cand;
    }
    gMemo[u] = best;
    return best;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* loudAndRich(int** richer, int richerSize, int* richerColSize,
                 int* quiet, int quietSize, int* returnSize) {
    n = quietSize;
    gQuiet = quiet;

    /* Count outgoing edges (poorer -> richer) */
    int *outCnt = calloc(n, sizeof(int));
    for (int i = 0; i < richerSize; ++i) {
        int a = richer[i][0];
        int b = richer[i][1];
        outCnt[b]++;               /* edge b -> a */
    }

    /* Allocate adjacency lists */
    gAdj = malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        if (outCnt[i] > 0)
            gAdj[i] = malloc(outCnt[i] * sizeof(int));
        else
            gAdj[i] = NULL;
    }
    gDeg = outCnt;   /* reuse the count array as degree info */

    /* Fill adjacency lists */
    int *cur = calloc(n, sizeof(int));
    for (int i = 0; i < richerSize; ++i) {
        int a = richer[i][0];
        int b = richer[i][1];
        gAdj[b][cur[b]++] = a;
    }
    free(cur);

    /* Memoization array */
    gMemo = malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) gMemo[i] = -1;

    int *answer = malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        answer[i] = dfs(i);
    }

    *returnSize = n;
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] LoudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var pair in richer) {
            int a = pair[0], b = pair[1];
            graph[b].Add(a); // edge from poorer to richer
        }

        int[] answer = new int[n];
        Array.Fill(answer, -1);

        int Dfs(int person) {
            if (answer[person] != -1) return answer[person];
            int best = person;
            foreach (int richerPerson in graph[person]) {
                int candidate = Dfs(richerPerson);
                if (quiet[candidate] < quiet[best]) best = candidate;
            }
            answer[person] = best;
            return best;
        }

        for (int i = 0; i < n; i++) Dfs(i);
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} richer
 * @param {number[]} quiet
 * @return {number[]}
 */
var loudAndRich = function(richer, quiet) {
    const n = quiet.length;
    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of richer) {
        // edge from poorer (b) to richer (a)
        graph[b].push(a);
    }
    const answer = new Array(n).fill(-1);
    
    function dfs(x) {
        if (answer[x] !== -1) return answer[x];
        let best = x;
        for (const y of graph[x]) {
            const cand = dfs(y);
            if (quiet[cand] < quiet[best]) best = cand;
        }
        answer[x] = best;
        return best;
    }
    
    for (let i = 0; i < n; ++i) dfs(i);
    return answer;
};
```

## Typescript

```typescript
function loudAndRich(richer: number[][], quiet: number[]): number[] {
    const n = quiet.length;
    const graph: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of richer) {
        // a is richer than b -> edge from b to a
        graph[b].push(a);
    }
    const answer: number[] = new Array(n).fill(-1);

    function dfs(person: number): number {
        if (answer[person] !== -1) return answer[person];
        let best = person;
        for (const richerPerson of graph[person]) {
            const candidate = dfs(richerPerson);
            if (quiet[candidate] < quiet[best]) {
                best = candidate;
            }
        }
        answer[person] = best;
        return best;
    }

    for (let i = 0; i < n; ++i) {
        dfs(i);
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $richer
     * @param Integer[] $quiet
     * @return Integer[]
     */
    function loudAndRich($richer, $quiet) {
        $n = count($quiet);
        $graph = array_fill(0, $n, []);
        foreach ($richer as $pair) {
            $a = $pair[0];
            $b = $pair[1];
            $graph[$b][] = $a; // edge from poorer to richer
        }
        $answer = array_fill(0, $n, -1);
        $dfs = function($x) use (&$dfs, &$graph, &$quiet, &$answer) {
            if ($answer[$x] != -1) {
                return $answer[$x];
            }
            $best = $x;
            foreach ($graph[$x] as $y) {
                $cand = $dfs($y);
                if ($quiet[$cand] < $quiet[$best]) {
                    $best = $cand;
                }
            }
            $answer[$x] = $best;
            return $best;
        };
        for ($i = 0; $i < $n; $i++) {
            $dfs($i);
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func loudAndRich(_ richer: [[Int]], _ quiet: [Int]) -> [Int] {
        let n = quiet.count
        var graph = [[Int]](repeating: [], count: n)
        for pair in richer {
            let a = pair[0]
            let b = pair[1]
            graph[b].append(a) // edge from poorer to richer
        }
        var memo = Array(repeating: -1, count: n)

        func dfs(_ person: Int) -> Int {
            if memo[person] != -1 { return memo[person] }
            var best = person
            for nxt in graph[person] {
                let cand = dfs(nxt)
                if quiet[cand] < quiet[best] {
                    best = cand
                }
            }
            memo[person] = best
            return best
        }

        var answer = [Int](repeating: 0, count: n)
        for i in 0..<n {
            answer[i] = dfs(i)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun loudAndRich(richer: Array<IntArray>, quiet: IntArray): IntArray {
        val n = quiet.size
        val graph = Array(n) { mutableListOf<Int>() }
        for (pair in richer) {
            val a = pair[0]
            val b = pair[1]
            graph[b].add(a)
        }
        val answer = IntArray(n) { -1 }
        fun dfs(x: Int): Int {
            if (answer[x] != -1) return answer[x]
            var best = x
            for (y in graph[x]) {
                val cand = dfs(y)
                if (quiet[cand] < quiet[best]) {
                    best = cand
                }
            }
            answer[x] = best
            return best
        }
        for (i in 0 until n) {
            dfs(i)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> loudAndRich(List<List<int>> richer, List<int> quiet) {
    int n = quiet.length;
    List<List<int>> graph = List.generate(n, (_) => []);
    for (var pair in richer) {
      int a = pair[0];
      int b = pair[1];
      // edge from poorer (b) to richer (a)
      graph[b].add(a);
    }

    List<int> answer = List.filled(n, -1);

    int dfs(int node) {
      if (answer[node] != -1) return answer[node];
      int best = node;
      for (int nei in graph[node]) {
        int cand = dfs(nei);
        if (quiet[cand] < quiet[best]) {
          best = cand;
        }
      }
      answer[node] = best;
      return best;
    }

    for (int i = 0; i < n; ++i) {
      dfs(i);
    }
    return answer;
  }
}
```

## Golang

```go
func loudAndRich(richer [][]int, quiet []int) []int {
	n := len(quiet)
	graph := make([][]int, n)
	for _, p := range richer {
		a, b := p[0], p[1] // a is richer than b
		graph[b] = append(graph[b], a)
	}
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = -1
	}
	var dfs func(int) int
	dfs = func(u int) int {
		if ans[u] != -1 {
			return ans[u]
		}
		best := u
		for _, v := range graph[u] {
			candidate := dfs(v)
			if quiet[candidate] < quiet[best] {
				best = candidate
			}
		}
		ans[u] = best
		return best
	}
	for i := 0; i < n; i++ {
		dfs(i)
	}
	return ans
}
```

## Ruby

```ruby
def loud_and_rich(richer, quiet)
  n = quiet.length
  graph = Array.new(n) { [] }
  richer.each do |a, b|
    graph[b] << a
  end

  ans = Array.new(n, -1)

  dfs = lambda do |person|
    return ans[person] if ans[person] != -1
    best = person
    graph[person].each do |richer_person|
      cand = dfs.call(richer_person)
      best = cand if quiet[cand] < quiet[best]
    end
    ans[person] = best
  end

  (0...n).each { |i| dfs.call(i) }
  ans
end
```

## Scala

```scala
object Solution {
  def loudAndRich(richer: Array[Array[Int]], quiet: Array[Int]): Array[Int] = {
    val n = quiet.length
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    for (pair <- richer) {
      val a = pair(0)
      val b = pair(1)
      adj(b) += a // edge from poorer to richer
    }
    val ans = Array.fill(n)(-1)

    def dfs(x: Int): Int = {
      if (ans(x) != -1) return ans(x)
      var best = x
      for (y <- adj(x)) {
        val cand = dfs(y)
        if (quiet(cand) < quiet(best)) best = cand
      }
      ans(x) = best
      best
    }

    for (i <- 0 until n) dfs(i)
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn loud_and_rich(richer: Vec<Vec<i32>>, quiet: Vec<i32>) -> Vec<i32> {
        fn dfs(
            u: usize,
            graph: &Vec<Vec<usize>>,
            quiet: &Vec<i32>,
            memo: &mut Vec<Option<usize>>,
        ) -> usize {
            if let Some(v) = memo[u] {
                return v;
            }
            let mut best = u;
            for &v in &graph[u] {
                let cand = dfs(v, graph, quiet, memo);
                if quiet[cand] < quiet[best] {
                    best = cand;
                }
            }
            memo[u] = Some(best);
            best
        }

        let n = quiet.len();
        let mut graph: Vec<Vec<usize>> = vec![Vec::new(); n];
        for pair in richer.iter() {
            let a = pair[0] as usize;
            let b = pair[1] as usize;
            // edge from poorer (b) to richer (a)
            graph[b].push(a);
        }

        let mut memo: Vec<Option<usize>> = vec![None; n];
        let mut answer: Vec<i32> = vec![0; n];
        for i in 0..n {
            let res = dfs(i, &graph, &quiet, &mut memo);
            answer[i] = res as i32;
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (loud-and-rich richer quiet)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length quiet))
         (adj (make-vector n '()))
         (quiet-vec (list->vector quiet))
         (ans (make-vector n -1)))
    ;; build adjacency: edge from poorer to richer
    (for-each (lambda (pair)
                (let ((a (first pair))   ; a is richer than b
                      (b (second pair))) ; b is poorer
                  (vector-set! adj b (cons a (vector-ref adj b)))))
              richer)
    ;; depth‑first search with memoization
    (define (dfs i)
      (let ((cached (vector-ref ans i)))
        (if (not (= cached -1))
            cached
            (let loop ((neighbors (vector-ref adj i)) (best i))
              (if (null? neighbors)
                  (begin
                    (vector-set! ans i best)
                    best)
                  (let* ((nbr (car neighbors))
                         (cand (dfs nbr))
                         (new-best (if (< (vector-ref quiet-vec cand)
                                          (vector-ref quiet-vec best))
                                       cand
                                       best)))
                    (loop (cdr neighbors) new-best)))))))
    ;; compute answer for every person
    (for ([i (in-range n)])
      (dfs i))
    (vector->list ans)))
```

## Erlang

```erlang
-spec loud_and_rich(Richer :: [[integer()]], Quiet :: [integer()]) -> [integer()].
loud_and_rich(Richer, Quiet) ->
    N = length(Quiet),
    Adj = build_adj(Richer, #{}),
    QuietT = list_to_tuple(Quiet),

    Memo0 = #{},
    MemoFinal = lists:foldl(
        fun(Node, Memo) ->
            {_, NewMemo} = dfs(Node, Adj, QuietT, Memo),
            NewMemo
        end,
        Memo0,
        lists:seq(0, N - 1)
    ),

    [maps:get(I, MemoFinal) || I <- lists:seq(0, N - 1)].

%% Build adjacency map: edge from poorer (b) to richer (a)
-spec build_adj([[integer()]], map()) -> map().
build_adj([], Adj) ->
    Adj;
build_adj([[A, B] | Rest], Adj) ->
    UpdatedAdj = maps:update_with(
        B,
        fun(List) -> [A | List] end,
        [A],
        Adj
    ),
    build_adj(Rest, UpdatedAdj).

%% Depth‑first search with memoization.
-spec dfs(integer(), map(), tuple(), map()) -> {integer(), map()}.
dfs(Node, Adj, QuietT, Memo) ->
    case maps:is_key(Node, Memo) of
        true ->
            {maps:get(Node, Memo), Memo};
        false ->
            Children = maps:get(Node, Adj, []),
            % start with the node itself as the best candidate
            Best0 = Node,
            {Best, MemoAfterChildren} = lists:foldl(
                fun(Child, {CurBest, CurMemo}) ->
                    {ChildBest, UpdatedMemo} = dfs(Child, Adj, QuietT, CurMemo),
                    if
                        element(ChildBest + 1, QuietT) < element(CurBest + 1, QuietT) ->
                            {ChildBest, UpdatedMemo};
                        true ->
                            {CurBest, UpdatedMemo}
                    end
                end,
                {Best0, Memo},
                Children
            ),
            NewMemo = maps:put(Node, Best, MemoAfterChildren),
            {Best, NewMemo}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec loud_and_rich(richer :: [[integer]], quiet :: [integer]) :: [integer]
  def loud_and_rich(richer, quiet) do
    n = length(quiet)

    graph =
      Enum.reduce(richer, %{}, fn [a, b], acc ->
        Map.update(acc, b, [a], &[a | &1])
      end)

    quiet_t = List.to_tuple(quiet)

    {answers, _memo} =
      0..(n - 1)
      |> Enum.map_reduce(%{}, fn i, memo ->
        {res, new_memo} = dfs(i, graph, quiet_t, memo)
        {res, new_memo}
      end)

    answers
  end

  defp dfs(i, graph, quiet_t, memo) do
    case Map.fetch(memo, i) do
      {:ok, val} ->
        {val, memo}

      :error ->
        children = Map.get(graph, i, [])

        {best, memo2} =
          Enum.reduce(children, {i, memo}, fn child, {cur_best, mem_acc} ->
            {cand, mem_next} = dfs(child, graph, quiet_t, mem_acc)

            if elem(quiet_t, cand) < elem(quiet_t, cur_best) do
              {cand, mem_next}
            else
              {cur_best, mem_next}
            end
          end)

        memo3 = Map.put(memo2, i, best)
        {best, memo3}
    end
  end
end
```
