# 1036. Escape a Large Maze

## Cpp

```cpp
class Solution {
public:
    bool isEscapePossible(vector<vector<int>>& blocked, vector<int>& source, vector<int>& target) {
        unordered_set<long long> blockSet;
        for (auto& b : blocked) {
            blockSet.insert(((long long)b[0] << 20) | b[1]);
        }
        return bfs(source, target, blockSet) && bfs(target, source, blockSet);
    }

private:
    const int LIMIT = 1000000;
    
    bool bfs(const vector<int>& start, const vector<int>& finish,
             const unordered_set<long long>& blockSet) {
        if (blockSet.empty()) return true;
        int n = blockSet.size();
        long long maxSteps = 1LL * n * (n - 1) / 2;   // upper bound of enclosed area
        
        auto encode = [&](int x, int y) -> long long {
            return ((long long)x << 20) | y;
        };
        
        queue<pair<int,int>> q;
        unordered_set<long long> visited;
        q.emplace(start[0], start[1]);
        visited.insert(encode(start[0], start[1]));
        
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty() && (long long)visited.size() <= maxSteps) {
            auto [x, y] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                if (nx < 0 || ny < 0 || nx >= LIMIT || ny >= LIMIT) continue;
                long long code = encode(nx, ny);
                if (blockSet.count(code) || visited.count(code)) continue;
                if (nx == finish[0] && ny == finish[1]) return true;
                q.emplace(nx, ny);
                visited.insert(code);
            }
        }
        // If we have explored more than the maximal enclosed area, escape is possible.
        return (long long)visited.size() > maxSteps;
    }
};
```

## Java

```java
class Solution {
    private static final int MAX = 1_000_000;
    private static final int[][] DIRS = {{1,0},{-1,0},{0,1},{0,-1}};
    
    public boolean isEscapePossible(int[][] blocked, int[] source, int[] target) {
        if (blocked == null || blocked.length == 0) return true;
        int n = blocked.length;
        long limit = (long)n * (n - 1) / 2; // maximum area that can be enclosed
        
        java.util.Set<Long> blockedSet = new java.util.HashSet<>();
        for (int[] b : blocked) {
            blockedSet.add(encode(b[0], b[1]));
        }
        
        return bfs(source, target, blockedSet, limit) && bfs(target, source, blockedSet, limit);
    }
    
    private boolean bfs(int[] start, int[] finish, java.util.Set<Long> blockedSet, long limit) {
        java.util.Deque<int[]> dq = new java.util.ArrayDeque<>();
        java.util.Set<Long> visited = new java.util.HashSet<>();
        dq.offer(start);
        visited.add(encode(start[0], start[1]));
        
        while (!dq.isEmpty() && visited.size() <= limit) {
            int[] cur = dq.poll();
            if (cur[0] == finish[0] && cur[1] == finish[1]) return true;
            for (int[] d : DIRS) {
                int nx = cur[0] + d[0];
                int ny = cur[1] + d[1];
                if (nx < 0 || nx >= MAX || ny < 0 || ny >= MAX) continue;
                long code = encode(nx, ny);
                if (blockedSet.contains(code) || visited.contains(code)) continue;
                visited.add(code);
                dq.offer(new int[]{nx, ny});
            }
        }
        // If we explored more than limit cells, we are not trapped.
        return visited.size() > limit;
    }
    
    private long encode(int x, int y) {
        return ((long)x << 32) | (y & 0xffffffffL);
    }
}
```

## Python

```python
class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        if not blocked:
            return True

        B = set(map(tuple, blocked))
        n = len(blocked)
        # maximum area that can be enclosed by n blocked cells
        limit = n * (n - 1) // 2

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(start, finish):
            from collections import deque
            q = deque()
            visited = set()
            q.append((start[0], start[1]))
            visited.add((start[0], start[1]))
            steps = 0
            while q and steps <= limit:
                x, y = q.popleft()
                if [x, y] == finish:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in B and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
                steps += 1
            # If we explored more than limit cells, we are not trapped
            return steps > limit

        return bfs(source, target) and bfs(target, source)
```

## Python3

```python
import collections
from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True

        B = len(blocked)
        limit = B * (B - 1) // 2  # maximum area that can be enclosed
        blocked_set = { (x, y) for x, y in blocked }
        MAX_COORD = 10**6

        def bfs(start: List[int], finish: List[int]) -> bool:
            q = collections.deque()
            visited = set()
            sx, sy = start
            fx, fy = finish
            q.append((sx, sy))
            visited.add((sx, sy))
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            while q and len(visited) <= limit:
                x, y = q.popleft()
                if (x, y) == (fx, fy):
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < MAX_COORD and 0 <= ny < MAX_COORD and (nx, ny) not in blocked_set and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))

            # If we explored more than limit cells, we are not trapped.
            return len(visited) > limit

        return bfs(source, target) and bfs(target, source)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    unsigned long long *table;
    int size;
} HashSet;

static const unsigned long long EMPTY_KEY = ULLONG_MAX;

static void hs_init(HashSet *hs, int expected) {
    int sz = 1;
    while (sz < expected * 2) sz <<= 1;
    hs->size = sz;
    hs->table = (unsigned long long *)malloc(sizeof(unsigned long long) * sz);
    for (int i = 0; i < sz; ++i) hs->table[i] = EMPTY_KEY;
}

static int hs_contains(const HashSet *hs, unsigned long long key) {
    int mask = hs->size - 1;
    int idx = (int)(key & mask);
    while (hs->table[idx] != EMPTY_KEY) {
        if (hs->table[idx] == key) return 1;
        idx = (idx + 1) & mask;
    }
    return 0;
}

static void hs_insert(HashSet *hs, unsigned long long key) {
    int mask = hs->size - 1;
    int idx = (int)(key & mask);
    while (hs->table[idx] != EMPTY_KEY && hs->table[idx] != key) {
        idx = (idx + 1) & mask;
    }
    hs->table[idx] = key;
}

/* BFS limited to 'limit' explored cells.
   Returns true if target is reachable or exploration exceeds limit. */
static int bfs(int sx, int sy, int tx, int ty, const HashSet *blocked, int limit) {
    if (sx == tx && sy == ty) return 1;

    HashSet visited;
    hs_init(&visited, limit * 2 + 10);

    unsigned long long startKey = ((unsigned long long)sx << 20) | (unsigned long long)sy;
    hs_insert(&visited, startKey);

    int maxNodes = limit > 0 ? limit + 5 : 5;
    int *qx = (int *)malloc(sizeof(int) * maxNodes);
    int *qy = (int *)malloc(sizeof(int) * maxNodes);
    int front = 0, back = 0;

    qx[back] = sx;
    qy[back] = sy;
    ++back;

    int visitedCount = 1;
    const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

    while (front < back) {
        int x = qx[front];
        int y = qy[front];
        ++front;

        for (int d = 0; d < 4; ++d) {
            int nx = x + dirs[d][0];
            int ny = y + dirs[d][1];

            if (nx < 0 || ny < 0 || nx >= 1000000 || ny >= 1000000) continue;

            unsigned long long key = ((unsigned long long)nx << 20) | (unsigned long long)ny;
            if (hs_contains(blocked, key)) continue;
            if (hs_contains(&visited, key)) continue;

            if (nx == tx && ny == ty) {
                free(qx);
                free(qy);
                free(visited.table);
                return 1;
            }

            hs_insert(&visited, key);
            ++visitedCount;
            if (visitedCount > limit) {
                free(qx);
                free(qy);
                free(visited.table);
                return 1;
            }

            qx[back] = nx;
            qy[back] = ny;
            ++back;
        }
    }

    free(qx);
    free(qy);
    free(visited.table);
    return 0;   // exhausted reachable area within limit
}

bool isEscapePossible(int** blocked, int blockedSize, int* blockedColSize,
                      int* source, int sourceSize, int* target, int targetSize) {
    if (blockedSize == 0) return true;

    HashSet bset;
    hs_init(&bset, blockedSize * 2 + 10);
    for (int i = 0; i < blockedSize; ++i) {
        unsigned long long key = ((unsigned long long)blocked[i][0] << 20) |
                                 (unsigned long long)blocked[i][1];
        hs_insert(&bset, key);
    }

    int limit = blockedSize * (blockedSize - 1) / 2;

    if (!bfs(source[0], source[1], target[0], target[1], &bset, limit)) {
        free(bset.table);
        return false;
    }
    if (!bfs(target[0], target[1], source[0], source[1], &bset, limit)) {
        free(bset.table);
        return false;
    }

    free(bset.table);
    return true;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private static readonly int[][] dirs = new int[][] {
        new int[] {0, 1},
        new int[] {1, 0},
        new int[] {0, -1},
        new int[] {-1, 0}
    };
    
    public bool IsEscapePossible(int[][] blocked, int[] source, int[] target) {
        if (blocked == null || blocked.Length == 0) return true;
        
        var blockedSet = new HashSet<long>();
        foreach (var b in blocked) {
            long key = ((long)b[0] << 32) | (uint)b[1];
            blockedSet.Add(key);
        }
        
        long limit = (long)blocked.Length * (blocked.Length - 1) / 2;
        
        bool CanEscape(int[] start, int[] finish) {
            var visited = new HashSet<long>();
            var queue = new Queue<int[]>();
            queue.Enqueue(start);
            visited.Add(((long)start[0] << 32) | (uint)start[1]);
            
            while (queue.Count > 0 && visited.Count <= limit) {
                var cur = queue.Dequeue();
                if (cur[0] == finish[0] && cur[1] == finish[1]) return true;
                
                foreach (var d in dirs) {
                    int nx = cur[0] + d[0];
                    int ny = cur[1] + d[1];
                    
                    if (nx < 0 || ny < 0 || nx >= 1000000 || ny >= 1000000) continue;
                    
                    long key = ((long)nx << 32) | (uint)ny;
                    if (blockedSet.Contains(key) || visited.Contains(key)) continue;
                    
                    visited.Add(key);
                    queue.Enqueue(new int[] { nx, ny });
                }
            }
            
            return visited.Count > limit;
        }
        
        return CanEscape(source, target) && CanEscape(target, source);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} blocked
 * @param {number[]} source
 * @param {number[]} target
 * @return {boolean}
 */
var isEscapePossible = function(blocked, source, target) {
    const BLOCKED_SET = new Set();
    for (const [x, y] of blocked) {
        BLOCKED_SET.add(`${x},${y}`);
    }
    const B = blocked.length;
    const LIMIT = B * (B - 1) / 2; // max area that can be enclosed
    const DIRS = [[1,0],[-1,0],[0,1],[0,-1]];
    const MAX = 1000000;

    function bfs(start, finish) {
        const visited = new Set();
        const queue = [];
        let head = 0;
        const startKey = `${start[0]},${start[1]}`;
        visited.add(startKey);
        queue.push(start);

        while (head < queue.length && visited.size <= LIMIT) {
            const [x, y] = queue[head++];
            if (x === finish[0] && y === finish[1]) return true;
            for (const [dx, dy] of DIRS) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || ny < 0 || nx >= MAX || ny >= MAX) continue;
                const key = `${nx},${ny}`;
                if (BLOCKED_SET.has(key) || visited.has(key)) continue;
                visited.add(key);
                queue.push([nx, ny]);
            }
        }
        // If we explored more than LIMIT cells, we're not trapped.
        return visited.size > LIMIT;
    }

    return bfs(source, target) && bfs(target, source);
};
```

## Typescript

```typescript
function isEscapePossible(blocked: number[][], source: number[], target: number[]): boolean {
    const blockedSet = new Set<string>();
    for (const b of blocked) {
        blockedSet.add(b[0] + ',' + b[1]);
    }
    const maxSteps = blocked.length * (blocked.length - 1) / 2;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const LIMIT = 1_000_000;

    function bfs(start: number[], finish: number[]): boolean {
        const visited = new Set<string>();
        const qx: number[] = [];
        const qy: number[] = [];
        let head = 0;
        qx.push(start[0]);
        qy.push(start[1]);
        visited.add(start[0] + ',' + start[1]);

        while (head < qx.length) {
            const x = qx[head];
            const y = qy[head];
            head++;

            if (x === finish[0] && y === finish[1]) return true;

            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || ny < 0 || nx >= LIMIT || ny >= LIMIT) continue;
                const key = nx + ',' + ny;
                if (blockedSet.has(key) || visited.has(key)) continue;
                visited.add(key);
                qx.push(nx);
                qy.push(ny);
            }

            if (visited.size > maxSteps) return true; // escaped the possible enclosure
        }
        return false;
    }

    return bfs(source, target) && bfs(target, source);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $blocked
     * @param Integer[] $source
     * @param Integer[] $target
     * @return Boolean
     */
    function isEscapePossible($blocked, $source, $target) {
        $blockedSet = [];
        foreach ($blocked as $b) {
            $blockedSet[$b[0] . ',' . $b[1]] = true;
        }
        $bCount = count($blocked);
        if ($bCount == 0) {
            return true;
        }
        // Maximum area that can be completely enclosed by B blocked cells
        $limit = intdiv($bCount * ($bCount - 1), 2);
        return $this->canReach($source, $target, $blockedSet, $limit) &&
               $this->canReach($target, $source, $blockedSet, $limit);
    }

    private function canReach($start, $goal, $blockedSet, $limit) {
        if ($start[0] == $goal[0] && $start[1] == $goal[1]) {
            return true;
        }
        $maxCoord = 1000000 - 1; // grid is [0, 10^6-1] in both dimensions
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        $queue = new SplQueue();
        $queue->enqueue($start);
        $visited = [];
        $keyStart = $start[0] . ',' . $start[1];
        $visited[$keyStart] = true;

        while (!$queue->isEmpty()) {
            $pos = $queue->dequeue();
            foreach ($dirs as $d) {
                $nx = $pos[0] + $d[0];
                $ny = $pos[1] + $d[1];
                if ($nx < 0 || $ny < 0 || $nx > $maxCoord || $ny > $maxCoord) {
                    continue;
                }
                $key = $nx . ',' . $ny;
                if (isset($blockedSet[$key]) || isset($visited[$key])) {
                    continue;
                }
                if ($nx == $goal[0] && $ny == $goal[1]) {
                    return true;
                }
                $queue->enqueue([$nx, $ny]);
                $visited[$key] = true;
                if (count($visited) > $limit) {
                    // Explored more cells than the maximum possible enclosure size
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isEscapePossible(_ blocked: [[Int]], _ source: [Int], _ target: [Int]) -> Bool {
        if blocked.isEmpty { return true }
        let factor = 1_000_000
        var blockedSet = Set<Int>()
        for b in blocked {
            blockedSet.insert(b[0] * factor + b[1])
        }
        let limit = blocked.count * (blocked.count - 1) / 2
        
        func bfs(_ start: [Int], _ finish: [Int]) -> Bool {
            var visited = Set<Int>()
            var queue = [(Int, Int)]()
            let sx = start[0], sy = start[1]
            let tx = finish[0], ty = finish[1]
            visited.insert(sx * factor + sy)
            queue.append((sx, sy))
            var idx = 0
            let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while idx < queue.count {
                if visited.count > limit { return true }
                let (x, y) = queue[idx]
                idx += 1
                if x == tx && y == ty { return true }
                for d in dirs {
                    let nx = x + d.0
                    let ny = y + d.1
                    if nx < 0 || nx >= factor || ny < 0 || ny >= factor { continue }
                    let key = nx * factor + ny
                    if blockedSet.contains(key) || visited.contains(key) { continue }
                    visited.insert(key)
                    queue.append((nx, ny))
                }
            }
            return false
        }
        
        return bfs(source, target) && bfs(target, source)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    private fun encode(x: Int, y: Int): Long = (x.toLong() shl 20) or y.toLong()
    private fun bfs(start: IntArray, finish: IntArray, blockedSet: Set<Long>, limit: Int): Boolean {
        val queue: ArrayDeque<IntArray> = ArrayDeque()
        val visited = HashSet<Long>()
        queue.add(start)
        visited.add(encode(start[0], start[1]))
        while (queue.isNotEmpty() && visited.size <= limit) {
            val cur = queue.removeFirst()
            if (cur[0] == finish[0] && cur[1] == finish[1]) return true
            for (d in dirs) {
                val nx = cur[0] + d[0]
                val ny = cur[1] + d[1]
                if (nx < 0 || nx >= 1_000_000 || ny < 0 || ny >= 1_000_000) continue
                val key = encode(nx, ny)
                if (!blockedSet.contains(key) && !visited.contains(key)) {
                    visited.add(key)
                    queue.add(intArrayOf(nx, ny))
                }
            }
        }
        return visited.size > limit
    }

    fun isEscapePossible(blocked: Array<IntArray>, source: IntArray, target: IntArray): Boolean {
        if (blocked.isEmpty()) return true
        val blockedSet = HashSet<Long>()
        for (b in blocked) {
            blockedSet.add(encode(b[0], b[1]))
        }
        val n = blocked.size
        val limit = n * (n - 1) / 2
        return bfs(source, target, blockedSet, limit) && bfs(target, source, blockedSet, limit)
    }
}
```

## Dart

```dart
class Solution {
  static const int _gridSize = 1000000;
  bool isEscapePossible(List<List<int>> blocked, List<int> source, List<int> target) {
    // Encode blocked cells into a set for O(1) lookup.
    final Set<String> blockedSet = {};
    for (var b in blocked) {
      blockedSet.add('${b[0]},${b[1]}');
    }

    int limit = blocked.length * (blocked.length - 1) ~/ 2;

    bool bfs(List<int> start, List<int> finish) {
      final Set<String> visited = {};
      final List<List<int>> queue = [];
      queue.add(start);
      visited.add('${start[0]},${start[1]}');

      const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
      ];

      int idx = 0;
      while (idx < queue.length && visited.length <= limit) {
        final cur = queue[idx++];
        for (var d in dirs) {
          int nx = cur[0] + d[0];
          int ny = cur[1] + d[1];
          if (nx < 0 || ny < 0 || nx >= _gridSize || ny >= _gridSize) continue;
          String key = '$nx,$ny';
          if (blockedSet.contains(key) || visited.contains(key)) continue;
          if (nx == finish[0] && ny == finish[1]) return true;
          visited.add(key);
          queue.add([nx, ny]);
        }
      }

      // If we explored more than the limit without being blocked,
      // it means we are not trapped.
      return visited.length > limit;
    }

    return bfs(source, target) && bfs(target, source);
  }
}
```

## Golang

```go
func isEscapePossible(blocked [][]int, source []int, target []int) bool {
	if len(blocked) == 0 {
		return true
	}
	const limit = 1000000
	bset := make(map[int64]struct{}, len(blocked))
	for _, p := range blocked {
		key := (int64(p[0]) << 32) | int64(p[1])
		bset[key] = struct{}{}
	}
	maxSteps := len(blocked) * (len(blocked) - 1) / 2

	bfs := func(start, finish []int) bool {
		dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
		visited := make(map[int64]struct{})
		qx := []int{start[0]}
		qy := []int{start[1]}
		startKey := (int64(start[0]) << 32) | int64(start[1])
		visited[startKey] = struct{}{}

		for len(qx) > 0 && len(visited) <= maxSteps {
			x, y := qx[0], qy[0]
			qx, qy = qx[1:], qy[1:]

			if x == finish[0] && y == finish[1] {
				return true
			}
			for _, d := range dir {
				nx, ny := x+d[0], y+d[1]
				if nx < 0 || nx >= limit || ny < 0 || ny >= limit {
					continue
				}
				key := (int64(nx) << 32) | int64(ny)
				if _, ok := bset[key]; ok {
					continue
				}
				if _, ok := visited[key]; ok {
					continue
				}
				visited[key] = struct{}{}
				qx = append(qx, nx)
				qy = append(qy, ny)
			}
		}
		return len(visited) > maxSteps
	}

	return bfs(source, target) && bfs(target, source)
}
```

## Ruby

```ruby
require 'set'

# @param {Integer[][]} blocked
# @param {Integer[]} source
# @param {Integer[]} target
# @return {Boolean}
def is_escape_possible(blocked, source, target)
  return true if blocked.empty?

  limit = 20000 # safe upper bound for trapped area (blocked.length <= 200)

  encode = ->(x, y) { (x << 20) + y }

  blocked_set = Set.new
  blocked.each do |b|
    blocked_set.add(encode.call(b[0], b[1]))
  end

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]
  max_coord = 1_000_000 - 1

  bfs = lambda do |start_x, start_y, finish_x, finish_y|
    visited = Set.new
    queue = []
    head = 0

    start_key = encode.call(start_x, start_y)
    visited.add(start_key)
    queue << [start_x, start_y]

    while head < queue.size && visited.size <= limit
      x, y = queue[head]
      head += 1

      return true if x == finish_x && y == finish_y

      dirs.each do |dx, dy|
        nx = x + dx
        ny = y + dy
        next if nx < 0 || ny < 0 || nx > max_coord || ny > max_coord

        key = encode.call(nx, ny)
        next if blocked_set.include?(key) || visited.include?(key)

        visited.add(key)
        queue << [nx, ny]
      end
    end

    visited.size > limit
  end

  bfs.call(source[0], source[1], target[0], target[1]) &&
    bfs.call(target[0], target[1], source[0], source[1])
end
```

## Scala

```scala
object Solution {
    def isEscapePossible(blocked: Array[Array[Int]], source: Array[Int], target: Array[Int]): Boolean = {
        if (blocked.isEmpty) return true

        val encode = (x: Int, y: Int) => x.toLong * 1000000L + y
        val blockedSet = scala.collection.mutable.HashSet[Long]()
        for (b <- blocked) blockedSet.add(encode(b(0), b(1)))

        val limit = blocked.length * (blocked.length - 1) / 2

        def bfs(start: Array[Int], finish: Array[Int]): Boolean = {
            val visited = scala.collection.mutable.HashSet[Long]()
            val q = new java.util.ArrayDeque[(Int, Int)]()
            q.add((start(0), start(1)))
            visited.add(encode(start(0), start(1)))

            val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
            while (!q.isEmpty && visited.size <= limit) {
                val (x, y) = q.poll()
                if (x == finish(0) && y == finish(1)) return true
                for ((dx, dy) <- dirs) {
                    val nx = x + dx
                    val ny = y + dy
                    if (nx >= 0 && nx < 1000000 && ny >= 0 && ny < 1000000) {
                        val code = encode(nx, ny)
                        if (!blockedSet.contains(code) && !visited.contains(code)) {
                            visited.add(code)
                            q.add((nx, ny))
                        }
                    }
                }
            }
            visited.size > limit
        }

        bfs(source, target) && bfs(target, source)
    }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn is_escape_possible(blocked: Vec<Vec<i32>>, source: Vec<i32>, target: Vec<i32>) -> bool {
        let n = blocked.len();
        if n == 0 {
            return true;
        }
        let limit = n * (n - 1) / 2; // maximum area that can be enclosed

        let mut block_set: HashSet<(i32, i32)> = HashSet::new();
        for b in blocked {
            block_set.insert((b[0], b[1]));
        }

        fn bfs(
            start: (i32, i32),
            finish: (i32, i32),
            block_set: &HashSet<(i32, i32)>,
            limit: usize,
        ) -> bool {
            let mut visited: HashSet<(i32, i32)> = HashSet::new();
            let mut queue: VecDeque<(i32, i32)> = VecDeque::new();

            visited.insert(start);
            queue.push_back(start);

            let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)];
            while let Some((x, y)) = queue.pop_front() {
                if (x, y) == finish {
                    return true;
                }
                for (dx, dy) in dirs.iter() {
                    let nx = x + dx;
                    let ny = y + dy;
                    if nx < 0 || ny < 0 || nx >= 1_000_000 || ny >= 1_000_000 {
                        continue;
                    }
                    let np = (nx, ny);
                    if block_set.contains(&np) || visited.contains(&np) {
                        continue;
                    }
                    visited.insert(np);
                    queue.push_back(np);
                }
                if visited.len() > limit {
                    return true; // escaped the possible enclosure
                }
            }
            false
        }

        let src = (source[0], source[1]);
        let tgt = (target[0], target[1]);

        bfs(src, tgt, &block_set, limit) && bfs(tgt, src, &block_set, limit)
    }
}
```

## Racket

```racket
(define (can-reach? start goal blocked bound)
  (let ((visited (make-hash)))
    (hash-set! visited (cons (first start) (second start)) #t)
    (let bfs-loop ((queue (list start)))
      (cond
        [(null? queue) #f]
        [(> (hash-count visited) bound) #t] ; escaped the possible enclosure
        [else
         (define curr (car queue))
         (define rest (cdr queue))
         (if (equal? curr goal)
             #t
             (let* ((x (first curr)) (y (second curr))
                    (neighbors (list (list (+ x 1) y)
                                     (list (- x 1) y)
                                     (list x (+ y 1))
                                     (list x (- y 1))))
                    (new-nei
                     (filter
                      (lambda (p)
                        (let ((nx (first p)) (ny (second p)))
                          (and (>= nx 0) (< nx 1000000)
                               (>= ny 0) (< ny 1000000)
                               (not (hash-has-key? blocked (cons nx ny)))
                               (not (hash-has-key? visited (cons nx ny))))))
                      neighbors)))
               (for ([p new-nei])
                 (hash-set! visited (cons (first p) (second p)) #t))
               (bfs-loop (append rest new-nei))))])))))

(define/contract (is-escape-possible blocked source target)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?) boolean?)
  (let* ((n (length blocked))
         (bound (quotient (* n (- n 1)) 2))
         (blocked-set (make-hash)))
    (for ([cell blocked])
      (hash-set! blocked-set (cons (first cell) (second cell)) #t))
    (and (can-reach? source target blocked-set bound)
         (can-reach? target source blocked-set bound))))
```

## Erlang

```erlang
-export([is_escape_possible/3]).

-spec is_escape_possible(Blocked :: [[integer()]], Source :: [integer()], Target :: [integer()]) -> boolean().
is_escape_possible(Blocked, Source, Target) ->
    Len = length(Blocked),
    case Len of
        0 -> true;
        _ ->
            BlockSet = lists:foldl(fun([X,Y], Acc) -> maps:put({X,Y}, true, Acc) end, #{}, Blocked),
            MaxSteps = Len * (Len - 1) div 2,
            {SX,SY} = list_to_tuple(Source),
            {TX,TY} = list_to_tuple(Target),
            can_reach({SX,SY}, {TX,TY}, BlockSet, MaxSteps) andalso
            can_reach({TX,TY}, {SX,SY}, BlockSet, MaxSteps)
    end.

list_to_tuple([A,B]) -> {A,B}.

can_reach(Start, Goal, BlockSet, Limit) ->
    Queue0 = queue:new(),
    Queue1 = queue:in(Start, Queue0),
    Visited0 = maps:put(Start, true, #{}),
    bfs(Queue1, Visited0, Goal, BlockSet, Limit).

bfs(Queue, Visited, Goal, BlockSet, Limit) ->
    case queue:is_empty(Queue) of
        true -> false;
        false ->
            {{value, Pos}, Q1} = queue:out(Queue),
            if Pos =:= Goal -> true;
               map_size(Visited) > Limit -> true;
               true ->
                   {Q2, Vis2} = explore_neighbors(Pos, Q1, Visited, BlockSet),
                   bfs(Q2, Vis2, Goal, BlockSet, Limit)
            end
    end.

explore_neighbors({X,Y}, Queue, Visited, BlockSet) ->
    Directions = [{0,1},{1,0},{0,-1},{-1,0}],
    explore_dirs(Directions, {X,Y}, Queue, Visited, BlockSet).

explore_dirs([], _Pos, Q, V, _BlockSet) -> {Q,V};
explore_dirs([{DX,DY}|Rest], {X,Y}, Q, V, BlockSet) ->
    NX = X + DX,
    NY = Y + DY,
    if NX < 0 orelse NX >= 1000000 orelse NY < 0 orelse NY >= 1000000 ->
            explore_dirs(Rest, {X,Y}, Q, V, BlockSet);
       maps:is_key({NX,NY}, BlockSet) ->
            explore_dirs(Rest, {X,Y}, Q, V, BlockSet);
       maps:is_key({NX,NY}, V) ->
            explore_dirs(Rest, {X,Y}, Q, V, BlockSet);
       true ->
            V1 = maps:put({NX,NY}, true, V),
            Q1 = queue:in({NX,NY}, Q),
            explore_dirs(Rest, {X,Y}, Q1, V1, BlockSet)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_escape_possible(blocked :: [[integer]], source :: [integer], target :: [integer]) :: boolean
  def is_escape_possible(blocked, source, target) do
    b_len = length(blocked)

    if b_len == 0 do
      true
    else
      blocked_set =
        blocked
        |> Enum.map(fn [x, y] -> {x, y} end)
        |> MapSet.new()

      limit = div(b_len * (b_len - 1), 2)

      case bfs(source, target, blocked_set, limit) do
        false -> false
        true -> bfs(target, source, blocked_set, limit)
      end
    end
  end

  defp bfs(start_list, finish_list, blocked_set, limit) do
    start = List.to_tuple(start_list)
    finish = List.to_tuple(finish_list)

    max_coord = 1_000_000 - 1
    dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

    queue = :queue.new() |> :queue.in(start)
    visited = MapSet.new([start])

    bfs_loop(queue, visited, finish, blocked_set, limit, dirs, max_coord)
  end

  defp bfs_loop(queue, visited, finish, blocked_set, limit, dirs, max_coord) do
    case :queue.out(queue) do
      {:empty, _} ->
        false

      {{:value, {x, y} = pos}, q2} ->
        if pos == finish do
          true
        else
          if MapSet.size(visited) > limit do
            true
          else
            {new_queue, new_visited} =
              Enum.reduce(dirs, {q2, visited}, fn {dx, dy}, {qacc, vacc} ->
                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx > max_coord or ny > max_coord do
                  {qacc, vacc}
                else
                  npos = {nx, ny}

                  cond do
                    MapSet.member?(blocked_set, npos) -> {qacc, vacc}
                    MapSet.member?(vacc, npos) -> {qacc, vacc}
                    true -> {:queue.in(npos, qacc), MapSet.put(vacc, npos)}
                  end
                end
              end)

            bfs_loop(new_queue, new_visited, finish, blocked_set, limit, dirs, max_coord)
          end
        end
    end
  end
end
```
