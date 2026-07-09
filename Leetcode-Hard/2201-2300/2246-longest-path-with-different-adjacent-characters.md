# 2246. Longest Path With Different Adjacent Characters

## Cpp

```cpp
class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }
        int ans = 0;
        function<int(int)> dfs = [&](int u) -> int {
            int best1 = 0, best2 = 0; // longest and second longest valid chains from children
            for (int v : children[u]) {
                int cur = dfs(v);
                if (s[v] == s[u]) continue;
                if (cur > best1) {
                    best2 = best1;
                    best1 = cur;
                } else if (cur > best2) {
                    best2 = cur;
                }
            }
            ans = max(ans, best1 + best2 + 1);
            return best1 + 1;
        };
        dfs(0);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int longestPath(int[] parent, String s) {
        int n = parent.length;
        List<Integer>[] children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            children[parent[i]].add(i);
        }

        int[] longestDown = new int[n];
        int[] order = new int[n];
        int idx = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int node = stack.pop();
            order[idx++] = node;
            for (int child : children[node]) {
                stack.push(child);
            }
        }

        int answer = 1;
        for (int i = n - 1; i >= 0; i--) {
            int node = order[i];
            int max1 = 0, max2 = 0;
            char curChar = s.charAt(node);
            for (int child : children[node]) {
                if (s.charAt(child) != curChar) {
                    int len = longestDown[child];
                    if (len > max1) {
                        max2 = max1;
                        max1 = len;
                    } else if (len > max2) {
                        max2 = len;
                    }
                }
            }
            longestDown[node] = 1 + max1;
            answer = Math.max(answer, 1 + max1 + max2);
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        import sys
        sys.setrecursionlimit(2000000)
        ans = 1

        def dfs(u):
            nonlocal ans
            best1 = best2 = 0  # longest and second longest valid child chains
            for v in children[u]:
                child_len = dfs(v)          # length of longest chain starting at v
                if s[v] != s[u]:            # can be concatenated through edge (u,v)
                    if child_len > best1:
                        best2 = best1
                        best1 = child_len
                    elif child_len > best2:
                        best2 = child_len
            ans = max(ans, best1 + best2 + 1)   # path passing through u
            return best1 + 1                    # longest chain from u downwards

        dfs(0)
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        sys.setrecursionlimit(2000000)
        ans = 0

        def dfs(u: int) -> int:
            nonlocal ans
            best1 = best2 = 0  # longest and second longest child chains that can extend
            for v in children[u]:
                cur_len = dfs(v)
                if s[v] == s[u]:
                    continue
                if cur_len > best1:
                    best2 = best1
                    best1 = cur_len
                elif cur_len > best2:
                    best2 = cur_len
            ans = max(ans, 1 + best1 + best2)
            return 1 + best1

        dfs(0)
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int node;
    char processed; // 0 = first visit, 1 = post processing
} StackItem;

int longestPath(int* parent, int parentSize, char* s) {
    int n = parentSize;
    if (n == 0) return 0;

    /* count children for each node */
    int *childCnt = calloc(n, sizeof(int));
    for (int i = 1; i < n; ++i) {
        childCnt[parent[i]]++;
    }

    /* allocate children arrays */
    int **children = malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        if (childCnt[i] > 0)
            children[i] = malloc(childCnt[i] * sizeof(int));
        else
            children[i] = NULL;
    }

    /* fill children arrays */
    int *idx = calloc(n, sizeof(int));
    for (int i = 1; i < n; ++i) {
        int p = parent[i];
        children[p][ idx[p]++ ] = i;
    }

    int *dp = malloc(n * sizeof(int));   // longest valid chain starting at node
    int answer = 1;                      // at least one node exists

    /* iterative post-order DFS */
    StackItem *stack = malloc(2 * n * sizeof(StackItem));
    int top = 0;
    stack[top++] = (StackItem){0, 0};   // start from root

    while (top) {
        StackItem cur = stack[--top];
        int u = cur.node;

        if (!cur.processed) {
            /* push post-processing marker */
            stack[top++] = (StackItem){u, 1};
            /* push children for processing */
            for (int i = 0; i < childCnt[u]; ++i) {
                int v = children[u][i];
                stack[top++] = (StackItem){v, 0};
            }
        } else {
            int best1 = 0, best2 = 0;
            for (int i = 0; i < childCnt[u]; ++i) {
                int v = children[u][i];
                if (s[v] != s[u]) {
                    int len = dp[v];
                    if (len > best1) {
                        best2 = best1;
                        best1 = len;
                    } else if (len > best2) {
                        best2 = len;
                    }
                }
            }
            dp[u] = 1 + best1;                 // longest chain downwards from u
            int cand = 1 + best1 + best2;       // path passing through u
            if (cand > answer) answer = cand;
        }
    }

    /* free allocated memory */
    for (int i = 0; i < n; ++i) {
        if (children[i]) free(children[i]);
    }
    free(children);
    free(childCnt);
    free(idx);
    free(dp);
    free(stack);

    return answer;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private List<int>[] children;
    private string chars;
    private int answer;

    public int LongestPath(int[] parent, string s) {
        int n = parent.Length;
        chars = s;
        children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            children[parent[i]].Add(i);
        }
        answer = 0;
        Dfs(0);
        return answer;
    }

    private int Dfs(int node) {
        int best1 = 0, best2 = 0;
        foreach (int child in children[node]) {
            int len = Dfs(child);
            if (chars[child] != chars[node]) {
                if (len > best1) {
                    best2 = best1;
                    best1 = len;
                } else if (len > best2) {
                    best2 = len;
                }
            }
        }
        answer = System.Math.Max(answer, 1 + best1 + best2);
        return 1 + best1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number}
 */
var longestPath = function(parent, s) {
    const n = parent.length;
    const children = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; ++i) {
        children[parent[i]].push(i);
    }
    const dp = new Array(n).fill(1); // longest chain starting at node
    let ans = 1;
    const stack = [[0, false]];
    while (stack.length) {
        const [node, visited] = stack.pop();
        if (!visited) {
            stack.push([node, true]);
            for (const child of children[node]) {
                stack.push([child, false]);
            }
        } else {
            let max1 = 0, max2 = 0;
            for (const child of children[node]) {
                if (s[child] !== s[node]) {
                    const cand = dp[child];
                    if (cand > max1) {
                        max2 = max1;
                        max1 = cand;
                    } else if (cand > max2) {
                        max2 = cand;
                    }
                }
            }
            dp[node] = 1 + max1; // chain from node downwards
            const total = 1 + max1 + max2; // path passing through node
            if (total > ans) ans = total;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function longestPath(parent: number[], s: string): number {
    const n = parent.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        children[parent[i]].push(i);
    }

    const dp: number[] = new Array(n).fill(0);
    let answer = 1;

    // stack elements: [node, visitedFlag]
    const stack: [number, boolean][] = [[0, false]];
    while (stack.length) {
        const [u, visited] = stack.pop()!;
        if (!visited) {
            stack.push([u, true]);
            for (const v of children[u]) {
                stack.push([v, false]);
            }
        } else {
            let max1 = 0, max2 = 0;
            for (const v of children[u]) {
                if (s[v] !== s[u]) {
                    const len = dp[v];
                    if (len > max1) {
                        max2 = max1;
                        max1 = len;
                    } else if (len > max2) {
                        max2 = len;
                    }
                }
            }
            dp[u] = 1 + max1;
            answer = Math.max(answer, 1 + max1 + max2);
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $parent
     * @param String $s
     * @return Integer
     */
    function longestPath($parent, $s) {
        $n = count($parent);
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $p = $parent[$i];
            $children[$p][] = $i;
        }

        $ans = 1;
        $dfs = function($node) use (&$children, &$s, &$ans, &$dfs) {
            $max1 = 0;
            $max2 = 0;
            foreach ($children[$node] as $child) {
                $len = $dfs($child);
                if ($s[$child] === $s[$node]) {
                    continue;
                }
                if ($len > $max1) {
                    $max2 = $max1;
                    $max1 = $len;
                } elseif ($len > $max2) {
                    $max2 = $len;
                }
            }
            $ans = max($ans, 1 + $max1 + $max2);
            return 1 + $max1;
        };

        $dfs(0);
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestPath(_ parent: [Int], _ s: String) -> Int {
        let n = parent.count
        var children = [[Int]](repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                let p = parent[i]
                children[p].append(i)
            }
        }
        let chars = Array(s)
        // iterative DFS to get processing order
        var stack = [Int]()
        var order = [Int]()
        stack.append(0)
        while let node = stack.popLast() {
            order.append(node)
            for child in children[node] {
                stack.append(child)
            }
        }
        var dp = [Int](repeating: 1, count: n) // longest chain starting at node
        var answer = 1
        for node in order.reversed() {
            var max1 = 0
            var max2 = 0
            for child in children[node] {
                if chars[child] == chars[node] { continue }
                let cand = dp[child]
                if cand > max1 {
                    max2 = max1
                    max1 = cand
                } else if cand > max2 {
                    max2 = cand
                }
            }
            answer = max(answer, max1 + max2 + 1)
            dp[node] = max1 + 1
        }
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun longestPath(parent: IntArray, s: String): Int {
        val n = parent.size
        val children = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            val p = parent[i]
            children[p].add(i)
        }

        val chars = s.toCharArray()
        val longest = IntArray(n)
        var answer = 1

        val stack: ArrayDeque<Pair<Int, Boolean>> = ArrayDeque()
        stack.add(Pair(0, false))

        while (stack.isNotEmpty()) {
            val (node, visited) = stack.removeLast()
            if (!visited) {
                stack.add(Pair(node, true))
                for (child in children[node]) {
                    stack.add(Pair(child, false))
                }
            } else {
                var best = 0
                var second = 0
                for (child in children[node]) {
                    if (chars[child] != chars[node]) {
                        val len = longest[child]
                        if (len > best) {
                            second = best
                            best = len
                        } else if (len > second) {
                            second = len
                        }
                    }
                }
                longest[node] = 1 + best
                answer = maxOf(answer, best + second + 1)
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int longestPath(List<int> parent, String s) {
    int n = parent.length;
    List<List<int>> children = List.generate(n, (_) => []);
    for (int i = 1; i < n; i++) {
      children[parent[i]].add(i);
    }

    // preorder traversal to get order
    List<int> order = [];
    List<int> stack = [0];
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int child in children[node]) {
        stack.add(child);
      }
    }

    List<int> dp = List.filled(n, 1);
    List<int> codes = s.codeUnits;
    int ans = 1;

    for (int idx = order.length - 1; idx >= 0; idx--) {
      int node = order[idx];
      int max1 = 0, max2 = 0;
      for (int child in children[node]) {
        if (codes[child] != codes[node]) {
          int len = dp[child];
          if (len > max1) {
            max2 = max1;
            max1 = len;
          } else if (len > max2) {
            max2 = len;
          }
        }
      }
      int candidate = max1 + max2 + 1;
      if (candidate > ans) ans = candidate;
      dp[node] = max1 + 1;
    }

    return ans;
  }
}
```

## Golang

```go
func longestPath(parent []int, s string) int {
	n := len(parent)
	children := make([][]int, n)
	for i := 1; i < n; i++ {
		p := parent[i]
		children[p] = append(children[p], i)
	}
	ans := 1
	var dfs func(int) int
	dfs = func(u int) int {
		max1, max2 := 0, 0
		for _, v := range children[u] {
			childLen := dfs(v)
			if s[v] == s[u] {
				continue
			}
			if childLen > max1 {
				max2 = max1
				max1 = childLen
			} else if childLen > max2 {
				max2 = childLen
			}
		}
		if cur := max1 + max2 + 1; cur > ans {
			ans = cur
		}
		return max1 + 1
	}
	dfs(0)
	return ans
}
```

## Ruby

```ruby
def longest_path(parent, s)
  n = parent.length
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = parent[i]
    children[p] << i
  end

  order = []
  stack = [0]
  while !stack.empty?
    node = stack.pop
    order << node
    children[node].each { |c| stack << c }
  end

  dp = Array.new(n, 1)
  ans = 1

  order.reverse_each do |node|
    max1 = 0
    max2 = 0
    children[node].each do |c|
      next if s[c] == s[node]
      len = dp[c]
      if len > max1
        max2 = max1
        max1 = len
      elsif len > max2
        max2 = len
      end
    end
    dp[node] = 1 + max1
    candidate = 1 + max1 + max2
    ans = candidate if candidate > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
  def longestPath(parent: Array[Int], s: String): Int = {
    val n = parent.length
    val children = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    var i = 1
    while (i < n) {
      val p = parent(i)
      children(p).append(i)
      i += 1
    }

    // iterative post-order traversal
    val nodeStack = new java.util.ArrayDeque[Int]()
    val visitedStack = new java.util.ArrayDeque[Boolean]()
    nodeStack.push(0)
    visitedStack.push(false)

    val order = new scala.collection.mutable.ArrayBuffer[Int]()

    while (!nodeStack.isEmpty) {
      val node = nodeStack.pop()
      val visited = visitedStack.pop()
      if (visited) {
        order.append(node)
      } else {
        nodeStack.push(node)
        visitedStack.push(true)
        val childs = children(node)
        var idx = 0
        while (idx < childs.length) {
          nodeStack.push(childs(idx))
          visitedStack.push(false)
          idx += 1
        }
      }
    }

    val dp = new Array[Int](n)
    var ans = 1

    var idxOrder = 0
    while (idxOrder < order.length) {
      val node = order(idxOrder)
      var max1 = 0
      var max2 = 0
      val childs = children(node)
      var j = 0
      while (j < childs.length) {
        val child = childs(j)
        if (s.charAt(child) != s.charAt(node)) {
          val len = dp(child)
          if (len > max1) {
            max2 = max1
            max1 = len
          } else if (len > max2) {
            max2 = len
          }
        }
        j += 1
      }
      dp(node) = max1 + 1
      val candidate = max1 + max2 + 1
      if (candidate > ans) ans = candidate
      idxOrder += 1
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_path(parent: Vec<i32>, s: String) -> i32 {
        let n = parent.len();
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = parent[i] as usize;
            children[p].push(i);
        }
        let chars = s.as_bytes();

        // Build a post-order traversal order using an explicit stack
        let mut stack = Vec::with_capacity(n);
        stack.push(0usize);
        let mut order = Vec::with_capacity(n);
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in children[u].iter() {
                stack.push(v);
            }
        }

        let mut dp: Vec<i32> = vec![1; n];
        let mut ans: i32 = 1;

        // Process nodes bottom‑up
        for &u in order.iter().rev() {
            let mut first = 0i32;
            let mut second = 0i32;
            for &v in children[u].iter() {
                if chars[v] != chars[u] {
                    let cand = dp[v] + 1;
                    if cand > first {
                        second = first;
                        first = cand;
                    } else if cand > second {
                        second = cand;
                    }
                }
            }
            dp[u] = if first > 0 { first } else { 1 };
            let candidate_path = if second > 0 {
                first + second - 1
            } else {
                first.max(1)
            };
            if candidate_path > ans {
                ans = candidate_path;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (longest-path parent s)
  (-> (listof exact-integer?) string? exact-integer?)
  (let* ((pvec (list->vector parent))
         (n (vector-length pvec))
         (adj (make-vector n '())))
    ;; build adjacency list
    (for ([i (in-range n)])
      (let ((par (vector-ref pvec i)))
        (when (not (= par -1))
          (vector-set! adj par (cons i (vector-ref adj par))))))
    (define maxAns 0)
    (define (dfs u)
      (define best1 0)
      (define best2 0)
      (for ([v (in-list (vector-ref adj u))])
        (let ((len (dfs v)))
          (when (char=? (string-ref s u) (string-ref s v))
            (set! len 0))
          (cond
            [(> len best1) (set! best2 best1) (set! best1 len)]
            [(> len best2) (set! best2 len)])))
      (let ((candidate (+ 1 best1 best2)))
        (when (> candidate maxAns)
          (set! maxAns candidate)))
      (+ 1 best1))
    (dfs 0)
    maxAns))
```

## Erlang

```erlang
-module(solution).
-export([longest_path/2]).

%% Public API
-spec longest_path(Parent :: [integer()], S :: unicode:unicode_binary()) -> integer().
longest_path(Parent, S) ->
    N = length(Parent),
    ParentT = list_to_tuple(Parent),
    CharList = binary_to_list(S),
    CharT = list_to_tuple(CharList),

    %% Build children map
    EmptyMap = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    Indices = lists:seq(1, N - 1),
    ChildrenMap = lists:foldl(
        fun(I, Acc) ->
            P = element(I + 1, ParentT),
            Old = maps:get(P, Acc, []),
            maps:put(P, [I | Old], Acc)
        end,
        EmptyMap,
        Indices),

    %% Initialize arrays for chain lengths and best path in subtree
    Chains0 = array:new(N, {default, 0}),
    Bests0 = array:new(N, {default, 0}),

    %% Iterative post-order DFS using explicit stack
    Stack0 = [{0, false}],
    {_FinalChains, FinalBests} = process(Stack0, Chains0, Bests0, ChildrenMap, CharT),
    array:get(0, FinalBests).

%% Process stack: returns {ChainsArray, BestsArray}
-spec process(
        Stack :: [{integer(), boolean()}],
        Chains :: array:array(),
        Bests :: array:array(),
        ChildrenMap :: map(),
        CharT :: tuple()
    ) -> {array:array(), array:array()}.
process([], Chains, Bests, _ChildrenMap, _CharT) ->
    {Chains, Bests};
process([{Node, false} | Rest], Chains, Bests, ChildrenMap, CharT) ->
    ChildIds = maps:get(Node, ChildrenMap, []),
    NewStack = [{Node, true} |
                lists:foldl(fun(C, Acc) -> [{C, false} | Acc] end, Rest, ChildIds)],
    process(NewStack, Chains, Bests, ChildrenMap, CharT);
process([{Node, true} | Rest], Chains, Bests, ChildrenMap, CharT) ->
    ChildIds = maps:get(Node, ChildrenMap, []),
    CharNode = element(Node + 1, CharT),

    {Top1, Top2, BestChildren} = lists:foldl(
        fun(Child, {T1, T2, B}) ->
            ChildChain = array:get(Child, Chains),
            ChildBest = array:get(Child, Bests),
            B1 = if ChildBest > B -> ChildBest; true -> B end,
            CharChild = element(Child + 1, CharT),
            ExtLen = if CharNode =/= CharChild -> ChildChain else 0 end,
            case ExtLen of
                L when L > T1 ->
                    {L, T1, B1};
                L when L > T2 ->
                    {T1, L, B1};
                _ ->
                    {T1, T2, B1}
            end
        end,
        {0, 0, 0},
        ChildIds),

    NodeChain = 1 + Top1,
    ThroughNode = 1 + Top1 + Top2,
    NodeBest = if BestChildren > ThroughNode -> BestChildren; true -> ThroughNode end,

    NewChains = array:set(Node, NodeChain, Chains),
    NewBests = array:set(Node, NodeBest, Bests),

    process(Rest, NewChains, NewBests, ChildrenMap, CharT).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_path(parent :: [integer], s :: String.t()) :: integer
  def longest_path(parent, s) do
    n = length(parent)
    parent_tuple = List.to_tuple(parent)

    # Build children adjacency list using Erlang array for O(1) access
    children =
      :array.new(n, default: [])

    children =
      Enum.reduce(1..(n - 1), children, fn i, acc ->
        p = elem(parent_tuple, i)
        list = :array.get(p, acc)
        :array.set(p, [i | list], acc)
      end)

    # DP array to store longest chain starting at each node
    dp = :array.new(n, default: 0)

    # Stack for iterative DFS: {node, visited_children?}
    stack = [{0, false}]
    ans = 1

    {_, final_ans} =
      dfs(stack, children, s, dp, ans)

    final_ans
  end

  defp dfs([], _children, _s, dp, ans), do: {dp, ans}

  defp dfs([{node, visited} | rest], children, s, dp, ans) do
    if not visited do
      child_list = :array.get(node, children)

      new_stack =
        Enum.reduce(child_list, [{node, true} | rest], fn child, acc ->
          [{child, false} | acc]
        end)

      dfs(new_stack, children, s, dp, ans)
    else
      char_node = :binary.at(s, node)
      child_list = :array.get(node, children)

      {max1, max2, dp_updated} =
        Enum.reduce(child_list, {0, 0, dp}, fn child, {m1, m2, dp_acc} ->
          if :binary.at(s, child) != char_node do
            len = :array.get(child, dp_acc)

            cond do
              len > m1 -> {len, m1, dp_acc}
              len > m2 -> {m1, len, dp_acc}
              true -> {m1, m2, dp_acc}
            end
          else
            {m1, m2, dp_acc}
          end
        end)

      cur_len = max1 + 1
      dp_new = :array.set(node, cur_len, dp_updated)
      ans_new = max(ans, max1 + max2 + 1)

      dfs(rest, children, s, dp_new, ans_new)
    end
  end
end
```
