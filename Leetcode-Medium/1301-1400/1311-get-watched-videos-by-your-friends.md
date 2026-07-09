# 1311. Get Watched Videos by Your Friends

## Cpp

```cpp
class Solution {
public:
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideos, vector<vector<int>>& friends, int id, int level) {
        int n = watchedVideos.size();
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(id);
        visited[id] = true;
        int curLevel = 0;
        while (!q.empty() && curLevel < level) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                int u = q.front(); q.pop();
                for (int v : friends[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        q.push(v);
                    }
                }
            }
            ++curLevel;
        }
        unordered_map<string, int> freq;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (const string& video : watchedVideos[u]) {
                ++freq[video];
            }
        }
        vector<pair<string,int>> items(freq.begin(), freq.end());
        sort(items.begin(), items.end(), [](const auto& a, const auto& b){
            if (a.second != b.second) return a.second < b.second;
            return a.first < b.first;
        });
        vector<string> result;
        result.reserve(items.size());
        for (auto& p : items) result.push_back(p.first);
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        int n = friends.length;
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();
        visited[id] = true;
        queue.offer(id);
        int currentLevel = 0;
        while (!queue.isEmpty() && currentLevel < level) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int person = queue.poll();
                for (int f : friends[person]) {
                    if (!visited[f]) {
                        visited[f] = true;
                        queue.offer(f);
                    }
                }
            }
            currentLevel++;
        }
        Map<String, Integer> freq = new HashMap<>();
        while (!queue.isEmpty()) {
            int person = queue.poll();
            for (String video : watchedVideos.get(person)) {
                freq.put(video, freq.getOrDefault(video, 0) + 1);
            }
        }
        List<String> result = new ArrayList<>(freq.keySet());
        result.sort((a, b) -> {
            int cmp = Integer.compare(freq.get(a), freq.get(b));
            if (cmp != 0) return cmp;
            return a.compareTo(b);
        });
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        from collections import deque, Counter

        n = len(friends)
        visited = [False] * n
        q = deque()
        q.append((id, 0))
        visited[id] = True
        target_friends = []

        while q:
            cur, dist = q.popleft()
            if dist == level:
                target_friends.append(cur)
                continue
            for nb in friends[cur]:
                if not visited[nb]:
                    visited[nb] = True
                    q.append((nb, dist + 1))

        cnt = Counter()
        for person in target_friends:
            cnt.update(watchedVideos[person])

        # sort by frequency then alphabetically
        result = sorted(cnt.keys(), key=lambda x: (cnt[x], x))
        return result
```

## Python3

```python
class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        from collections import deque, Counter
        n = len(friends)
        visited = [False] * n
        q = deque([id])
        visited[id] = True
        cur = 0
        while q and cur < level:
            for _ in range(len(q)):
                node = q.popleft()
                for nb in friends[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        q.append(nb)
            cur += 1
        cnt = Counter()
        while q:
            person = q.popleft()
            for v in watchedVideos[person]:
                cnt[v] += 1
        return sorted(cnt.keys(), key=lambda x: (cnt[x], x))
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static char* dupStr(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    memcpy(p, s, len + 1);
    return p;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** watchedVideosByFriends(char*** watchedVideos, int watchedVideosSize, int* watchedVideosColSize,
                              int** friends, int friendsSize, int* friendsColSize,
                              int id, int level, int* returnSize) {
    bool visited[101] = {false};
    int cur[101], next[101];
    int curSize = 0, nextSize = 0;

    cur[curSize++] = id;
    visited[id] = true;

    for (int d = 0; d < level; ++d) {
        nextSize = 0;
        for (int i = 0; i < curSize; ++i) {
            int u = cur[i];
            for (int k = 0; k < friendsColSize[u]; ++k) {
                int v = friends[u][k];
                if (!visited[v]) {
                    visited[v] = true;
                    next[nextSize++] = v;
                }
            }
        }
        memcpy(cur, next, nextSize * sizeof(int));
        curSize = nextSize;
    }

    if (curSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    typedef struct {
        char *name;
        int cnt;
    } Entry;

    // maximum possible distinct videos is curSize * max per person (100)
    Entry *entries = (Entry *)malloc(curSize * 100 * sizeof(Entry));
    int m = 0;

    for (int i = 0; i < curSize; ++i) {
        int person = cur[i];
        int vidCount = watchedVideosColSize[person];
        for (int j = 0; j < vidCount; ++j) {
            char *video = watchedVideos[person][j];
            int idx = -1;
            for (int e = 0; e < m; ++e) {
                if (strcmp(entries[e].name, video) == 0) {
                    idx = e;
                    break;
                }
            }
            if (idx == -1) {
                entries[m].name = dupStr(video);
                entries[m].cnt = 1;
                ++m;
            } else {
                entries[idx].cnt++;
            }
        }
    }

    int cmp(const void *a, const void *b) {
        const Entry *ea = (const Entry *)a;
        const Entry *eb = (const Entry *)b;
        if (ea->cnt != eb->cnt)
            return ea->cnt - eb->cnt;
        return strcmp(ea->name, eb->name);
    }

    qsort(entries, m, sizeof(Entry), cmp);

    char **res = (char **)malloc(m * sizeof(char *));
    for (int i = 0; i < m; ++i) {
        res[i] = entries[i].name;
    }
    free(entries);

    *returnSize = m;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> WatchedVideosByFriends(IList<IList<string>> watchedVideos, int[][] friends, int id, int level) {
        int n = friends.Length;
        bool[] visited = new bool[n];
        Queue<int> queue = new Queue<int>();
        visited[id] = true;
        queue.Enqueue(id);
        int currentLevel = 0;

        while (queue.Count > 0 && currentLevel < level) {
            int size = queue.Count;
            for (int i = 0; i < size; i++) {
                int person = queue.Dequeue();
                foreach (int f in friends[person]) {
                    if (!visited[f]) {
                        visited[f] = true;
                        queue.Enqueue(f);
                    }
                }
            }
            currentLevel++;
        }

        // Now queue contains all people at exactly 'level' distance
        Dictionary<string, int> freq = new Dictionary<string, int>();
        while (queue.Count > 0) {
            int person = queue.Dequeue();
            foreach (string video in watchedVideos[person]) {
                if (!freq.ContainsKey(video)) freq[video] = 0;
                freq[video]++;
            }
        }

        List<string> result = new List<string>(freq.Keys);
        result.Sort((a, b) => {
            int cmp = freq[a].CompareTo(freq[b]);
            return cmp != 0 ? cmp : string.CompareOrdinal(a, b);
        });

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} watchedVideos
 * @param {number[][]} friends
 * @param {number} id
 * @param {number} level
 * @return {string[]}
 */
var watchedVideosByFriends = function(watchedVideos, friends, id, level) {
    const n = watchedVideos.length;
    const visited = new Array(n).fill(false);
    let queue = [id];
    visited[id] = true;
    let dist = 0;

    while (queue.length && dist < level) {
        const next = [];
        for (const person of queue) {
            for (const nb of friends[person]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    next.push(nb);
                }
            }
        }
        queue = next;
        dist++;
    }

    const freq = new Map();
    for (const person of queue) {
        for (const video of watchedVideos[person]) {
            freq.set(video, (freq.get(video) || 0) + 1);
        }
    }

    const sorted = Array.from(freq.entries()).sort((a, b) => {
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0;
    });

    return sorted.map(pair => pair[0]);
};
```

## Typescript

```typescript
function watchedVideosByFriends(watchedVideos: string[][], friends: number[][], id: number, level: number): string[] {
    const n = watchedVideos.length;
    const visited = new Array<boolean>(n).fill(false);
    visited[id] = true;
    let currentLevel = 0;
    let queue: number[] = [id];

    while (queue.length && currentLevel < level) {
        const next: number[] = [];
        for (const person of queue) {
            for (const f of friends[person]) {
                if (!visited[f]) {
                    visited[f] = true;
                    next.push(f);
                }
            }
        }
        queue = next;
        currentLevel++;
    }

    const freqMap = new Map<string, number>();
    for (const person of queue) {
        for (const video of watchedVideos[person]) {
            freqMap.set(video, (freqMap.get(video) ?? 0) + 1);
        }
    }

    const entries = Array.from(freqMap.entries());
    entries.sort((a, b) => {
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[0].localeCompare(b[0]);
    });

    return entries.map(e => e[0]);
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $watchedVideos
     * @param Integer[][] $friends
     * @param Integer $id
     * @param Integer $level
     * @return String[]
     */
    function watchedVideosByFriends($watchedVideos, $friends, $id, $level) {
        $n = count($watchedVideos);
        $visited = array_fill(0, $n, false);
        $queue = [];
        $queue[] = $id;
        $visited[$id] = true;
        $currentLevel = 0;

        while (!empty($queue) && $currentLevel < $level) {
            $size = count($queue);
            for ($i = 0; $i < $size; $i++) {
                $person = array_shift($queue);
                foreach ($friends[$person] as $nbr) {
                    if (!$visited[$nbr]) {
                        $visited[$nbr] = true;
                        $queue[] = $nbr;
                    }
                }
            }
            $currentLevel++;
        }

        // $queue now contains all friends at exact distance $level
        $freq = [];
        foreach ($queue as $person) {
            foreach ($watchedVideos[$person] as $video) {
                if (!isset($freq[$video])) {
                    $freq[$video] = 0;
                }
                $freq[$video]++;
            }
        }

        $videos = array_keys($freq);
        usort($videos, function($a, $b) use ($freq) {
            if ($freq[$a] == $freq[$b]) {
                return strcmp($a, $b);
            }
            return $freq[$a] <=> $freq[$b];
        });

        return $videos;
    }
}
```

## Swift

```swift
class Solution {
    func watchedVideosByFriends(_ watchedVideos: [[String]], _ friends: [[Int]], _ id: Int, _ level: Int) -> [String] {
        let n = watchedVideos.count
        var visited = [Bool](repeating: false, count: n)
        var queue: [(person: Int, depth: Int)] = []
        var head = 0
        var targetFriends: [Int] = []
        
        queue.append((id, 0))
        visited[id] = true
        
        while head < queue.count {
            let (curr, depth) = queue[head]
            head += 1
            
            if depth == level {
                targetFriends.append(curr)
                continue
            }
            
            for nb in friends[curr] {
                if !visited[nb] {
                    visited[nb] = true
                    queue.append((nb, depth + 1))
                }
            }
        }
        
        var freq: [String: Int] = [:]
        for person in targetFriends {
            for video in watchedVideos[person] {
                freq[video, default: 0] += 1
            }
        }
        
        let sortedVideos = freq.keys.sorted { a, b in
            let fa = freq[a]!
            let fb = freq[b]!
            if fa == fb {
                return a < b
            } else {
                return fa < fb
            }
        }
        
        return sortedVideos
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun watchedVideosByFriends(
        watchedVideos: List<List<String>>,
        friends: Array<IntArray>,
        id: Int,
        level: Int
    ): List<String> {
        val n = friends.size
        val visited = BooleanArray(n)
        var current = mutableListOf<Int>()
        visited[id] = true
        current.add(id)

        repeat(level) {
            val next = mutableListOf<Int>()
            for (person in current) {
                for (f in friends[person]) {
                    if (!visited[f]) {
                        visited[f] = true
                        next.add(f)
                    }
                }
            }
            current = next
        }

        val freqMap = HashMap<String, Int>()
        for (person in current) {
            for (video in watchedVideos[person]) {
                freqMap[video] = freqMap.getOrDefault(video, 0) + 1
            }
        }

        return freqMap.entries
            .sortedWith(compareBy<Map.Entry<String, Int>> { it.value }.thenBy { it.key })
            .map { it.key }
    }
}
```

## Dart

```dart
class Solution {
  List<String> watchedVideosByFriends(
      List<List<String>> watchedVideos,
      List<List<int>> friends,
      int id,
      int level) {
    int n = watchedVideos.length;
    List<bool> visited = List.filled(n, false);
    List<int> current = [id];
    visited[id] = true;

    for (int l = 0; l < level && current.isNotEmpty; ++l) {
      List<int> next = [];
      for (int person in current) {
        for (int f in friends[person]) {
          if (!visited[f]) {
            visited[f] = true;
            next.add(f);
          }
        }
      }
      current = next;
    }

    Map<String, int> freq = {};
    for (int person in current) {
      for (String video in watchedVideos[person]) {
        freq[video] = (freq[video] ?? 0) + 1;
      }
    }

    List<MapEntry<String, int>> entries = freq.entries.toList();
    entries.sort((a, b) {
      if (a.value != b.value) return a.value - b.value;
      return a.key.compareTo(b.key);
    });

    return entries.map((e) => e.key).toList();
  }
}
```

## Golang

```go
package main

import "sort"

func watchedVideosByFriends(watchedVideos [][]string, friends [][]int, id int, level int) []string {
	n := len(friends)
	visited := make([]bool, n)
	queue := []int{id}
	visited[id] = true

	for l := 0; l < level; l++ {
		next := []int{}
		for _, cur := range queue {
			for _, nb := range friends[cur] {
				if !visited[nb] {
					visited[nb] = true
					next = append(next, nb)
				}
			}
		}
		queue = next
	}

	freq := make(map[string]int)
	for _, person := range queue {
		for _, video := range watchedVideos[person] {
			freq[video]++
		}
	}

	type pair struct {
		name string
		cnt  int
	}
	pairs := make([]pair, 0, len(freq))
	for name, cnt := range freq {
		pairs = append(pairs, pair{name, cnt})
	}

	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].cnt == pairs[j].cnt {
			return pairs[i].name < pairs[j].name
		}
		return pairs[i].cnt < pairs[j].cnt
	})

	res := make([]string, len(pairs))
	for i, p := range pairs {
		res[i] = p.name
	}
	return res
}
```

## Ruby

```ruby
def watched_videos_by_friends(watched_videos, friends, id, level)
  n = watched_videos.size
  visited = Array.new(n, false)
  queue = [id]
  visited[id] = true
  current_level = 0

  while !queue.empty? && current_level < level
    next_queue = []
    queue.each do |person|
      friends[person].each do |nbr|
        unless visited[nbr]
          visited[nbr] = true
          next_queue << nbr
        end
      end
    end
    queue = next_queue
    current_level += 1
  end

  freq = Hash.new(0)
  queue.each do |person|
    watched_videos[person].each { |video| freq[video] += 1 }
  end

  freq.keys.sort_by { |video| [freq[video], video] }
end
```

## Scala

```scala
object Solution {
    def watchedVideosByFriends(watchedVideos: List[List[String]], friends: Array[Array[Int]], id: Int, level: Int): List[String] = {
        val n = friends.length
        val visited = Array.fill(n)(false)
        val queue = scala.collection.mutable.Queue[Int]()
        queue.enqueue(id)
        visited(id) = true
        var currentLevel = 0

        while (queue.nonEmpty && currentLevel < level) {
            val size = queue.size
            for (_ <- 0 until size) {
                val person = queue.dequeue()
                for (nbr <- friends(person)) {
                    if (!visited(nbr)) {
                        visited(nbr) = true
                        queue.enqueue(nbr)
                    }
                }
            }
            currentLevel += 1
        }

        val countMap = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (person <- queue) {
            for (video <- watchedVideos(person)) {
                countMap(video) = countMap(video) + 1
            }
        }

        countMap.toSeq.sortBy { case (video, cnt) => (cnt, video) }.map(_._1).toList
    }
}
```

## Rust

```rust
use std::collections::{VecDeque, HashMap};

impl Solution {
    pub fn watched_videos_by_friends(
        watched_videos: Vec<Vec<String>>,
        friends: Vec<Vec<i32>>,
        id: i32,
        level: i32,
    ) -> Vec<String> {
        let n = watched_videos.len();
        let mut visited = vec![false; n];
        let mut queue = VecDeque::new();

        let start = id as usize;
        visited[start] = true;
        queue.push_back(start);

        for _ in 0..level {
            let size = queue.len();
            for _ in 0..size {
                if let Some(cur) = queue.pop_front() {
                    for &nbr_i32 in &friends[cur] {
                        let nbr = nbr_i32 as usize;
                        if !visited[nbr] {
                            visited[nbr] = true;
                            queue.push_back(nbr);
                        }
                    }
                }
            }
        }

        let mut count: HashMap<String, i32> = HashMap::new();
        for &person in queue.iter() {
            for video in &watched_videos[person] {
                *count.entry(video.clone()).or_insert(0) += 1;
            }
        }

        let mut items: Vec<(String, i32)> = count.into_iter().collect();
        items.sort_by(|a, b| {
            if a.1 != b.1 {
                a.1.cmp(&b.1)
            } else {
                a.0.cmp(&b.0)
            }
        });

        items.into_iter().map(|(s, _)| s).collect()
    }
}
```

## Racket

```racket
(define/contract (watched-videos-by-friends watchedVideos friends id level)
  (-> (listof (listof string?)) (listof (listof exact-integer?)) exact-integer? exact-integer? (listof string?))
  (let* ((n (length watchedVideos))
         (adj (list->vector friends))
         (visited (make-vector n #f)))
    (vector-set! visited id #t)
    (let bfs ((queue (list (cons id 0))) (result '()))
      (cond
        [(null? queue)
         (let* ((freq (make-hash))
                (collect (lambda (fid)
                           (for-each (lambda (video)
                                       (hash-update! freq video add1 0))
                                     (list-ref watchedVideos fid)))))
           (for-each collect result)
           (let* ((items (hash->list freq))
                  (sorted (sort items
                                (lambda (a b)
                                  (let ((fa (cdr a)) (fb (cdr b))
                                        (sa (car a)) (sb (car b)))
                                    (if (= fa fb)
                                        (string<? sa sb)
                                        (< fa fb)))))))
             (map car sorted)))]
        [else
         (define current (car queue))
         (define rest (cdr queue))
         (define node (car current))
         (define depth (cdr current))
         (cond
           [(= depth level)
            (bfs rest (cons node result))]
           [else
            (let* ((neighbors (vector-ref adj node))
                   (new-neighbors (filter (lambda (nbr) (not (vector-ref visited nbr))) neighbors)))
              (for-each (lambda (nbr) (vector-set! visited nbr #t)) new-neighbors)
              (define new-queue
                (append rest (map (lambda (nbr) (cons nbr (+ depth 1))) new-neighbors)))
              (bfs new-queue result))]))))))
```

## Erlang

```erlang
-spec watched_videos_by_friends(WatchedVideos :: [[unicode:unicode_binary()]], Friends :: [[integer()]], Id :: integer(), Level :: integer()) -> [unicode:unicode_binary()].
watched_videos_by_friends(WatchedVideos, Friends, Id, Level) ->
    LevelFriends = bfs_level(Friends, Id, Level),
    FreqMap = count_videos(LevelFriends, WatchedVideos, #{}),
    VideoCounts = maps:to_list(FreqMap),
    Sorted = lists:sort(
        fun({V1, C1}, {V2, C2}) ->
            case C1 == C2 of
                true -> V1 < V2;
                false -> C1 < C2
            end
        end,
        VideoCounts),
    [V || {V, _} <- Sorted].

bfs_level(Friends, Id, Level) ->
    Visited0 = #{Id => true},
    bfs_iter(Friends, Level, [Id], Visited0).

bfs_iter(_Friends, 0, Curr, _Visited) -> Curr;
bfs_iter(Friends, L, Curr, Visited) ->
    {Next, Visited1} = lists:foldl(
        fun(Node, {Acc, Vis}) ->
            Neighs = lists:nth(Node + 1, Friends),
            lists:foldl(
                fun(N, {A, V}) ->
                    case maps:is_key(N, V) of
                        true -> {A, V};
                        false -> {[N | A], V#{N => true}}
                    end
                end,
                {Acc, Vis},
                Neighs)
        end,
        {[], Visited},
        Curr),
    bfs_iter(Friends, L - 1, Next, Visited1).

count_videos([], _WatchedVideos, Map) -> Map;
count_videos([Id | Rest], WatchedVideos, Map) ->
    Videos = lists:nth(Id + 1, WatchedVideos),
    NewMap = lists:foldl(
        fun(Vid, Acc) ->
            case maps:is_key(Vid, Acc) of
                true ->
                    C = maps:get(Vid, Acc),
                    Acc#{Vid => C + 1};
                false -> Acc#{Vid => 1}
            end
        end,
        Map,
        Videos),
    count_videos(Rest, WatchedVideos, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec watched_videos_by_friends(watched_videos :: [[String.t]], friends :: [[integer]], id :: integer, level :: integer) :: [String.t]
  def watched_videos_by_friends(watched_videos, friends, id, level) do
    target_ids = bfs_level(friends, id, level)

    videos =
      Enum.flat_map(target_ids, fn friend_id ->
        Enum.at(watched_videos, friend_id)
      end)

    freq_map =
      Enum.reduce(videos, %{}, fn video, acc ->
        Map.update(acc, video, 1, &(&1 + 1))
      end)

    freq_map
    |> Enum.map(fn {video, cnt} -> {cnt, video} end)
    |> Enum.sort_by(fn {cnt, video} -> {cnt, video} end)
    |> Enum.map(fn {_cnt, video} -> video end)
  end

  defp bfs_level(friends, start_id, target_level) do
    visited = MapSet.new([start_id])
    bfs_loop(friends, [start_id], visited, 0, target_level)
  end

  defp bfs_loop(_friends, current, _visited, depth, target_level) when depth == target_level do
    current
  end

  defp bfs_loop(friends, current, visited, depth, target_level) do
    next =
      Enum.flat_map(current, fn node ->
        Enum.at(friends, node)
      end)
      |> Enum.filter(fn n -> not MapSet.member?(visited, n) end)

    new_visited = Enum.reduce(next, visited, &MapSet.put(&2, &1))

    bfs_loop(friends, next, new_visited, depth + 1, target_level)
  end
end
```
