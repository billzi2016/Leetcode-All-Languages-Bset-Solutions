# 0773. Sliding Puzzle

## Cpp

```cpp
class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        const vector<vector<int>> dirs = {
            {1, 3},        // position 0
            {0, 2, 4},     // position 1
            {1, 5},        // position 2
            {0, 4},        // position 3
            {1, 3, 5},     // position 4
            {2, 4}         // position 5
        };
        string start;
        for (auto& row : board) {
            for (int v : row) start.push_back('0' + v);
        }
        const string target = "123450";
        if (start == target) return 0;

        unordered_set<string> visited{start};
        queue<string> q;
        q.push(start);
        int moves = 0;

        while (!q.empty()) {
            ++moves;
            int sz = q.size();
            while (sz--) {
                string cur = q.front(); q.pop();
                int zeroPos = cur.find('0');
                for (int nxt : dirs[zeroPos]) {
                    string nextState = cur;
                    swap(nextState[zeroPos], nextState[nxt]);
                    if (nextState == target) return moves;
                    if (!visited.count(nextState)) {
                        visited.insert(nextState);
                        q.push(move(nextState));
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
    public int slidingPuzzle(int[][] board) {
        // Neighbor positions for each index in the flattened string
        int[][] neighbors = {
            {1, 3},      // 0
            {0, 2, 4},   // 1
            {1, 5},      // 2
            {0, 4},      // 3
            {1, 3, 5},   // 4
            {2, 4}       // 5
        };
        
        StringBuilder sb = new StringBuilder();
        for (int[] row : board) {
            for (int val : row) {
                sb.append(val);
            }
        }
        String start = sb.toString();
        String target = "123450";
        if (start.equals(target)) return 0;
        
        java.util.Queue<String> queue = new java.util.ArrayDeque<>();
        java.util.Set<String> visited = new java.util.HashSet<>();
        queue.offer(start);
        visited.add(start);
        int moves = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String cur = queue.poll();
                if (cur.equals(target)) return moves;
                int zeroPos = cur.indexOf('0');
                for (int nb : neighbors[zeroPos]) {
                    String next = swap(cur, zeroPos, nb);
                    if (!visited.contains(next)) {
                        visited.add(next);
                        queue.offer(next);
                    }
                }
            }
            moves++;
        }
        return -1;
    }
    
    private String swap(String s, int i, int j) {
        char[] arr = s.toCharArray();
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        return new String(arr);
    }
}
```

## Python

```python
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from collections import deque

        # Flatten the board to a string
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        if start == target:
            return 0

        # Neighbor positions for each index in the flattened board
        neighbors = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4)
        }

        visited = set([start])
        q = deque([start])
        moves = 0

        while q:
            moves += 1
            for _ in range(len(q)):
                cur = q.popleft()
                zero_idx = cur.index('0')
                for nb in neighbors[zero_idx]:
                    lst = list(cur)
                    lst[zero_idx], lst[nb] = lst[nb], lst[zero_idx]
                    nxt = ''.join(lst)
                    if nxt == target:
                        return moves
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

        return -1
```

## Python3

```python
class Solution:
    def slidingPuzzle(self, board):
        from collections import deque

        # Convert board to string state
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        if start == target:
            return 0

        # Adjacent positions for each index in the flattened 2x3 board
        neighbors = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4)
        }

        visited = {start}
        q = deque([start])
        moves = 0

        while q:
            moves += 1
            for _ in range(len(q)):
                cur = q.popleft()
                zero_idx = cur.index('0')
                for nb in neighbors[zero_idx]:
                    lst = list(cur)
                    lst[zero_idx], lst[nb] = lst[nb], lst[zero_idx]
                    nxt = ''.join(lst)
                    if nxt == target:
                        return moves
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

        return -1
```

## C

```c
#include <string.h>
#include <stdbool.h>

int slidingPuzzle(int** board, int boardSize, int* boardColSize) {
    const char target[7] = "123450";
    /* adjacency list for each position (0..5), -1 marks end */
    const int neighbor[6][4] = {
        {1, 3, -1, -1},   // 0
        {0, 2, 4, -1},    // 1
        {1, 5, -1, -1},   // 2
        {0, 4, -1, -1},   // 3
        {1, 3, 5, -1},    // 4
        {2, 4, -1, -1}    // 5
    };

    char start[7];
    int idx = 0;
    for (int i = 0; i < boardSize; ++i) {
        for (int j = 0; j < boardColSize[i]; ++j) {
            start[idx++] = (char)('0' + board[i][j]);
        }
    }
    start[6] = '\0';

    /* queue for BFS, maximum possible states are 720 */
    char q[720][7];
    int front = 0, rear = 0;
    memcpy(q[rear++], start, 7);

    /* visited list */
    char visited[720][7];
    int vcnt = 0;
    memcpy(visited[vcnt++], start, 7);

    int moves = 0;
    while (front < rear) {
        int levelSize = rear - front;
        for (int i = 0; i < levelSize; ++i) {
            char *cur = q[front++];
            if (strcmp(cur, target) == 0) return moves;

            int zeroPos = 0;
            while (zeroPos < 6 && cur[zeroPos] != '0') ++zeroPos;

            for (int k = 0; k < 4; ++k) {
                int nb = neighbor[zeroPos][k];
                if (nb == -1) continue;

                char next[7];
                memcpy(next, cur, 6);
                /* swap zero with neighbor */
                char tmp = next[zeroPos];
                next[zeroPos] = next[nb];
                next[nb] = tmp;
                next[6] = '\0';

                bool seen = false;
                for (int v = 0; v < vcnt; ++v) {
                    if (strcmp(visited[v], next) == 0) {
                        seen = true;
                        break;
                    }
                }
                if (!seen) {
                    memcpy(visited[vcnt++], next, 7);
                    memcpy(q[rear++], next, 7);
                }
            }
        }
        ++moves;
    }
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public int SlidingPuzzle(int[][] board) {
        // Flatten the board into a string representation
        StringBuilder sb = new StringBuilder();
        foreach (var row in board) {
            foreach (var val in row) {
                sb.Append(val);
            }
        }
        string start = sb.ToString();
        const string target = "123450";
        if (start == target) return 0;

        // Neighbor positions for each index in the flattened 2x3 board
        int[][] neighbors = new int[6][]
        {
            new int[]{1,3},    // 0
            new int[]{0,2,4},  // 1
            new int[]{1,5},    // 2
            new int[]{0,4},    // 3
            new int[]{1,3,5},  // 4
            new int[]{2,4}     // 5
        };

        var visited = new HashSet<string>();
        var queue = new Queue<string>();
        visited.Add(start);
        queue.Enqueue(start);
        int moves = 0;

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                string cur = queue.Dequeue();
                if (cur == target) return moves;

                int zeroPos = cur.IndexOf('0');
                foreach (int nxt in neighbors[zeroPos]) {
                    char[] arr = cur.ToCharArray();
                    // swap zero with neighbor
                    char temp = arr[zeroPos];
                    arr[zeroPos] = arr[nxt];
                    arr[nxt] = temp;
                    string nextState = new string(arr);
                    if (!visited.Contains(nextState)) {
                        visited.Add(nextState);
                        queue.Enqueue(nextState);
                    }
                }
            }
            moves++;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} board
 * @return {number}
 */
var slidingPuzzle = function(board) {
    const target = "123450";
    let start = "";
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 3; j++) {
            start += board[i][j];
        }
    }
    if (start === target) return 0;

    const neighbors = [
        [1, 3],      // 0
        [0, 2, 4],   // 1
        [1, 5],      // 2
        [0, 4],      // 3
        [1, 3, 5],   // 4
        [2, 4]       // 5
    ];

    const visited = new Set();
    visited.add(start);
    const queue = [[start, 0]];
    let head = 0;

    while (head < queue.length) {
        const [state, steps] = queue[head++];
        const zeroIdx = state.indexOf('0');
        for (const nb of neighbors[zeroIdx]) {
            const newState = swap(state, zeroIdx, nb);
            if (!visited.has(newState)) {
                if (newState === target) return steps + 1;
                visited.add(newState);
                queue.push([newState, steps + 1]);
            }
        }
    }

    return -1;
};

function swap(str, i, j) {
    const arr = str.split('');
    const tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
    return arr.join('');
}
```

## Typescript

```typescript
function slidingPuzzle(board: number[][]): number {
    const target = "123450";
    let start = "";
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            start += board[i][j];
        }
    }

    if (start === target) return 0;

    const neighbors: number[][] = [
        [1, 3],      // 0
        [0, 2, 4],   // 1
        [1, 5],      // 2
        [0, 4],      // 3
        [1, 3, 5],   // 4
        [2, 4]       // 5
    ];

    const visited = new Set<string>();
    visited.add(start);
    const queue: string[] = [start];
    let head = 0;
    let moves = 0;

    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const cur = queue[head++];
            if (cur === target) return moves;

            const zeroIdx = cur.indexOf('0');
            for (const nb of neighbors[zeroIdx]) {
                const arr = cur.split('');
                [arr[zeroIdx], arr[nb]] = [arr[nb], arr[zeroIdx]];
                const next = arr.join('');
                if (!visited.has(next)) {
                    visited.add(next);
                    queue.push(next);
                }
            }
        }
        moves++;
    }

    return -1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function slidingPuzzle($board) {
        $target = "123450";
        $start = "";
        foreach ($board as $row) {
            foreach ($row as $val) {
                $start .= (string)$val;
            }
        }
        if ($start === $target) {
            return 0;
        }

        $neighbors = [
            [1, 3],       // 0
            [0, 2, 4],    // 1
            [1, 5],       // 2
            [0, 4],       // 3
            [1, 3, 5],    // 4
            [2, 4]        // 5
        ];

        $queue = new SplQueue();
        $queue->enqueue($start);
        $visited = [$start => true];
        $moves = 0;

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            for ($i = 0; $i < $size; $i++) {
                $state = $queue->dequeue();
                if ($state === $target) {
                    return $moves;
                }
                $zeroPos = strpos($state, '0');
                foreach ($neighbors[$zeroPos] as $nextPos) {
                    $chars = str_split($state);
                    $tmp = $chars[$zeroPos];
                    $chars[$zeroPos] = $chars[$nextPos];
                    $chars[$nextPos] = $tmp;
                    $newState = implode('', $chars);
                    if (!isset($visited[$newState])) {
                        $visited[$newState] = true;
                        $queue->enqueue($newState);
                    }
                }
            }
            $moves++;
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func slidingPuzzle(_ board: [[Int]]) -> Int {
        let target = "123450"
        var start = ""
        for i in 0..<2 {
            for j in 0..<3 {
                start.append(String(board[i][j]))
            }
        }
        if start == target { return 0 }
        
        let neighbors: [[Int]] = [
            [1, 3],      // 0
            [0, 2, 4],   // 1
            [1, 5],      // 2
            [0, 4],      // 3
            [1, 3, 5],   // 4
            [2, 4]       // 5
        ]
        
        var visited = Set<String>()
        visited.insert(start)
        var queue: [String] = [start]
        var head = 0
        var moves = 0
        
        while head < queue.count {
            let levelSize = queue.count - head
            for _ in 0..<levelSize {
                let state = queue[head]
                head += 1
                if state == target { return moves }
                
                guard let zeroIdxPos = state.firstIndex(of: "0") else { continue }
                let zeroIdx = state.distance(from: state.startIndex, to: zeroIdxPos)
                
                for nb in neighbors[zeroIdx] {
                    var chars = Array(state)
                    chars.swapAt(zeroIdx, nb)
                    let newState = String(chars)
                    if !visited.contains(newState) {
                        visited.insert(newState)
                        queue.append(newState)
                    }
                }
            }
            moves += 1
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun slidingPuzzle(board: Array<IntArray>): Int {
        val sb = StringBuilder()
        for (row in board) {
            for (v in row) sb.append(v)
        }
        val start = sb.toString()
        val target = "123450"
        if (start == target) return 0

        val neighbors = arrayOf(
            intArrayOf(1, 3),          // 0
            intArrayOf(0, 2, 4),       // 1
            intArrayOf(1, 5),          // 2
            intArrayOf(0, 4),          // 3
            intArrayOf(1, 3, 5),       // 4
            intArrayOf(2, 4)           // 5
        )

        val visited = HashSet<String>()
        val queue: ArrayDeque<String> = ArrayDeque()
        visited.add(start)
        queue.add(start)

        var moves = 0
        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val cur = queue.removeFirst()
                if (cur == target) return moves
                val zeroIdx = cur.indexOf('0')
                for (nextIdx in neighbors[zeroIdx]) {
                    val chars = cur.toCharArray()
                    val tmp = chars[zeroIdx]
                    chars[zeroIdx] = chars[nextIdx]
                    chars[nextIdx] = tmp
                    val nextState = String(chars)
                    if (visited.add(nextState)) {
                        queue.addLast(nextState)
                    }
                }
            }
            moves++
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int slidingPuzzle(List<List<int>> board) {
    const String target = "123450";
    // Flatten the board into a string
    String start = '';
    for (var row in board) {
      for (var v in row) {
        start += v.toString();
      }
    }

    if (start == target) return 0;

    // Adjacent positions for each index in the flattened board
    const List<List<int>> adj = [
      [1, 3],       // 0
      [0, 2, 4],    // 1
      [1, 5],       // 2
      [0, 4],       // 3
      [1, 3, 5],    // 4
      [2, 4]        // 5
    ];

    Set<String> visited = {start};
    Queue<String> queue = Queue<String>();
    queue.add(start);
    int moves = 0;

    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      for (int i = 0; i < levelSize; i++) {
        String cur = queue.removeFirst();
        if (cur == target) return moves;

        int zeroPos = cur.indexOf('0');
        for (int nb in adj[zeroPos]) {
          List<String> chars = cur.split('');
          String tmp = chars[zeroPos];
          chars[zeroPos] = chars[nb];
          chars[nb] = tmp;
          String next = chars.join();
          if (!visited.contains(next)) {
            visited.add(next);
            queue.add(next);
          }
        }
      }
      moves++;
    }

    return -1;
  }
}
```

## Golang

```go
package main

import "strings"

func slidingPuzzle(board [][]int) int {
	target := "123450"
	var sb strings.Builder
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			sb.WriteByte(byte(board[i][j] + '0'))
		}
	}
	start := sb.String()
	if start == target {
		return 0
	}

	neighbors := [][]int{
		{1, 3},    // 0
		{0, 2, 4}, // 1
		{1, 5},    // 2
		{0, 4},    // 3
		{1, 3, 5}, // 4
		{2, 4},    // 5
	}

	queue := []string{start}
	visited := map[string]bool{start: true}
	moves := 0

	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]

			if cur == target {
				return moves
			}

			zeroPos := strings.Index(cur, "0")
			for _, nb := range neighbors[zeroPos] {
				b := []byte(cur)
				b[zeroPos], b[nb] = b[nb], b[zeroPos]
				next := string(b)
				if !visited[next] {
					visited[next] = true
					queue = append(queue, next)
				}
			}
		}
		moves++
	}
	return -1
}
```

## Ruby

```ruby
require 'set'

def sliding_puzzle(board)
  start = board.flatten.map(&:to_s).join
  target = "123450"
  return 0 if start == target

  neighbors = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4],
    [1, 3, 5],
    [2, 4]
  ]

  visited = Set.new([start])
  queue = [start]
  moves = 0

  until queue.empty?
    next_queue = []
    queue.each do |state|
      return moves if state == target
      zero_idx = state.index('0')
      neighbors[zero_idx].each do |ni|
        new_state = state.dup
        new_state[zero_idx], new_state[ni] = new_state[ni], new_state[zero_idx]
        unless visited.include?(new_state)
          visited.add(new_state)
          next_queue << new_state
        end
      end
    end
    moves += 1
    queue = next_queue
  end

  -1
end
```

## Scala

```scala
object Solution {
    def slidingPuzzle(board: Array[Array[Int]]): Int = {
        val target = "123450"
        val sb = new StringBuilder
        for (i <- 0 until 2) {
            for (j <- 0 until 3) {
                sb.append(board(i)(j))
            }
        }
        val start = sb.toString()
        if (start == target) return 0

        val neighbors = Array(
            Array(1, 3),      // 0
            Array(0, 2, 4),   // 1
            Array(1, 5),      // 2
            Array(0, 4),      // 3
            Array(1, 3, 5),   // 4
            Array(2, 4)       // 5
        )

        import scala.collection.mutable.{Queue, Set}
        val queue = Queue[String]()
        val visited = Set[String]()

        queue.enqueue(start)
        visited += start

        var moves = 0
        while (queue.nonEmpty) {
            val size = queue.size
            for (_ <- 0 until size) {
                val cur = queue.dequeue()
                if (cur == target) return moves
                val zeroPos = cur.indexOf('0')
                for (nextPos <- neighbors(zeroPos)) {
                    val arr = cur.toCharArray
                    val tmp = arr(zeroPos)
                    arr(zeroPos) = arr(nextPos)
                    arr(nextPos) = tmp
                    val nextState = new String(arr)
                    if (!visited.contains(nextState)) {
                        visited += nextState
                        queue.enqueue(nextState)
                    }
                }
            }
            moves += 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sliding_puzzle(board: Vec<Vec<i32>>) -> i32 {
        use std::collections::{HashSet, VecDeque};

        let mut start = String::new();
        for row in board.iter() {
            for &v in row.iter() {
                start.push((b'0' + v as u8) as char);
            }
        }

        let target = "123450".to_string();
        if start == target {
            return 0;
        }

        let adj: Vec<Vec<usize>> = vec![
            vec![1, 3],
            vec![0, 2, 4],
            vec![1, 5],
            vec![0, 4],
            vec![1, 3, 5],
            vec![2, 4],
        ];

        let mut visited: HashSet<String> = HashSet::new();
        visited.insert(start.clone());

        let mut queue: VecDeque<String> = VecDeque::new();
        queue.push_back(start);

        let mut moves: i32 = 0;

        while !queue.is_empty() {
            let level_size = queue.len();
            for _ in 0..level_size {
                if let Some(cur) = queue.pop_front() {
                    if cur == target {
                        return moves;
                    }
                    let zero_pos = cur.find('0').unwrap();

                    for &next_pos in adj[zero_pos].iter() {
                        let mut chars: Vec<char> = cur.chars().collect();
                        chars.swap(zero_pos, next_pos);
                        let next_state: String = chars.iter().collect();
                        if !visited.contains(&next_state) {
                            visited.insert(next_state.clone());
                            queue.push_back(next_state);
                        }
                    }
                }
            }
            moves += 1;
        }

        -1
    }
}
```

## Racket

```racket
(define moves
  (vector (list 1 3)          ; index 0
          (list 0 2 4)        ; index 1
          (list 1 5)          ; index 2
          (list 0 4)          ; index 3
          (list 1 3 5)        ; index 4
          (list 2 4)))        ; index 5

(define/contract (sliding-puzzle board)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((start
           (apply string-append
                  (map number->string (flatten board))))
         (target "123450"))
    (if (string=? start target)
        0
        (let ((visited (make-hash))
              (queue (list start)))
          (hash-set! visited start #t)
          (let bfs ((q queue) (steps 0))
            (if (null? q)
                -1
                (let loop ((curr q) (next '()))
                  (cond
                    [(null? curr)
                     (bfs next (+ steps 1))]
                    [else
                     (define state (car curr))
                     (if (string=? state target)
                         steps
                         (let ()
                           ;; find position of '0'
                           (define zero-pos
                             (let loop ((i 0))
                               (if (= i (string-length state))
                                   -1
                                   (if (char=? (string-ref state i) #\0)
                                       i
                                       (loop (+ i 1))))))
                           (define neighbors (vector-ref moves zero-pos))
                           (define new-next
                             (for/fold ([acc next]) ([np neighbors])
                               (let* ((vec (list->vector (string->list state)))
                                      (tmp (vector-ref vec zero-pos))
                                      (val (vector-ref vec np)))
                                 (vector-set! vec zero-pos val)
                                 (vector-set! vec np tmp)
                                 (define new-state
                                   (list->string (vector->list vec)))
                                 (if (hash-has-key? visited new-state)
                                     acc
                                     (begin
                                       (hash-set! visited new-state #t)
                                       (cons new-state acc)))) ))
                           (loop (cdr curr) new-next))])))))))))
```

## Erlang

```erlang
-module(solution).
-export([sliding_puzzle/1]).

-spec sliding_puzzle(Board :: [[integer()]]) -> integer().
sliding_puzzle(Board) ->
    Start = flatten_board(Board),
    Target = [1,2,3,4,5,0],
    case Start == Target of
        true -> 0;
        false ->
            Neighbors = [
                [1,3],      % position 0
                [0,2,4],    % position 1
                [1,5],      % position 2
                [0,4],      % position 3
                [1,3,5],    % position 4
                [2,4]       % position 5
            ],
            Queue0 = queue:new(),
            Queue1 = queue:in({Start,0}, Queue0),
            Visited0 = maps:put(Start, true, #{}),
            bfs(Queue1, Visited0, Target, Neighbors)
    end.

flatten_board(Board) ->
    lists:foldl(fun(Row, Acc) -> Acc ++ Row end, [], Board).

zero_pos(List) -> zero_pos(List, 0).
zero_pos([0|_],Idx) -> Idx;
zero_pos([_|T],Idx) -> zero_pos(T,Idx+1).

set_nth([_|T],0,V) -> [V|T];
set_nth([H|T],N,V) when N > 0 ->
    [H | set_nth(T,N-1,V)].

swap(List,I,J) ->
    ElemI = lists:nth(I+1, List),
    ElemJ = lists:nth(J+1, List),
    L1 = set_nth(List, I, ElemJ),
    set_nth(L1, J, ElemI).

bfs(Queue, Visited, Target, Neighbors) ->
    case queue:is_empty(Queue) of
        true -> -1;
        false ->
            {{value,{State,Steps}}, QRest} = queue:out(Queue),
            if State == Target ->
                    Steps;
               true ->
                    ZPos = zero_pos(State),
                    NeighborList = lists:nth(ZPos+1, Neighbors),
                    {NewQ, NewVisited} = process_neighbors(NeighborList, State, ZPos, Steps, QRest, Visited),
                    bfs(NewQ, NewVisited, Target, Neighbors)
            end
    end.

process_neighbors([], _State, _ZPos, _Steps, Queue, Visited) ->
    {Queue, Visited};
process_neighbors([N|Rest], State, ZPos, Steps, Queue, Visited) ->
    NewState = swap(State, ZPos, N),
    case maps:is_key(NewState, Visited) of
        true ->
            process_neighbors(Rest, State, ZPos, Steps, Queue, Visited);
        false ->
            V1 = maps:put(NewState, true, Visited),
            Q1 = queue:in({NewState, Steps+1}, Queue),
            process_neighbors(Rest, State, ZPos, Steps, Q1, V1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sliding_puzzle(board :: [[integer]]) :: integer
  def sliding_puzzle(board) do
    target = "123450"

    start_state =
      board
      |> List.flatten()
      |> Enum.map(&Integer.to_string/1)
      |> Enum.join()

    if start_state == target, do: 0, else bfs(start_state, target)
  end

  defp bfs(start_state, target) do
    adj = %{
      0 => [1, 3],
      1 => [0, 2, 4],
      2 => [1, 5],
      3 => [0, 4],
      4 => [1, 3, 5],
      5 => [2, 4]
    }

    visited = MapSet.new([start_state])
    queue = :queue.from_list([{start_state, 0}])

    bfs_loop(queue, visited, target, adj)
  end

  defp bfs_loop(queue, visited, target, adj) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{state, moves}, q} ->
        if state == target do
          moves
        else
          zero_pos = find_zero(state)

          {new_queue, new_visited} =
            Enum.reduce(adj[zero_pos], {q, visited}, fn nb, {q_acc, v_acc} ->
              ns = swap(state, zero_pos, nb)

              if MapSet.member?(v_acc, ns) do
                {q_acc, v_acc}
              else
                {
                  :queue.in({ns, moves + 1}, q_acc),
                  MapSet.put(v_acc, ns)
                }
              end
            end)

          bfs_loop(new_queue, new_visited, target, adj)
        end
    end
  end

  defp find_zero(state) do
    state
    |> String.to_charlist()
    |> Enum.find_index(fn c -> c == ?0 end)
  end

  defp swap(state, i, j) do
    chars = String.to_charlist(state)
    ci = Enum.at(chars, i)
    cj = Enum.at(chars, j)

    chars = List.replace_at(chars, i, cj)
    chars = List.replace_at(chars, j, ci)

    List.to_string(chars)
  end
end
```
