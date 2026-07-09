# 2059. Minimum Operations to Convert Number

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums, int start, int goal) {
        const int LIMIT = 1000;
        vector<bool> visited(LIMIT + 1, false);
        queue<pair<int,int>> q;
        if (start == goal) return 0; // though problem guarantees start != goal
        visited[start] = true;
        q.emplace(start, 0);
        while (!q.empty()) {
            auto [cur, steps] = q.front();
            q.pop();
            for (int v : nums) {
                int nxt[3] = {cur + v, cur - v, cur ^ v};
                for (int i = 0; i < 3; ++i) {
                    int x = nxt[i];
                    if (x == goal) return steps + 1;
                    if (0 <= x && x <= LIMIT && !visited[x]) {
                        visited[x] = true;
                        q.emplace(x, steps + 1);
                    }
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(int[] nums, int start, int goal) {
        if (start == goal) return 0;
        boolean[] visited = new boolean[1001];
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        visited[start] = true;
        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int cur = queue.poll();
                for (int num : nums) {
                    int[] nextVals = {cur + num, cur - num, cur ^ num};
                    for (int nxt : nextVals) {
                        if (nxt == goal) return steps + 1;
                        if (0 <= nxt && nxt <= 1000 && !visited[nxt]) {
                            visited[nxt] = true;
                            queue.offer(nxt);
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        from collections import deque

        if start == goal:
            return 0

        visited = [False] * 1001
        q = deque()
        q.append((start, 0))
        visited[start] = True

        while q:
            x, steps = q.popleft()
            for num in nums:
                for nxt in (x + num, x - num, x ^ num):
                    if nxt == goal:
                        return steps + 1
                    if 0 <= nxt <= 1000 and not visited[nxt]:
                        visited[nxt] = True
                        q.append((nxt, steps + 1))
        return -1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = [False] * 1001
        q = deque()
        q.append((start, 0))
        if 0 <= start <= 1000:
            visited[start] = True

        while q:
            x, steps = q.popleft()
            for num in nums:
                # addition
                nx = x + num
                if nx == goal:
                    return steps + 1
                if 0 <= nx <= 1000 and not visited[nx]:
                    visited[nx] = True
                    q.append((nx, steps + 1))
                # subtraction
                nx = x - num
                if nx == goal:
                    return steps + 1
                if 0 <= nx <= 1000 and not visited[nx]:
                    visited[nx] = True
                    q.append((nx, steps + 1))
                # xor
                nx = x ^ num
                if nx == goal:
                    return steps + 1
                if 0 <= nx <= 1000 and not visited[nx]:
                    visited[nx] = True
                    q.append((nx, steps + 1))

        return -1
```

## C

```c
#include <stddef.h>

int minimumOperations(int* nums, int numsSize, int start, int goal) {
    if (start == goal) return 0;
    char visited[1001] = {0};
    int qVal[2005];
    int qStep[2005];
    int head = 0, tail = 0;

    qVal[tail] = start;
    qStep[tail] = 0;
    tail++;
    visited[start] = 1;

    while (head < tail) {
        int x = qVal[head];
        int steps = qStep[head];
        head++;

        for (int i = 0; i < numsSize; ++i) {
            int y;

            // addition
            y = x + nums[i];
            if (y == goal) return steps + 1;
            if (y >= 0 && y <= 1000 && !visited[y]) {
                visited[y] = 1;
                qVal[tail] = y;
                qStep[tail] = steps + 1;
                tail++;
            }

            // subtraction
            y = x - nums[i];
            if (y == goal) return steps + 1;
            if (y >= 0 && y <= 1000 && !visited[y]) {
                visited[y] = 1;
                qVal[tail] = y;
                qStep[tail] = steps + 1;
                tail++;
            }

            // xor
            y = x ^ nums[i];
            if (y == goal) return steps + 1;
            if (y >= 0 && y <= 1000 && !visited[y]) {
                visited[y] = 1;
                qVal[tail] = y;
                qStep[tail] = steps + 1;
                tail++;
            }
        }
    }

    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperations(int[] nums, int start, int goal) {
        const int MIN = 0;
        const int MAX = 1000;
        int[] dist = new int[MAX + 1];
        for (int i = 0; i <= MAX; i++) dist[i] = -1;

        var q = new System.Collections.Generic.Queue<int>();
        q.Enqueue(start);
        dist[start] = 0;

        while (q.Count > 0) {
            int x = q.Dequeue();
            int d = dist[x];

            foreach (int num in nums) {
                // addition
                long add = (long)x + num;
                if (add == goal) return d + 1;
                if (add >= MIN && add <= MAX && dist[(int)add] == -1) {
                    dist[(int)add] = d + 1;
                    q.Enqueue((int)add);
                }

                // subtraction
                long sub = (long)x - num;
                if (sub == goal) return d + 1;
                if (sub >= MIN && sub <= MAX && dist[(int)sub] == -1) {
                    dist[(int)sub] = d + 1;
                    q.Enqueue((int)sub);
                }

                // xor
                int xor = x ^ num;
                if (xor == goal) return d + 1;
                if (xor >= MIN && xor <= MAX && dist[xor] == -1) {
                    dist[xor] = d + 1;
                    q.Enqueue(xor);
                }
            }
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minimumOperations = function(nums, start, goal) {
    const MAX = 1000;
    if (start === goal) return 0; // just in case
    
    const visited = new Array(MAX + 1).fill(false);
    const queue = [];
    let head = 0;
    
    queue.push([start, 0]);
    visited[start] = true;
    
    while (head < queue.length) {
        const [cur, steps] = queue[head++];
        for (const num of nums) {
            const candidates = [cur + num, cur - num, cur ^ num];
            for (const nxt of candidates) {
                if (nxt === goal) return steps + 1;
                if (nxt >= 0 && nxt <= MAX && !visited[nxt]) {
                    visited[nxt] = true;
                    queue.push([nxt, steps + 1]);
                }
            }
        }
    }
    
    return -1;
};
```

## Typescript

```typescript
function minimumOperations(nums: number[], start: number, goal: number): number {
    const LIMIT = 1000;
    if (start === goal) return 0;

    const visited = new Array(LIMIT + 1).fill(false);
    const qVal: number[] = [];
    const qStep: number[] = [];
    let head = 0;

    visited[start] = true;
    qVal.push(start);
    qStep.push(0);

    while (head < qVal.length) {
        const x = qVal[head];
        const steps = qStep[head];
        head++;

        for (const num of nums) {
            const candidates = [x + num, x - num, x ^ num];
            for (const nx of candidates) {
                if (nx === goal) return steps + 1;
                if (0 <= nx && nx <= LIMIT && !visited[nx]) {
                    visited[nx] = true;
                    qVal.push(nx);
                    qStep.push(steps + 1);
                }
            }
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $start
     * @param Integer $goal
     * @return Integer
     */
    function minimumOperations($nums, $start, $goal) {
        $queue = new SplQueue();
        $visited = array_fill(0, 1001, false);
        $queue->enqueue([$start, 0]);
        $visited[$start] = true;

        while (!$queue->isEmpty()) {
            [$x, $steps] = $queue->dequeue();

            foreach ($nums as $num) {
                // addition
                $nx = $x + $num;
                if ($nx == $goal) return $steps + 1;
                if ($nx >= 0 && $nx <= 1000 && !$visited[$nx]) {
                    $visited[$nx] = true;
                    $queue->enqueue([$nx, $steps + 1]);
                }

                // subtraction
                $nx = $x - $num;
                if ($nx == $goal) return $steps + 1;
                if ($nx >= 0 && $nx <= 1000 && !$visited[$nx]) {
                    $visited[$nx] = true;
                    $queue->enqueue([$nx, $steps + 1]);
                }

                // xor
                $nx = $x ^ $num;
                if ($nx == $goal) return $steps + 1;
                if ($nx >= 0 && $nx <= 1000 && !$visited[$nx]) {
                    $visited[$nx] = true;
                    $queue->enqueue([$nx, $steps + 1]);
                }
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int], _ start: Int, _ goal: Int) -> Int {
        var visited = Array(repeating: false, count: 1001)
        var queue: [(Int, Int)] = []
        queue.append((start, 0))
        if start >= 0 && start <= 1000 {
            visited[start] = true
        }
        var index = 0
        while index < queue.count {
            let (x, steps) = queue[index]
            index += 1
            for num in nums {
                let candidates = [x + num, x - num, x ^ num]
                for nx in candidates {
                    if nx == goal { return steps + 1 }
                    if nx >= 0 && nx <= 1000 && !visited[nx] {
                        visited[nx] = true
                        queue.append((nx, steps + 1))
                    }
                }
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray, start: Int, goal: Int): Int {
        val max = 1000
        val visited = BooleanArray(max + 1)
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        queue.add(Pair(start, 0))
        visited[start] = true

        while (queue.isNotEmpty()) {
            val (x, steps) = queue.removeFirst()
            for (num in nums) {
                var nx = x + num
                if (nx == goal) return steps + 1
                if (nx in 0..max && !visited[nx]) {
                    visited[nx] = true
                    queue.add(Pair(nx, steps + 1))
                }

                nx = x - num
                if (nx == goal) return steps + 1
                if (nx in 0..max && !visited[nx]) {
                    visited[nx] = true
                    queue.add(Pair(nx, steps + 1))
                }

                nx = x xor num
                if (nx == goal) return steps + 1
                if (nx in 0..max && !visited[nx]) {
                    visited[nx] = true
                    queue.add(Pair(nx, steps + 1))
                }
            }
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minimumOperations(List<int> nums, int start, int goal) {
    const int MIN = 0;
    const int MAX = 1000;
    List<int> dist = List.filled(MAX + 1, -1);
    Queue<int> q = Queue<int>();
    dist[start] = 0;
    q.add(start);

    while (q.isNotEmpty) {
      int cur = q.removeFirst();
      int curDist = dist[cur];
      for (int num in nums) {
        // addition
        int nxt = cur + num;
        if (nxt == goal) return curDist + 1;
        if (nxt >= MIN && nxt <= MAX && dist[nxt] == -1) {
          dist[nxt] = curDist + 1;
          q.add(nxt);
        }
        // subtraction
        nxt = cur - num;
        if (nxt == goal) return curDist + 1;
        if (nxt >= MIN && nxt <= MAX && dist[nxt] == -1) {
          dist[nxt] = curDist + 1;
          q.add(nxt);
        }
        // xor
        nxt = cur ^ num;
        if (nxt == goal) return curDist + 1;
        if (nxt >= MIN && nxt <= MAX && dist[nxt] == -1) {
          dist[nxt] = curDist + 1;
          q.add(nxt);
        }
      }
    }

    return -1;
  }
}
```

## Golang

```go
func minimumOperations(nums []int, start int, goal int) int {
	const limit = 1000
	visited := make([]bool, limit+1)
	type node struct {
		val   int
		steps int
	}
	queue := []node{{start, 0}}
	if start == goal {
		return 0
	}
	visited[start] = true

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		for _, num := range nums {
			candidates := []int{cur.val + num, cur.val - num, cur.val ^ num}
			for _, nxt := range candidates {
				if nxt == goal {
					return cur.steps + 1
				}
				if nxt >= 0 && nxt <= limit && !visited[nxt] {
					visited[nxt] = true
					queue = append(queue, node{nxt, cur.steps + 1})
				}
			}
		}
	}
	return -1
}
```

## Ruby

```ruby
def minimum_operations(nums, start, goal)
  max_val = 1000
  return 0 if start == goal

  visited = Array.new(max_val + 1, false)
  queue = [[start, 0]]
  visited[start] = true
  head = 0

  while head < queue.length
    x, steps = queue[head]
    head += 1

    nums.each do |num|
      # addition
      y = x + num
      return steps + 1 if y == goal
      if y.between?(0, max_val) && !visited[y]
        visited[y] = true
        queue << [y, steps + 1]
      end

      # subtraction
      y = x - num
      return steps + 1 if y == goal
      if y.between?(0, max_val) && !visited[y]
        visited[y] = true
        queue << [y, steps + 1]
      end

      # xor
      y = x ^ num
      return steps + 1 if y == goal
      if y.between?(0, max_val) && !visited[y]
        visited[y] = true
        queue << [y, steps + 1]
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int], start: Int, goal: Int): Int = {
        val maxVal = 1000
        val visited = new Array[Boolean](maxVal + 1)
        import scala.collection.mutable.ArrayDeque
        val queue = ArrayDeque[(Int, Int)]()
        if (start >= 0 && start <= maxVal) {
            visited(start) = true
            queue.append((start, 0))
        }
        while (queue.nonEmpty) {
            val (x, steps) = queue.removeHead()
            for (num <- nums) {
                val candidates = Array(x + num, x - num, x ^ num)
                for (next <- candidates) {
                    if (next == goal) return steps + 1
                    if (next >= 0 && next <= maxVal && !visited(next)) {
                        visited(next) = true
                        queue.append((next, steps + 1))
                    }
                }
            }
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>, start: i32, goal: i32) -> i32 {
        use std::collections::VecDeque;
        const LIMIT: i32 = 1000;
        let mut visited = vec![false; (LIMIT + 1) as usize];
        let mut queue = VecDeque::new();

        if start >= 0 && start <= LIMIT {
            visited[start as usize] = true;
            queue.push_back((start, 0));
        }

        while let Some((x, steps)) = queue.pop_front() {
            for &num in &nums {
                let candidates = [x + num, x - num, x ^ num];
                for &next in &candidates {
                    if next == goal {
                        return steps + 1;
                    }
                    if next >= 0 && next <= LIMIT {
                        let idx = next as usize;
                        if !visited[idx] {
                            visited[idx] = true;
                            queue.push_back((next, steps + 1));
                        }
                    }
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(define/contract (minimum-operations nums start goal)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let/ec return
    (when (= start goal) (return 0))
    (define visited (make-vector 1001 #f))
    (vector-set! visited start #t)
    (define queue (make-vector 2005 #f)) ; enough for all possible states
    (define head 0)
    (define tail 0)
    (vector-set! queue tail (cons start 0))
    (set! tail (+ tail 1))
    (let loop ()
      (if (= head tail)
          (return -1)
          (let* ([pair (vector-ref queue head)]
                 [cur (car pair)]
                 [steps (cdr pair)])
            (set! head (+ head 1))
            (for ([num nums])
              (for ([op (list '+ '- 'xor)])
                (define new
                  (cond [(eq? op '+) (+ cur num)]
                        [(eq? op '-) (- cur num)]
                        [else (bitwise-xor cur num)]))
                (when (= new goal)
                  (return (+ steps 1)))
                (when (and (>= new 0) (<= new 1000) (not (vector-ref visited new)))
                  (vector-set! visited new #t)
                  (vector-set! queue tail (cons new (+ steps 1)))
                  (set! tail (+ tail 1)))))
            (loop))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations/3]).

-spec minimum_operations(Nums :: [integer()], Start :: integer(), Goal :: integer()) -> integer().
minimum_operations(Nums, Start, Goal) ->
    Vis0 = case (Start >= 0 andalso Start =< 1000) of
               true -> sets:add_element(Start, sets:new());
               false -> sets:new()
           end,
    Q0 = queue:in({Start, 0}, queue:new()),
    bfs(Q0, Vis0, Nums, Goal).

bfs(Q, Visited, Nums, Goal) ->
    case queue:out(Q) of
        {empty, _} ->
            -1;
        {{value, {X, Steps}}, QRest} ->
            case process_nums(Nums, X, Steps, QRest, Visited, Goal) of
                {_Q, _Vis, Answer} when is_integer(Answer) ->
                    Answer;
                {NewQ, NewVis, not_found} ->
                    bfs(NewQ, NewVis, Nums, Goal)
            end
    end.

process_nums([Num | Rest], X, Steps, Q, Vis, Goal) ->
    Candidates = [X + Num, X - Num, X bxor Num],
    case try_candidates(Candidates, Steps, Q, Vis, Goal) of
        {found, Answer} ->
            {Q, Vis, Answer};
        {continue, Q1, Vis1} ->
            process_nums(Rest, X, Steps, Q1, Vis1, Goal)
    end;
process_nums([], _X, _Steps, Q, Vis, _Goal) ->
    {Q, Vis, not_found}.

try_candidates([], _Steps, Q, Vis, _Goal) ->
    {continue, Q, Vis};
try_candidates([C | Cs], Steps, Q, Vis, Goal) ->
    if
        C =:= Goal ->
            {found, Steps + 1};
        (C >= 0 andalso C =< 1000) andalso not sets:is_element(C, Vis) ->
            NewVis = sets:add_element(C, Vis),
            NewQ = queue:in({C, Steps + 1}, Q),
            try_candidates(Cs, Steps, NewQ, NewVis, Goal);
        true ->
            try_candidates(Cs, Steps, Q, Vis, Goal)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer], start :: integer, goal :: integer) :: integer
  def minimum_operations(nums, start, goal) do
    if start == goal do
      0
    else
      bfs(nums, start, goal)
    end
  end

  defp bfs(nums, start, goal) do
    queue = :queue.new() |> :queue.in({start, 0})
    visited = MapSet.new([start])
    bfs_loop(queue, visited, nums, goal)
  end

  defp bfs_loop(queue, visited, nums, goal) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {x, steps}}, q} ->
        {new_q, new_visited, found} =
          Enum.reduce(nums, {q, visited, nil}, fn n,
                                                {acc_q, acc_vis, acc_found} = acc ->
            if acc_found != nil do
              acc
            else
              ops = [x + n, x - n, Bitwise.bxor(x, n)]

              Enum.reduce(ops, {acc_q, acc_vis, nil}, fn new_val,
                                                       {q2, vis2, f} ->
                cond do
                  f != nil ->
                    {q2, vis2, f}

                  new_val == goal ->
                    {q2, vis2, steps + 1}

                  new_val >= 0 and new_val <= 1000 and not MapSet.member?(vis2, new_val) ->
                    {:queue.in({new_val, steps + 1}, q2), MapSet.put(vis2, new_val), nil}

                  true ->
                    {q2, vis2, nil}
                end
              end)
            end
          end)

        case found do
          nil -> bfs_loop(new_q, new_visited, nums, goal)
          ans -> ans
        end
    end
  end
end
```
