# 3242. Design Neighbor Sum Service

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class NeighborSum {
    vector<vector<int>> grid_;
    unordered_map<int, pair<int,int>> pos;
    int n;
public:
    NeighborSum(vector<vector<int>>& grid) : grid_(grid) {
        n = grid.size();
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                pos[grid[i][j]] = {i, j};
    }
    
    int adjacentSum(int value) {
        auto [i, j] = pos[value];
        static const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        int sum = 0;
        for (auto &d : dirs) {
            int ni = i + d[0], nj = j + d[1];
            if (ni >= 0 && ni < n && nj >= 0 && nj < n)
                sum += grid_[ni][nj];
        }
        return sum;
    }
    
    int diagonalSum(int value) {
        auto [i, j] = pos[value];
        static const int dirs[4][2] = {{-1,-1},{-1,1},{1,-1},{1,1}};
        int sum = 0;
        for (auto &d : dirs) {
            int ni = i + d[0], nj = j + d[1];
            if (ni >= 0 && ni < n && nj >= 0 && nj < n)
                sum += grid_[ni][nj];
        }
        return sum;
    }
};

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum* obj = new NeighborSum(grid);
 * int param_1 = obj->adjacentSum(value);
 * int param_2 = obj->diagonalSum(value);
 */
```

## Java

```java
class NeighborSum {
    private final int[][] grid;
    private final int[] rows;
    private final int[] cols;
    private final int n;

    public NeighborSum(int[][] grid) {
        this.grid = grid;
        this.n = grid.length;
        int size = n * n;
        rows = new int[size];
        cols = new int[size];
        for (int i = 0; i < size; i++) {
            rows[i] = -1;
            cols[i] = -1;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                rows[val] = i;
                cols[val] = j;
            }
        }
    }

    public int adjacentSum(int value) {
        int i = rows[value];
        int j = cols[value];
        int sum = 0;
        if (i > 0) sum += grid[i - 1][j];
        if (i < n - 1) sum += grid[i + 1][j];
        if (j > 0) sum += grid[i][j - 1];
        if (j < n - 1) sum += grid[i][j + 1];
        return sum;
    }

    public int diagonalSum(int value) {
        int i = rows[value];
        int j = cols[value];
        int sum = 0;
        if (i > 0 && j > 0) sum += grid[i - 1][j - 1];
        if (i > 0 && j < n - 1) sum += grid[i - 1][j + 1];
        if (i < n - 1 && j > 0) sum += grid[i + 1][j - 1];
        if (i < n - 1 && j < n - 1) sum += grid[i + 1][j + 1];
        return sum;
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */
```

## Python

```python
class NeighborSum(object):
    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid
        self.n = len(grid)
        self.pos = {}
        for i in range(self.n):
            for j in range(self.n):
                self.pos[grid[i][j]] = (i, j)

    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        i, j = self.pos[value]
        s = 0
        if i > 0:
            s += self.grid[i - 1][j]
        if i < self.n - 1:
            s += self.grid[i + 1][j]
        if j > 0:
            s += self.grid[i][j - 1]
        if j < self.n - 1:
            s += self.grid[i][j + 1]
        return s

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        i, j = self.pos[value]
        s = 0
        if i > 0 and j > 0:
            s += self.grid[i - 1][j - 1]
        if i > 0 and j < self.n - 1:
            s += self.grid[i - 1][j + 1]
        if i < self.n - 1 and j > 0:
            s += self.grid[i + 1][j - 1]
        if i < self.n - 1 and j < self.n - 1:
            s += self.grid[i + 1][j + 1]
        return s

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
```

## Python3

```python
from typing import List

class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.pos = {}
        for i in range(self.n):
            for j in range(self.n):
                self.pos[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.pos[value]
        total = 0
        if i > 0:
            total += self.grid[i - 1][j]
        if i + 1 < self.n:
            total += self.grid[i + 1][j]
        if j > 0:
            total += self.grid[i][j - 1]
        if j + 1 < self.n:
            total += self.grid[i][j + 1]
        return total

    def diagonalSum(self, value: int) -> int:
        i, j = self.pos[value]
        total = 0
        if i > 0 and j > 0:
            total += self.grid[i - 1][j - 1]
        if i > 0 and j + 1 < self.n:
            total += self.grid[i - 1][j + 1]
        if i + 1 < self.n and j > 0:
            total += self.grid[i + 1][j - 1]
        if i + 1 < self.n and j + 1 < self.n:
            total += self.grid[i + 1][j + 1]
        return total
```

## C

```c
typedef struct {
    int n;
    int **grid;
    int *rowPos;
    int *colPos;
} NeighborSum;

NeighborSum* neighborSumCreate(int** grid, int gridSize, int* gridColSize) {
    NeighborSum* obj = (NeighborSum*)malloc(sizeof(NeighborSum));
    obj->n = gridSize;
    obj->grid = grid;
    int total = gridSize * gridSize;
    obj->rowPos = (int*)malloc(total * sizeof(int));
    obj->colPos = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            int val = grid[i][j];
            obj->rowPos[val] = i;
            obj->colPos[val] = j;
        }
    }
    return obj;
}

int neighborSumAdjacentSum(NeighborSum* obj, int value) {
    int i = obj->rowPos[value];
    int j = obj->colPos[value];
    int sum = 0;
    if (i > 0)               sum += obj->grid[i - 1][j];
    if (i < obj->n - 1)      sum += obj->grid[i + 1][j];
    if (j > 0)               sum += obj->grid[i][j - 1];
    if (j < obj->n - 1)      sum += obj->grid[i][j + 1];
    return sum;
}

int neighborSumDiagonalSum(NeighborSum* obj, int value) {
    int i = obj->rowPos[value];
    int j = obj->colPos[value];
    int sum = 0;
    if (i > 0 && j > 0)               sum += obj->grid[i - 1][j - 1];
    if (i > 0 && j < obj->n - 1)      sum += obj->grid[i - 1][j + 1];
    if (i < obj->n - 1 && j > 0)      sum += obj->grid[i + 1][j - 1];
    if (i < obj->n - 1 && j < obj->n - 1) sum += obj->grid[i + 1][j + 1];
    return sum;
}

void neighborSumFree(NeighborSum* obj) {
    if (!obj) return;
    free(obj->rowPos);
    free(obj->colPos);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class NeighborSum {
    private readonly int[][] _grid;
    private readonly int _n;
    private readonly Dictionary<int, (int i, int j)> _pos;

    public NeighborSum(int[][] grid) {
        _grid = grid;
        _n = grid.Length;
        _pos = new Dictionary<int, (int, int)>(_n * _n);
        for (int i = 0; i < _n; i++) {
            for (int j = 0; j < _n; j++) {
                _pos[grid[i][j]] = (i, j);
            }
        }
    }

    public int AdjacentSum(int value) {
        var (i, j) = _pos[value];
        int sum = 0;
        if (i > 0) sum += _grid[i - 1][j];
        if (i < _n - 1) sum += _grid[i + 1][j];
        if (j > 0) sum += _grid[i][j - 1];
        if (j < _n - 1) sum += _grid[i][j + 1];
        return sum;
    }

    public int DiagonalSum(int value) {
        var (i, j) = _pos[value];
        int sum = 0;
        if (i > 0 && j > 0) sum += _grid[i - 1][j - 1];
        if (i > 0 && j < _n - 1) sum += _grid[i - 1][j + 1];
        if (i < _n - 1 && j > 0) sum += _grid[i + 1][j - 1];
        if (i < _n - 1 && j < _n - 1) sum += _grid[i + 1][j + 1];
        return sum;
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.AdjacentSum(value);
 * int param_2 = obj.DiagonalSum(value);
 */
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 */
var NeighborSum = function(grid) {
    this.grid = grid;
    this.n = grid.length;
    this.pos = new Map(); // value -> [i, j]
    for (let i = 0; i < this.n; i++) {
        for (let j = 0; j < this.n; j++) {
            this.pos.set(grid[i][j], [i, j]);
        }
    }
};

/** 
 * @param {number} value
 * @return {number}
 */
NeighborSum.prototype.adjacentSum = function(value) {
    const coord = this.pos.get(value);
    if (!coord) return 0;
    const [i, j] = coord;
    let sum = 0;
    if (i > 0) sum += this.grid[i - 1][j];
    if (i < this.n - 1) sum += this.grid[i + 1][j];
    if (j > 0) sum += this.grid[i][j - 1];
    if (j < this.n - 1) sum += this.grid[i][j + 1];
    return sum;
};

/** 
 * @param {number} value
 * @return {number}
 */
NeighborSum.prototype.diagonalSum = function(value) {
    const coord = this.pos.get(value);
    if (!coord) return 0;
    const [i, j] = coord;
    let sum = 0;
    if (i > 0 && j > 0) sum += this.grid[i - 1][j - 1];
    if (i > 0 && j < this.n - 1) sum += this.grid[i - 1][j + 1];
    if (i < this.n - 1 && j > 0) sum += this.grid[i + 1][j - 1];
    if (i < this.n - 1 && j < this.n - 1) sum += this.grid[i + 1][j + 1];
    return sum;
};
```

## Typescript

```typescript
class NeighborSum {
    private grid: number[][];
    private pos: Map<number, [number, number]>;

    constructor(grid: number[][]) {
        this.grid = grid;
        this.pos = new Map();
        for (let i = 0; i < grid.length; i++) {
            for (let j = 0; j < grid[i].length; j++) {
                this.pos.set(grid[i][j], [i, j]);
            }
        }
    }

    adjacentSum(value: number): number {
        const coord = this.pos.get(value);
        if (!coord) return 0;
        const [i, j] = coord;
        let sum = 0;
        const dirs = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ];
        for (const [di, dj] of dirs) {
            const ni = i + di;
            const nj = j + dj;
            if (ni >= 0 && ni < this.grid.length && nj >= 0 && nj < this.grid[0].length) {
                sum += this.grid[ni][nj];
            }
        }
        return sum;
    }

    diagonalSum(value: number): number {
        const coord = this.pos.get(value);
        if (!coord) return 0;
        const [i, j] = coord;
        let sum = 0;
        const dirs = [
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1]
        ];
        for (const [di, dj] of dirs) {
            const ni = i + di;
            const nj = j + dj;
            if (ni >= 0 && ni < this.grid.length && nj >= 0 && nj < this.grid[0].length) {
                sum += this.grid[ni][nj];
            }
        }
        return sum;
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * var obj = new NeighborSum(grid)
 * var param_1 = obj.adjacentSum(value)
 * var param_2 = obj.diagonalSum(value)
 */
```

## Php

```php
class NeighborSum {
    private array $grid;
    private array $pos = [];
    private int $n;

    /**
     * @param Integer[][] $grid
     */
    public function __construct($grid) {
        $this->grid = $grid;
        $this->n = count($grid);
        for ($i = 0; $i < $this->n; $i++) {
            for ($j = 0; $j < $this->n; $j++) {
                $val = $grid[$i][$j];
                $this->pos[$val] = [$i, $j];
            }
        }
    }

    /**
     * @param Integer $value
     * @return Integer
     */
    public function adjacentSum($value) {
        if (!isset($this->pos[$value])) return 0;
        [$i, $j] = $this->pos[$value];
        $sum = 0;
        // up
        if ($i > 0) $sum += $this->grid[$i - 1][$j];
        // down
        if ($i < $this->n - 1) $sum += $this->grid[$i + 1][$j];
        // left
        if ($j > 0) $sum += $this->grid[$i][$j - 1];
        // right
        if ($j < $this->n - 1) $sum += $this->grid[$i][$j + 1];
        return $sum;
    }

    /**
     * @param Integer $value
     * @return Integer
     */
    public function diagonalSum($value) {
        if (!isset($this->pos[$value])) return 0;
        [$i, $j] = $this->pos[$value];
        $sum = 0;
        // top-left
        if ($i > 0 && $j > 0) $sum += $this->grid[$i - 1][$j - 1];
        // top-right
        if ($i > 0 && $j < $this->n - 1) $sum += $this->grid[$i - 1][$j + 1];
        // bottom-left
        if ($i < $this->n - 1 && $j > 0) $sum += $this->grid[$i + 1][$j - 1];
        // bottom-right
        if ($i < $this->n - 1 && $j < $this->n - 1) $sum += $this->grid[$i + 1][$j + 1];
        return $sum;
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * $obj = new NeighborSum($grid);
 * $ret_1 = $obj->adjacentSum($value);
 * $ret_2 = $obj->diagonalSum($value);
 */
```

## Swift

```swift
class NeighborSum {
    private var pos: [Int: (Int, Int)] = [:]
    private var grid: [[Int]]
    private let n: Int

    init(_ grid: [[Int]]) {
        self.grid = grid
        self.n = grid.count
        for i in 0..<n {
            for j in 0..<n {
                pos[grid[i][j]] = (i, j)
            }
        }
    }

    func adjacentSum(_ value: Int) -> Int {
        guard let (i, j) = pos[value] else { return 0 }
        var sum = 0
        if i > 0 { sum += grid[i - 1][j] }
        if i < n - 1 { sum += grid[i + 1][j] }
        if j > 0 { sum += grid[i][j - 1] }
        if j < n - 1 { sum += grid[i][j + 1] }
        return sum
    }

    func diagonalSum(_ value: Int) -> Int {
        guard let (i, j) = pos[value] else { return 0 }
        var sum = 0
        if i > 0 && j > 0 { sum += grid[i - 1][j - 1] }
        if i > 0 && j < n - 1 { sum += grid[i - 1][j + 1] }
        if i < n - 1 && j > 0 { sum += grid[i + 1][j - 1] }
        if i < n - 1 && j < n - 1 { sum += grid[i + 1][j + 1] }
        return sum
    }
}
```

## Kotlin

```kotlin
class NeighborSum(private val grid: Array<IntArray>) {
    private val position = HashMap<Int, Pair<Int, Int>>()
    private val n = grid.size

    init {
        for (i in 0 until n) {
            for (j in 0 until n) {
                position[grid[i][j]] = i to j
            }
        }
    }

    fun adjacentSum(value: Int): Int {
        val (i, j) = position[value]!!
        var sum = 0
        val dirs = arrayOf(
            intArrayOf(-1, 0),
            intArrayOf(1, 0),
            intArrayOf(0, -1),
            intArrayOf(0, 1)
        )
        for (d in dirs) {
            val ni = i + d[0]
            val nj = j + d[1]
            if (ni in 0 until n && nj in 0 until n) {
                sum += grid[ni][nj]
            }
        }
        return sum
    }

    fun diagonalSum(value: Int): Int {
        val (i, j) = position[value]!!
        var sum = 0
        val dirs = arrayOf(
            intArrayOf(-1, -1),
            intArrayOf(-1, 1),
            intArrayOf(1, -1),
            intArrayOf(1, 1)
        )
        for (d in dirs) {
            val ni = i + d[0]
            val nj = j + d[1]
            if (ni in 0 until n && nj in 0 until n) {
                sum += grid[ni][nj]
            }
        }
        return sum
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * var obj = NeighborSum(grid)
 * var param_1 = obj.adjacentSum(value)
 * var param_2 = obj.diagonalSum(value)
 */
```

## Dart

```dart
class NeighborSum {
  late final List<List<int>> _grid;
  late final Map<int, List<int>> _pos;
  late final int _n;

  NeighborSum(List<List<int>> grid) {
    _grid = grid;
    _n = grid.length;
    _pos = {};
    for (int i = 0; i < _n; ++i) {
      for (int j = 0; j < _n; ++j) {
        _pos[grid[i][j]] = [i, j];
      }
    }
  }

  int adjacentSum(int value) {
    final p = _pos[value]!;
    final i = p[0], j = p[1];
    int sum = 0;
    if (i > 0) sum += _grid[i - 1][j];
    if (i < _n - 1) sum += _grid[i + 1][j];
    if (j > 0) sum += _grid[i][j - 1];
    if (j < _n - 1) sum += _grid[i][j + 1];
    return sum;
  }

  int diagonalSum(int value) {
    final p = _pos[value]!;
    final i = p[0], j = p[1];
    int sum = 0;
    if (i > 0 && j > 0) sum += _grid[i - 1][j - 1];
    if (i > 0 && j < _n - 1) sum += _grid[i - 1][j + 1];
    if (i < _n - 1 && j > 0) sum += _grid[i + 1][j - 1];
    if (i < _n - 1 && j < _n - 1) sum += _grid[i + 1][j + 1];
    return sum;
  }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = NeighborSum(grid);
 * int param1 = obj.adjacentSum(value);
 * int param2 = obj.diagonalSum(value);
 */
```

## Golang

```go
type NeighborSum struct {
	pos  map[int][2]int
	grid [][]int
	n    int
}

func Constructor(grid [][]int) NeighborSum {
	n := len(grid)
	pos := make(map[int][2]int, n*n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			val := grid[i][j]
			pos[val] = [2]int{i, j}
		}
	}
	return NeighborSum{pos: pos, grid: grid, n: n}
}

func (this *NeighborSum) AdjacentSum(value int) int {
	coord := this.pos[value]
	i, j := coord[0], coord[1]
	sum := 0
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for _, d := range dirs {
		ni, nj := i+d[0], j+d[1]
		if ni >= 0 && ni < this.n && nj >= 0 && nj < this.n {
			sum += this.grid[ni][nj]
		}
	}
	return sum
}

func (this *NeighborSum) DiagonalSum(value int) int {
	coord := this.pos[value]
	i, j := coord[0], coord[1]
	sum := 0
	dirs := [][2]int{{-1, -1}, {-1, 1}, {1, -1}, {1, 1}}
	for _, d := range dirs {
		ni, nj := i+d[0], j+d[1]
		if ni >= 0 && ni < this.n && nj >= 0 && nj < this.n {
			sum += this.grid[ni][nj]
		}
	}
	return sum
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * obj := Constructor(grid);
 * param_1 := obj.AdjacentSum(value);
 * param_2 := obj.DiagonalSum(value);
 */
```

## Ruby

```ruby
class NeighborSum
  # :type grid: Integer[][]
  def initialize(grid)
    @grid = grid
    @n = grid.length
    @pos = {}
    grid.each_with_index do |row, i|
      row.each_with_index do |val, j|
        @pos[val] = [i, j]
      end
    end
  end

  # :type value: Integer
  # :rtype: Integer
  def adjacent_sum(value)
    i, j = @pos[value]
    sum = 0
    [[-1, 0], [1, 0], [0, -1], [0, 1]].each do |di, dj|
      ni = i + di
      nj = j + dj
      if ni.between?(0, @n - 1) && nj.between?(0, @n - 1)
        sum += @grid[ni][nj]
      end
    end
    sum
  end

  # :type value: Integer
  # :rtype: Integer
  def diagonal_sum(value)
    i, j = @pos[value]
    sum = 0
    [[-1, -1], [-1, 1], [1, -1], [1, 1]].each do |di, dj|
      ni = i + di
      nj = j + dj
      if ni.between?(0, @n - 1) && nj.between?(0, @n - 1)
        sum += @grid[ni][nj]
      end
    end
    sum
  end
end
```

## Scala

```scala
class NeighborSum(_grid: Array[Array[Int]]) {
  private val n: Int = _grid.length
  private val rows: Array[Int] = new Array[Int](n * n)
  private val cols: Array[Int] = new Array[Int](n * n)

  for (i <- 0 until n; j <- 0 until n) {
    val v = _grid(i)(j)
    rows(v) = i
    cols(v) = j
  }

  def adjacentSum(value: Int): Int = {
    var sum = 0
    val r = rows(value)
    val c = cols(value)
    if (r > 0) sum += _grid(r - 1)(c)
    if (r < n - 1) sum += _grid(r + 1)(c)
    if (c > 0) sum += _grid(r)(c - 1)
    if (c < n - 1) sum += _grid(r)(c + 1)
    sum
  }

  def diagonalSum(value: Int): Int = {
    var sum = 0
    val r = rows(value)
    val c = cols(value)
    if (r > 0 && c > 0) sum += _grid(r - 1)(c - 1)
    if (r > 0 && c < n - 1) sum += _grid(r - 1)(c + 1)
    if (r < n - 1 && c > 0) sum += _grid(r + 1)(c - 1)
    if (r < n - 1 && c < n - 1) sum += _grid(r + 1)(c + 1)
    sum
  }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * val obj = new NeighborSum(grid)
 * val param_1 = obj.adjacentSum(value)
 * val param_2 = obj.diagonalSum(value)
 */
```

## Rust

```rust
struct NeighborSum {
    grid: Vec<Vec<i32>>,
    pos: Vec<(usize, usize)>,
    n: usize,
}

impl NeighborSum {
    fn new(grid: Vec<Vec<i32>>) -> Self {
        let n = grid.len();
        let size = n * n;
        let mut pos = vec![(0usize, 0usize); size];
        for i in 0..n {
            for j in 0..n {
                let val = grid[i][j] as usize;
                pos[val] = (i, j);
            }
        }
        NeighborSum { grid, pos, n }
    }

    fn adjacent_sum(&self, value: i32) -> i32 {
        let (i, j) = self.pos[value as usize];
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        let mut sum = 0;
        for &(dx, dy) in &dirs {
            let ni = i as isize + dx;
            let nj = j as isize + dy;
            if ni >= 0 && (ni as usize) < self.n && nj >= 0 && (nj as usize) < self.n {
                sum += self.grid[ni as usize][nj as usize];
            }
        }
        sum
    }

    fn diagonal_sum(&self, value: i32) -> i32 {
        let (i, j) = self.pos[value as usize];
        let dirs = [(1isize, 1), (1, -1), (-1, 1), (-1, -1)];
        let mut sum = 0;
        for &(dx, dy) in &dirs {
            let ni = i as isize + dx;
            let nj = j as isize + dy;
            if ni >= 0 && (ni as usize) < self.n && nj >= 0 && (nj as usize) < self.n {
                sum += self.grid[ni as usize][nj as usize];
            }
        }
        sum
    }
}
```

## Racket

```racket
(define neighbor-sum%
  (class object%
    (init-field grid)
    (super-new)

    ;; map each value to its coordinates
    (define pos (make-hash))
    (define n (length grid))
    (for ([i (in-range n)]
          [row (in-list grid)])
      (for ([j (in-range n)]
            [val (in-list row)])
        (hash-set! pos val (list i j))))

    (define/public (adjacent-sum value)
      (let* ((coord (hash-ref pos value))
             (i (first coord))
             (j (second coord))
             (dirs '((-1 . 0) (1 . 0) (0 . -1) (0 . 1)))
             (sum 0))
        (for ([d dirs])
          (define ni (+ i (car d)))
          (define nj (+ j (cdr d)))
          (when (and (>= ni 0) (< ni n)
                     (>= nj 0) (< nj n))
            (set! sum (+ sum (list-ref (list-ref grid ni) nj)))))
        sum))

    (define/public (diagonal-sum value)
      (let* ((coord (hash-ref pos value))
             (i (first coord))
             (j (second coord))
             (dirs '((-1 . -1) (-1 . 1) (1 . -1) (1 . 1)))
             (sum 0))
        (for ([d dirs])
          (define ni (+ i (car d)))
          (define nj (+ j (cdr d)))
          (when (and (>= ni 0) (< ni n)
                     (>= nj 0) (< nj n))
            (set! sum (+ sum (list-ref (list-ref grid ni) nj)))))
        sum))))
```

## Erlang

```erlang
-module(neighbor_sum).
-export([neighbor_sum_init_/1,
         neighbor_sum_adjacent_sum/1,
         neighbor_sum_diagonal_sum/1]).

-spec neighbor_sum_init_(Grid :: [[integer()]]) -> any().
neighbor_sum_init_(Grid) ->
    N = length(Grid),
    PosMap = build_pos_map(Grid, 0, #{}),
    put(state, #{grid => Grid, n => N, pos => PosMap}),
    ok.

-spec neighbor_sum_adjacent_sum(Value :: integer()) -> integer().
neighbor_sum_adjacent_sum(Value) ->
    State = get(state),
    PosMap = maps:get(pos, State),
    Grid   = maps:get(grid, State),
    N      = maps:get(n, State),
    {R, C} = maps:get(Value, PosMap),
    AdjDirs = [{-1,0},{1,0},{0,-1},{0,1}],
    lists:foldl(fun({DR, DC}, Acc) ->
        R2 = R + DR,
        C2 = C + DC,
        if
            R2 >= 0, R2 < N, C2 >= 0, C2 < N ->
                RowList = lists:nth(R2 + 1, Grid),
                Val = lists:nth(C2 + 1, RowList),
                Acc + Val;
            true -> Acc
        end
    end, 0, AdjDirs).

-spec neighbor_sum_diagonal_sum(Value :: integer()) -> integer().
neighbor_sum_diagonal_sum(Value) ->
    State = get(state),
    PosMap = maps:get(pos, State),
    Grid   = maps:get(grid, State),
    N      = maps:get(n, State),
    {R, C} = maps:get(Value, PosMap),
    DiaDirs = [{-1,-1},{-1,1},{1,-1},{1,1}],
    lists:foldl(fun({DR, DC}, Acc) ->
        R2 = R + DR,
        C2 = C + DC,
        if
            R2 >= 0, R2 < N, C2 >= 0, C2 < N ->
                RowList = lists:nth(R2 + 1, Grid),
                Val = lists:nth(C2 + 1, RowList),
                Acc + Val;
            true -> Acc
        end
    end, 0, DiaDirs).

%% Helper to build value -> {Row,Col} map (zero‑based indices)
build_pos_map([], _RowIdx, Map) ->
    Map;
build_pos_map([Row|Rest], RowIdx, Map) ->
    NewMap = build_row_map(Row, RowIdx, 0, Map),
    build_pos_map(Rest, RowIdx + 1, NewMap).

build_row_map([], _RowIdx, _ColIdx, Map) ->
    Map;
build_row_map([Val|Vals], RowIdx, ColIdx, Map) ->
    Updated = maps:put(Val, {RowIdx, ColIdx}, Map),
    build_row_map(Vals, RowIdx, ColIdx + 1, Updated).
```

## Elixir

```elixir
defmodule NeighborSum do
  @table :neighbor_sum_table

  @spec init_(grid :: [[integer]]) :: any
  def init_(grid) do
    case :ets.info(@table) do
      :undefined -> :ok
      _ -> :ets.delete(@table)
    end

    :ets.new(@table, [:named_table, :public, read_concurrency: true])

    n = length(grid)

    Enum.with_index(grid)
    |> Enum.each(fn {row, i} ->
      Enum.with_index(row)
      |> Enum.each(fn {val, j} ->
        :ets.insert(@table, {val, {i, j}})
        :ets.insert(@table, {{:coord, i, j}, val})
      end)
    end)

    :ets.insert(@table, {:size, n})
    :ok
  end

  @spec adjacent_sum(value :: integer) :: integer
  def adjacent_sum(value) do
    case :ets.lookup(@table, value) do
      [{^value, {i, j}}] ->
        n = get_size()
        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

        Enum.reduce(dirs, 0, fn {dx, dy}, acc ->
          x = i + dx
          y = j + dy

          if x >= 0 and x < n and y >= 0 and y < n do
            case :ets.lookup(@table, {{:coord, x, y}}) do
              [{_, v}] -> acc + v
              _ -> acc
            end
          else
            acc
          end
        end)

      _ ->
        0
    end
  end

  @spec diagonal_sum(value :: integer) :: integer
  def diagonal_sum(value) do
    case :ets.lookup(@table, value) do
      [{^value, {i, j}}] ->
        n = get_size()
        dirs = [{-1, -1}, {-1, 1}, {1, -1}, {1, 1}]

        Enum.reduce(dirs, 0, fn {dx, dy}, acc ->
          x = i + dx
          y = j + dy

          if x >= 0 and x < n and y >= 0 and y < n do
            case :ets.lookup(@table, {{:coord, x, y}}) do
              [{_, v}] -> acc + v
              _ -> acc
            end
          else
            acc
          end
        end)

      _ ->
        0
    end
  end

  defp get_size do
    case :ets.lookup(@table, :size) do
      [{:size, n}] -> n
      _ -> 0
    end
  end
end
```
