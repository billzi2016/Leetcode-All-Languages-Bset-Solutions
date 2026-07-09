# 0593. Valid Square

## Cpp

```cpp
class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        auto dist2 = [](const vector<int>& a, const vector<int>& b) -> long long {
            long long dx = (long long)a[0] - b[0];
            long long dy = (long long)a[1] - b[1];
            return dx*dx + dy*dy;
        };
        vector<vector<int>*> pts = {&p1, &p2, &p3, &p4};
        vector<long long> d;
        for (int i = 0; i < 4; ++i) {
            for (int j = i+1; j < 4; ++j) {
                d.push_back(dist2(*pts[i], *pts[j]));
            }
        }
        sort(d.begin(), d.end());
        // first four are sides, last two are diagonals
        return d[0] > 0 &&
               d[0] == d[1] && d[1] == d[2] && d[2] == d[3] &&
               d[4] == d[5] && d[4] > d[0];
    }
};
```

## Java

```java
class Solution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] pts = {p1, p2, p3, p4};
        int[] dists = new int[6];
        int idx = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = i + 1; j < 4; j++) {
                int dx = pts[i][0] - pts[j][0];
                int dy = pts[i][1] - pts[j][1];
                dists[idx++] = dx * dx + dy * dy;
            }
        }
        java.util.Arrays.sort(dists);
        // first four are sides, last two are diagonals
        if (dists[0] == 0) return false; // overlapping points
        boolean sidesEqual = dists[0] == dists[1] && dists[1] == dists[2] && dists[2] == dists[3];
        boolean diagonalsEqual = dists[4] == dists[5];
        boolean diagonalCorrect = dists[4] == 2 * dists[0];
        return sidesEqual && diagonalsEqual && diagonalCorrect;
    }
}
```

## Python

```python
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist(a, b):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx * dx + dy * dy

        points = [p1, p2, p3, p4]
        dists = []
        for i in range(4):
            for j in range(i + 1, 4):
                d = dist(points[i], points[j])
                if d == 0:
                    return False
                dists.append(d)

        freq = {}
        for d in dists:
            freq[d] = freq.get(d, 0) + 1

        if len(freq) != 2:
            return False

        side, diag = sorted(freq.items(), key=lambda x: x[0])
        # side length should appear 4 times, diagonal 2 times
        if side[1] != 4 or diag[1] != 2:
            return False
        # diagonal length is twice the side length in a square
        return diag[0] == 2 * side[0]
```

## Python3

```python
from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        
        def dist_sq(a: List[int], b: List[int]) -> int:
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx * dx + dy * dy
        
        dists = {}
        for i in range(4):
            for j in range(i + 1, 4):
                d = dist_sq(points[i], points[j])
                if d == 0:
                    return False
                dists[d] = dists.get(d, 0) + 1
        
        if len(dists) != 2:
            return False
        
        side, diag = sorted(dists.items(), key=lambda x: x[0])
        # side length should appear 4 times, diagonal 2 times
        return side[1] == 4 and diag[1] == 2 and diag[0] == 2 * side[0]
```

## C

```c
bool validSquare(int* p1, int p1Size, int* p2, int p2Size, int* p3, int p3Size, int* p4, int p4Size) {
    (void)p1Size; (void)p2Size; (void)p3Size; (void)p4Size;
    long long d[6];
    auto dist2 = [](int *a, int *b)->long long{
        long long dx = (long long)a[0] - b[0];
        long long dy = (long long)a[1] - b[1];
        return dx*dx + dy*dy;
    };
    d[0] = dist2(p1, p2);
    d[1] = dist2(p1, p3);
    d[2] = dist2(p1, p4);
    d[3] = dist2(p2, p3);
    d[4] = dist2(p2, p4);
    d[5] = dist2(p3, p4);
    
    long long side = -1;
    for (int i = 0; i < 6; ++i) {
        if (d[i] != 0) {
            if (side == -1 || d[i] < side) side = d[i];
        }
    }
    if (side == -1) return false; // all points coincide
    
    int cntSide = 0, cntDiag = 0;
    long long diag = -1;
    for (int i = 0; i < 6; ++i) {
        if (d[i] == side) cntSide++;
        else {
            if (diag == -1) diag = d[i];
            else if (d[i] != diag) return false; // more than two distinct distances
            cntDiag++;
        }
    }
    if (cntSide != 4 || cntDiag != 2) return false;
    if (diag != 2 * side) return false;
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool ValidSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        var points = new int[][] { p1, p2, p3, p4 };
        var dists = new List<int>(6);
        for (int i = 0; i < 4; i++) {
            for (int j = i + 1; j < 4; j++) {
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                dists.Add(dx * dx + dy * dy);
            }
        }
        dists.Sort();
        // first four are sides, last two are diagonals
        return dists[0] > 0 &&
               dists[0] == dists[1] && dists[1] == dists[2] && dists[2] == dists[3] &&
               dists[4] == dists[5] &&
               dists[4] == 2 * dists[0];
    }
}
```

## Javascript

```javascript
var validSquare = function(p1, p2, p3, p4) {
    const pts = [p1, p2, p3, p4];
    const dists = [];
    for (let i = 0; i < 4; i++) {
        for (let j = i + 1; j < 4; j++) {
            const dx = pts[i][0] - pts[j][0];
            const dy = pts[i][1] - pts[j][1];
            const d = dx * dx + dy * dy;
            if (d === 0) return false;
            dists.push(d);
        }
    }
    const freq = {};
    for (const d of dists) {
        freq[d] = (freq[d] || 0) + 1;
    }
    const keys = Object.keys(freq);
    if (keys.length !== 2) return false;
    const a = Number(keys[0]), b = Number(keys[1]);
    const ca = freq[a], cb = freq[b];
    let side, diag;
    if (ca === 4 && cb === 2) {
        side = a; diag = b;
    } else if (ca === 2 && cb === 4) {
        side = b; diag = a;
    } else {
        return false;
    }
    return diag === 2 * side;
};
```

## Typescript

```typescript
function validSquare(p1: number[], p2: number[], p3: number[], p4: number[]): boolean {
    const dist = (a: number[], b: number[]) => {
        const dx = a[0] - b[0];
        const dy = a[1] - b[1];
        return dx * dx + dy * dy;
    };
    
    const dists = [
        dist(p1, p2),
        dist(p1, p3),
        dist(p1, p4),
        dist(p2, p3),
        dist(p2, p4),
        dist(p3, p4)
    ];
    
    dists.sort((x, y) => x - y);
    
    // first four should be equal (sides), last two equal (diagonals)
    const side = dists[0];
    if (side === 0) return false; // overlapping points
    
    for (let i = 1; i < 4; i++) {
        if (dists[i] !== side) return false;
    }
    
    const diag = dists[4];
    if (diag !== dists[5]) return false;
    
    // In a square, diagonal^2 = 2 * side^2
    if (diag !== 2 * side) return false;
    
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $p1
     * @param Integer[] $p2
     * @param Integer[] $p3
     * @param Integer[] $p4
     * @return Boolean
     */
    function validSquare($p1, $p2, $p3, $p4) {
        // helper to compute squared distance between two points
        $dist = function($a, $b) {
            $dx = $a[0] - $b[0];
            $dy = $a[1] - $b[1];
            return $dx * $dx + $dy * $dy;
        };

        $dists = [
            $dist($p1, $p2),
            $dist($p1, $p3),
            $dist($p1, $p4),
            $dist($p2, $p3),
            $dist($p2, $p4),
            $dist($p3, $p4)
        ];

        sort($dists); // ascending

        // first four should be equal (sides), last two equal (diagonals)
        // also side length must be > 0 and diagonal = 2 * side
        if ($dists[0] == 0) {
            return false;
        }

        $side = $dists[0];
        for ($i = 1; $i < 4; $i++) {
            if ($dists[$i] != $side) {
                return false;
            }
        }

        $diag = $dists[4];
        if ($diag != $dists[5]) {
            return false;
        }

        // diagonal squared should be twice side squared
        return $diag == 2 * $side;
    }
}
```

## Swift

```swift
class Solution {
    func validSquare(_ p1: [Int], _ p2: [Int], _ p3: [Int], _ p4: [Int]) -> Bool {
        func dist(_ a: [Int], _ b: [Int]) -> Int {
            let dx = a[0] - b[0]
            let dy = a[1] - b[1]
            return dx * dx + dy * dy
        }
        
        var dists = [Int]()
        let points = [p1, p2, p3, p4]
        for i in 0..<4 {
            for j in i+1..<4 {
                dists.append(dist(points[i], points[j]))
            }
        }
        dists.sort()
        
        // For a square: first four distances are equal (sides), last two are equal (diagonals)
        // and side length must be > 0, diagonal = 2 * side (Pythagoras)
        return dists[0] > 0 &&
               dists[0] == dists[1] && dists[1] == dists[2] && dists[2] == dists[3] &&
               dists[4] == dists[5] &&
               dists[4] == 2 * dists[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validSquare(p1: IntArray, p2: IntArray, p3: IntArray, p4: IntArray): Boolean {
        val pts = arrayOf(p1, p2, p3, p4)
        val dists = IntArray(6)
        var idx = 0
        for (i in 0 until 4) {
            for (j in i + 1 until 4) {
                val dx = pts[i][0] - pts[j][0]
                val dy = pts[i][1] - pts[j][1]
                dists[idx++] = dx * dx + dy * dy
            }
        }
        dists.sort()
        return dists[0] > 0 &&
               dists[0] == dists[1] && dists[1] == dists[2] && dists[2] == dists[3] &&
               dists[4] == dists[5] && dists[4] == 2 * dists[0]
    }
}
```

## Dart

```dart
class Solution {
  bool validSquare(List<int> p1, List<int> p2, List<int> p3, List<int> p4) {
    int distSq(List<int> a, List<int> b) {
      int dx = a[0] - b[0];
      int dy = a[1] - b[1];
      return dx * dx + dy * dy;
    }

    List<int> d = [
      distSq(p1, p2),
      distSq(p1, p3),
      distSq(p1, p4),
      distSq(p2, p3),
      distSq(p2, p4),
      distSq(p3, p4),
    ];

    d.sort();
    // first four are sides, last two are diagonals
    if (d[0] == 0) return false;
    bool sidesEqual = d[0] == d[1] && d[1] == d[2] && d[2] == d[3];
    bool diagonalsEqual = d[4] == d[5];
    bool diagonalRelation = d[4] == 2 * d[0];

    return sidesEqual && diagonalsEqual && diagonalRelation;
  }
}
```

## Golang

```go
func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	dist := func(a, b []int) int {
		dx := a[0] - b[0]
		dy := a[1] - b[1]
		return dx*dx + dy*dy
	}
	points := [][]int{p1, p2, p3, p4}
	counts := make(map[int]int)
	for i := 0; i < 4; i++ {
		for j := i + 1; j < 4; j++ {
			d := dist(points[i], points[j])
			counts[d]++
		}
	}
	if len(counts) != 2 {
		return false
	}
	var side, diag int
	for d, c := range counts {
		if c == 4 {
			side = d
		} else if c == 2 {
			diag = d
		} else {
			return false
		}
	}
	if side == 0 || diag != 2*side {
		return false
	}
	return true
}
```

## Ruby

```ruby
def valid_square(p1, p2, p3, p4)
  pts = [p1, p2, p3, p4]
  dists = []
  (0...4).each do |i|
    ((i + 1)...4).each do |j|
      dx = pts[i][0] - pts[j][0]
      dy = pts[i][1] - pts[j][1]
      dists << dx * dx + dy * dy
    end
  end
  dists.sort!
  side = dists[0]
  return false if side == 0
  return false unless dists[0] == dists[1] && dists[1] == dists[2] && dists[2] == dists[3]
  return false unless dists[4] == dists[5]
  dists[4] == 2 * side
end
```

## Scala

```scala
object Solution {
  def validSquare(p1: Array[Int], p2: Array[Int], p3: Array[Int], p4: Array[Int]): Boolean = {
    val pts = Array(p1, p2, p3, p4)

    def dist(i: Int, j: Int): Long = {
      val dx = pts(i)(0) - pts(j)(0)
      val dy = pts(i)(1) - pts(j)(1)
      dx.toLong * dx + dy.toLong * dy
    }

    val dists = Array(
      dist(0, 1), dist(0, 2), dist(0, 3),
      dist(1, 2), dist(1, 3),
      dist(2, 3)
    )

    java.util.Arrays.sort(dists)

    // smallest distance must be > 0 (non‑overlapping points)
    if (dists(0) == 0L) return false

    val side = dists(0)
    // first four distances are sides
    if (!(dists(1) == side && dists(2) == side && dists(3) == side)) return false

    // last two distances are diagonals and must be equal
    val diag = dists(4)
    if (dists(5) != diag) return false

    // diagonal length squared should be twice the side length squared
    diag == 2L * side
  }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_square(p1: Vec<i32>, p2: Vec<i32>, p3: Vec<i32>, p4: Vec<i32>) -> bool {
        let points = [p1, p2, p3, p4];
        let mut dists = Vec::with_capacity(6);
        for i in 0..4 {
            for j in (i + 1)..4 {
                let dx = points[i][0] - points[j][0];
                let dy = points[i][1] - points[j][1];
                let dist = (dx as i64) * (dx as i64) + (dy as i64) * (dy as i64);
                dists.push(dist);
            }
        }
        dists.sort_unstable();
        if dists[0] == 0 {
            return false;
        }
        dists[0] == dists[1]
            && dists[1] == dists[2]
            && dists[2] == dists[3]
            && dists[4] == dists[5]
            && dists[4] == 2 * dists[0]
    }
}
```

## Racket

```racket
(define/contract (valid-square p1 p2 p3 p4)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) boolean?)
  (letrec ((dist2 (lambda (a b)
                    (let* ((dx (- (first a) (first b)))
                           (dy (- (second a) (second b))))
                      (+ (* dx dx) (* dy dy))))))
    (let* ((d12 (dist2 p1 p2))
           (d13 (dist2 p1 p3))
           (d14 (dist2 p1 p4))
           (d23 (dist2 p2 p3))
           (d24 (dist2 p2 p4))
           (d34 (dist2 p3 p4))
           (sorted (sort (list d12 d13 d14 d23 d24 d34) <)))
      (match sorted
        [(list s1 s2 s3 s4 d1 d2)
         (and (> s1 0)
              (= s1 s2 s3 s4)
              (= d1 d2)
              (not (= s1 d1)))]
        [_ #false]))))
```

## Erlang

```erlang
-spec valid_square(P1 :: [integer()], P2 :: [integer()], P3 :: [integer()], P4 :: [integer()]) -> boolean().
valid_square(P1, P2, P3, P4) ->
    Dists = lists:sort([
        dist(P1, P2),
        dist(P1, P3),
        dist(P1, P4),
        dist(P2, P3),
        dist(P2, P4),
        dist(P3, P4)
    ]),
    case Dists of
        [S, S, S, S, D, D] when S > 0, D =:= 2 * S -> true;
        _ -> false
    end.

dist([X1, Y1], [X2, Y2]) ->
    Dx = X1 - X2,
    Dy = Y1 - Y2,
    Dx * Dx + Dy * Dy.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_square(p1 :: [integer], p2 :: [integer], p3 :: [integer], p4 :: [integer]) :: boolean
  def valid_square(p1, p2, p3, p4) do
    pts = [p1, p2, p3, p4]

    distances =
      for i <- 0..2,
          j <- (i + 1)..3,
          do: squared_distance(Enum.at(pts, i), Enum.at(pts, j))

    freq = Enum.frequencies(distances)

    if map_size(freq) != 2 do
      false
    else
      [{d1, c1}, {d2, c2}] = Map.to_list(freq)

      {side_len, side_cnt, diag_len, diag_cnt} =
        if d1 < d2 do
          {d1, c1, d2, c2}
        else
          {d2, c2, d1, c1}
        end

      side_cnt == 4 and diag_cnt == 2 and side_len > 0 and diag_len == 2 * side_len
    end
  end

  defp squared_distance([x1, y1], [x2, y2]) do
    dx = x1 - x2
    dy = y1 - y2
    dx * dx + dy * dy
  end
end
```
