# 3025. Find the Number of Ways to Place People I

## Cpp

```cpp
class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int xi = points[i][0], yi = points[i][1];
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                int xj = points[j][0], yj = points[j][1];
                // i should be upper-left of j
                if (xi <= xj && yi >= yj && (xi < xj || yi > yj)) {
                    bool ok = true;
                    for (int k = 0; k < n; ++k) {
                        if (k == i || k == j) continue;
                        int xk = points[k][0], yk = points[k][1];
                        if (xi <= xk && xk <= xj && yj <= yk && yk <= yi) {
                            ok = false;
                            break;
                        }
                    }
                    if (ok) ++ans;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numberOfPairs(int[][] points) {
        int n = points.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int x2 = points[j][0];
                int y2 = points[j][1];
                // A is upper-left of B
                if (x1 < x2 && y1 > y2) {
                    boolean ok = true;
                    for (int k = 0; k < n; k++) {
                        if (k == i || k == j) continue;
                        int x = points[k][0];
                        int y = points[k][1];
                        if (x1 <= x && x <= x2 && y2 <= y && y <= y1) {
                            ok = false;
                            break;
                        }
                    }
                    if (ok) ans++;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        cnt = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                # check if i is upper-left of j
                if x1 <= x2 and y1 >= y2:
                    ok = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if x1 < xk < x2 and y2 < yk < y1:
                            ok = False
                            break
                    if ok:
                        cnt += 1
                # check if j is upper-left of i
                elif x2 <= x1 and y2 >= y1:
                    ok = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if x2 < xk < x1 and y1 < yk < y2:
                            ok = False
                            break
                    if ok:
                        cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        ans = 0
        for i in range(n):
            xi, yi = points[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = points[j]
                if xi <= xj and yi >= yj:
                    ok = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if xi <= xk <= xj and yj <= yk <= yi:
                            ok = False
                            break
                    if ok:
                        ans += 1
        return ans
```

## C

```c
int numberOfPairs(int** points, int pointsSize, int* pointsColSize) {
    int ans = 0;
    for (int i = 0; i < pointsSize; ++i) {
        int xi = points[i][0];
        int yi = points[i][1];
        for (int j = 0; j < pointsSize; ++j) {
            if (i == j) continue;
            int xj = points[j][0];
            int yj = points[j][1];
            if (xi < xj && yi > yj) { // i is upper‑left of j
                int ok = 1;
                for (int k = 0; k < pointsSize; ++k) {
                    if (k == i || k == j) continue;
                    int xk = points[k][0];
                    int yk = points[k][1];
                    if (xk >= xi && xk <= xj && yk >= yj && yk <= yi) {
                        ok = 0;
                        break;
                    }
                }
                if (ok) ++ans;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfPairs(int[][] points) {
        int n = points.Length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (points[i][0] < points[j][0] && points[i][1] > points[j][1]) {
                    bool ok = true;
                    for (int k = 0; k < n; k++) {
                        if (k == i || k == j) continue;
                        int x = points[k][0];
                        int y = points[k][1];
                        if (points[i][0] <= x && x <= points[j][0] &&
                            points[j][1] <= y && y <= points[i][1]) {
                            ok = false;
                            break;
                        }
                    }
                    if (ok) count++;
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfPairs = function(points) {
    const n = points.length;
    let count = 0;
    for (let i = 0; i < n; ++i) {
        const [x1, y1] = points[i];
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            const [x2, y2] = points[j];
            // A is upper-left of B
            if (x1 < x2 && y1 > y2) {
                let ok = true;
                for (let k = 0; k < n; ++k) {
                    if (k === i || k === j) continue;
                    const [x, y] = points[k];
                    if (x >= x1 && x <= x2 && y <= y1 && y >= y2) {
                        ok = false;
                        break;
                    }
                }
                if (ok) count++;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function numberOfPairs(points: number[][]): number {
    const n = points.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const [x1, y1] = points[i];
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const [x2, y2] = points[j];
            if (x1 <= x2 && y1 >= y2) {
                let ok = true;
                for (let k = 0; k < n; k++) {
                    if (k === i || k === j) continue;
                    const [xk, yk] = points[k];
                    if (x1 < xk && xk < x2 && y2 < yk && yk < y1) {
                        ok = false;
                        break;
                    }
                }
                if (ok) ans++;
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function numberOfPairs($points) {
        $n = count($points);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $x1 = $points[$i][0];
                $y1 = $points[$i][1];
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];

                $validPair = false;
                $ulX = $ulY = $lrX = $lrY = 0;

                if ($x1 <= $x2 && $y1 >= $y2) {
                    $validPair = true;
                    $ulX = $x1; $ulY = $y1;
                    $lrX = $x2; $lrY = $y2;
                } elseif ($x2 <= $x1 && $y2 >= $y1) {
                    $validPair = true;
                    $ulX = $x2; $ulY = $y2;
                    $lrX = $x1; $lrY = $y1;
                }

                if (!$validPair) continue;

                $empty = true;
                for ($k = 0; $k < $n; $k++) {
                    if ($k == $i || $k == $j) continue;
                    $x = $points[$k][0];
                    $y = $points[$k][1];
                    if ($ulX <= $x && $x <= $lrX && $lrY <= $y && $y <= $ulY) {
                        $empty = false;
                        break;
                    }
                }

                if ($empty) $ans++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPairs(_ points: [[Int]]) -> Int {
        let n = points.count
        var result = 0
        for i in 0..<n {
            let xi = points[i][0]
            let yi = points[i][1]
            for j in 0..<n where i != j {
                let xj = points[j][0]
                let yj = points[j][1]
                if xi <= xj && yi >= yj && !(xi == xj && yi == yj) {
                    var ok = true
                    for k in 0..<n where k != i && k != j {
                        let xk = points[k][0]
                        let yk = points[k][1]
                        if xi <= xk && xk <= xj && yj <= yk && yk <= yi {
                            ok = false
                            break
                        }
                    }
                    if ok { result += 1 }
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPairs(points: Array<IntArray>): Int {
        val n = points.size
        var count = 0
        for (i in 0 until n) {
            val xi = points[i][0]
            val yi = points[i][1]
            for (j in 0 until n) {
                if (i == j) continue
                val xj = points[j][0]
                val yj = points[j][1]
                // i as upper-left, j as lower-right
                if (xi < xj && yi > yj) {
                    var ok = true
                    for (k in 0 until n) {
                        if (k == i || k == j) continue
                        val xk = points[k][0]
                        val yk = points[k][1]
                        if (xk >= xi && xk <= xj && yk >= yj && yk <= yi) {
                            ok = false
                            break
                        }
                    }
                    if (ok) count++
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPairs(List<List<int>> points) {
    int n = points.length;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        int x1 = points[i][0];
        int y1 = points[i][1];
        int x2 = points[j][0];
        int y2 = points[j][1];
        if (x1 <= x2 && y1 >= y2) {
          bool ok = true;
          for (int k = 0; k < n; ++k) {
            if (k == i || k == j) continue;
            int x = points[k][0];
            int y = points[k][1];
            if (x1 < x && x < x2 && y2 < y && y < y1) {
              ok = false;
              break;
            }
          }
          if (ok) ans++;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func numberOfPairs(points [][]int) int {
    n := len(points)
    count := 0
    for i := 0; i < n; i++ {
        xi, yi := points[i][0], points[i][1]
        for j := 0; j < n; j++ {
            if i == j {
                continue
            }
            xj, yj := points[j][0], points[j][1]
            if xi < xj && yi > yj { // A is upper‑left of B
                ok := true
                for k := 0; k < n; k++ {
                    if k == i || k == j {
                        continue
                    }
                    xk, yk := points[k][0], points[k][1]
                    if xi < xk && xk < xj && yj < yk && yk < yi {
                        ok = false
                        break
                    }
                }
                if ok {
                    count++
                }
            }
        }
    }
    return count
}
```

## Ruby

```ruby
def number_of_pairs(points)
  n = points.size
  count = 0
  (0...n).each do |i|
    xi, yi = points[i]
    (0...n).each do |j|
      next if i == j
      xj, yj = points[j]
      next unless xi < xj && yi > yj
      ok = true
      (0...n).each do |k|
        next if k == i || k == j
        xk, yk = points[k]
        if xi <= xk && xk <= xj && yj <= yk && yk <= yi
          ok = false
          break
        end
      end
      count += 1 if ok
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def numberOfPairs(points: Array[Array[Int]]): Int = {
        val n = points.length
        var ans = 0
        for (i <- 0 until n) {
            val xi = points(i)(0)
            val yi = points(i)(1)
            for (j <- i + 1 until n) {
                val xj = points(j)(0)
                val yj = points(j)(1)

                var ulX = 0
                var ulY = 0
                var lrX = 0
                var lrY = 0
                var okOrientation = false

                if (xi <= xj && yi >= yj) {
                    ulX = xi; ulY = yi; lrX = xj; lrY = yj
                    okOrientation = true
                } else if (xj <= xi && yj >= yi) {
                    ulX = xj; ulY = yj; lrX = xi; lrY = yi
                    okOrientation = true
                }

                if (!okOrientation) {
                    // not an upper‑left / lower‑right pair
                } else {
                    var empty = true
                    for (k <- 0 until n if empty && k != i && k != j) {
                        val xk = points(k)(0)
                        val yk = points(k)(1)
                        if (ulX <= xk && xk <= lrX && lrY <= yk && yk <= ulY) {
                            empty = false
                        }
                    }
                    if (empty) ans += 1
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_pairs(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut ans = 0;
        for i in 0..n {
            let (xi, yi) = (points[i][0], points[i][1]);
            for j in 0..n {
                if i == j { continue; }
                let (xj, yj) = (points[j][0], points[j][1]);
                if xi < xj && yi > yj {
                    let mut ok = true;
                    for k in 0..n {
                        if k == i || k == j { continue; }
                        let (xk, yk) = (points[k][0], points[k][1]);
                        if xi <= xk && xk <= xj && yj <= yk && yk <= yi {
                            ok = false;
                            break;
                        }
                    }
                    if ok {
                        ans += 1;
                    }
                }
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-pairs points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ((n (length points)))
    (let loop ((i 0) (cnt 0))
      (if (= i n)
          cnt
          (let inner ((j 0) (cnt2 cnt))
            (if (= j n)
                (loop (+ i 1) cnt2)
                (if (or (= i j)
                        (not (< (first (list-ref points i)) (first (list-ref points j))))
                        (not (> (second (list-ref points i)) (second (list-ref points j)))))
                    (inner (+ j 1) cnt2)
                    (let* ((x1 (first (list-ref points i)))
                           (y1 (second (list-ref points i)))
                           (x2 (first (list-ref points j)))
                           (y2 (second (list-ref points j))))
                      (let ((ok?
                             (for/and ([k (in-range n)]
                                       #:when (not (or (= k i) (= k j))))
                               (let ((x (first (list-ref points k)))
                                     (y (second (list-ref points k))))
                                 (or (< x x1) (> x x2) (< y y2) (> y y1))))))
                        (inner (+ j 1) (if ok? (+ cnt2 1) cnt2)))))))))))
```

## Erlang

```erlang
-spec number_of_pairs(Points :: [[integer()]]) -> integer().
number_of_pairs(Points) ->
    Pairs = [{X1, Y1, X2, Y2} ||
                [X1, Y1] <- Points,
                [X2, Y2] <- Points,
                X1 < X2,
                Y1 > Y2],
    lists:foldl(fun({X1, Y1, X2, Y2}, Acc) ->
        case has_inner_point(Points, X1, Y1, X2, Y2) of
            true -> Acc;
            false -> Acc + 1
        end
    end, 0, Pairs).

-spec has_inner_point([[integer()]], integer(), integer(), integer(), integer()) -> boolean().
has_inner_point(Points, X1, Y1, X2, Y2) ->
    lists:any(fun([X, Y]) ->
        (X >= X1 andalso X =< X2) andalso
        (Y =< Y1 andalso Y >= Y2) andalso
        not ((X == X1 andalso Y == Y1) orelse (X == X2 andalso Y == Y2))
    end, Points).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(points :: [[integer]]) :: integer
  def number_of_pairs(points) do
    points_list = Enum.map(points, fn [x, y] -> {x, y} end)
    n = length(points_list)

    Enum.reduce(0..(n - 1), 0, fn i, acc_i ->
      Enum.reduce(0..(n - 1), acc_i, fn j, acc_j ->
        if i != j do
          {x1, y1} = Enum.at(points_list, i)
          {x2, y2} = Enum.at(points_list, j)

          if x1 < x2 and y1 > y2 do
            ok =
              Enum.all?(0..(n - 1), fn k ->
                if k == i or k == j do
                  true
                else
                  {x, y} = Enum.at(points_list, k)
                  not (x1 <= x and x <= x2 and y2 <= y and y <= y1)
                end
              end)

            if ok, do: acc_j + 1, else: acc_j
          else
            acc_j
          end
        else
          acc_j
        end
      end)
    end)
  end
end
```
