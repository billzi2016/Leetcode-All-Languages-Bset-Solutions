# 3143. Maximum Points Inside the Square

## Cpp

```cpp
class Solution {
public:
    int maxPointsInsideSquare(vector<vector<int>>& points, string s) {
        int n = points.size();
        using ll = long long;
        vector<pair<ll,int>> order;
        order.reserve(n);
        for (int i = 0; i < n; ++i) {
            ll x = points[i][0];
            ll y = points[i][1];
            ll d = max(std::llabs(x), std::llabs(y));
            order.emplace_back(d, i);
        }
        sort(order.begin(), order.end(),
             [](const pair<ll,int>& a, const pair<ll,int>& b){ return a.first < b.first; });
        
        unordered_set<char> seen;
        int count = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && order[j].first == order[i].first) ++j;
            
            bool bad = false;
            unordered_set<char> group;
            for (int k = i; k < j; ++k) {
                char c = s[order[k].second];
                if (seen.count(c) || group.count(c)) {
                    bad = true;
                    break;
                }
                group.insert(c);
            }
            if (bad) break;
            
            // add group tags to seen
            for (char c : group) {
                seen.insert(c);
                ++count;
            }
            i = j;
        }
        return count;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxPointsInsideSquare(int[][] points, String s) {
        int n = points.length;
        long[] d = new long[n];
        for (int i = 0; i < n; i++) {
            long x = Math.abs((long) points[i][0]);
            long y = Math.abs((long) points[i][1]);
            d[i] = Math.max(x, y);
        }
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Long.compare(d[a], d[b]));

        HashSet<Character> seen = new HashSet<>();
        int i = 0;
        while (i < n) {
            long curD = d[idx[i]];
            int j = i;
            boolean conflict = false;
            HashSet<Character> groupSet = new HashSet<>();
            while (j < n && d[idx[j]] == curD) {
                char tag = s.charAt(idx[j]);
                if (seen.contains(tag) || !groupSet.add(tag)) {
                    conflict = true;
                    break;
                }
                j++;
            }
            if (conflict) break;
            for (int k = i; k < j; k++) {
                seen.add(s.charAt(idx[k]));
            }
            i = j;
        }
        return seen.size();
    }
}
```

## Python

```python
class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        """
        :type points: List[List[int]]
        :type s: str
        :rtype: int
        """
        n = len(points)
        arr = []
        for i in range(n):
            x, y = points[i]
            r = max(abs(x), abs(y))
            arr.append((r, s[i]))
        arr.sort(key=lambda x: x[0])
        
        seen = set()
        count = 0
        i = 0
        while i < n:
            cur_r = arr[i][0]
            # collect group with same r
            j = i
            group_tags = []
            conflict = False
            while j < n and arr[j][0] == cur_r:
                tag = arr[j][1]
                if tag in seen:
                    conflict = True
                    break
                group_tags.append(tag)
                j += 1
            if conflict:
                break
            # check duplicates within the group itself
            if len(set(group_tags)) != len(group_tags):
                break
            # add group tags to seen
            for tag in group_tags:
                seen.add(tag)
            count += len(group_tags)
            i = j
        return count
```

## Python3

```python
class Solution:
    def maxPointsInsideSquare(self, points, s):
        n = len(points)
        arr = [(max(abs(x), abs(y)), ch) for (x, y), ch in zip(points, s)]
        arr.sort(key=lambda x: x[0])
        seen = set()
        i = 0
        ans = 0
        while i < n:
            d = arr[i][0]
            group_tags = []
            j = i
            dup_in_group = False
            while j < n and arr[j][0] == d:
                tag = arr[j][1]
                if tag in group_tags:
                    dup_in_group = True
                    break
                group_tags.append(tag)
                j += 1
            if dup_in_group:
                break
            # check intersection with seen
            conflict = False
            for tag in group_tags:
                if tag in seen:
                    conflict = True
                    break
            if conflict:
                break
            # add group tags to seen
            for tag in group_tags:
                seen.add(tag)
            ans = len(seen)
            i = j
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long d;
    char tag;
} Item;

static int cmpItem(const void *a, const void *b) {
    long long da = ((const Item *)a)->d;
    long long db = ((const Item *)b)->d;
    if (da < db) return -1;
    if (da > db) return 1;
    return 0;
}

int maxPointsInsideSquare(int** points, int pointsSize, int* pointsColSize, char* s) {
    if (pointsSize == 0) return 0;
    Item *arr = (Item *)malloc(sizeof(Item) * pointsSize);
    for (int i = 0; i < pointsSize; ++i) {
        long long x = points[i][0];
        long long y = points[i][1];
        long long adx = x >= 0 ? x : -x;
        long long ady = y >= 0 ? y : -y;
        long long d = adx > ady ? adx : ady; // max(|x|,|y|)
        arr[i].d = d;
        arr[i].tag = s[i];
    }
    qsort(arr, pointsSize, sizeof(Item), cmpItem);
    
    unsigned int seenMask = 0;
    int count = 0;
    int i = 0;
    while (i < pointsSize) {
        long long curD = arr[i].d;
        unsigned int groupMask = 0;
        int j = i;
        // process all items with same distance
        while (j < pointsSize && arr[j].d == curD) {
            int bit = 1 << (arr[j].tag - 'a');
            if ((seenMask & bit) || (groupMask & bit)) {
                free(arr);
                return count; // conflict found, cannot include this group
            }
            groupMask |= bit;
            ++j;
        }
        // no conflicts in this group, add them
        seenMask |= groupMask;
        count += (j - i);
        i = j;
    }
    free(arr);
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxPointsInsideSquare(int[][] points, string s) {
        int n = points.Length;
        var arr = new (long d, int idx)[n];
        for (int i = 0; i < n; i++) {
            long x = Math.Abs((long)points[i][0]);
            long y = Math.Abs((long)points[i][1]);
            long d = Math.Max(x, y);
            arr[i] = (d, i);
        }
        Array.Sort(arr, (a, b) => a.d.CompareTo(b.d));

        var seen = new HashSet<char>();
        int count = 0;
        int i = 0;
        while (i < n) {
            long curD = arr[i].d;
            int j = i;
            while (j < n && arr[j].d == curD) j++;

            bool conflict = false;
            var groupSeen = new HashSet<char>();
            for (int k = i; k < j; k++) {
                char tag = s[arr[k].idx];
                if (seen.Contains(tag) || groupSeen.Contains(tag)) {
                    conflict = true;
                    break;
                }
                groupSeen.Add(tag);
            }

            if (conflict) {
                return count;
            }

            foreach (char ch in groupSeen) {
                seen.Add(ch);
            }
            count += (j - i);
            i = j;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @param {string} s
 * @return {number}
 */
var maxPointsInsideSquare = function(points, s) {
    const n = points.length;
    const arr = new Array(n);
    for (let i = 0; i < n; ++i) {
        const x = points[i][0];
        const y = points[i][1];
        const d = Math.max(Math.abs(x), Math.abs(y));
        arr[i] = [d, s.charCodeAt(i)];
    }
    arr.sort((a, b) => a[0] - b[0]);
    const seen = new Set();
    let cnt = 0;
    for (let i = 0; i < n; ++i) {
        const tag = arr[i][1];
        if (seen.has(tag)) break;
        seen.add(tag);
        ++cnt;
    }
    return cnt;
};
```

## Typescript

```typescript
function maxPointsInsideSquare(points: number[][], s: string): number {
    const n = points.length;
    const arr: { d: number; tag: string }[] = new Array(n);
    for (let i = 0; i < n; i++) {
        const x = points[i][0];
        const y = points[i][1];
        const d = Math.max(Math.abs(x), Math.abs(y));
        arr[i] = { d, tag: s[i] };
    }
    arr.sort((a, b) => a.d - b.d);
    const seen = new Set<string>();
    let i = 0;
    while (i < n) {
        const curD = arr[i].d;
        const groupTags: string[] = [];
        let j = i;
        while (j < n && arr[j].d === curD) {
            groupTags.push(arr[j].tag);
            j++;
        }
        // check duplicates within the same distance group
        const groupSet = new Set<string>();
        for (const tag of groupTags) {
            if (groupSet.has(tag)) return seen.size;
            groupSet.add(tag);
        }
        // check conflict with previously included tags
        for (const tag of groupTags) {
            if (seen.has(tag)) return seen.size;
        }
        // add current group's tags to the global set
        for (const tag of groupTags) seen.add(tag);
        i = j;
    }
    return seen.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param String $s
     * @return Integer
     */
    function maxPointsInsideSquare($points, $s) {
        $n = count($points);
        $arr = [];
        for ($i = 0; $i < $n; ++$i) {
            $x = $points[$i][0];
            $y = $points[$i][1];
            $d = max(abs($x), abs($y));
            $arr[] = [$d, $s[$i]];
        }
        usort($arr, function($a, $b) {
            if ($a[0] == $b[0]) return 0;
            return ($a[0] < $b[0]) ? -1 : 1;
        });

        $seen = [];
        $count = 0;
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $currD = $arr[$i][0];
            // collect tags in this group
            $groupTags = [];
            $j = $i;
            while ($j < $n && $arr[$j][0] == $currD) {
                $tag = $arr[$j][1];
                $groupTags[] = $tag;
                $j++;
            }
            // check for duplicates with previously seen tags
            $invalid = false;
            foreach ($groupTags as $tag) {
                if (isset($seen[$tag])) {
                    $invalid = true;
                    break;
                }
            }
            if (!$invalid) {
                // also check duplicates within the group itself
                $freq = [];
                foreach ($groupTags as $tag) {
                    if (isset($freq[$tag])) {
                        $invalid = true;
                        break;
                    }
                    $freq[$tag] = 1;
                }
            }
            if ($invalid) {
                // cannot include this distance, stop
                $ans = max($ans, $count);
                break;
            }
            // safe to add all tags in group
            foreach ($groupTags as $tag) {
                $seen[$tag] = true;
            }
            $count += count($groupTags);
            $i = $j;
        }
        $ans = max($ans, $count); // if loop finished without break
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxPointsInsideSquare(_ points: [[Int]], _ s: String) -> Int {
        let n = points.count
        var order = [(d: Int, idx: Int)]()
        order.reserveCapacity(n)
        for (i, p) in points.enumerated() {
            let x = p[0]
            let y = p[1]
            let d = max(abs(x), abs(y))
            order.append((d, i))
        }
        order.sort { $0.d < $1.d }
        let tags = Array(s)
        var seen = Set<Character>()
        var count = 0
        for item in order {
            let ch = tags[item.idx]
            if seen.contains(ch) {
                break
            }
            seen.insert(ch)
            count += 1
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPointsInsideSquare(points: Array<IntArray>, s: String): Int {
        val n = points.size
        val INF = Long.MAX_VALUE
        val first = LongArray(26) { INF }
        val second = LongArray(26) { INF }

        for (i in 0 until n) {
            val x = points[i][0]
            val y = points[i][1]
            val d = maxOf(kotlin.math.abs(x), kotlin.math.abs(y)).toLong()
            val idx = s[i] - 'a'
            if (d < first[idx]) {
                second[idx] = first[idx]
                first[idx] = d
            } else if (d < second[idx]) {
                second[idx] = d
            }
        }

        var limit = INF
        for (c in 0 until 26) {
            if (second[c] != INF && second[c] < limit) {
                limit = second[c]
            }
        }

        if (limit == INF) return n

        var ans = 0
        for (i in 0 until n) {
            val x = points[i][0]
            val y = points[i][1]
            val d = maxOf(kotlin.math.abs(x), kotlin.math.abs(y)).toLong()
            if (d < limit) ans++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxPointsInsideSquare(List<List<int>> points, String s) {
    int n = points.length;
    List<_Item> items = List.generate(n, (i) {
      int x = points[i][0];
      int y = points[i][1];
      int d = x.abs() > y.abs() ? x.abs() : y.abs();
      return _Item(d, s.codeUnitAt(i) - 97);
    });
    items.sort((a, b) => a.d.compareTo(b.d));

    List<bool> seen = List.filled(26, false);
    int ans = 0;
    int i = 0;
    while (i < n) {
      int curD = items[i].d;
      List<bool> groupSeen = List.filled(26, false);
      bool dup = false;
      int j = i;
      while (j < n && items[j].d == curD) {
        int tag = items[j].tag;
        if (seen[tag] || groupSeen[tag]) {
          dup = true;
          break;
        }
        groupSeen[tag] = true;
        j++;
      }
      if (dup) break;
      for (int k = i; k < j; k++) {
        seen[items[k].tag] = true;
      }
      ans += (j - i);
      i = j;
    }
    return ans;
  }
}

class _Item {
  int d;
  int tag;
  _Item(this.d, this.tag);
}
```

## Golang

```go
import "sort"

func maxPointsInsideSquare(points [][]int, s string) int {
	type item struct {
		d   int64
		tag byte
	}
	n := len(points)
	arr := make([]item, n)
	for i := 0; i < n; i++ {
		x, y := points[i][0], points[i][1]
		if x < 0 {
			x = -x
		}
		if y < 0 {
			y = -y
		}
		var d int64
		if x > y {
			d = int64(x)
		} else {
			d = int64(y)
		}
		arr[i] = item{d: d, tag: s[i]}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].d < arr[j].d })

	var seen [26]bool
	count := 0
	for i := 0; i < n; {
		j := i + 1
		for j < n && arr[j].d == arr[i].d {
			j++
		}
		var localSeen [26]bool
		conflict := false
		for k := i; k < j; k++ {
			idx := arr[k].tag - 'a'
			if seen[idx] || localSeen[idx] {
				conflict = true
				break
			}
			localSeen[idx] = true
		}
		if conflict {
			break
		}
		for k := i; k < j; k++ {
			idx := arr[k].tag - 'a'
			seen[idx] = true
		}
		count += j - i
		i = j
	}
	return count
}
```

## Ruby

```ruby
def max_points_inside_square(points, s)
  n = points.length
  arr = Array.new(n) do |i|
    x, y = points[i]
    d = 2 * [x.abs, y.abs].max
    [d, s[i]]
  end

  arr.sort_by! { |pair| pair[0] }

  seen = {}
  count = 0
  i = 0
  while i < n
    j = i
    while j < n && arr[j][0] == arr[i][0]
      j += 1
    end

    conflict = false
    group_tags = {}

    (i...j).each do |k|
      tag = arr[k][1]
      if seen.key?(tag) || group_tags.key?(tag)
        conflict = true
        break
      else
        group_tags[tag] = true
      end
    end

    break if conflict

    (i...j).each do |k|
      tag = arr[k][1]
      seen[tag] = true
      count += 1
    end

    i = j
  end

  count
end
```

## Scala

```scala
object Solution {
    def maxPointsInsideSquare(points: Array[Array[Int]], s: String): Int = {
        val n = points.length
        val lists = Array.fill(26)(new scala.collection.mutable.ArrayBuffer[Long]())
        var i = 0
        while (i < n) {
            val x = points(i)(0).toLong
            val y = points(i)(1).toLong
            val L = 2L * math.max(math.abs(x), math.abs(y))
            val idx = s.charAt(i) - 'a'
            lists(idx) += L
            i += 1
        }
        var limit = Long.MaxValue
        val minVals = new Array[Long](26)
        java.util.Arrays.fill(minVals, Long.MaxValue)

        for (c <- 0 until 26) {
            val arr = lists(c)
            if (!arr.isEmpty) {
                var min1 = Long.MaxValue
                var min2 = Long.MaxValue
                var j = 0
                while (j < arr.size) {
                    val v = arr(j)
                    if (v < min1) {
                        min2 = min1
                        min1 = v
                    } else if (v < min2) {
                        min2 = v
                    }
                    j += 1
                }
                minVals(c) = min1
                if (min2 != Long.MaxValue) {
                    limit = math.min(limit, min2)
                }
            }
        }

        var ans = 0
        for (c <- 0 until 26) {
            val v = minVals(c)
            if (v != Long.MaxValue && v < limit) ans += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn max_points_inside_square(points: Vec<Vec<i32>>, s: String) -> i32 {
        let n = points.len();
        if n == 0 {
            return 0;
        }
        // (distance, tag)
        let mut data: Vec<(i64, u8)> = Vec::with_capacity(n);
        for (i, p) in points.iter().enumerate() {
            let x = p[0] as i64;
            let y = p[1] as i64;
            let d = std::cmp::max(x.abs(), y.abs());
            let tag = s.as_bytes()[i];
            data.push((d, tag));
        }
        data.sort_by_key(|k| k.0);
        let mut seen: HashSet<u8> = HashSet::new();
        let mut count: usize = 0;
        let mut i = 0usize;
        while i < n {
            let cur_d = data[i].0;
            let mut group_set: HashSet<u8> = HashSet::new();
            let mut j = i;
            while j < n && data[j].0 == cur_d {
                let tag = data[j].1;
                if seen.contains(&tag) || group_set.contains(&tag) {
                    return count as i32;
                }
                group_set.insert(tag);
                j += 1;
            }
            // add group's tags to global set
            for &tag in group_set.iter() {
                seen.insert(tag);
            }
            count += j - i;
            i = j;
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (max-points-inside-square points s)
  (-> (listof (listof exact-integer?)) string? exact-integer?)
  (let* ((pairs
          (let loop ((i 0) (lst points) (acc '()))
            (if (null? lst)
                (reverse acc)
                (let* ((pt (car lst))
                       (x (first pt))
                       (y (second pt))
                       (d (max (abs x) (abs y)))
                       (ch (string-ref s i)))
                  (loop (+ i 1) (cdr lst) (cons (cons d ch) acc))))))
         (sorted-pairs (sort pairs (lambda (a b) (< (car a) (car b)))))
         (seen (make-hash)))
    (let recur ((lst sorted-pairs) (cnt 0))
      (if (null? lst)
          cnt
          (let* ((curr-d (car (car lst))))
            (define-values (rest group)
              (let loop2 ((rem lst) (g '()))
                (if (or (null? rem) (not (= (car (car rem)) curr-d)))
                    (values rem (reverse g))
                    (loop2 (cdr rem) (cons (car rem) g)))))
            (let ((conflict #f)
                  (temp (make-hash)))
              (for ([p group])
                (define ch (cdr p))
                (when (or (hash-has-key? seen ch) (hash-has-key? temp ch))
                  (set! conflict #t))
                (hash-set! temp ch #t))
              (if conflict
                  cnt
                  (begin
                    (for ([p group])
                      (hash-set! seen (cdr p) #t))
                    (recur rest (+ cnt (length group)))))))))))
```

## Erlang

```erlang
-spec max_points_inside_square(Points :: [[integer()]], S :: unicode:unicode_binary()) -> integer().
max_points_inside_square(Points, S) ->
    Tags = binary_to_list(S),
    Pairs = lists:zip(Points, Tags),
    DTagList = [ {calc_d(Point), Tag} || {Point, Tag} <- Pairs ],
    Sorted = lists:keysort(1, DTagList),
    process_sorted(Sorted, #{}, 0).

calc_d([X, Y]) ->
    AbsX = erlang:abs(X),
    AbsY = erlang:abs(Y),
    if AbsX >= AbsY -> AbsX; true -> AbsY end.

process_sorted([], _Seen, Count) -> Count;
process_sorted([{D,_}|_] = List, Seen, Count) ->
    {Group, Rest} = take_same_d(List, D, []),
    case group_valid(Group, Seen) of
        true ->
            NewSeen = add_group_tags(Group, Seen),
            process_sorted(Rest, NewSeen, Count + length(Group));
        false ->
            Count
    end.

take_same_d([], _D, Acc) -> {lists:reverse(Acc), []};
take_same_d([{D1,_}=H|T], D, Acc) when D1 =:= D ->
    take_same_d(T, D, [H|Acc]);
take_same_d(Rest, _D, Acc) -> {lists:reverse(Acc), Rest}.

group_valid(Group, Seen) ->
    group_valid(Group, Seen, #{}).

group_valid([], _Seen, _Local) -> true;
group_valid([{_,Tag}|Rest], Seen, Local) ->
    case maps:is_key(Tag, Seen) orelse maps:is_key(Tag, Local) of
        true -> false;
        false -> group_valid(Rest, Seen, maps:put(Tag, true, Local))
    end.

add_group_tags(Group, Seen) ->
    lists:foldl(fun({_,Tag}, Acc) -> maps:put(Tag, true, Acc) end, Seen, Group).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_points_inside_square(points :: [[integer]], s :: String.t) :: integer
  def max_points_inside_square(points, s) do
    tags = String.to_charlist(s)

    data =
      Enum.with_index(points)
      |> Enum.map(fn {pt, idx} ->
        [x, y] = pt
        r = max(abs(x), abs(y))
        {r, Enum.at(tags, idx)}
      end)

    sorted = Enum.sort_by(data, fn {r, _} -> r end)

    groups = Enum.chunk_by(sorted, fn {r, _} -> r end)

    {result, _} =
      Enum.reduce_while(groups, {0, MapSet.new()}, fn group, {cnt, set} ->
        group_tags = Enum.map(group, fn {_r, t} -> t end)

        dup_within = length(group_tags) != MapSet.size(MapSet.new(group_tags))
        conflict = dup_within or Enum.any?(group_tags, &MapSet.member?(set, &1))

        if conflict do
          {:halt, {cnt, set}}
        else
          new_set = Enum.reduce(group_tags, set, fn t, acc -> MapSet.put(acc, t) end)
          {:cont, {cnt + length(group), new_set}}
        end
      end)

    result
  end
end
```
