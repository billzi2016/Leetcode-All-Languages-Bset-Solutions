# 2456. Most Popular Video Creator

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> mostPopularCreator(vector<string>& creators, vector<string>& ids, vector<int>& views) {
        unordered_map<string, long long> total;
        unordered_map<string, pair<int, string>> best; // {maxViews, id}
        int n = creators.size();
        for (int i = 0; i < n; ++i) {
            const string& c = creators[i];
            const string& id = ids[i];
            int v = views[i];
            total[c] += v;
            if (!best.count(c)) {
                best[c] = {v, id};
            } else {
                auto &p = best[c];
                if (v > p.first || (v == p.first && id < p.second)) {
                    p = {v, id};
                }
            }
        }
        long long maxPop = 0;
        for (const auto& kv : total) {
            if (kv.second > maxPop) maxPop = kv.second;
        }
        vector<vector<string>> ans;
        for (const auto& kv : total) {
            if (kv.second == maxPop) {
                const string& creator = kv.first;
                ans.push_back({creator, best[creator].second});
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class CreatorInfo {
        long totalViews;
        int maxVideoViews;
        String bestId;
        CreatorInfo(long total, int maxV, String id) {
            this.totalViews = total;
            this.maxVideoViews = maxV;
            this.bestId = id;
        }
    }

    public List<List<String>> mostPopularCreator(String[] creators, String[] ids, int[] views) {
        int n = creators.length;
        java.util.Map<String, CreatorInfo> map = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            String creator = creators[i];
            String id = ids[i];
            int view = views[i];
            CreatorInfo info = map.get(creator);
            if (info == null) {
                info = new CreatorInfo(view, view, id);
                map.put(creator, info);
            } else {
                info.totalViews += view;
                if (view > info.maxVideoViews ||
                    (view == info.maxVideoViews && id.compareTo(info.bestId) < 0)) {
                    info.maxVideoViews = view;
                    info.bestId = id;
                }
            }
        }

        long maxTotal = 0;
        for (CreatorInfo info : map.values()) {
            if (info.totalViews > maxTotal) {
                maxTotal = info.totalViews;
            }
        }

        List<List<String>> result = new java.util.ArrayList<>();
        for (java.util.Map.Entry<String, CreatorInfo> entry : map.entrySet()) {
            CreatorInfo info = entry.getValue();
            if (info.totalViews == maxTotal) {
                List<String> pair = new java.util.ArrayList<>(2);
                pair.add(entry.getKey());
                pair.add(info.bestId);
                result.add(pair);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        stats = {}
        for c, vid, v in zip(creators, ids, views):
            if c not in stats:
                # total_views, best_view, best_id
                stats[c] = [v, v, vid]
            else:
                stats[c][0] += v
                if v > stats[c][1] or (v == stats[c][1] and vid < stats[c][2]):
                    stats[c][1] = v
                    stats[c][2] = vid
        max_pop = max(info[0] for info in stats.values())
        result = []
        for c, (total, _, best_id) in stats.items():
            if total == max_pop:
                result.append([c, best_id])
        return result
```

## Python3

```python
from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        stats = {}
        for c, vid, v in zip(creators, ids, views):
            if c not in stats:
                # total_views, best_view, best_id
                stats[c] = [v, v, vid]
            else:
                total, best_v, best_id = stats[c]
                total += v
                if v > best_v or (v == best_v and vid < best_id):
                    best_v, best_id = v, vid
                stats[c] = [total, best_v, best_id]

        max_popularity = max(total for total, _, _ in stats.values())
        result = []
        for creator, (total, _, best_id) in stats.items():
            if total == max_popularity:
                result.append([creator, best_id])
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *creator;
    char *id;
    int view;
} Video;

typedef struct {
    char *name;
    long long total;
    int bestView;
    char *bestId;
} CreatorInfo;

static int video_cmp(const void *a, const void *b) {
    const Video *va = (const Video *)a;
    const Video *vb = (const Video *)b;
    return strcmp(va->creator, vb->creator);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** mostPopularCreator(char** creators, int creatorsSize,
                           char** ids, int idsSize,
                           int* views, int viewsSize,
                           int* returnSize, int** returnColumnSizes) {
    int n = creatorsSize;
    Video *videos = (Video *)malloc(n * sizeof(Video));
    for (int i = 0; i < n; ++i) {
        videos[i].creator = creators[i];
        videos[i].id = ids[i];
        videos[i].view = views[i];
    }

    qsort(videos, n, sizeof(Video), video_cmp);

    CreatorInfo *infos = (CreatorInfo *)malloc(n * sizeof(CreatorInfo));
    int m = 0; // number of unique creators

    for (int i = 0; i < n;) {
        char *curCreator = videos[i].creator;
        long long sum = 0;
        int bestV = -1;
        char *bestId = NULL;

        while (i < n && strcmp(videos[i].creator, curCreator) == 0) {
            sum += videos[i].view;
            if (videos[i].view > bestV ||
               (videos[i].view == bestV && strcmp(videos[i].id, bestId) < 0)) {
                bestV = videos[i].view;
                bestId = videos[i].id;
            }
            ++i;
        }

        infos[m].name = curCreator;
        infos[m].total = sum;
        infos[m].bestView = bestV;
        infos[m].bestId = bestId;
        ++m;
    }

    long long maxTotal = 0;
    for (int i = 0; i < m; ++i) {
        if (infos[i].total > maxTotal) {
            maxTotal = infos[i].total;
        }
    }

    int resultCount = 0;
    for (int i = 0; i < m; ++i) {
        if (infos[i].total == maxTotal) {
            ++resultCount;
        }
    }

    char ***answer = (char ***)malloc(resultCount * sizeof(char **));
    int *colSizes = (int *)malloc(resultCount * sizeof(int));

    int idx = 0;
    for (int i = 0; i < m; ++i) {
        if (infos[i].total == maxTotal) {
            answer[idx] = (char **)malloc(2 * sizeof(char *));
            answer[idx][0] = strdup(infos[i].name);
            answer[idx][1] = strdup(infos[i].bestId);
            colSizes[idx] = 2;
            ++idx;
        }
    }

    *returnSize = resultCount;
    *returnColumnSizes = colSizes;

    free(videos);
    free(infos);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> MostPopularCreator(string[] creators, string[] ids, int[] views) {
        var dict = new Dictionary<string, (long total, int maxViews, string bestId)>();
        for (int i = 0; i < creators.Length; i++) {
            string creator = creators[i];
            string id = ids[i];
            int view = views[i];

            if (!dict.TryGetValue(creator, out var info)) {
                info = (0L, -1, "");
            }

            long newTotal = info.total + view;
            int curMaxViews = info.maxViews;
            string curBestId = info.bestId;

            if (view > curMaxViews) {
                curMaxViews = view;
                curBestId = id;
            } else if (view == curMaxViews && string.CompareOrdinal(id, curBestId) < 0) {
                curBestId = id;
            }

            dict[creator] = (newTotal, curMaxViews, curBestId);
        }

        long maxTotal = 0;
        foreach (var kv in dict) {
            if (kv.Value.total > maxTotal) {
                maxTotal = kv.Value.total;
            }
        }

        var result = new List<IList<string>>();
        foreach (var kv in dict) {
            if (kv.Value.total == maxTotal) {
                result.Add(new List<string> { kv.Key, kv.Value.bestId });
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} creators
 * @param {string[]} ids
 * @param {number[]} views
 * @return {string[][]}
 */
var mostPopularCreator = function(creators, ids, views) {
    const map = new Map(); // creator -> {total, bestViews, bestId}
    for (let i = 0; i < creators.length; ++i) {
        const c = creators[i];
        const id = ids[i];
        const v = views[i];
        if (!map.has(c)) {
            map.set(c, { total: 0, bestViews: -1, bestId: '' });
        }
        const info = map.get(c);
        info.total += v;
        if (v > info.bestViews || (v === info.bestViews && id < info.bestId)) {
            info.bestViews = v;
            info.bestId = id;
        }
    }

    let maxTotal = 0;
    for (const { total } of map.values()) {
        if (total > maxTotal) maxTotal = total;
    }

    const result = [];
    for (const [creator, data] of map.entries()) {
        if (data.total === maxTotal) {
            result.push([creator, data.bestId]);
        }
    }
    return result;
};
```

## Typescript

```typescript
function mostPopularCreator(creators: string[], ids: string[], views: number[]): string[][] {
    const map = new Map<string, { total: number; bestViews: number; bestId: string }>();
    
    for (let i = 0; i < creators.length; ++i) {
        const creator = creators[i];
        const id = ids[i];
        const view = views[i];
        
        if (!map.has(creator)) {
            map.set(creator, { total: view, bestViews: view, bestId: id });
        } else {
            const data = map.get(creator)!;
            data.total += view;
            if (view > data.bestViews) {
                data.bestViews = view;
                data.bestId = id;
            } else if (view === data.bestViews && id < data.bestId) {
                data.bestId = id;
            }
        }
    }
    
    let maxTotal = 0;
    for (const { total } of map.values()) {
        if (total > maxTotal) maxTotal = total;
    }
    
    const result: string[][] = [];
    for (const [creator, data] of map.entries()) {
        if (data.total === maxTotal) {
            result.push([creator, data.bestId]);
        }
    }
    
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $creators
     * @param String[] $ids
     * @param Integer[] $views
     * @return String[][]
     */
    function mostPopularCreator($creators, $ids, $views) {
        $total = [];
        $bestView = [];
        $bestId = [];

        $n = count($creators);
        for ($i = 0; $i < $n; $i++) {
            $c = $creators[$i];
            $id = $ids[$i];
            $v = $views[$i];

            if (!isset($total[$c])) {
                $total[$c] = 0;
                $bestView[$c] = -1;
                $bestId[$c] = '';
            }

            $total[$c] += $v;

            if ($v > $bestView[$c] || ($v == $bestView[$c] && strcmp($id, $bestId[$c]) < 0)) {
                $bestView[$c] = $v;
                $bestId[$c] = $id;
            }
        }

        $maxTotal = 0;
        foreach ($total as $val) {
            if ($val > $maxTotal) {
                $maxTotal = $val;
            }
        }

        $result = [];
        foreach ($total as $creator => $val) {
            if ($val == $maxTotal) {
                $result[] = [$creator, $bestId[$creator]];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func mostPopularCreator(_ creators: [String], _ ids: [String], _ views: [Int]) -> [[String]] {
        var totalViews = [String: Int]()
        var bestVideo = [String: (views: Int, id: String)]()
        
        for i in 0..<creators.count {
            let creator = creators[i]
            let videoId = ids[i]
            let viewCount = views[i]
            
            totalViews[creator, default: 0] += viewCount
            
            if let current = bestVideo[creator] {
                if viewCount > current.views || (viewCount == current.views && videoId < current.id) {
                    bestVideo[creator] = (viewCount, videoId)
                }
            } else {
                bestVideo[creator] = (viewCount, videoId)
            }
        }
        
        guard let maxPopularity = totalViews.values.max() else { return [] }
        
        var result = [[String]]()
        for (creator, pop) in totalViews where pop == maxPopularity {
            if let info = bestVideo[creator] {
                result.append([creator, info.id])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private data class CreatorInfo(
        var total: Long = 0L,
        var bestView: Int = -1,
        var bestId: String = ""
    )
    
    fun mostPopularCreator(creators: Array<String>, ids: Array<String>, views: IntArray): List<List<String>> {
        val map = HashMap<String, CreatorInfo>()
        for (i in creators.indices) {
            val creator = creators[i]
            val id = ids[i]
            val view = views[i]
            val info = map.getOrPut(creator) { CreatorInfo() }
            info.total += view.toLong()
            if (view > info.bestView || (view == info.bestView && id < info.bestId)) {
                info.bestView = view
                info.bestId = id
            }
        }
        var maxTotal = 0L
        for (info in map.values) {
            if (info.total > maxTotal) maxTotal = info.total
        }
        val result = ArrayList<List<String>>()
        for ((creator, info) in map) {
            if (info.total == maxTotal) {
                result.add(listOf(creator, info.bestId))
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> mostPopularCreator(
      List<String> creators, List<String> ids, List<int> views) {
    final Map<String, int> totalViews = {};
    final Map<String, List<dynamic>> bestVideo = {};

    for (int i = 0; i < creators.length; ++i) {
      String creator = creators[i];
      String id = ids[i];
      int view = views[i];

      totalViews[creator] = (totalViews[creator] ?? 0) + view;

      if (!bestVideo.containsKey(creator)) {
        bestVideo[creator] = [view, id];
      } else {
        var cur = bestVideo[creator]!;
        if (view > cur[0]) {
          cur[0] = view;
          cur[1] = id;
        } else if (view == cur[0] && id.compareTo(cur[1]) < 0) {
          cur[1] = id;
        }
      }
    }

    int maxPopularity = 0;
    for (var v in totalViews.values) {
      if (v > maxPopularity) maxPopularity = v;
    }

    List<List<String>> answer = [];
    totalViews.forEach((creator, pop) {
      if (pop == maxPopularity) {
        answer.add([creator, bestVideo[creator]![1] as String]);
      }
    });

    return answer;
  }
}
```

## Golang

```go
func mostPopularCreator(creators []string, ids []string, views []int) [][]string {
	total := make(map[string]int64)
	bestView := make(map[string]int)
	bestID := make(map[string]string)

	for i := 0; i < len(creators); i++ {
		c := creators[i]
		v := views[i]
		id := ids[i]

		total[c] += int64(v)

		if cur, ok := bestView[c]; !ok || v > cur {
			bestView[c] = v
			bestID[c] = id
		} else if v == cur && id < bestID[c] {
			bestID[c] = id
		}
	}

	var maxTotal int64 = -1
	for _, sum := range total {
		if sum > maxTotal {
			maxTotal = sum
		}
	}

	res := [][]string{}
	for c, sum := range total {
		if sum == maxTotal {
			res = append(res, []string{c, bestID[c]})
		}
	}
	return res
}
```

## Ruby

```ruby
def most_popular_creator(creators, ids, views)
  total_views = Hash.new(0)
  best_video = {}

  creators.each_index do |i|
    creator = creators[i]
    vid_id = ids[i]
    view_cnt = views[i]

    total_views[creator] += view_cnt

    if !best_video.key?(creator) ||
       view_cnt > best_video[creator][0] ||
       (view_cnt == best_video[creator][0] && vid_id < best_video[creator][1])
      best_video[creator] = [view_cnt, vid_id]
    end
  end

  max_popularity = total_views.values.max
  result = []

  total_views.each do |creator, pop|
    if pop == max_popularity
      result << [creator, best_video[creator][1]]
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def mostPopularCreator(creators: Array[String], ids: Array[String], views: Array[Int]): List[List[String]] = {
        val totalViews = mutable.Map[String, Long]().withDefaultValue(0L)
        val bestVideo = mutable.Map[String, (Int, String)]()

        for (i <- creators.indices) {
            val creator = creators(i)
            val id = ids(i)
            val view = views(i)

            totalViews(creator) = totalViews(creator) + view

            bestVideo.get(creator) match {
                case None => bestVideo(creator) = (view, id)
                case Some((bestView, bestId)) =>
                    if (view > bestView || (view == bestView && id < bestId))
                        bestVideo(creator) = (view, id)
            }
        }

        val maxTotal = totalViews.values.max
        totalViews.iterator
          .filter(_._2 == maxTotal)
          .map { case (creator, _) => List(creator, bestVideo(creator)._2) }
          .toList
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn most_popular_creator(creators: Vec<String>, ids: Vec<String>, views: Vec<i32>) -> Vec<Vec<String>> {
        let mut map: HashMap<String, (i64, i32, String)> = HashMap::new();
        for i in 0..creators.len() {
            let creator = &creators[i];
            let id = &ids[i];
            let view = views[i];
            let entry = map.entry(creator.clone()).or_insert((0i64, -1i32, String::new()));
            entry.0 += view as i64;
            if view > entry.1 || (view == entry.1 && id < &entry.2) {
                entry.1 = view;
                entry.2 = id.clone();
            }
        }

        let mut max_pop: i64 = 0;
        for (_, (total, _, _)) in map.iter() {
            if *total > max_pop {
                max_pop = *total;
            }
        }

        let mut result: Vec<Vec<String>> = Vec::new();
        for (creator, (total, _, best_id)) in map.into_iter() {
            if total == max_pop {
                result.push(vec![creator, best_id]);
            }
        }
        result
    }
}
```

## Racket

```racket
(define-struct info (total best-view best-id) #:mutable)

(define/contract (most-popular-creator creators ids views)
  (-> (listof string?) (listof string?) (listof exact-integer?) (listof (listof string?)))
  (let ([h (make-hash)])
    (for ([c creators] [i ids] [v views])
      (define existing (hash-ref h c #f))
      (if existing
          (begin
            (set-info-total! existing (+ (info-total existing) v))
            (cond [(> v (info-best-view existing))
                   (set-info-best-view! existing v)
                   (set-info-best-id!   existing i)]
                  [(and (= v (info-best-view existing))
                        (string<? i (info-best-id existing)))
                   (set-info-best-id! existing i)]))
          (hash-set! h c (make-info v v i))))
    ;; determine maximum total popularity
    (define max-total -1)
    (for ([inf (in-hash-values h)])
      (when (> (info-total inf) max-total)
        (set! max-total (info-total inf))))
    ;; collect creators with maximal popularity and their best video id
    (let loop ((keys (hash-keys h)) (acc '()))
      (if (null? keys)
          (reverse acc)
          (let* ([c (car keys)]
                 [inf (hash-ref h c)])
            (if (= (info-total inf) max-total)
                (loop (cdr keys) (cons (list c (info-best-id inf)) acc))
                (loop (cdr keys) acc)))))))
```

## Erlang

```erlang
-spec most_popular_creator(Creators :: [unicode:unicode_binary()], Ids :: [unicode:unicode_binary()], Views :: [integer()]) -> [[unicode:unicode_binary()]].
most_popular_creator(Creators, Ids, Views) ->
    Pairs = lists:zip3(Creators, Ids, Views),
    CreatorMap = lists:foldl(
        fun({C, I, V}, Map) ->
            Info = maps:get(C, Map, #{total => 0, best_view => -1, best_id => <<>>}),
            Total = maps:get(total, Info) + V,
            BestView = maps:get(best_view, Info),
            BestId = maps:get(best_id, Info),
            {NewBestView, NewBestId} =
                if
                    V > BestView ->
                        {V, I};
                    V == BestView ->
                        case binary:compare(I, BestId) of
                            lt -> {V, I};
                            _  -> {BestView, BestId}
                        end;
                    true ->
                        {BestView, BestId}
                end,
            NewInfo = Info#{total => Total, best_view => NewBestView, best_id => NewBestId},
            maps:put(C, NewInfo, Map)
        end,
        #{},
        Pairs
    ),
    MaxTotal = maps:fold(fun(_C, #{total := T}, Acc) -> max(T, Acc) end, 0, CreatorMap),
    [ [Creator, BestId] ||
        {Creator, #{total := T, best_id := BestId}} <- maps:to_list(CreatorMap),
        T =:= MaxTotal
    ].
```

## Elixir

```elixir
defmodule Solution do
  @spec most_popular_creator(creators :: [String.t()], ids :: [String.t()], views :: [integer]) :: [[String.t()]]
  def most_popular_creator(creators, ids, views) do
    {total_map, best_map} =
      Enum.zip([creators, ids, views])
      |> Enum.reduce({%{}, %{}}, fn {creator, id, view}, {tot_acc, best_acc} ->
        # update total popularity
        new_total = Map.get(tot_acc, creator, 0) + view
        tot_acc = Map.put(tot_acc, creator, new_total)

        # update most viewed video for the creator
        new_best =
          case Map.get(best_acc, creator) do
            nil ->
              {view, id}

            {cur_view, cur_id} ->
              cond do
                view > cur_view ->
                  {view, id}

                view == cur_view and String.compare(id, cur_id) == :lt ->
                  {view, id}

                true ->
                  {cur_view, cur_id}
              end
          end

        best_acc = Map.put(best_acc, creator, new_best)
        {tot_acc, best_acc}
      end)

    max_total = total_map |> Map.values() |> Enum.max()

    for {creator, total} <- total_map, total == max_total do
      {_view, best_id} = Map.fetch!(best_map, creator)
      [creator, best_id]
    end
  end
end
```
