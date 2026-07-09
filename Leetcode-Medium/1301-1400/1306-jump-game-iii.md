# 1306. Jump Game III

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        vector<char> visited(n, 0);
        queue<int> q;
        q.push(start);
        visited[start] = 1;
        while (!q.empty()) {
            int i = q.front(); q.pop();
            if (arr[i] == 0) return true;
            int jump = arr[i];
            int nxt = i + jump;
            if (nxt < n && !visited[nxt]) {
                visited[nxt] = 1;
                q.push(nxt);
            }
            nxt = i - jump;
            if (nxt >= 0 && !visited[nxt]) {
                visited[nxt] = 1;
                q.push(nxt);
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean canReach(int[] arr, int start) {
        int n = arr.length;
        boolean[] visited = new boolean[n];
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int idx = queue.poll();
            if (arr[idx] == 0) {
                return true;
            }
            int jump = arr[idx];

            int next = idx + jump;
            if (next < n && !visited[next]) {
                visited[next] = true;
                queue.add(next);
            }

            next = idx - jump;
            if (next >= 0 && !visited[next]) {
                visited[next] = true;
                queue.add(next);
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        from collections import deque

        n = len(arr)
        visited = [False] * n
        q = deque([start])
        visited[start] = True

        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            jump = arr[i]
            for nxt in (i + jump, i - jump):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        return False
```

## Python3

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        from collections import deque
        q = deque([start])
        while q:
            i = q.popleft()
            if visited[i]:
                continue
            visited[i] = True
            if arr[i] == 0:
                return True
            jump = arr[i]
            for nxt in (i + jump, i - jump):
                if 0 <= nxt < n and not visited[nxt]:
                    q.append(nxt)
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool canReach(int* arr, int arrSize, int start) {
    char *visited = (char *)calloc(arrSize, sizeof(char));
    if (!visited) return false;

    int *queue = (int *)malloc(sizeof(int) * arrSize);
    if (!queue) {
        free(visited);
        return false;
    }

    int head = 0, tail = 0;
    queue[tail++] = start;
    visited[start] = 1;

    while (head < tail) {
        int idx = queue[head++];
        if (arr[idx] == 0) {
            free(visited);
            free(queue);
            return true;
        }

        int jump = arr[idx];
        int next = idx + jump;
        if (next < arrSize && !visited[next]) {
            visited[next] = 1;
            queue[tail++] = next;
        }
        next = idx - jump;
        if (next >= 0 && !visited[next]) {
            visited[next] = 1;
            queue[tail++] = next;
        }
    }

    free(visited);
    free(queue);
    return false;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public bool CanReach(int[] arr, int start) {
        int n = arr.Length;
        var visited = new bool[n];
        var queue = new Queue<int>();
        queue.Enqueue(start);
        visited[start] = true;

        while (queue.Count > 0) {
            int i = queue.Dequeue();
            if (arr[i] == 0) return true;

            int jump = arr[i];

            int next = i + jump;
            if (next < n && !visited[next]) {
                visited[next] = true;
                queue.Enqueue(next);
            }

            next = i - jump;
            if (next >= 0 && !visited[next]) {
                visited[next] = true;
                queue.Enqueue(next);
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    const n = arr.length;
    const visited = new Array(n).fill(false);
    const stack = [start];
    
    while (stack.length) {
        const i = stack.pop();
        if (visited[i]) continue;
        visited[i] = true;
        if (arr[i] === 0) return true;
        const jump = arr[i];
        const left = i - jump;
        const right = i + jump;
        if (left >= 0 && !visited[left]) stack.push(left);
        if (right < n && !visited[right]) stack.push(right);
    }
    
    return false;
};
```

## Typescript

```typescript
function canReach(arr: number[], start: number): boolean {
    const n = arr.length;
    const visited = new Array<boolean>(n).fill(false);
    const stack: number[] = [start];
    
    while (stack.length) {
        const i = stack.pop()!;
        if (visited[i]) continue;
        visited[i] = true;
        if (arr[i] === 0) return true;
        
        const left = i - arr[i];
        const right = i + arr[i];
        if (left >= 0 && !visited[left]) stack.push(left);
        if (right < n && !visited[right]) stack.push(right);
    }
    
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $start
     * @return Boolean
     */
    function canReach($arr, $start) {
        $n = count($arr);
        $visited = array_fill(0, $n, false);
        $queue = new SplQueue();
        $queue->enqueue($start);
        $visited[$start] = true;

        while (!$queue->isEmpty()) {
            $i = $queue->dequeue();
            if ($arr[$i] == 0) {
                return true;
            }

            $next = $i + $arr[$i];
            if ($next < $n && !$visited[$next]) {
                $visited[$next] = true;
                $queue->enqueue($next);
            }

            $prev = $i - $arr[$i];
            if ($prev >= 0 && !$visited[$prev]) {
                $visited[$prev] = true;
                $queue->enqueue($prev);
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canReach(_ arr: [Int], _ start: Int) -> Bool {
        let n = arr.count
        var visited = [Bool](repeating: false, count: n)
        var queue = [Int]()
        var head = 0

        queue.append(start)
        visited[start] = true

        while head < queue.count {
            let i = queue[head]
            head += 1
            if arr[i] == 0 { return true }
            let jump = arr[i]

            let forward = i + jump
            if forward < n && !visited[forward] {
                visited[forward] = true
                queue.append(forward)
            }

            let backward = i - jump
            if backward >= 0 && !visited[backward] {
                visited[backward] = true
                queue.append(backward)
            }
        }

        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canReach(arr: IntArray, start: Int): Boolean {
        val n = arr.size
        val visited = BooleanArray(n)
        val queue = ArrayDeque<Int>()
        queue.add(start)
        visited[start] = true

        while (queue.isNotEmpty()) {
            val i = queue.removeFirst()
            if (arr[i] == 0) return true
            val jump = arr[i]

            var next = i + jump
            if (next < n && !visited[next]) {
                visited[next] = true
                queue.add(next)
            }

            next = i - jump
            if (next >= 0 && !visited[next]) {
                visited[next] = true
                queue.add(next)
            }
        }
        return false
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  bool canReach(List<int> arr, int start) {
    int n = arr.length;
    List<bool> visited = List.filled(n, false);
    Queue<int> queue = Queue<int>();
    queue.add(start);
    visited[start] = true;

    while (queue.isNotEmpty) {
      int i = queue.removeFirst();
      if (arr[i] == 0) return true;

      int jump = arr[i];
      int next = i + jump;
      if (next < n && !visited[next]) {
        visited[next] = true;
        queue.add(next);
      }
      next = i - jump;
      if (next >= 0 && !visited[next]) {
        visited[next] = true;
        queue.add(next);
      }
    }

    return false;
  }
}
```

## Golang

```go
func canReach(arr []int, start int) bool {
    n := len(arr)
    visited := make([]bool, n)
    queue := []int{start}
    visited[start] = true

    for i := 0; i < len(queue); i++ {
        idx := queue[i]
        if arr[idx] == 0 {
            return true
        }
        step := arr[idx]

        next := idx + step
        if next < n && !visited[next] {
            visited[next] = true
            queue = append(queue, next)
        }

        prev := idx - step
        if prev >= 0 && !visited[prev] {
            visited[prev] = true
            queue = append(queue, prev)
        }
    }
    return false
}
```

## Ruby

```ruby
def can_reach(arr, start)
  n = arr.length
  visited = Array.new(n, false)
  stack = [start]

  until stack.empty?
    i = stack.pop
    next if visited[i]

    return true if arr[i] == 0

    visited[i] = true
    jump = arr[i]
    left = i - jump
    right = i + jump

    stack << left if left >= 0 && !visited[left]
    stack << right if right < n && !visited[right]
  end

  false
end
```

## Scala

```scala
object Solution {
    def canReach(arr: Array[Int], start: Int): Boolean = {
        val n = arr.length
        val visited = new Array[Boolean](n)
        val queue = new java.util.ArrayDeque[Int]()
        queue.add(start)
        visited(start) = true

        while (!queue.isEmpty) {
            val i = queue.poll()
            if (arr(i) == 0) return true
            val jump = arr(i)

            val forward = i + jump
            if (forward >= 0 && forward < n && !visited(forward)) {
                visited(forward) = true
                queue.add(forward)
            }

            val backward = i - jump
            if (backward >= 0 && backward < n && !visited(backward)) {
                visited(backward) = true
                queue.add(backward)
            }
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        use std::collections::VecDeque;
        let n = arr.len();
        if n == 0 {
            return false;
        }
        let start_idx = start as usize;
        let mut visited = vec![false; n];
        let mut queue = VecDeque::new();
        visited[start_idx] = true;
        queue.push_back(start_idx);
        while let Some(i) = queue.pop_front() {
            if arr[i] == 0 {
                return true;
            }
            let jump = arr[i] as usize;
            // forward
            let next = i + jump;
            if next < n && !visited[next] {
                visited[next] = true;
                queue.push_back(next);
            }
            // backward
            if i >= jump {
                let prev = i - jump;
                if !visited[prev] {
                    visited[prev] = true;
                    queue.push_back(prev);
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (can-reach arr start)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (let ([visited (make-vector n #f)]
          [queue   (make-vector n -1)]
          [head    0]
          [tail    0])
      (vector-set! visited start #t)
      (vector-set! queue tail start)
      (set! tail (+ tail 1))
      (let loop ()
        (if (= head tail)
            #f
            (let ((i (vector-ref queue head)))
              (set! head (+ head 1))
              (if (= (vector-ref v i) 0)
                  #t
                  (let ((step (vector-ref v i)))
                    (for ([j (list (+ i step) (- i step))])
                      (when (and (>= j 0) (< j n) (not (vector-ref visited j)))
                        (vector-set! visited j #t)
                        (vector-set! queue tail j)
                        (set! tail (+ tail 1))))
                    (loop)))))))))
```

## Erlang

```erlang
-module(solution).
-export([can_reach/2]).

-spec can_reach(Arr :: [integer()], Start :: integer()) -> boolean().
can_reach(Arr, Start) ->
    Tuple = list_to_tuple(Arr),
    Len = tuple_size(Tuple),
    Visited0 = maps:put(Start, true, #{}),
    Queue0 = queue:in(Start, queue:new()),
    bfs(Queue0, Tuple, Len, Visited0).

bfs(Queue, Tuple, Len, Visited) ->
    case queue:out(Queue) of
        {empty, _} ->
            false;
        {{value, Pos}, RestQueue} ->
            Value = element(Pos + 1, Tuple),
            if
                Value == 0 ->
                    true;
                true ->
                    Nexts = [Pos - Value, Pos + Value],
                    {NewQueue, NewVisited} =
                        lists:foldl(
                            fun(N, {QAcc, VAcc}) ->
                                case (N >= 0) andalso (N < Len) andalso not maps:is_key(N, VAcc) of
                                    true ->
                                        {queue:in(N, QAcc), maps:put(N, true, VAcc)};
                                    false ->
                                        {QAcc, VAcc}
                                end
                            end,
                            {RestQueue, Visited},
                            Nexts),
                    bfs(NewQueue, Tuple, Len, NewVisited)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_reach(arr :: [integer], start :: integer) :: boolean
  def can_reach(arr, start) do
    n = length(arr)
    arr_t = List.to_tuple(arr)

    visited = MapSet.new([start])
    queue = :queue.from_list([start])

    bfs(queue, visited, arr_t, n)
  end

  defp bfs(queue, visited, arr_t, n) do
    case :queue.out(queue) do
      {:empty, _} ->
        false

      {{:value, idx}, q2} ->
        if elem(arr_t, idx) == 0 do
          true
        else
          step = elem(arr_t, idx)
          next_idxs = [idx + step, idx - step]

          {new_queue, new_visited} =
            Enum.reduce(next_idxs, {q2, visited}, fn ni, {qq, vv} ->
              if ni >= 0 and ni < n and not MapSet.member?(vv, ni) do
                {:queue.in(ni, qq), MapSet.put(vv, ni)}
              else
                {qq, vv}
              end
            end)

          bfs(new_queue, new_visited, arr_t, n)
        end
    end
  end
end
```
