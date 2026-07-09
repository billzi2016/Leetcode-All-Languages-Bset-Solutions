# 0909. Snakes and Ladders

## Cpp

```cpp
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        int target = n * n;
        vector<bool> visited(target + 1, false);
        queue<pair<int,int>> q; // {square, steps}
        q.push({1, 0});
        visited[1] = true;
        
        auto getPos = [&](int s) -> pair<int,int> {
            int quot = (s - 1) / n;
            int rem = (s - 1) % n;
            int r = n - 1 - quot;
            int c = (quot % 2 == 0) ? rem : (n - 1 - rem);
            return {r, c};
        };
        
        while (!q.empty()) {
            auto [cur, steps] = q.front();
            q.pop();
            if (cur == target) return steps;
            for (int dice = 1; dice <= 6; ++dice) {
                int nxt = cur + dice;
                if (nxt > target) break;
                auto [r, c] = getPos(nxt);
                int dest = board[r][c] != -1 ? board[r][c] : nxt;
                if (!visited[dest]) {
                    visited[dest] = true;
                    q.push({dest, steps + 1});
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
    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        int target = n * n;
        boolean[] visited = new boolean[target + 1];
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        queue.offer(1);
        visited[1] = true;
        int moves = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int cur = queue.poll();
                if (cur == target) return moves;
                for (int dice = 1; dice <= 6; dice++) {
                    int next = cur + dice;
                    if (next > target) break;
                    int[] rc = getPos(next, n);
                    int r = rc[0], c = rc[1];
                    if (board[r][c] != -1) {
                        next = board[r][c];
                    }
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.offer(next);
                    }
                }
            }
            moves++;
        }
        return -1;
    }

    private int[] getPos(int s, int n) {
        int quot = (s - 1) / n;
        int rem = (s - 1) % n;
        int row = n - 1 - quot;
        int col = (quot % 2 == 0) ? rem : n - 1 - rem;
        return new int[]{row, col};
    }
}
```

## Python

```python
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(board)

        def get_pos(s):
            # convert square number (1-indexed) to board coordinates
            s -= 1
            row_from_bottom = s // n
            r = n - 1 - row_from_bottom
            c_idx = s % n
            if row_from_bottom % 2 == 0:
                c = c_idx
            else:
                c = n - 1 - c_idx
            return r, c

        target = n * n
        visited = [False] * (target + 1)
        q = deque()
        q.append((1, 0))  # (square, moves)
        visited[1] = True

        while q:
            cur, moves = q.popleft()
            if cur == target:
                return moves
            for dice in range(1, 7):
                nxt = cur + dice
                if nxt > target:
                    continue
                r, c = get_pos(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, moves + 1))
        return -1
```

## Python3

```python
class Solution:
    def snakesAndLadders(self, board):
        from collections import deque
        n = len(board)

        def get_pos(s):
            s -= 1
            row_from_bottom = s // n
            col_idx = s % n
            r = n - 1 - row_from_bottom
            if row_from_bottom % 2 == 0:
                c = col_idx
            else:
                c = n - 1 - col_idx
            return r, c

        target = n * n
        visited = [False] * (target + 1)
        q = deque()
        q.append((1, 0))
        visited[1] = True

        while q:
            cur, moves = q.popleft()
            if cur == target:
                return moves
            for dice in range(1, 7):
                nxt = cur + dice
                if nxt > target:
                    continue
                r, c = get_pos(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, moves + 1))
        return -1
```

## C

```c
#include <stdlib.h>

int snakesAndLadders(int** board, int boardSize, int* boardColSize) {
    int n = boardSize;
    int total = n * n;

    char *visited = (char *)calloc(total + 1, sizeof(char));
    int *dist = (int *)malloc((total + 1) * sizeof(int));
    for (int i = 0; i <= total; ++i) dist[i] = -1;

    int *queue = (int *)malloc((total + 5) * sizeof(int));
    int head = 0, tail = 0;

    visited[1] = 1;
    dist[1] = 0;
    queue[tail++] = 1;

    while (head < tail) {
        int cur = queue[head++];
        if (cur == total) {
            int ans = dist[cur];
            free(visited);
            free(dist);
            free(queue);
            return ans;
        }
        for (int dice = 1; dice <= 6; ++dice) {
            int nxt = cur + dice;
            if (nxt > total) break;

            int q = (nxt - 1) / n;               // rows moved up from bottom
            int r = n - 1 - q;                    // actual row index
            int rem = (nxt - 1) % n;
            int c = (q % 2 == 0) ? rem : (n - 1 - rem); // column based on direction

            if (board[r][c] != -1) nxt = board[r][c];

            if (!visited[nxt]) {
                visited[nxt] = 1;
                dist[nxt] = dist[cur] + 1;
                queue[tail++] = nxt;
            }
        }
    }

    free(visited);
    free(dist);
    free(queue);
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int SnakesAndLadders(int[][] board)
    {
        int n = board.Length;
        int target = n * n;
        int[] dist = new int[target + 1];
        for (int i = 0; i <= target; i++) dist[i] = -1;

        var q = new System.Collections.Generic.Queue<int>();
        dist[1] = 0;
        q.Enqueue(1);

        while (q.Count > 0)
        {
            int cur = q.Dequeue();
            if (cur == target) return dist[cur];

            for (int dice = 1; dice <= 6; dice++)
            {
                int nxt = cur + dice;
                if (nxt > target) break;

                var rc = GetPos(nxt, n);
                int r = rc.Item1, c = rc.Item2;
                int dest = board[r][c] == -1 ? nxt : board[r][c];

                if (dist[dest] == -1)
                {
                    dist[dest] = dist[cur] + 1;
                    q.Enqueue(dest);
                }
            }
        }

        return -1;
    }

    private (int, int) GetPos(int s, int n)
    {
        int quot = (s - 1) / n;
        int rem = (s - 1) % n;
        int row = n - 1 - quot;
        int col = (quot & 1) == 0 ? rem : n - 1 - rem;
        return (row, col);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function(board) {
    const n = board.length;
    const target = n * n;
    const visited = new Array(target + 1).fill(false);
    const queue = [];
    let head = 0;
    
    queue.push(1);
    visited[1] = true;
    let moves = 0;
    
    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const cur = queue[head++];
            if (cur === target) return moves;
            for (let dice = 1; dice <= 6; dice++) {
                let nxt = cur + dice;
                if (nxt > target) continue;
                const [r, c] = getPos(nxt);
                if (board[r][c] !== -1) {
                    nxt = board[r][c];
                }
                if (!visited[nxt]) {
                    visited[nxt] = true;
                    queue.push(nxt);
                }
            }
        }
        moves++;
    }
    
    return -1;
    
    function getPos(s) {
        const quot = Math.floor((s - 1) / n);
        const rem = (s - 1) % n;
        const row = n - 1 - quot;
        const col = (quot % 2 === 0) ? rem : n - 1 - rem;
        return [row, col];
    }
};
```

## Typescript

```typescript
function snakesAndLadders(board: number[][]): number {
    const n = board.length;
    const target = n * n;
    const visited = new Array(target + 1).fill(false);
    const queue: number[] = [];
    const steps: number[] = [];
    let head = 0;

    visited[1] = true;
    queue.push(1);
    steps.push(0);

    while (head < queue.length) {
        const cur = queue[head];
        const step = steps[head];
        head++;

        if (cur === target) return step;

        for (let dice = 1; dice <= 6; dice++) {
            let nxt = cur + dice;
            if (nxt > target) continue;

            const [r, c] = getPos(nxt);
            if (board[r][c] !== -1) {
                nxt = board[r][c];
            }

            if (!visited[nxt]) {
                visited[nxt] = true;
                if (nxt === target) return step + 1;
                queue.push(nxt);
                steps.push(step + 1);
            }
        }
    }

    return -1;

    function getPos(s: number): [number, number] {
        const quot = Math.floor((s - 1) / n);
        const rem = (s - 1) % n;
        const row = n - 1 - quot;
        const col = quot % 2 === 0 ? rem : n - 1 - rem;
        return [row, col];
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function snakesAndLadders($board) {
        $n = count($board);
        $target = $n * $n;
        $visited = array_fill(0, $target + 1, false);

        $queue = new SplQueue();
        $queue->enqueue([1, 0]); // position, steps
        $visited[1] = true;

        while (!$queue->isEmpty()) {
            [$pos, $steps] = $queue->dequeue();

            if ($pos == $target) {
                return $steps;
            }

            for ($dice = 1; $dice <= 6; $dice++) {
                $next = $pos + $dice;
                if ($next > $target) {
                    continue;
                }

                // map square number to board coordinates
                $quotient = intdiv($next - 1, $n);
                $remainder = ($next - 1) % $n;
                $row = $n - 1 - $quotient;

                if ((($n - $row) & 1) == 1) { // left to right
                    $col = $remainder;
                } else { // right to left
                    $col = $n - 1 - $remainder;
                }

                $dest = ($board[$row][$col] != -1) ? $board[$row][$col] : $next;

                if (!$visited[$dest]) {
                    $visited[$dest] = true;
                    $queue->enqueue([$dest, $steps + 1]);
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
    func snakesAndLadders(_ board: [[Int]]) -> Int {
        let n = board.count
        let target = n * n
        var visited = Array(repeating: false, count: target + 1)
        var queue: [(Int, Int)] = []   // (square, moves)
        queue.append((1, 0))
        visited[1] = true
        var index = 0
        
        while index < queue.count {
            let (curr, steps) = queue[index]
            index += 1
            if curr == target { return steps }
            
            for dice in 1...6 {
                var next = curr + dice
                if next > target { continue }
                
                let (r, c) = position(of: next, size: n)
                let dest = board[r][c]
                if dest != -1 {
                    next = dest
                }
                
                if !visited[next] {
                    visited[next] = true
                    queue.append((next, steps + 1))
                }
            }
        }
        return -1
    }
    
    private func position(of square: Int, size n: Int) -> (Int, Int) {
        let quot = (square - 1) / n
        let rem = (square - 1) % n
        let row = n - 1 - quot
        let col: Int
        if quot % 2 == 0 {
            col = rem
        } else {
            col = n - 1 - rem
        }
        return (row, col)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun snakesAndLadders(board: Array<IntArray>): Int {
        val n = board.size
        val target = n * n
        val visited = BooleanArray(target + 1)
        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        queue.add(1)
        visited[1] = true
        var moves = 0

        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val cur = queue.poll()
                if (cur == target) return moves
                for (dice in 1..6) {
                    var next = cur + dice
                    if (next > target) continue

                    val rowFromBottom = (next - 1) / n
                    val r = n - 1 - rowFromBottom
                    val cIdx = (next - 1) % n
                    val col = if (rowFromBottom % 2 == 0) cIdx else n - 1 - cIdx

                    var dest = next
                    val cell = board[r][col]
                    if (cell != -1) {
                        dest = cell
                    }

                    if (!visited[dest]) {
                        visited[dest] = true
                        queue.add(dest)
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
  int snakesAndLadders(List<List<int>> board) {
    int n = board.length;
    int target = n * n;

    List<int> getPos(int s) {
      int rowFromBottom = (s - 1) ~/ n;
      int colInRow = (s - 1) % n;
      int r = n - 1 - rowFromBottom;
      int c = (rowFromBottom % 2 == 0) ? colInRow : n - 1 - colInRow;
      return [r, c];
    }

    List<int> dist = List.filled(target + 1, -1);
    Queue<int> q = Queue<int>();
    dist[1] = 0;
    q.add(1);

    while (q.isNotEmpty) {
      int cur = q.removeFirst();
      if (cur == target) return dist[cur];
      for (int dice = 1; dice <= 6; ++dice) {
        int nxt = cur + dice;
        if (nxt > target) continue;
        var rc = getPos(nxt);
        int r = rc[0], c = rc[1];
        if (board[r][c] != -1) {
          nxt = board[r][c];
        }
        if (dist[nxt] == -1) {
          dist[nxt] = dist[cur] + 1;
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
func snakesAndLadders(board [][]int) int {
    n := len(board)
    target := n * n

    // Convert square number to board coordinates.
    getPos := func(s int) (int, int) {
        s-- // zero‑based
        row := n - 1 - s/n
        col := s % n
        if ((n-1-row)%2 == 1) { // reversed direction on this row
            col = n - 1 - col
        }
        return row, col
    }

    visited := make([]bool, target+1)
    queue := []int{1}
    visited[1] = true
    steps := 0

    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            cur := queue[0]
            queue = queue[1:]

            if cur == target {
                return steps
            }

            for nxt := cur + 1; nxt <= cur+6 && nxt <= target; nxt++ {
                r, c := getPos(nxt)
                dest := nxt
                if board[r][c] != -1 {
                    dest = board[r][c]
                }
                if !visited[dest] {
                    visited[dest] = true
                    queue = append(queue, dest)
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
def snakes_and_ladders(board)
  n = board.size
  total = n * n
  get_pos = lambda do |num|
    r_from_bottom = (num - 1) / n
    row = n - 1 - r_from_bottom
    col = (num - 1) % n
    col = n - 1 - col if r_from_bottom.odd?
    [row, col]
  end

  visited = Array.new(total + 1, false)
  queue = [[1, 0]]
  visited[1] = true
  idx = 0

  while idx < queue.size
    cur, steps = queue[idx]
    idx += 1
    return steps if cur == total
    (1..6).each do |dice|
      nxt = cur + dice
      break if nxt > total
      r, c = get_pos.call(nxt)
      dest = board[r][c]
      final = dest == -1 ? nxt : dest
      next if visited[final]
      visited[final] = true
      queue << [final, steps + 1]
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def snakesAndLadders(board: Array[Array[Int]]): Int = {
        val n = board.length
        val target = n * n
        val dist = Array.fill(target + 1)(-1)
        import scala.collection.mutable.Queue
        val q = Queue[Int]()
        dist(1) = 0
        q.enqueue(1)

        def getPos(s: Int): (Int, Int) = {
            val quot = (s - 1) / n
            val rem = (s - 1) % n
            val r = n - 1 - quot
            val c = if ((quot & 1) == 0) rem else n - 1 - rem
            (r, c)
        }

        while (q.nonEmpty) {
            val cur = q.dequeue()
            if (cur == target) return dist(cur)
            for (dice <- 1 to 6) {
                var nxt = cur + dice
                if (nxt <= target) {
                    val (r, c) = getPos(nxt)
                    val dest = board(r)(c)
                    if (dest != -1) nxt = dest
                    if (dist(nxt) == -1) {
                        dist(nxt) = dist(cur) + 1
                        q.enqueue(nxt)
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
    pub fn snakes_and_ladders(board: Vec<Vec<i32>>) -> i32 {
        use std::collections::VecDeque;
        let n = board.len();
        let total = n * n;

        // Convert square number (1-indexed) to board coordinates (row, col)
        let to_coord = |s: usize| -> (usize, usize) {
            let quot = (s - 1) / n;
            let rem = (s - 1) % n;
            let row = n - 1 - quot;
            // direction depends on distance from bottom
            if ((n - 1 - row) % 2) == 0 {
                // left to right
                (row, rem)
            } else {
                // right to left
                (row, n - 1 - rem)
            }
        };

        let mut visited = vec![false; total + 1];
        let mut q: VecDeque<(usize, i32)> = VecDeque::new();
        q.push_back((1, 0));
        visited[1] = true;

        while let Some((pos, steps)) = q.pop_front() {
            if pos == total {
                return steps;
            }
            for dice in 1..=6 {
                let mut next = pos + dice;
                if next > total {
                    continue;
                }
                let (r, c) = to_coord(next);
                if board[r][c] != -1 {
                    next = board[r][c] as usize;
                }
                if !visited[next] {
                    visited[next] = true;
                    q.push_back((next, steps + 1));
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define (square->coord s n)
  (let* ((z (- s 1))
         (row-from-bottom (quotient z n))
         (row (- (- n 1) row-from-bottom))
         (pos-in-row (remainder z n))
         (col (if (even? row-from-bottom)
                  pos-in-row
                  (- n 1 pos-in-row))))
    (values row col)))

(define/contract (snakes-and-ladders board)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length board))
         (target (* n n))
         (visited (make-vector (+ target 1) #f)))
    (vector-set! visited 1 #t)
    (let bfs ((queue (list 1)) (moves 0))
      (cond
        [(null? queue) -1]
        [(member target queue) moves]
        [else
         (let next-level ((remaining queue) (next '()))
           (if (null? remaining)
               (bfs (reverse next) (+ moves 1))
               (let* ((pos (car remaining)))
                 (let loop-dice ((d 1) (acc next))
                   (if (> d 6)
                       (next-level (cdr remaining) acc)
                       (let ((dest (+ pos d)))
                         (if (> dest target)
                             (loop-dice (+ d 1) acc)
                             (let-values ([(row col) (square->coord dest n)])
                               (let* ((cell (list-ref (list-ref board row) col))
                                      (final (if (= cell -1) dest cell)))
                                 (if (vector-ref visited final)
                                     (loop-dice (+ d 1) acc)
                                     (begin
                                       (vector-set! visited final #t)
                                       (loop-dice (+ d 1) (cons final acc))))))))))))))])))))
```

## Erlang

```erlang
-module(solution).
-export([snakes_and_ladders/1]).

snakes_and_ladders(Board) ->
    N = length(Board),
    Max = N * N,
    DestMap = build_dest_map(Board, N, Max),
    Visited0 = maps:put(1, true, #{}),
    Q0 = queue:in({1, 0}, queue:new()),
    bfs(Q0, Visited0, DestMap, Max).

build_dest_map(Board, N, Max) ->
    build_dest_map(1, Board, N, Max, #{}).

build_dest_map(S, _Board, _N, Max, Map) when S > Max ->
    Map;
build_dest_map(S, Board, N, Max, Map) ->
    {Row, Col} = square_to_pos(S, N),
    RowList = lists:nth(Row + 1, Board),
    Value = lists:nth(Col + 1, RowList),
    Dest = case Value of
        -1 -> S;
        _ -> Value
    end,
    NewMap = maps:put(S, Dest, Map),
    build_dest_map(S + 1, Board, N, Max, NewMap).

square_to_pos(S, N) ->
    RFromBottom = (S - 1) div N,
    CInRow = (S - 1) rem N,
    Row = N - 1 - RFromBottom,
    case (RFromBottom band 1) of
        0 -> Col = CInRow;
        1 -> Col = N - 1 - CInRow
    end,
    {Row, Col}.

bfs(Q, Visited, DestMap, Max) ->
    case queue:out(Q) of
        {empty, _} ->
            -1;
        {{value, {Curr, Steps}}, Q1} ->
            if Curr == Max ->
                    Steps;
               true ->
                    {NewQ, NewVis} = process_dice(Curr, Steps, lists:seq(1, 6), Q1, Visited, DestMap, Max),
                    bfs(NewQ, NewVis, DestMap, Max)
            end
    end.

process_dice(_Curr, _Steps, [], Q, Vis, _DestMap, _Max) ->
    {Q, Vis};
process_dice(Curr, Steps, [D | Rest], Q, Vis, DestMap, Max) ->
    Next = Curr + D,
    if Next > Max ->
            process_dice(Curr, Steps, Rest, Q, Vis, DestMap, Max);
       true ->
            Dest = maps:get(Next, DestMap),
            case maps:is_key(Dest, Vis) of
                true ->
                    process_dice(Curr, Steps, Rest, Q, Vis, DestMap, Max);
                false ->
                    NewVis = maps:put(Dest, true, Vis),
                    NewQ = queue:in({Dest, Steps + 1}, Q),
                    process_dice(Curr, Steps, Rest, NewQ, NewVis, DestMap, Max)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec snakes_and_ladders(board :: [[integer]]) :: integer
  def snakes_and_ladders(board) do
    n = length(board)
    total = n * n

    start_queue = :queue.in({1, 0}, :queue.new())
    visited = MapSet.new([1])

    bfs(start_queue, visited, board, n, total)
  end

  defp bfs(queue, visited, board, n, total) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {square, steps}}, q_rest} ->
        if square == total do
          steps
        else
          {new_queue, new_visited} =
            Enum.reduce(1..6, {q_rest, visited}, fn dice, {q_acc, vis_acc} ->
              nxt = square + dice

              if nxt > total do
                {q_acc, vis_acc}
              else
                final = destination(board, nxt, n)

                if MapSet.member?(vis_acc, final) do
                  {q_acc, vis_acc}
                else
                  {
                    :queue.in({final, steps + 1}, q_acc),
                    MapSet.put(vis_acc, final)
                  }
                end
              end
            end)

          bfs(new_queue, new_visited, board, n, total)
        end
    end
  end

  defp destination(board, sq, n) do
    {r, c} = to_coord(sq, n)
    val = board |> Enum.at(r) |> Enum.at(c)

    if val != -1, do: val, else: sq
  end

  defp to_coord(sq, n) do
    idx = sq - 1
    row_from_bottom = div(idx, n)
    r = n - 1 - row_from_bottom
    col_in_row = rem(idx, n)

    c =
      if rem(row_from_bottom, 2) == 0,
        do: col_in_row,
        else: n - 1 - col_in_row

    {r, c}
  end
end
```
