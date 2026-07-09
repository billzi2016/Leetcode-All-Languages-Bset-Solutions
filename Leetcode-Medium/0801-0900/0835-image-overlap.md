# 0835. Image Overlap

## Cpp

```cpp
class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        vector<pair<int,int>> ones1, ones2;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (img1[i][j] == 1) ones1.emplace_back(i, j);
                if (img2[i][j] == 1) ones2.emplace_back(i, j);
            }
        }
        int ans = 0;
        unordered_map<long long,int> cnt;
        for (auto &p : ones1) {
            for (auto &q : ones2) {
                int dx = p.first - q.first;
                int dy = p.second - q.second;
                long long key = (static_cast<long long>(dx) << 32) ^ (dy & 0xffffffffLL);
                ans = max(ans, ++cnt[key]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        int n = img1.length;
        List<int[]> ones1 = new ArrayList<>();
        List<int[]> ones2 = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (img1[i][j] == 1) ones1.add(new int[]{i, j});
                if (img2[i][j] == 1) ones2.add(new int[]{i, j});
            }
        }
        Map<Integer, Integer> freq = new HashMap<>();
        int maxOverlap = 0;
        for (int[] p1 : ones1) {
            for (int[] p2 : ones2) {
                int dx = p1[0] - p2[0];
                int dy = p1[1] - p2[1];
                // Encode translation vector into a single integer key.
                int key = (dx + 30) * 61 + (dy + 30);
                int cnt = freq.getOrDefault(key, 0) + 1;
                freq.put(key, cnt);
                if (cnt > maxOverlap) {
                    maxOverlap = cnt;
                }
            }
        }
        return maxOverlap;
    }
}
```

## Python

```python
class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not ones1 or not ones2:
            return 0

        offset_count = {}
        max_overlap = 0
        for x1, y1 in ones1:
            for x2, y2 in ones2:
                dx = x1 - x2
                dy = y1 - y2
                key = (dx, dy)
                cnt = offset_count.get(key, 0) + 1
                offset_count[key] = cnt
                if cnt > max_overlap:
                    max_overlap = cnt

        return max_overlap
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not ones1 or not ones2:
            return 0

        offset_count = defaultdict(int)
        max_overlap = 0
        for x1, y1 in ones1:
            for x2, y2 in ones2:
                dx = x1 - x2
                dy = y1 - y2
                offset_count[(dx, dy)] += 1
                if offset_count[(dx, dy)] > max_overlap:
                    max_overlap = offset_count[(dx, dy)]
        return max_overlap
```

## C

```c
#include <stdlib.h>
#include <string.h>

int largestOverlap(int** img1, int img1Size, int* img1ColSize,
                   int** img2, int img2Size, int* img2ColSize) {
    int n = img1Size;
    int maxCells = n * n;

    int *p1x = (int *)malloc(maxCells * sizeof(int));
    int *p1y = (int *)malloc(maxCells * sizeof(int));
    int *p2x = (int *)malloc(maxCells * sizeof(int));
    int *p2y = (int *)malloc(maxCells * sizeof(int));

    int cnt1 = 0, cnt2 = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < img1ColSize[i]; ++j) {
            if (img1[i][j] == 1) {
                p1x[cnt1] = i;
                p1y[cnt1] = j;
                ++cnt1;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < img2ColSize[i]; ++j) {
            if (img2[i][j] == 1) {
                p2x[cnt2] = i;
                p2y[cnt2] = j;
                ++cnt2;
            }
        }
    }

    if (cnt1 == 0 || cnt2 == 0) {
        free(p1x); free(p1y);
        free(p2x); free(p2y);
        return 0;
    }

    int offset = n;                     // shift range [-n+1, n-1] fits in [ -n , n ]
    int dim = 2 * n + 1;                // size enough for all possible shifts
    int **freq = (int **)malloc(dim * sizeof(int *));
    for (int i = 0; i < dim; ++i) {
        freq[i] = (int *)calloc(dim, sizeof(int));
    }

    int best = 0;
    for (int i = 0; i < cnt1; ++i) {
        for (int j = 0; j < cnt2; ++j) {
            int dx = p2x[j] - p1x[i];
            int dy = p2y[j] - p1y[i];
            int ix = dx + offset;
            int iy = dy + offset;
            ++freq[ix][iy];
            if (freq[ix][iy] > best) best = freq[ix][iy];
        }
    }

    for (int i = 0; i < dim; ++i) free(freq[i]);
    free(freq);
    free(p1x); free(p1y);
    free(p2x); free(p2y);
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int LargestOverlap(int[][] img1, int[][] img2)
    {
        int n = img1.Length;
        var ones1 = new List<(int x, int y)>();
        var ones2 = new List<(int x, int y)>();

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (img1[i][j] == 1)
                    ones1.Add((i, j));
                if (img2[i][j] == 1)
                    ones2.Add((i, j));
            }
        }

        if (ones1.Count == 0 || ones2.Count == 0)
            return 0;

        var dict = new Dictionary<(int dx, int dy), int>();
        int maxOverlap = 0;

        foreach (var p in ones1)
        {
            foreach (var q in ones2)
            {
                int dx = p.x - q.x;
                int dy = p.y - q.y;
                var key = (dx, dy);
                if (dict.ContainsKey(key))
                    dict[key]++;
                else
                    dict[key] = 1;

                if (dict[key] > maxOverlap)
                    maxOverlap = dict[key];
            }
        }

        return maxOverlap;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} img1
 * @param {number[][]} img2
 * @return {number}
 */
var largestOverlap = function(img1, img2) {
    const n = img1.length;
    const ones1 = [];
    const ones2 = [];
    
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (img1[i][j] === 1) ones1.push([i, j]);
            if (img2[i][j] === 1) ones2.push([i, j]);
        }
    }
    
    if (ones1.length === 0 || ones2.length === 0) return 0;
    
    const map = new Map();
    let maxOverlap = 0;
    
    for (const [x1, y1] of ones1) {
        for (const [x2, y2] of ones2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            const key = `${dx},${dy}`;
            const cnt = (map.get(key) || 0) + 1;
            map.set(key, cnt);
            if (cnt > maxOverlap) maxOverlap = cnt;
        }
    }
    
    return maxOverlap;
};
```

## Typescript

```typescript
function largestOverlap(img1: number[][], img2: number[][]): number {
    const n = img1.length;
    const ones1: [number, number][] = [];
    const ones2: [number, number][] = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (img1[i][j] === 1) ones1.push([i, j]);
            if (img2[i][j] === 1) ones2.push([i, j]);
        }
    }

    if (ones1.length === 0 || ones2.length === 0) return 0;

    const shiftCount = new Map<string, number>();
    let maxOverlap = 0;

    for (const [x1, y1] of ones1) {
        for (const [x2, y2] of ones2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            const key = `${dx},${dy}`;
            const cnt = (shiftCount.get(key) ?? 0) + 1;
            shiftCount.set(key, cnt);
            if (cnt > maxOverlap) maxOverlap = cnt;
        }
    }

    return maxOverlap;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $img1
     * @param Integer[][] $img2
     * @return Integer
     */
    function largestOverlap($img1, $img2) {
        $n = count($img1);
        $ones1 = [];
        $ones2 = [];

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($img1[$i][$j] == 1) {
                    $ones1[] = [$i, $j];
                }
                if ($img2[$i][$j] == 1) {
                    $ones2[] = [$i, $j];
                }
            }
        }

        $maxOverlap = 0;
        $counter = [];

        foreach ($ones1 as $p1) {
            foreach ($ones2 as $p2) {
                $dx = $p2[0] - $p1[0];
                $dy = $p2[1] - $p1[1];
                $key = $dx . ',' . $dy;
                if (!isset($counter[$key])) {
                    $counter[$key] = 0;
                }
                $counter[$key]++;
                if ($counter[$key] > $maxOverlap) {
                    $maxOverlap = $counter[$key];
                }
            }
        }

        return $maxOverlap;
    }
}
```

## Swift

```swift
struct Offset: Hashable {
    let x: Int
    let y: Int
}

class Solution {
    func largestOverlap(_ img1: [[Int]], _ img2: [[Int]]) -> Int {
        let n = img1.count
        var ones1 = [(Int, Int)]()
        var ones2 = [(Int, Int)]()
        
        for i in 0..<n {
            for j in 0..<n {
                if img1[i][j] == 1 { ones1.append((i, j)) }
                if img2[i][j] == 1 { ones2.append((i, j)) }
            }
        }
        
        var offsetCount = [Offset: Int]()
        var maxOverlap = 0
        
        for (x1, y1) in ones1 {
            for (x2, y2) in ones2 {
                let off = Offset(x: x1 - x2, y: y1 - y2)
                let newCount = (offsetCount[off] ?? 0) + 1
                offsetCount[off] = newCount
                if newCount > maxOverlap {
                    maxOverlap = newCount
                }
            }
        }
        
        return maxOverlap
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestOverlap(img1: Array<IntArray>, img2: Array<IntArray>): Int {
        val n = img1.size
        val ones1 = mutableListOf<Pair<Int, Int>>()
        val ones2 = mutableListOf<Pair<Int, Int>>()
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (img1[i][j] == 1) ones1.add(Pair(i, j))
                if (img2[i][j] == 1) ones2.add(Pair(i, j))
            }
        }

        val shiftCount = HashMap<Pair<Int, Int>, Int>()
        var maxOverlap = 0

        for ((x1, y1) in ones1) {
            for ((x2, y2) in ones2) {
                val dx = x1 - x2
                val dy = y1 - y2
                val key = Pair(dx, dy)
                val cnt = (shiftCount[key] ?: 0) + 1
                shiftCount[key] = cnt
                if (cnt > maxOverlap) maxOverlap = cnt
            }
        }

        return maxOverlap
    }
}
```

## Dart

```dart
class Solution {
  int largestOverlap(List<List<int>> img1, List<List<int>> img2) {
    int n = img1.length;
    List<List<int>> ones1 = [];
    List<List<int>> ones2 = [];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (img1[i][j] == 1) ones1.add([i, j]);
        if (img2[i][j] == 1) ones2.add([i, j]);
      }
    }

    Map<String, int> offsetCount = {};
    int maxOverlap = 0;

    for (var p in ones1) {
      for (var q in ones2) {
        int dx = p[0] - q[0];
        int dy = p[1] - q[1];
        String key = '$dx,$dy';
        int cnt = (offsetCount[key] ?? 0) + 1;
        offsetCount[key] = cnt;
        if (cnt > maxOverlap) maxOverlap = cnt;
      }
    }

    return maxOverlap;
  }
}
```

## Golang

```go
func largestOverlap(img1 [][]int, img2 [][]int) int {
    var ones1 [][2]int
    var ones2 [][2]int
    n := len(img1)
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if img1[i][j] == 1 {
                ones1 = append(ones1, [2]int{i, j})
            }
            if img2[i][j] == 1 {
                ones2 = append(ones2, [2]int{i, j})
            }
        }
    }

    maxOverlap := 0
    offsetCount := make(map[[2]int]int)

    for _, p1 := range ones1 {
        for _, p2 := range ones2 {
            dx := p1[0] - p2[0]
            dy := p1[1] - p2[1]
            key := [2]int{dx, dy}
            offsetCount[key]++
            if offsetCount[key] > maxOverlap {
                maxOverlap = offsetCount[key]
            }
        }
    }

    return maxOverlap
}
```

## Ruby

```ruby
def largest_overlap(img1, img2)
  n = img1.size
  ones1 = []
  ones2 = []

  (0...n).each do |i|
    (0...n).each do |j|
      ones1 << [i, j] if img1[i][j] == 1
      ones2 << [i, j] if img2[i][j] == 1
    end
  end

  return 0 if ones1.empty? || ones2.empty?

  shift_count = Hash.new(0)
  max_overlap = 0

  ones1.each do |x1, y1|
    ones2.each do |x2, y2|
      dx = x1 - x2
      dy = y1 - y2
      key = [dx, dy]
      shift_count[key] += 1
      max_overlap = shift_count[key] if shift_count[key] > max_overlap
    end
  end

  max_overlap
end
```

## Scala

```scala
object Solution {
    def largestOverlap(img1: Array[Array[Int]], img2: Array[Array[Int]]): Int = {
        val n = img1.length
        val ones1 = scala.collection.mutable.ArrayBuffer[(Int, Int)]()
        val ones2 = scala.collection.mutable.ArrayBuffer[(Int, Int)]()

        for (i <- 0 until n; j <- 0 until n) {
            if (img1(i)(j) == 1) ones1.append((i, j))
            if (img2(i)(j) == 1) ones2.append((i, j))
        }

        val shiftCount = scala.collection.mutable.Map[(Int, Int), Int]()
        var maxOverlap = 0

        for ((x1, y1) <- ones1; (x2, y2) <- ones2) {
            val dx = x2 - x1
            val dy = y2 - y1
            val key = (dx, dy)
            val cnt = shiftCount.getOrElse(key, 0) + 1
            shiftCount.update(key, cnt)
            if (cnt > maxOverlap) maxOverlap = cnt
        }

        maxOverlap
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_overlap(img1: Vec<Vec<i32>>, img2: Vec<Vec<i32>>) -> i32 {
        let n = img1.len();
        let mut ones1 = Vec::new();
        let mut ones2 = Vec::new();

        for i in 0..n {
            for j in 0..n {
                if img1[i][j] == 1 {
                    ones1.push((i as i32, j as i32));
                }
                if img2[i][j] == 1 {
                    ones2.push((i as i32, j as i32));
                }
            }
        }

        use std::collections::HashMap;
        let mut count: HashMap<(i32, i32), i32> = HashMap::new();
        let mut max_overlap = 0;

        for &(x1, y1) in &ones1 {
            for &(x2, y2) in &ones2 {
                let dx = x2 - x1;
                let dy = y2 - y1;
                let entry = count.entry((dx, dy)).or_insert(0);
                *entry += 1;
                if *entry > max_overlap {
                    max_overlap = *entry;
                }
            }
        }

        max_overlap
    }
}
```

## Racket

```racket
(define/contract (largest-overlap img1 img2)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ((n (length img1))
         (coords1
          (for/list ([i (in-range n)]
                     [j (in-range n)]
                     #:when (= (list-ref (list-ref img1 i) j) 1))
            (cons i j)))
         (coords2
          (for/list ([i (in-range n)]
                     [j (in-range n)]
                     #:when (= (list-ref (list-ref img2 i) j) 1))
            (cons i j))))
    (if (or (null? coords1) (null? coords2))
        0
        (let ((h (make-hash)))
          (for* ([p coords1] [q coords2])
            (define dx (- (car q) (car p)))
            (define dy (- (cdr q) (cdr p)))
            (define key (cons dx dy))
            (hash-set! h key (+ 1 (hash-ref h key 0))))
          (let ((max-val 0))
            (for ([v (in-hash-values h)])
              (when (> v max-val)
                (set! max-val v)))
            max-val)))))
```

## Erlang

```erlang
-module(solution).
-export([largest_overlap/2]).

-spec largest_overlap(Img1 :: [[integer()]], Img2 :: [[integer()]]) -> integer().
largest_overlap(Img1, Img2) ->
    N = length(Img1),
    List1 = coords_of_ones(Img1, 0),
    Set2 = set_of_ones(Img2, 0),
    Shifts = lists:seq(-N + 1, N - 1),
    compute_max(Shifts, Shifts, List1, Set2, N, 0).

coords_of_ones([], _RowIdx) -> [];
coords_of_ones([Row | Rest], RowIdx) ->
    Cols = cols_of_row(Row, RowIdx, 0),
    Cols ++ coords_of_ones(Rest, RowIdx + 1).

cols_of_row([], _RowIdx, _ColIdx) -> [];
cols_of_row([Val | Rest], RowIdx, ColIdx) ->
    Tail = cols_of_row(Rest, RowIdx, ColIdx + 1),
    case Val of
        1 -> [{RowIdx, ColIdx} | Tail];
        _ -> Tail
    end.

set_of_ones(Matrix, RowIdx) ->
    set_of_ones(Matrix, RowIdx, sets:new()).

set_of_ones([], _RowIdx, Set) -> Set;
set_of_ones([Row | Rest], RowIdx, Set0) ->
    Set1 = add_row_ones(Row, RowIdx, 0, Set0),
    set_of_ones(Rest, RowIdx + 1, Set1).

add_row_ones([], _RowIdx, _ColIdx, Set) -> Set;
add_row_ones([Val | Rest], RowIdx, ColIdx, Set0) ->
    Set1 = case Val of
        1 -> sets:add_element({RowIdx, ColIdx}, Set0);
        _ -> Set0
    end,
    add_row_ones(Rest, RowIdx, ColIdx + 1, Set1).

compute_max([], _DyList, _List1, _Set2, _N, Max) -> Max;
compute_max([Dx | RestDx], DyList, List1, Set2, N, CurrentMax) ->
    NewMax = compute_dy(DyList, Dx, List1, Set2, N, CurrentMax),
    compute_max(RestDx, DyList, List1, Set2, N, NewMax).

compute_dy([], _Dx, _List1, _Set2, _N, Max) -> Max;
compute_dy([Dy | RestDy], Dx, List1, Set2, N, CurrentMax) ->
    Overlap = overlap_count(List1, Set2, Dx, Dy, N),
    NewMax = if Overlap > CurrentMax -> Overlap; true -> CurrentMax end,
    compute_dy(RestDy, Dx, List1, Set2, N, NewMax).

overlap_count(List1, Set2, Dx, Dy, N) ->
    overlap_count(List1, Set2, Dx, Dy, N, 0).

overlap_count([], _Set2, _Dx, _Dy, _N, Acc) -> Acc;
overlap_count([{I, J} | Rest], Set2, Dx, Dy, N, Acc) ->
    I2 = I + Dx,
    J2 = J + Dy,
    NewAcc = if
        I2 >= 0, I2 < N, J2 >= 0, J2 < N,
        sets:is_element({I2, J2}, Set2) -> Acc + 1;
        true -> Acc
    end,
    overlap_count(Rest, Set2, Dx, Dy, N, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_overlap(img1 :: [[integer]], img2 :: [[integer]]) :: integer
  def largest_overlap(img1, img2) do
    n = length(img1)

    list1 =
      Enum.with_index(img1)
      |> Enum.flat_map(fn {row, i} ->
        Enum.with_index(row)
        |> Enum.filter(fn {val, _j} -> val == 1 end)
        |> Enum.map(fn {_val, j} -> {i, j} end)
      end)

    set2 =
      Enum.with_index(img2)
      |> Enum.reduce(MapSet.new(), fn {row, i}, acc ->
        row
        |> Enum.with_index()
        |> Enum.reduce(acc, fn {val, j}, a ->
          if val == 1, do: MapSet.put(a, {i, j}), else: a
        end)
      end)

    shifts = -(n - 1)..(n - 1)

    Enum.reduce(shifts, 0, fn dx, best ->
      Enum.reduce(shifts, best, fn dy, cur_best ->
        count =
          Enum.reduce(list1, 0, fn {x, y}, c ->
            nx = x + dx
            ny = y + dy

            if MapSet.member?(set2, {nx, ny}), do: c + 1, else: c
          end)

        if count > cur_best, do: count, else: cur_best
      end)
    end)
  end
end
```
