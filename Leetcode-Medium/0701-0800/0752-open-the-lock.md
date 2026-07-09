# 0752. Open the Lock

## Cpp

```cpp
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> blocked(deadends.begin(), deadends.end());
        const string start = "0000";
        if (blocked.count(start)) return -1;
        if (start == target) return 0;

        queue<string> q;
        q.push(start);
        blocked.insert(start); // mark as visited

        int turns = 0;
        while (!q.empty()) {
            ++turns;
            int sz = q.size();
            while (sz--) {
                string cur = q.front(); q.pop();
                for (int i = 0; i < 4; ++i) {
                    char orig = cur[i];
                    int d = orig - '0';
                    // move forward
                    cur[i] = char('0' + (d + 1) % 10);
                    if (!blocked.count(cur)) {
                        if (cur == target) return turns;
                        q.push(cur);
                        blocked.insert(cur);
                    }
                    // move backward
                    cur[i] = char('0' + (d + 9) % 10);
                    if (!blocked.count(cur)) {
                        if (cur == target) return turns;
                        q.push(cur);
                        blocked.insert(cur);
                    }
                    cur[i] = orig; // restore
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        if (dead.contains("0000")) return -1;
        if ("0000".equals(target)) return 0;

        Queue<String> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>(dead);
        queue.offer("0000");
        visited.add("0000");

        int turns = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String cur = queue.poll();
                if (cur.equals(target)) return turns;

                char[] chars = cur.toCharArray();
                for (int j = 0; j < 4; j++) {
                    char original = chars[j];

                    // turn wheel forward
                    chars[j] = original == '9' ? '0' : (char) (original + 1);
                    String up = new String(chars);
                    if (!visited.contains(up)) {
                        visited.add(up);
                        queue.offer(up);
                    }

                    // turn wheel backward
                    chars[j] = original == '0' ? '9' : (char) (original - 1);
                    String down = new String(chars);
                    if (!visited.contains(down)) {
                        visited.add(down);
                        queue.offer(down);
                    }

                    // restore original digit
                    chars[j] = original;
                }
            }
            turns++;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        from collections import deque

        start = "0000"
        dead_set = set(deadends)
        if start == target:
            return 0
        if start in dead_set:
            return -1

        visited = set()
        visited.update(dead_set)
        visited.add(start)

        q = deque([start])
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                cur = q.popleft()
                # generate neighbors
                cur_list = list(cur)
                for i in range(4):
                    orig_digit = int(cur_list[i])
                    for delta in (-1, 1):
                        nd = (orig_digit + delta) % 10
                        nxt = cur[:i] + str(nd) + cur[i+1:]
                        if nxt == target:
                            return steps
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
        return -1
```

## Python3

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        start = "0000"
        if start == target:
            return 0

        dead = set(deadends)
        if start in dead:
            return -1

        visited = set(dead)
        visited.add(start)

        q = deque([start])
        steps = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return steps
                for i in range(4):
                    digit = int(cur[i])
                    for nxt in ((digit + 1) % 10, (digit - 1) % 10):
                        nxt_state = cur[:i] + str(nxt) + cur[i+1:]
                        if nxt_state not in visited:
                            visited.add(nxt_state)
                            q.append(nxt_state)
            steps += 1
        return -1
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int strToInt(const char *s) {
    int v = 0;
    for (int i = 0; i < 4; ++i) {
        v = v * 10 + (s[i] - '0');
    }
    return v;
}

int openLock(char** deadends, int deadendsSize, char* target) {
    const int MAX_STATE = 10000;
    bool visited[MAX_STATE] = {false};
    int dist[MAX_STATE];
    for (int i = 0; i < MAX_STATE; ++i) dist[i] = -1;

    // mark deadends as visited
    for (int i = 0; i < deadendsSize; ++i) {
        int d = strToInt(deadends[i]);
        visited[d] = true;
    }

    int start = 0; // "0000"
    if (visited[start]) return -1;

    int targetVal = strToInt(target);
    if (start == targetVal) return 0;

    // BFS queue
    int q[MAX_STATE];
    int head = 0, tail = 0;
    q[tail++] = start;
    visited[start] = true;
    dist[start] = 0;

    const int pow10[4] = {1000, 100, 10, 1};

    while (head < tail) {
        int cur = q[head++];
        int curDist = dist[cur];
        // generate neighbors
        for (int i = 0; i < 4; ++i) {
            int digit = (cur / pow10[i]) % 10;
            int up = (digit + 1) % 10;
            int down = (digit + 9) % 10; // equivalent to -1 mod 10

            int neighbor_up = cur + (up - digit) * pow10[i];
            if (!visited[neighbor_up]) {
                if (neighbor_up == targetVal) return curDist + 1;
                visited[neighbor_up] = true;
                dist[neighbor_up] = curDist + 1;
                q[tail++] = neighbor_up;
            }

            int neighbor_down = cur + (down - digit) * pow10[i];
            if (!visited[neighbor_down]) {
                if (neighbor_down == targetVal) return curDist + 1;
                visited[neighbor_down] = true;
                dist[neighbor_down] = curDist + 1;
                q[tail++] = neighbor_down;
            }
        }
    }

    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int OpenLock(string[] deadends, string target)
    {
        var deadSet = new HashSet<string>(deadends);
        const string start = "0000";
        if (deadSet.Contains(start))
            return -1;
        if (target == start)
            return 0;

        var visited = new HashSet<string>(deadSet);
        var queue = new Queue<string>();
        queue.Enqueue(start);
        visited.Add(start);

        int turns = 0;
        while (queue.Count > 0)
        {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++)
            {
                string cur = queue.Dequeue();
                if (cur == target)
                    return turns;

                char[] chars = cur.ToCharArray();
                for (int j = 0; j < 4; j++)
                {
                    char original = chars[j];
                    int digit = original - '0';

                    // turn wheel forward
                    chars[j] = (char)('0' + (digit + 1) % 10);
                    string next = new string(chars);
                    if (!visited.Contains(next))
                    {
                        visited.Add(next);
                        queue.Enqueue(next);
                    }

                    // turn wheel backward
                    chars[j] = (char)('0' + (digit + 9) % 10); // equivalent to -1 mod 10
                    next = new string(chars);
                    if (!visited.Contains(next))
                    {
                        visited.Add(next);
                        queue.Enqueue(next);
                    }

                    // restore original digit for next wheel iteration
                    chars[j] = original;
                }
            }
            turns++;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
var openLock = function(deadends, target) {
    const start = "0000";
    if (start === target) return 0;
    
    const deadSet = new Set(deadends);
    if (deadSet.has(start)) return -1;
    
    const visited = new Set(deadSet);
    visited.add(start);
    
    const queue = [start];
    let steps = 0;
    let head = 0;
    
    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const cur = queue[head++];
            if (cur === target) return steps;
            
            for (let pos = 0; pos < 4; pos++) {
                const digit = cur.charCodeAt(pos) - 48; // '0' -> 0
                const up = (digit + 1) % 10;
                const down = (digit + 9) % 10;
                
                const upStr = cur.slice(0, pos) + String.fromCharCode(up + 48) + cur.slice(pos + 1);
                if (!visited.has(upStr)) {
                    visited.add(upStr);
                    queue.push(upStr);
                }
                
                const downStr = cur.slice(0, pos) + String.fromCharCode(down + 48) + cur.slice(pos + 1);
                if (!visited.has(downStr)) {
                    visited.add(downStr);
                    queue.push(downStr);
                }
            }
        }
        steps++;
    }
    
    return -1;
};
```

## Typescript

```typescript
function openLock(deadends: string[], target: string): number {
    const deadSet = new Set<string>(deadends);
    if (deadSet.has("0000")) return -1;

    const visited = new Set<string>(deadSet);
    const queue: string[] = ["0000"];
    visited.add("0000");
    let head = 0;
    let steps = 0;

    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const cur = queue[head++];
            if (cur === target) return steps;

            for (let pos = 0; pos < 4; pos++) {
                const digit = cur.charCodeAt(pos) - 48; // '0' -> 0
                for (const delta of [-1, 1]) {
                    const nd = (digit + delta + 10) % 10;
                    const next =
                        cur.slice(0, pos) + nd.toString() + cur.slice(pos + 1);
                    if (!visited.has(next)) {
                        visited.add(next);
                        queue.push(next);
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
     * @param String[] $deadends
     * @param String $target
     * @return Integer
     */
    function openLock($deadends, $target) {
        $dead = array_flip($deadends);
        $start = "0000";

        if (isset($dead[$start])) {
            return -1;
        }
        if ($target === $start) {
            return 0;
        }

        $queue = new SplQueue();
        $queue->enqueue([$start, 0]);

        // visited includes deadends to avoid revisiting them
        $visited = $dead;
        $visited[$start] = true;

        while (!$queue->isEmpty()) {
            [$node, $steps] = $queue->dequeue();

            if ($node === $target) {
                return $steps;
            }

            for ($i = 0; $i < 4; $i++) {
                $digit = intval($node[$i]);
                foreach ([-1, 1] as $diff) {
                    $newDigit = ($digit + $diff + 10) % 10;
                    $newNode = $node;
                    $newNode[$i] = (string)$newDigit;

                    if (!isset($visited[$newNode])) {
                        $visited[$newNode] = true;
                        $queue->enqueue([$newNode, $steps + 1]);
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
    func openLock(_ deadends: [String], _ target: String) -> Int {
        let deadSet = Set(deadends)
        if deadSet.contains("0000") { return -1 }
        if target == "0000" { return 0 }
        
        var visited = deadSet
        visited.insert("0000")
        
        var queue = [String]()
        queue.append("0000")
        var head = 0
        var steps = 0
        
        while head < queue.count {
            let levelSize = queue.count - head
            for _ in 0..<levelSize {
                let node = queue[head]
                head += 1
                if node == target { return steps }
                
                let chars = Array(node)
                for i in 0..<4 {
                    let digit = Int(String(chars[i]))!
                    
                    // turn wheel forward (+1)
                    var upChars = chars
                    upChars[i] = Character("\((digit + 1) % 10)")
                    let upStr = String(upChars)
                    if !visited.contains(upStr) {
                        visited.insert(upStr)
                        queue.append(upStr)
                    }
                    
                    // turn wheel backward (-1)
                    var downChars = chars
                    downChars[i] = Character("\((digit + 9) % 10)") // (digit - 1 + 10) % 10
                    let downStr = String(downChars)
                    if !visited.contains(downStr) {
                        visited.insert(downStr)
                        queue.append(downStr)
                    }
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
    fun openLock(deadends: Array<String>, target: String): Int {
        val deadSet = HashSet<String>(deadends.size)
        for (d in deadends) deadSet.add(d)

        if ("0000" == target) return 0
        if (deadSet.contains("0000")) return -1

        val visited = HashSet<String>()
        visited.addAll(deadSet)

        val queue: ArrayDeque<String> = ArrayDeque()
        queue.add("0000")
        visited.add("0000")

        var steps = 0
        while (!queue.isEmpty()) {
            val levelSize = queue.size
            repeat(levelSize) {
                val cur = queue.removeFirst()
                if (cur == target) return steps
                for (i in 0 until 4) {
                    val chars = cur.toCharArray()
                    val digit = chars[i] - '0'
                    // turn wheel up
                    var up = (digit + 1) % 10
                    chars[i] = ('0' + up)
                    val upStr = String(chars)
                    if (!visited.contains(upStr)) {
                        visited.add(upStr)
                        queue.add(upStr)
                    }
                    // turn wheel down
                    var down = (digit + 9) % 10
                    chars[i] = ('0' + down)
                    val downStr = String(chars)
                    if (!visited.contains(downStr)) {
                        visited.add(downStr)
                        queue.add(downStr)
                    }
                }
            }
            steps++
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int openLock(List<String> deadends, String target) {
    Set<String> dead = deadends.toSet();
    if (dead.contains('0000')) return -1;
    if (target == '0000') return 0;

    Set<String> visited = {...dead};
    List<String> queue = [];
    int head = 0;
    queue.add('0000');
    visited.add('0000');

    int steps = 0;
    while (head < queue.length) {
      int levelSize = queue.length - head;
      for (int i = 0; i < levelSize; i++) {
        String cur = queue[head++];
        if (cur == target) return steps;
        for (int j = 0; j < 4; j++) {
          int digit = cur.codeUnitAt(j) - 48;

          int nd1 = (digit + 1) % 10;
          String nb1 = cur.substring(0, j) + nd1.toString() + cur.substring(j + 1);
          if (!visited.contains(nb1)) {
            visited.add(nb1);
            queue.add(nb1);
          }

          int nd2 = (digit + 9) % 10; // equivalent to (digit - 1 + 10) % 10
          String nb2 = cur.substring(0, j) + nd2.toString() + cur.substring(j + 1);
          if (!visited.contains(nb2)) {
            visited.add(nb2);
            queue.add(nb2);
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
func openLock(deadends []string, target string) int {
    deadSet := make(map[string]bool)
    for _, d := range deadends {
        deadSet[d] = true
    }

    start := "0000"
    if deadSet[start] {
        return -1
    }
    if target == start {
        return 0
    }

    visited := make(map[string]bool)
    for k := range deadSet {
        visited[k] = true
    }

    queue := []string{start}
    visited[start] = true
    steps := 0

    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            cur := queue[0]
            queue = queue[1:]

            if cur == target {
                return steps
            }

            b := []byte(cur)
            for j := 0; j < 4; j++ {
                orig := b[j]
                digit := int(orig - '0')
                for _, d := range []int{-1, 1} {
                    nd := (digit + d + 10) % 10
                    b[j] = byte('0' + nd)
                    nb := string(b)
                    if !visited[nb] {
                        visited[nb] = true
                        queue = append(queue, nb)
                    }
                }
                b[j] = orig
            }
        }
        steps++
    }

    return -1
}
```

## Ruby

```ruby
require 'set'

def open_lock(deadends, target)
  dead_set = Set.new(deadends)
  start = "0000"
  return -1 if dead_set.include?(start)
  return 0 if start == target

  visited = Set.new([start])
  queue = [start]
  head = 0
  steps = 0

  while head < queue.length
    level_end = queue.length
    while head < level_end
      cur = queue[head]
      head += 1
      return steps if cur == target

      4.times do |i|
        digit = cur[i].ord - 48

        up_digit = (digit + 1) % 10
        up_state = cur[0...i] + up_digit.to_s + cur[(i + 1)..-1]
        unless dead_set.include?(up_state) || visited.include?(up_state)
          visited << up_state
          queue << up_state
        end

        down_digit = (digit - 1) % 10
        down_state = cur[0...i] + down_digit.to_s + cur[(i + 1)..-1]
        unless dead_set.include?(down_state) || visited.include?(down_state)
          visited << down_state
          queue << down_state
        end
      end
    end
    steps += 1
  end

  -1
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{Queue, Set}
  
  def openLock(deadends: Array[String], target: String): Int = {
    val deadSet = deadends.toSet
    if (deadSet.contains("0000")) return -1
    if (target == "0000") return 0

    val visited: Set[String] = Set() ++= deadSet
    val queue: Queue[String] = Queue()
    queue.enqueue("0000")
    visited.add("0000")

    var steps = 0
    while (queue.nonEmpty) {
      val levelSize = queue.size
      for (_ <- 0 until levelSize) {
        val cur = queue.dequeue()
        if (cur == target) return steps

        val chars = cur.toCharArray
        for (i <- 0 until 4) {
          val orig = chars(i)

          // turn wheel forward
          chars(i) = ((orig - '0' + 1) % 10 + '0').toChar
          val up = new String(chars)
          if (!visited.contains(up)) {
            visited.add(up)
            queue.enqueue(up)
          }

          // turn wheel backward
          chars(i) = ((orig - '0' + 9) % 10 + '0').toChar
          val down = new String(chars)
          if (!visited.contains(down)) {
            visited.add(down)
            queue.enqueue(down)
          }

          // restore original digit
          chars(i) = orig
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
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        let mut dead_set: HashSet<i32> = HashSet::new();
        for d in deadends.iter() {
            dead_set.insert(Self::str_to_int(d));
        }
        let target_val = Self::str_to_int(&target);
        if dead_set.contains(&0) {
            return -1;
        }
        if target_val == 0 {
            return 0;
        }

        let mut visited: HashSet<i32> = dead_set.clone();
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new(); // (state, steps)
        queue.push_back((0, 0));
        visited.insert(0);

        while let Some((state, steps)) = queue.pop_front() {
            if state == target_val {
                return steps;
            }
            for pos in 0..4 {
                let pow = 10_i32.pow(3 - pos as u32);
                let digit = (state / pow) % 10;
                for delta in [-1i32, 1] {
                    let nd = (digit + delta + 10) % 10;
                    let new_state = state + (nd - digit) * pow;
                    if !visited.contains(&new_state) {
                        visited.insert(new_state);
                        queue.push_back((new_state, steps + 1));
                    }
                }
            }
        }

        -1
    }

    fn str_to_int(s: &str) -> i32 {
        s.bytes().fold(0, |acc, b| acc * 10 + (b - b'0') as i32)
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(provide open-lock)

(define/contract (open-lock deadends target)
  (-> (listof string?) string? exact-integer?)
  (let* ((start "0000")
         (dead-set (make-hash)))
    ;; insert deadends into the visited set
    (for ([d (in-list deadends)])
      (hash-set! dead-set d #t))
    (cond
      [(string=? start target) 0]
      [(hash-has-key? dead-set start) -1]
      [else
       (hash-set! dead-set start #t)
       (let loop ((frontier (list start)) (turns 0))
         (if (null? frontier)
             -1
             (if (member target frontier string=?)
                 turns
                 (let* ([next-frontier
                         (for/fold ([acc '()]) ([node (in-list frontier)])
                           (let inner ((i 0) (acc acc))
                             (if (= i 4)
                                 acc
                                 (let* ([up   (make-neighbor node i 1)]
                                        [down (make-neighbor node i -1)]
                                        [new-acc
                                         (foldl (lambda (nbr a)
                                                  (if (hash-has-key? dead-set nbr)
                                                      a
                                                      (begin (hash-set! dead-set nbr #t)
                                                             (cons nbr a))))
                                                acc
                                                (list up down))])
                                   (inner (+ i 1) new-acc))))]) )
                   (loop next-frontier (+ turns 1))))]))]))

(define (make-neighbor s idx delta)
  (let* ((vec (string->vector s))
         (c (vector-ref vec idx))
         (digit (- (char->integer c) (char->integer #\0)))
         (new-digit (modulo (+ digit delta) 10))
         (new-char (integer->char (+ new-digit (char->integer #\0)))))
    (vector-set! vec idx new-char)
    (vector->string vec)))
```

## Erlang

```erlang
-export([open_lock/2]).

-spec open_lock(Deadends :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
open_lock(Deadends, Target) ->
    DeadSet = maps:from_list([{D, true} || D <- Deadends]),
    Start = <<"0000">>,
    case maps:is_key(Start, DeadSet) of
        true -> -1;
        false ->
            Visited0 = maps:put(Start, true, DeadSet),
            bfs([Start], Visited0, Target, 0)
    end.

bfs([], _Visited, _Target, _Steps) -> -1;
bfs(CurrentLevel, Visited, Target, Steps) ->
    case lists:any(fun(Node) -> Node =:= Target end, CurrentLevel) of
        true -> Steps;
        false ->
            {NextLevel, NewVisited} = generate_next(CurrentLevel, Visited),
            bfs(NextLevel, NewVisited, Target, Steps + 1)
    end.

generate_next(Nodes, Visited) ->
    lists:foldl(fun(Node, {AccList, Vis}) ->
        Ns = neighbors(Node),
        lists:foldl(fun(N, {A, V}) ->
                case maps:is_key(N, V) of
                    true -> {A, V};
                    false -> {[N | A], maps:put(N, true, V)}
                end
            end, {AccList, Vis}, Ns)
    end, {[], Visited}, Nodes).

neighbors(Node) ->
    Bytes = binary_to_list(Node),
    lists:foldl(fun(Pos, Acc) ->
        Digit = lists:nth(Pos + 1, Bytes),
        NextDigit = ((Digit - $0 + 1) rem 10) + $0,
        PrevDigit = ((Digit - $0 + 9) rem 10) + $0,
        ListNext = replace_at(Bytes, Pos, NextDigit),
        ListPrev = replace_at(Bytes, Pos, PrevDigit),
        [list_to_binary(ListNext), list_to_binary(ListPrev) | Acc]
    end, [], lists:seq(0, 3)).

replace_at(List, Index, NewVal) ->
    {Head, [_Old | Tail]} = lists:split(Index, List),
    Head ++ [NewVal] ++ Tail.
```

## Elixir

```elixir
defmodule Solution do
  @spec open_lock(deadends :: [String.t()], target :: String.t()) :: integer()
  def open_lock(deadends, target) do
    dead_set = MapSet.new(deadends)
    start = "0000"

    cond do
      start == target ->
        0

      MapSet.member?(dead_set, start) ->
        -1

      true ->
        visited = MapSet.put(dead_set, start)
        queue = :queue.from_list([{start, 0}])
        bfs(queue, visited, target)
    end
  end

  defp bfs(queue, visited, target) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {state, steps}}, q_rest} ->
        if state == target do
          steps
        else
          {new_queue, new_visited} =
            Enum.reduce(neighbors(state), {q_rest, visited}, fn nb, {q_acc, v_acc} ->
              if MapSet.member?(v_acc, nb) do
                {q_acc, v_acc}
              else
                {:queue.in({nb, steps + 1}, q_acc), MapSet.put(v_acc, nb)}
              end
            end)

          bfs(new_queue, new_visited, target)
        end
    end
  end

  defp neighbors(state) do
    chars = String.graphemes(state)

    for i <- 0..3, delta <- [-1, 1] do
      digit = String.to_integer(Enum.at(chars, i))
      ndigit = rem(digit + delta + 10, 10)
      new_chars = List.replace_at(chars, i, Integer.to_string(ndigit))
      Enum.join(new_chars)
    end
  end
end
```
