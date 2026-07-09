# 1828. Queries on Number of Points Inside a Circle

## Cpp

```cpp
class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int cx = q[0], cy = q[1];
            long long r2 = 1LL * q[2] * q[2];
            int cnt = 0;
            for (const auto& p : points) {
                long long dx = p[0] - cx;
                long long dy = p[1] - cy;
                if (dx*dx + dy*dy <= r2) ++cnt;
            }
            ans.push_back(cnt);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int cx = queries[i][0];
            int cy = queries[i][1];
            int r = queries[i][2];
            int r2 = r * r;
            int count = 0;
            for (int[] p : points) {
                int dx = p[0] - cx;
                int dy = p[1] - cy;
                if (dx * dx + dy * dy <= r2) {
                    count++;
                }
            }
            ans[i] = count;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for x, y, r in queries:
            r2 = r * r
            cnt = 0
            for px, py in points:
                dx = px - x
                dy = py - y
                if dx * dx + dy * dy <= r2:
                    cnt += 1
            ans.append(cnt)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for xq, yq, rq in queries:
            r2 = rq * rq
            cnt = 0
            for xp, yp in points:
                dx = xp - xq
                dy = yp - yq
                if dx * dx + dy * dy <= r2:
                    cnt += 1
            ans.append(cnt)
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countPoints(int** points, int pointsSize, int* pointsColSize,
                 int** queries, int queriesSize, int* queriesColSize,
                 int* returnSize) {
    int *result = (int *)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;
    
    for (int q = 0; q < queriesSize; ++q) {
        int cx = queries[q][0];
        int cy = queries[q][1];
        int r  = queries[q][2];
        long long rsq = (long long)r * r;
        int cnt = 0;
        
        for (int p = 0; p < pointsSize; ++p) {
            long long dx = (long long)points[p][0] - cx;
            long long dy = (long long)points[p][1] - cy;
            if (dx * dx + dy * dy <= rsq) {
                ++cnt;
            }
        }
        result[q] = cnt;
    }
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] CountPoints(int[][] points, int[][] queries) {
        int q = queries.Length;
        int[] answer = new int[q];
        for (int i = 0; i < q; i++) {
            int cx = queries[i][0];
            int cy = queries[i][1];
            int r = queries[i][2];
            long rr = (long)r * r;
            int count = 0;
            foreach (var p in points) {
                long dx = p[0] - cx;
                long dy = p[1] - cy;
                if (dx * dx + dy * dy <= rr) {
                    count++;
                }
            }
            answer[i] = count;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @param {number[][]} queries
 * @return {number[]}
 */
var countPoints = function(points, queries) {
    const ans = new Array(queries.length).fill(0);
    for (let i = 0; i < queries.length; ++i) {
        const [cx, cy, r] = queries[i];
        const r2 = r * r;
        let cnt = 0;
        for (const [px, py] of points) {
            const dx = px - cx;
            const dy = py - cy;
            if (dx * dx + dy * dy <= r2) cnt++;
        }
        ans[i] = cnt;
    }
    return ans;
};
```

## Typescript

```typescript
function countPoints(points: number[][], queries: number[][]): number[] {
    const result: number[] = [];
    for (const [qx, qy, qr] of queries) {
        const r2 = qr * qr;
        let cnt = 0;
        for (const [px, py] of points) {
            const dx = px - qx;
            const dy = py - qy;
            if (dx * dx + dy * dy <= r2) cnt++;
        }
        result.push(cnt);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function countPoints($points, $queries) {
        $result = [];
        foreach ($queries as $q) {
            [$cx, $cy, $r] = $q;
            $r2 = $r * $r;
            $cnt = 0;
            foreach ($points as $p) {
                $dx = $p[0] - $cx;
                $dy = $p[1] - $cy;
                if ($dx * $dx + $dy * $dy <= $r2) {
                    $cnt++;
                }
            }
            $result[] = $cnt;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countPoints(_ points: [[Int]], _ queries: [[Int]]) -> [Int] {
        var answers = [Int]()
        for query in queries {
            let cx = query[0]
            let cy = query[1]
            let r2 = query[2] * query[2]
            var cnt = 0
            for point in points {
                let dx = point[0] - cx
                let dy = point[1] - cy
                if dx * dx + dy * dy <= r2 {
                    cnt += 1
                }
            }
            answers.append(cnt)
        }
        return answers
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPoints(points: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val result = IntArray(queries.size)
        for (i in queries.indices) {
            val q = queries[i]
            val cx = q[0]
            val cy = q[1]
            val r2 = q[2] * q[2]
            var count = 0
            for (p in points) {
                val dx = p[0] - cx
                val dy = p[1] - cy
                if (dx * dx + dy * dy <= r2) {
                    count++
                }
            }
            result[i] = count
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> countPoints(List<List<int>> points, List<List<int>> queries) {
    List<int> answer = List.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      int cx = queries[i][0];
      int cy = queries[i][1];
      int r = queries[i][2];
      int rSq = r * r;
      int count = 0;
      for (var p in points) {
        int dx = p[0] - cx;
        int dy = p[1] - cy;
        if (dx * dx + dy * dy <= rSq) {
          count++;
        }
      }
      answer[i] = count;
    }
    return answer;
  }
}
```

## Golang

```go
func countPoints(points [][]int, queries [][]int) []int {
    ans := make([]int, len(queries))
    for i, q := range queries {
        cx, cy, r := q[0], q[1], q[2]
        rr := r * r
        cnt := 0
        for _, p := range points {
            dx := p[0] - cx
            dy := p[1] - cy
            if dx*dx+dy*dy <= rr {
                cnt++
            }
        }
        ans[i] = cnt
    }
    return ans
}
```

## Ruby

```ruby
def count_points(points, queries)
  result = []
  queries.each do |qx, qy, r|
    r2 = r * r
    cnt = 0
    points.each do |px, py|
      dx = px - qx
      dy = py - qy
      cnt += 1 if dx * dx + dy * dy <= r2
    end
    result << cnt
  end
  result
end
```

## Scala

```scala
object Solution {
    def countPoints(points: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
        val qLen = queries.length
        val res = new Array[Int](qLen)
        var i = 0
        while (i < qLen) {
            val cx = queries(i)(0)
            val cy = queries(i)(1)
            val r2 = queries(i)(2).toLong * queries(i)(2)
            var cnt = 0
            var j = 0
            while (j < points.length) {
                val dx = points(j)(0) - cx
                val dy = points(j)(1) - cy
                if (dx.toLong * dx + dy.toLong * dy <= r2) cnt += 1
                j += 1
            }
            res(i) = cnt
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_points(points: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = Vec::with_capacity(queries.len());
        for q in &queries {
            let cx = q[0] as i64;
            let cy = q[1] as i64;
            let r2 = (q[2] as i64) * (q[2] as i64);
            let mut count = 0;
            for p in &points {
                let dx = p[0] as i64 - cx;
                let dy = p[1] as i64 - cy;
                if dx * dx + dy * dy <= r2 {
                    count += 1;
                }
            }
            result.push(count);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (count-points points queries)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (map
   (lambda (q)
     (let* ((cx (car q))
            (cy (cadr q))
            (r  (caddr q))
            (r2 (* r r)))
       (let loop ((ps points) (cnt 0))
         (if (null? ps)
             cnt
             (let* ((p  (car ps))
                    (dx (- (car p) cx))
                    (dy (- (cadr p) cy))
                    (dist2 (+ (* dx dx) (* dy dy))))
               (loop (cdr ps) (if (<= dist2 r2) (add1 cnt) cnt)))))))
   queries))
```

## Erlang

```erlang
-export([count_points/2]).
-spec count_points(Points :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
count_points(Points, Queries) ->
    lists:map(
      fun([Qx, Qy, R]) ->
          R2 = R * R,
          lists:foldl(
            fun([Px, Py], Acc) ->
                Dx = Px - Qx,
                Dy = Py - Qy,
                if Dx*Dx + Dy*Dy =< R2 -> Acc + 1; true -> Acc end
            end,
            0,
            Points)
      end,
      Queries).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_points(points :: [[integer]], queries :: [[integer]]) :: [integer]
  def count_points(points, queries) do
    Enum.map(queries, fn [qx, qy, r] ->
      rsq = r * r

      Enum.reduce(points, 0, fn [px, py], acc ->
        dx = px - qx
        dy = py - qy

        if dx * dx + dy * dy <= rsq do
          acc + 1
        else
          acc
        end
      end)
    end)
  end
end
```
