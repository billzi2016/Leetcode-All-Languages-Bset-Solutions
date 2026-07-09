# 1376. Time Needed to Inform All Employees

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        vector<vector<int>> children(n);
        for (int i = 0; i < n; ++i) {
            if (manager[i] != -1) {
                children[manager[i]].push_back(i);
            }
        }
        int maxTime = 0;
        stack<pair<int,int>> st;
        st.emplace(headID, 0);
        while (!st.empty()) {
            auto [node, curTime] = st.top();
            st.pop();
            maxTime = max(maxTime, curTime);
            for (int child : children[node]) {
                st.emplace(child, curTime + informTime[node]);
            }
        }
        return maxTime;
    }
};
```

## Java

```java
class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        List<Integer>[] subordinates = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            subordinates[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            int m = manager[i];
            if (m != -1) {
                subordinates[m].add(i);
            }
        }
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{headID, 0});
        int maxTime = 0;
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int node = cur[0];
            int elapsed = cur[1];
            maxTime = Math.max(maxTime, elapsed);
            for (int child : subordinates[node]) {
                stack.push(new int[]{child, elapsed + informTime[node]});
            }
        }
        return maxTime;
    }
}
```

## Python

```python
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        children = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                children[m].append(i)

        max_time = 0
        stack = [(headID, 0)]  # (node, accumulated time)
        while stack:
            node, cur_time = stack.pop()
            if not children[node]:
                if cur_time > max_time:
                    max_time = cur_time
            else:
                next_time = cur_time + informTime[node]
                for child in children[node]:
                    stack.append((child, next_time))
        return max_time
```

## Python3

```python
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                children[mgr].append(emp)

        max_time = 0
        stack = [(headID, 0)]  # (current employee, time accumulated to reach this employee)
        while stack:
            node, cur_time = stack.pop()
            if not children[node]:  # leaf
                if cur_time > max_time:
                    max_time = cur_time
            else:
                next_time = cur_time + informTime[node]
                for sub in children[node]:
                    stack.append((sub, next_time))
        return max_time
```

## C

```c
#include <stdlib.h>

int numOfMinutes(int n, int headID, int* manager, int managerSize, int* informTime, int informTimeSize) {
    (void)managerSize;
    (void)informTimeSize;

    // Count children for each employee
    int *childCount = calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (manager[i] != -1) {
            childCount[manager[i]]++;
        }
    }

    // Allocate adjacency lists
    int **children = malloc(n * sizeof(int*));
    int *idx = calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (childCount[i] > 0) {
            children[i] = malloc(childCount[i] * sizeof(int));
        } else {
            children[i] = NULL;
        }
    }

    // Fill adjacency lists
    for (int i = 0; i < n; ++i) {
        int p = manager[i];
        if (p != -1) {
            children[p][idx[p]++] = i;
        }
    }

    // Iterative DFS using stacks
    int *stackNode = malloc(n * sizeof(int));
    long long *stackTime = malloc(n * sizeof(long long));
    int top = 0;
    stackNode[top] = headID;
    stackTime[top] = 0LL;
    ++top;

    long long maxTime = 0;

    while (top > 0) {
        --top;
        int node = stackNode[top];
        long long curTime = stackTime[top];

        if (childCount[node] == 0) {
            if (curTime > maxTime) maxTime = curTime;
        } else {
            long long nextTime = curTime + informTime[node];
            for (int i = 0; i < childCount[node]; ++i) {
                int child = children[node][i];
                stackNode[top] = child;
                stackTime[top] = nextTime;
                ++top;
            }
        }
    }

    // Cleanup
    for (int i = 0; i < n; ++i) {
        free(children[i]);
    }
    free(children);
    free(childCount);
    free(idx);
    free(stackNode);
    free(stackTime);

    return (int)maxTime;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int NumOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        var subordinates = new List<int>[n];
        for (int i = 0; i < n; i++) {
            subordinates[i] = new List<int>();
        }
        for (int i = 0; i < n; i++) {
            int m = manager[i];
            if (m != -1) {
                subordinates[m].Add(i);
            }
        }

        int maxTime = 0;
        var stack = new Stack<(int node, int time)>();
        stack.Push((headID, 0));

        while (stack.Count > 0) {
            var (node, curTime) = stack.Pop();
            if (subordinates[node].Count == 0) {
                if (curTime > maxTime) maxTime = curTime;
            }
            foreach (int child in subordinates[node]) {
                stack.Push((child, curTime + informTime[node]));
            }
        }

        return maxTime;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} headID
 * @param {number[]} manager
 * @param {number[]} informTime
 * @return {number}
 */
var numOfMinutes = function(n, headID, manager, informTime) {
    const children = Array.from({ length: n }, () => []);
    for (let i = 0; i < n; i++) {
        const m = manager[i];
        if (m !== -1) {
            children[m].push(i);
        }
    }

    let maxTime = 0;
    const stack = [[headID, 0]]; // [node, time accumulated so far]

    while (stack.length) {
        const [node, curTime] = stack.pop();
        if (children[node].length === 0) {
            if (curTime > maxTime) maxTime = curTime;
        } else {
            const nextTime = curTime + informTime[node];
            for (const child of children[node]) {
                stack.push([child, nextTime]);
            }
        }
    }

    return maxTime;
};
```

## Typescript

```typescript
function numOfMinutes(n: number, headID: number, manager: number[], informTime: number[]): number {
    const subordinates: number[][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < n; i++) {
        const m = manager[i];
        if (m !== -1) {
            subordinates[m].push(i);
        }
    }

    let maxTime = 0;
    const stack: [number, number][] = [[headID, 0]];

    while (stack.length) {
        const [node, elapsed] = stack.pop()!;
        const current = elapsed + informTime[node];
        if (subordinates[node].length === 0) {
            if (current > maxTime) maxTime = current;
        } else {
            for (const child of subordinates[node]) {
                stack.push([child, current]);
            }
        }
    }

    return maxTime;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $headID
     * @param Integer[] $manager
     * @param Integer[] $informTime
     * @return Integer
     */
    function numOfMinutes($n, $headID, $manager, $informTime) {
        // Build adjacency list of subordinates for each manager
        $children = array_fill(0, $n, []);
        for ($i = 0; $i < $n; $i++) {
            $m = $manager[$i];
            if ($m != -1) {
                $children[$m][] = $i;
            }
        }

        $maxTime = 0;
        // Stack for DFS: each element is [employeeId, accumulatedTime]
        $stack = [];
        $stack[] = [$headID, 0];

        while (!empty($stack)) {
            $item = array_pop($stack);
            $emp = $item[0];
            $timeSoFar = $item[1];

            if (empty($children[$emp])) { // leaf node
                if ($timeSoFar > $maxTime) {
                    $maxTime = $timeSoFar;
                }
            } else {
                foreach ($children[$emp] as $sub) {
                    $stack[] = [$sub, $timeSoFar + $informTime[$emp]];
                }
            }
        }

        return $maxTime;
    }
}
```

## Swift

```swift
class Solution {
    func numOfMinutes(_ n: Int, _ headID: Int, _ manager: [Int], _ informTime: [Int]) -> Int {
        var subordinates = [[Int]](repeating: [], count: n)
        for i in 0..<n {
            let m = manager[i]
            if m != -1 {
                subordinates[m].append(i)
            }
        }
        
        var maxTime = 0
        var stack: [(node: Int, elapsed: Int)] = [(headID, 0)]
        
        while let (node, elapsed) = stack.popLast() {
            let current = elapsed + informTime[node]
            if subordinates[node].isEmpty {
                maxTime = max(maxTime, current)
            } else {
                for child in subordinates[node] {
                    stack.append((child, current))
                }
            }
        }
        
        return maxTime
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfMinutes(n: Int, headID: Int, manager: IntArray, informTime: IntArray): Int {
        val subordinates = Array(n) { mutableListOf<Int>() }
        for (i in 0 until n) {
            val m = manager[i]
            if (m != -1) {
                subordinates[m].add(i)
            }
        }
        var maxTime = 0
        val stack = java.util.ArrayDeque<Pair<Int, Int>>()
        stack.add(Pair(headID, 0))
        while (stack.isNotEmpty()) {
            val (node, curTime) = stack.poll()
            if (curTime > maxTime) maxTime = curTime
            for (child in subordinates[node]) {
                stack.add(Pair(child, curTime + informTime[node]))
            }
        }
        return maxTime
    }
}
```

## Dart

```dart
class Solution {
  int numOfMinutes(int n, int headID, List<int> manager, List<int> informTime) {
    // Build adjacency list of subordinates for each employee.
    var children = List<List<int>>.generate(n, (_) => <int>[]);
    for (int i = 0; i < n; i++) {
      int m = manager[i];
      if (m != -1) {
        children[m].add(i);
      }
    }

    int maxTime = 0;
    var nodeStack = <int>[];
    var timeStack = <int>[];

    nodeStack.add(headID);
    timeStack.add(0);

    while (nodeStack.isNotEmpty) {
      int node = nodeStack.removeLast();
      int curTime = timeStack.removeLast();

      if (children[node].isEmpty) {
        if (curTime > maxTime) maxTime = curTime;
      } else {
        int nextTime = curTime + informTime[node];
        for (int child in children[node]) {
          nodeStack.add(child);
          timeStack.add(nextTime);
        }
      }
    }

    return maxTime;
  }
}
```

## Golang

```go
func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	children := make([][]int, n)
	for i, m := range manager {
		if m != -1 {
			children[m] = append(children[m], i)
		}
	}

	type pair struct{ id, time int }
	stack := []pair{{headID, 0}}
	maxTime := 0

	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if cur.time > maxTime {
			maxTime = cur.time
		}
		for _, child := range children[cur.id] {
			stack = append(stack, pair{child, cur.time + informTime[cur.id]})
		}
	}
	return maxTime
}
```

## Ruby

```ruby
def num_of_minutes(n, head_id, manager, inform_time)
  subordinates = Array.new(n) { [] }
  manager.each_with_index do |m, i|
    next if m == -1
    subordinates[m] << i
  end

  max_time = 0
  stack = [[head_id, 0]]
  until stack.empty?
    node, cur = stack.pop
    if subordinates[node].empty?
      max_time = cur if cur > max_time
    else
      next_time = cur + inform_time[node]
      subordinates[node].each { |child| stack << [child, next_time] }
    end
  end

  max_time
end
```

## Scala

```scala
object Solution {
    def numOfMinutes(n: Int, headID: Int, manager: Array[Int], informTime: Array[Int]): Int = {
        val subordinates = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        var i = 0
        while (i < n) {
            val m = manager(i)
            if (m != -1) {
                subordinates(m).append(i)
            }
            i += 1
        }

        import java.util.ArrayDeque
        val stack: ArrayDeque[(Int, Int)] = new ArrayDeque()
        stack.addLast((headID, 0))
        var maxTime = 0

        while (!stack.isEmpty) {
            val (node, timeSoFar) = stack.removeLast()
            if (timeSoFar > maxTime) maxTime = timeSoFar
            val nextTime = timeSoFar + informTime(node)
            val children = subordinates(node)
            var idx = 0
            while (idx < children.length) {
                stack.addLast((children(idx), nextTime))
                idx += 1
            }
        }

        maxTime
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        let n_usize = n as usize;
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for (i, &m) in manager.iter().enumerate() {
            if m != -1 {
                children[m as usize].push(i);
            }
        }

        let mut stack: Vec<(usize, i32)> = Vec::with_capacity(n_usize);
        stack.push((head_id as usize, 0));
        let mut max_time = 0;

        while let Some((node, cur_time)) = stack.pop() {
            if cur_time > max_time {
                max_time = cur_time;
            }
            for &child in &children[node] {
                let next_time = cur_time + inform_time[node];
                stack.push((child, next_time));
            }
        }

        max_time
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(provide num-of-minutes)

(define/contract (num-of-minutes n headID manager informTime)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([mgr (list->vector manager)]
         [time (list->vector informTime)]
         [children (make-vector n '())])
    ;; build adjacency list of subordinates
    (for ([i (in-range n)])
      (let ([m (vector-ref mgr i)])
        (when (not (= m -1))
          (vector-set! children m (cons i (vector-ref children m))))))
    (define max-time 0)
    ;; iterative DFS using explicit stack of (node . accumulated_time)
    (let loop ((stack (list (cons headID 0))))
      (if (null? stack)
          max-time
          (let* ([pair (car stack)]
                 [node (car pair)]
                 [acc (cdr pair)]
                 [rest (cdr stack)]
                 [child-list (vector-ref children node)])
            (if (null? child-list)
                (begin
                  (when (> acc max-time) (set! max-time acc))
                  (loop rest))
                (let ([new-acc (+ acc (vector-ref time node))])
                  (loop (foldl (lambda (child st) (cons (cons child new-acc) st))
                               rest
                               child-list)))))))))
```

## Erlang

```erlang
-module(solution).
-export([num_of_minutes/4]).

-spec num_of_minutes(N :: integer(), HeadID :: integer(),
                     Manager :: [integer()], InformTime :: [integer()]) -> integer().
num_of_minutes(_N, HeadID, Manager, InformTime) ->
    ChildrenMap = build_children(Manager, 0, #{}),
    bfs([{HeadID, 0}], 0, ChildrenMap, InformTime).

%% Build a map from manager to list of direct subordinates.
-spec build_children([integer()], integer(), map()) -> map().
build_children([], _Idx, Map) ->
    Map;
build_children([M|Rest], Idx, Map) ->
    NewMap = case M of
        -1 -> Map;
        _  ->
            Children = maps:get(M, Map, []),
            maps:put(M, [Idx | Children], Map)
    end,
    build_children(Rest, Idx + 1, NewMap).

%% Breadth‑first traversal accumulating times and tracking the maximum.
-spec bfs([{integer(), integer()}], integer(), map(), [integer()]) -> integer().
bfs([], Max, _ChildrenMap, _InformTime) ->
    Max;
bfs([{Node, Acc}|QueueTail], Max, ChildrenMap, InformTime) ->
    % Erlang lists are 1‑based.
    Inform = lists:nth(Node + 1, InformTime),
    CurTime = Acc + Inform,
    NewMax = if CurTime > Max -> CurTime; true -> Max end,
    Children = maps:get(Node, ChildrenMap, []),
    NewQueue = [{Child, CurTime} || Child <- Children] ++ QueueTail,
    bfs(NewQueue, NewMax, ChildrenMap, InformTime).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_minutes(n :: integer, head_id :: integer, manager :: [integer], inform_time :: [integer]) :: integer
  def num_of_minutes(_n, head_id, manager, inform_time) do
    children =
      Enum.with_index(manager)
      |> Enum.reduce(%{}, fn {m, i}, acc ->
        if m != -1 do
          Map.update(acc, m, [i], fn list -> [i | list] end)
        else
          acc
        end
      end)

    inform_arr = :array.from_list(inform_time)
    dfs([{head_id, 0}], children, inform_arr, 0)
  end

  defp dfs([], _children, _inform_arr, max), do: max

  defp dfs([{node, cur_time} | rest], children, inform_arr, max) do
    new_max = if cur_time > max, do: cur_time, else: max
    child_list = Map.get(children, node, [])
    add_time = :array.get(node, inform_arr)

    new_stack =
      Enum.reduce(child_list, rest, fn child, acc ->
        [{child, cur_time + add_time} | acc]
      end)

    dfs(new_stack, children, inform_arr, new_max)
  end
end
```
