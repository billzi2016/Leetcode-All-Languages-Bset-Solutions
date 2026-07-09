# 1240. Tiling a Rectangle with the Fewest Squares

## Cpp

```cpp
class Solution {
public:
    int tilingRectangle(int n, int m) {
        if (n == m) return 1;
        // make width the smaller side to reduce branching
        if (n < m) swap(n, m);
        vector<int> h(m, 0);               // heights of each column
        int best = n * m;                  // worst case: all 1x1 squares
        const int totalArea = n * m;

        function<void(int)> dfs = [&](int used) {
            if (used >= best) return;

            // find the leftmost column with minimal filled height
            int minH = INT_MAX, idx = -1;
            for (int i = 0; i < m; ++i) {
                if (h[i] < minH) {
                    minH = h[i];
                    idx = i;
                }
            }

            // all rows are filled
            if (minH == n) {
                best = used;
                return;
            }

            // remaining area
            int filled = 0;
            for (int v : h) filled += v;
            int remain = totalArea - filled;

            // width of consecutive columns that share the same minimal height
            int width = 0;
            while (idx + width < m && h[idx + width] == minH) ++width;
            int maxSize = min(width, n - minH);   // largest square we can place now

            // lower bound pruning: even if we fill remaining area with the biggest possible squares
            int lb = (remain + maxSize * maxSize - 1) / (maxSize * maxSize);
            if (used + lb >= best) return;

            // try placing squares from largest to smallest
            for (int sz = maxSize; sz >= 1; --sz) {
                for (int k = 0; k < sz; ++k) h[idx + k] += sz;
                dfs(used + 1);
                for (int k = 0; k < sz; ++k) h[idx + k] -= sz;
            }
        };

        dfs(0);
        return best;
    }
};
```

## Java

```java
class Solution {
    private int n, m, best;

    public int tilingRectangle(int n, int m) {
        if (n == m) return 1;
        this.n = n;
        this.m = m;
        // initial upper bound using greedy Euclidean algorithm
        int a = n, b = m, cnt = 0;
        while (a > 0 && b > 0) {
            if (a < b) { int t = a; a = b; b = t; }
            cnt += a / b;
            a %= b;
        }
        best = cnt;

        int[] heights = new int[m];
        dfs(heights, 0);
        return best;
    }

    private void dfs(int[] h, int used) {
        if (used >= best) return;

        // find the leftmost column with minimal filled height
        int minH = Integer.MAX_VALUE, idx = -1;
        for (int i = 0; i < m; i++) {
            if (h[i] < minH) {
                minH = h[i];
                idx = i;
            }
        }

        // all rows are filled
        if (minH == n) {
            best = used;
            return;
        }

        int maxSide = Math.min(n - minH, m - idx);
        for (int size = maxSide; size >= 1; size--) {
            boolean canPlace = true;
            for (int j = idx; j < idx + size; j++) {
                if (h[j] != minH) {
                    canPlace = false;
                    break;
                }
            }
            if (!canPlace) continue;

            // place square
            for (int j = idx; j < idx + size; j++) h[j] += size;
            dfs(h, used + 1);
            // backtrack
            for (int j = idx; j < idx + size; j++) h[j] -= size;
        }
    }
}
```

## Python

```python
class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == m:
            return 1
        # make n the larger dimension to reduce width (columns)
        if n < m:
            n, m = m, n
        self.n = n          # height of rectangle
        self.m = m          # width (number of columns)
        self.best = n * m   # worst case: all 1x1 squares
        self.height = [0] * self.m  # filled height for each column

        self._dfs(0)
        return self.best

    def _dfs(self, cnt):
        if cnt >= self.best:
            return
        min_h = min(self.height)
        if min_h == self.n:          # fully tiled
            self.best = cnt
            return
        idx = self.height.index(min_h)

        # maximum square side we can place at (idx, min_h)
        max_len = 0
        limit = min(self.n - min_h, self.m - idx)
        for l in range(1, limit + 1):
            ok = True
            for j in range(idx, idx + l):
                if self.height[j] != min_h:
                    ok = False
                    break
            if not ok:
                break
            max_len = l

        # lower bound pruning
        remain_area = self.n * self.m - sum(self.height)
        min_needed = (remain_area + max_len * max_len - 1) // (max_len * max_len)
        if cnt + min_needed >= self.best:
            return

        for size in range(max_len, 0, -1):
            for j in range(idx, idx + size):
                self.height[j] += size
            self._dfs(cnt + 1)
            for j in range(idx, idx + size):
                self.height[j] -= size
```

## Python3

```python
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        # make width the smaller dimension to reduce branching
        if m > n:
            n, m = m, n

        self.n, self.m = n, m
        self.heights = [0] * self.m
        self.best = n * m  # worst case: all 1x1 squares

        def dfs(cnt: int):
            if cnt >= self.best:
                return
            min_h = min(self.heights)
            if min_h == self.n:          # rectangle fully covered
                self.best = cnt
                return

            idx = self.heights.index(min_h)

            # maximum square side we can place at (idx, min_h)
            max_len = 0
            while idx + max_len < self.m and self.heights[idx + max_len] == min_h:
                max_len += 1
            max_len = min(max_len, self.n - min_h)

            for size in range(max_len, 0, -1):
                # place square of side 'size'
                for k in range(idx, idx + size):
                    self.heights[k] += size

                # lower bound heuristic: remaining area / (largest possible square)^2
                remain = 0
                max_possible = 0
                for h in self.heights:
                    diff = self.n - h
                    remain += diff
                    if diff > max_possible:
                        max_possible = diff
                if remain == 0:
                    lower = 0
                else:
                    lower = (remain + max_possible * max_possible - 1) // (max_possible * max_possible)

                if cnt + 1 + lower < self.best:
                    dfs(cnt + 1)

                # undo placement
                for k in range(idx, idx + size):
                    self.heights[k] -= size

        dfs(0)
        return self.best
```

## C

```c
int N, M;
int bestAns;
char used[14][14];
int totalArea;
int filledCnt;

static int min(int a, int b) { return a < b ? a : b; }

int canPlace(int x, int y, int sz) {
    for (int i = x; i < x + sz; ++i)
        for (int j = y; j < y + sz; ++j)
            if (used[i][j]) return 0;
    return 1;
}

void setPlace(int x, int y, int sz, char val) {
    for (int i = x; i < x + sz; ++i)
        for (int j = y; j < y + sz; ++j)
            used[i][j] = val;
}

void dfs(int cnt) {
    if (cnt >= bestAns) return;

    int fx = -1, fy = -1;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (!used[i][j]) { fx = i; fy = j; goto found; }
        }
    }
found:
    if (fx == -1) {               // all filled
        bestAns = cnt;
        return;
    }

    int maxLen = min(N - fx, M - fy);
    for (int sz = maxLen; sz >= 1; --sz) {
        if (!canPlace(fx, fy, sz)) continue;
        setPlace(fx, fy, sz, 1);
        filledCnt += sz * sz;

        dfs(cnt + 1);

        filledCnt -= sz * sz;
        setPlace(fx, fy, sz, 0);
    }
}

int tilingRectangle(int n, int m) {
    if (n == m) return 1;
    N = n; M = m;
    totalArea = N * M;
    bestAns = totalArea;          // worst case: all 1x1 squares
    filledCnt = 0;
    for (int i = 0; i < 14; ++i)
        for (int j = 0; j < 14; ++j)
            used[i][j] = 0;

    dfs(0);
    return bestAns;
}
```

## Csharp

```csharp
public class Solution {
    private int n, m;
    private int best;
    private int[] heights;

    public int TilingRectangle(int n, int m) {
        if (n == m) return 1;
        // make n the smaller side to reduce width of state array
        if (n > m) {
            int tmp = n;
            n = m;
            m = tmp;
        }
        this.n = n;
        this.m = m;
        heights = new int[m];
        best = n * m; // worst case: all 1x1 squares
        Dfs(0);
        return best;
    }

    private void Dfs(int used) {
        if (used >= best) return;

        // find the leftmost column with minimal filled height
        int minH = n, idx = -1;
        for (int i = 0; i < m; i++) {
            if (heights[i] < minH) {
                minH = heights[i];
                idx = i;
                if (minH == 0) break;
            }
        }

        // all filled
        if (minH == n) {
            best = used;
            return;
        }

        // compute maximal square side we can place at (idx, minH)
        int width = 0;
        while (idx + width < m && heights[idx + width] == minH) width++;
        int maxSide = Math.Min(width, n - minH);

        // lower bound pruning based on remaining area
        int filled = 0;
        for (int h : heights) filled += h;
        int remain = n * m - filled;
        int maxSquareArea = maxSide * maxSide;
        int minAdditional = (remain + maxSquareArea - 1) / maxSquareArea;
        if (used + minAdditional >= best) return;

        // try squares from large to small
        for (int size = maxSide; size >= 1; size--) {
            for (int i = 0; i < size; i++) heights[idx + i] += size;
            Dfs(used + 1);
            for (int i = 0; i < size; i++) heights[idx + i] -= size;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var tilingRectangle = function(n, m) {
    if (n === m) return 1;
    // ensure n <= m to reduce width
    if (n > m) [n, m] = [m, n];
    const heights = new Array(m).fill(0);
    let best = n * m; // worst case: all 1x1 squares

    function dfs(used) {
        if (used >= best) return;

        // find the leftmost column with minimal filled height
        let minH = Infinity, idx = -1;
        for (let i = 0; i < m; ++i) {
            if (heights[i] < minH) {
                minH = heights[i];
                idx = i;
            }
        }

        // all columns are fully filled
        if (minH === n) {
            best = used;
            return;
        }

        // remaining area and a simple lower bound prune
        const remainArea = n * m - heights.reduce((a, b) => a + b, 0);
        const maxPossibleSide = Math.min(n - minH, m - idx);
        const lowerBound = Math.ceil(remainArea / (maxPossibleSide * maxPossibleSide));
        if (used + lowerBound >= best) return;

        // try to place squares of decreasing size
        for (let size = maxPossibleSide; size >= 1; --size) {
            let canPlace = true;
            for (let j = idx; j < idx + size; ++j) {
                if (heights[j] !== minH) { canPlace = false; break; }
            }
            if (!canPlace) continue;

            // place the square
            for (let j = idx; j < idx + size; ++j) heights[j] += size;
            dfs(used + 1);
            // backtrack
            for (let j = idx; j < idx + size; ++j) heights[j] -= size;
        }
    }

    dfs(0);
    return best;
};
```

## Typescript

```typescript
function tilingRectangle(n: number, m: number): number {
    if (n < m) [n, m] = [m, n];
    const heights = new Array(m).fill(0);
    let best = n * m; // worst case: all 1x1 squares

    function dfs(cnt: number): void {
        if (cnt >= best) return;

        // find the leftmost column with minimal filled height
        let minH = Number.MAX_SAFE_INTEGER;
        let idx = -1;
        for (let i = 0; i < m; i++) {
            if (heights[i] < minH) {
                minH = heights[i];
                idx = i;
                if (minH === 0) break; // early exit when we hit the topmost empty row
            }
        }

        // all columns are fully filled
        if (minH === n) {
            best = cnt;
            return;
        }

        const maxSize = Math.min(n - minH, m - idx);
        for (let size = maxSize; size >= 1; size--) {
            // check if a square of this size can be placed at (minH, idx)
            let ok = true;
            for (let j = idx; j < idx + size; j++) {
                if (heights[j] !== minH) {
                    ok = false;
                    break;
                }
            }
            if (!ok) continue;

            // place the square
            for (let j = idx; j < idx + size; j++) heights[j] += size;
            dfs(cnt + 1);
            // remove the square (backtrack)
            for (let j = idx; j < idx + size; j++) heights[j] -= size;
        }
    }

    dfs(0);
    return best;
}
```

## Php

```php
class Solution {
    private int $n;
    private int $m;
    /** @var bool[][] */
    private array $grid;
    private int $best;

    /**
     * @param Integer $n
     * @param Integer $m
     * @return Integer
     */
    function tilingRectangle($n, $m) {
        if ($n == $m) return 1;
        $this->n = $n;
        $this->m = $m;
        $this->grid = array_fill(0, $n, array_fill(0, $m, false));
        $this->best = $n * $m; // worst case: all 1x1 squares
        $this->dfs(0, 0);
        return $this->best;
    }

    private function dfs(int $cnt, int $filled): void {
        if ($cnt >= $this->best) return;

        $total = $this->n * $this->m;
        if ($filled == $total) {
            $this->best = $cnt;
            return;
        }

        // simple lower bound pruning
        $maxSide = min($this->n, $this->m);
        $remaining = $total - $filled;
        $lb = intdiv($remaining + $maxSide * $maxSide - 1, $maxSide * $maxSide);
        if ($cnt + $lb >= $this->best) return;

        // find first empty cell (top‑leftmost)
        $found = false;
        for ($i = 0; $i < $this->n && !$found; $i++) {
            for ($j = 0; $j < $this->m; $j++) {
                if (!$this->grid[$i][$j]) {
                    $x = $i;
                    $y = $j;
                    $found = true;
                    break;
                }
            }
        }

        // maximum square size we can try at (x, y)
        $maxSize = min($this->n - $x, $this->m - $y);
        for ($size = $maxSize; $size >= 1; $size--) {
            if ($this->canPlace($x, $y, $size)) {
                $this->place($x, $y, $size, true);
                $this->dfs($cnt + 1, $filled + $size * $size);
                $this->place($x, $y, $size, false);
            }
        }
    }

    private function canPlace(int $x, int $y, int $size): bool {
        for ($i = $x; $i < $x + $size; $i++) {
            for ($j = $y; $j < $y + $size; $j++) {
                if ($this->grid[$i][$j]) return false;
            }
        }
        return true;
    }

    private function place(int $x, int $y, int $size, bool $val): void {
        for ($i = $x; $i < $x + $size; $i++) {
            for ($j = $y; $j < $y + $size; $j++) {
                $this->grid[$i][$j] = $val;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func tilingRectangle(_ n: Int, _ m: Int) -> Int {
        if n == m { return 1 }
        var heights = Array(repeating: 0, count: m)
        let totalArea = n * m
        var best = totalArea
        
        func dfs(_ cnt: Int) {
            if cnt >= best { return }
            
            // find the leftmost column with minimal filled height
            var minH = Int.max
            var idx = -1
            for i in 0..<m {
                let h = heights[i]
                if h < minH {
                    minH = h
                    idx = i
                }
            }
            
            // all cells are filled
            if minH == n {
                best = cnt
                return
            }
            
            // lower bound pruning
            var remain = 0
            for h in heights {
                remain += (n - h)
            }
            let maxSide = max(n, m)
            let lowerBound = (remain + maxSide * maxSide - 1) / (maxSide * maxSide)
            if cnt + lowerBound >= best { return }
            
            // maximum square size we can place at (idx, minH)
            var limit = min(n - minH, m - idx)
            var maxSize = 0
            var size = 1
            while size <= limit {
                var ok = true
                for j in idx..<(idx + size) {
                    if heights[j] != minH {
                        ok = false
                        break
                    }
                }
                if !ok { break }
                maxSize = size
                size += 1
            }
            
            // try squares from largest to smallest
            var s = maxSize
            while s >= 1 {
                for j in idx..<(idx + s) {
                    heights[j] += s
                }
                dfs(cnt + 1)
                for j in idx..<(idx + s) {
                    heights[j] -= s
                }
                s -= 1
            }
        }
        
        dfs(0)
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    private var rows = 0
    private var cols = 0
    private lateinit var heights: IntArray
    private var best = Int.MAX_VALUE

    fun tilingRectangle(n: Int, m: Int): Int {
        if (n == m) return 1
        rows = n
        cols = m
        heights = IntArray(cols)
        best = n * m
        dfs(0)
        return best
    }

    private fun dfs(cnt: Int) {
        if (cnt >= best) return

        var minH = Int.MAX_VALUE
        var idx = -1
        for (i in 0 until cols) {
            val h = heights[i]
            if (h < minH) {
                minH = h
                idx = i
            }
        }

        if (minH == rows) {
            best = cnt
            return
        }

        var limit = 0
        while (idx + limit < cols && heights[idx + limit] == minH) {
            limit++
        }
        val maxSide = kotlin.math.min(limit, rows - minH)

        for (size in maxSide downTo 1) {
            for (k in idx until idx + size) {
                heights[k] += size
            }
            dfs(cnt + 1)
            for (k in idx until idx + size) {
                heights[k] -= size
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  late int _n;
  late int _m;
  late List<int> _heights;
  late int _best;

  void _dfs(int used) {
    if (used >= _best) return;

    // find the column with minimal filled height
    int minH = _heights[0];
    int idx = 0;
    for (int i = 1; i < _m; i++) {
      if (_heights[i] < minH) {
        minH = _heights[i];
        idx = i;
      }
    }

    // all rows are filled
    if (minH == _n) {
      _best = used;
      return;
    }

    // maximum possible square side at this position
    int maxSide = _n - minH;
    int width = 0;
    for (int j = idx; j < _m && _heights[j] == minH; j++) {
      width++;
    }
    if (width < maxSide) maxSide = width;

    // try larger squares first
    for (int size = maxSide; size >= 1; size--) {
      for (int k = idx; k < idx + size; k++) {
        _heights[k] += size;
      }
      _dfs(used + 1);
      for (int k = idx; k < idx + size; k++) {
        _heights[k] -= size;
      }
    }
  }

  int tilingRectangle(int n, int m) {
    if (n == m) return 1;

    // make n the smaller dimension to reduce state space
    if (n > m) {
      int tmp = n;
      n = m;
      m = tmp;
    }
    _n = n;
    _m = m;
    _heights = List.filled(_m, 0);
    _best = n * m; // worst case: all 1x1 squares
    _dfs(0);
    return _best;
  }
}
```

## Golang

```go
func tilingRectangle(n int, m int) int {
	if n == m {
		return 1
	}
	w, h := n, m
	if w > h {
		w, h = h, w
	}
	best := max(n, m)
	heights := make([]int, w)

	var dfs func(used int)
	dfs = func(used int) {
		if used >= best {
			return
		}
		minH, idx := h+1, -1
		maxH := 0
		for i, v := range heights {
			if v < minH {
				minH = v
				idx = i
			}
			if v > maxH {
				maxH = v
			}
		}
		if maxH == h { // fully tiled
			if used < best {
				best = used
			}
			return
		}
		// count consecutive columns from idx with the same min height
		width := 0
		for i := idx; i < w && heights[i] == minH; i++ {
			width++
		}
		maxSize := width
		if h-minH < maxSize {
			maxSize = h - minH
		}
		for size := maxSize; size >= 1; size-- {
			for i := idx; i < idx+size; i++ {
				heights[i] += size
			}
			dfs(used + 1)
			for i := idx; i < idx+size; i++ {
				heights[i] -= size
			}
		}
	}
	dfs(0)
	return best
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def tiling_rectangle(n, m)
  return 1 if n == m
  if n > m
    n, m = m, n
  end

  @n = n
  @m = m
  @best = n * m
  @heights = Array.new(m, 0)
  max_square_global = [n, m].min

  dfs = nil
  dfs = ->(count) do
    return if count >= @best

    min_h = @heights.min
    if min_h == @n
      @best = count if count < @best
      return
    end

    idx = @heights.index(min_h)

    max_width = 0
    while idx + max_width < @m && @heights[idx + max_width] == min_h
      max_width += 1
    end
    max_side = [@n - min_h, max_width].min

    remaining = @n * @m - @heights.sum
    lower = (remaining + max_square_global * max_square_global - 1) / (max_square_global * max_square_global)
    return if count + lower >= @best

    side = max_side
    while side > 0
      (idx...idx + side).each { |j| @heights[j] += side }
      dfs.call(count + 1)
      (idx...idx + side).each { |j| @heights[j] -= side }
      side -= 1
    end
  end

  dfs.call(0)
  @best
end
```

## Scala

```scala
object Solution {
    def tilingRectangle(n: Int, m: Int): Int = {
        if (n == m) return 1
        var N = n
        var M = m
        if (N > M) { val t = N; N = M; M = t } // ensure N <= M

        val totalArea = N * M
        val heights = new Array[Int](M)
        var best = Int.MaxValue

        def dfs(used: Int): Unit = {
            if (used >= best) return

            // find leftmost column with minimal filled height
            var minH = N
            var idx = -1
            var i = 0
            while (i < M) {
                if (heights(i) < minH) {
                    minH = heights(i)
                    idx = i
                }
                i += 1
            }

            // all filled
            if (minH == N) {
                best = used
                return
            }

            // maximum square side we can place at (minH, idx)
            var maxSide = Math.min(N - minH, M - idx)
            var sizeLimit = maxSide
            var k = idx
            while (k < idx + maxSide) {
                val limit = N - heights(k)
                if (limit < sizeLimit) sizeLimit = limit
                k += 1
            }

            // lower bound pruning
            var sum = 0
            i = 0
            while (i < M) { sum += heights(i); i += 1 }
            val remaining = totalArea - sum
            val maxPossibleSide = Math.min(N, M)
            val lowerBound = (remaining + maxPossibleSide * maxPossibleSide - 1) / (maxPossibleSide * maxPossibleSide)
            if (used + lowerBound >= best) return

            var sz = sizeLimit
            while (sz >= 1) {
                // place square of side sz
                k = idx
                while (k < idx + sz) { heights(k) += sz; k += 1 }
                dfs(used + 1)
                k = idx
                while (k < idx + sz) { heights(k) -= sz; k += 1 }
                sz -= 1
            }
        }

        dfs(0)
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn tiling_rectangle(n: i32, m: i32) -> i32 {
        let n = n as usize;
        let m = m as usize;
        if n == m {
            return 1;
        }
        let total = n * m;
        let max_side = std::cmp::min(n, m);
        let mut best = total as i32; // worst case: all 1x1 squares
        let mut grid = vec![vec![false; m]; n];
        Self::dfs(n, m, total, max_side, &mut grid, 0, 0, &mut best);
        best
    }

    fn dfs(
        n: usize,
        m: usize,
        total: usize,
        max_side: usize,
        grid: &mut Vec<Vec<bool>>,
        cnt: i32,
        filled: usize,
        best: &mut i32,
    ) {
        if cnt >= *best {
            return;
        }
        let remain = total - filled;
        if remain == 0 {
            *best = cnt.min(*best);
            return;
        }
        // simple lower bound pruning
        let min_needed = ((remain + max_side * max_side - 1) / (max_side * max_side)) as i32;
        if cnt + min_needed >= *best {
            return;
        }

        // find first empty cell
        let mut r0 = 0usize;
        let mut c0 = 0usize;
        'outer: for i in 0..n {
            for j in 0..m {
                if !grid[i][j] {
                    r0 = i;
                    c0 = j;
                    break 'outer;
                }
            }
        }

        // maximum square size we can try at (r0,c0)
        let mut max_len = std::cmp::min(n - r0, m - c0);
        while max_len > 0 && !Self::can_place(grid, r0, c0, max_len) {
            max_len -= 1;
        }

        for sz in (1..=max_len).rev() {
            Self::place(grid, r0, c0, sz, true);
            Self::dfs(
                n,
                m,
                total,
                max_side,
                grid,
                cnt + 1,
                filled + sz * sz,
                best,
            );
            Self::place(grid, r0, c0, sz, false);
        }
    }

    fn can_place(grid: &Vec<Vec<bool>>, r: usize, c: usize, sz: usize) -> bool {
        for i in r..r + sz {
            for j in c..c + sz {
                if grid[i][j] {
                    return false;
                }
            }
        }
        true
    }

    fn place(grid: &mut Vec<Vec<bool>>, r: usize, c: usize, sz: usize, val: bool) {
        for i in r..r + sz {
            for j in c..c + sz {
                grid[i][j] = val;
            }
        }
    }
}
```

## Racket

```racket
(define/contract (tiling-rectangle n m)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((total (* n m))
         (board
          (let ([b (make-vector n)])
            (for ([i (in-range n)])
              (vector-set! b i (make-vector m #f)))
            b))
         (best (box total)))
    (define (find-first-empty)
      (let loop ((i 0))
        (if (= i n) #f
            (let inner ((j 0))
              (cond [(= j m) (loop (+ i 1))]
                    [(not (vector-ref (vector-ref board i) j)) (cons i j)]
                    [else (inner (+ j 1))])))))
    (define (can-place? i j size)
      (and (<= (+ i size) n)
           (<= (+ j size) m)
           (let loop ((x i))
             (if (= x (+ i size)) #t
                 (let inner ((y j))
                   (cond [(= y (+ j size)) (loop (+ x 1))]
                         [(vector-ref (vector-ref board x) y) #f]
                         [else (inner (+ y 1))]))))))
    (define (place! i j size val)
      (for ([x (in-range i (+ i size))])
        (for ([y (in-range j (+ j size))])
          (vector-set! (vector-ref board x) y val))))
    (define (dfs count filled)
      (when (< count (unbox best))
        (let ((first-empty (find-first-empty)))
          (if (not first-empty)
              (set-box! best count)
              (let* ((i (car first-empty))
                     (j (cdr first-empty))
                     (max-size (min (- n i) (- m j))))
                (define remaining (- total filled))
                (define max-square (* max-size max-size))
                (define lower (+ count (ceiling (/ remaining max-square))))
                (when (< lower (unbox best))
                  (let loop ((size max-size))
                    (when (> size 0)
                      (when (can-place? i j size)
                        (place! i j size #t)
                        (dfs (+ count 1) (+ filled (* size size)))
                        (place! i j size #f))
                      (loop (- size 1))))))))))
    (dfs 0 0)
    (unbox best)))
```

## Erlang

```erlang
-spec tiling_rectangle(N :: integer(), M :: integer()) -> integer().
tiling_rectangle(N, M) ->
    if N == M -> 1;
       true ->
          {H, W} = if N > M -> {N, M}; true -> {M, N} end,
          InitialHeights = lists:duplicate(W, 0),
          Upper = N * M,
          dfs(InitialHeights, 0, Upper, H, W)
    end.

dfs(_Heights, Used, Best, _N, _W) when Used >= Best ->
    Best;
dfs(Heights, Used, Best, N, W) ->
    case all_filled(Heights, N) of
        true -> erlang:min(Best, Used);
        false ->
            {MinH, Idx} = find_min(Heights),
            Run = run_len(Heights, Idx, MinH),
            MaxSize = erlang:min(N - MinH, Run),
            dfs_sizes(MaxSize, Heights, Used, Best, N, W, Idx, MinH)
    end.

dfs_sizes(0, _Heights, _Used, Best, _N, _W, _Idx, _MinH) ->
    Best;
dfs_sizes(Size, Heights, Used, Best, N, W, Idx, MinH) ->
    NewBest1 =
        if Size >= 1 ->
            NewHeights = update_heights(Heights, Idx, Size, MinH + Size),
            Res = dfs(NewHeights, Used + 1, Best, N, W),
            erlang:min(Best, Res);
           true -> Best
        end,
    if Size - 1 > 0 ->
        dfs_sizes(Size - 1, Heights, Used, NewBest1, N, W, Idx, MinH);
       true -> NewBest1
    end.

all_filled([], _N) -> true;
all_filled([H|T], N) when H == N -> all_filled(T, N);
all_filled(_, _) -> false.

find_min(Heights) ->
    find_min(Heights, 0, 1 bsl 30, 0).

find_min([], _Pos, Min, Idx) -> {Min, Idx};
find_min([H|T], Pos, CurMin, CurIdx) ->
    if H < CurMin ->
            find_min(T, Pos + 1, H, Pos);
       true ->
            find_min(T, Pos + 1, CurMin, CurIdx)
    end.

run_len(Heights, StartIdx, Min) ->
    {_, Rest} = lists:split(StartIdx, Heights),
    run_len_rest(Rest, Min, 0).

run_len_rest([], _Min, Acc) -> Acc;
run_len_rest([H|T], Min, Acc) when H == Min ->
    run_len_rest(T, Min, Acc + 1);
run_len_rest(_, _Min, Acc) -> Acc.

update_heights(Heights, StartIdx, Size, NewHeight) ->
    {Prefix, Rest} = lists:split(StartIdx, Heights),
    {_OldMid, Suffix} = lists:split(Size, Rest),
    UpdatedMid = lists:duplicate(Size, NewHeight),
    Prefix ++ UpdatedMid ++ Suffix.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec tiling_rectangle(n :: integer, m :: integer) :: integer
  def tiling_rectangle(n, m) when n == m, do: 1

  def tiling_rectangle(n, m) do
    board = List.duplicate(0, n)
    best_initial = n * m
    dfs(board, 0, best_initial, n, m)
  end

  # depth‑first search with pruning
  defp dfs(_board, cnt, best, _n, _m) when cnt >= best, do: best

  defp dfs(board, cnt, best, n, m) do
    case find_empty(board, m) do
      nil ->
        min(cnt, best)

      {r, c} ->
        max_len = min(n - r, m - c)
        sizes = Enum.reverse(1..max_len)

        Enum.reduce(sizes, best, fn size, cur_best ->
          if cnt + 1 >= cur_best do
            cur_best
          else
            if can_place?(board, r, c, size, m) do
              new_board = place(board, r, c, size, m)
              dfs(new_board, cnt + 1, cur_best, n, m)
            else
              cur_best
            end
          end
        end)
    end
  end

  # find first empty cell (row, col) or nil if full
  defp find_empty(board, m) do
    full = (1 <<< m) - 1
    find_empty_row(board, 0, full, m)
  end

  defp find_empty_row([], _r, _full, _m), do: nil

  defp find_empty_row([row_mask | rest], r, full, m) do
    if row_mask == full do
      find_empty_row(rest, r + 1, full, m)
    else
      c = find_first_zero(row_mask, m)
      {r, c}
    end
  end

  # first column in the row that is zero
  defp find_first_zero(mask, m) do
    Enum.find(0..(m - 1), fn c -> (mask &&& (1 <<< c)) == 0 end)
  end

  # can we place a square of given size at (r,c)?
  defp can_place?(board, r, c, size, m) do
    mask = ((1 <<< size) - 1) <<< c

    Enum.reduce_while(r..(r + size - 1), true, fn row_idx, _acc ->
      row_mask = Enum.at(board, row_idx)

      if (row_mask &&& mask) == 0 do
        {:cont, true}
      else
        {:halt, false}
      end
    end) == true
  end

  # place a square (set bits)
  defp place(board, r, c, size, m) do
    mask = ((1 <<< size) - 1) <<< c

    Enum.with_index(board)
    |> Enum.map(fn {row_mask, idx} ->
      if idx >= r and idx < r + size do
        row_mask ||| mask
      else
        row_mask
      end
    end)
  end
end
```
