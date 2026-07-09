# 3235. Check if the Rectangle Corner Is Reachable

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, r;
        DSU(int n): p(n), r(n,0) { iota(p.begin(), p.end(), 0); }
        int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(r[a]<r[b]) swap(a,b);
            p[b]=a;
            if(r[a]==r[b]) r[a]++;
        }
    };
    
    bool canReachCorner(int xCorner, int yCorner, vector<vector<int>>& circles) {
        int n = circles.size();
        const int LEFT = n;
        const int RIGHT = n+1;
        const int BOTTOM = n+2;
        const int TOP = n+3;
        DSU dsu(n+4);
        
        // Union circles with edges they touch
        for(int i=0;i<n;++i){
            long long x = circles[i][0];
            long long y = circles[i][1];
            long long r = circles[i][2];
            if (x - r <= 0) dsu.unite(i, LEFT);
            if (x + r >= xCorner) dsu.unite(i, RIGHT);
            if (y - r <= 0) dsu.unite(i, BOTTOM);
            if (y + r >= yCorner) dsu.unite(i, TOP);
        }
        
        // Union intersecting circles
        for(int i=0;i<n;++i){
            long long xi = circles[i][0];
            long long yi = circles[i][1];
            long long ri = circles[i][2];
            for(int j=i+1;j<n;++j){
                long long xj = circles[j][0];
                long long yj = circles[j][1];
                long long rj = circles[j][2];
                long long dx = xi - xj;
                long long dy = yi - yj;
                __int128 dist2 = (__int128)dx*dx + (__int128)dy*dy;
                long long sum = ri + rj;
                __int128 rad2 = (__int128)sum * sum;
                if (dist2 <= rad2) dsu.unite(i, j);
            }
        }
        
        // Check blocking conditions
        if (dsu.find(LEFT) == dsu.find(RIGHT)) return false;
        if (dsu.find(TOP) == dsu.find(BOTTOM)) return false;
        if (dsu.find(LEFT) == dsu.find(BOTTOM)) return false; // start corner blocked
        if (dsu.find(RIGHT) == dsu.find(TOP)) return false;   // end corner blocked
        
        return true;
    }
};
```

## Java

```java
class Solution {
    private static class DSU {
        int[] parent;
        byte[] rank;
        DSU(int n) {
            parent = new int[n];
            rank = new byte[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void union(int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return;
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb;
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra;
            } else {
                parent[rb] = ra;
                rank[ra]++;
            }
        }
    }

    public boolean canReachCorner(int xCorner, int yCorner, int[][] circles) {
        int n = circles.length;
        // indices for sides
        int LEFT = n;
        int RIGHT = n + 1;
        int BOTTOM = n + 2;
        int TOP = n + 3;

        DSU dsu = new DSU(n + 4);

        // Union circles that intersect or touch
        for (int i = 0; i < n; i++) {
            long xi = circles[i][0];
            long yi = circles[i][1];
            long ri = circles[i][2];

            // Touch sides
            if (xi - ri <= 0) dsu.union(i, LEFT);
            if (xi + ri >= xCorner) dsu.union(i, RIGHT);
            if (yi - ri <= 0) dsu.union(i, BOTTOM);
            if (yi + ri >= yCorner) dsu.union(i, TOP);

            // Check with later circles
            for (int j = i + 1; j < n; j++) {
                long xj = circles[j][0];
                long yj = circles[j][1];
                long rj = circles[j][2];

                long dx = xi - xj;
                long dy = yi - yj;
                long distSq = dx * dx + dy * dy;
                long radSum = ri + rj;
                if (distSq <= radSum * radSum) {
                    dsu.union(i, j);
                }
            }
        }

        // Forbidden connections
        boolean leftBottom = dsu.find(LEFT) == dsu.find(BOTTOM);
        boolean rightTop = dsu.find(RIGHT) == dsu.find(TOP);
        boolean leftRight = dsu.find(LEFT) == dsu.find(RIGHT);
        boolean topBottom = dsu.find(TOP) == dsu.find(BOTTOM);

        return !(leftBottom || rightTop || leftRight || topBottom);
    }
}
```

## Python

```python
class Solution(object):
    def canReachCorner(self, xCorner, yCorner, circles):
        """
        :type xCorner: int
        :type yCorner: int
        :type circles: List[List[int]]
        :rtype: bool
        """
        n = len(circles)
        parent = list(range(n + 4))
        rank = [0] * (n + 4)

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        LEFT = n
        RIGHT = n + 1
        BOTTOM = n + 2
        TOP = n + 3

        # Connect circles with rectangle sides they touch
        for i, (x, y, r) in enumerate(circles):
            if x - r <= 0:
                union(i, LEFT)
            if x + r >= xCorner:
                union(i, RIGHT)
            if y - r <= 0:
                union(i, BOTTOM)
            if y + r >= yCorner:
                union(i, TOP)

        # Connect intersecting circles
        for i in range(n):
            xi, yi, ri = circles[i]
            for j in range(i + 1, n):
                xj, yj, rj = circles[j]
                dx = xi - xj
                dy = yi - yj
                dr = ri + rj
                if dx * dx + dy * dy <= dr * dr:
                    union(i, j)

        # Check blocking connections
        if find(LEFT) == find(RIGHT):
            return False
        if find(TOP) == find(BOTTOM):
            return False
        if find(LEFT) == find(BOTTOM):
            return False
        if find(RIGHT) == find(TOP):
            return False
        return True
```

## Python3

```python
class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles):
        n = len(circles)
        parent = list(range(n + 4))
        rank = [0] * (n + 4)

        LEFT, RIGHT, BOTTOM, TOP = n, n + 1, n + 2, n + 3

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        # connect circles with sides
        for i, (x, y, r) in enumerate(circles):
            if x - r <= 0:
                union(i, LEFT)
            if x + r >= xCorner:
                union(i, RIGHT)
            if y - r <= 0:
                union(i, BOTTOM)
            if y + r >= yCorner:
                union(i, TOP)

        # connect intersecting circles
        for i in range(n):
            xi, yi, ri = circles[i]
            for j in range(i + 1, n):
                xj, yj, rj = circles[j]
                dx = xi - xj
                dy = yi - yj
                if dx * dx + dy * dy <= (ri + rj) * (ri + rj):
                    union(i, j)

        # check blocking connections
        if find(LEFT) == find(RIGHT):
            return False
        if find(TOP) == find(BOTTOM):
            return False
        if find(LEFT) == find(BOTTOM):
            return False
        if find(RIGHT) == find(TOP):
            return False
        return True
```

## C

```c
bool canReachCorner(int xCorner, int yCorner, int** circles, int circlesSize, int* circlesColSize) {
    int n = circlesSize;
    int LEFT = n;
    int RIGHT = n + 1;
    int BOTTOM = n + 2;
    int TOP = n + 3;
    int total = n + 4;

    // DSU structures
    int *parent = (int*)malloc(total * sizeof(int));
    int *rank = (int*)calloc(total, sizeof(int));
    for (int i = 0; i < total; ++i) parent[i] = i;

    // Find with path compression
    int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    // Union by rank
    void unite(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra == rb) return;
        if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }
    }

    // Process circles with walls
    for (int i = 0; i < n; ++i) {
        long long xi = circles[i][0];
        long long yi = circles[i][1];
        long long ri = circles[i][2];

        if (xi - ri <= 0) unite(i, LEFT);
        if (xi + ri >= xCorner) unite(i, RIGHT);
        if (yi - ri <= 0) unite(i, BOTTOM);
        if (yi + ri >= yCorner) unite(i, TOP);
    }

    // Process circle-circle intersections
    for (int i = 0; i < n; ++i) {
        long long xi = circles[i][0];
        long long yi = circles[i][1];
        long long ri = circles[i][2];
        for (int j = i + 1; j < n; ++j) {
            long long xj = circles[j][0];
            long long yj = circles[j][1];
            long long rj = circles[j][2];
            long long dx = xi - xj;
            long long dy = yi - yj;
            long long distSq = dx * dx + dy * dy;
            long long radSum = ri + rj;
            if (distSq <= radSum * radSum) {
                unite(i, j);
            }
        }
    }

    bool blocked = false;
    // left-right
    if (find(LEFT) == find(RIGHT)) blocked = true;
    // top-bottom
    if (find(TOP) == find(BOTTOM)) blocked = true;
    // start corner blocked: left-bottom connected
    if (find(LEFT) == find(BOTTOM)) blocked = true;
    // end corner blocked: right-top connected
    if (find(RIGHT) == find(TOP)) blocked = true;

    free(parent);
    free(rank);
    return !blocked;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanReachCorner(int xCorner, int yCorner, int[][] circles)
    {
        int n = circles.Length;
        int left = n;
        int right = n + 1;
        int bottom = n + 2;
        int top = n + 3;

        DSU dsu = new DSU(n + 4);

        for (int i = 0; i < n; i++)
        {
            long x = circles[i][0];
            long y = circles[i][1];
            long r = circles[i][2];

            if (x - r <= 0) dsu.Union(i, left);
            if (x + r >= xCorner) dsu.Union(i, right);
            if (y - r <= 0) dsu.Union(i, bottom);
            if (y + r >= yCorner) dsu.Union(i, top);
        }

        for (int i = 0; i < n; i++)
        {
            long xi = circles[i][0];
            long yi = circles[i][1];
            long ri = circles[i][2];
            for (int j = i + 1; j < n; j++)
            {
                long xj = circles[j][0];
                long yj = circles[j][1];
                long rj = circles[j][2];

                long dx = xi - xj;
                long dy = yi - yj;
                long distSq = dx * dx + dy * dy;
                long radSum = ri + rj;
                if (distSq <= radSum * radSum)
                {
                    dsu.Union(i, j);
                }
            }
        }

        // Check blocking connections
        if (dsu.Find(left) == dsu.Find(right)) return false;
        if (dsu.Find(top) == dsu.Find(bottom)) return false;
        if (dsu.Find(left) == dsu.Find(bottom)) return false;
        if (dsu.Find(right) == dsu.Find(top)) return false;

        return true;
    }

    private class DSU
    {
        private int[] parent;
        private int[] rank;

        public DSU(int size)
        {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) parent[i] = i;
        }

        public int Find(int x)
        {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }

        public void Union(int a, int b)
        {
            int pa = Find(a);
            int pb = Find(b);
            if (pa == pb) return;
            if (rank[pa] < rank[pb])
                parent[pa] = pb;
            else if (rank[pa] > rank[pb])
                parent[pb] = pa;
            else
            {
                parent[pb] = pa;
                rank[pa]++;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} xCorner
 * @param {number} yCorner
 * @param {number[][]} circles
 * @return {boolean}
 */
var canReachCorner = function(xCorner, yCorner, circles) {
    const n = circles.length;
    // side indices: upper, right, lower, left
    const idxUpper = n;       // top edge (y = yCorner)
    const idxRight = n + 1;   // right edge (x = xCorner)
    const idxLower = n + 2;   // bottom edge (y = 0)
    const idxLeft  = n + 3;   // left edge (x = 0)

    const parent = new Array(n + 4);
    const rank = new Array(n + 4).fill(0);
    for (let i = 0; i < n + 4; ++i) parent[i] = i;

    function find(x) {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a, b) {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (rank[ra] < rank[rb]) parent[ra] = rb;
        else if (rank[ra] > rank[rb]) parent[rb] = ra;
        else { parent[rb] = ra; rank[ra]++; }
    }

    // Union circles with sides they touch
    for (let i = 0; i < n; ++i) {
        const [xi, yi, ri] = circles[i];
        if (xi - ri <= 0) union(i, idxLeft);
        if (xi + ri >= xCorner) union(i, idxRight);
        if (yi - ri <= 0) union(i, idxLower);
        if (yi + ri >= yCorner) union(i, idxUpper);
    }

    // Union intersecting circles
    for (let i = 0; i < n; ++i) {
        const [xi, yi, ri] = circles[i];
        for (let j = i + 1; j < n; ++j) {
            const [xj, yj, rj] = circles[j];
            const dx = BigInt(xi - xj);
            const dy = BigInt(yi - yj);
            const dist2 = dx * dx + dy * dy;
            const sumR = BigInt(ri + rj);
            if (dist2 <= sumR * sumR) {
                union(i, j);
            }
        }
    }

    // If any blocking connection exists, path is impossible
    if (find(idxLeft) === find(idxLower)) return false;   // start corner blocked
    if (find(idxRight) === find(idxUpper)) return false;  // end corner blocked
    if (find(idxLeft) === find(idxRight)) return false;   // left-right barrier
    if (find(idxUpper) === find(idxLower)) return false;  // top-bottom barrier

    return true;
};
```

## Typescript

```typescript
function canReachCorner(xCorner: number, yCorner: number, circles: number[][]): boolean {
    const n = circles.length;
    const LEFT = n;
    const RIGHT = n + 1;
    const BOTTOM = n + 2;
    const TOP = n + 3;
    const total = n + 4;

    const parent = new Int32Array(total);
    for (let i = 0; i < total; ++i) parent[i] = i;

    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a: number, b: number): void {
        const ra = find(a);
        const rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    }

    const xC = BigInt(xCorner);
    const yC = BigInt(yCorner);

    // connect circles to sides
    for (let i = 0; i < n; ++i) {
        const [xi, yi, ri] = circles[i];
        const xiB = BigInt(xi);
        const yiB = BigInt(yi);
        const riB = BigInt(ri);

        if (xiB - riB <= 0n) union(i, LEFT);
        if (xC - xiB <= riB) union(i, RIGHT);
        if (yiB - riB <= 0n) union(i, BOTTOM);
        if (yC - yiB <= riB) union(i, TOP);
    }

    // connect circles with each other
    for (let i = 0; i < n; ++i) {
        const [xi, yi, ri] = circles[i];
        const xiB = BigInt(xi);
        const yiB = BigInt(yi);
        const riB = BigInt(ri);
        for (let j = i + 1; j < n; ++j) {
            const [xj, yj, rj] = circles[j];
            const xjB = BigInt(xj);
            const yjB = BigInt(yj);
            const rjB = BigInt(rj);

            const dx = xiB - xjB;
            const dy = yiB - yjB;
            const distSq = dx * dx + dy * dy;
            const radSum = riB + rjB;
            if (distSq <= radSum * radSum) {
                union(i, j);
            }
        }
    }

    // check forbidden connections
    if (find(LEFT) === find(RIGHT)) return false;
    if (find(TOP) === find(BOTTOM)) return false;
    if (find(LEFT) === find(BOTTOM)) return false;
    if (find(RIGHT) === find(TOP)) return false;

    return true;
}
```

## Php

```php
class DSU {
    private $parent = [];
    private $rank = [];

    public function __construct(int $size) {
        for ($i = 0; $i < $size; $i++) {
            $this->parent[$i] = $i;
            $this->rank[$i] = 0;
        }
    }

    public function find(int $x): int {
        if ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    public function union(int $a, int $b): void {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) {
            return;
        }
        if ($this->rank[$pa] < $this->rank[$pb]) {
            $this->parent[$pa] = $pb;
        } elseif ($this->rank[$pa] > $this->rank[$pb]) {
            $this->parent[$pb] = $pa;
        } else {
            $this->parent[$pb] = $pa;
            $this->rank[$pa]++;
        }
    }
}

class Solution {

    /**
     * @param Integer $xCorner
     * @param Integer $yCorner
     * @param Integer[][] $circles
     * @return Boolean
     */
    function canReachCorner($xCorner, $yCorner, $circles) {
        $n = count($circles);
        // indices: top=n, right=n+1, bottom=n+2, left=n+3
        $dsu = new DSU($n + 4);

        for ($i = 0; $i < $n; $i++) {
            [$xi, $yi, $ri] = $circles[$i];
            if ($xi - $ri <= 0) {
                $dsu->union($i, $n + 3); // left
            }
            if ($xi + $ri >= $xCorner) {
                $dsu->union($i, $n + 1); // right
            }
            if ($yi - $ri <= 0) {
                $dsu->union($i, $n + 2); // bottom
            }
            if ($yi + $ri >= $yCorner) {
                $dsu->union($i, $n); // top
            }
        }

        for ($i = 0; $i < $n; $i++) {
            [$xi, $yi, $ri] = $circles[$i];
            for ($j = $i + 1; $j < $n; $j++) {
                [$xj, $yj, $rj] = $circles[$j];
                $dx = $xi - $xj;
                $dy = $yi - $yj;
                $distSq = $dx * $dx + $dy * $dy;
                $radSum = $ri + $rj;
                if ($distSq <= $radSum * $radSum) {
                    $dsu->union($i, $j);
                }
            }
        }

        $left   = $n + 3;
        $right  = $n + 1;
        $bottom = $n + 2;
        $top    = $n;

        if ($dsu->find($left) === $dsu->find($right)) return false;
        if ($dsu->find($top) === $dsu->find($bottom)) return false;
        if ($dsu->find($left) === $dsu->find($bottom)) return false;
        if ($dsu->find($right) === $dsu->find($top)) return false;

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canReachCorner(_ xCorner: Int, _ yCorner: Int, _ circles: [[Int]]) -> Bool {
        let n = circles.count
        // Nodes: 0..n-1 circles, n:left, n+1:right, n+2:bottom, n+3:top
        let leftNode = n
        let rightNode = n + 1
        let bottomNode = n + 2
        let topNode = n + 3
        var parent = Array(0..<(n + 4))
        
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        
        func union(_ a: Int, _ b: Int) {
            let ra = find(a)
            let rb = find(b)
            if ra != rb {
                parent[ra] = rb
            }
        }
        
        // Preprocess circles as Int64 for safe arithmetic
        var xs = [Int64]()
        var ys = [Int64]()
        var rs = [Int64]()
        for c in circles {
            xs.append(Int64(c[0]))
            ys.append(Int64(c[1]))
            rs.append(Int64(c[2]))
        }
        let X = Int64(xCorner)
        let Y = Int64(yCorner)
        
        // Union circles with sides they touch
        for i in 0..<n {
            if xs[i] - rs[i] <= 0 { union(i, leftNode) }
            if xs[i] + rs[i] >= X { union(i, rightNode) }
            if ys[i] - rs[i] <= 0 { union(i, bottomNode) }
            if ys[i] + rs[i] >= Y { union(i, topNode) }
        }
        
        // Union intersecting circles
        for i in 0..<n {
            for j in (i+1)..<n {
                let dx = xs[i] - xs[j]
                let dy = ys[i] - ys[j]
                let dist2 = dx*dx + dy*dy
                let radSum = rs[i] + rs[j]
                if dist2 <= radSum * radSum {
                    union(i, j)
                }
            }
        }
        
        // Check blocking connections
        if find(leftNode) == find(bottomNode) { return false }
        if find(rightNode) == find(topNode) { return false }
        if find(leftNode) == find(rightNode) { return false }
        if find(topNode) == find(bottomNode) { return false }
        
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class DSU(size: Int) {
        private val parent = IntArray(size) { it }
        fun find(x: Int): Int {
            var a = x
            while (parent[a] != a) {
                parent[a] = parent[parent[a]]
                a = parent[a]
            }
            return a
        }
        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            parent[ra] = rb
        }
    }

    fun canReachCorner(xCorner: Int, yCorner: Int, circles: Array<IntArray>): Boolean {
        val n = circles.size
        val left = n
        val right = n + 1
        val bottom = n + 2
        val top = n + 3
        val dsu = DSU(n + 4)

        for (i in 0 until n) {
            val xi = circles[i][0].toLong()
            val yi = circles[i][1].toLong()
            val ri = circles[i][2].toLong()

            if (xi - ri <= 0L) dsu.union(i, left)
            if (xCorner.toLong() - xi <= ri) dsu.union(i, right)
            if (yi - ri <= 0L) dsu.union(i, bottom)
            if (yCorner.toLong() - yi <= ri) dsu.union(i, top)
        }

        for (i in 0 until n) {
            val xi = circles[i][0].toLong()
            val yi = circles[i][1].toLong()
            val ri = circles[i][2].toLong()
            for (j in i + 1 until n) {
                val xj = circles[j][0].toLong()
                val yj = circles[j][1].toLong()
                val rj = circles[j][2].toLong()
                val dx = xi - xj
                val dy = yi - yj
                val distSq = dx * dx + dy * dy
                val radSum = ri + rj
                if (distSq <= radSum * radSum) {
                    dsu.union(i, j)
                }
            }
        }

        if (dsu.find(left) == dsu.find(right)) return false
        if (dsu.find(top) == dsu.find(bottom)) return false
        if (dsu.find(left) == dsu.find(bottom)) return false
        if (dsu.find(right) == dsu.find(top)) return false
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canReachCorner(int xCorner, int yCorner, List<List<int>> circles) {
    int n = circles.length;
    int left = n;
    int right = n + 1;
    int bottom = n + 2;
    int top = n + 3;
    int size = n + 4;

    List<int> parent = List<int>.generate(size, (i) => i);
    List<int> rank = List<int>.filled(size, 0);

    int find(int x) {
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }

    void union(int a, int b) {
      int ra = find(a);
      int rb = find(b);
      if (ra == rb) return;
      if (rank[ra] < rank[rb]) {
        parent[ra] = rb;
      } else if (rank[ra] > rank[rb]) {
        parent[rb] = ra;
      } else {
        parent[rb] = ra;
        rank[ra]++;
      }
    }

    // Connect circles with each other
    for (int i = 0; i < n; ++i) {
      int xi = circles[i][0];
      int yi = circles[i][1];
      int ri = circles[i][2];
      for (int j = i + 1; j < n; ++j) {
        int xj = circles[j][0];
        int yj = circles[j][1];
        int rj = circles[j][2];
        int dx = xi - xj;
        int dy = yi - yj;
        int distSq = dx * dx + dy * dy;
        int radSum = ri + rj;
        if (distSq <= radSum * radSum) {
          union(i, j);
        }
      }
    }

    // Connect circles with rectangle edges
    for (int i = 0; i < n; ++i) {
      int x = circles[i][0];
      int y = circles[i][1];
      int r = circles[i][2];
      if (x - r <= 0) union(i, left);
      if (x + r >= xCorner) union(i, right);
      if (y - r <= 0) union(i, bottom);
      if (y + r >= yCorner) union(i, top);
    }

    bool blocked = false;
    // left-right block
    if (find(left) == find(right)) blocked = true;
    // top-bottom block
    if (find(top) == find(bottom)) blocked = true;
    // start corner blocked (left & bottom)
    if (find(left) == find(bottom)) blocked = true;
    // end corner blocked (right & top)
    if (find(right) == find(top)) blocked = true;

    return !blocked;
  }
}
```

## Golang

```go
package main

type UnionFind struct {
	parent []int
	rank   []int
}

func NewUnionFind(n int) *UnionFind {
	p := make([]int, n)
	r := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
	}
	return &UnionFind{parent: p, rank: r}
}

func (uf *UnionFind) Find(x int) int {
	if uf.parent[x] != x {
		uf.parent[x] = uf.Find(uf.parent[x])
	}
	return uf.parent[x]
}

func (uf *UnionFind) Union(a, b int) {
	ra := uf.Find(a)
	rb := uf.Find(b)
	if ra == rb {
		return
	}
	if uf.rank[ra] < uf.rank[rb] {
		uf.parent[ra] = rb
	} else if uf.rank[ra] > uf.rank[rb] {
		uf.parent[rb] = ra
	} else {
		uf.parent[rb] = ra
		uf.rank[ra]++
	}
}

func canReachCorner(xCorner int, yCorner int, circles [][]int) bool {
	n := len(circles)
	uf := NewUnionFind(n + 4)

	leftIdx := n
	rightIdx := n + 1
	bottomIdx := n + 2
	topIdx := n + 3

	xc := int64(xCorner)
	yc := int64(yCorner)

	for i, c := range circles {
		xi := int64(c[0])
		yi := int64(c[1])
		ri := int64(c[2])

		if xi-ri <= 0 {
			uf.Union(i, leftIdx)
		}
		if xi+ri >= xc {
			uf.Union(i, rightIdx)
		}
		if yi-ri <= 0 {
			uf.Union(i, bottomIdx)
		}
		if yi+ri >= yc {
			uf.Union(i, topIdx)
		}
	}

	for i := 0; i < n; i++ {
		xi := int64(circles[i][0])
		yi := int64(circles[i][1])
		ri := int64(circles[i][2])
		for j := i + 1; j < n; j++ {
			xj := int64(circles[j][0])
			yj := int64(circles[j][1])
			rj := int64(circles[j][2])

			dx := xi - xj
			dy := yi - yj
			distSq := dx*dx + dy*dy
			sumR := ri + rj
			if distSq <= sumR*sumR {
				uf.Union(i, j)
			}
		}
	}

	if uf.Find(leftIdx) == uf.Find(rightIdx) {
		return false
	}
	if uf.Find(topIdx) == uf.Find(bottomIdx) {
		return false
	}
	if uf.Find(leftIdx) == uf.Find(bottomIdx) {
		return false
	}
	if uf.Find(rightIdx) == uf.Find(topIdx) {
		return false
	}
	return true
}
```

## Ruby

```ruby
def can_reach_corner(x_corner, y_corner, circles)
  n = circles.length
  left = n
  right = n + 1
  bottom = n + 2
  top = n + 3

  parent = Array.new(n + 4) { |i| i }
  rank = Array.new(n + 4, 0)

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if rank[ra] < rank[rb]
      parent[ra] = rb
    elsif rank[ra] > rank[rb]
      parent[rb] = ra
    else
      parent[rb] = ra
      rank[ra] += 1
    end
  end

  circles.each_with_index do |c, i|
    x, y, r = c
    union.call(i, left)   if x - r <= 0
    union.call(i, right)  if x + r >= x_corner
    union.call(i, bottom) if y - r <= 0
    union.call(i, top)    if y + r >= y_corner
  end

  (0...n).each do |i|
    xi, yi, ri = circles[i]
    ((i + 1)...n).each do |j|
      xj, yj, rj = circles[j]
      dx = xi - xj
      dy = yi - yj
      dist2 = dx * dx + dy * dy
      rad_sum = ri + rj
      union.call(i, j) if dist2 <= rad_sum * rad_sum
    end
  end

  return false if find.call(left) == find.call(right)
  return false if find.call(top) == find.call(bottom)
  return false if find.call(left) == find.call(bottom)
  return false if find.call(right) == find.call(top)

  true
end
```

## Scala

```scala
object Solution {
  def canReachCorner(xCorner: Int, yCorner: Int, circles: Array[Array[Int]]): Boolean = {
    val n = circles.length
    val LEFT = n
    val RIGHT = n + 1
    val BOTTOM = n + 2
    val TOP = n + 3
    val total = n + 4

    // Union-Find structure
    val parent = Array.tabulate(total)(i => i)
    val rank = new Array[Int](total)

    def find(x: Int): Int = {
      var v = x
      while (parent(v) != v) {
        parent(v) = parent(parent(v))
        v = parent(v)
      }
      v
    }

    def union(a: Int, b: Int): Unit = {
      var ra = find(a)
      var rb = find(b)
      if (ra == rb) return
      if (rank(ra) < rank(rb)) {
        parent(ra) = rb
      } else if (rank(ra) > rank(rb)) {
        parent(rb) = ra
      } else {
        parent(rb) = ra
        rank(ra) += 1
      }
    }

    // Preprocess circles as Long for safe arithmetic
    val xs = new Array[Long](n)
    val ys = new Array[Long](n)
    val rs = new Array[Long](n)

    var i = 0
    while (i < n) {
      xs(i) = circles(i)(0).toLong
      ys(i) = circles(i)(1).toLong
      rs(i) = circles(i)(2).toLong

      if (xs(i) - rs(i) <= 0L) union(i, LEFT)
      if (xs(i) + rs(i) >= xCorner.toLong) union(i, RIGHT)
      if (ys(i) - rs(i) <= 0L) union(i, BOTTOM)
      if (ys(i) + rs(i) >= yCorner.toLong) union(i, TOP)

      i += 1
    }

    // Connect intersecting circles
    var a = 0
    while (a < n) {
      var b = a + 1
      while (b < n) {
        val dx = xs(a) - xs(b)
        val dy = ys(a) - ys(b)
        val distSq = dx * dx + dy * dy
        val radSum = rs(a) + rs(b)
        if (distSq <= radSum * radSum) union(a, b)
        b += 1
      }
      a += 1
    }

    // Check blocking connections
    val leftRoot = find(LEFT)
    val rightRoot = find(RIGHT)
    val topRoot = find(TOP)
    val bottomRoot = find(BOTTOM)

    !(leftRoot == rightRoot ||
      topRoot == bottomRoot ||
      leftRoot == bottomRoot ||
      rightRoot == topRoot)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn can_reach_corner(x_corner: i32, y_corner: i32, circles: Vec<Vec<i32>>) -> bool {
        #[derive(Clone)]
        struct DSU {
            parent: Vec<usize>,
            rank: Vec<u8>,
        }
        impl DSU {
            fn new(n: usize) -> Self {
                let mut parent = Vec::with_capacity(n);
                for i in 0..n {
                    parent.push(i);
                }
                let rank = vec![0; n];
                DSU { parent, rank }
            }
            fn find(&mut self, x: usize) -> usize {
                if self.parent[x] != x {
                    let root = self.find(self.parent[x]);
                    self.parent[x] = root;
                }
                self.parent[x]
            }
            fn union(&mut self, a: usize, b: usize) {
                let mut ra = self.find(a);
                let mut rb = self.find(b);
                if ra == rb {
                    return;
                }
                if self.rank[ra] < self.rank[rb] {
                    std::mem::swap(&mut ra, &mut rb);
                }
                self.parent[rb] = ra;
                if self.rank[ra] == self.rank[rb] {
                    self.rank[ra] += 1;
                }
            }
        }

        let n = circles.len();
        // indices for sides: up, right, down, left
        let up = n;
        let right = n + 1;
        let down = n + 2;
        let left = n + 3;

        let mut dsu = DSU::new(n + 4);
        let xc = x_corner as i64;
        let yc = y_corner as i64;

        // process each circle
        for (i, c) in circles.iter().enumerate() {
            let xi = c[0] as i64;
            let yi = c[1] as i64;
            let ri = c[2] as i64;

            if xi - ri <= 0 {
                dsu.union(i, left);
            }
            if xi + ri >= xc {
                dsu.union(i, right);
            }
            if yi - ri <= 0 {
                dsu.union(i, down);
            }
            if yi + ri >= yc {
                dsu.union(i, up);
            }
        }

        // connect overlapping circles
        for i in 0..n {
            let xi = circles[i][0] as i64;
            let yi = circles[i][1] as i64;
            let ri = circles[i][2] as i64;
            for j in (i + 1)..n {
                let xj = circles[j][0] as i64;
                let yj = circles[j][1] as i64;
                let rj = circles[j][2] as i64;

                let dx = xi - xj;
                let dy = yi - yj;
                let dist_sq = dx * dx + dy * dy;
                let rad_sum = ri + rj;
                if dist_sq <= rad_sum * rad_sum {
                    dsu.union(i, j);
                }
            }
        }

        // check blocking connections
        let left_root = dsu.find(left);
        let right_root = dsu.find(right);
        let up_root = dsu.find(up);
        let down_root = dsu.find(down);

        if left_root == right_root
            || up_root == down_root
            || left_root == down_root
            || right_root == up_root
        {
            false
        } else {
            true
        }
    }
}
```

## Racket

```racket
(define/contract (can-reach-corner xCorner yCorner circles)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) boolean?)
  (let* ((n (length circles))
         (left n) (right (+ n 1)) (bottom (+ n 2)) (top (+ n 3))
         (size (+ n 4))
         (parent (make-vector size))
         (rank (make-vector size 0)))
    ;; initialise DSU
    (for ([i (in-range size)])
      (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x) x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    (define (union a b)
      (let* ((ra (find a)) (rb (find b)))
        (when (not (= ra rb))
          (let ((rank-a (vector-ref rank ra))
                (rank-b (vector-ref rank rb)))
            (cond [(< rank-a rank-b) (vector-set! parent ra rb)]
                  [(> rank-a rank-b) (vector-set! parent rb ra)]
                  [else
                   (vector-set! parent rb ra)
                   (vector-set! rank ra (+ rank-a 1))])))))
    ;; process circles
    (for ([i (in-range n)])
      (let* ((c (list-ref circles i))
             (xi (first c))
             (yi (second c))
             (ri (third c)))
        (when (<= (- xi ri) 0) (union i left))
        (when (>= (+ xi ri) xCorner) (union i right))
        (when (<= (- yi ri) 0) (union i bottom))
        (when (>= (+ yi ri) yCorner) (union i top))
        (for ([j (in-range (+ i 1) n)])
          (let* ((c2 (list-ref circles j))
                 (xj (first c2))
                 (yj (second c2))
                 (rj (third c2))
                 (dx (- xi xj))
                 (dy (- yi yj))
                 (dist2 (+ (* dx dx) (* dy dy)))
                 (rad-sum (+ ri rj))
                 (rad-sum2 (* rad-sum rad-sum)))
            (when (<= dist2 rad-sum2)
              (union i j))))))
    ;; point inside any circle?
    (define (point-inside? px py)
      (let loop ((lst circles))
        (cond [(null? lst) #f]
              [else
               (let* ((c (car lst))
                      (xi (first c))
                      (yi (second c))
                      (ri (third c))
                      (dx (- px xi))
                      (dy (- py yi))
                      (dist2 (+ (* dx dx) (* dy dy))))
                 (if (< dist2 (* ri ri)) #t
                     (loop (cdr lst))))])))
    (if (or (point-inside? 0 0) (point-inside? xCorner yCorner))
        #f
        (let ((blocked
               (or (= (find left) (find right))
                   (= (find top) (find bottom))
                   (= (find left) (find bottom))
                   (= (find right) (find top)))))
          (not blocked)))))
```

## Erlang

```erlang
-spec can_reach_corner(XCorner :: integer(), YCorner :: integer(), Circles :: [[integer()]]) -> boolean().
can_reach_corner(XCorner, YCorner, Circles) ->
    N = length(Circles),
    Total = N + 4,
    InitParent = maps:from_list([{Idx, Idx} || Idx <- lists:seq(0, Total - 1)]),

    ParentAfterPairs = process_pairs(0, Circles, N, InitParent),
    FinalParent = connect_sides(Circles, XCorner, YCorner, N, ParentAfterPairs),

    {RootLeft, P1}   = find(N + 3, FinalParent), % left side
    {RootRight, P2}  = find(N + 1, P1),          % right side
    {RootTop, P3}    = find(N,     P2),          % top side
    {RootBottom, _}  = find(N + 2, P3),          % bottom side

    if RootLeft == RootRight orelse
       RootTop == RootBottom orelse
       RootLeft == RootBottom orelse
       RootRight == RootTop ->
            false;
       true -> true
    end.

%% Process all circle-circle intersections
process_pairs(I, _Circles, N, Parent) when I >= N - 1 ->
    Parent;
process_pairs(I, Circles, N, Parent) ->
    CircleI = lists:nth(I + 1, Circles),
    ParentAfterJ = process_j(I, I + 1, CircleI, Circles, N, Parent),
    process_pairs(I + 1, Circles, N, ParentAfterJ).

process_j(_I, J, _CircleI, _Circles, N, Parent) when J >= N ->
    Parent;
process_j(I, J, CircleI, Circles, N, Parent) ->
    CircleJ = lists:nth(J + 1, Circles),
    NewParent =
        case circles_touch(CircleI, CircleJ) of
            true -> union(I, J, Parent);
            false -> Parent
        end,
    process_j(I, J + 1, CircleI, Circles, N, NewParent).

%% Connect circles to rectangle sides if they touch or intersect them
connect_sides(Circles, XCorner, YCorner, N, Parent) ->
    connect_side_loop(0, Circles, XCorner, YCorner, N, Parent).

connect_side_loop(I, _Circles, _XCorner, _YCorner, N, Parent) when I >= N ->
    Parent;
connect_side_loop(I, Circles, XCorner, YCorner, N, Parent) ->
    [X, Y, R] = lists:nth(I + 1, Circles),
    P1 = if X - R =< 0 -> union(I, N + 3, Parent); true -> Parent end,
    P2 = if X + R >= XCorner -> union(I, N + 1, P1); true -> P1 end,
    P3 = if Y - R =< 0 -> union(I, N + 2, P2); true -> P2 end,
    P4 = if Y + R >= YCorner -> union(I, N, P3); true -> P3 end,
    connect_side_loop(I + 1, Circles, XCorner, YCorner, N, P4).

%% Union-Find operations
find(Id, Parent) ->
    case maps:get(Id, Parent) of
        Id -> {Id, Parent};
        Pid ->
            {Root, UpdatedParent} = find(Pid, Parent),
            NewParent = maps:put(Id, Root, UpdatedParent),
            {Root, NewParent}
    end.

union(A, B, Parent) ->
    {RootA, TempParent1} = find(A, Parent),
    {RootB, TempParent2} = find(B, TempParent1),
    if
        RootA == RootB -> TempParent2;
        true -> maps:put(RootA, RootB, TempParent2)
    end.

%% Geometry helper
circles_touch([X1, Y1, R1], [X2, Y2, R2]) ->
    Dx = X1 - X2,
    Dy = Y1 - Y2,
    DistSq = Dx * Dx + Dy * Dy,
    SumR = R1 + R2,
    DistSq =< SumR * SumR.
```

## Elixir

```elixir
defmodule DSU do
  defstruct parent: %{}, rank: %{}

  def new(size) do
    parent = Enum.into(0..size - 1, %{}, fn i -> {i, i} end)
    rank = Enum.into(0..size - 1, %{}, fn i -> {i, 0} end)
    %DSU{parent: parent, rank: rank}
  end

  def find(dsu, x) do
    p = Map.get(dsu.parent, x)

    if p == x do
      {dsu, x}
    else
      {dsu2, root} = find(dsu, p)
      new_parent = Map.put(dsu2.parent, x, root)
      {%DSU{dsu2 | parent: new_parent}, root}
    end
  end

  def union(dsu, x, y) do
    {dsu1, rx} = find(dsu, x)
    {dsu2, ry} = find(dsu1, y)

    if rx == ry do
      dsu2
    else
      rankx = Map.get(dsu2.rank, rx)
      ranky = Map.get(dsu2.rank, ry)

      cond do
        rankx < ranky ->
          parent = Map.put(dsu2.parent, rx, ry)
          %DSU{dsu2 | parent: parent}

        rankx > ranky ->
          parent = Map.put(dsu2.parent, ry, rx)
          %DSU{dsu2 | parent: parent}

        true ->
          parent = Map.put(dsu2.parent, ry, rx)
          rank = Map.update!(dsu2.rank, rx, &(&1 + 1))
          %DSU{parent: parent, rank: rank}
      end
    end
  end

  def connected?(dsu, x, y) do
    {_, rx} = find(dsu, x)
    {_, ry} = find(dsu, y)
    rx == ry
  end
end

defmodule Solution do
  @spec can_reach_corner(x_corner :: integer, y_corner :: integer, circles :: [[integer]]) :: boolean
  def can_reach_corner(x_corner, y_corner, circles) do
    n = length(circles)

    left = n
    right = n + 1
    bottom = n + 2
    top = n + 3

    dsu0 = DSU.new(n + 4)

    # Union circles with rectangle sides they touch
    dsu1 =
      Enum.reduce(0..n - 1, dsu0, fn i, acc ->
        [xi, yi, ri] = Enum.at(circles, i)

        acc
        |> maybe_union(i, left, xi - ri <= 0)
        |> maybe_union(i, right, xi + ri >= x_corner)
        |> maybe_union(i, bottom, yi - ri <= 0)
        |> maybe_union(i, top, yi + ri >= y_corner)
      end)

    # Union intersecting circles
    dsu2 =
      Enum.reduce(0..n - 2, dsu1, fn i, acc ->
        [xi, yi, ri] = Enum.at(circles, i)

        Enum.reduce(i + 1..n - 1, acc, fn j, acc2 ->
          [xj, yj, rj] = Enum.at(circles, j)
          dx = xi - xj
          dy = yi - yj
          rad_sum = ri + rj

          if dx * dx + dy * dy <= rad_sum * rad_sum do
            DSU.union(acc2, i, j)
          else
            acc2
          end
        end)
      end)

    blocked =
      DSU.connected?(dsu2, left, bottom) or
        DSU.connected?(dsu2, top, right) or
        DSU.connected?(dsu2, left, right) or
        DSU.connected?(dsu2, top, bottom)

    not blocked
  end

  defp maybe_union(dsu, a, b, true), do: DSU.union(dsu, a, b)
  defp maybe_union(dsu, _a, _b, false), do: dsu
end
```
