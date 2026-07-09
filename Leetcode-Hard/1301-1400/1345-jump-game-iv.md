# 1345. Jump Game IV

## Cpp

```cpp
class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return 0;
        
        unordered_map<int, vector<int>> pos;
        pos.reserve(n * 2);
        for (int i = 0; i < n; ++i) {
            pos[arr[i]].push_back(i);
        }
        
        vector<char> visited(n, false);
        queue<int> q;
        q.push(0);
        visited[0] = true;
        int steps = 0;
        
        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                int i = q.front(); q.pop();
                if (i == n - 1) return steps;
                
                // neighbor i-1
                if (i - 1 >= 0 && !visited[i - 1]) {
                    visited[i - 1] = true;
                    q.push(i - 1);
                }
                // neighbor i+1
                if (i + 1 < n && !visited[i + 1]) {
                    visited[i + 1] = true;
                    q.push(i + 1);
                }
                // same value jumps
                auto it = pos.find(arr[i]);
                if (it != pos.end()) {
                    for (int j : it->second) {
                        if (!visited[j]) {
                            visited[j] = true;
                            q.push(j);
                        }
                    }
                    pos.erase(it); // prevent future redundant checks
                }
            }
            ++steps;
        }
        return -1; // should never reach here
    }
};
```

## Java

```java
class Solution {
    public int minJumps(int[] arr) {
        int n = arr.length;
        if (n <= 1) return 0;

        // Map each value to list of indices having that value
        java.util.HashMap<Integer, java.util.List<Integer>> idxMap = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            idxMap.computeIfAbsent(arr[i], k -> new java.util.ArrayList<>()).add(i);
        }

        boolean[] visited = new boolean[n];
        java.util.Queue<Integer> queue = new java.util.ArrayDeque<>();
        queue.offer(0);
        visited[0] = true;
        int steps = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s++) {
                int cur = queue.poll();
                if (cur == n - 1) return steps;

                // Jump to same value indices
                java.util.List<Integer> sameValIndices = idxMap.get(arr[cur]);
                if (sameValIndices != null) {
                    for (int nxt : sameValIndices) {
                        if (!visited[nxt]) {
                            visited[nxt] = true;
                            queue.offer(nxt);
                        }
                    }
                    // Prevent future redundant processing
                    sameValIndices.clear();
                }

                // Jump to adjacent indices
                if (cur - 1 >= 0 && !visited[cur - 1]) {
                    visited[cur - 1] = true;
                    queue.offer(cur - 1);
                }
                if (cur + 1 < n && !visited[cur + 1]) {
                    visited[cur + 1] = true;
                    queue.offer(cur + 1);
                }
            }
            steps++;
        }

        return -1; // Should never reach here for valid input
    }
}
```

## Python

```python
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n <= 1:
            return 0

        from collections import defaultdict, deque

        # map each value to all indices having that value
        idxs = defaultdict(list)
        for i, v in enumerate(arr):
            idxs[v].append(i)

        visited = [False] * n
        visited[0] = True
        q = deque()
        q.append((0, 0))  # (index, steps)

        while q:
            i, step = q.popleft()
            if i == n - 1:
                return step

            # neighbor i-1
            if i - 1 >= 0 and not visited[i - 1]:
                visited[i - 1] = True
                q.append((i - 1, step + 1))
            # neighbor i+1
            if i + 1 < n and not visited[i + 1]:
                visited[i + 1] = True
                q.append((i + 1, step + 1))

            # all same-value jumps
            val = arr[i]
            for j in idxs[val]:
                if not visited[j]:
                    visited[j] = True
                    q.append((j, step + 1))
            # clear to prevent future redundant checks
            idxs[val].clear()

        return -1  # should never reach here for valid input
```

## Python3

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        # map each value to all indices having that value
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)

        visited = [False] * n
        visited[0] = True
        q = deque([0])
        steps = 0

        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                if idx == n - 1:
                    return steps

                # neighbors: i-1, i+1, same value indices
                nxt = []
                if idx + 1 < n:
                    nxt.append(idx + 1)
                if idx - 1 >= 0:
                    nxt.append(idx - 1)

                nxt.extend(pos[arr[idx]])
                # clear to prevent future redundant traversals
                pos[arr[idx]].clear()

                for nb in nxt:
                    if not visited[nb]:
                        visited[nb] = True
                        q.append(nb)
            steps += 1

        return steps
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include "uthash.h"

typedef struct {
    int val;                // key
    int *indices;           // dynamic array of positions with this value
    int cnt;                // number of stored indices
    int cap;                // capacity of the array
    UT_hash_handle hh;      // hash handle
} ValueNode;

int minJumps(int* arr, int arrSize) {
    if (arrSize <= 1) return 0;

    // Build hashmap from value to list of indices
    ValueNode *map = NULL;
    for (int i = 0; i < arrSize; ++i) {
        ValueNode *node = NULL;
        HASH_FIND_INT(map, &arr[i], node);
        if (!node) {
            node = (ValueNode *)malloc(sizeof(ValueNode));
            node->val = arr[i];
            node->cnt = 0;
            node->cap = 4;
            node->indices = (int *)malloc(node->cap * sizeof(int));
            HASH_ADD_INT(map, val, node);
        }
        if (node->cnt == node->cap) {
            node->cap <<= 1;
            node->indices = (int *)realloc(node->indices, node->cap * sizeof(int));
        }
        node->indices[node->cnt++] = i;
    }

    // BFS initialization
    char *visited = (char *)calloc(arrSize, sizeof(char));
    int *queue = (int *)malloc(arrSize * sizeof(int));
    int front = 0, back = 0;
    queue[back++] = 0;
    visited[0] = 1;
    int steps = 0;

    while (front < back) {
        int layerSize = back - front;
        for (int i = 0; i < layerSize; ++i) {
            int cur = queue[front++];
            if (cur == arrSize - 1) {
                free(visited);
                free(queue);
                // clean remaining hashmap
                ValueNode *tmp, *iter;
                HASH_ITER(hh, map, iter, tmp) {
                    free(iter->indices);
                    HASH_DEL(map, iter);
                    free(iter);
                }
                return steps;
            }

            // neighbor: cur - 1
            if (cur - 1 >= 0 && !visited[cur - 1]) {
                visited[cur - 1] = 1;
                queue[back++] = cur - 1;
            }
            // neighbor: cur + 1
            if (cur + 1 < arrSize && !visited[cur + 1]) {
                visited[cur + 1] = 1;
                queue[back++] = cur + 1;
            }

            // same value jumps
            ValueNode *node = NULL;
            HASH_FIND_INT(map, &arr[cur], node);
            if (node) {
                for (int k = 0; k < node->cnt; ++k) {
                    int idx = node->indices[k];
                    if (!visited[idx]) {
                        visited[idx] = 1;
                        queue[back++] = idx;
                    }
                }
                // remove entry to avoid future processing
                HASH_DEL(map, node);
                free(node->indices);
                free(node);
            }
        }
        ++steps;
    }

    // Cleanup (should not reach here)
    free(visited);
    free(queue);
    ValueNode *tmp, *iter;
    HASH_ITER(hh, map, iter, tmp) {
        free(iter->indices);
        HASH_DEL(map, iter);
        free(iter);
    }
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinJumps(int[] arr) {
        int n = arr.Length;
        if (n <= 1) return 0;

        var indicesByValue = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!indicesByValue.TryGetValue(arr[i], out var list)) {
                list = new List<int>();
                indicesByValue[arr[i]] = list;
            }
            list.Add(i);
        }

        var visited = new bool[n];
        var queue = new Queue<int>();
        queue.Enqueue(0);
        visited[0] = true;
        int steps = 0;

        while (queue.Count > 0) {
            int size = queue.Count;
            for (int s = 0; s < size; s++) {
                int idx = queue.Dequeue();
                if (idx == n - 1) return steps;

                // Jump to same value indices
                if (indicesByValue.TryGetValue(arr[idx], out var sameList)) {
                    foreach (int j in sameList) {
                        if (!visited[j]) {
                            visited[j] = true;
                            queue.Enqueue(j);
                        }
                    }
                    // Prevent future redundant checks
                    indicesByValue.Remove(arr[idx]);
                }

                // Jump to idx - 1
                if (idx - 1 >= 0 && !visited[idx - 1]) {
                    visited[idx - 1] = true;
                    queue.Enqueue(idx - 1);
                }
                // Jump to idx + 1
                if (idx + 1 < n && !visited[idx + 1]) {
                    visited[idx + 1] = true;
                    queue.Enqueue(idx + 1);
                }
            }
            steps++;
        }

        return -1; // Should never reach here for valid input
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    const n = arr.length;
    if (n <= 1) return 0;

    // Build map from value to all indices having that value
    const posMap = new Map();
    for (let i = 0; i < n; ++i) {
        const v = arr[i];
        if (!posMap.has(v)) posMap.set(v, []);
        posMap.get(v).push(i);
    }

    const visited = new Array(n).fill(false);
    const queue = [0];
    let head = 0;
    visited[0] = true;
    let steps = 0;

    while (head < queue.length) {
        const layerSize = queue.length - head;
        for (let s = 0; s < layerSize; ++s) {
            const i = queue[head++];
            if (i === n - 1) return steps;

            // neighbor i-1
            if (i - 1 >= 0 && !visited[i - 1]) {
                visited[i - 1] = true;
                queue.push(i - 1);
            }
            // neighbor i+1
            if (i + 1 < n && !visited[i + 1]) {
                visited[i + 1] = true;
                queue.push(i + 1);
            }
            // neighbors with same value
            const sameVals = posMap.get(arr[i]);
            if (sameVals) {
                for (const j of sameVals) {
                    if (!visited[j]) {
                        visited[j] = true;
                        queue.push(j);
                    }
                }
                // clear to prevent future redundant checks
                posMap.delete(arr[i]);
            }
        }
        ++steps;
    }

    return -1; // unreachable (problem guarantees a path)
};
```

## Typescript

```typescript
function minJumps(arr: number[]): number {
    const n = arr.length;
    if (n <= 1) return 0;

    const graph = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        const v = arr[i];
        if (!graph.has(v)) graph.set(v, []);
        graph.get(v)!.push(i);
    }

    const visited = new Array<boolean>(n);
    visited[0] = true;
    let queue: number[] = [0];
    let steps = 0;

    while (queue.length) {
        const nextQueue: number[] = [];
        for (const idx of queue) {
            if (idx === n - 1) return steps;

            const val = arr[idx];

            const sameList = graph.get(val);
            if (sameList) {
                for (const j of sameList) {
                    if (!visited[j]) {
                        visited[j] = true;
                        nextQueue.push(j);
                    }
                }
                graph.delete(val);
            }

            if (idx - 1 >= 0 && !visited[idx - 1]) {
                visited[idx - 1] = true;
                nextQueue.push(idx - 1);
            }
            if (idx + 1 < n && !visited[idx + 1]) {
                visited[idx + 1] = true;
                nextQueue.push(idx + 1);
            }
        }
        queue = nextQueue;
        steps++;
    }

    return -1; // unreachable in valid inputs
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function minJumps($arr) {
        $n = count($arr);
        if ($n <= 1) return 0;

        // Build value to indices map
        $graph = [];
        for ($i = 0; $i < $n; $i++) {
            $val = $arr[$i];
            if (!isset($graph[$val])) {
                $graph[$val] = [];
            }
            $graph[$val][] = $i;
        }

        $visited = array_fill(0, $n, false);
        $visited[0] = true;

        $queue = new SplQueue();
        $queue->enqueue([0, 0]); // [index, steps]

        while (!$queue->isEmpty()) {
            [$idx, $steps] = $queue->dequeue();

            if ($idx == $n - 1) {
                return $steps;
            }

            // Neighbor: idx - 1
            $next = $idx - 1;
            if ($next >= 0 && !$visited[$next]) {
                $visited[$next] = true;
                $queue->enqueue([$next, $steps + 1]);
            }

            // Neighbor: idx + 1
            $next = $idx + 1;
            if ($next < $n && !$visited[$next]) {
                $visited[$next] = true;
                $queue->enqueue([$next, $steps + 1]);
            }

            // Same value jumps
            $val = $arr[$idx];
            if (isset($graph[$val])) {
                foreach ($graph[$val] as $j) {
                    if (!$visited[$j]) {
                        $visited[$j] = true;
                        $queue->enqueue([$j, $steps + 1]);
                    }
                }
                // Prevent future redundant processing
                unset($graph[$val]);
            }
        }

        return -1; // Should never reach here for valid input
    }
}
```

## Swift

```swift
class Solution {
    func minJumps(_ arr: [Int]) -> Int {
        let n = arr.count
        if n <= 1 { return 0 }
        
        // Build value to indices map
        var indexMap = [Int: [Int]]()
        for i in 0..<n {
            indexMap[arr[i], default: []].append(i)
        }
        
        var visited = Array(repeating: false, count: n)
        visited[0] = true
        
        var queue = [Int]()
        queue.append(0)
        var head = 0
        var steps = 0
        
        while head < queue.count {
            let currentLevelCount = queue.count - head
            for _ in 0..<currentLevelCount {
                let i = queue[head]
                head += 1
                
                if i == n - 1 { return steps }
                
                // Move to i-1
                if i - 1 >= 0 && !visited[i - 1] {
                    visited[i - 1] = true
                    queue.append(i - 1)
                }
                // Move to i+1
                if i + 1 < n && !visited[i + 1] {
                    visited[i + 1] = true
                    queue.append(i + 1)
                }
                // Jump to same value indices
                if let sameIndices = indexMap[arr[i]] {
                    for j in sameIndices {
                        if !visited[j] {
                            visited[j] = true
                            queue.append(j)
                        }
                    }
                    // Clear to prevent future redundant checks
                    indexMap[arr[i]] = nil
                }
            }
            steps += 1
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minJumps(arr: IntArray): Int {
        val n = arr.size
        if (n <= 1) return 0

        // Map each value to all indices having that value
        val posMap = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            posMap.computeIfAbsent(arr[i]) { mutableListOf() }.add(i)
        }

        val visited = BooleanArray(n)
        val queue: ArrayDeque<Int> = ArrayDeque()
        queue.add(0)
        visited[0] = true
        var steps = 0

        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val idx = queue.removeFirst()
                if (idx == n - 1) return steps

                // Jump to all same-value indices
                posMap[arr[idx]]?.let { list ->
                    for (j in list) {
                        if (!visited[j]) {
                            visited[j] = true
                            queue.add(j)
                        }
                    }
                    // Prevent future redundant processing
                    posMap.remove(arr[idx])
                }

                // Jump to idx - 1
                if (idx - 1 >= 0 && !visited[idx - 1]) {
                    visited[idx - 1] = true
                    queue.add(idx - 1)
                }
                // Jump to idx + 1
                if (idx + 1 < n && !visited[idx + 1]) {
                    visited[idx + 1] = true
                    queue.add(idx + 1)
                }
            }
            steps++
        }

        return -1 // Should never reach here for valid input
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minJumps(List<int> arr) {
    int n = arr.length;
    if (n <= 1) return 0;

    // Map each value to all its indices.
    final Map<int, List<int>> pos = {};
    for (int i = 0; i < n; i++) {
      pos.putIfAbsent(arr[i], () => []).add(i);
    }

    final List<bool> visited = List.filled(n, false);
    visited[0] = true;

    final Queue<int> q = Queue<int>();
    q.addLast(0);
    int steps = 0;

    while (q.isNotEmpty) {
      int size = q.length;
      for (int i = 0; i < size; i++) {
        int cur = q.removeFirst();
        if (cur == n - 1) return steps;

        // Jump to all indices with the same value.
        if (pos.containsKey(arr[cur])) {
          for (int nxt in pos[arr[cur]]!) {
            if (!visited[nxt]) {
              visited[nxt] = true;
              q.addLast(nxt);
            }
          }
          // Prevent future redundant processing of this value.
          pos.remove(arr[cur]);
        }

        // Jump to adjacent indices.
        if (cur - 1 >= 0 && !visited[cur - 1]) {
          visited[cur - 1] = true;
          q.addLast(cur - 1);
        }
        if (cur + 1 < n && !visited[cur + 1]) {
          visited[cur + 1] = true;
          q.addLast(cur + 1);
        }
      }
      steps++;
    }

    return -1; // Unreachable (per problem constraints this line never executes)
  }
}
```

## Golang

```go
func minJumps(arr []int) int {
	if len(arr) <= 1 {
		return 0
	}
	n := len(arr)
	graph := make(map[int][]int, n)
	for i, v := range arr {
		graph[v] = append(graph[v], i)
	}
	visited := make([]bool, n)
	queue := []int{0}
	visited[0] = true
	steps := 0

	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			if cur == n-1 {
				return steps
			}
			var nextIndices []int
			if cur-1 >= 0 {
				nextIndices = append(nextIndices, cur-1)
			}
			if cur+1 < n {
				nextIndices = append(nextIndices, cur+1)
			}
			if sameVals, ok := graph[arr[cur]]; ok {
				nextIndices = append(nextIndices, sameVals...)
				delete(graph, arr[cur])
			}
			for _, nxt := range nextIndices {
				if !visited[nxt] {
					visited[nxt] = true
					queue = append(queue, nxt)
				}
			}
		}
		steps++
	}
	return -1
}
```

## Ruby

```ruby
def min_jumps(arr)
  n = arr.length
  return 0 if n <= 1

  # map each value to list of its indices
  idx_map = Hash.new { |h, k| h[k] = [] }
  arr.each_with_index { |v, i| idx_map[v] << i }

  visited = Array.new(n, false)
  visited[0] = true

  queue = [0]
  steps = 0

  until queue.empty?
    next_queue = []
    queue.each do |i|
      return steps if i == n - 1

      # neighbor i-1
      if i - 1 >= 0 && !visited[i - 1]
        visited[i - 1] = true
        next_queue << i - 1
      end

      # neighbor i+1
      if i + 1 < n && !visited[i + 1]
        visited[i + 1] = true
        next_queue << i + 1
      end

      # all same-value indices
      if idx_map.key?(arr[i])
        idx_map[arr[i]].each do |j|
          unless visited[j]
            visited[j] = true
            next_queue << j
          end
        end
        idx_map.delete(arr[i]) # avoid future redundant work
      end
    end
    queue = next_queue
    steps += 1
  end

  -1
end
```

## Scala

```scala
object Solution {
  def minJumps(arr: Array[Int]): Int = {
    val n = arr.length
    if (n <= 1) return 0

    import scala.collection.mutable.{ArrayBuffer, HashMap, ArrayDeque}

    // map each value to list of indices having that value
    val idxMap = new HashMap[Int, ArrayBuffer[Int]]()
    for (i <- 0 until n) {
      idxMap.getOrElseUpdate(arr(i), ArrayBuffer.empty[Int]) += i
    }

    val visited = Array.fill[Boolean](n)(false)
    visited(0) = true

    val queue = new ArrayDeque[Int]()
    queue.append(0)

    var steps = 0
    while (queue.nonEmpty) {
      val size = queue.size
      for (_ <- 0 until size) {
        val cur = queue.removeHead()
        if (cur == n - 1) return steps

        // jump to same value indices
        idxMap.get(arr(cur)) match {
          case Some(list) =>
            for (j <- list) {
              if (!visited(j)) {
                visited(j) = true
                queue.append(j)
              }
            }
            // clear to prevent future redundant checks
            idxMap.remove(arr(cur))
          case None => // nothing
        }

        // jump to cur - 1
        val left = cur - 1
        if (left >= 0 && !visited(left)) {
          visited(left) = true
          queue.append(left)
        }
        // jump to cur + 1
        val right = cur + 1
        if (right < n && !visited(right)) {
          visited(right) = true
          queue.append(right)
        }
      }
      steps += 1
    }

    -1 // should never reach here
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n <= 1 {
            return 0;
        }
        use std::collections::{HashMap, VecDeque};

        // Map each value to all indices having that value
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            pos.entry(v).or_default().push(i);
        }

        let mut visited = vec![false; n];
        visited[0] = true;
        let mut queue: VecDeque<usize> = VecDeque::new();
        queue.push_back(0);
        let mut steps: i32 = 0;

        while !queue.is_empty() {
            let layer_size = queue.len();
            for _ in 0..layer_size {
                let idx = queue.pop_front().unwrap();
                if idx == n - 1 {
                    return steps;
                }

                // neighbor idx-1
                if idx > 0 && !visited[idx - 1] {
                    visited[idx - 1] = true;
                    queue.push_back(idx - 1);
                }
                // neighbor idx+1
                if idx + 1 < n && !visited[idx + 1] {
                    visited[idx + 1] = true;
                    queue.push_back(idx + 1);
                }

                // all same-value indices
                if let Some(same) = pos.get(&arr[idx]) {
                    for &j in same.iter() {
                        if !visited[j] {
                            visited[j] = true;
                            queue.push_back(j);
                        }
                    }
                }
                // prevent future redundant processing of this value
                pos.remove(&arr[idx]);
            }
            steps += 1;
        }

        steps
    }
}
```

## Racket

```racket
(define/contract (min-jumps arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (if (<= n 1) 
        0
        (call/cc
          (lambda (return)
            ;; map value -> list of indices having that value
            (define h (make-hash))
            (for ([i (in-range n)])
              (let* ((val (vector-ref v i))
                     (lst (hash-ref h val '())))
                (hash-set! h val (cons i lst))))
            ;; visited flags
            (define visited (make-vector n #f))
            ;; BFS queue implemented with a vector and two pointers
            (define queue (make-vector n 0))
            (define front 0)
            (define back 0)
            (define steps 0)
            ;; start from index 0
            (vector-set! visited 0 #t)
            (vector-set! queue back 0)
            (set! back (+ back 1))
            ;; BFS loop
            (let loop ()
              (when (< front back)
                (let ((size (- back front)))
                  (for ([k (in-range size)])
                    (define i (vector-ref queue front))
                    (set! front (+ front 1))
                    (when (= i (- n 1))
                      (return steps))
                    ;; jump to same value indices
                    (let* ((val (vector-ref v i))
                           (same (hash-ref h val '())))
                      (for ([j same])
                        (unless (vector-ref visited j)
                          (vector-set! visited j #t)
                          (vector-set! queue back j)
                          (set! back (+ back 1))))
                      ;; clear to avoid revisiting
                      (hash-set! h val '()))
                    ;; jump to i-1
                    (when (and (> i 0) (not (vector-ref visited (- i 1))))
                      (vector-set! visited (- i 1) #t)
                      (vector-set! queue back (- i 1))
                      (set! back (+ back 1)))
                    ;; jump to i+1
                    (when (and (< i (- n 1)) (not (vector-ref visited (+ i 1))))
                      (vector-set! visited (+ i 1) #t)
                      (vector-set! queue back (+ i 1))
                      (set! back (+ back 1)))))
                (set! steps (+ steps 1))
                (loop)))
            -1))))
```

## Erlang

```erlang
-export([min_jumps/1]).

-spec min_jumps(Arr :: [integer()]) -> integer().
min_jumps(Arr) ->
    case length(Arr) of
        0 -> 0;
        1 -> 0;
        N ->
            ArrArray = array:from_list(Arr),
            ValueMap = build_map(Arr, 0, #{}),
            Q0 = :queue.in({0, 0}, :queue.new()),
            Vis0 = maps:put(0, true, #{}),
            bfs(Q0, Vis0, ValueMap, N, ArrArray)
    end.

build_map([], _, M) -> M;
build_map([H | T], I, M) ->
    Updated = maps:update_with(
        H,
        fun(L) -> [I | L] end,
        [I],
        M),
    build_map(T, I + 1, Updated).

bfs(Queue, Visited, ValueMap, N, ArrArray) ->
    case :queue.out(Queue) of
        {empty, _} ->
            -1;
        {{value, {Idx, Steps}}, QRest} ->
            if Idx =:= N - 1 ->
                    Steps;
               true ->
                    NewSteps = Steps + 1,
                    {Q1, Vis1, VMap1} = add_index(Idx + 1, NewSteps, QRest, Visited, ValueMap, N),
                    {Q2, Vis2, VMap2} = add_index(Idx - 1, NewSteps, Q1, Vis1, VMap1, N),
                    Val = array:get(Idx, ArrArray),
                    SameList = maps:get(Val, VMap2, []),
                    {Q3, Vis3} = add_same(SameList, NewSteps, Q2, Vis2),
                    VMap3 = maps:remove(Val, VMap2),
                    bfs(Q3, Vis3, VMap3, N, ArrArray)
            end
    end.

add_index(Index, Steps, Queue, Visited, ValueMap, N) ->
    if Index >= 0, Index < N,
       not maps:is_key(Index, Visited) ->
            Q1 = :queue.in({Index, Steps}, Queue),
            V1 = maps:put(Index, true, Visited),
            {Q1, V1, ValueMap};
       true ->
            {Queue, Visited, ValueMap}
    end.

add_same([], _Steps, Queue, Visited) -> {Queue, Visited};
add_same([J | Rest], Steps, Queue, Visited) ->
    case maps:is_key(J, Visited) of
        true ->
            add_same(Rest, Steps, Queue, Visited);
        false ->
            Q1 = :queue.in({J, Steps}, Queue),
            V1 = maps:put(J, true, Visited),
            add_same(Rest, Steps, Q1, V1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_jumps(arr :: [integer]) :: integer
  def min_jumps(arr) do
    n = length(arr)

    if n <= 1 do
      0
    else
      arr_tuple = List.to_tuple(arr)

      val_map =
        Enum.with_index(arr)
        |> Enum.reduce(%{}, fn {v, i}, acc ->
          Map.update(acc, v, [i], &[i | &1])
        end)

      visited = MapSet.new([0])
      queue = :queue.new() |> :queue.in({0, 0})
      bfs(queue, visited, val_map, arr_tuple, n - 1)
    end
  end

  defp bfs(queue, visited, val_map, arr_tuple, target) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {idx, steps}}, q2} ->
        if idx == target do
          steps
        else
          # left neighbor
          {q, vis} =
            if idx > 0 and not MapSet.member?(visited, idx - 1) do
              {:queue.in({idx - 1, steps + 1}, q2), MapSet.put(visited, idx - 1)}
            else
              {q2, visited}
            end

          # right neighbor
          {q, vis} =
            if idx + 1 < tuple_size(arr_tuple) and not MapSet.member?(vis, idx + 1) do
              {:queue.in({idx + 1, steps + 1}, q), MapSet.put(vis, idx + 1)}
            else
              {q, vis}
            end

          # same value jumps
          val = elem(arr_tuple, idx)
          same_indices = Map.get(val_map, val, [])

          {q, vis} =
            Enum.reduce(same_indices, {q, vis}, fn j, {q_acc, vis_acc} ->
              if MapSet.member?(vis_acc, j) do
                {q_acc, vis_acc}
              else
                {:queue.in({j, steps + 1}, q_acc), MapSet.put(vis_acc, j)}
              end
            end)

          new_val_map = Map.delete(val_map, val)
          bfs(q, vis, new_val_map, arr_tuple, target)
        end
    end
  end
end
```
