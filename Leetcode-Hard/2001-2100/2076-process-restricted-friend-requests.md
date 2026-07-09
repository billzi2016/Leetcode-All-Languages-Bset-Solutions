# 2076. Process Restricted Friend Requests

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, sz;
        DSU(int n) : parent(n), sz(n,1) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }
        void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (sz[a] < sz[b]) swap(a,b);
            parent[b] = a;
            sz[a] += sz[b];
        }
    };
    
    vector<bool> friendRequests(int n, vector<vector<int>>& restrictions, vector<vector<int>>& requests) {
        DSU dsu(n);
        vector<pair<int,int>> restr;
        restr.reserve(restrictions.size());
        for (auto &r : restrictions) restr.emplace_back(r[0], r[1]);
        
        vector<bool> ans;
        ans.reserve(requests.size());
        for (auto &req : requests) {
            int u = req[0], v = req[1];
            int ru = dsu.find(u);
            int rv = dsu.find(v);
            if (ru == rv) {
                ans.push_back(true);
                continue;
            }
            bool ok = true;
            for (auto &p : restr) {
                int x = p.first, y = p.second;
                int rx = dsu.find(x);
                int ry = dsu.find(y);
                if ((rx == ru && ry == rv) || (rx == rv && ry == ru)) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                dsu.unite(ru, rv);
                ans.push_back(true);
            } else {
                ans.push_back(false);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public boolean[] friendRequests(int n, int[][] restrictions, int[][] requests) {
        DSU dsu = new DSU(n);
        boolean[] ans = new boolean[requests.length];
        for (int i = 0; i < requests.length; i++) {
            int u = requests[i][0];
            int v = requests[i][1];
            int pu = dsu.find(u);
            int pv = dsu.find(v);
            if (pu == pv) {
                ans[i] = true;
                continue;
            }
            boolean ok = true;
            for (int[] r : restrictions) {
                int x = r[0], y = r[1];
                int px = dsu.find(x), py = dsu.find(y);
                if ((px == pu && py == pv) || (px == pv && py == pu)) {
                    ok = false;
                    break;
                }
            }
            ans[i] = ok;
            if (ok) {
                dsu.union(pu, pv);
            }
        }
        return ans;
    }

    private static class DSU {
        int[] parent;
        int[] rank;

        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
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
    }
}
```

## Python

```python
class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        res = []
        for u, v in requests:
            ru, rv = find(u), find(v)
            if ru == rv:
                res.append(True)
                continue
            conflict = False
            for x, y in restrictions:
                rx, ry = find(x), find(y)
                # merging ru and rv would connect a restricted pair
                if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                    conflict = True
                    break
            if conflict:
                res.append(False)
            else:
                union(ru, rv)
                res.append(True)
        return res
```

## Python3

```python
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        res = []
        for u, v in requests:
            ru, rv = find(u), find(v)
            if ru == rv:
                res.append(True)
                continue

            conflict = False
            for x, y in restrictions:
                rx, ry = find(x), find(y)
                # If after merging u and v, x and y would be connected
                # This happens when one is in component ru and other in rv
                if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                    conflict = True
                    break

            if conflict:
                res.append(False)
            else:
                union(ru, rv)
                res.append(True)

        return res
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int find(int *parent, int x) {
    if (parent[x] != x) parent[x] = find(parent, parent[x]);
    return parent[x];
}

static void unite(int *parent, int *rank, int x, int y) {
    int rx = find(parent, x);
    int ry = find(parent, y);
    if (rx == ry) return;
    if (rank[rx] < rank[ry]) {
        parent[rx] = ry;
    } else if (rank[rx] > rank[ry]) {
        parent[ry] = rx;
    } else {
        parent[ry] = rx;
        rank[rx]++;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* friendRequests(int n, int** restrictions, int restrictionsSize, int* restrictionsColSize,
                     int** requests, int requestsSize, int* requestsColSize, int* returnSize) {
    int *parent = (int *)malloc(n * sizeof(int));
    int *rank   = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    bool *ans = (bool *)malloc(requestsSize * sizeof(bool));
    *returnSize = requestsSize;

    for (int i = 0; i < requestsSize; ++i) {
        int u = requests[i][0];
        int v = requests[i][1];
        int pu = find(parent, u);
        int pv = find(parent, v);

        bool ok = true;
        if (pu != pv) {
            for (int j = 0; j < restrictionsSize; ++j) {
                int x = restrictions[j][0];
                int y = restrictions[j][1];
                int px = find(parent, x);
                int py = find(parent, y);
                if ((pu == px && pv == py) || (pu == py && pv == px)) {
                    ok = false;
                    break;
                }
            }
        }

        ans[i] = ok;
        if (ok && pu != pv) {
            unite(parent, rank, pu, pv);
        }
    }

    free(parent);
    free(rank);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public bool[] FriendRequests(int n, int[][] restrictions, int[][] requests)
    {
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int Find(int x)
        {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }

        void Union(int a, int b)
        {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (rank[ra] < rank[rb])
                parent[ra] = rb;
            else if (rank[ra] > rank[rb])
                parent[rb] = ra;
            else
            {
                parent[rb] = ra;
                rank[ra]++;
            }
        }

        bool[] result = new bool[requests.Length];
        for (int i = 0; i < requests.Length; i++)
        {
            int u = requests[i][0];
            int v = requests[i][1];
            int ru = Find(u);
            int rv = Find(v);

            bool ok = true;
            if (ru != rv)
            {
                foreach (var r in restrictions)
                {
                    int x = r[0], y = r[1];
                    int rx = Find(x), ry = Find(y);
                    if ((rx == ru && ry == rv) || (rx == rv && ry == ru))
                    {
                        ok = false;
                        break;
                    }
                }
            }

            result[i] = ok;
            if (ok) Union(u, v);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} restrictions
 * @param {number[][]} requests
 * @return {boolean[]}
 */
var friendRequests = function(n, restrictions, requests) {
    const parent = new Array(n);
    const rank = new Array(n).fill(0);
    for (let i = 0; i < n; ++i) parent[i] = i;
    
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    
    const union = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }
    };
    
    const res = [];
    for (const [u, v] of requests) {
        let fu = find(u);
        let fv = find(v);
        if (fu === fv) {
            res.push(true);
            continue;
        }
        let ok = true;
        for (const [x, y] of restrictions) {
            const fx = find(x);
            const fy = find(y);
            // merging fu and fv would connect x and y
            if ((fx === fu && fy === fv) || (fx === fv && fy === fu)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            union(fu, fv);
            res.push(true);
        } else {
            res.push(false);
        }
    }
    return res;
};
```

## Typescript

```typescript
function friendRequests(n: number, restrictions: number[][], requests: number[][]): boolean[] {
    const parent = new Array<number>(n);
    const rank = new Array<number>(n).fill(0);
    for (let i = 0; i < n; ++i) parent[i] = i;

    const find = (x: number): number => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };

    const union = (a: number, b: number): void => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (rank[ra] < rank[rb]) {
            [ra, rb] = [rb, ra];
        }
        parent[rb] = ra;
        if (rank[ra] === rank[rb]) rank[ra]++;
    };

    const res: boolean[] = [];

    for (const [u, v] of requests) {
        let ru = find(u);
        let rv = find(v);
        if (ru === rv) {
            res.push(true);
            continue;
        }
        let ok = true;
        for (const [x, y] of restrictions) {
            const rx = find(x);
            const ry = find(y);
            // If after merging ru and rv, x and y would become connected
            if ((rx === ru && ry === rv) || (rx === rv && ry === ru)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            union(ru, rv);
            res.push(true);
        } else {
            res.push(false);
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $restrictions
     * @param Integer[][] $requests
     * @return Boolean[]
     */
    function friendRequests($n, $restrictions, $requests) {
        $parent = range(0, $n - 1);
        $rank   = array_fill(0, $n, 0);

        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        $union = function ($a, $b) use (&$parent, &$rank, $find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra == $rb) return;
            if ($rank[$ra] < $rank[$rb]) {
                $parent[$ra] = $rb;
            } elseif ($rank[$ra] > $rank[$rb]) {
                $parent[$rb] = $ra;
            } else {
                $parent[$rb] = $ra;
                $rank[$ra]++;
            }
        };

        $result = [];

        foreach ($requests as $req) {
            [$u, $v] = $req;
            $ru = $find($u);
            $rv = $find($v);

            if ($ru == $rv) {
                $result[] = true;
                continue;
            }

            $can = true;
            foreach ($restrictions as $res) {
                [$x, $y] = $res;
                $rx = $find($x);
                $ry = $find($y);
                if ( ($rx == $ru && $ry == $rv) || ($rx == $rv && $ry == $ru) ) {
                    $can = false;
                    break;
                }
            }

            if ($can) {
                $union($u, $v);
                $result[] = true;
            } else {
                $result[] = false;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    private class DSU {
        var parent: [Int]
        var rank: [Int]
        init(_ n: Int) {
            parent = Array(0..<n)
            rank = [Int](repeating: 0, count: n)
        }
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        func union(_ a: Int, _ b: Int) {
            var ra = find(a)
            var rb = find(b)
            if ra == rb { return }
            if rank[ra] < rank[rb] {
                parent[ra] = rb
            } else if rank[ra] > rank[rb] {
                parent[rb] = ra
            } else {
                parent[rb] = ra
                rank[ra] += 1
            }
        }
    }

    func friendRequests(_ n: Int, _ restrictions: [[Int]], _ requests: [[Int]]) -> [Bool] {
        let dsu = DSU(n)
        var answer = [Bool]()
        for req in requests {
            let u = req[0]
            let v = req[1]
            let ru = dsu.find(u)
            let rv = dsu.find(v)

            var ok = true
            if ru != rv {
                for r in restrictions {
                    let x = r[0], y = r[1]
                    let rx = dsu.find(x)
                    let ry = dsu.find(y)
                    if (rx == ru && ry == rv) || (rx == rv && ry == ru) {
                        ok = false
                        break
                    }
                }
            }

            answer.append(ok)
            if ok && ru != rv {
                dsu.union(ru, rv)
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun friendRequests(n: Int, restrictions: Array<IntArray>, requests: Array<IntArray>): BooleanArray {
        val uf = UnionFind(n)
        val result = BooleanArray(requests.size)
        for (i in requests.indices) {
            val u = requests[i][0]
            val v = requests[i][1]
            var ok = true
            val pu = uf.find(u)
            val pv = uf.find(v)
            if (pu != pv) {
                for (r in restrictions) {
                    val aRoot = uf.find(r[0])
                    val bRoot = uf.find(r[1])
                    if ((aRoot == pu && bRoot == pv) || (aRoot == pv && bRoot == pu)) {
                        ok = false
                        break
                    }
                }
            }
            result[i] = ok
            if (ok) {
                uf.union(u, v)
            }
        }
        return result
    }

    private class UnionFind(n: Int) {
        private val parent = IntArray(n) { it }
        private val rank = IntArray(n)

        fun find(x: Int): Int {
            var p = x
            while (parent[p] != p) {
                parent[p] = parent[parent[p]]
                p = parent[p]
            }
            return p
        }

        fun union(a: Int, b: Int) {
            var x = find(a)
            var y = find(b)
            if (x == y) return
            if (rank[x] < rank[y]) {
                val tmp = x
                x = y
                y = tmp
            }
            parent[y] = x
            if (rank[x] == rank[y]) rank[x]++
        }
    }
}
```

## Dart

```dart
class Solution {
  List<bool> friendRequests(int n, List<List<int>> restrictions, List<List<int>> requests) {
    var parent = List<int>.generate(n, (i) => i);
    var rank = List<int>.filled(n, 0);

    int find(int x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    void unionSets(int a, int b) {
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

    List<bool> result = [];
    for (var req in requests) {
      int u = req[0];
      int v = req[1];
      int ru = find(u);
      int rv = find(v);
      if (ru == rv) {
        result.add(true);
        continue;
      }
      bool can = true;
      for (var res in restrictions) {
        int x = res[0];
        int y = res[1];
        int rx = find(x);
        int ry = find(y);
        // If after merging ru and rv, x and y would become connected
        if ((rx == ru && ry == rv) || (rx == rv && ry == ru)) {
          can = false;
          break;
        }
      }
      if (can) {
        unionSets(ru, rv);
        result.add(true);
      } else {
        result.add(false);
      }
    }
    return result;
  }
}
```

## Golang

```go
type dsu struct {
	parent []int
	size   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	sz := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
		sz[i] = 1
	}
	return &dsu{parent: p, size: sz}
}

func (d *dsu) find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.find(d.parent[x])
	}
	return d.parent[x]
}

func (d *dsu) union(a, b int) {
	ra := d.find(a)
	rb := d.find(b)
	if ra == rb {
		return
	}
	if d.size[ra] < d.size[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	d.size[ra] += d.size[rb]
}

func friendRequests(n int, restrictions [][]int, requests [][]int) []bool {
	ds := newDSU(n)
	ans := make([]bool, len(requests))

	for i, req := range requests {
		u, v := req[0], req[1]
		ru, rv := ds.find(u), ds.find(v)

		if ru == rv {
			ans[i] = true
			continue
		}

		conflict := false
		for _, r := range restrictions {
			x, y := r[0], r[1]
			rx, ry := ds.find(x), ds.find(y)
			if (rx == ru && ry == rv) || (rx == rv && ry == ru) {
				conflict = true
				break
			}
		}

		if conflict {
			ans[i] = false
		} else {
			ds.union(ru, rv)
			ans[i] = true
		}
	}
	return ans
}
```

## Ruby

```ruby
class DSU
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @rank = Array.new(n, 0)
  end

  def find(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(x, y)
    xr = find(x)
    yr = find(y)
    return false if xr == yr
    if @rank[xr] < @rank[yr]
      @parent[xr] = yr
    elsif @rank[xr] > @rank[yr]
      @parent[yr] = xr
    else
      @parent[yr] = xr
      @rank[xr] += 1
    end
    true
  end
end

def friend_requests(n, restrictions, requests)
  dsu = DSU.new(n)
  result = []
  requests.each do |u, v|
    ru = dsu.find(u)
    rv = dsu.find(v)
    if ru == rv
      result << true
      next
    end

    conflict = false
    restrictions.each do |x, y|
      rx = dsu.find(x)
      ry = dsu.find(y)
      if (rx == ru && ry == rv) || (rx == rv && ry == ru)
        conflict = true
        break
      end
    end

    if conflict
      result << false
    else
      dsu.union(ru, rv)
      result << true
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  def friendRequests(n: Int, restrictions: Array[Array[Int]], requests: Array[Array[Int]]): Array[Boolean] = {
    val uf = new UnionFind(n)
    val m = requests.length
    val ans = new Array[Boolean](m)

    var i = 0
    while (i < m) {
      val u = requests(i)(0)
      val v = requests(i)(1)
      var ru = uf.find(u)
      var rv = uf.find(v)

      if (ru == rv) {
        ans(i) = true
      } else {
        var ok = true
        var j = 0
        while (j < restrictions.length && ok) {
          val x = restrictions(j)(0)
          val y = restrictions(j)(1)
          val rx = uf.find(x)
          val ry = uf.find(y)
          if ((rx == ru && ry == rv) || (rx == rv && ry == ru)) ok = false
          j += 1
        }
        if (ok) {
          uf.union(ru, rv)
          ans(i) = true
        } else {
          ans(i) = false
        }
      }
      i += 1
    }

    ans
  }

  private class UnionFind(val n: Int) {
    private val parent = Array.tabulate(n)(i => i)
    private val size   = Array.fill(n)(1)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def union(a: Int, b: Int): Unit = {
      var x = find(a)
      var y = find(b)
      if (x == y) return
      if (size(x) < size(y)) { val t = x; x = y; y = t }
      parent(y) = x
      size(x) += size(y)
    }
  }
}
```

## Rust

```rust
struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = vec![0; n];
        for i in 0..n {
            parent[i] = i;
        }
        DSU {
            parent,
            rank: vec![0; n],
        }
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

impl Solution {
    pub fn friend_requests(n: i32, restrictions: Vec<Vec<i32>>, requests: Vec<Vec<i32>>) -> Vec<bool> {
        let n_usize = n as usize;
        let mut dsu = DSU::new(n_usize);
        let restr: Vec<(usize, usize)> = restrictions
            .iter()
            .map(|v| (v[0] as usize, v[1] as usize))
            .collect();

        let mut ans = Vec::with_capacity(requests.len());

        for req in requests {
            let u = req[0] as usize;
            let v = req[1] as usize;

            let ru = dsu.find(u);
            let rv = dsu.find(v);

            if ru == rv {
                ans.push(true);
                continue;
            }

            let mut ok = true;
            for &(x, y) in &restr {
                let rx = dsu.find(x);
                let ry = dsu.find(y);
                if (rx == ru && ry == rv) || (rx == rv && ry == ru) {
                    ok = false;
                    break;
                }
            }

            if ok {
                dsu.union(ru, rv);
                ans.push(true);
            } else {
                ans.push(false);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (friend-requests n restrictions requests)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof boolean?))
  (let ([parent (make-vector n)]
        [rank   (make-vector n 0)])
    ;; initialize DSU
    (for ([i (in-range n)]) (vector-set! parent i i))

    (define (find x)
      (let loop ((x x))
        (let ([p (vector-ref parent x)])
          (if (= p x)
              x
              (let ([root (loop p)])
                (vector-set! parent x root)
                root)))))

    (define (union a b)
      (let* ([ra (find a)]
             [rb (find b)])
        (when (not (= ra rb))
          (let ([rank-a (vector-ref rank ra)]
                [rank-b (vector-ref rank rb)])
            (if (> rank-a rank-b)
                (vector-set! parent rb ra)
                (begin
                  (vector-set! parent ra rb)
                  (when (= rank-a rank-b)
                    (vector-set! rank rb (+ (vector-ref rank rb) 1)))))))))

    (let ([result '()])
      (for ([req requests])
        (define u (first req))
        (define v (second req))
        (if (= (find u) (find v))
            (set! result (cons #t result))
            (let* ([ru (find u)]
                   [rv (find v)]
                   [ok  #t])
              (for ([pair restrictions] #:break (not ok))
                (define x (first pair))
                (define y (second pair))
                (when (or (and (= (find x) ru) (= (find y) rv))
                          (and (= (find x) rv) (= (find y) ru)))
                  (set! ok #f)))
              (if ok
                  (begin (union u v) (set! result (cons #t result)))
                  (set! result (cons #f result))))))
      (reverse result))))
```

## Erlang

```erlang
-module(solution).
-export([friend_requests/3]).

-spec friend_requests(N :: integer(), Restrictions :: [[integer()]], Requests :: [[integer()]]) -> [boolean()].
friend_requests(N, Restrictions, Requests) ->
    Parent0 = maps:from_list([{I, I} || I <- lists:seq(0, N-1)]),
    Rank0 = #{},
    {ResultRev, _ParentFinal, _RankFinal} = process_requests(Requests, Restrictions, Parent0, Rank0, []),
    lists:reverse(ResultRev).

%% Process each request recursively
process_requests([], _Restrictions, Parent, Rank, Acc) ->
    {Acc, Parent, Rank};
process_requests([[U,V]|Rest], Restrictions, Parent, Rank, Acc) ->
    RU = find_root(U, Parent),
    RV = find_root(V, Parent),
    case RU == RV of
        true ->
            process_requests(Rest, Restrictions, Parent, Rank, [true|Acc]);
        false ->
            case can_merge(RU, RV, Restrictions, Parent) of
                true ->
                    {NewParent, NewRank} = union(RU, RV, Parent, Rank),
                    process_requests(Rest, Restrictions, NewParent, NewRank, [true|Acc]);
                false ->
                    process_requests(Rest, Restrictions, Parent, Rank, [false|Acc])
            end
    end.

%% Check if merging components RU and RV violates any restriction
can_merge(_RU, _RV, [], _Parent) -> true;
can_merge(RU, RV, [[X,Y]|Rest], Parent) ->
    RX = find_root(X, Parent),
    RY = find_root(Y, Parent),
    case ((RX == RU) andalso (RY == RV)) orelse ((RX == RV) andalso (RY == RU)) of
        true -> false;
        false -> can_merge(RU, RV, Rest, Parent)
    end.

%% Find root without path compression (pure read)
find_root(Node, Parent) ->
    case maps:get(Node, Parent) of
        Node -> Node;
        P -> find_root(P, Parent)
    end.

%% Union by rank
union(RU, RV, Parent, Rank) ->
    RankU = maps:get(RU, Rank, 0),
    RankV = maps:get(RV, Rank, 0),
    case RankU < RankV of
        true ->
            {maps:put(RU, RV, Parent), Rank};
        false ->
            case RankU > RankV of
                true ->
                    {maps:put(RV, RU, Parent), Rank};
                false ->
                    % equal rank, attach RV under RU and increase RU's rank
                    NewParent = maps:put(RV, RU, Parent),
                    NewRank = maps:put(RU, RankU + 1, Rank),
                    {NewParent, NewRank}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec friend_requests(integer, [[integer]], [[integer]]) :: [boolean]
  def friend_requests(n, restrictions, requests) do
    parent = Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, i) end)
    size = Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, 1) end)

    {_, _, rev_res} =
      Enum.reduce(requests, {parent, size, []}, fn [u, v], {par, sz, res} ->
        pu = find_root(par, u)
        pv = find_root(par, v)

        if pu == pv do
          {par, sz, [true | res]}
        else
          conflict =
            Enum.any?(restrictions, fn [x, y] ->
              rx = find_root(par, x)
              ry = find_root(par, y)
              (rx == pu and ry == pv) or (rx == pv and ry == pu)
            end)

          if conflict do
            {par, sz, [false | res]}
          else
            {new_par, new_sz} = union(par, sz, pu, pv)
            {new_par, new_sz, [true | res]}
          end
        end
      end)

    Enum.reverse(rev_res)
  end

  defp find_root(parent, x) do
    p = Map.get(parent, x)
    if p == x, do: x, else: find_root(parent, p)
  end

  defp union(parent, size, a, b) do
    sa = Map.get(size, a)
    sb = Map.get(size, b)

    cond do
      sa < sb ->
        parent2 = Map.put(parent, a, b)
        size2 = Map.put(size, b, sa + sb)
        {parent2, size2}
      true ->
        parent2 = Map.put(parent, b, a)
        size2 = Map.put(size, a, sa + sb)
        {parent2, size2}
    end
  end
end
```
