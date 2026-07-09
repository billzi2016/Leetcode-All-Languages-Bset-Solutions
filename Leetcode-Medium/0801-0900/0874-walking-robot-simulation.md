# 0874. Walking Robot Simulation

## Cpp

```cpp
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<long long> obs;
        obs.reserve(obstacles.size() * 2 + 1);
        for (const auto& p : obstacles) {
            long long key = ((long long)p[0] << 32) ^ (static_cast<unsigned int>(p[1]));
            obs.insert(key);
        }
        // directions: north, east, south, west
        const int dx[4] = {0, 1, 0, -1};
        const int dy[4] = {1, 0, -1, 0};
        int dir = 0; // start facing north
        int x = 0, y = 0;
        int maxDist2 = 0;
        for (int cmd : commands) {
            if (cmd == -2) {               // turn left
                dir = (dir + 3) % 4;
            } else if (cmd == -1) {        // turn right
                dir = (dir + 1) % 4;
            } else {
                for (int step = 0; step < cmd; ++step) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    long long key = ((long long)nx << 32) ^ (static_cast<unsigned int>(ny));
                    if (obs.find(key) != obs.end()) {
                        break;
                    }
                    x = nx;
                    y = ny;
                }
                maxDist2 = max(maxDist2, x * x + y * y);
            }
        }
        return maxDist2;
    }
};
```

## Java

```java
class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        java.util.HashSet<Long> obstacleSet = new java.util.HashSet<>();
        for (int[] obs : obstacles) {
            long key = ((long)obs[0] << 32) ^ (obs[1] & 0xffffffffL);
            obstacleSet.add(key);
        }
        // direction vectors: north, east, south, west
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int dir = 0; // start facing north
        int x = 0, y = 0;
        int maxDistSq = 0;
        for (int cmd : commands) {
            if (cmd == -2) { // turn left
                dir = (dir + 3) % 4;
            } else if (cmd == -1) { // turn right
                dir = (dir + 1) % 4;
            } else {
                for (int step = 0; step < cmd; step++) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    long key = ((long)nx << 32) ^ (ny & 0xffffffffL);
                    if (obstacleSet.contains(key)) {
                        break;
                    }
                    x = nx;
                    y = ny;
                    int distSq = x * x + y * y;
                    if (distSq > maxDistSq) {
                        maxDistSq = distSq;
                    }
                }
            }
        }
        return maxDistSq;
    }
}
```

## Python

```python
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # store obstacles as a set of coordinate tuples for O(1) lookup
        obs_set = set(map(tuple, obstacles))
        
        # direction vectors: North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # start facing north
        
        x = y = 0
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -2:          # turn left
                dir_idx = (dir_idx + 3) % 4
            elif cmd == -1:        # turn right
                dir_idx = (dir_idx + 1) % 4
            else:
                dx, dy = dirs[dir_idx]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs_set:
                        break
                    x, y = nx, ny
                    max_dist_sq = max(max_dist_sq, x * x + y * y)
        return max_dist_sq
```

## Python3

```python
from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = { (x, y) for x, y in obstacles }
        # Directions: North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # start facing north
        x = y = 0
        max_dist_sq = 0

        for cmd in commands:
            if cmd == -2:          # turn left
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:        # turn right
                dir_idx = (dir_idx + 1) % 4
            else:                  # move forward cmd steps
                dx, dy = dirs[dir_idx]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    max_dist_sq = max(max_dist_sq, x * x + y * y)

        return max_dist_sq
```

## C

```c
#include <stdlib.h>

static int cmp_ll(const void *a, const void *b) {
    long long va = *(const long long *)a;
    long long vb = *(const long long *)b;
    return (va > vb) - (va < vb);
}

int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesSize, int* obstaclesColSize) {
    long long *obs = NULL;
    if (obstaclesSize > 0) {
        obs = (long long *)malloc(sizeof(long long) * obstaclesSize);
        for (int i = 0; i < obstaclesSize; ++i) {
            int x = obstacles[i][0];
            int y = obstacles[i][1];
            obs[i] = ((long long)x << 32) ^ (unsigned int)y;
        }
        qsort(obs, obstaclesSize, sizeof(long long), cmp_ll);
    }

    int dir = 0;                     // 0:N, 1:E, 2:S, 3:W
    const int dx[4] = {0, 1, 0, -1};
    const int dy[4] = {1, 0, -1, 0};

    int x = 0, y = 0;
    int maxDist2 = 0;

    for (int i = 0; i < commandsSize; ++i) {
        int cmd = commands[i];
        if (cmd == -2) {                 // turn left
            dir = (dir + 3) % 4;
        } else if (cmd == -1) {          // turn right
            dir = (dir + 1) % 4;
        } else {
            for (int step = 0; step < cmd; ++step) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                int blocked = 0;
                if (obstaclesSize > 0) {
                    long long key = ((long long)nx << 32) ^ (unsigned int)ny;
                    void *found = bsearch(&key, obs, obstaclesSize, sizeof(long long), cmp_ll);
                    if (found != NULL) blocked = 1;
                }
                if (blocked) break;
                x = nx;
                y = ny;
                int dist2 = x * x + y * y;
                if (dist2 > maxDist2) maxDist2 = dist2;
            }
        }
    }

    if (obs) free(obs);
    return maxDist2;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int RobotSim(int[] commands, int[][] obstacles) {
        var obstacleSet = new HashSet<(int, int)>();
        foreach (var ob in obstacles) {
            obstacleSet.Add((ob[0], ob[1]));
        }

        // Directions: North, East, South, West
        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };
        int dir = 0; // start facing north

        int x = 0, y = 0;
        long maxDist2 = 0;

        foreach (int cmd in commands) {
            if (cmd == -2) {               // turn left
                dir = (dir + 3) % 4;
            } else if (cmd == -1) {        // turn right
                dir = (dir + 1) % 4;
            } else {
                for (int step = 0; step < cmd; ++step) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (obstacleSet.Contains((nx, ny))) {
                        break;
                    }
                    x = nx;
                    y = ny;
                    long dist2 = (long)x * x + (long)y * y;
                    if (dist2 > maxDist2) {
                        maxDist2 = dist2;
                    }
                }
            }
        }

        return (int)maxDist2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} commands
 * @param {number[][]} obstacles
 * @return {number}
 */
var robotSim = function(commands, obstacles) {
    const obstacleSet = new Set();
    for (const [ox, oy] of obstacles) {
        obstacleSet.add(`${ox},${oy}`);
    }
    
    // direction vectors: North, East, South, West
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    let dir = 0; // start facing north
    let x = 0, y = 0;
    let maxDistSq = 0;
    
    for (const cmd of commands) {
        if (cmd === -2) {          // turn left
            dir = (dir + 3) % 4;
        } else if (cmd === -1) {   // turn right
            dir = (dir + 1) % 4;
        } else {
            for (let step = 0; step < cmd; step++) {
                const nx = x + dx[dir];
                const ny = y + dy[dir];
                if (obstacleSet.has(`${nx},${ny}`)) {
                    break;
                }
                x = nx;
                y = ny;
                const distSq = x * x + y * y;
                if (distSq > maxDistSq) maxDistSq = distSq;
            }
        }
    }
    
    return maxDistSq;
};
```

## Typescript

```typescript
function robotSim(commands: number[], obstacles: number[][]): number {
    const obstacleSet = new Set<string>();
    for (const [ox, oy] of obstacles) {
        obstacleSet.add(`${ox},${oy}`);
    }

    // Directions: North, East, South, West
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    let dir = 0; // start facing north

    let x = 0, y = 0;
    let maxDistSq = 0;

    for (const cmd of commands) {
        if (cmd === -2) {               // turn left
            dir = (dir + 3) % 4;
        } else if (cmd === -1) {        // turn right
            dir = (dir + 1) % 4;
        } else {
            for (let step = 0; step < cmd; ++step) {
                const nx = x + dx[dir];
                const ny = y + dy[dir];
                if (obstacleSet.has(`${nx},${ny}`)) {
                    break;
                }
                x = nx;
                y = ny;
                const distSq = x * x + y * y;
                if (distSq > maxDistSq) maxDistSq = distSq;
            }
        }
    }

    return maxDistSq;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $commands
     * @param Integer[][] $obstacles
     * @return Integer
     */
    function robotSim($commands, $obstacles) {
        // Build obstacle set for O(1) lookup
        $obsSet = [];
        foreach ($obstacles as $o) {
            $key = $o[0] . ',' . $o[1];
            $obsSet[$key] = true;
        }

        // Directions: North, East, South, West
        $dx = [0, 1, 0, -1];
        $dy = [1, 0, -1, 0];
        $dir = 0; // start facing north

        $x = 0;
        $y = 0;
        $maxDist = 0;

        foreach ($commands as $c) {
            if ($c == -2) {               // turn left
                $dir = ($dir + 3) % 4;
            } elseif ($c == -1) {         // turn right
                $dir = ($dir + 1) % 4;
            } else {                      // move forward c steps
                for ($step = 0; $step < $c; $step++) {
                    $nx = $x + $dx[$dir];
                    $ny = $y + $dy[$dir];
                    $key = $nx . ',' . $ny;
                    if (isset($obsSet[$key])) {
                        break; // obstacle encountered
                    }
                    $x = $nx;
                    $y = $ny;
                    $dist = $x * $x + $y * $y;
                    if ($dist > $maxDist) {
                        $maxDist = $dist;
                    }
                }
            }
        }

        return $maxDist;
    }
}
```

## Swift

```swift
class Solution {
    func robotSim(_ commands: [Int], _ obstacles: [[Int]]) -> Int {
        struct Point: Hashable {
            let x: Int
            let y: Int
        }
        
        var obstacleSet = Set<Point>()
        for obs in obstacles where obs.count == 2 {
            obstacleSet.insert(Point(x: obs[0], y: obs[1]))
        }
        
        let dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] // N, E, S, W
        var dirIdx = 0
        var x = 0, y = 0
        var maxDist = 0
        
        for cmd in commands {
            if cmd == -2 {               // turn left
                dirIdx = (dirIdx + 3) % 4
            } else if cmd == -1 {        // turn right
                dirIdx = (dirIdx + 1) % 4
            } else {
                for _ in 0..<cmd {
                    let nx = x + dirs[dirIdx][0]
                    let ny = y + dirs[dirIdx][1]
                    if obstacleSet.contains(Point(x: nx, y: ny)) {
                        break
                    }
                    x = nx
                    y = ny
                    let dist = x * x + y * y
                    if dist > maxDist { maxDist = dist }
                }
            }
        }
        
        return maxDist
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun robotSim(commands: IntArray, obstacles: Array<IntArray>): Int {
        val obstacleSet = HashSet<Long>()
        for (obs in obstacles) {
            val ox = obs[0]
            val oy = obs[1]
            val key = (ox.toLong() shl 32) or (oy.toLong() and 0xffffffffL)
            obstacleSet.add(key)
        }
        var x = 0
        var y = 0
        var dir = 0 // 0:N, 1:E, 2:S, 3:W
        val dx = intArrayOf(0, 1, 0, -1)
        val dy = intArrayOf(1, 0, -1, 0)
        var maxDist = 0
        for (cmd in commands) {
            when (cmd) {
                -2 -> dir = (dir + 3) % 4 // turn left
                -1 -> dir = (dir + 1) % 4 // turn right
                else -> {
                    var steps = cmd
                    while (steps-- > 0) {
                        val nx = x + dx[dir]
                        val ny = y + dy[dir]
                        val key = (nx.toLong() shl 32) or (ny.toLong() and 0xffffffffL)
                        if (!obstacleSet.contains(key)) {
                            x = nx
                            y = ny
                            val dist = x * x + y * y
                            if (dist > maxDist) maxDist = dist
                        } else {
                            break
                        }
                    }
                }
            }
        }
        return maxDist
    }
}
```

## Dart

```dart
class Solution {
  int robotSim(List<int> commands, List<List<int>> obstacles) {
    const int M = 60013;
    final Set<int> obstacleSet = {};
    for (var obs in obstacles) {
      obstacleSet.add(obs[0] + M * obs[1]);
    }

    const List<List<int>> dirs = [
      [0, 1],   // north
      [1, 0],   // east
      [0, -1],  // south
      [-1, 0]   // west
    ];
    int dirIdx = 0;
    int x = 0, y = 0;
    int maxDistSq = 0;

    for (final cmd in commands) {
      if (cmd == -2) {
        dirIdx = (dirIdx + 3) % 4; // turn left
      } else if (cmd == -1) {
        dirIdx = (dirIdx + 1) % 4; // turn right
      } else {
        for (int step = 0; step < cmd; ++step) {
          final nx = x + dirs[dirIdx][0];
          final ny = y + dirs[dirIdx][1];
          if (obstacleSet.contains(nx + M * ny)) break;
          x = nx;
          y = ny;
          final distSq = x * x + y * y;
          if (distSq > maxDistSq) maxDistSq = distSq;
        }
      }
    }

    return maxDistSq;
  }
}
```

## Golang

```go
func robotSim(commands []int, obstacles [][]int) int {
	type point struct{ x, y int }
	obstacleSet := make(map[point]struct{}, len(obstacles))
	for _, o := range obstacles {
		obstacleSet[point{o[0], o[1]}] = struct{}{}
	}
	// directions: north, east, south, west
	dx := []int{0, 1, 0, -1}
	dy := []int{1, 0, -1, 0}
	dir := 0 // start facing north
	x, y := 0, 0
	maxDist := 0

	for _, cmd := range commands {
		switch cmd {
		case -2: // turn left
			dir = (dir + 3) % 4
		case -1: // turn right
			dir = (dir + 1) % 4
		default:
			for step := 0; step < cmd; step++ {
				nx, ny := x+dx[dir], y+dy[dir]
				if _, ok := obstacleSet[point{nx, ny}]; ok {
					break
				}
				x, y = nx, ny
				dist := x*x + y*y
				if dist > maxDist {
					maxDist = dist
				}
			}
		}
	}
	return maxDist
}
```

## Ruby

```ruby
require 'set'

def robot_sim(commands, obstacles)
  obstacle_set = Set.new
  obstacles.each { |ox, oy| obstacle_set.add([ox, oy]) }

  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  dir_idx = 0
  x = y = 0
  max_dist2 = 0

  commands.each do |c|
    if c == -2
      dir_idx = (dir_idx + 3) % 4
    elsif c == -1
      dir_idx = (dir_idx + 1) % 4
    else
      dx, dy = dirs[dir_idx]
      c.times do
        nx = x + dx
        ny = y + dy
        break if obstacle_set.include?([nx, ny])
        x = nx
        y = ny
        cur = x * x + y * y
        max_dist2 = cur if cur > max_dist2
      end
    end
  end

  max_dist2
end
```

## Scala

```scala
object Solution {
  def robotSim(commands: Array[Int], obstacles: Array[Array[Int]]): Int = {
    val obstacleSet = scala.collection.mutable.HashSet[Long]()
    for (obs <- obstacles) {
      val key = (obs(0).toLong << 32) | (obs(1).toLong & 0xffffffffL)
      obstacleSet.add(key)
    }

    val dx = Array(0, 1, 0, -1)
    val dy = Array(1, 0, -1, 0)

    var x = 0
    var y = 0
    var dir = 0 // 0:N,1:E,2:S,3:W
    var maxDist: Long = 0L

    for (cmd <- commands) {
      cmd match {
        case -2 => dir = (dir + 3) % 4          // turn left
        case -1 => dir = (dir + 1) % 4          // turn right
        case steps =>
          var s = steps
          while (s > 0) {
            val nx = x + dx(dir)
            val ny = y + dy(dir)
            val key = (nx.toLong << 32) | (ny.toLong & 0xffffffffL)
            if (obstacleSet.contains(key)) {
              s = 0 // stop moving for this command
            } else {
              x = nx
              y = ny
              val dist = x.toLong * x + y.toLong * y
              if (dist > maxDist) maxDist = dist
              s -= 1
            }
          }
      }
    }

    maxDist.toInt
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let mut obstacle_set: HashSet<(i32, i32)> = HashSet::new();
        for obs in obstacles.iter() {
            if obs.len() == 2 {
                obstacle_set.insert((obs[0], obs[1]));
            }
        }

        // direction vectors: North, East, South, West
        let dx = [0, 1, 0, -1];
        let dy = [1, 0, -1, 0];
        let mut dir = 0; // start facing north

        let (mut x, mut y) = (0i32, 0i32);
        let mut max_dist: i64 = 0;

        for cmd in commands {
            match cmd {
                -2 => { // turn left
                    dir = (dir + 3) % 4;
                }
                -1 => { // turn right
                    dir = (dir + 1) % 4;
                }
                steps if steps > 0 => {
                    for _ in 0..steps {
                        let nx = x + dx[dir];
                        let ny = y + dy[dir];
                        if obstacle_set.contains(&(nx, ny)) {
                            break;
                        } else {
                            x = nx;
                            y = ny;
                            let dist = (x as i64) * (x as i64) + (y as i64) * (y as i64);
                            if dist > max_dist {
                                max_dist = dist;
                            }
                        }
                    }
                }
                _ => {}
            }
        }

        max_dist as i32
    }
}
```

## Racket

```racket
(define/contract (robot-sim commands obstacles)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ([MULT 60013]
         [encode (lambda (x y) (+ x (* MULT y)))]
         [obs (make-hash)])
    ;; store obstacles
    (for ([p obstacles])
      (hash-set! obs (encode (first p) (second p)) #t))
    (define dx '#(0 1 0 -1))
    (define dy '#(1 0 -1 0))
    (let loop ((cmds commands)
               (x 0) (y 0) (dir 0) (maxd 0))
      (if (null? cmds)
          maxd
          (let* ([c (car cmds)])
            (cond
              [(= c -2) ; turn left
               (loop (cdr cmds) x y (modulo (- dir 1) 4) maxd)]
              [(= c -1) ; turn right
               (loop (cdr cmds) x y (modulo (+ dir 1) 4) maxd)]
              [else ; move forward c steps
               (let step-loop ((steps c) (cx x) (cy y) (curmax maxd))
                 (if (= steps 0)
                     (loop (cdr cmds) cx cy dir curmax)
                     (let* ([nx (+ cx (vector-ref dx dir))]
                            [ny (+ cy (vector-ref dy dir))])
                       (if (hash-has-key? obs (encode nx ny))
                           (loop (cdr cmds) cx cy dir curmax) ; obstacle blocks further movement for this command
                           (let ([newmax (max curmax (+ (* nx nx) (* ny ny)))])
                             (step-loop (- steps 1) nx ny newmax))))))]))))))
```

## Erlang

```erlang
-module(solution).
-export([robot_sim/2]).

-spec robot_sim(Commands :: [integer()], Obstacles :: [[integer()]]) -> integer().
robot_sim(Commands, Obstacles) ->
    ObstacleSet = maps:from_list([{ {X,Y}, true } || [X,Y] <- Obstacles]),
    process_commands(Commands, 0, 0, 0, 0, ObstacleSet).

%% Process the list of commands recursively.
process_commands([], _DirIdx, _X, _Y, MaxDist, _Obs) ->
    MaxDist;
process_commands([Cmd | Rest], DirIdx, X, Y, MaxDist, Obs) ->
    case Cmd of
        -2 -> % turn left
            NewDir = (DirIdx + 3) rem 4,
            process_commands(Rest, NewDir, X, Y, MaxDist, Obs);
        -1 -> % turn right
            NewDir = (DirIdx + 1) rem 4,
            process_commands(Rest, NewDir, X, Y, MaxDist, Obs);
        Steps when Steps > 0 ->
            {NX, NY, NMax} = move_steps(Steps, DirIdx, X, Y, MaxDist, Obs),
            process_commands(Rest, DirIdx, NX, NY, NMax, Obs)
    end.

%% Move forward step by step, stopping at obstacles.
move_steps(0, _DirIdx, X, Y, MaxDist, _Obs) ->
    {X, Y, MaxDist};
move_steps(N, DirIdx, X, Y, MaxDist, Obs) ->
    {DX, DY} = direction(DirIdx),
    NX = X + DX,
    NY = Y + DY,
    case maps:is_key({NX, NY}, Obs) of
        true ->
            {X, Y, MaxDist}; % obstacle encountered, stop moving
        false ->
            Dist = NX * NX + NY * NY,
            NewMax = if Dist > MaxDist -> Dist; true -> MaxDist end,
            move_steps(N - 1, DirIdx, NX, NY, NewMax, Obs)
    end.

%% Direction vectors: 0=N, 1=E, 2=S, 3=W
direction(0) -> {0, 1};
direction(1) -> {1, 0};
direction(2) -> {0, -1};
direction(3) -> {-1, 0}.
```

## Elixir

```elixir
defmodule Solution do
  @spec robot_sim(commands :: [integer], obstacles :: [[integer]]) :: integer
  def robot_sim(commands, obstacles) do
    obstacle_set = MapSet.new(Enum.map(obstacles, fn [x, y] -> {x, y} end))

    dirs = [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]
    initial_state = %{x: 0, y: 0, dir: 0, max: 0}

    final_state =
      Enum.reduce(commands, initial_state, fn cmd, state ->
        case cmd do
          -2 ->
            %{state | dir: rem(state.dir + 3, 4)}

          -1 ->
            %{state | dir: rem(state.dir + 1, 4)}

          steps when steps > 0 ->
            {dx, dy} = Enum.at(dirs, state.dir)

            {new_x, new_y, new_max} =
              move_steps(steps, dx, dy, state.x, state.y, state.max, obstacle_set)

            %{state | x: new_x, y: new_y, max: new_max}
        end
      end)

    final_state.max
  end

  defp move_steps(steps, dx, dy, x, y, cur_max, obstacles) do
    Enum.reduce_while(1..steps, {x, y, cur_max}, fn _, {cx, cy, cmax} ->
      nx = cx + dx
      ny = cy + dy

      if MapSet.member?(obstacles, {nx, ny}) do
        {:halt, {cx, cy, cmax}}
      else
        ndist = nx * nx + ny * ny
        nmax = if ndist > cmax, do: ndist, else: cmax
        {:cont, {nx, ny, nmax}}
      end
    end)
  end
end
```
