# 2013. Detect Squares

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class DetectSquares {
    unordered_map<int, unordered_map<int,int>> mp; // x -> (y -> count)
public:
    DetectSquares() {}
    
    void add(vector<int> point) {
        int x = point[0], y = point[1];
        ++mp[x][y];
    }
    
    int count(vector<int> point) {
        int x = point[0], y = point[1];
        if (!mp.count(x)) return 0;
        long long ans = 0;
        for (const auto& [y2, cntY2] : mp[x]) {
            if (y2 == y) continue;
            int d = abs(y2 - y);
            
            // square to the right
            int nx = x + d;
            if (mp.count(nx)) {
                int c1 = 0, c2 = 0;
                auto it1 = mp[nx].find(y);
                if (it1 != mp[nx].end()) c1 = it1->second;
                auto it2 = mp[nx].find(y2);
                if (it2 != mp[nx].end()) c2 = it2->second;
                ans += 1LL * cntY2 * c1 * c2;
            }
            
            // square to the left
            nx = x - d;
            if (mp.count(nx)) {
                int c1 = 0, c2 = 0;
                auto it1 = mp[nx].find(y);
                if (it1 != mp[nx].end()) c1 = it1->second;
                auto it2 = mp[nx].find(y2);
                if (it2 != mp[nx].end()) c2 = it2->second;
                ans += 1LL * cntY2 * c1 * c2;
            }
        }
        return static_cast<int>(ans);
    }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */
```

## Java

```java
class DetectSquares {
    private final java.util.Map<Integer, java.util.Map<Integer, Integer>> yMap;
    private final java.util.Map<String, Integer> pointCount;

    public DetectSquares() {
        yMap = new java.util.HashMap<>();
        pointCount = new java.util.HashMap<>();
    }

    public void add(int[] point) {
        int x = point[0];
        int y = point[1];
        yMap.computeIfAbsent(y, k -> new java.util.HashMap<>())
            .merge(x, 1, Integer::sum);
        String key = x + "," + y;
        pointCount.merge(key, 1, Integer::sum);
    }

    public int count(int[] point) {
        int x = point[0];
        int y = point[1];
        java.util.Map<Integer, Integer> sameY = yMap.get(y);
        if (sameY == null) return 0;
        int total = 0;
        for (java.util.Map.Entry<Integer, Integer> entry : sameY.entrySet()) {
            int x2 = entry.getKey();
            int cnt1 = entry.getValue(); // count of (x2, y)
            if (x2 == x) continue; // need a different x to form side
            int d = Math.abs(x2 - x);
            // square above the line
            int yUpper = y + d;
            String keyA = x + "," + yUpper;
            String keyB = x2 + "," + yUpper;
            Integer cntA = pointCount.get(keyA);
            Integer cntB = pointCount.get(keyB);
            if (cntA != null && cntB != null) {
                total += cnt1 * cntA * cntB;
            }
            // square below the line
            int yLower = y - d;
            keyA = x + "," + yLower;
            keyB = x2 + "," + yLower;
            cntA = pointCount.get(keyA);
            cntB = pointCount.get(keyB);
            if (cntA != null && cntB != null) {
                total += cnt1 * cntA * cntB;
            }
        }
        return total;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.add(point);
 * int param_2 = obj.count(point);
 */
```

## Python

```python
class DetectSquares(object):
    def __init__(self):
        from collections import defaultdict
        self.point_cnt = {}
        self.row = defaultdict(lambda: defaultdict(int))

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        key = (x, y)
        self.point_cnt[key] = self.point_cnt.get(key, 0) + 1
        self.row[y][x] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x, y = point
        ans = 0
        if y not in self.row:
            return 0
        for x1, cnt_x1 in self.row[y].items():
            if x1 == x:
                continue
            d = abs(x1 - x)
            # upper square
            y2 = y + d
            ans += cnt_x1 * self.point_cnt.get((x, y2), 0) * self.point_cnt.get((x1, y2), 0)
            # lower square
            y2 = y - d
            ans += cnt_x1 * self.point_cnt.get((x, y2), 0) * self.point_cnt.get((x1, y2), 0)
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
```

## Python3

```python
class DetectSquares:
    def __init__(self):
        from collections import defaultdict
        self.point_cnt = {}
        self.x_map = defaultdict(lambda: defaultdict(int))

    def add(self, point):
        x, y = point
        key = (x, y)
        self.point_cnt[key] = self.point_cnt.get(key, 0) + 1
        self.x_map[x][y] += 1

    def count(self, point):
        x0, y0 = point
        ans = 0
        if x0 not in self.x_map:
            return 0
        for y, cnt_y in self.x_map[x0].items():
            if y == y0:
                continue
            d = abs(y - y0)
            # square to the right
            nx = x0 + d
            cnt1 = self.point_cnt.get((nx, y0), 0)
            cnt2 = self.point_cnt.get((nx, y), 0)
            if cnt1 and cnt2:
                ans += cnt_y * cnt1 * cnt2
            # square to the left
            nx = x0 - d
            cnt1 = self.point_cnt.get((nx, y0), 0)
            cnt2 = self.point_cnt.get((nx, y), 0)
            if cnt1 and cnt2:
                ans += cnt_y * cnt1 * cnt2
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int freq[1001][1001];
} DetectSquares;

DetectSquares* detectSquaresCreate() {
    DetectSquares *obj = (DetectSquares*)calloc(1, sizeof(DetectSquares));
    return obj;
}

void detectSquaresAdd(DetectSquares* obj, int* point, int pointSize) {
    int x = point[0];
    int y = point[1];
    obj->freq[x][y] += 1;
}

int detectSquaresCount(DetectSquares* obj, int* point, int pointSize) {
    int x = point[0];
    int y = point[1];
    long long total = 0;
    for (int nx = 0; nx <= 1000; ++nx) {
        if (nx == x) continue;
        int cntHorizontal = obj->freq[nx][y];
        if (cntHorizontal == 0) continue;
        int d = nx > x ? nx - x : x - nx;

        // Square above
        if (y + d <= 1000) {
            int cnt1 = obj->freq[x][y + d];
            int cnt2 = obj->freq[nx][y + d];
            total += (long long)cntHorizontal * cnt1 * cnt2;
        }
        // Square below
        if (y - d >= 0) {
            int cnt1 = obj->freq[x][y - d];
            int cnt2 = obj->freq[nx][y - d];
            total += (long long)cntHorizontal * cnt1 * cnt2;
        }
    }
    return (int)total;
}

void detectSquaresFree(DetectSquares* obj) {
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class DetectSquares {
    // y -> (x -> count)
    private readonly Dictionary<int, Dictionary<int, int>> yMap = new Dictionary<int, Dictionary<int, int>>();

    public DetectSquares() {
    }

    public void Add(int[] point) {
        int x = point[0];
        int y = point[1];
        if (!yMap.TryGetValue(y, out var dictX)) {
            dictX = new Dictionary<int, int>();
            yMap[y] = dictX;
        }
        dictX.TryGetValue(x, out var cur);
        dictX[x] = cur + 1;
    }

    public int Count(int[] point) {
        int x0 = point[0];
        int y0 = point[1];
        long total = 0;

        if (!yMap.TryGetValue(y0, out var sameYDict))
            return 0;

        foreach (var kvp in sameYDict) {
            int x1 = kvp.Key;
            int cnt1 = kvp.Value;
            if (x1 == x0) continue; // need a horizontal side

            int d = Math.Abs(x1 - x0);

            // Upper square
            int y2 = y0 + d;
            int cA = GetCount(x0, y2);
            int cB = GetCount(x1, y2);
            total += (long)cnt1 * cA * cB;

            // Lower square
            y2 = y0 - d;
            cA = GetCount(x0, y2);
            cB = GetCount(x1, y2);
            total += (long)cnt1 * cA * cB;
        }

        return (int)total;
    }

    private int GetCount(int x, int y) {
        if (!yMap.TryGetValue(y, out var dictX))
            return 0;
        dictX.TryGetValue(x, out var cnt);
        return cnt;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.Add(point);
 * int param_2 = obj.Count(point);
 */
```

## Javascript

```javascript
var DetectSquares = function() {
    this.points = new Map(); // x -> Map(y -> count)
};

DetectSquares.prototype.add = function(point) {
    const [x, y] = point;
    if (!this.points.has(x)) {
        this.points.set(x, new Map());
    }
    const col = this.points.get(x);
    col.set(y, (col.get(y) || 0) + 1);
};

DetectSquares.prototype.count = function(point) {
    const [x, y] = point;
    let total = 0;
    for (const [xp, colX] of this.points.entries()) {
        if (xp === x) continue;
        const cnt1 = colX.get(y);
        if (!cnt1) continue; // no point sharing same y
        const d = Math.abs(xp - x);
        // upper square (y + d)
        const cnt2Up = (this.points.get(x)?.get(y + d)) || 0;
        const cnt3Up = (colX.get(y + d)) || 0;
        total += cnt1 * cnt2Up * cnt3Up;
        // lower square (y - d)
        const cnt2Down = (this.points.get(x)?.get(y - d)) || 0;
        const cnt3Down = (colX.get(y - d)) || 0;
        total += cnt1 * cnt2Down * cnt3Down;
    }
    return total;
};
```

## Typescript

```typescript
class DetectSquares {
    private rows: Map<number, Map<number, number>>;

    constructor() {
        this.rows = new Map();
    }

    add(point: number[]): void {
        const [x, y] = point;
        if (!this.rows.has(y)) {
            this.rows.set(y, new Map());
        }
        const colMap = this.rows.get(y)!;
        colMap.set(x, (colMap.get(x) ?? 0) + 1);
    }

    count(point: number[]): number {
        const [x, y] = point;
        const rowMap = this.rows.get(y);
        if (!rowMap) return 0;

        let total = 0;
        for (const [px, cntX] of rowMap.entries()) {
            if (px === x) continue;
            const d = Math.abs(px - x);

            // Upper square
            const upperRow = this.rows.get(y + d);
            if (upperRow) {
                const cntY1 = upperRow.get(x) ?? 0;
                const cntY2 = upperRow.get(px) ?? 0;
                total += cntX * cntY1 * cntY2;
            }

            // Lower square
            const lowerRow = this.rows.get(y - d);
            if (lowerRow) {
                const cntY1 = lowerRow.get(x) ?? 0;
                const cntY2 = lowerRow.get(px) ?? 0;
                total += cntX * cntY1 * cntY2;
            }
        }

        return total;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
```

## Php

```php
class DetectSquares {
    private $cnt;
    private $xs;

    function __construct() {
        $this->cnt = [];
        $this->xs = [];
    }

    /**
     * @param Integer[] $point
     * @return NULL
     */
    function add($point) {
        $x = $point[0];
        $y = $point[1];
        $key = $x . '#' . $y;
        if (!isset($this->cnt[$key])) {
            $this->cnt[$key] = 0;
        }
        $this->cnt[$key]++;

        if (!isset($this->xs[$x])) {
            $this->xs[$x] = [];
        }
        if (!isset($this->xs[$x][$y])) {
            $this->xs[$x][$y] = 0;
        }
        $this->xs[$x][$y]++;
    }

    /**
     * @param Integer[] $point
     * @return Integer
     */
    function count($point) {
        $x = $point[0];
        $y = $point[1];
        $result = 0;
        if (!isset($this->xs[$x])) {
            return 0;
        }
        foreach ($this->xs[$x] as $y2 => $cntY2) {
            if ($y2 == $y) continue;
            $d = abs($y - $y2);
            // squares to the right and left
            foreach ([1, -1] as $sign) {
                $nx = $x + $sign * $d;
                $key1 = $nx . '#' . $y;
                $key2 = $nx . '#' . $y2;
                if (isset($this->cnt[$key1]) && isset($this->cnt[$key2])) {
                    $result += $cntY2 * $this->cnt[$key1] * $this->cnt[$key2];
                }
            }
        }
        return $result;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * $obj = new DetectSquares();
 * $obj->add($point);
 * $ret_2 = $obj->count($point);
 */
```

## Swift

```swift
class DetectSquares {
    private var pointsByX: [Int: [Int: Int]] = [:]

    init() { }

    func add(_ point: [Int]) {
        let x = point[0]
        let y = point[1]
        if pointsByX[x] == nil {
            pointsByX[x] = [:]
        }
        pointsByX[x]![y, default: 0] += 1
    }

    func count(_ point: [Int]) -> Int {
        let x = point[0]
        let y = point[1]
        var result = 0
        let columnAtX = pointsByX[x] ?? [:]

        for (px, inner) in pointsByX where px != x {
            guard let pCount = inner[y] else { continue }   // point (px, y)
            let side = abs(px - x)

            // Square above
            let yUpper = y + side
            if let cnt1 = columnAtX[yUpper], let cnt2 = inner[yUpper] {
                result += pCount * cnt1 * cnt2
            }

            // Square below
            let yLower = y - side
            if let cnt1 = columnAtX[yLower], let cnt2 = inner[yLower] {
                result += pCount * cnt1 * cnt2
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class DetectSquares() {
    private val points = HashMap<Int, HashMap<Int, Int>>()

    fun add(point: IntArray) {
        val x = point[0]
        val y = point[1]
        val inner = points.getOrPut(x) { HashMap() }
        inner[y] = (inner[y] ?: 0) + 1
    }

    fun count(point: IntArray): Int {
        val x = point[0]
        val y = point[1]
        var ans = 0
        for ((xi, mapXi) in points) {
            if (xi == x) continue
            val cntSameY = mapXi[y] ?: continue
            val side = kotlin.math.abs(xi - x)

            // upper square
            var y2 = y + side
            val cnt1Upper = points[x]?.get(y2) ?: 0
            val cnt2Upper = points[xi]?.get(y2) ?: 0
            ans += cntSameY * cnt1Upper * cnt2Upper

            // lower square
            y2 = y - side
            val cnt1Lower = points[x]?.get(y2) ?: 0
            val cnt2Lower = points[xi]?.get(y2) ?: 0
            ans += cntSameY * cnt1Lower * cnt2Lower
        }
        return ans
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
```

## Dart

```dart
class DetectSquares {
  final Map<int, int> _cnt = {};

  DetectSquares();

  int _encode(int x, int y) => x * 1001 + y;

  void add(List<int> point) {
    int key = _encode(point[0], point[1]);
    _cnt[key] = (_cnt[key] ?? 0) + 1;
  }

  int count(List<int> point) {
    int x = point[0];
    int y = point[1];
    int queryKey = _encode(x, y);
    int cntQuery = _cnt[queryKey] ?? 0;
    if (cntQuery == 0) return 0;

    int ans = 0;
    for (var entry in _cnt.entries) {
      int key = entry.key;
      int px = key ~/ 1001;
      int py = key % 1001;
      if (py != y || px == x) continue;

      int d = (px - x).abs();

      // square above
      int y2 = y + d;
      int k1 = _encode(x, y2);
      int k2 = _encode(px, y2);
      int cnt1 = _cnt[k1] ?? 0;
      int cnt2 = _cnt[k2] ?? 0;
      if (cnt1 > 0 && cnt2 > 0) {
        ans += cntQuery * entry.value * cnt1 * cnt2;
      }

      // square below
      y2 = y - d;
      k1 = _encode(x, y2);
      k2 = _encode(px, y2);
      cnt1 = _cnt[k1] ?? 0;
      cnt2 = _cnt[k2] ?? 0;
      if (cnt1 > 0 && cnt2 > 0) {
        ans += cntQuery * entry.value * cnt1 * cnt2;
      }
    }
    return ans;
  }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = DetectSquares();
 * obj.add(point);
 * int param2 = obj.count(point);
 */
```

## Golang

```go
type point struct {
	x, y int
}

type DetectSquares struct {
	cnt map[point]int
}

/** Initialize your data structure here. */
func Constructor() DetectSquares {
	return DetectSquares{cnt: make(map[point]int)}
}

/** Add the [x,y] point to the data structure. */
func (this *DetectSquares) Add(point []int) {
	p := point{x: point[0], y: point[1]}
	this.cnt[p]++
}

/** Count the number of ways to form axis-aligned squares with the given point. */
func (this *DetectSquares) Count(point []int) int {
	x, y := point[0], point[1]
	ans := 0
	for p, c := range this.cnt {
		if p.y != y || p.x == x {
			continue
		}
		side := abs(p.x - x)

		// upper square (y + side)
		p1 := point{x: x, y: y + side}
		p2 := point{x: p.x, y: y + side}
		ans += c * this.cnt[p1] * this.cnt[p2]

		// lower square (y - side)
		p3 := point{x: x, y: y - side}
		p4 := point{x: p.x, y: y - side}
		ans += c * this.cnt[p3] * this.cnt[p4]
	}
	return ans
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(point);
 * param_2 := obj.Count(point);
 */
```

## Ruby

```ruby
class DetectSquares
    def initialize()
        @point_counts = Hash.new(0)               # key: [x, y] -> count
        @points_by_x = Hash.new { |h, k| h[k] = Hash.new(0) }  # x => {y => count}
    end

=begin
    :type point: Integer[]
    :rtype: Void
=end
    def add(point)
        x, y = point
        @point_counts[[x, y]] += 1
        @points_by_x[x][y] += 1
    end

=begin
    :type point: Integer[]
    :rtype: Integer
=end
    def count(point)
        px, py = point
        total = 0
        return 0 unless @points_by_x.key?(px)

        @points_by_x[px].each do |y2, cnt|
            next if y2 == py
            d = (y2 - py).abs

            # Square to the right
            xr = px + d
            total += cnt *
                     (@point_counts[[xr, py]] || 0) *
                     (@point_counts[[xr, y2]] || 0)

            # Square to the left
            xl = px - d
            total += cnt *
                     (@point_counts[[xl, py]] || 0) *
                     (@point_counts[[xl, y2]] || 0)
        end

        total
    end
end
```

## Scala

```scala
import scala.collection.mutable

class DetectSquares() {

  private val pointCount = mutable.Map[(Int, Int), Int]().withDefaultValue(0)

  def add(point: Array[Int]): Unit = {
    val key = (point(0), point(1))
    pointCount(key) = pointCount(key) + 1
  }

  def count(point: Array[Int]): Int = {
    val x1 = point(0)
    val y1 = point(1)
    var total: Long = 0L

    for (((x2, y2), cnt2) <- pointCount if y2 == y1 && x2 != x1) {
      val d = (x2 - x1).abs

      // square above the query point
      var y3 = y1 + d
      val cnt3Up = pointCount.getOrElse((x1, y3), 0)
      val cnt4Up = pointCount.getOrElse((x2, y3), 0)
      total += cnt2.toLong * cnt3Up * cnt4Up

      // square below the query point
      y3 = y1 - d
      val cnt3Down = pointCount.getOrElse((x1, y3), 0)
      val cnt4Down = pointCount.getOrElse((x2, y3), 0)
      total += cnt2.toLong * cnt3Down * cnt4Down
    }

    total.toInt
  }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * val obj = new DetectSquares()
 * obj.add(point)
 * val param_2 = obj.count(point)
 */
```

## Rust

```rust
use std::collections::HashMap;

struct DetectSquares {
    points: HashMap<(i32, i32), i32>,
    y_map: HashMap<i32, HashMap<i32, i32>>, // y -> (x -> count)
}

impl DetectSquares {
    fn new() -> Self {
        DetectSquares {
            points: HashMap::new(),
            y_map: HashMap::new(),
        }
    }

    fn add(&mut self, point: Vec<i32>) {
        let x = point[0];
        let y = point[1];
        *self.points.entry((x, y)).or_insert(0) += 1;
        self.y_map
            .entry(y)
            .or_insert_with(HashMap::new)
            .entry(x)
            .and_modify(|c| *c += 1)
            .or_insert(1);
    }

    fn count(&self, point: Vec<i32>) -> i32 {
        let x = point[0];
        let y = point[1];
        let mut total = 0i32;
        if let Some(x_map) = self.y_map.get(&y) {
            for (&x2, &cnt2) in x_map.iter() {
                if x2 == x {
                    continue;
                }
                let d = (x2 - x).abs();

                // upper side
                let y_up = y + d;
                if let (Some(&cnt3), Some(&cnt4)) = (
                    self.points.get(&(x, y_up)),
                    self.points.get(&(x2, y_up)),
                ) {
                    total += cnt2 * cnt3 * cnt4;
                }

                // lower side
                let y_down = y - d;
                if let (Some(&cnt3), Some(&cnt4)) = (
                    self.points.get(&(x, y_down)),
                    self.points.get(&(x2, y_down)),
                ) {
                    total += cnt2 * cnt3 * cnt4;
                }
            }
        }
        total
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * let mut obj = DetectSquares::new();
 * obj.add(point);
 * let ret_2: i32 = obj.count(point);
 */
```

## Racket

```racket
(define detect-squares%
  (class object%
    (super-new)

    (init-field) ; no init fields

    (field [points (make-hash)]) ; point -> count

    ;; add : (listof exact-integer?) -> void?
    (define/public (add point)
      (let* ([x (first point)]
             [y (second point)]
             [key (cons x y)])
        (hash-set! points key (+ 1 (hash-ref points key 0)))))

    ;; count : (listof exact-integer?) -> exact-integer?
    (define/public (count point)
      (let* ([x (first point)]
             [y (second point)])
        (define total 0)
        (hash-for-each points
          (lambda (k v)
            (let ([px (car k)]
                  [py (cdr k)])
              (when (and (= py y) (not (= px x)))
                (let* ([d (abs (- px x))])
                  (for ([sign (list 1 -1)])
                    (let* ([ny (+ y (* sign d))]
                           [cnt1 (hash-ref points (cons x ny) 0)]
                           [cnt2 (hash-ref points (cons px ny) 0)])
                      (set! total (+ total (* v cnt1 cnt2))))))))))
        total))))
```

## Erlang

```erlang
-module(detect_squares).
-export([detect_squares_init_/0, detect_squares_add/1, detect_squares_count/1]).

%% Initialize the data structure.
detect_squares_init_() ->
    put(ds_map, #{}),
    ok.

%% Add a point to the data structure.
detect_squares_add(Point) when is_list(Point), length(Point) =:= 2 ->
    [X, Y] = Point,
    Map = get(ds_map),
    Key = {X, Y},
    Count = maps:get(Key, Map, 0) + 1,
    put(ds_map, maps:put(Key, Count, Map)),
    ok.

%% Count the number of axis-aligned squares that can be formed with the given point.
detect_squares_count(Point) when is_list(Point), length(Point) =:= 2 ->
    [Xq, Yq] = Point,
    Map = get(ds_map),
    lists:foldl(
        fun({{X1, Y1}, C1}, Acc) ->
            case (Y1 == Yq) andalso (X1 =/= Xq) of
                true ->
                    D = erlang:abs(X1 - Xq),

                    % Square above the query point
                    C2_up = maps:get({Xq, Yq + D}, Map, 0),
                    C3_up = maps:get({X1, Yq + D}, Map, 0),
                    Up = C1 * C2_up * C3_up,

                    % Square below the query point
                    C2_down = maps:get({Xq, Yq - D}, Map, 0),
                    C3_down = maps:get({X1, Yq - D}, Map, 0),
                    Down = C1 * C2_down * C3_down,

                    Acc + Up + Down;
                false ->
                    Acc
            end
        end,
        0,
        maps:to_list(Map)
    ).
```

## Elixir

```elixir
defmodule DetectSquares do
  @table :detect_squares

  @spec init_() :: any
  def init_() do
    case :ets.info(@table) do
      :undefined -> :ok
      _ -> :ets.delete(@table)
    end

    :ets.new(@table, [:named_table, :public, {:read_concurrency, true}])
    :ok
  end

  @spec add(point :: [integer]) :: any
  def add([x, y]) do
    key = {x, y}

    case :ets.lookup(@table, key) do
      [] -> :ets.insert(@table, {key, 1})
      [{^key, cnt}] -> :ets.insert(@table, {key, cnt + 1})
    end

    :ok
  end

  @spec count(point :: [integer]) :: integer
  def count([x0, y0]) do
    entries = :ets.tab2list(@table)

    Enum.reduce(entries, 0, fn {{x1, y1}, cnt1}, acc ->
      if y1 == y0 and x1 != x0 do
        d = abs(x1 - x0)

        up_left = get_count({x0, y0 + d})
        up_right = get_count({x1, y0 + d})

        down_left = get_count({x0, y0 - d})
        down_right = get_count({x1, y0 - d})

        acc +
          cnt1 * up_left * up_right +
          cnt1 * down_left * down_right
      else
        acc
      end
    end)
  end

  defp get_count(key) do
    case :ets.lookup(@table, key) do
      [{^key, cnt}] -> cnt
      [] -> 0
    end
  end
end
```
