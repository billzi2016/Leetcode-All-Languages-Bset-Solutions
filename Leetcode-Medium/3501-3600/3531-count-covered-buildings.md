# 3531. Count Covered Buildings

## Cpp

```cpp
class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        int m = buildings.size();
        vector<char> rowOk(m, 0), colOk(m, 0);
        unordered_map<int, vector<pair<int,int>>> rows;
        unordered_map<int, vector<pair<int,int>>> cols;
        rows.reserve(m * 2);
        cols.reserve(m * 2);
        for (int i = 0; i < m; ++i) {
            int x = buildings[i][0];
            int y = buildings[i][1];
            rows[x].push_back({y, i});
            cols[y].push_back({x, i});
        }
        for (auto &p : rows) {
            auto &vec = p.second;
            if (vec.size() <= 2) continue;
            sort(vec.begin(), vec.end(),
                 [](const pair<int,int>& a, const pair<int,int>& b){ return a.first < b.first; });
            for (size_t k = 1; k + 1 < vec.size(); ++k) {
                rowOk[vec[k].second] = 1;
            }
        }
        for (auto &p : cols) {
            auto &vec = p.second;
            if (vec.size() <= 2) continue;
            sort(vec.begin(), vec.end(),
                 [](const pair<int,int>& a, const pair<int,int>& b){ return a.first < b.first; });
            for (size_t k = 1; k + 1 < vec.size(); ++k) {
                colOk[vec[k].second] = 1;
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            if (rowOk[i] && colOk[i]) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countCoveredBuildings(int n, int[][] buildings) {
        java.util.Map<Integer, java.util.List<Integer>> rowMap = new java.util.HashMap<>();
        java.util.Map<Integer, java.util.List<Integer>> colMap = new java.util.HashMap<>();
        for (int[] b : buildings) {
            int x = b[0];
            int y = b[1];
            rowMap.computeIfAbsent(x, k -> new java.util.ArrayList<>()).add(y);
            colMap.computeIfAbsent(y, k -> new java.util.ArrayList<>()).add(x);
        }
        java.util.Set<Long> horiz = new java.util.HashSet<>();
        for (java.util.Map.Entry<Integer, java.util.List<Integer>> e : rowMap.entrySet()) {
            java.util.List<Integer> list = e.getValue();
            if (list.size() <= 2) continue;
            java.util.Collections.sort(list);
            int x = e.getKey();
            for (int i = 1; i < list.size() - 1; i++) {
                long key = ((long) x << 32) | (list.get(i) & 0xffffffffL);
                horiz.add(key);
            }
        }
        java.util.Set<Long> vert = new java.util.HashSet<>();
        for (java.util.Map.Entry<Integer, java.util.List<Integer>> e : colMap.entrySet()) {
            java.util.List<Integer> list = e.getValue();
            if (list.size() <= 2) continue;
            java.util.Collections.sort(list);
            int y = e.getKey();
            for (int i = 1; i < list.size() - 1; i++) {
                long key = ((long) list.get(i) << 32) | (y & 0xffffffffL);
                vert.add(key);
            }
        }
        int count = 0;
        for (int[] b : buildings) {
            long key = ((long) b[0] << 32) | (b[1] & 0xffffffffL);
            if (horiz.contains(key) && vert.contains(key)) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        m = len(buildings)
        horiz_ok = [False] * m  # has both left and right
        vert_ok = [False] * m   # has both below and above

        rows = defaultdict(list)   # y -> list of (x, idx)
        cols = defaultdict(list)   # x -> list of (y, idx)

        for idx, (x, y) in enumerate(buildings):
            rows[y].append((x, idx))
            cols[x].append((y, idx))

        # process rows for left/right
        for lst in rows.values():
            if len(lst) < 3:
                continue
            lst.sort()  # sort by x
            for i in range(1, len(lst) - 1):
                _, idx = lst[i]
                horiz_ok[idx] = True

        # process columns for below/above
        for lst in cols.values():
            if len(lst) < 3:
                continue
            lst.sort()  # sort by y
            for i in range(1, len(lst) - 1):
                _, idx = lst[i]
                vert_ok[idx] = True

        count = 0
        for i in range(m):
            if horiz_ok[i] and vert_ok[i]:
                count += 1
        return count
```

## Python3

```python
from typing import List
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        m = len(buildings)
        horiz = [False] * m
        vert = [False] * m

        # map rows (y) to list of (x, idx)
        row_map = {}
        for idx, (x, y) in enumerate(buildings):
            row_map.setdefault(y, []).append((x, idx))
        for lst in row_map.values():
            if len(lst) <= 2:
                continue
            lst.sort()
            for _, idx in lst[1:-1]:
                horiz[idx] = True

        # map columns (x) to list of (y, idx)
        col_map = {}
        for idx, (x, y) in enumerate(buildings):
            col_map.setdefault(x, []).append((y, idx))
        for lst in col_map.values():
            if len(lst) <= 2:
                continue
            lst.sort()
            for _, idx in lst[1:-1]:
                vert[idx] = True

        return sum(1 for i in range(m) if horiz[i] and vert[i])
```

## C

```c
#include <stdlib.h>

typedef struct {
    int v;
    int idx;
} Pair;

static int cmpPair(const void *a, const void *b) {
    int av = ((const Pair *)a)->v;
    int bv = ((const Pair *)b)->v;
    return (av > bv) - (av < bv);
}

int countCoveredBuildings(int n, int** buildings, int buildingsSize, int* buildingsColSize){
    if (buildingsSize == 0) return 0;

    int *rowCnt = (int*)calloc(n + 1, sizeof(int));
    int *colCnt = (int*)calloc(n + 1, sizeof(int));

    for (int i = 0; i < buildingsSize; ++i) {
        int x = buildings[i][0];
        int y = buildings[i][1];
        rowCnt[x]++;
        colCnt[y]++;
    }

    Pair **rows = (Pair**)calloc(n + 1, sizeof(Pair*));
    Pair **cols = (Pair**)calloc(n + 1, sizeof(Pair*));

    for (int i = 1; i <= n; ++i) {
        if (rowCnt[i] > 0) rows[i] = (Pair*)malloc(rowCnt[i] * sizeof(Pair));
        if (colCnt[i] > 0) cols[i] = (Pair*)malloc(colCnt[i] * sizeof(Pair));
    }

    int *rowPos = (int*)calloc(n + 1, sizeof(int));
    int *colPos = (int*)calloc(n + 1, sizeof(int));

    for (int i = 0; i < buildingsSize; ++i) {
        int x = buildings[i][0];
        int y = buildings[i][1];
        rows[x][rowPos[x]].v = y;
        rows[x][rowPos[x]].idx = i;
        rowPos[x]++;

        cols[y][colPos[y]].v = x;
        cols[y][colPos[y]].idx = i;
        colPos[y]++;
    }

    char *rowOk = (char*)calloc(buildingsSize, sizeof(char));
    char *colOk = (char*)calloc(buildingsSize, sizeof(char));

    for (int i = 1; i <= n; ++i) {
        int cnt = rowCnt[i];
        if (cnt >= 3) {
            qsort(rows[i], cnt, sizeof(Pair), cmpPair);
            for (int j = 1; j < cnt - 1; ++j) {
                rowOk[rows[i][j].idx] = 1;
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        int cnt = colCnt[i];
        if (cnt >= 3) {
            qsort(cols[i], cnt, sizeof(Pair), cmpPair);
            for (int j = 1; j < cnt - 1; ++j) {
                colOk[cols[i][j].idx] = 1;
            }
        }
    }

    int result = 0;
    for (int i = 0; i < buildingsSize; ++i) {
        if (rowOk[i] && colOk[i]) result++;
    }

    // free allocated memory
    for (int i = 1; i <= n; ++i) {
        if (rows[i]) free(rows[i]);
        if (cols[i]) free(cols[i]);
    }
    free(rows);
    free(cols);
    free(rowCnt);
    free(colCnt);
    free(rowPos);
    free(colPos);
    free(rowOk);
    free(colOk);

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int CountCoveredBuildings(int n, int[][] buildings) {
        int m = buildings.Length;
        var coordToIdx = new Dictionary<(int, int), int>(m);
        for (int i = 0; i < m; i++) {
            int x = buildings[i][0];
            int y = buildings[i][1];
            coordToIdx[(x, y)] = i;
        }

        var rows = new Dictionary<int, List<int>>();
        var cols = new Dictionary<int, List<int>>();

        foreach (var b in buildings) {
            int x = b[0], y = b[1];
            if (!rows.TryGetValue(y, out var rowList)) {
                rowList = new List<int>();
                rows[y] = rowList;
            }
            rowList.Add(x);

            if (!cols.TryGetValue(x, out var colList)) {
                colList = new List<int>();
                cols[x] = colList;
            }
            colList.Add(y);
        }

        bool[] hasLR = new bool[m];
        bool[] hasUD = new bool[m];

        foreach (var kvp in rows) {
            int y = kvp.Key;
            var list = kvp.Value;
            list.Sort();
            for (int i = 0; i < list.Count; i++) {
                if (i > 0 && i < list.Count - 1) {
                    int x = list[i];
                    int idx = coordToIdx[(x, y)];
                    hasLR[idx] = true;
                }
            }
        }

        foreach (var kvp in cols) {
            int x = kvp.Key;
            var list = kvp.Value;
            list.Sort();
            for (int i = 0; i < list.Count; i++) {
                if (i > 0 && i < list.Count - 1) {
                    int y = list[i];
                    int idx = coordToIdx[(x, y)];
                    hasUD[idx] = true;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            if (hasLR[i] && hasUD[i]) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} buildings
 * @return {number}
 */
var countCoveredBuildings = function(n, buildings) {
    const m = buildings.length;
    const leftRight = new Array(m).fill(false);
    const upDown = new Array(m).fill(false);
    
    // map coordinate string to its index in buildings array
    const coordToIdx = new Map();
    for (let i = 0; i < m; ++i) {
        const [x, y] = buildings[i];
        coordToIdx.set(`${x},${y}`, i);
    }
    
    // group by rows (same x)
    const rows = new Map(); // x -> array of y
    // group by columns (same y)
    const cols = new Map(); // y -> array of x
    
    for (const [x, y] of buildings) {
        if (!rows.has(x)) rows.set(x, []);
        rows.get(x).push(y);
        
        if (!cols.has(y)) cols.set(y, []);
        cols.get(y).push(x);
    }
    
    // process rows: need left and right neighbor (same x, smaller/larger y)
    for (const [x, arr] of rows) {
        if (arr.length <= 2) continue;
        arr.sort((a, b) => a - b);
        for (let i = 1; i < arr.length - 1; ++i) {
            const idx = coordToIdx.get(`${x},${arr[i]}`);
            leftRight[idx] = true;
        }
    }
    
    // process columns: need above and below neighbor (same y, smaller/larger x)
    for (const [y, arr] of cols) {
        if (arr.length <= 2) continue;
        arr.sort((a, b) => a - b);
        for (let i = 1; i < arr.length - 1; ++i) {
            const idx = coordToIdx.get(`${arr[i]},${y}`);
            upDown[idx] = true;
        }
    }
    
    let count = 0;
    for (let i = 0; i < m; ++i) {
        if (leftRight[i] && upDown[i]) ++count;
    }
    return count;
};
```

## Typescript

```typescript
function countCoveredBuildings(n: number, buildings: number[][]): number {
    const rowMap = new Map<number, number[]>();
    const colMap = new Map<number, number[]>();

    for (const [x, y] of buildings) {
        if (!rowMap.has(y)) rowMap.set(y, []);
        rowMap.get(y)!.push(x);
        if (!colMap.has(x)) colMap.set(x, []);
        colMap.get(x)!.push(y);
    }

    const horiz = new Set<string>();
    for (const [y, xs] of rowMap.entries()) {
        xs.sort((a, b) => a - b);
        for (let i = 1; i < xs.length - 1; ++i) {
            horiz.add(`${xs[i]},${y}`);
        }
    }

    const vert = new Set<string>();
    for (const [x, ys] of colMap.entries()) {
        ys.sort((a, b) => a - b);
        for (let i = 1; i < ys.length - 1; ++i) {
            vert.add(`${x},${ys[i]}`);
        }
    }

    let count = 0;
    for (const [x, y] of buildings) {
        const key = `${x},${y}`;
        if (horiz.has(key) && vert.has(key)) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $buildings
     * @return Integer
     */
    function countCoveredBuildings($n, $buildings) {
        $rowMap = [];
        $colMap = [];

        foreach ($buildings as $b) {
            [$x, $y] = $b;
            $rowMap[$y][] = $x;
            $colMap[$x][] = $y;
        }

        $hasLR = []; // left and right exist
        foreach ($rowMap as $y => $xs) {
            if (count($xs) < 3) continue;
            sort($xs, SORT_NUMERIC);
            $len = count($xs);
            for ($i = 1; $i < $len - 1; ++$i) {
                $key = $xs[$i] . ',' . $y;
                $hasLR[$key] = true;
            }
        }

        $hasUD = []; // up and down exist
        foreach ($colMap as $x => $ys) {
            if (count($ys) < 3) continue;
            sort($ys, SORT_NUMERIC);
            $len = count($ys);
            for ($i = 1; $i < $len - 1; ++$i) {
                $key = $x . ',' . $ys[$i];
                $hasUD[$key] = true;
            }
        }

        $count = 0;
        foreach ($buildings as $b) {
            [$x, $y] = $b;
            $key = $x . ',' . $y;
            if (isset($hasLR[$key]) && isset($hasUD[$key])) {
                ++$count;
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countCoveredBuildings(_ n: Int, _ buildings: [[Int]]) -> Int {
        let m = buildings.count
        var left = [Bool](repeating: false, count: m)
        var right = [Bool](repeating: false, count: m)
        var above = [Bool](repeating: false, count: m)
        var below = [Bool](repeating: false, count: m)
        
        var rowMap = [Int: [(coord: Int, idx: Int)]]()
        var colMap = [Int: [(coord: Int, idx: Int)]]()
        
        for (i, b) in buildings.enumerated() {
            let x = b[0]
            let y = b[1]
            rowMap[y, default: []].append((x, i))
            colMap[x, default: []].append((y, i))
        }
        
        // Process rows for left/right
        for (_, arr) in rowMap {
            let sortedArr = arr.sorted { $0.coord < $1.coord }
            let cnt = sortedArr.count
            if cnt <= 2 { continue }
            for i in 0..<cnt {
                let idx = sortedArr[i].idx
                if i > 0 { left[idx] = true }
                if i + 1 < cnt { right[idx] = true }
            }
        }
        
        // Process columns for below/above
        for (_, arr) in colMap {
            let sortedArr = arr.sorted { $0.coord < $1.coord }
            let cnt = sortedArr.count
            if cnt <= 2 { continue }
            for i in 0..<cnt {
                let idx = sortedArr[i].idx
                if i > 0 { below[idx] = true }          // smaller y exists
                if i + 1 < cnt { above[idx] = true }    // larger y exists
            }
        }
        
        var result = 0
        for i in 0..<m {
            if left[i] && right[i] && above[i] && below[i] {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCoveredBuildings(n: Int, buildings: Array<IntArray>): Int {
        val rowMap = HashMap<Int, MutableList<Int>>()
        val colMap = HashMap<Int, MutableList<Int>>()
        for (b in buildings) {
            val x = b[0]
            val y = b[1]
            rowMap.computeIfAbsent(x) { mutableListOf() }.add(y)
            colMap.computeIfAbsent(y) { mutableListOf() }.add(x)
        }

        fun encode(x: Int, y: Int): Long {
            return (x.toLong() shl 32) or (y.toLong() and 0xffffffffL)
        }

        val horizSet = HashSet<Long>()
        for ((row, list) in rowMap) {
            if (list.size > 2) {
                list.sort()
                for (i in 1 until list.size - 1) {
                    horizSet.add(encode(row, list[i]))
                }
            }
        }

        val vertSet = HashSet<Long>()
        for ((col, list) in colMap) {
            if (list.size > 2) {
                list.sort()
                for (i in 1 until list.size - 1) {
                    vertSet.add(encode(list[i], col))
                }
            }
        }

        var count = 0
        for (b in buildings) {
            val key = encode(b[0], b[1])
            if (horizSet.contains(key) && vertSet.contains(key)) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countCoveredBuildings(int n, List<List<int>> buildings) {
    int m = buildings.length;
    List<bool> rowOk = List.filled(m, false);
    List<bool> colOk = List.filled(m, false);

    Map<int, List<List<int>>> rows = {};
    Map<int, List<List<int>>> cols = {};

    for (int i = 0; i < m; ++i) {
      int x = buildings[i][0];
      int y = buildings[i][1];
      rows.putIfAbsent(x, () => []).add([y, i]);
      cols.putIfAbsent(y, () => []).add([x, i]);
    }

    // Process rows: left and right
    for (var entry in rows.values) {
      entry.sort((a, b) => a[0].compareTo(b[0])); // sort by y
      int len = entry.length;
      if (len <= 2) continue; // none can have both sides
      for (int i = 1; i < len - 1; ++i) {
        rowOk[entry[i][1]] = true;
      }
    }

    // Process columns: above and below
    for (var entry in cols.values) {
      entry.sort((a, b) => a[0].compareTo(b[0])); // sort by x
      int len = entry.length;
      if (len <= 2) continue; // none can have both sides
      for (int i = 1; i < len - 1; ++i) {
        colOk[entry[i][1]] = true;
      }
    }

    int count = 0;
    for (int i = 0; i < m; ++i) {
      if (rowOk[i] && colOk[i]) count++;
    }
    return count;
  }
}
```

## Golang

```go
func countCoveredBuildings(n int, buildings [][]int) int {
	type pair struct {
		val int
		idx int
	}
	rows := make(map[int][]pair)
	cols := make(map[int][]pair)

	for i, b := range buildings {
		x, y := b[0], b[1]
		rows[y] = append(rows[y], pair{val: x, idx: i})
		cols[x] = append(cols[x], pair{val: y, idx: i})
	}

	rowCovered := make([]bool, len(buildings))
	colCovered := make([]bool, len(buildings))

	for _, list := range rows {
		if len(list) <= 2 {
			continue
		}
		// sort by coordinate value
		sort.Slice(list, func(i, j int) bool { return list[i].val < list[j].val })
		for k := 1; k < len(list)-1; k++ {
			rowCovered[list[k].idx] = true
		}
	}

	for _, list := range cols {
		if len(list) <= 2 {
			continue
		}
		sort.Slice(list, func(i, j int) bool { return list[i].val < list[j].val })
		for k := 1; k < len(list)-1; k++ {
			colCovered[list[k].idx] = true
		}
	}

	count := 0
	for i := range buildings {
		if rowCovered[i] && colCovered[i] {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_covered_buildings(n, buildings)
  rows = Hash.new { |h, k| h[k] = [] }
  cols = Hash.new { |h, k| h[k] = [] }

  buildings.each do |x, y|
    rows[y] << x
    cols[x] << y
  end

  flag = Hash.new(0)

  rows.each do |y, xs|
    next if xs.length < 3
    xs.sort!
    (1...xs.length - 1).each do |i|
      flag[[xs[i], y]] += 1
    end
  end

  cols.each do |x, ys|
    next if ys.length < 3
    ys.sort!
    (1...ys.length - 1).each do |i|
      flag[[x, ys[i]]] += 1
    end
  end

  count = 0
  buildings.each do |x, y|
    count += 1 if flag[[x, y]] == 2
  end
  count
end
```

## Scala

```scala
object Solution {
    def countCoveredBuildings(n: Int, buildings: Array[Array[Int]]): Int = {
        val m = buildings.length
        val idxMap = scala.collection.mutable.HashMap[(Int, Int), Int]()
        for (i <- 0 until m) {
            val x = buildings(i)(0)
            val y = buildings(i)(1)
            idxMap((x, y)) = i
        }

        import scala.collection.mutable.{ArrayBuffer, HashMap}
        val rows = new HashMap[Int, ArrayBuffer[Int]]()
        val cols = new HashMap[Int, ArrayBuffer[Int]]()

        for (b <- buildings) {
            val x = b(0)
            val y = b(1)
            rows.getOrElseUpdate(x, ArrayBuffer()).append(y)
            cols.getOrElseUpdate(y, ArrayBuffer()).append(x)
        }

        val leftRight = new Array[Boolean](m)
        val upDown = new Array[Boolean](m)

        for ((row, buf) <- rows) {
            if (buf.length > 2) {
                buf.sortInPlace()
                var i = 1
                while (i < buf.length - 1) {
                    val y = buf(i)
                    val idx = idxMap((row, y))
                    leftRight(idx) = true
                    i += 1
                }
            }
        }

        for ((col, buf) <- cols) {
            if (buf.length > 2) {
                buf.sortInPlace()
                var i = 1
                while (i < buf.length - 1) {
                    val x = buf(i)
                    val idx = idxMap((x, col))
                    upDown(idx) = true
                    i += 1
                }
            }
        }

        var count = 0
        var i = 0
        while (i < m) {
            if (leftRight(i) && upDown(i)) count += 1
            i += 1
        }
        count
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_covered_buildings(_n: i32, buildings: Vec<Vec<i32>>) -> i32 {
        let mut row_map: HashMap<i32, (i32, i32)> = HashMap::new(); // x -> (min_y, max_y)
        let mut col_map: HashMap<i32, (i32, i32)> = HashMap::new(); // y -> (min_x, max_x)

        for b in &buildings {
            let x = b[0];
            let y = b[1];

            row_map
                .entry(x)
                .and_modify(|e| {
                    if y < e.0 { e.0 = y; }
                    if y > e.1 { e.1 = y; }
                })
                .or_insert((y, y));

            col_map
                .entry(y)
                .and_modify(|e| {
                    if x < e.0 { e.0 = x; }
                    if x > e.1 { e.1 = x; }
                })
                .or_insert((x, x));
        }

        let mut count = 0;
        for b in &buildings {
            let x = b[0];
            let y = b[1];

            let (row_min, row_max) = row_map.get(&x).unwrap();
            let (col_min, col_max) = col_map.get(&y).unwrap();

            if y > *row_min && y < *row_max && x > *col_min && x < *col_max {
                count += 1;
            }
        }

        count as i32
    }
}
```

## Racket

```racket
(define/contract (count-covered-buildings n buildings)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length buildings))
         (xvec (make-vector m))
         (yvec (make-vector m))
         (row-hash (make-hash))
         (col-hash (make-hash)))
    ;; Populate vectors and hash tables
    (for ([b buildings] [i (in-naturals)])
      (let ((x (first b)) (y (second b)))
        (vector-set! xvec i x)
        (vector-set! yvec i y)
        (hash-update! row-hash y (lambda (lst) (cons (list x i) lst)) '())
        (hash-update! col-hash x (lambda (lst) (cons (list y i) lst)) '())))

    (define horiz (make-vector m #f))
    (define vert  (make-vector m #f))

    ;; Process rows for left/right
    (for ([pair (in-hash-values row-hash)])
      (let* ((sorted (sort pair (lambda (a b) (< (first a) (first b)))))
             (len (length sorted)))
        (when (>= len 3)
          (for ([p sorted] [idx (in-naturals)])
            (when (and (> idx 0) (< idx (- len 1)))
              (vector-set! horiz (second p) #t))))))

    ;; Process columns for above/below
    (for ([pair (in-hash-values col-hash)])
      (let* ((sorted (sort pair (lambda (a b) (< (first a) (first b)))))
             (len (length sorted)))
        (when (>= len 3)
          (for ([p sorted] [idx (in-naturals)])
            (when (and (> idx 0) (< idx (- len 1)))
              (vector-set! vert (second p) #t))))))

    ;; Count buildings covered in all four directions
    (let ((cnt 0))
      (for ([i (in-range m)])
        (when (and (vector-ref horiz i) (vector-ref vert i))
          (set! cnt (+ cnt 1))))
      cnt)))
```

## Erlang

```erlang
-spec count_covered_buildings(N :: integer(), Buildings :: [[integer()]]) -> integer().
count_covered_buildings(_N, Buildings) ->
    %% Build row and column maps: Y => [X], X => [Y]
    {RowMap0, ColMap0} = lists:foldl(
        fun([X, Y], {RAcc, CAcc}) ->
            RNew = maps:update_with(Y,
                    fun(L) -> [X | L] end,
                    [X],
                    RAcc),
            CNew = maps:update_with(X,
                    fun(L) -> [Y | L] end,
                    [Y],
                    CAcc),
            {RNew, CNew}
        end,
        {#{}, #{}},
        Buildings),

    %% Determine interior buildings in rows
    RowInteriorSet = maps:fold(
        fun(Y, Xlist, SetAcc) ->
            SortedX = lists:sort(Xlist),
            case length(SortedX) of
                L when L =< 2 -> SetAcc;
                _ ->
                    InteriorXs = interior_elements(SortedX),
                    add_to_set({Y}, InteriorXs, SetAcc)
            end
        end,
        sets:new(),
        RowMap0),

    %% Determine interior buildings in columns
    ColInteriorSet = maps:fold(
        fun(X, Ylist, SetAcc) ->
            SortedY = lists:sort(Ylist),
            case length(SortedY) of
                L when L =< 2 -> SetAcc;
                _ ->
                    InteriorYs = interior_elements(SortedY),
                    add_to_set({X}, InteriorYs, SetAcc)
            end
        end,
        sets:new(),
        ColMap0),

    %% Count buildings that are interior in both row and column
    lists:foldl(
        fun([X, Y], Cnt) ->
            case {sets:is_element({X, Y}, RowInteriorSet),
                  sets:is_element({X, Y}, ColInteriorSet)} of
                {true, true} -> Cnt + 1;
                _ -> Cnt
            end
        end,
        0,
        Buildings).

%% Return list without first and last elements (interior)
-spec interior_elements([integer()]) -> [integer()].
interior_elements(List) ->
    case List of
        [_] -> [];
        [] -> [];
        [_First | Rest] ->
            Rev = lists:reverse(Rest),
            case Rev of
                [_Last | MiddleRev] ->
                    lists:reverse(MiddleRev);
                _ -> []
            end
    end.

%% Add a set of coordinates sharing the same fixed coordinate (row or column)
-spec add_to_set({integer()}, [integer()], sets:set()) -> sets:set().
add_to_set({Fixed}, VarList, Set) ->
    lists:foldl(
        fun(Var, Acc) ->
            case Fixed of
                Y when is_integer(Y) -> % row processing, Fixed = Y, Var = X
                    sets:add_element({Var, Y}, Acc);
                X when is_integer(X) -> % column processing, Fixed = X, Var = Y
                    sets:add_element({X, Var}, Acc)
            end
        end,
        Set,
        VarList).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_covered_buildings(n :: integer, buildings :: [[integer]]) :: integer
  def count_covered_buildings(_n, buildings) do
    {row_map, col_map} =
      Enum.reduce(buildings, {%{}, %{}}, fn [x, y], {rmap, cmap} ->
        rmap = Map.update(rmap, x, [y], &[y | &1])
        cmap = Map.update(cmap, y, [x], &[x | &1])
        {rmap, cmap}
      end)

    row_covered =
      Enum.reduce(row_map, MapSet.new(), fn {x, ys}, acc ->
        sorted = Enum.sort(ys)
        len = length(sorted)

        if len > 2 do
          interior = Enum.slice(sorted, 1, len - 2)

          Enum.reduce(interior, acc, fn y, a -> MapSet.put(a, {x, y}) end)
        else
          acc
        end
      end)

    col_covered =
      Enum.reduce(col_map, MapSet.new(), fn {y, xs}, acc ->
        sorted = Enum.sort(xs)
        len = length(sorted)

        if len > 2 do
          interior = Enum.slice(sorted, 1, len - 2)

          Enum.reduce(interior, acc, fn x, a -> MapSet.put(a, {x, y}) end)
        else
          acc
        end
      end)

    Enum.count(buildings, fn [x, y] ->
      MapSet.member?(row_covered, {x, y}) and MapSet.member?(col_covered, {x, y})
    end)
  end
end
```
