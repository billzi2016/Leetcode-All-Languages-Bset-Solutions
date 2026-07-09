# 1654. Minimum Jumps to Reach Home

## Cpp

```cpp
class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        unordered_set<int> forbid(forbidden.begin(), forbidden.end());
        if (x == 0) return 0;
        int maxForbidden = 0;
        for (int v : forbidden) maxForbidden = max(maxForbidden, v);
        int limit = max({maxForbidden, x}) + a + b; // safe upper bound
        limit = max(limit, 6000); // ensure enough space
        
        vector<array<bool,2>> visited(limit + 1, {false,false});
        queue<pair<int,bool>> q;
        q.emplace(0, false);
        visited[0][0] = true;
        int steps = 0;
        
        while (!q.empty()) {
            ++steps;
            int sz = q.size();
            while (sz--) {
                auto [pos, lastBack] = q.front(); q.pop();
                
                // forward jump
                int fwd = pos + a;
                if (fwd == x) return steps;
                if (fwd <= limit && !forbid.count(fwd) && !visited[fwd][0]) {
                    visited[fwd][0] = true;
                    q.emplace(fwd, false);
                }
                
                // backward jump (only if previous wasn't backward)
                if (!lastBack) {
                    int back = pos - b;
                    if (back == x) return steps;
                    if (back >= 0 && !forbid.count(back) && !visited[back][1]) {
                        visited[back][1] = true;
                        q.emplace(back, true);
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
    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        if (x == 0) return 0;
        int maxForbidden = 0;
        for (int f : forbidden) maxForbidden = Math.max(maxForbidden, f);
        // Upper bound: enough to cover possible overshoot
        int upper = Math.max(maxForbidden + a + b, x + a + b) + 1000; // safety margin
        boolean[] isForbidden = new boolean[upper + 1];
        for (int f : forbidden) {
            if (f <= upper) isForbidden[f] = true;
        }
        // visited[position][lastWasBackward?1:0]
        boolean[][] visited = new boolean[upper + 1][2];
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0}); // position, lastJumpWasBackward (0=no,1=yes)
        visited[0][0] = true;
        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                int pos = cur[0];
                int lastBack = cur[1];
                // forward jump
                int fwd = pos + a;
                if (fwd == x) return steps + 1;
                if (fwd <= upper && !isForbidden[fwd] && !visited[fwd][0]) {
                    visited[fwd][0] = true;
                    queue.offer(new int[]{fwd, 0});
                }
                // backward jump (only if previous wasn't backward)
                if (lastBack == 0) {
                    int back = pos - b;
                    if (back == x) return steps + 1;
                    if (back >= 0 && !isForbidden[back] && !visited[back][1]) {
                        visited[back][1] = true;
                        queue.offer(new int[]{back, 1});
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
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        from collections import deque

        forbid = set(forbidden)
        # Upper bound for positions to consider.
        max_forbid = max(forbidden) if forbidden else 0
        limit = max(max_forbid + a + b, x) + b + a  # safe upper bound

        queue = deque()
        # (position, last_move_was_backward)
        queue.append((0, False, 0))
        visited = set()
        visited.add((0, False))

        while queue:
            pos, back, steps = queue.popleft()
            if pos == x:
                return steps

            # forward jump
            nxt = pos + a
            if nxt <= limit and nxt not in forbid and (nxt, False) not in visited:
                visited.add((nxt, False))
                queue.append((nxt, False, steps + 1))

            # backward jump (only if previous move wasn't backward)
            if not back:
                nxt = pos - b
                if nxt >= 0 and nxt not in forbid and (nxt, True) not in visited:
                    visited.add((nxt, True))
                    queue.append((nxt, True, steps + 1))

        return -1
```

## Python3

```python
class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        from collections import deque

        forbid = set(forbidden)
        # Upper bound for positions to explore
        max_forbid = max(forbidden) if forbidden else 0
        limit = max(max_forbid + a + b, x + a + b, 6000)

        visited = set()
        dq = deque()
        # (position, last_move_was_backward)
        dq.append((0, False, 0))  # position, backward_flag, steps
        visited.add((0, False))

        while dq:
            pos, back, steps = dq.popleft()
            if pos == x:
                return steps

            # forward jump
            nxt = pos + a
            if nxt <= limit and nxt not in forbid and (nxt, False) not in visited:
                visited.add((nxt, False))
                dq.append((nxt, False, steps + 1))

            # backward jump (only if previous move wasn't backward)
            if not back:
                nxt = pos - b
                if nxt >= 0 and nxt not in forbid and (nxt, True) not in visited:
                    visited.add((nxt, True))
                    dq.append((nxt, True, steps + 1))

        return -1
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int pos;
    int back;   // 0 if last jump was forward or start, 1 if last jump was backward
    int steps;
} Node;

int minimumJumps(int* forbidden, int forbiddenSize, int a, int b, int x) {
    const int MAX = 6000;               // safe upper bound for positions
    bool forbid[MAX + 1];
    for (int i = 0; i <= MAX; ++i) forbid[i] = false;
    for (int i = 0; i < forbiddenSize; ++i) {
        if (forbidden[i] <= MAX) forbid[forbidden[i]] = true;
    }

    bool visited[MAX + 1][2];
    for (int i = 0; i <= MAX; ++i) {
        visited[i][0] = visited[i][1] = false;
    }

    // queue implementation
    int capacity = (MAX + 1) * 4;
    Node* q = (Node*)malloc(sizeof(Node) * capacity);
    int head = 0, tail = 0;

    // start from position 0, last jump not backward
    visited[0][0] = true;
    q[tail++] = (Node){0, 0, 0};

    while (head < tail) {
        Node cur = q[head++];
        if (cur.pos == x) {
            free(q);
            return cur.steps;
        }

        // forward jump
        int nxtF = cur.pos + a;
        if (nxtF <= MAX && !forbid[nxtF] && !visited[nxtF][0]) {
            visited[nxtF][0] = true;
            q[tail++] = (Node){nxtF, 0, cur.steps + 1};
        }

        // backward jump (only if previous was not backward)
        if (cur.back == 0) {
            int nxtB = cur.pos - b;
            if (nxtB >= 0 && !forbid[nxtB] && !visited[nxtB][1]) {
                visited[nxtB][1] = true;
                q[tail++] = (Node){nxtB, 1, cur.steps + 1};
            }
        }

        // ensure queue capacity (should never overflow with given limits)
        if (tail >= capacity) {
            int newCap = capacity * 2;
            Node* newQ = (Node*)realloc(q, sizeof(Node) * newCap);
            if (!newQ) { free(q); return -1; }
            q = newQ;
            capacity = newCap;
        }
    }

    free(q);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumJumps(int[] forbidden, int a, int b, int x) {
        var forbidSet = new HashSet<int>(forbidden);
        int limit = 6000; // sufficient upper bound based on constraints
        bool[,] visited = new bool[limit + 1, 2]; // [position, lastWasBackward]

        var queue = new Queue<(int pos, bool back)>();
        queue.Enqueue((0, false));
        visited[0, 0] = true;

        int steps = 0;
        while (queue.Count > 0) {
            int size = queue.Count;
            for (int i = 0; i < size; i++) {
                var cur = queue.Dequeue();
                int pos = cur.pos;
                bool back = cur.back;

                if (pos == x) return steps;

                // forward jump
                int nf = pos + a;
                if (nf <= limit && !forbidSet.Contains(nf) && !visited[nf, 0]) {
                    visited[nf, 0] = true;
                    queue.Enqueue((nf, false));
                }

                // backward jump (only if previous wasn't backward)
                if (!back) {
                    int nb = pos - b;
                    if (nb >= 0 && !forbidSet.Contains(nb) && !visited[nb, 1]) {
                        visited[nb, 1] = true;
                        queue.Enqueue((nb, true));
                    }
                }
            }
            steps++;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} forbidden
 * @param {number} a
 * @param {number} b
 * @param {number} x
 * @return {number}
 */
var minimumJumps = function(forbidden, a, b, x) {
    const forbidSet = new Set(forbidden);
    if (x === 0) return 0;
    
    // Upper bound for positions we need to consider.
    const maxForbidden = Math.max(0, ...forbidden);
    const limit = Math.max(maxForbidden + a + b, x + a + b, 6000); // safe upper bound
    
    const queue = [];
    // state: [position, lastJumpWasBackward]
    queue.push([0, false, 0]); // position, backward flag, steps
    const visited = new Set();
    visited.add(`0,false`);
    
    while (queue.length) {
        const [pos, back, steps] = queue.shift();
        
        // forward jump
        let nextPos = pos + a;
        if (nextPos === x) return steps + 1;
        if (nextPos <= limit && !forbidSet.has(nextPos)) {
            const key = `${nextPos},false`;
            if (!visited.has(key)) {
                visited.add(key);
                queue.push([nextPos, false, steps + 1]);
            }
        }
        
        // backward jump (only if previous wasn't backward)
        if (!back) {
            nextPos = pos - b;
            if (nextPos === x) return steps + 1;
            if (nextPos >= 0 && !forbidSet.has(nextPos)) {
                const key = `${nextPos},true`;
                if (!visited.has(key)) {
                    visited.add(key);
                    queue.push([nextPos, true, steps + 1]);
                }
            }
        }
    }
    
    return -1;
};
```

## Typescript

```typescript
function minimumJumps(forbidden: number[], a: number, b: number, x: number): number {
    const forbid = new Set<number>(forbidden);
    const LIMIT = 6000; // safe upper bound based on constraints
    const visited = new Set<string>();
    const queue: [number, boolean][] = [];
    let head = 0;
    queue.push([0, false]);
    visited.add('0-0'); // position-flag (0 for false, 1 for true)

    let steps = 0;
    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const [pos, prevBack] = queue[head++];
            if (pos === x) return steps;

            // forward jump
            const fwd = pos + a;
            if (fwd <= LIMIT && !forbid.has(fwd)) {
                const keyF = `${fwd}-0`;
                if (!visited.has(keyF)) {
                    visited.add(keyF);
                    queue.push([fwd, false]);
                }
            }

            // backward jump (only if previous wasn't backward)
            if (!prevBack) {
                const back = pos - b;
                if (back >= 0 && !forbid.has(back)) {
                    const keyB = `${back}-1`;
                    if (!visited.has(keyB)) {
                        visited.add(keyB);
                        queue.push([back, true]);
                    }
                }
            }
        }
        steps++;
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $forbidden
     * @param Integer $a
     * @param Integer $b
     * @param Integer $x
     * @return Integer
     */
    function minimumJumps($forbidden, $a, $b, $x) {
        // Upper bound for positions to consider.
        $limit = 6000; // sufficient given constraints

        // Forbidden positions set for O(1) lookup.
        $forbiddenSet = array_flip($forbidden);

        // visited[position][dir] where dir: 0 = last jump was forward (or start), 1 = last jump was backward
        $visited = [];

        // BFS queue implementation using parallel arrays.
        $queuePos   = [];
        $queueSteps = [];
        $queueDir   = []; // 0 for forward-last, 1 for backward-last

        $head = 0;

        // start from position 0, 0 steps, last move considered as forward (so we can go backward later)
        $queuePos[]   = 0;
        $queueSteps[] = 0;
        $queueDir[]   = 0;
        $visited[0][0] = true;

        while ($head < count($queuePos)) {
            $pos   = $queuePos[$head];
            $steps = $queueSteps[$head];
            $dir   = $queueDir[$head];
            $head++;

            if ($pos === $x) {
                return $steps;
            }

            // Try forward jump
            $nextForward = $pos + $a;
            if ($nextForward <= $limit && !isset($forbiddenSet[$nextForward])) {
                if (!isset($visited[$nextForward][0])) {
                    $visited[$nextForward][0] = true;
                    $queuePos[]   = $nextForward;
                    $queueSteps[] = $steps + 1;
                    $queueDir[]   = 0; // last jump is forward
                }
            }

            // Try backward jump only if previous jump wasn't backward
            if ($dir === 0) {
                $nextBackward = $pos - $b;
                if ($nextBackward >= 0 && !isset($forbiddenSet[$nextBackward])) {
                    if (!isset($visited[$nextBackward][1])) {
                        $visited[$nextBackward][1] = true;
                        $queuePos[]   = $nextBackward;
                        $queueSteps[] = $steps + 1;
                        $queueDir[]   = 1; // last jump is backward
                    }
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
    func minimumJumps(_ forbidden: [Int], _ a: Int, _ b: Int, _ x: Int) -> Int {
        var forbid = Set<Int>(forbidden)
        if x == 0 { return 0 }
        
        // Upper bound to limit search space
        let limit = 6000
        
        var visited = Set<Int>()
        var queue: [(pos: Int, back: Bool, steps: Int)] = []
        queue.append((0, false, 0))
        visited.insert(0) // encode position*2 + (back ? 1 : 0)
        
        var idx = 0
        while idx < queue.count {
            let cur = queue[idx]
            idx += 1
            
            if cur.pos == x { return cur.steps }
            
            // Jump forward
            let nextF = cur.pos + a
            if nextF <= limit && !forbid.contains(nextF) {
                let code = nextF * 2
                if !visited.contains(code) {
                    visited.insert(code)
                    queue.append((nextF, false, cur.steps + 1))
                }
            }
            
            // Jump backward (only if previous jump wasn't backward)
            if !cur.back {
                let nextB = cur.pos - b
                if nextB >= 0 && !forbid.contains(nextB) {
                    let code = nextB * 2 + 1
                    if !visited.contains(code) {
                        visited.insert(code)
                        queue.append((nextB, true, cur.steps + 1))
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
    fun minimumJumps(forbidden: IntArray, a: Int, b: Int, x: Int): Int {
        if (x == 0) return 0
        val forbiddenSet = HashSet<Int>()
        for (v in forbidden) forbiddenSet.add(v)

        // Upper bound sufficient for all reachable positions.
        val LIMIT = 6000
        val visited = Array(LIMIT + 1) { BooleanArray(2) } // [pos][lastWasBackward?]
        val queue: java.util.ArrayDeque<Triple<Int, Boolean, Int>> = java.util.ArrayDeque()
        queue.add(Triple(0, false, 0))
        visited[0][0] = true

        while (queue.isNotEmpty()) {
            val (pos, lastBack, steps) = queue.poll()

            // Jump forward
            var next = pos + a
            if (next == x) return steps + 1
            if (next <= LIMIT && !forbiddenSet.contains(next) && !visited[next][0]) {
                visited[next][0] = true
                queue.add(Triple(next, false, steps + 1))
            }

            // Jump backward (only if previous jump wasn't backward)
            if (!lastBack) {
                next = pos - b
                if (next == x) return steps + 1
                if (next >= 0 && !forbiddenSet.contains(next) && !visited[next][1]) {
                    visited[next][1] = true
                    queue.add(Triple(next, true, steps + 1))
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
  int minimumJumps(List<int> forbidden, int a, int b, int x) {
    final Set<int> forbid = forbidden.toSet();
    const int LIMIT = 6000; // safe upper bound based on constraints
    List<List<bool>> visited = List.generate(LIMIT + 1, (_) => [false, false]);
    Queue<List<int>> q = Queue<List<int>>();
    q.add([0, 0]); // position, last jump was backward? (0 = no, 1 = yes)
    visited[0][0] = true;
    int steps = 0;

    while (q.isNotEmpty) {
      int size = q.length;
      for (int i = 0; i < size; i++) {
        var cur = q.removeFirst();
        int pos = cur[0];
        int lastBack = cur[1];

        if (pos == x) return steps;

        // forward jump
        int fwd = pos + a;
        if (fwd <= LIMIT && !forbid.contains(fwd) && !visited[fwd][0]) {
          visited[fwd][0] = true;
          q.add([fwd, 0]);
        }

        // backward jump (only if previous wasn't backward)
        if (lastBack == 0) {
          int back = pos - b;
          if (back >= 0 && !forbid.contains(back) && !visited[back][1]) {
            visited[back][1] = true;
            q.add([back, 1]);
          }
        }
      }
      steps++;
    }

    return -1;
  }
}
```

## Golang

```go
func minimumJumps(forbidden []int, a int, b int, x int) int {
	const maxLimit = 6000
	limit := maxLimit

	forbid := make([]bool, limit+1)
	for _, v := range forbidden {
		if v <= limit {
			forbid[v] = true
		}
	}
	if forbid[0] {
		return -1
	}

	type node struct {
		pos   int
		back  bool
		steps int
	}
	queue := []node{{0, false, 0}}
	visited := make([][2]bool, limit+1)
	visited[0][0] = true

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.pos == x {
			return cur.steps
		}

		// forward jump
		nf := cur.pos + a
		if nf <= limit && !forbid[nf] && !visited[nf][0] {
			visited[nf][0] = true
			queue = append(queue, node{nf, false, cur.steps + 1})
		}

		// backward jump (only if previous wasn't backward)
		if !cur.back {
			nb := cur.pos - b
			if nb >= 0 && !forbid[nb] && !visited[nb][1] {
				visited[nb][1] = true
				queue = append(queue, node{nb, true, cur.steps + 1})
			}
		}
	}
	return -1
}
```

## Ruby

```ruby
def minimum_jumps(forbidden, a, b, x)
  forbid = {}
  forbidden.each { |v| forbid[v] = true }

  max_forbid = forbidden.max || 0
  limit = [max_forbid + a + b, x + a + b].max + 1000

  visited = Array.new(limit + 1) { [false, false] } # [came from forward, came from backward]
  queue = []
  queue << [0, false, 0] # position, last move was backward?, steps
  visited[0][0] = true

  until queue.empty?
    pos, last_back, steps = queue.shift
    return steps if pos == x

    # forward jump
    nxt = pos + a
    if nxt <= limit && !forbid[nxt] && !visited[nxt][0]
      visited[nxt][0] = true
      queue << [nxt, false, steps + 1]
    end

    # backward jump (only if previous move wasn't backward)
    unless last_back
      nxt2 = pos - b
      if nxt2 >= 0 && !forbid[nxt2] && !visited[nxt2][1]
        visited[nxt2][1] = true
        queue << [nxt2, true, steps + 1]
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def minimumJumps(forbidden: Array[Int], a: Int, b: Int, x: Int): Int = {
        if (x == 0) return 0
        val forbidSet = forbidden.toSet
        val upper = 6000 // safe bound covering all reachable positions
        val visited = Array.ofDim[Boolean](upper + 1, 2) // [pos][lastWasBackward? 0:false,1:true]
        import scala.collection.mutable.Queue
        val q: Queue[(Int, Boolean)] = Queue()
        q.enqueue((0, false))
        visited(0)(0) = true
        var steps = 0

        while (q.nonEmpty) {
            val size = q.size
            for (_ <- 0 until size) {
                val (pos, lastBackward) = q.dequeue()
                if (pos == x) return steps

                // forward jump
                val fwd = pos + a
                if (fwd <= upper && !forbidSet.contains(fwd) && !visited(fwd)(0)) {
                    visited(fwd)(0) = true
                    q.enqueue((fwd, false))
                }

                // backward jump (only if previous wasn't backward)
                if (!lastBackward) {
                    val backPos = pos - b
                    if (backPos >= 0 && !forbidSet.contains(backPos) && !visited(backPos)(1)) {
                        visited(backPos)(1) = true
                        q.enqueue((backPos, true))
                    }
                }
            }
            steps += 1
        }

        -1
    }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn minimum_jumps(forbidden: Vec<i32>, a: i32, b: i32, x: i32) -> i32 {
        const LIMIT: i32 = 6000; // safe upper bound for positions
        let forbid_set: HashSet<i32> = forbidden.into_iter().collect();

        let mut visited_forward = vec![false; (LIMIT + 1) as usize];
        let mut visited_backward = vec![false; (LIMIT + 1) as usize];

        let mut queue: VecDeque<(i32, bool, i32)> = VecDeque::new(); // (position, last_was_backward, steps)
        queue.push_back((0, false, 0));
        visited_forward[0] = true;

        while let Some((pos, back, steps)) = queue.pop_front() {
            if pos == x {
                return steps;
            }

            // Jump forward
            let next = pos + a;
            if next <= LIMIT && !forbid_set.contains(&next) && !visited_forward[next as usize] {
                visited_forward[next as usize] = true;
                queue.push_back((next, false, steps + 1));
            }

            // Jump backward (only if previous jump wasn't backward)
            if !back {
                let back_pos = pos - b;
                if back_pos >= 0
                    && !forbid_set.contains(&back_pos)
                    && !visited_backward[back_pos as usize]
                {
                    visited_backward[back_pos as usize] = true;
                    queue.push_back((back_pos, true, steps + 1));
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(require racket/queue)

(define/contract (minimum-jumps forbidden a b x)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([forbidden-set (make-hash)])
    (for-each (lambda (pos) (hash-set! forbidden-set pos #t)) forbidden)
    (define max-forbidden
      (if (null? forbidden) 0 (apply max forbidden)))
    ;; generous upper bound to keep search finite
    (define limit (+ (max max-forbidden x) a b (* 2 2000)))
    (define visited (make-hash))
    (define q (make-queue))

    (define (state-key pos back?) (cons pos back?))

    (hash-set! visited (state-key 0 #f) #t)
    (enqueue! q (list 0 0 #f)) ; position, steps, last move was backward?

    (let loop ()
      (if (queue-empty? q)
          -1
          (let* ([curr (dequeue! q)]
                 [pos (first curr)]
                 [steps (second curr)]
                 [back? (third curr)])
            (cond [(= pos x) steps]
                  [else
                   ;; forward jump
                   (define next-forward (+ pos a))
                   (when (and (<= next-forward limit)
                              (not (hash-has-key? forbidden-set next-forward))
                              (not (hash-has-key? visited (state-key next-forward #f))))
                     (hash-set! visited (state-key next-forward #f) #t)
                     (enqueue! q (list next-forward (+ steps 1) #f)))
                   ;; backward jump, only if previous wasn't backward
                   (when (and (not back?) (>= (- pos b) 0))
                     (define next-back (- pos b))
                     (when (and (not (hash-has-key? forbidden-set next-back))
                                (not (hash-has-key? visited (state-key next-back #t))))
                       (hash-set! visited (state-key next-back #t) #t)
                       (enqueue! q (list next-back (+ steps 1) #t))))
                   (loop)]))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_jumps/4]).

-include_lib("stdlib/include/sets.hrl").

-spec minimum_jumps(Forbidden :: [integer()], A :: integer(), B :: integer(), X :: integer()) -> integer().
minimum_jumps(Forbidden, A, B, X) ->
    ForbiddenSet = sets:from_list(Forbidden),
    Limit = 6000,
    Visited0 = maps:new(),
    Queue0 = queue:new(),
    Queue1 = queue:in({0, false, 0}, Queue0),
    Visited1 = maps:put({0, false}, true, Visited0),
    bfs(Queue1, Visited1, ForbiddenSet, A, B, X, Limit).

bfs(Queue, Visited, ForbiddenSet, A, B, X, Limit) ->
    case queue:out(Queue) of
        {{value, {Pos, Back, Steps}}, Q1} ->
            if Pos =:= X ->
                    Steps;
               true ->
                    Fwd = Pos + A,
                    {Q2, Vis2} = enqueue_if({Fwd, false}, Steps + 1, Q1, Visited, Limit, ForbiddenSet),
                    {Q3, Vis3} =
                        case Back of
                            false ->
                                Bwd = Pos - B,
                                if Bwd >= 0 ->
                                        enqueue_if({Bwd, true}, Steps + 1, Q2, Vis2, Limit, ForbiddenSet);
                                   true -> {Q2, Vis2}
                                end;
                            true ->
                                {Q2, Vis2}
                        end,
                    bfs(Q3, Vis3, ForbiddenSet, A, B, X, Limit)
            end;
        {empty, _} ->
            -1
    end.

enqueue_if({Pos, BackFlag}, Steps, Queue, Visited, Limit, ForbiddenSet) ->
    if Pos =< Limit,
       not sets:is_element(Pos, ForbiddenSet),
       not maps:is_key({Pos, BackFlag}, Visited) ->
            {queue:in({Pos, BackFlag, Steps}, Queue), maps:put({Pos, BackFlag}, true, Visited)};
       true ->
            {Queue, Visited}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_jumps(forbidden :: [integer], a :: integer, b :: integer, x :: integer) :: integer
  def minimum_jumps(forbidden, a, b, x) do
    forbid = MapSet.new(forbidden)
    max_val = Enum.max([x | forbidden] ++ [0])
    limit = max_val + a + b + 1000

    initial_queue = :queue.new() |> :queue.in({0, false, 0})
    visited = MapSet.new([{0, false}])

    bfs(initial_queue, forbid, limit, x, a, b, visited)
  end

  defp bfs(queue, forbid, limit, target, a, b, visited) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {pos, back, steps}}, q} ->
        if pos == target do
          steps
        else
          # forward jump
          new_pos = pos + a

          {q1, visited1} =
            if new_pos <= limit and not MapSet.member?(forbid, new_pos) and
                 not MapSet.member?(visited, {new_pos, false}) do
              {
                :queue.in({new_pos, false, steps + 1}, q),
                MapSet.put(visited, {new_pos, false})
              }
            else
              {q, visited}
            end

          # backward jump (only if previous move wasn't backward)
          {q2, visited2} =
            if not back do
              new_back = pos - b

              if new_back >= 0 and not MapSet.member?(forbid, new_back) and
                   not MapSet.member?(visited1, {new_back, true}) do
                {
                  :queue.in({new_back, true, steps + 1}, q1),
                  MapSet.put(visited1, {new_back, true})
                }
              else
                {q1, visited1}
              end
            else
              {q1, visited1}
            end

          bfs(q2, forbid, limit, target, a, b, visited2)
        end
    end
  end
end
```
