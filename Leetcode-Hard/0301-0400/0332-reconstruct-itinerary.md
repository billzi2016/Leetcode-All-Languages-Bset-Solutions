# 0332. Reconstruct Itinerary

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, multiset<string>> g;
        for (auto& t : tickets) {
            g[t[0]].insert(t[1]);
        }
        vector<string> path;
        function<void(const string&)> dfs = [&](const string& u) {
            auto& dests = g[u];
            while (!dests.empty()) {
                string v = *dests.begin();
                dests.erase(dests.begin());
                dfs(v);
            }
            path.push_back(u);
        };
        dfs("JFK");
        reverse(path.begin(), path.end());
        return path;
    }
};
```

## Java

```java
class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> graph = new HashMap<>();
        for (List<String> ticket : tickets) {
            String from = ticket.get(0);
            String to = ticket.get(1);
            graph.computeIfAbsent(from, k -> new PriorityQueue<>()).add(to);
        }
        LinkedList<String> itinerary = new LinkedList<>();
        dfs("JFK", graph, itinerary);
        return itinerary;
    }

    private void dfs(String airport, Map<String, PriorityQueue<String>> graph, LinkedList<String> itinerary) {
        PriorityQueue<String> dests = graph.get(airport);
        while (dests != null && !dests.isEmpty()) {
            String next = dests.poll();
            dfs(next, graph, itinerary);
        }
        itinerary.addFirst(airport);
    }
}
```

## Python

```python
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections
        import heapq

        graph = collections.defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def visit(airport):
            dests = graph[airport]
            while dests:
                next_airport = heapq.heappop(dests)
                visit(next_airport)
            route.append(airport)

        visit("JFK")
        return route[::-1]
```

## Python3

```python
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                next_dest = heapq.heappop(graph[stack[-1]])
                stack.append(next_dest)
            route.append(stack.pop())
        return route[::-1]
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *dest;
    int size;
    int cap;
} Adj;

static char **airportNames = NULL;   // global for comparator

/* Comparator for qsort of strings */
static int cmpStr(const void *a, const void *b) {
    const char *const *pa = (const char *const *)a;
    const char *const *pb = (const char *const *)b;
    return strcmp(*pa, *pb);
}

/* Comparator for qsort of destination ids in descending lexical order */
static int cmpDestDesc(const void *a, const void *b) {
    int id1 = *(const int *)a;
    int id2 = *(const int *)b;
    return strcmp(airportNames[id2], airportNames[id1]); // reverse order
}

/* Binary search to get id of an airport (airportNames is sorted ascending) */
static int getId(const char *s, int n) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        int cmp = strcmp(s, airportNames[mid]);
        if (cmp == 0) return mid;
        else if (cmp < 0) hi = mid - 1;
        else lo = mid + 1;
    }
    return -1; // should never happen
}

/* Add edge to adjacency list */
static void addEdge(Adj *adj, int v) {
    if (adj->size == adj->cap) {
        int newCap = adj->cap ? adj->cap * 2 : 4;
        adj->dest = realloc(adj->dest, newCap * sizeof(int));
        adj->cap = newCap;
    }
    adj->dest[adj->size++] = v;
}

/* DFS for Hierholzer's algorithm */
static void dfs(int u, Adj *graph, int *route, int *pos) {
    Adj *adj = &graph[u];
    while (adj->size > 0) {
        int v = adj->dest[--adj->size]; // pop smallest (stored at back)
        dfs(v, graph, route, pos);
    }
    route[(*pos)++] = u;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findItinerary(char*** tickets, int ticketsSize, int* ticketsColSize, int* returnSize) {
    /* 1. Collect all airport strings */
    int total = ticketsSize * 2;
    char **all = malloc(total * sizeof(char *));
    int idx = 0;
    for (int i = 0; i < ticketsSize; ++i) {
        all[idx++] = strdup(tickets[i][0]);
        all[idx++] = strdup(tickets[i][1]);
    }

    /* 2. Sort and deduplicate */
    qsort(all, total, sizeof(char *), cmpStr);
    char **uniq = malloc(total * sizeof(char *));
    int nNodes = 0;
    for (int i = 0; i < total; ++i) {
        if (i == 0 || strcmp(all[i], all[i - 1]) != 0) {
            uniq[nNodes++] = all[i];
        } else {
            free(all[i]); // duplicate
        }
    }
    free(all);
    airportNames = uniq; // set global for comparators

    /* 3. Build graph */
    Adj *graph = calloc(nNodes, sizeof(Adj));
    for (int i = 0; i < ticketsSize; ++i) {
        int from = getId(tickets[i][0], nNodes);
        int to   = getId(tickets[i][1], nNodes);
        addEdge(&graph[from], to);
    }

    /* 4. Sort each adjacency list in descending lexical order */
    for (int i = 0; i < nNodes; ++i) {
        if (graph[i].size > 0) {
            qsort(graph[i].dest, graph[i].size, sizeof(int), cmpDestDesc);
        }
    }

    /* 5. Hierholzer's algorithm */
    int start = getId("JFK", nNodes);
    int *route = malloc((ticketsSize + 1) * sizeof(int));
    int pos = 0;
    dfs(start, graph, route, &pos);

    /* 6. Prepare answer in correct order */
    char **answer = malloc(pos * sizeof(char *));
    for (int i = 0; i < pos; ++i) {
        int id = route[pos - 1 - i]; // reverse
        answer[i] = strdup(airportNames[id]);
    }
    *returnSize = pos;

    /* Cleanup */
    free(route);
    for (int i = 0; i < nNodes; ++i) {
        free(graph[i].dest);
    }
    free(graph);
    for (int i = 0; i < nNodes; ++i) {
        free(airportNames[i]);
    }
    free(airportNames);

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> FindItinerary(IList<IList<string>> tickets) {
        var graph = new Dictionary<string, List<string>>();
        foreach (var ticket in tickets) {
            string from = ticket[0];
            string to = ticket[1];
            if (!graph.ContainsKey(from)) graph[from] = new List<string>();
            graph[from].Add(to);
        }
        foreach (var kvp in graph) {
            kvp.Value.Sort((a, b) => b.CompareTo(a)); // descending for stack pop
        }

        var itinerary = new List<string>();

        void Visit(string airport) {
            while (graph.ContainsKey(airport) && graph[airport].Count > 0) {
                var destList = graph[airport];
                string next = destList[destList.Count - 1];
                destList.RemoveAt(destList.Count - 1);
                Visit(next);
            }
            itinerary.Add(airport);
        }

        Visit("JFK");
        itinerary.Reverse();
        return itinerary;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    const graph = {};
    for (const [from, to] of tickets) {
        if (!graph[from]) graph[from] = [];
        graph[from].push(to);
    }
    // Sort destinations in descending lexical order so we can pop the smallest
    for (const src in graph) {
        graph[src].sort((a, b) => b.localeCompare(a));
    }

    const itinerary = [];

    function dfs(airport) {
        const dests = graph[airport];
        while (dests && dests.length) {
            const next = dests.pop();
            dfs(next);
        }
        itinerary.push(airport);
    }

    dfs('JFK');
    return itinerary.reverse();
};
```

## Typescript

```typescript
function findItinerary(tickets: string[][]): string[] {
    const adj = new Map<string, string[]>();
    for (const [from, to] of tickets) {
        if (!adj.has(from)) adj.set(from, []);
        adj.get(from)!.push(to);
    }
    // sort each adjacency list in descending lexical order
    for (const dests of adj.values()) {
        dests.sort((a, b) => b.localeCompare(a));
    }

    const result: string[] = [];
    function dfs(node: string): void {
        const stack = adj.get(node);
        while (stack && stack.length > 0) {
            const next = stack.pop()!;
            dfs(next);
        }
        result.push(node);
    }

    dfs('JFK');
    return result.reverse();
}
```

## Php

```php
class Solution {
    private $graph = [];
    private $route = [];

    /**
     * @param String[][] $tickets
     * @return String[]
     */
    function findItinerary($tickets) {
        foreach ($tickets as $ticket) {
            [$from, $to] = $ticket;
            if (!isset($this->graph[$from])) {
                $this->graph[$from] = [];
            }
            $this->graph[$from][] = $to;
            // Ensure destination node exists in graph to avoid undefined index later
            if (!isset($this->graph[$to])) {
                $this->graph[$to] = [];
            }
        }

        foreach ($this->graph as &$destinations) {
            rsort($destinations);
        }
        unset($destinations);

        $this->visit('JFK');

        return array_reverse($this->route);
    }

    private function visit($airport) {
        while (!empty($this->graph[$airport])) {
            $next = array_pop($this->graph[$airport]);
            $this->visit($next);
        }
        $this->route[] = $airport;
    }
}
```

## Swift

```swift
class Solution {
    func findItinerary(_ tickets: [[String]]) -> [String] {
        var graph = [String: [String]]()
        for ticket in tickets {
            let from = ticket[0]
            let to = ticket[1]
            graph[from, default: []].append(to)
        }
        for key in graph.keys {
            graph[key]!.sort(by: >) // descending so we can pop smallest
        }
        
        var route = [String]()
        func dfs(_ airport: String) {
            while let dests = graph[airport], !dests.isEmpty {
                let next = graph[airport]!.removeLast()
                dfs(next)
            }
            route.append(airport)
        }
        
        dfs("JFK")
        return Array(route.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findItinerary(tickets: List<List<String>>): List<String> {
        val graph = HashMap<String, java.util.PriorityQueue<String>>()
        for (ticket in tickets) {
            val from = ticket[0]
            val to = ticket[1]
            graph.computeIfAbsent(from) { java.util.PriorityQueue() }.add(to)
        }
        val itinerary = mutableListOf<String>()
        fun dfs(airport: String) {
            val pq = graph[airport]
            while (pq != null && pq.isNotEmpty()) {
                dfs(pq.poll())
            }
            itinerary.add(airport)
        }
        dfs("JFK")
        return itinerary.reversed()
    }
}
```

## Dart

```dart
class Solution {
  List<String> findItinerary(List<List<String>> tickets) {
    final Map<String, List<String>> graph = {};
    for (var ticket in tickets) {
      graph.putIfAbsent(ticket[0], () => []).add(ticket[1]);
    }
    for (var entry in graph.entries) {
      entry.value.sort((a, b) => b.compareTo(a));
    }

    final List<String> itinerary = [];

    void dfs(String airport) {
      final dests = graph[airport];
      while (dests != null && dests.isNotEmpty) {
        final next = dests.removeLast();
        dfs(next);
      }
      itinerary.add(airport);
    }

    dfs('JFK');
    return itinerary.reversed.toList();
  }
}
```

## Golang

```go
import "sort"

func findItinerary(tickets [][]string) []string {
	adj := make(map[string][]string)
	for _, t := range tickets {
		from, to := t[0], t[1]
		adj[from] = append(adj[from], to)
	}
	for from := range adj {
		dests := adj[from]
		sort.Slice(dests, func(i, j int) bool { return dests[i] > dests[j] })
		adj[from] = dests
	}

	var route []string
	var dfs func(string)
	dfs = func(node string) {
		for len(adj[node]) > 0 {
			next := adj[node][len(adj[node])-1]
			adj[node] = adj[node][:len(adj[node])-1]
			dfs(next)
		}
		route = append(route, node)
	}

	dfs("JFK")
	for i, j := 0, len(route)-1; i < j; i, j = i+1, j-1 {
		route[i], route[j] = route[j], route[i]
	}
	return route
}
```

## Ruby

```ruby
def find_itinerary(tickets)
  graph = Hash.new { |h, k| h[k] = [] }
  tickets.each { |from, to| graph[from] << to }

  graph.each_value { |arr| arr.sort!.reverse! }

  route = []
  dfs = lambda do |airport|
    while !graph[airport].empty?
      next_airport = graph[airport].pop
      dfs.call(next_airport)
    end
    route << airport
  end

  dfs.call('JFK')
  route.reverse
end
```

## Scala

```scala
object Solution {
  import java.util.PriorityQueue
  def findItinerary(tickets: List[List[String]]): List[String] = {
    val graph = scala.collection.mutable.Map[String, PriorityQueue[String]]()
    for (ticket <- tickets) {
      val from = ticket(0)
      val to   = ticket(1)
      val pq = graph.getOrElseUpdate(from, new PriorityQueue[String]())
      pq.add(to)
    }
    val itinerary = scala.collection.mutable.ListBuffer[String]()
    def dfs(node: String): Unit = {
      var pq = graph.getOrElse(node, null)
      while (pq != null && !pq.isEmpty) {
        val next = pq.poll()
        dfs(next)
      }
      itinerary += node
    }
    dfs("JFK")
    itinerary.reverse.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        use std::collections::HashMap;
        let mut graph: HashMap<String, Vec<String>> = HashMap::new();
        for ticket in tickets {
            let from = ticket[0].clone();
            let to = ticket[1].clone();
            graph.entry(from).or_default().push(to);
        }
        for dests in graph.values_mut() {
            dests.sort_by(|a, b| b.cmp(a));
        }

        let mut route: Vec<String> = Vec::new();
        Self::dfs("JFK".to_string(), &mut graph, &mut route);
        route.reverse();
        route
    }

    fn dfs(
        curr: String,
        graph: &mut std::collections::HashMap<String, Vec<String>>,
        route: &mut Vec<String>,
    ) {
        while let Some(next) = {
            if let Some(v) = graph.get_mut(&curr) {
                v.pop()
            } else {
                None
            }
        } {
            Self::dfs(next, graph, route);
        }
        route.push(curr);
    }
}
```

## Racket

```racket
(define/contract (find-itinerary tickets)
  (-> (listof (listof string?)) (listof string?))
  (let* ((adj (make-hash)))
    ;; build adjacency lists
    (for ([t tickets])
      (define from (first t))
      (define to   (second t))
      (hash-update! adj from (lambda (lst) (cons to lst)) '()))
    ;; sort each list in descending lexical order so we can pop from the front
    (for ([k (in-hash-keys adj)])
      (define sorted (sort (hash-ref adj k) string>?))
      (hash-set! adj k sorted))
    (define result '())
    (define (visit node)
      (let loop ()
        (define dests (hash-ref adj node '()))
        (when (pair? dests)
          (define next (car dests))
          (hash-set! adj node (cdr dests))
          (visit next)
          (loop)))
      (set! result (cons node result)))
    (visit "JFK")
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([find_itinerary/1]).

-spec find_itinerary(Tickets :: [[unicode:unicode_binary()]]) -> [unicode:unicode_binary()].
find_itinerary(Tickets) ->
    Adj = build_adj(Tickets),
    PathRev = hierholzer(["JFK"], Adj, []),
    lists:reverse(PathRev).

build_adj(Tickets) ->
    Adj0 = lists:foldl(fun([From, To], Acc) ->
                DestList = maps:get(From, Acc, []),
                maps:put(From, [To | DestList], Acc)
            end, #{}, Tickets),
    maps:map(fun(_K, L) -> lists:sort(L) end, Adj0).

hierholzer(Stack, Adj, Path) ->
    case Stack of
        [] -> Path;
        [V|Rest] ->
            DestList = maps:get(V, Adj, []),
            case DestList of
                [] ->
                    hierholzer(Rest, Adj, [V | Path]);
                [Next|Remaining] ->
                    NewAdj = maps:put(V, Remaining, Adj),
                    hierholzer([Next, V | Rest], NewAdj, Path)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_itinerary(tickets :: [[String.t]]) :: [String.t]
  def find_itinerary(tickets) do
    graph = build_graph(tickets)
    dfs(["JFK"], graph, [])
  end

  defp build_graph(tickets) do
    tickets
    |> Enum.reduce(%{}, fn [from, to], acc ->
      Map.update(acc, from, [to], &[to | &1])
    end)
    |> Enum.map(fn {k, v} -> {k, Enum.sort(v)} end)
    |> Enum.into(%{})
  end

  defp dfs([], _graph, route), do: Enum.reverse(route)

  defp dfs([node | rest] = stack, graph, route) do
    case Map.get(graph, node, []) do
      [] ->
        # no outgoing edges, add to itinerary
        dfs(rest, graph, [node | route])

      [next | remaining] ->
        # take the smallest lexical destination
        new_graph = Map.put(graph, node, remaining)
        dfs([next | stack], new_graph, route)
    end
  end
end
```
