# 2069. Walking Robot Simulation II

## Cpp

```cpp
class Robot {
public:
    Robot(int width, int height) {
        w = width;
        h = height;
        // build perimeter positions
        for (int x = 0; x < w; ++x) pos.emplace_back(x, 0);
        for (int y = 1; y < h; ++y) pos.emplace_back(w - 1, y);
        for (int x = w - 2; x >= 0; --x) pos.emplace_back(x, h - 1);
        for (int y = h - 2; y >= 1; --y) pos.emplace_back(0, y);
        L = pos.size();
        dirs.resize(L);
        // direction at start is East
        dirs[0] = "East";
        for (int i = 1; i < L; ++i) {
            int dx = pos[i].first - pos[i-1].first;
            int dy = pos[i].second - pos[i-1].second;
            if (dx == 1) dirs[i] = "East";
            else if (dx == -1) dirs[i] = "West";
            else if (dy == 1) dirs[i] = "North";
            else if (dy == -1) dirs[i] = "South";
        }
        idx = 0;
    }
    
    void step(int num) {
        idx = (idx + num) % L;
    }
    
    vector<int> getPos() {
        return {pos[idx].first, pos[idx].second};
    }
    
    string getDir() {
        return dirs[idx];
    }
private:
    int w, h, L;
    long long idx;
    vector<pair<int,int>> pos;
    vector<string> dirs;
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
```

## Java

```java
class Robot {
    private final int[] xs;
    private final int[] ys;
    private final String[] dirs;
    private final int perim;
    private int idx;

    public Robot(int width, int height) {
        this.perim = 2 * (width + height) - 4;
        this.xs = new int[perim];
        this.ys = new int[perim];
        this.dirs = new String[perim];
        int k = 0;

        // bottom edge, moving East
        for (int x = 0; x < width; x++) {
            xs[k] = x;
            ys[k] = 0;
            dirs[k] = "East";
            k++;
        }
        // right edge, moving North
        for (int y = 1; y < height; y++) {
            xs[k] = width - 1;
            ys[k] = y;
            dirs[k] = "North";
            k++;
        }
        // top edge, moving West
        for (int x = width - 2; x >= 0; x--) {
            xs[k] = x;
            ys[k] = height - 1;
            dirs[k] = "West";
            k++;
        }
        // left edge, moving South
        for (int y = height - 2; y >= 1; y--) {
            xs[k] = 0;
            ys[k] = y;
            dirs[k] = "South";
            k++;
        }
    }

    public void step(int num) {
        idx = (idx + num) % perim;
    }

    public int[] getPos() {
        return new int[]{xs[idx], ys[idx]};
    }

    public String getDir() {
        return dirs[idx];
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.step(num);
 * int[] param_2 = obj.getPos();
 * String param_3 = obj.getDir();
 */
```

## Python

```python
class Robot(object):
    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.w = width
        self.h = height
        self.L = 2 * (width + height) - 4
        self.pos = []
        self.dir = []

        # bottom edge (East)
        for x in range(width):
            self.pos.append([x, 0])
            self.dir.append("East")
        # right edge (North), skip the corner already added
        for y in range(1, height):
            self.pos.append([width - 1, y])
            self.dir.append("North")
        # top edge (West), skip the corner already added
        for x in range(width - 2, -1, -1):
            self.pos.append([x, height - 1])
            self.dir.append("West")
        # left edge (South), skip both corners already added
        for y in range(height - 2, 0, -1):
            self.pos.append([0, y])
            self.dir.append("South")

        self.idx = 0

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.idx = (self.idx + num) % self.L

    def getPos(self):
        """
        :rtype: List[int]
        """
        return list(self.pos[self.idx])

    def getDir(self):
        """
        :rtype: str
        """
        return self.dir[self.idx]
```

## Python3

```python
from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # perimeter length
        self.L = 2 * (width + height) - 4
        # precompute positions and directions in counter‑clockwise order starting at (0,0) facing East
        self.pos: List[List[int]] = []
        self.dir: List[str] = []

        # bottom edge (y = 0), x from 0 to width-1
        for x in range(width):
            self.pos.append([x, 0])
            self.dir.append("East")
        # right edge (x = width-1), y from 1 to height-1
        for y in range(1, height):
            self.pos.append([width - 1, y])
            self.dir.append("North")
        # top edge (y = height-1), x from width-2 down to 0
        for x in range(width - 2, -1, -1):
            self.pos.append([x, height - 1])
            self.dir.append("West")
        # left edge (x = 0), y from height-2 down to 1
        for y in range(height - 2, 0, -1):
            self.pos.append([0, y])
            self.dir.append("South")

        self.idx = 0  # current index on the perimeter

    def step(self, num: int) -> None:
        self.idx = (self.idx + num) % self.L

    def getPos(self) -> List[int]:
        return self.pos[self.idx][:]

    def getDir(self) -> str:
        return self.dir[self.idx]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int width;
    int height;
    int perim;
    int *xs;
    int *ys;
    char *dirIdxArr;   // 0:East,1:North,2:West,3:South
    int posIdx;
} Robot;

static const char *DIR_STR[4] = {"East", "North", "West", "South"};

Robot* robotCreate(int width, int height) {
    Robot* obj = (Robot*)malloc(sizeof(Robot));
    obj->width = width;
    obj->height = height;
    obj->perim = 2 * (width + height) - 4;

    obj->xs = (int *)malloc(obj->perim * sizeof(int));
    obj->ys = (int *)malloc(obj->perim * sizeof(int));
    obj->dirIdxArr = (char *)malloc(obj->perim * sizeof(char));

    int x = 0, y = 0;
    int d = 0; // 0:East
    for (int i = 0; i < obj->perim; ++i) {
        obj->xs[i] = x;
        obj->ys[i] = y;
        obj->dirIdxArr[i] = (char)d;

        int nx = x, ny = y;
        if (d == 0) nx = x + 1;
        else if (d == 1) ny = y + 1;
        else if (d == 2) nx = x - 1;
        else ny = y - 1;

        if (nx < 0 || nx >= width || ny < 0 || ny >= height) {
            d = (d + 1) % 4; // turn left
            if (d == 0) nx = x + 1, ny = y;
            else if (d == 1) nx = x, ny = y + 1;
            else if (d == 2) nx = x - 1, ny = y;
            else nx = x, ny = y - 1;
        }
        x = nx;
        y = ny;
    }

    obj->posIdx = 0;
    return obj;
}

void robotStep(Robot* obj, int num) {
    if (obj->perim == 0) return;
    obj->posIdx = (obj->posIdx + num) % obj->perim;
}

int* robotGetPos(Robot* obj, int* retSize) {
    *retSize = 2;
    int* res = (int*)malloc(2 * sizeof(int));
    res[0] = obj->xs[obj->posIdx];
    res[1] = obj->ys[obj->posIdx];
    return res;
}

char* robotGetDir(Robot* obj) {
    return (char *)DIR_STR[(int)obj->dirIdxArr[obj->posIdx]];
}

void robotFree(Robot* obj) {
    if (!obj) return;
    free(obj->xs);
    free(obj->ys);
    free(obj->dirIdxArr);
    free(obj);
}

/**
 * Your Robot struct will be instantiated and called as such:
 * Robot* obj = robotCreate(width, height);
 * robotStep(obj, num);
 *
 * int* param_2 = robotGetPos(obj, retSize);
 *
 * char* param_3 = robotGetDir(obj);
 *
 * robotFree(obj);
 */
```

## Csharp

```csharp
public class Robot
{
    private readonly int[] _x;
    private readonly int[] _y;
    private readonly string[] _dir;
    private int _posIdx;
    private readonly int _len;

    public Robot(int width, int height)
    {
        int w = width, h = height;
        _len = 2 * (w + h) - 4;
        _x = new int[_len];
        _y = new int[_len];
        _dir = new string[_len];

        int i = 0;
        // bottom edge: left to right
        for (int x = 0; x < w; x++)
        {
            _x[i] = x;
            _y[i] = 0;
            _dir[i] = "East";
            i++;
        }
        // right edge: bottom+1 to top
        for (int y = 1; y < h; y++)
        {
            _x[i] = w - 1;
            _y[i] = y;
            _dir[i] = "North";
            i++;
        }
        // top edge: right-1 down to left
        for (int x = w - 2; x >= 0; x--)
        {
            _x[i] = x;
            _y[i] = h - 1;
            _dir[i] = "West";
            i++;
        }
        // left edge: top-1 down to bottom+1
        for (int y = h - 2; y >= 1; y--)
        {
            _x[i] = 0;
            _y[i] = y;
            _dir[i] = "South";
            i++;
        }
        // start at (0,0) facing East -> index 0
        _posIdx = 0;
    }

    public void Step(int num)
    {
        _posIdx = (_posIdx + num) % _len;
    }

    public int[] GetPos()
    {
        return new int[] { _x[_posIdx], _y[_posIdx] };
    }

    public string GetDir()
    {
        return _dir[_posIdx];
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.Step(num);
 * int[] param_2 = obj.GetPos();
 * string param_3 = obj.GetDir();
 */
```

## Javascript

```javascript
/**
 * @param {number} width
 * @param {number} height
 */
var Robot = function(width, height) {
    this.perim = [];
    // bottom edge (left to right)
    for (let x = 0; x < width; x++) {
        this.perim.push({ x: x, y: 0 });
    }
    // right edge (bottom+1 to top)
    for (let y = 1; y < height; y++) {
        this.perim.push({ x: width - 1, y: y });
    }
    // top edge (right-1 to left)
    for (let x = width - 2; x >= 0; x--) {
        this.perim.push({ x: x, y: height - 1 });
    }
    // left edge (top-1 down to bottom+1)
    for (let y = height - 2; y > 0; y--) {
        this.perim.push({ x: 0, y: y });
    }

    this.L = this.perim.length;
    this.dirs = new Array(this.L);
    for (let i = 0; i < this.L; i++) {
        if (i === 0) {
            this.dirs[i] = "East";
        } else {
            const prev = this.perim[i - 1];
            const cur = this.perim[i];
            if (cur.x > prev.x) this.dirs[i] = "East";
            else if (cur.y > prev.y) this.dirs[i] = "North";
            else if (cur.x < prev.x) this.dirs[i] = "West";
            else this.dirs[i] = "South";
        }
    }

    this.idx = 0; // start at (0,0)
};

/** 
 * @param {number} num
 * @return {void}
 */
Robot.prototype.step = function(num) {
    this.idx = (this.idx + num) % this.L;
};

/**
 * @return {number[]}
 */
Robot.prototype.getPos = function() {
    const p = this.perim[this.idx];
    return [p.x, p.y];
};

/**
 * @return {string}
 */
Robot.prototype.getDir = function() {
    return this.dirs[this.idx];
};
```

## Typescript

```typescript
class Robot {
    private xs: number[];
    private ys: number[];
    private dirs: string[];
    private idx: number;
    private L: number;

    constructor(width: number, height: number) {
        this.xs = [];
        this.ys = [];
        this.dirs = [];

        // Bottom edge (East)
        for (let x = 0; x < width; x++) {
            this.xs.push(x);
            this.ys.push(0);
            this.dirs.push("East");
        }
        // Right edge (North), skip bottom-right corner
        for (let y = 1; y < height; y++) {
            this.xs.push(width - 1);
            this.ys.push(y);
            this.dirs.push("North");
        }
        // Top edge (West), skip top-right corner
        for (let x = width - 2; x >= 0; x--) {
            this.xs.push(x);
            this.ys.push(height - 1);
            this.dirs.push("West");
        }
        // Left edge (South), skip top-left and bottom-left corners
        for (let y = height - 2; y >= 1; y--) {
            this.xs.push(0);
            this.ys.push(y);
            this.dirs.push("South");
        }

        this.L = this.xs.length;
        this.idx = 0; // start at (0,0) facing East
    }

    step(num: number): void {
        this.idx = (this.idx + num) % this.L;
    }

    getPos(): number[] {
        return [this.xs[this.idx], this.ys[this.idx]];
    }

    getDir(): string {
        return this.dirs[this.idx];
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = new Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */
```

## Php

```php
class Robot {
    private $posX = [];
    private $posY = [];
    private $dirs = [];
    private $idx = 0;
    private $L = 0;

    /**
     * @param Integer $width
     * @param Integer $height
     */
    function __construct($width, $height) {
        $w = $width;
        $h = $height;
        $this->L = 2 * ($w + $h) - 4;

        // bottom edge (East)
        for ($x = 0; $x < $w; $x++) {
            $this->posX[] = $x;
            $this->posY[] = 0;
            $this->dirs[] = ($x == $w - 1) ? "North" : "East";
        }

        // right edge (North)
        for ($y = 1; $y < $h; $y++) {
            $this->posX[] = $w - 1;
            $this->posY[] = $y;
            $this->dirs[] = ($y == $h - 1) ? "West" : "North";
        }

        // top edge (West)
        for ($x = $w - 2; $x >= 0; $x--) {
            $this->posX[] = $x;
            $this->posY[] = $h - 1;
            $this->dirs[] = ($x == 0) ? "South" : "West";
        }

        // left edge (South)
        for ($y = $h - 2; $y >= 1; $y--) {
            $this->posX[] = 0;
            $this->posY[] = $y;
            $this->dirs[] = "South";
        }
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function step($num) {
        $this->idx = ($this->idx + $num) % $this->L;
    }

    /**
     * @return Integer[]
     */
    function getPos() {
        return [$this->posX[$this->idx], $this->posY[$this->idx]];
    }

    /**
     * @return String
     */
    function getDir() {
        return $this->dirs[$this->idx];
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * $obj = new Robot($width, $height);
 * $obj->step($num);
 * $ret_2 = $obj->getPos();
 * $ret_3 = $obj->getDir();
 */
```

## Swift

```swift
class Robot {
    private var xs: [Int]
    private var ys: [Int]
    private var dirs: [String]
    private var idx: Int = 0
    private let L: Int

    init(_ width: Int, _ height: Int) {
        var xArr = [Int]()
        var yArr = [Int]()
        var dArr = [String]()

        // Bottom edge (left to right)
        for x in 0..<width {
            xArr.append(x)
            yArr.append(0)
            if x == width - 1 {
                dArr.append("North")
            } else {
                dArr.append("East")
            }
        }

        // Right edge (bottom to top, excluding bottom corner)
        if height > 1 {
            for y in 1..<height {
                xArr.append(width - 1)
                yArr.append(y)
                if y == height - 1 {
                    dArr.append("West")
                } else {
                    dArr.append("North")
                }
            }
        }

        // Top edge (right to left, excluding right corner)
        if width > 1 && height > 0 {
            for x in stride(from: width - 2, through: 0, by: -1) {
                xArr.append(x)
                yArr.append(height - 1)
                if x == 0 {
                    dArr.append("South")
                } else {
                    dArr.append("West")
                }
            }
        }

        // Left edge (top to bottom, excluding both corners)
        if height > 2 && width > 1 {
            for y in stride(from: height - 2, through: 1, by: -1) {
                xArr.append(0)
                yArr.append(y)
                dArr.append("South")
            }
        }

        self.xs = xArr
        self.ys = yArr
        self.dirs = dArr
        self.L = xs.count
    }

    func step(_ num: Int) {
        idx = (idx + num) % L
    }

    func getPos() -> [Int] {
        return [xs[idx], ys[idx]]
    }

    func getDir() -> String {
        return dirs[idx]
    }
}
```

## Kotlin

```kotlin
class Robot(width: Int, height: Int) {
    private val xs: IntArray
    private val ys: IntArray
    private val dirs: Array<String>
    private var idx = 0

    init {
        val perim = 2 * (width + height) - 4
        xs = IntArray(perim)
        ys = IntArray(perim)
        dirs = Array(perim) { "" }
        var p = 0
        // start cell
        xs[p] = 0; ys[p] = 0; dirs[p] = "East"; p++
        // move east along bottom row (excluding start)
        for (i in 1 until width) {
            xs[p] = i; ys[p] = 0; dirs[p] = "East"; p++
        }
        // move north along right column
        for (j in 1 until height) {
            xs[p] = width - 1; ys[p] = j; dirs[p] = "North"; p++
        }
        // move west along top row
        for (i in width - 2 downTo 0) {
            xs[p] = i; ys[p] = height - 1; dirs[p] = "West"; p++
        }
        // move south along left column (excluding corners)
        for (j in height - 2 downTo 1) {
            xs[p] = 0; ys[p] = j; dirs[p] = "South"; p++
        }
    }

    fun step(num: Int) {
        val perim = xs.size
        idx = (idx + num % perim) % perim
    }

    fun getPos(): IntArray {
        return intArrayOf(xs[idx], ys[idx])
    }

    fun getDir(): String {
        return dirs[idx]
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */
```

## Dart

```dart
class Robot {
  final int width;
  final int height;
  late final List<List<int>> positions;
  late final List<String> directions;
  int idx = 0;
  late final int perimeter;

  Robot(int width, int height)
      : width = width,
        height = height {
    perimeter = 2 * (width + height) - 4;
    positions = List.generate(perimeter, (_) => [0, 0]);
    directions = List.filled(perimeter, '');
    _precompute();
  }

  void _precompute() {
    int x = 0, y = 0;
    int dirIdx = 0; // 0: East, 1: North, 2: West, 3: South
    const dirs = ['East', 'North', 'West', 'South'];
    const dx = [1, 0, -1, 0];
    const dy = [0, 1, 0, -1];

    for (int i = 0; i < perimeter; i++) {
      positions[i][0] = x;
      positions[i][1] = y;
      directions[i] = dirs[dirIdx];

      int nx = x + dx[dirIdx];
      int ny = y + dy[dirIdx];
      if (nx < 0 || nx >= width || ny < 0 || ny >= height) {
        dirIdx = (dirIdx + 1) % 4; // turn left
        nx = x + dx[dirIdx];
        ny = y + dy[dirIdx];
      }
      x = nx;
      y = ny;
    }
  }

  void step(int num) {
    idx = (idx + num) % perimeter;
  }

  List<int> getPos() {
    return positions[idx];
  }

  String getDir() {
    return directions[idx];
  }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = Robot(width, height);
 * obj.step(num);
 * List<int> param2 = obj.getPos();
 * String param3 = obj.getDir();
 */
```

## Golang

```go
type Robot struct {
	xs    []int
	ys    []int
	dir   []string
	idx   int
	perim int
}

func Constructor(width int, height int) Robot {
	if width < 2 || height < 2 {
		return Robot{}
	}
	perim := 2*(width+height) - 4
	xs := make([]int, perim)
	ys := make([]int, perim)
	dir := make([]string, perim)

	i := 0
	// start position (0,0), facing East
	xs[0], ys[0] = 0, 0
	dir[0] = "East"
	i++

	// bottom edge moving east (excluding starting cell)
	for x := 1; x < width; x++ {
		xs[i], ys[i] = x, 0
		dir[i] = "East"
		i++
	}
	// right edge moving north (exclude corner already added)
	for y := 1; y < height; y++ {
		xs[i], ys[i] = width-1, y
		dir[i] = "North"
		i++
	}
	// top edge moving west (exclude corner)
	for x := width - 2; x >= 0; x-- {
		xs[i], ys[i] = x, height-1
		dir[i] = "West"
		i++
	}
	// left edge moving south (exclude both corners)
	for y := height - 2; y > 0; y-- {
		xs[i], ys[i] = 0, y
		dir[i] = "South"
		i++
	}

	return Robot{
		xs:    xs,
		ys:    ys,
		dir:   dir,
		idx:   0,
		perim: perim,
	}
}

func (this *Robot) Step(num int) {
	if this.perim == 0 {
		return
	}
	this.idx = (this.idx + num) % this.perim
}

func (this *Robot) GetPos() []int {
	return []int{this.xs[this.idx], this.ys[this.idx]}
}

func (this *Robot) GetDir() string {
	return this.dir[this.idx]
}

/**
 * Your Robot object will be instantiated and called as such:
 * obj := Constructor(width, height);
 * obj.Step(num);
 * param_2 := obj.GetPos();
 * param_3 := obj.GetDir();
 */
```

## Ruby

```ruby
class Robot
  def initialize(width, height)
    @w = width
    @h = height
    @perim = 2 * (@w + @h) - 4
    @idx = 0
  end

  def step(num)
    @idx = (@idx + num) % @perim
  end

  def get_pos
    x, y = pos_from_idx(@idx)
    [x, y]
  end

  def get_dir
    _, y = pos_from_idx(@idx)
    if y == 0
      "East"
    elsif (x = pos_from_idx(@idx)[0]) == @w - 1
      "North"
    elsif y == @h - 1
      "West"
    else
      "South"
    end
  end

  private

  def pos_from_idx(idx)
    w = @w
    h = @h
    if idx < w
      # bottom edge
      [idx, 0]
    elsif idx < w + h - 1
      # right edge (excluding bottom corner)
      [w - 1, idx - (w - 1)]
    elsif idx < w + h - 1 + w - 1
      # top edge (excluding right corner)
      offset = idx - (w + h - 1)
      [w - 2 - offset, h - 1]
    else
      # left edge (excluding top and bottom corners)
      offset = idx - (w + h - 1 + w - 1)
      [0, h - 2 - offset]
    end
  end
end
```

## Scala

```scala
class Robot(_width: Int, _height: Int) {
  private val w = _width
  private val h = _height
  private val perim = 2 * w + 2 * h - 4
  private val xs = new Array[Int](perim)
  private val ys = new Array[Int](perim)
  private val dirs = new Array[String](perim)

  {
    var pos = 0
    // bottom row (left to right)
    for (x <- 0 until w) {
      xs(pos) = x
      ys(pos) = 0
      dirs(pos) = if (x == w - 1) "North" else "East"
      pos += 1
    }
    // right column (bottom+1 to top)
    for (y <- 1 until h) {
      xs(pos) = w - 1
      ys(pos) = y
      dirs(pos) = if (y == h - 1) "West" else "North"
      pos += 1
    }
    // top row (right-1 to left)
    for (x <- (w - 2) to 0 by -1) {
      xs(pos) = x
      ys(pos) = h - 1
      dirs(pos) = if (x == 0) "South" else "West"
      pos += 1
    }
    // left column (top-1 down to bottom+1)
    for (y <- (h - 2) to 1 by -1) {
      xs(pos) = 0
      ys(pos) = y
      dirs(pos) = "South"
      pos += 1
    }
  }

  private var idx: Int = 0

  def step(num: Int): Unit = {
    idx = (idx + num) % perim
  }

  def getPos(): Array[Int] = {
    Array(xs(idx), ys(idx))
  }

  def getDir(): String = {
    dirs(idx)
  }
}

/**
 * Your Robot object will be instantiated and called as such:
 * val obj = new Robot(width, height)
 * obj.step(num)
 * val param_2 = obj.getPos()
 * val param_3 = obj.getDir()
 */
```

## Rust

```rust
use std::cell::Cell;

pub struct Robot {
    states: Vec<(i32, i32, u8)>,
    period: usize,
    idx: Cell<usize>,
}

impl Robot {
    pub fn new(width: i32, height: i32) -> Self {
        let perim_len = 2 * (width + height) - 4; // number of distinct perimeter cells
        let period = (2 * perim_len) as usize;   // full cycle length for state (position+direction)

        // direction order: East(0), North(1), West(2), South(3)
        let dirs: [(i32, i32); 4] = [(1, 0), (0, 1), (-1, 0), (0, -1)];

        let mut states = Vec::with_capacity(period);
        let mut x = 0;
        let mut y = 0;
        let mut d: usize = 0; // start facing East

        states.push((x, y, d as u8));

        while states.len() < period {
            let (dx, dy) = dirs[d];
            let nx = x + dx;
            let ny = y + dy;

            if nx < 0 || nx >= width || ny < 0 || ny >= height {
                // turn left (counter‑clockwise)
                d = (d + 1) % 4;
                let (dx2, dy2) = dirs[d];
                x += dx2;
                y += dy2;
            } else {
                x = nx;
                y = ny;
            }
            states.push((x, y, d as u8));
        }

        Robot {
            states,
            period,
            idx: Cell::new(0),
        }
    }

    pub fn step(&self, num: i32) {
        let cur = self.idx.get();
        let new_idx = (cur + num as usize) % self.period;
        self.idx.set(new_idx);
    }

    pub fn get_pos(&self) -> Vec<i32> {
        let (x, y, _) = self.states[self.idx.get()];
        vec![x, y]
    }

    pub fn get_dir(&self) -> String {
        const DIR_STR: [&str; 4] = ["East", "North", "West", "South"];
        let (_, _, d) = self.states[self.idx.get()];
        DIR_STR[d as usize].to_string()
    }
}

/*
Your Robot object will be instantiated and called as such:
let obj = Robot::new(width, height);
obj.step(num);
let ret_2: Vec<i32> = obj.get_pos();
let ret_3: String = obj.get_dir();
*/
```

## Racket

```racket
(define robot%
  (class object%
    (super-new)
    (init-field width height)

    (define L (+ (* 2 width) (* 2 height) -4))
    (define cur-idx 0)

    (define/public (step num)
      (set! cur-idx (modulo (+ cur-idx num) L)))

    (define/public (get-pos)
      (let* ((idx cur-idx)
             (w width)
             (h height))
        (cond
          [(< idx w)                     ; bottom edge
           (list idx 0)]
          [(< idx (+ w (- h 1)))         ; right edge
           (let ((y (- idx w)))
             (list (- w 1) (+ y 1)))]
          [(< idx (+ w (- h 1) (- w 1))) ; top edge
           (let ((offset (- idx (+ w (- h 1)))))
             (list (- (- w 2) offset) (- h 1)))]
          [else                          ; left edge
           (let ((offset (- idx (+ w (- h 1) (- w 1)))))
             (list 0 (- (- h 2) offset)))])))

    (define/public (get-dir)
      (let* ((idx cur-idx)
             (w width)
             (h height))
        (cond
          [(< idx w) "East"]
          [(< idx (+ w (- h 1))) "North"]
          [(< idx (+ w (- h 1) (- w 1))) "West"]
          [else "South"]))))
```

## Erlang

```erlang
-spec robot_init_(Width :: integer(), Height :: integer()) -> any().
robot_init_(Width, Height) ->
    put(width, Width),
    put(height, Height),
    East = [{X,0} || X <- lists:seq(0, Width-1)],
    North = [{Width-1,Y} || Y <- lists:seq(1, Height-1)],
    West = [{X,Height-1} || X <- lists:seq(Width-2, 0, -1)],
    South = [{0,Y} || Y <- lists:seq(Height-2, 1, -1)],
    Perim = East ++ North ++ West ++ South,
    put(perimeter, Perim),
    put(len, length(Perim)),
    put(idx, 0),
    ok.

-spec robot_step(Num :: integer()) -> any().
robot_step(Num) ->
    Idx = get(idx),
    L = get(len),
    NewIdx = (Idx + Num) rem L,
    put(idx, NewIdx),
    ok.

-spec robot_get_pos() -> [integer()].
robot_get_pos() ->
    Perim = get(perimeter),
    Idx = get(idx),
    {X,Y} = lists:nth(Idx + 1, Perim),
    [X, Y].

-spec robot_get_dir() -> unicode:unicode_binary().
robot_get_dir() ->
    Width = get(width),
    Height = get(height),
    Pos = robot_get_pos(),
    [X,Y] = Pos,
    case {X,Y} of
        {_,0} when X < Width-1 -> <<"East">>;
        {W,_} when W =:= Width-1, Y < Height-1 -> <<"North">>;
        {_,H} when H =:= Height-1, X > 0 -> <<"West">>;
        _ -> <<"South">>
    end.
```

## Elixir

```elixir
defmodule Robot do
  @spec init_(width :: integer, height :: integer) :: any
  def init_(width, height) do
    perimeter = 2 * (width + height) - 4
    Process.put(:robot_state, %{w: width, h: height, len: perimeter, idx: 0})
    nil
  end

  @spec step(num :: integer) :: any
  def step(num) do
    state = Process.get(:robot_state)
    new_idx = rem(state.idx + num, state.len)
    Process.put(:robot_state, %{state | idx: new_idx})
    nil
  end

  @spec get_pos() :: [integer]
  def get_pos() do
    {x, y, _dir} = current_pos_dir()
    [x, y]
  end

  @spec get_dir() :: String.t()
  def get_dir() do
    {_x, _y, dir} = current_pos_dir()
    dir
  end

  # Helper to compute position and direction from current index
  defp current_pos_dir() do
    state = Process.get(:robot_state)
    w = state.w
    h = state.h
    idx = state.idx

    {x, y} =
      cond do
        idx < w ->
          {idx, 0}

        idx < w + h - 1 ->
          i = idx - w
          {w - 1, i + 1}

        idx < w + h - 1 + w - 1 ->
          i = idx - (w + h - 1)
          {w - 2 - i, h - 1}

        true ->
          i = idx - (w + h - 1 + w - 1)
          {0, h - 2 - i}
      end

    dir =
      cond do
        x == 0 and y == 0 -> "East"
        x == w - 1 and y == 0 -> "North"
        x == w - 1 and y == h - 1 -> "West"
        x == 0 and y == h - 1 -> "South"
        y == 0 -> "East"
        x == w - 1 -> "North"
        y == h - 1 -> "West"
        x == 0 -> "South"
      end

    {x, y, dir}
  end
end
```
