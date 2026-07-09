# 0815. Bus Routes

## Cpp

```cpp
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;
        int n = routes.size();
        unordered_map<int, vector<int>> stop_to_routes;
        for (int i = 0; i < n; ++i) {
            for (int stop : routes[i]) {
                stop_to_routes[stop].push_back(i);
            }
        }
        if (!stop_to_routes.count(source) || !stop_to_routes.count(target)) return -1;
        
        vector<int> visited(n, 0);
        queue<pair<int,int>> q; // {route index, buses taken}
        for (int r : stop_to_routes[source]) {
            visited[r] = 1;
            q.emplace(r, 1);
        }
        
        while (!q.empty()) {
            auto [curRoute, buses] = q.front();
            q.pop();
            for (int stop : routes[curRoute]) {
                if (stop == target) return buses;
                for (int nextRoute : stop_to_routes[stop]) {
                    if (!visited[nextRoute]) {
                        visited[nextRoute] = 1;
                        q.emplace(nextRoute, buses + 1);
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
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;
        int n = routes.length;
        // Map each stop to the list of bus route indices that include it
        java.util.Map<Integer, java.util.List<Integer>> stopToRoutes = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int stop : routes[i]) {
                stopToRoutes.computeIfAbsent(stop, k -> new java.util.ArrayList<>()).add(i);
            }
        }
        // If either source or target is not present in any route, impossible
        if (!stopToRoutes.containsKey(source) || !stopToRoutes.containsKey(target)) return -1;

        int[] dist = new int[n];
        java.util.Arrays.fill(dist, -1);
        java.util.Queue<Integer> queue = new java.util.ArrayDeque<>();

        // Initialize BFS with all routes that contain the source stop
        for (int routeIdx : stopToRoutes.get(source)) {
            dist[routeIdx] = 1; // taking first bus
            queue.offer(routeIdx);
        }

        while (!queue.isEmpty()) {
            int curRoute = queue.poll();
            // Check if current route reaches target directly
            for (int stop : routes[curRoute]) {
                if (stop == target) {
                    return dist[curRoute];
                }
            }
            // Explore neighboring routes via stops on the current route
            for (int stop : routes[curRoute]) {
                java.util.List<Integer> neighborRoutes = stopToRoutes.get(stop);
                if (neighborRoutes == null) continue;
                for (int nextRoute : neighborRoutes) {
                    if (dist[nextRoute] == -1) {
                        dist[nextRoute] = dist[curRoute] + 1;
                        queue.offer(nextRoute);
                    }
                }
                // Clear to prevent future redundant processing
                neighborRoutes.clear();
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0

        from collections import defaultdict, deque

        stop_to_routes = defaultdict(list)
        for i, r in enumerate(routes):
            for s in r:
                stop_to_routes[s].append(i)

        if source not in stop_to_routes or target not in stop_to_routes:
            # If either start or end stop is never visited by any bus
            return -1

        visited_routes = set()
        q = deque()

        for r in stop_to_routes[source]:
            visited_routes.add(r)
            q.append(r)

        buses = 1
        while q:
            for _ in range(len(q)):
                cur_route = q.popleft()
                if target in routes[cur_route]:
                    return buses
                for stop in routes[cur_route]:
                    for nxt_route in stop_to_routes[stop]:
                        if nxt_route not in visited_routes:
                            visited_routes.add(nxt_route)
                            q.append(nxt_route)
            buses += 1

        return -1
```

## Python3

```python
class Solution:
    def numBusesToDestination(self, routes, source, target):
        from collections import defaultdict, deque
        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for i, r in enumerate(routes):
            for s in r:
                stop_to_routes[s].append(i)

        visited_routes = set()
        q = deque()
        # start with all routes that contain the source
        for route_idx in stop_to_routes.get(source, []):
            visited_routes.add(route_idx)
            q.append((route_idx, 1))  # (route index, buses taken)

        while q:
            cur_route, buses = q.popleft()
            if target in routes[cur_route]:
                return buses
            for stop in routes[cur_route]:
                for nxt_route in stop_to_routes[stop]:
                    if nxt_route not in visited_routes:
                        visited_routes.add(nxt_route)
                        q.append((nxt_route, buses + 1))
        return -1
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *data;
    int size;
    int cap;
} Vec;

static void vecPush(Vec *v, int val) {
    if (v->size == v->cap) {
        v->cap = v->cap ? v->cap * 2 : 4;
        v->data = realloc(v->data, v->cap * sizeof(int));
    }
    v->data[v->size++] = val;
}

int numBusesToDestination(int** routes, int routesSize, int* routesColSize, int source, int target) {
    if (source == target) return 0;

    const int MAX_STOP = 1000000;
    Vec *stopRoutes = calloc(MAX_STOP + 1, sizeof(Vec));

    for (int i = 0; i < routesSize; ++i) {
        int sz = routesColSize[i];
        for (int j = 0; j < sz; ++j) {
            int stop = routes[i][j];
            vecPush(&stopRoutes[stop], i);
        }
    }

    bool *visitedRoute = calloc(routesSize, sizeof(bool));
    int *queue = malloc(routesSize * sizeof(int));
    int qhead = 0, qtail = 0;

    Vec *srcVec = &stopRoutes[source];
    for (int i = 0; i < srcVec->size; ++i) {
        int r = srcVec->data[i];
        if (!visitedRoute[r]) {
            visitedRoute[r] = true;
            queue[qtail++] = r;
        }
    }

    int buses = 1;
    while (qhead < qtail) {
        int levelSize = qtail - qhead;
        for (int i = 0; i < levelSize; ++i) {
            int routeIdx = queue[qhead++];
            int *stops = routes[routeIdx];
            int sz = routesColSize[routeIdx];

            for (int p = 0; p < sz; ++p) {
                if (stops[p] == target) {
                    free(visitedRoute);
                    free(queue);
                    // Note: stopRoutes vectors are not freed as LeetCode does not require it.
                    return buses;
                }
            }

            for (int p = 0; p < sz; ++p) {
                int s = stops[p];
                Vec *vec = &stopRoutes[s];
                for (int k = 0; k < vec->size; ++k) {
                    int nxt = vec->data[k];
                    if (!visitedRoute[nxt]) {
                        visitedRoute[nxt] = true;
                        queue[qtail++] = nxt;
                    }
                }
            }
        }
        ++buses;
    }

    free(visitedRoute);
    free(queue);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int NumBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;

        // Map each stop to the list of bus route indices that include it
        var stopToRoutes = new Dictionary<int, List<int>>();
        for (int i = 0; i < routes.Length; i++) {
            foreach (int stop in routes[i]) {
                if (!stopToRoutes.TryGetValue(stop, out var list)) {
                    list = new List<int>();
                    stopToRoutes[stop] = list;
                }
                list.Add(i);
            }
        }

        // If either source or target is not present in any route, impossible
        if (!stopToRoutes.ContainsKey(source) || !stopToRoutes.ContainsKey(target))
            return -1;

        var visitedRoute = new bool[routes.Length];
        var queue = new Queue<int>();

        // Initialize BFS with all routes that can be boarded at the source stop
        foreach (int routeIdx in stopToRoutes[source]) {
            visitedRoute[routeIdx] = true;
            queue.Enqueue(routeIdx);
        }

        int busesTaken = 1; // we have taken one bus to board any of the initial routes

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                int curRoute = queue.Dequeue();
                foreach (int stop in routes[curRoute]) {
                    if (stop == target) return busesTaken;

                    // Explore neighboring routes via this stop
                    foreach (int nextRoute in stopToRoutes[stop]) {
                        if (!visitedRoute[nextRoute]) {
                            visitedRoute[nextRoute] = true;
                            queue.Enqueue(nextRoute);
                        }
                    }
                }
            }
            busesTaken++;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} routes
 * @param {number} source
 * @param {number} target
 * @return {number}
 */
var numBusesToDestination = function(routes, source, target) {
    if (source === target) return 0;
    
    const stopMap = new Map(); // stop -> list of route indices
    for (let i = 0; i < routes.length; ++i) {
        for (const stop of routes[i]) {
            if (!stopMap.has(stop)) stopMap.set(stop, []);
            stopMap.get(stop).push(i);
        }
    }
    
    if (!stopMap.has(source)) return -1;
    
    const visitedRoute = new Array(routes.length).fill(false);
    const queue = [];
    let qHead = 0;
    
    // initialize BFS with all routes that contain the source
    for (const r of stopMap.get(source)) {
        visitedRoute[r] = true;
        queue.push([r, 1]); // [route index, buses taken]
    }
    
    while (qHead < queue.length) {
        const [curRoute, busCount] = queue[qHead++];
        for (const stop of routes[curRoute]) {
            if (stop === target) return busCount;
            const nextRoutes = stopMap.get(stop);
            if (!nextRoutes) continue;
            for (const nr of nextRoutes) {
                if (!visitedRoute[nr]) {
                    visitedRoute[nr] = true;
                    queue.push([nr, busCount + 1]);
                }
            }
            // avoid revisiting this stop's routes again
            stopMap.set(stop, []);
        }
    }
    
    return -1;
};
```

## Typescript

```typescript
function numBusesToDestination(routes: number[][], source: number, target: number): number {
    if (source === target) return 0;

    const stopToRoutes = new Map<number, number[]>();
    for (let i = 0; i < routes.length; i++) {
        for (const stop of routes[i]) {
            let list = stopToRoutes.get(stop);
            if (!list) {
                list = [];
                stopToRoutes.set(stop, list);
            }
            list.push(i);
        }
    }

    const visitedRoute = new Array<boolean>(routes.length).fill(false);
    const queue: number[] = [];
    const busesTaken = new Map<number, number>();

    const startRoutes = stopToRoutes.get(source) || [];
    for (const r of startRoutes) {
        visitedRoute[r] = true;
        queue.push(r);
        busesTaken.set(r, 1);
    }

    let qIdx = 0;
    while (qIdx < queue.length) {
        const cur = queue[qIdx++];
        const curBuses = busesTaken.get(cur)!;

        // If current route reaches target, return answer
        for (const stop of routes[cur]) {
            if (stop === target) return curBuses;
        }

        // Explore neighboring routes via each stop on current route
        for (const stop of routes[cur]) {
            const neigh = stopToRoutes.get(stop);
            if (!neigh) continue;
            for (const nr of neigh) {
                if (!visitedRoute[nr]) {
                    visitedRoute[nr] = true;
                    queue.push(nr);
                    busesTaken.set(nr, curBuses + 1);
                }
            }
            // Prevent revisiting the same stop's routes later
            stopToRoutes.set(stop, []);
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $routes
     * @param Integer $source
     * @param Integer $target
     * @return Integer
     */
    function numBusesToDestination($routes, $source, $target) {
        if ($source === $target) {
            return 0;
        }

        $stopToRoutes = [];
        foreach ($routes as $i => $route) {
            foreach ($route as $stop) {
                $stopToRoutes[$stop][] = $i;
            }
        }

        if (!isset($stopToRoutes[$source])) {
            return -1;
        }

        $n = count($routes);
        $visitedRoute = array_fill(0, $n, false);
        $queue = new SplQueue();

        foreach ($stopToRoutes[$source] as $r) {
            $queue->enqueue($r);
            $visitedRoute[$r] = true;
        }

        $buses = 1;

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            for ($i = 0; $i < $levelSize; $i++) {
                $routeIdx = $queue->dequeue();
                foreach ($routes[$routeIdx] as $stop) {
                    if ($stop == $target) {
                        return $buses;
                    }
                    if (!isset($stopToRoutes[$stop])) {
                        continue;
                    }
                    foreach ($stopToRoutes[$stop] as $nextRoute) {
                        if (!$visitedRoute[$nextRoute]) {
                            $queue->enqueue($nextRoute);
                            $visitedRoute[$nextRoute] = true;
                        }
                    }
                }
            }
            $buses++;
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func numBusesToDestination(_ routes: [[Int]], _ source: Int, _ target: Int) -> Int {
        if source == target { return 0 }
        
        var stopToBuses = [Int: [Int]]()
        for (i, route) in routes.enumerated() {
            for stop in route {
                stopToBuses[stop, default: []].append(i)
            }
        }
        
        guard let startBuses = stopToBuses[source] else { return -1 }
        
        var visited = Set<Int>()
        var queue = [(bus: Int, depth: Int)]()
        for b in startBuses {
            visited.insert(b)
            queue.append((b, 1))
        }
        
        var idx = 0
        while idx < queue.count {
            let (busIdx, depth) = queue[idx]
            idx += 1
            
            for stop in routes[busIdx] {
                if stop == target { return depth }
                if let nextBuses = stopToBuses[stop] {
                    for nb in nextBuses where !visited.contains(nb) {
                        visited.insert(nb)
                        queue.append((nb, depth + 1))
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
    fun numBusesToDestination(routes: Array<IntArray>, source: Int, target: Int): Int {
        if (source == target) return 0
        val stopToRoutes = HashMap<Int, MutableList<Int>>()
        for (i in routes.indices) {
            for (stop in routes[i]) {
                stopToRoutes.computeIfAbsent(stop) { mutableListOf() }.add(i)
            }
        }
        val startRoutes = stopToRoutes[source] ?: return -1
        val visited = BooleanArray(routes.size)
        val dist = IntArray(routes.size)
        val q: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        for (r in startRoutes) {
            visited[r] = true
            dist[r] = 1
            q.add(r)
        }
        while (!q.isEmpty()) {
            val cur = q.removeFirst()
            // Check if current route reaches target
            for (stop in routes[cur]) {
                if (stop == target) return dist[cur]
            }
            // Expand to neighboring routes via stops
            for (stop in routes[cur]) {
                val nextRoutes = stopToRoutes[stop] ?: continue
                for (next in nextRoutes) {
                    if (!visited[next]) {
                        visited[next] = true
                        dist[next] = dist[cur] + 1
                        q.add(next)
                    }
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
  int numBusesToDestination(List<List<int>> routes, int source, int target) {
    if (source == target) return 0;

    final int n = routes.length;
    final Map<int, List<int>> stopToRoutes = {};

    for (int i = 0; i < n; i++) {
      for (final int stop in routes[i]) {
        stopToRoutes.putIfAbsent(stop, () => []).add(i);
      }
    }

    if (!stopToRoutes.containsKey(source) || !stopToRoutes.containsKey(target)) {
      return -1;
    }

    final List<bool> visitedRoute = List.filled(n, false);
    final Queue<int> queue = Queue<int>();

    for (final int idx in stopToRoutes[source]!) {
      queue.add(idx);
      visitedRoute[idx] = true;
    }

    int buses = 1;

    while (queue.isNotEmpty) {
      final int levelSize = queue.length;
      for (int i = 0; i < levelSize; i++) {
        final int curRoute = queue.removeFirst();
        for (final int stop in routes[curRoute]) {
          if (stop == target) return buses;

          final List<int>? nextRoutes = stopToRoutes[stop];
          if (nextRoutes != null) {
            for (final int nr in nextRoutes) {
              if (!visitedRoute[nr]) {
                visitedRoute[nr] = true;
                queue.add(nr);
              }
            }
          }
        }
      }
      buses++;
    }

    return -1;
  }
}
```

## Golang

```go
func numBusesToDestination(routes [][]int, source int, target int) int {
	if source == target {
		return 0
	}
	// map each stop to the list of routes that include it
	stopRoutes := make(map[int][]int)
	for i, r := range routes {
		for _, s := range r {
			stopRoutes[s] = append(stopRoutes[s], i)
		}
	}

	visitedRoute := make([]bool, len(routes))
	queue := []int{}

	// start from all routes that contain the source stop
	if starts, ok := stopRoutes[source]; ok {
		for _, idx := range starts {
			visitedRoute[idx] = true
			queue = append(queue, idx)
		}
	} else {
		return -1
	}

	buses := 1
	for len(queue) > 0 {
		nextQueue := []int{}
		for _, routeIdx := range queue {
			for _, stop := range routes[routeIdx] {
				if stop == target {
					return buses
				}
				for _, nb := range stopRoutes[stop] {
					if !visitedRoute[nb] {
						visitedRoute[nb] = true
						nextQueue = append(nextQueue, nb)
					}
				}
			}
		}
		queue = nextQueue
		buses++
	}
	return -1
}
```

## Ruby

```ruby
def num_buses_to_destination(routes, source, target)
  return 0 if source == target

  # Map each stop to the list of route indices that include it
  stop_to_routes = Hash.new { |h, k| h[k] = [] }
  routes.each_with_index do |stops, idx|
    stops.each { |s| stop_to_routes[s] << idx }
  end

  return -1 unless stop_to_routes.key?(source)

  visited_route = Array.new(routes.size, false)
  visited_stop = {}

  queue = []
  # Initialize BFS with all routes that contain the source stop
  stop_to_routes[source].each do |r|
    visited_route[r] = true
    queue << [r, 1]   # [route_index, buses_taken]
  end

  until queue.empty?
    r, buses = queue.shift
    return buses if routes[r].include?(target)

    routes[r].each do |stop|
      next if visited_stop[stop]

      stop_to_routes[stop].each do |nbr|
        unless visited_route[nbr]
          visited_route[nbr] = true
          queue << [nbr, buses + 1]
        end
      end

      visited_stop[stop] = true
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
  def numBusesToDestination(routes: Array[Array[Int]], source: Int, target: Int): Int = {
    if (source == target) return 0

    val stopToRoutes = scala.collection.mutable.HashMap[Int, scala.collection.mutable.ArrayBuffer[Int]]()
    for (i <- routes.indices) {
      for (stop <- routes(i)) {
        stopToRoutes.getOrElseUpdate(stop, scala.collection.mutable.ArrayBuffer()) += i
      }
    }

    if (!stopToRoutes.contains(source)) return -1

    import scala.collection.mutable.{Queue, Set}
    val visitedRoute = Set[Int]()
    val q = Queue[(Int, Int)]() // (route index, buses taken)

    for (r <- stopToRoutes(source)) {
      visitedRoute += r
      q.enqueue((r, 1))
    }

    while (q.nonEmpty) {
      val (curRoute, buses) = q.dequeue()
      if (routes(curRoute).contains(target)) return buses

      for (stop <- routes(curRoute)) {
        val neighborRoutes = stopToRoutes.getOrElse(stop, scala.collection.mutable.ArrayBuffer())
        for (nr <- neighborRoutes) {
          if (!visitedRoute.contains(nr)) {
            visitedRoute += nr
            q.enqueue((nr, buses + 1))
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
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        if source == target {
            return 0;
        }
        use std::collections::{HashMap, VecDeque};

        // Map each stop to the list of routes (by index) that include it
        let mut stop_to_routes: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, route) in routes.iter().enumerate() {
            for &stop in route {
                stop_to_routes.entry(stop).or_default().push(i);
            }
        }

        // If source stop is not on any bus, impossible
        let start_routes = match stop_to_routes.get(&source) {
            Some(v) => v.clone(),
            None => return -1,
        };

        let mut visited_route = vec![false; routes.len()];
        let mut queue: VecDeque<(usize, i32)> = VecDeque::new();

        // Initialize BFS with all routes that can be boarded at the source
        for &r in &start_routes {
            visited_route[r] = true;
            if routes[r].contains(&target) {
                return 1; // direct bus to target
            }
            queue.push_back((r, 1));
        }

        while let Some((route_idx, buses)) = queue.pop_front() {
            for &stop in &routes[route_idx] {
                if stop == target {
                    return buses;
                }
                if let Some(neighbor_routes) = stop_to_routes.get(&stop) {
                    for &nbr in neighbor_routes {
                        if !visited_route[nbr] {
                            visited_route[nbr] = true;
                            queue.push_back((nbr, buses + 1));
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
(define/contract (num-buses-to-destination routes source target)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length routes))
         ;; map stop -> list of route indices containing it
         (stop->routes (make-hash)))
    ;; build the mapping
    (for ([i (in-range n)])
      (for ([st (in-list (list-ref routes i))])
        (hash-update! stop->routes st (lambda (lst) (cons i lst)) '())))

    (if (= source target)
        0
        (let* ((start (hash-ref stop->routes source '()))
               (visited (make-vector n #f)))
          (if (null? start)
              -1
              (begin
                ;; mark starting routes visited
                (for ([r (in-list start)]) (vector-set! visited r #t))
                ;; BFS over routes
                (let bfs ((curr start) (buses 1))
                  (cond
                    [(null? curr) -1] ; queue empty, not reachable
                    [else
                     (define (process-route rid rest next)
                       (let ((stops (list-ref routes rid)))
                         (if (member target stops)
                             buses
                             (let loop-stops ((ss stops) (acc next))
                               (cond
                                 [(null? ss) (process-route (car rest) (cdr rest) acc)]
                                 [else
                                  (define stop (car ss))
                                  (define neigh (hash-ref stop->routes stop '()))
                                  ;; clear to avoid revisiting this stop later
                                  (hash-set! stop->routes stop '())
                                  (let ((new-neigh
                                         (foldl (lambda (nbr a)
                                                  (if (vector-ref visited nbr)
                                                      a
                                                      (begin
                                                        (vector-set! visited nbr #t)
                                                        (cons nbr a)))
                                                  )
                                                acc neigh)))
                                    (loop-stops (cdr ss) new-neigh))]))))
                     ;; start processing first route in curr list
                     (process-route (car curr) (cdr curr) '()))]
                    )))))))))
```

## Erlang

```erlang
-spec num_buses_to_destination(Routes :: [[integer()]], Source :: integer(), Target :: integer()) -> integer().
num_buses_to_destination(Routes, Source, Target) ->
    case Source =:= Target of
        true -> 0;
        false ->
            StopMap = build_stop_map(Routes),
            StartRoutes = maps:get(Source, StopMap, []),
            case StartRoutes of
                [] -> -1;
                _ ->
                    Visited0 = lists:foldl(fun(I, V) -> maps:put(I, true, V) end, #{}, StartRoutes),
                    Queue0 = lists:foldl(fun(I, Q) -> queue:in({I, 1}, Q) end, queue:new(), StartRoutes),
                    bfs(Queue0, Visited0, Routes, StopMap, Target)
            end
    end.

build_stop_map(Routes) ->
    build_stop_map(Routes, 0, #{}).

build_stop_map([], _Idx, Acc) -> Acc;
build_stop_map([Stops|Rest], Idx, Acc) ->
    NewAcc = lists:foldl(
        fun(S, M) ->
            maps:update_with(
                S,
                fun(L) -> [Idx | L] end,
                [Idx],
                M)
        end,
        Acc,
        Stops),
    build_stop_map(Rest, Idx + 1, NewAcc).

bfs(Queue, Visited, Routes, StopMap, Target) ->
    case queue:out(Queue) of
        {empty, _} -> -1;
        {{value, {Idx, BusCnt}}, QRest} ->
            RouteStops = lists:nth(Idx + 1, Routes),
            case lists:member(Target, RouteStops) of
                true -> BusCnt;
                false ->
                    {NewQueue, NewVisited} =
                        lists:foldl(
                            fun(Stop, {QAcc, VAcc}) ->
                                NeighborRoutes = maps:get(Stop, StopMap, []),
                                lists:foldl(
                                    fun(NIdx, {Q2, V2}) ->
                                        case maps:is_key(NIdx, V2) of
                                            true -> {Q2, V2};
                                            false ->
                                                {
                                                    queue:in({NIdx, BusCnt + 1}, Q2),
                                                    maps:put(NIdx, true, V2)
                                                }
                                        end
                                    end,
                                    {QAcc, VAcc},
                                    NeighborRoutes)
                            end,
                            {QRest, Visited},
                            RouteStops),
                    bfs(NewQueue, NewVisited, Routes, StopMap, Target)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_buses_to_destination(routes :: [[integer]], source :: integer, target :: integer) :: integer
  def num_buses_to_destination(routes, source, target) do
    if source == target do
      0
    else
      bfs(routes, source, target)
    end
  end

  defp bfs(routes, source, target) do
    stop_to_routes =
      Enum.reduce(Enum.with_index(routes), %{}, fn {stops, idx}, acc ->
        Enum.reduce(stops, acc, fn stop, a ->
          Map.update(a, stop, [idx], fn list -> [idx | list] end)
        end)
      end)

    start_routes = Map.get(stop_to_routes, source, [])

    if start_routes == [] do
      -1
    else
      # quick check: any starting route already reaches target?
      if Enum.any?(start_routes, fn r -> Enum.member?(Enum.at(routes, r), target) end) do
        1
      else
        visited = MapSet.new(start_routes)
        queue = :queue.from_list(Enum.map(start_routes, fn r -> {r, 1} end))
        bfs_loop(queue, visited, routes, stop_to_routes, target)
      end
    end
  end

  defp bfs_loop(queue, visited, routes, stop_to_routes, target) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {route_idx, buses}}, q_rest} ->
        route_stops = Enum.at(routes, route_idx)

        if Enum.member?(route_stops, target) do
          buses
        else
          {new_queue, new_visited} =
            Enum.reduce(route_stops, {q_rest, visited}, fn stop, {q_acc, vis_acc} ->
              next_routes = Map.get(stop_to_routes, stop, [])

              Enum.reduce(next_routes, {q_acc, vis_acc}, fn nr, {qq, vv} ->
                if MapSet.member?(vv, nr) do
                  {qq, vv}
                else
                  { :queue.in({nr, buses + 1}, qq), MapSet.put(vv, nr) }
                end
              end)
            end)

          bfs_loop(new_queue, new_visited, routes, stop_to_routes, target)
        end
    end
  end
end
```
