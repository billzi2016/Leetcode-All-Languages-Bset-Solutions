# 2092. Find All People With Secret

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class DSU {
public:
    vector<int> parent, rnk;
    DSU(int n = 0) { init(n); }
    void init(int n) {
        parent.resize(n);
        rnk.assign(n, 0);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return;
        if (rnk[a] < rnk[b]) swap(a, b);
        parent[b] = a;
        if (rnk[a] == rnk[b]) ++rnk[a];
    }
};

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        sort(meetings.begin(), meetings.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[2] < b[2]; });
        
        DSU dsu(n);
        vector<char> knows(n, 0);
        knows[0] = knows[firstPerson] = 1;
        dsu.unite(0, firstPerson);
        
        int m = meetings.size();
        int i = 0;
        while (i < m) {
            int curTime = meetings[i][2];
            unordered_set<int> people;
            // union all meetings at this time
            int j = i;
            while (j < m && meetings[j][2] == curTime) {
                int x = meetings[j][0], y = meetings[j][1];
                dsu.unite(x, y);
                people.insert(x);
                people.insert(y);
                ++j;
            }
            // determine who knows the secret after this time
            vector<int> toReset;
            for (int p : people) {
                if (dsu.find(p) == dsu.find(0)) {
                    knows[p] = 1;
                } else {
                    toReset.push_back(p);
                }
            }
            // reset connections of those who still don't know the secret
            for (int p : toReset) {
                dsu.parent[p] = p;
                dsu.rnk[p] = 0;
            }
            i = j;
        }
        
        vector<int> ans;
        for (int i = 0; i < n; ++i)
            if (knows[i]) ans.push_back(i);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        boolean[] knows = new boolean[n];
        knows[0] = true;
        knows[firstPerson] = true;

        Arrays.sort(meetings, (a, b) -> Integer.compare(a[2], b[2]));

        int i = 0;
        while (i < meetings.length) {
            int curTime = meetings[i][2];
            Map<Integer, List<Integer>> adj = new HashMap<>();
            Set<Integer> participants = new HashSet<>();

            int j = i;
            while (j < meetings.length && meetings[j][2] == curTime) {
                int x = meetings[j][0];
                int y = meetings[j][1];
                adj.computeIfAbsent(x, k -> new ArrayList<>()).add(y);
                adj.computeIfAbsent(y, k -> new ArrayList<>()).add(x);
                participants.add(x);
                participants.add(y);
                j++;
            }

            Queue<Integer> queue = new ArrayDeque<>();
            Set<Integer> visited = new HashSet<>();

            for (int p : participants) {
                if (knows[p]) {
                    queue.offer(p);
                    visited.add(p);
                }
            }

            while (!queue.isEmpty()) {
                int cur = queue.poll();
                for (int nb : adj.getOrDefault(cur, Collections.emptyList())) {
                    if (!visited.contains(nb)) {
                        visited.add(nb);
                        queue.offer(nb);
                    }
                }
            }

            for (int p : visited) {
                knows[p] = true;
            }

            i = j;
        }

        List<Integer> result = new ArrayList<>();
        for (int idx = 0; idx < n; idx++) {
            if (knows[idx]) {
                result.add(idx);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        from collections import defaultdict, deque

        knows = [False] * n
        knows[0] = True
        knows[firstPerson] = True

        meetings.sort(key=lambda x: x[2])
        i, m = 0, len(meetings)

        while i < m:
            t = meetings[i][2]
            adj = defaultdict(list)
            participants = set()
            j = i
            # gather all meetings at the same time
            while j < m and meetings[j][2] == t:
                x, y, _ = meetings[j]
                adj[x].append(y)
                adj[y].append(x)
                participants.add(x)
                participants.add(y)
                j += 1

            # start BFS from people who already know the secret at this time
            q = deque([p for p in participants if knows[p]])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not knows[v]:
                        knows[v] = True
                        q.append(v)

            i = j

        return [idx for idx, val in enumerate(knows) if val]
```

## Python3

```python
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        class UnionFind:
            __slots__ = ("parent", "rank")
            def __init__(self, size: int):
                self.parent = list(range(size))
                self.rank = [0] * size
            def find(self, x: int) -> int:
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def unite(self, x: int, y: int) -> None:
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return
                if self.rank[rx] < self.rank[ry]:
                    self.parent[rx] = ry
                elif self.rank[rx] > self.rank[ry]:
                    self.parent[ry] = rx
                else:
                    self.parent[ry] = rx
                    self.rank[rx] += 1
            def reset(self, x: int) -> None:
                self.parent[x] = x
                self.rank[x] = 0

        meetings.sort(key=lambda m: m[2])
        uf = UnionFind(n)
        uf.unite(0, firstPerson)

        i = 0
        m = len(meetings)
        while i < m:
            t = meetings[i][2]
            participants = set()
            j = i
            # union all meetings at this time
            while j < m and meetings[j][2] == t:
                x, y, _ = meetings[j]
                uf.unite(x, y)
                participants.add(x)
                participants.add(y)
                j += 1

            # determine which participants are connected to person 0
            known = set()
            root0 = uf.find(0)
            for p in participants:
                if uf.find(p) == root0:
                    known.add(p)

            # reset those not known
            for p in participants:
                if p not in known:
                    uf.reset(p)

            i = j

        res = [i for i in range(n) if uf.find(i) == uf.find(0)]
        return res
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int x;
    int y;
    int t;
} Meeting;

static int cmpMeeting(const void *a, const void *b) {
    const Meeting *m1 = (const Meeting *)a;
    const Meeting *m2 = (const Meeting *)b;
    return m1->t - m2->t;
}

/* Union-Find structure */
static int *parentArr;
static int *rankArr;

static int findSet(int x) {
    if (parentArr[x] != x)
        parentArr[x] = findSet(parentArr[x]);
    return parentArr[x];
}

static void uniteSet(int a, int b) {
    int ra = findSet(a);
    int rb = findSet(b);
    if (ra == rb) return;
    if (rankArr[ra] < rankArr[rb]) {
        parentArr[ra] = rb;
    } else if (rankArr[ra] > rankArr[rb]) {
        parentArr[rb] = ra;
    } else {
        parentArr[rb] = ra;
        rankArr[ra]++;
    }
}

static void resetSet(int x) {
    parentArr[x] = x;
    rankArr[x] = 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findAllPeople(int n, int** meetings, int meetingsSize, int* meetingsColSize,
                   int firstPerson, int* returnSize) {
    Meeting *arr = (Meeting *)malloc(sizeof(Meeting) * meetingsSize);
    for (int i = 0; i < meetingsSize; ++i) {
        arr[i].x = meetings[i][0];
        arr[i].y = meetings[i][1];
        arr[i].t = meetings[i][2];
    }
    qsort(arr, meetingsSize, sizeof(Meeting), cmpMeeting);

    parentArr = (int *)malloc(sizeof(int) * n);
    rankArr   = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) {
        parentArr[i] = i;
        rankArr[i] = 0;
    }

    bool *knows = (bool *)calloc(n, sizeof(bool));
    knows[0] = true;
    knows[firstPerson] = true;
    uniteSet(0, firstPerson);

    int *rootMark = (int *)calloc(n, sizeof(int));   // timestamp marks
    int stamp = 1;

    int i = 0;
    while (i < meetingsSize) {
        int curTime = arr[i].t;
        int j = i;
        while (j < meetingsSize && arr[j].t == curTime) ++j; // [i, j)

        int groupCnt = j - i;
        int *participants = (int *)malloc(sizeof(int) * groupCnt * 2);
        int pcnt = 0;

        /* unite all pairs of this time */
        for (int k = i; k < j; ++k) {
            uniteSet(arr[k].x, arr[k].y);
            participants[pcnt++] = arr[k].x;
            participants[pcnt++] = arr[k].y;
        }

        int curStamp = stamp++;

        /* mark roots that already know the secret */
        for (int idx = 0; idx < pcnt; ++idx) {
            int p = participants[idx];
            if (knows[p]) {
                int r = findSet(p);
                rootMark[r] = curStamp;
            }
        }

        /* propagate knowledge within components that have the secret */
        for (int idx = 0; idx < pcnt; ++idx) {
            int p = participants[idx];
            int r = findSet(p);
            if (rootMark[r] == curStamp)
                knows[p] = true;
        }

        /* reset components that do NOT have the secret */
        for (int idx = 0; idx < pcnt; ++idx) {
            int p = participants[idx];
            int r = findSet(p);
            if (rootMark[r] != curStamp) {
                resetSet(p);
            }
        }

        free(participants);
        i = j;
    }

    /* collect result */
    int *res = (int *)malloc(sizeof(int) * n);
    int cnt = 0;
    for (int v = 0; v < n; ++v) {
        if (knows[v]) res[cnt++] = v;
    }
    *returnSize = cnt;

    free(arr);
    free(parentArr);
    free(rankArr);
    free(knows);
    free(rootMark);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindAllPeople(int n, int[][] meetings, int firstPerson) {
        bool[] knows = new bool[n];
        knows[0] = true;
        knows[firstPerson] = true;

        Array.Sort(meetings, (a, b) => a[2].CompareTo(b[2]));

        int i = 0;
        while (i < meetings.Length) {
            int curTime = meetings[i][2];
            // collect all meetings with the same time
            var group = new List<int[]>();
            while (i < meetings.Length && meetings[i][2] == curTime) {
                group.Add(meetings[i]);
                i++;
            }

            var adj = new Dictionary<int, List<int>>();
            var participants = new HashSet<int>();

            foreach (var m in group) {
                int x = m[0], y = m[1];
                if (!adj.ContainsKey(x)) adj[x] = new List<int>();
                if (!adj.ContainsKey(y)) adj[y] = new List<int>();
                adj[x].Add(y);
                adj[y].Add(x);
                participants.Add(x);
                participants.Add(y);
            }

            var queue = new Queue<int>();
            var visited = new HashSet<int>();

            foreach (int p in participants) {
                if (knows[p]) {
                    queue.Enqueue(p);
                    visited.Add(p);
                }
            }

            while (queue.Count > 0) {
                int cur = queue.Dequeue();
                if (!adj.ContainsKey(cur)) continue;
                foreach (int nb in adj[cur]) {
                    if (!knows[nb]) knows[nb] = true;
                    if (!visited.Contains(nb)) {
                        visited.Add(nb);
                        queue.Enqueue(nb);
                    }
                }
            }
        }

        var result = new List<int>();
        for (int idx = 0; idx < n; idx++) {
            if (knows[idx]) result.Add(idx);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
var findAllPeople = function(n, meetings, firstPerson) {
    const knows = new Array(n).fill(false);
    knows[0] = true;
    knows[firstPerson] = true;

    // sort meetings by time
    meetings.sort((a, b) => a[2] - b[2]);

    let i = 0;
    while (i < meetings.length) {
        const curTime = meetings[i][2];
        const adj = new Map();          // person -> list of neighbors at this time
        const participants = new Set(); // all people involved in meetings at curTime

        // gather all meetings with the same timestamp
        let j = i;
        while (j < meetings.length && meetings[j][2] === curTime) {
            const [x, y] = meetings[j];
            if (!adj.has(x)) adj.set(x, []);
            if (!adj.has(y)) adj.set(y, []);
            adj.get(x).push(y);
            adj.get(y).push(x);
            participants.add(x);
            participants.add(y);
            j++;
        }

        // BFS/DFS propagation within this time slice
        const queue = [];
        for (const p of participants) {
            if (knows[p]) queue.push(p);
        }
        let head = 0;
        while (head < queue.length) {
            const cur = queue[head++];
            const neigh = adj.get(cur) || [];
            for (const nb of neigh) {
                if (!knows[nb]) {
                    knows[nb] = true;
                    queue.push(nb);
                }
            }
        }

        i = j; // move to next time group
    }

    const result = [];
    for (let idx = 0; idx < n; idx++) {
        if (knows[idx]) result.push(idx);
    }
    return result;
};
```

## Typescript

```typescript
function findAllPeople(n: number, meetings: number[][], firstPerson: number): number[] {
    const knows = new Array<boolean>(n).fill(false);
    knows[0] = true;
    knows[firstPerson] = true;

    meetings.sort((a, b) => a[2] - b[2]);

    let i = 0;
    while (i < meetings.length) {
        const time = meetings[i][2];
        const adj = new Map<number, number[]>();
        const participants = new Set<number>();

        // gather all meetings at the same timestamp
        while (i < meetings.length && meetings[i][2] === time) {
            const [x, y] = meetings[i];
            if (!adj.has(x)) adj.set(x, []);
            if (!adj.has(y)) adj.set(y, []);
            adj.get(x)!.push(y);
            adj.get(y)!.push(x);
            participants.add(x);
            participants.add(y);
            i++;
        }

        // start BFS from people who already know the secret at this time
        const queue: number[] = [];
        for (const p of participants) {
            if (knows[p]) queue.push(p);
        }
        let qIdx = 0;
        while (qIdx < queue.length) {
            const person = queue[qIdx++];
            const neigh = adj.get(person);
            if (!neigh) continue;
            for (const nb of neigh) {
                if (!knows[nb]) {
                    knows[nb] = true;
                    queue.push(nb);
                }
            }
        }
    }

    const result: number[] = [];
    for (let idx = 0; idx < n; idx++) {
        if (knows[idx]) result.push(idx);
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $meetings
     * @param Integer $firstPerson
     * @return Integer[]
     */
    function findAllPeople($n, $meetings, $firstPerson) {
        // sort meetings by time
        usort($meetings, function($a, $b) {
            return $a[2] <=> $b[2];
        });
        
        $knows = array_fill(0, $n, false);
        $knows[0] = true;
        $knows[$firstPerson] = true;
        
        $m = count($meetings);
        $i = 0;
        while ($i < $m) {
            $time = $meetings[$i][2];
            $j = $i;
            // find range with same time
            while ($j < $m && $meetings[$j][2] == $time) {
                $j++;
            }
            
            // build adjacency for this timestamp
            $adj = [];
            $participants = [];
            for ($k = $i; $k < $j; $k++) {
                [$x, $y, $t] = $meetings[$k];
                if (!isset($adj[$x])) $adj[$x] = [];
                if (!isset($adj[$y])) $adj[$y] = [];
                $adj[$x][] = $y;
                $adj[$y][] = $x;
                $participants[$x] = true;
                $participants[$y] = true;
            }
            
            // BFS starting from already known participants
            $queue = new SplQueue();
            foreach ($participants as $person => $_) {
                if ($knows[$person]) {
                    $queue->enqueue($person);
                }
            }
            $visitedInTime = [];
            while (!$queue->isEmpty()) {
                $p = $queue->dequeue();
                if (isset($visitedInTime[$p])) continue;
                $visitedInTime[$p] = true;
                if (!isset($adj[$p])) continue;
                foreach ($adj[$p] as $nbr) {
                    if (!$knows[$nbr]) {
                        $knows[$nbr] = true;
                        $queue->enqueue($nbr);
                    }
                }
            }
            
            $i = $j; // move to next time group
        }
        
        $result = [];
        for ($idx = 0; $idx < $n; $idx++) {
            if ($knows[$idx]) $result[] = $idx;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findAllPeople(_ n: Int, _ meetings: [[Int]], _ firstPerson: Int) -> [Int] {
        var sortedMeetings = meetings.sorted { $0[2] < $1[2] }
        var knowsSecret = Array(repeating: false, count: n)
        knowsSecret[0] = true
        knowsSecret[firstPerson] = true
        
        var i = 0
        while i < sortedMeetings.count {
            let currentTime = sortedMeetings[i][2]
            var adjacency = [Int: [Int]]()
            var participants = Set<Int>()
            var j = i
            while j < sortedMeetings.count && sortedMeetings[j][2] == currentTime {
                let x = sortedMeetings[j][0]
                let y = sortedMeetings[j][1]
                adjacency[x, default: []].append(y)
                adjacency[y, default: []].append(x)
                participants.insert(x)
                participants.insert(y)
                j += 1
            }
            
            var queue = [Int]()
            var head = 0
            var visited = Set<Int>()
            for p in participants where knowsSecret[p] {
                queue.append(p)
                visited.insert(p)
            }
            
            while head < queue.count {
                let person = queue[head]
                head += 1
                if let neighbors = adjacency[person] {
                    for nb in neighbors {
                        if !knowsSecret[nb] {
                            knowsSecret[nb] = true
                        }
                        if !visited.contains(nb) {
                            visited.insert(nb)
                            queue.append(nb)
                        }
                    }
                }
            }
            
            i = j
        }
        
        var result = [Int]()
        for idx in 0..<n where knowsSecret[idx] {
            result.append(idx)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findAllPeople(n: Int, meetings: Array<IntArray>, firstPerson: Int): List<Int> {
        val sorted = meetings.sortedWith(compareBy<IntArray> { it[2] })
        val know = BooleanArray(n)
        know[0] = true
        know[firstPerson] = true

        var idx = 0
        while (idx < sorted.size) {
            val curTime = sorted[idx][2]
            val adj = HashMap<Int, MutableList<Int>>()
            val participants = HashSet<Int>()
            var j = idx
            while (j < sorted.size && sorted[j][2] == curTime) {
                val x = sorted[j][0]
                val y = sorted[j][1]
                adj.computeIfAbsent(x) { ArrayList() }.add(y)
                adj.computeIfAbsent(y) { ArrayList() }.add(x)
                participants.add(x)
                participants.add(y)
                j++
            }

            val queue: ArrayDeque<Int> = ArrayDeque()
            for (p in participants) {
                if (know[p]) {
                    queue.add(p)
                }
            }

            while (!queue.isEmpty()) {
                val person = queue.removeFirst()
                val neighbors = adj[person] ?: continue
                for (nbr in neighbors) {
                    if (!know[nbr]) {
                        know[nbr] = true
                        queue.add(nbr)
                    }
                }
            }

            idx = j
        }

        val result = ArrayList<Int>()
        for (i in 0 until n) {
            if (know[i]) result.add(i)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findAllPeople(int n, List<List<int>> meetings, int firstPerson) {
    // Union-Find data structures
    List<int> parent = List.generate(n, (i) => i);
    List<int> rank = List.filled(n, 0);

    int find(int x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    void unionSet(int a, int b) {
      int pa = find(a);
      int pb = find(b);
      if (pa == pb) return;
      if (rank[pa] < rank[pb]) {
        parent[pa] = pb;
      } else if (rank[pa] > rank[pb]) {
        parent[pb] = pa;
      } else {
        parent[pb] = pa;
        rank[pa]++;
      }
    }

    // Initially person 0 knows the secret and shares with firstPerson at time 0
    unionSet(0, firstPerson);

    // Sort meetings by time
    meetings.sort((a, b) => a[2].compareTo(b[2]));

    int i = 0;
    while (i < meetings.length) {
      int curTime = meetings[i][2];
      Set<int> participants = {};

      // Union all meetings happening at the same time
      int j = i;
      while (j < meetings.length && meetings[j][2] == curTime) {
        int x = meetings[j][0];
        int y = meetings[j][1];
        unionSet(x, y);
        participants.add(x);
        participants.add(y);
        j++;
      }

      // Reset those not connected to person 0
      for (int p in participants) {
        if (find(p) != find(0)) {
          parent[p] = p;
          rank[p] = 0;
        }
      }

      i = j;
    }

    List<int> result = [];
    int rootZero = find(0);
    for (int person = 0; person < n; person++) {
      if (find(person) == rootZero) {
        result.add(person);
      }
    }
    return result;
  }
}
```

## Golang

```go
package main

import "sort"

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	sort.Slice(meetings, func(i, j int) bool { return meetings[i][2] < meetings[j][2] })
	knows := make([]bool, n)
	knows[0] = true
	knows[firstPerson] = true

	for i := 0; i < len(meetings); {
		t := meetings[i][2]
		j := i
		for j < len(meetings) && meetings[j][2] == t {
			j++
		}

		adj := make(map[int][]int)
		participants := make([]int, 0)
		seen := make(map[int]bool)

		for k := i; k < j; k++ {
			x, y := meetings[k][0], meetings[k][1]
			adj[x] = append(adj[x], y)
			adj[y] = append(adj[y], x)
			if !seen[x] {
				seen[x] = true
				participants = append(participants, x)
			}
			if !seen[y] {
				seen[y] = true
				participants = append(participants, y)
			}
		}

		queue := make([]int, 0)
		visited := make(map[int]bool)

		for _, p := range participants {
			if knows[p] && !visited[p] {
				queue = append(queue, p)
				visited[p] = true
			}
		}

		for len(queue) > 0 {
			cur := queue[0]
			queue = queue[1:]
			for _, nb := range adj[cur] {
				if !knows[nb] {
					knows[nb] = true
				}
				if !visited[nb] {
					visited[nb] = true
					queue = append(queue, nb)
				}
			}
		}

		i = j
	}

	res := make([]int, 0)
	for idx, v := range knows {
		if v {
			res = append(res, idx)
		}
	}
	return res
}
```

## Ruby

```ruby
def find_all_people(n, meetings, first_person)
  # Sort meetings by time
  meetings.sort_by! { |m| m[2] }

  # Group meetings that happen at the same time
  time_groups = {}
  meetings.each do |x, y, t|
    (time_groups[t] ||= []) << [x, y]
  end

  knows = Array.new(n, false)
  knows[0] = true
  knows[first_person] = true

  # Process each timestamp in increasing order
  time_groups.each_value do |pairs|
    # Build adjacency list for this timestamp only
    adj = Hash.new { |h, k| h[k] = [] }
    pairs.each do |x, y|
      adj[x] << y
      adj[y] << x
    end

    # Initialize BFS queue with people who already know the secret at this time
    queue = []
    visited_start = {}
    pairs.each do |x, y|
      if knows[x] && !visited_start[x]
        queue << x
        visited_start[x] = true
      end
      if knows[y] && !visited_start[y]
        queue << y
        visited_start[y] = true
      end
    end

    # Propagate the secret within this time's connected components
    until queue.empty?
      cur = queue.shift
      adj[cur].each do |nbr|
        next if knows[nbr]

        knows[nbr] = true
        queue << nbr
      end
    end
  end

  result = []
  (0...n).each { |i| result << i if knows[i] }
  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, HashMap, HashSet}
  def findAllPeople(n: Int, meetings: Array[Array[Int]], firstPerson: Int): List[Int] = {
    val knows = Array.fill[Boolean](n)(false)
    knows(0) = true
    knows(firstPerson) = true

    // sort meetings by time
    val sorted = meetings.sortBy(_(2))

    // visited marker for each round to avoid resetting a boolean array
    val visitedRound = Array.fill[Int](n)(-1)
    var currentRound = 0

    var i = 0
    while (i < sorted.length) {
      val time = sorted(i)(2)

      // build adjacency list for this time slice
      val adj = new HashMap[Int, ArrayBuffer[Int]]()
      val participants = new HashSet[Int]()

      var j = i
      while (j < sorted.length && sorted(j)(2) == time) {
        val x = sorted(j)(0)
        val y = sorted(j)(1)

        adj.getOrElseUpdate(x, new ArrayBuffer[Int]()) += y
        adj.getOrElseUpdate(y, new ArrayBuffer[Int]()) += x

        participants += x
        participants += y

        j += 1
      }

      // BFS/DFS within this time slice starting from already known people
      currentRound += 1
      val queue = new java.util.ArrayDeque[Int]()

      for (p <- participants) {
        if (knows(p)) {
          queue.add(p)
          visitedRound(p) = currentRound
        }
      }

      while (!queue.isEmpty) {
        val cur = queue.poll()
        adj.get(cur).foreach { neighList =>
          for (nbr <- neighList) {
            if (!knows(nbr)) knows(nbr) = true
            if (visitedRound(nbr) != currentRound) {
              visitedRound(nbr) = currentRound
              queue.add(nbr)
            }
          }
        }
      }

      i = j
    }

    val result = new ArrayBuffer[Int]()
    for (idx <- 0 until n) if (knows(idx)) result += idx
    result.toList
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        let rank = vec![0; n];
        DSU { parent, rank }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let mut xr = self.find(x);
        let mut yr = self.find(y);
        if xr == yr {
            return;
        }
        if self.rank[xr] < self.rank[yr] {
            std::mem::swap(&mut xr, &mut yr);
        }
        self.parent[yr] = xr;
        if self.rank[xr] == self.rank[yr] {
            self.rank[xr] += 1;
        }
    }

    fn reset(&mut self, x: usize) {
        self.parent[x] = x;
        self.rank[x] = 0;
    }
}

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let n_usize = n as usize;
        let mut meetings = meetings;
        meetings.sort_by(|a, b| a[2].cmp(&b[2]));

        let mut dsu = DSU::new(n_usize);
        dsu.union(0, first_person as usize);

        let mut i = 0usize;
        while i < meetings.len() {
            let cur_time = meetings[i][2];
            let mut j = i;
            while j < meetings.len() && meetings[j][2] == cur_time {
                j += 1;
            }

            // Union all meetings at this time
            for k in i..j {
                let x = meetings[k][0] as usize;
                let y = meetings[k][1] as usize;
                dsu.union(x, y);
            }

            // Determine root of person 0 after unions
            let root0 = dsu.find(0);

            // Reset participants whose component is not connected to 0
            for k in i..j {
                let x = meetings[k][0] as usize;
                let y = meetings[k][1] as usize;
                if dsu.find(x) != root0 {
                    dsu.reset(x);
                }
                if dsu.find(y) != root0 {
                    dsu.reset(y);
                }
            }

            i = j;
        }

        let mut result = Vec::new();
        let root0_final = dsu.find(0);
        for person in 0..n_usize {
            if dsu.find(person) == root0_final {
                result.push(person as i32);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (find-all-people n meetings firstPerson)
  (-> exact-integer?
      (listof (listof exact-integer?))
      exact-integer?
      (listof exact-integer?))
  (let* ((sorted
          (sort meetings
                (lambda (a b) (< (list-ref a 2) (list-ref b 2)))))
         (len (length sorted))
         (knows (make-vector n #f)))
    ;; initial secret holders
    (vector-set! knows 0 #t)
    (vector-set! knows firstPerson #t)

    ;; process meetings grouped by equal time
    (define (process-group start)
      (let* ((t (list-ref (list-ref sorted start) 2))
             (adj (make-hash))
             (next-idx
              (let loop-collect ((i start))
                (if (and (< i len)
                         (= (list-ref (list-ref sorted i) 2) t))
                    (begin
                      (define meet (list-ref sorted i))
                      (define x (list-ref meet 0))
                      (define y (list-ref meet 1))
                      (hash-set! adj x (cons y (hash-ref adj x '())))
                      (hash-set! adj y (cons x (hash-ref adj y '())))

                      (loop-collect (+ i 1)))
                    i))))
        ;; propagate secret within this time slice
        (let ((stack '()))
          (for ([person (in-hash-keys adj)])
            (when (vector-ref knows person)
              (set! stack (cons person stack))))
          (let dfs ((stk stack))
            (when (not (null? stk))
              (define p (car stk))
              (define rest (cdr stk))
              (for ([nbr (in-list (hash-ref adj p '()))])
                (when (not (vector-ref knows nbr))
                  (vector-set! knows nbr #t)
                  (set! rest (cons nbr rest))))
              (dfs rest))))
        next-idx))

    ;; outer loop over all groups
    (let loop ((idx 0))
      (when (< idx len)
        (define nxt (process-group idx))
        (loop nxt)))

    ;; collect result
    (let ((res '()))
      (for ([i (in-range n)])
        (when (vector-ref knows i)
          (set! res (cons i res))))
      (reverse res))))
```

## Erlang

```erlang
-module(solution).
-export([find_all_people/3]).

-spec find_all_people(N :: integer(), Meetings :: [[integer()]], FirstPerson :: integer()) -> [integer()].
find_all_people(_N, Meetings, FirstPerson) ->
    % initial known set contains person 0 and firstPerson
    Known0 = sets:add_element(0, sets:new()),
    Known = sets:add_element(FirstPerson, Known0),

    % convert meetings to {Time,X,Y} tuples and sort by time
    Tuples = [ {Time, X, Y} || [X, Y, Time] <- Meetings ],
    Sorted = lists:sort(Tuples),

    process_groups(Sorted, Known).

%% Process groups of meetings having the same timestamp
process_groups([], Known) ->
    sets:to_list(Known);
process_groups(MeetingsSorted, Known) ->
    [{Time, _, _} | _] = MeetingsSorted,
    {GroupPairs, Rest} = split_by_time(Time, MeetingsSorted, []),
    Adj = build_adj(GroupPairs, #{}),

    % initial queue: known persons that appear in this time's adjacency map
    Queue0 = [ P || {P,_} <- maps:to_list(Adj), sets:is_element(P, Known) ],

    NewKnown = bfs_queue(Queue0, Adj, Known),
    process_groups(Rest, NewKnown).

%% Split meetings list into those with the given Time and the rest
split_by_time(_Time, [], Acc) ->
    {lists:reverse(Acc), []};
split_by_time(Time, [{Time, X, Y} | Rest], Acc) ->
    split_by_time(Time, Rest, [{X, Y} | Acc]);
split_by_time(Time, List, Acc) ->
    {lists:reverse(Acc), List}.

%% Build adjacency map for a group of meetings (list of {X,Y})
build_adj([], Adj) -> Adj;
build_adj([{X, Y} | T], Adj0) ->
    Adj1 = maps:update_with(X,
            fun(L) -> [Y | L] end,
            [Y],
            Adj0),
    Adj2 = maps:update_with(Y,
            fun(L) -> [X | L] end,
            [X],
            Adj1),
    build_adj(T, Adj2).

%% BFS propagation within the same timestamp
bfs_queue([], _Adj, Known) ->
    Known;
bfs_queue([Person | Q], Adj, Known) ->
    Neighs = maps:get(Person, Adj, []),
    {NewKnown, NewQ} = lists:foldl(
        fun(Nbr, {Kg, AccQ}) ->
            case sets:is_element(Nbr, Kg) of
                true -> {Kg, AccQ};
                false -> {sets:add_element(Nbr, Kg), AccQ ++ [Nbr]}
            end
        end,
        {Known, Q},
        Neighs),
    bfs_queue(NewQ, Adj, NewKnown).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_all_people(n :: integer, meetings :: [[integer]], first_person :: integer) :: [integer]
  def find_all_people(_n, meetings, first_person) do
    sorted = Enum.sort_by(meetings, fn [_x, _y, t] -> t end)
    known = MapSet.new([0, first_person])
    final_known = process(sorted, known)
    MapSet.to_list(final_known) |> Enum.sort()
  end

  defp process([], known), do: known

  defp process(meetings, known) do
    [first | _] = meetings
    t = Enum.at(first, 2)

    {group, rest} = Enum.split_while(meetings, fn [_x, _y, time] -> time == t end)

    {adj, participants} = build_graph(group, %{}, MapSet.new())

    init_queue =
      MapSet.intersection(known, participants)
      |> MapSet.to_list()

    new_known = bfs(init_queue, adj, known, MapSet.new())
    process(rest, new_known)
  end

  defp build_graph([], adj, parts), do: {adj, parts}

  defp build_graph([[x, y, _] | rest], adj, parts) do
    adj1 = Map.update(adj, x, [y], fn lst -> [y | lst] end)
    adj2 = Map.update(adj1, y, [x], fn lst -> [x | lst] end)
    parts = parts |> MapSet.put(x) |> MapSet.put(y)
    build_graph(rest, adj2, parts)
  end

  defp bfs([], _adj, known, _visited), do: known

  defp bfs([person | rest], adj, known, visited) do
    if MapSet.member?(visited, person) do
      bfs(rest, adj, known, visited)
    else
      visited = MapSet.put(visited, person)
      known = MapSet.put(known, person)
      neighbors = Map.get(adj, person, [])
      bfs(neighbors ++ rest, adj, known, visited)
    end
  end
end
```
