# 0497. Random Point in Non-overlapping Rectangles

## Cpp

```cpp
class Solution {
public:
    Solution(std::vector<std::vector<int>>& rects) : rects_(rects), gen_(std::random_device{}()) {
        pref_.reserve(rects.size());
        long long sum = 0;
        for (const auto& r : rects_) {
            long long w = static_cast<long long>(r[2] - r[0] + 1);
            long long h = static_cast<long long>(r[3] - r[1] + 1);
            sum += w * h;
            pref_.push_back(sum);
        }
        total_ = sum;
    }
    
    std::vector<int> pick() {
        std::uniform_int_distribution<long long> dist(0, total_ - 1);
        long long target = dist(gen_);
        int idx = static_cast<int>(std::lower_bound(pref_.begin(), pref_.end(), target + 1) - pref_.begin());
        const auto& r = rects_[idx];
        long long w = static_cast<long long>(r[2] - r[0] + 1);
        long long offset = target - (idx == 0 ? 0 : pref_[idx - 1]);
        int dx = static_cast<int>(offset % w);
        int dy = static_cast<int>(offset / w);
        return {r[0] + dx, r[1] + dy};
    }
    
private:
    std::vector<std::vector<int>> rects_;
    std::vector<long long> pref_;
    long long total_;
    std::mt19937 gen_;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(rects);
 * vector<int> param_1 = obj->pick();
 */
```

## Java

```java
class Solution {
    private int[][] rects;
    private long[] pref;
    private long total;

    public Solution(int[][] rects) {
        this.rects = rects;
        int n = rects.length;
        pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            long cnt = ((long) rects[i][2] - rects[i][0] + 1) *
                       ((long) rects[i][3] - rects[i][1] + 1);
            pref[i + 1] = pref[i] + cnt;
        }
        total = pref[n];
    }

    public int[] pick() {
        long target = java.util.concurrent.ThreadLocalRandom.current().nextLong(total);
        int lo = 0, hi = rects.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (target >= pref[mid + 1]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        int idx = lo;
        long offset = target - pref[idx];
        int[] r = rects[idx];
        int width = r[2] - r[0] + 1;
        int dx = (int) (offset % width);
        int dy = (int) (offset / width);
        return new int[]{r[0] + dx, r[1] + dy};
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.pick();
 */
```

## Python

```python
import random
import bisect

class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.prefix = []
        total = 0
        for a, b, x, y in rects:
            cnt = (x - a + 1) * (y - b + 1)
            total += cnt
            self.prefix.append(total)
        self.total = total

    def pick(self):
        """
        :rtype: List[int]
        """
        target = random.randint(0, self.total - 1)
        idx = bisect.bisect_right(self.prefix, target)
        a, b, x, y = self.rects[idx]
        prev = self.prefix[idx - 1] if idx > 0 else 0
        offset = target - prev
        width = x - a + 1
        px = a + (offset % width)
        py = b + (offset // width)
        return [px, py]
```

## Python3

```python
import random, bisect
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.cum = []
        total = 0
        for a, b, x, y in rects:
            cnt = (x - a + 1) * (y - b + 1)
            total += cnt
            self.cum.append(total)

    def pick(self) -> List[int]:
        target = random.randrange(self.cum[-1])
        idx = bisect.bisect_left(self.cum, target + 1)
        a, b, x, y = self.rects[idx]
        width = x - a + 1
        offset = target - (self.cum[idx - 1] if idx else 0)
        dx = offset % width
        dy = offset // width
        return [a + dx, b + dy]
```

## C

```c
typedef struct {
    int **rects;
    int rectsSize;
    long long *prefix;
    long long total;
} Solution;

Solution* solutionCreate(int** rects, int rectsSize, int* rectsColSize) {
    (void)rectsColSize; // unused, each row has length 4
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj->rectsSize = rectsSize;
    obj->rects = (int**)malloc(rectsSize * sizeof(int*));
    obj->prefix = (long long*)malloc(rectsSize * sizeof(long long));
    long long sum = 0;
    for (int i = 0; i < rectsSize; ++i) {
        obj->rects[i] = (int*)malloc(4 * sizeof(int));
        for (int j = 0; j < 4; ++j) {
            obj->rects[i][j] = rects[i][j];
        }
        long long width = (long long)(obj->rects[i][2] - obj->rects[i][0] + 1);
        long long height = (long long)(obj->rects[i][3] - obj->rects[i][1] + 1);
        sum += width * height;
        obj->prefix[i] = sum;
    }
    obj->total = sum;
    srand((unsigned)time(NULL));
    return obj;
}

int* solutionPick(Solution* obj, int* retSize) {
    long long r = (long long)(rand() % obj->total);
    // binary search for rectangle
    int lo = 0, hi = obj->rectsSize - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (r < obj->prefix[mid]) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    int idx = lo;
    long long prev = (idx == 0) ? 0 : obj->prefix[idx - 1];
    long long offset = r - prev; // 0‑based index inside rectangle
    long long width = (long long)(obj->rects[idx][2] - obj->rects[idx][0] + 1);
    int x = obj->rects[idx][0] + (int)(offset % width);
    int y = obj->rects[idx][1] + (int)(offset / width);
    int* res = (int*)malloc(2 * sizeof(int));
    res[0] = x;
    res[1] = y;
    *retSize = 2;
    return res;
}

void solutionFree(Solution* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->rectsSize; ++i) {
        free(obj->rects[i]);
    }
    free(obj->rects);
    free(obj->prefix);
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(rects, rectsSize, rectsColSize);
 * int* param_1 = solutionPick(obj, retSize);
 *
 * solutionFree(obj);
 */
```

## Csharp

```csharp
public class Solution
{
    private readonly int[][] _rects;
    private readonly long[] _prefixSums;
    private readonly long _totalPoints;
    private readonly System.Random _rand;

    public Solution(int[][] rects)
    {
        _rects = rects;
        _prefixSums = new long[rects.Length];
        long sum = 0;
        for (int i = 0; i < rects.Length; i++)
        {
            int a = rects[i][0];
            int b = rects[i][1];
            int x = rects[i][2];
            int y = rects[i][3];
            long points = ((long)(x - a + 1)) * (y - b + 1);
            sum += points;
            _prefixSums[i] = sum;
        }
        _totalPoints = sum;
        _rand = new System.Random();
    }

    public int[] Pick()
    {
        long target = (long)(_rand.NextDouble() * _totalPoints);
        // binary search for rectangle
        int left = 0, right = _prefixSums.Length - 1;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (_prefixSums[mid] > target)
                right = mid;
            else
                left = mid + 1;
        }
        int idx = left;
        long prevSum = idx == 0 ? 0 : _prefixSums[idx - 1];
        long offset = target - prevSum;

        int a = _rects[idx][0];
        int b = _rects[idx][1];
        int x = _rects[idx][2];
        //int y = _rects[idx][3];

        int width = x - a + 1;
        int dx = (int)(offset % width);
        int dy = (int)(offset / width);

        return new int[] { a + dx, b + dy };
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.Pick();
 */
```

## Javascript

```javascript
/**
 * @param {number[][]} rects
 */
var Solution = function(rects) {
    this.rects = rects;
    this.prefix = [];
    let sum = 0;
    for (const r of rects) {
        const cnt = (r[2] - r[0] + 1) * (r[3] - r[1] + 1);
        sum += cnt;
        this.prefix.push(sum);
    }
    this.total = sum;
};

/**
 * @return {number[]}
 */
Solution.prototype.pick = function() {
    const target = Math.floor(Math.random() * this.total);
    // binary search for rectangle
    let lo = 0, hi = this.prefix.length - 1;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (target < this.prefix[mid]) hi = mid;
        else lo = mid + 1;
    }
    const rect = this.rects[lo];
    const x1 = rect[0], y1 = rect[1], x2 = rect[2], y2 = rect[3];
    const width = x2 - x1 + 1;
    const prev = lo === 0 ? 0 : this.prefix[lo - 1];
    const offset = target - prev;
    const dx = offset % width;
    const dy = Math.floor(offset / width);
    return [x1 + dx, y1 + dy];
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */
```

## Typescript

```typescript
class Solution {
    private rects: number[][];
    private pref: number[];
    private total: number;

    constructor(rects: number[][]) {
        this.rects = rects;
        this.pref = [];
        let sum = 0;
        for (const r of rects) {
            const cnt = (r[2] - r[0] + 1) * (r[3] - r[1] + 1);
            sum += cnt;
            this.pref.push(sum);
        }
        this.total = sum;
    }

    pick(): number[] {
        const target = Math.floor(Math.random() * this.total);
        let lo = 0, hi = this.pref.length - 1;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (target >= this.pref[mid]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        const idx = lo;
        const rect = this.rects[idx];
        const prev = idx === 0 ? 0 : this.pref[idx - 1];
        let offset = target - prev;
        const width = rect[2] - rect[0] + 1;
        const x = rect[0] + (offset % width);
        const y = rect[1] + Math.floor(offset / width);
        return [x, y];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */
```

## Php

```php
class Solution {
    private $rects;
    private $prefix = [];
    private $total = 0;

    /**
     * @param Integer[][] $rects
     */
    public function __construct($rects) {
        $this->rects = $rects;
        foreach ($rects as $r) {
            [$x1, $y1, $x2, $y2] = $r;
            $cnt = ($x2 - $x1 + 1) * ($y2 - $y1 + 1);
            $this->total += $cnt;
            $this->prefix[] = $this->total;
        }
    }

    /**
     * @return Integer[]
     */
    public function pick() {
        $rand = random_int(0, $this->total - 1);

        // binary search to find the rectangle
        $left = 0;
        $right = count($this->prefix) - 1;
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($rand < $this->prefix[$mid]) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        $idx = $left;

        $prev = $idx > 0 ? $this->prefix[$idx - 1] : 0;
        $offset = $rand - $prev;

        [$x1, $y1, $x2, $y2] = $this->rects[$idx];
        $width = $x2 - $x1 + 1;

        $dx = $offset % $width;
        $dy = intdiv($offset, $width);

        $x = $x1 + $dx;
        $y = $y1 + $dy;

        return [$x, $y];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = new Solution($rects);
 * $ret_1 = $obj->pick();
 */
```

## Swift

```swift
class Solution {
    private var rects: [[Int]]
    private var prefix: [Int]
    private var totalPoints: Int

    init(_ rects: [[Int]]) {
        self.rects = rects
        self.prefix = []
        var sum = 0
        for r in rects {
            let count = (r[2] - r[0] + 1) * (r[3] - r[1] + 1)
            sum += count
            prefix.append(sum)
        }
        self.totalPoints = sum
    }

    func pick() -> [Int] {
        let rand = Int.random(in: 0..<totalPoints)
        var lo = 0
        var hi = prefix.count - 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if rand >= prefix[mid] {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        let idx = lo
        let rect = rects[idx]
        let prev = idx == 0 ? 0 : prefix[idx - 1]
        var offset = rand - prev
        let width = rect[2] - rect[0] + 1
        let dx = offset % width
        let dy = offset / width
        let x = rect[0] + dx
        let y = rect[1] + dy
        return [x, y]
    }
}
```

## Kotlin

```kotlin
class Solution(rects: Array<IntArray>) {
    private val rects = rects
    private val pref: LongArray
    private val rand = java.util.Random()

    init {
        pref = LongArray(rects.size)
        var sum = 0L
        for (i in rects.indices) {
            val r = rects[i]
            val cnt = (r[2] - r[0] + 1).toLong() * (r[3] - r[1] + 1)
            sum += cnt
            pref[i] = sum
        }
    }

    fun pick(): IntArray {
        val total = pref.last()
        val target = (rand.nextDouble() * total).toLong()
        var lo = 0
        var hi = pref.size - 1
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (target < pref[mid]) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        val idx = lo
        val prev = if (idx == 0) 0L else pref[idx - 1]
        var offset = target - prev
        val r = rects[idx]
        val width = r[2] - r[0] + 1
        val xOffset = (offset % width).toInt()
        offset /= width
        val yOffset = offset.toInt()
        return intArrayOf(r[0] + xOffset, r[1] + yOffset)
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(rects)
 * var param_1 = obj.pick()
 */
```

## Dart

```dart
import 'dart:math';

class Solution {
  final List<List<int>> _rects;
  final List<int> _prefix;
  final int _total;
  final Random _rand;

  Solution(List<List<int>> rects)
      : _rects = rects,
        _prefix = [] ,
        _rand = Random(),
        _total = (() {
          int sum = 0;
          for (var r in rects) {
            int cnt = (r[2] - r[0] + 1) * (r[3] - r[1] + 1);
            sum += cnt;
          }
          return sum;
        }()) {
    int sum = 0;
    for (var r in rects) {
      int cnt = (r[2] - r[0] + 1) * (r[3] - r[1] + 1);
      sum += cnt;
      _prefix.add(sum);
    }
  }

  List<int> pick() {
    int target = _rand.nextInt(_total); // 0 .. total-1
    int lo = 0, hi = _prefix.length - 1;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (_prefix[mid] <= target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    int idx = lo;
    var rect = _rects[idx];
    int x1 = rect[0], y1 = rect[1], x2 = rect[2], y2 = rect[3];
    int width = x2 - x1 + 1;

    int prevCount = idx == 0 ? 0 : _prefix[idx - 1];
    int offset = target - prevCount;
    int dx = offset % width;
    int dy = offset ~/ width;

    return [x1 + dx, y1 + dy];
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(rects);
 * List<int> param1 = obj.pick();
 */
```

## Golang

```go
package main

import (
	"math/rand"
	"sort"
	"time"
)

type Solution struct {
	rects [][]int
	pref  []int64
	total int64
}

func Constructor(rects [][]int) Solution {
	rand.Seed(time.Now().UnixNano())
	pref := make([]int64, len(rects))
	var total int64
	for i, rc := range rects {
		w := int64(rc[2] - rc[0] + 1)
		h := int64(rc[3] - rc[1] + 1)
		cnt := w * h
		total += cnt
		pref[i] = total
	}
	return Solution{
		rects: rects,
		pref:  pref,
		total: total,
	}
}

func (this *Solution) Pick() []int {
	r := rand.Int63n(this.total)
	idx := sort.Search(len(this.pref), func(i int) bool { return this.pref[i] > r })
	var prev int64
	if idx > 0 {
		prev = this.pref[idx-1]
	}
	offset := r - prev

	rect := this.rects[idx]
	w := int64(rect[2] - rect[0] + 1)

	dx := int(offset % w)
	dy := int(offset / w)

	x := rect[0] + dx
	y := rect[1] + dy
	return []int{x, y}
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(rects);
 * param_1 := obj.Pick();
 */
```

## Ruby

```ruby
class Solution
  # :type rects: Integer[][]
  def initialize(rects)
    @rects = rects
    @prefix = []
    total = 0
    rects.each do |r|
      w = r[2] - r[0] + 1
      h = r[3] - r[1] + 1
      cnt = w * h
      total += cnt
      @prefix << total
    end
    @total_points = total
  end

  # :rtype: Integer[]
  def pick()
    target = rand(@total_points)
    lo = 0
    hi = @prefix.length - 1
    while lo < hi
      mid = (lo + hi) / 2
      if @prefix[mid] <= target
        lo = mid + 1
      else
        hi = mid
      end
    end
    idx = lo
    rect = @rects[idx]
    prev = idx == 0 ? 0 : @prefix[idx - 1]
    offset = target - prev

    w = rect[2] - rect[0] + 1
    x_offset = offset % w
    y_offset = offset / w

    [rect[0] + x_offset, rect[1] + y_offset]
  end
end
```

## Scala

```scala
class Solution(_rects: Array[Array[Int]]) {
  private val rects = _rects
  private val prefix = new Array[Long](rects.length)
  private var total: Long = 0L
  private val rand = new scala.util.Random()

  for (i <- rects.indices) {
    val r = rects(i)
    val cnt = (r(2).toLong - r(0).toLong + 1L) * (r(3).toLong - r(1).toLong + 1L)
    total += cnt
    prefix(i) = total
  }

  def pick(): Array[Int] = {
    val target = (rand.nextDouble() * total).toLong
    var lo = 0
    var hi = rects.length - 1
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (prefix(mid) <= target) lo = mid + 1 else hi = mid
    }
    val r = rects(lo)
    val x0 = r(0)
    val y0 = r(1)
    val xLen = r(2) - r(0) + 1
    val yLen = r(3) - r(1) + 1
    val dx = rand.nextInt(xLen)
    val dy = rand.nextInt(yLen)
    Array(x0 + dx, y0 + dy)
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(rects)
 * val param_1 = obj.pick()
 */
```

## Rust

```rust
use rand::prelude::*;
use std::cmp::Ordering;

struct Solution {
    rects: Vec<Vec<i32>>,
    prefix: Vec<i64>,
    total: i64,
}

impl Solution {
    fn new(rects: Vec<Vec<i32>>) -> Self {
        let mut prefix = Vec::with_capacity(rects.len());
        let mut sum: i64 = 0;
        for r in &rects {
            let cnt = (r[2] - r[0] + 1) as i64 * (r[3] - r[1] + 1) as i64;
            sum += cnt;
            prefix.push(sum);
        }
        Solution { rects, prefix, total: sum }
    }

    fn pick(&self) -> Vec<i32> {
        let mut rng = thread_rng();
        let target = rng.gen_range(0..self.total);
        // find rectangle index where prefix > target
        let idx = match self.prefix.binary_search_by(|&v| {
            if v > target { Ordering::Greater } else { Ordering::Less }
        }) {
            Ok(pos) => pos,
            Err(pos) => pos,
        };
        let rect = &self.rects[idx];
        let prev = if idx == 0 { 0 } else { self.prefix[idx - 1] };
        let offset = target - prev;
        let width = (rect[2] - rect[0] + 1) as i64;
        let dx = (offset % width) as i32;
        let dy = (offset / width) as i32;
        vec![rect[0] + dx, rect[1] + dy]
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(rects);
 * let ret_1: Vec<i32> = obj.pick();
 */
```

## Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; rects : (listof (listof exact-integer?))
    (init-field
      rects)
    
    (field [cum '()] [total 0])
    
    ;; compute cumulative point counts for each rectangle
    (begin
      (for ([rect rects])
        (let* ([x1 (list-ref rect 0)]
               [y1 (list-ref rect 1)]
               [x2 (list-ref rect 2)]
               [y2 (list-ref rect 3)])
          (define cnt (* (+ (- x2 x1) 1)
                         (+ (- y2 y1) 1)))
          (set! total (+ total cnt))
          (set! cum (append cum (list total))))))
    
    ; pick : -> (listof exact-integer?)
    (define/public (pick)
      (let* ([idx (random total)]
             [rect-index
              (let loop ([i 0] [cs cum])
                (if (< idx (car cs))
                    i
                    (loop (+ i 1) (cdr cs))))]
             [rect (list-ref rects rect-index)]
             [x1 (list-ref rect 0)]
             [y1 (list-ref rect 1)]
             [x2 (list-ref rect 2)]
             [y2 (list-ref rect 3)])
        (let* ([dx (- x2 x1)]
               [dy (- y2 y1)]
               [rx (random (+ dx 1))]
               [ry (random (+ dy 1))])
          (list (+ x1 rx) (+ y1 ry)))))
    ))
```

## Erlang

```erlang
-module(solution).
-export([solution_init_/1, solution_pick/0]).

%% Initialize with list of rectangles.
-spec solution_init_(Rects :: [[integer()]]) -> any().
solution_init_(Rects) ->
    % Seed random generator
    Seed = {erlang:monotonic_time(),
            erlang:system_time(),
            erlang:unique_integer()},
    rand:seed(exsplus, Seed),
    {PrefList, Total} = build_prefix(Rects),
    put(solution_state,
        #{rects => Rects,
          pref  => PrefList,
          total => Total}),
    ok.

%% Pick a random integer point uniformly.
-spec solution_pick() -> [integer()].
solution_pick() ->
    State = get(solution_state),
    Total = maps:get(total, State),
    K = rand:uniform(Total) - 1,
    Pref = maps:get(pref, State),
    Rects = maps:get(rects, State),

    Index = find_index(Pref, K, 0),

    {PrevSum, Rect} =
        case Index of
            0 -> {0, lists:nth(1, Rects)};
            _ ->
                Prev = lists:nth(Index, Pref),
                {Prev, lists:nth(Index + 1, Rects)}
        end,

    Offset = K - PrevSum,
    [A, B, X, Y] = Rect,
    W = X - A + 1,
    Dx = Offset rem W,
    Dy = Offset div W,
    Xc = A + Dx,
    Yc = B + Dy,
    [Xc, Yc].

%% Helper to build cumulative counts.
build_prefix(Rects) ->
    build_prefix(Rects, [], 0).

build_prefix([], AccRev, Total) ->
    {lists:reverse(AccRev), Total};
build_prefix([[A, B, X, Y] | Rest], AccRev, Sum) ->
    Count = (X - A + 1) * (Y - B + 1),
    NewSum = Sum + Count,
    build_prefix(Rest, [NewSum | AccRev], NewSum).

%% Find first index where cumulative > K.
find_index([], _K, Index) -> Index;
find_index([P | Rest], K, Index) ->
    if
        K < P -> Index;
        true  -> find_index(Rest, K, Index + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec init_(rects :: [[integer]]) :: any
  def init_(rects) do
    counts =
      Enum.map(rects, fn [x1, _y1, x2, _y2] ->
        (x2 - x1 + 1) * (Enum.at(&1, 3) - Enum.at(&1, 1) + 1)
      end)

    prefix = Enum.scan(counts, &(&1 + &2))
    total = List.last(prefix) || 0
    Process.put(:rect_data, {rects, prefix, total})
    :ok
  end

  @spec pick() :: [integer]
  def pick() do
    {rects, prefix, total} = Process.get(:rect_data)

    r = :rand.uniform(total)
    idx = Enum.find_index(prefix, fn cum -> r <= cum end) || 0

    rect = Enum.at(rects, idx)
    [x1, y1, x2, y2] = rect

    prev = if idx == 0, do: 0, else: Enum.at(prefix, idx - 1)
    offset = r - prev - 1

    width = x2 - x1 + 1
    dx = rem(offset, width)
    dy = div(offset, width)

    [x1 + dx, y1 + dy]
  end
end
```
