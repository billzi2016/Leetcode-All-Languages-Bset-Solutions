# 2509. Cycle Length Queries in a Tree

## Cpp

```cpp
class Solution {
public:
    vector<int> cycleLengthQueries(int n, vector<vector<int>>& queries) {
        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int a = q[0], b = q[1];
            int dist = 0;
            while (a != b) {
                if (a > b) {
                    a >>= 1; // move up to parent
                } else {
                    b >>= 1;
                }
                ++dist;
            }
            ans.push_back(dist + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] cycleLengthQueries(int n, int[][] queries) {
        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int a = queries[i][0];
            int b = queries[i][1];
            int depthA = depth(a);
            int depthB = depth(b);
            int origDepthA = depthA;
            int origDepthB = depthB;
            // Bring to same depth
            while (depthA > depthB) {
                a >>= 1;
                depthA--;
            }
            while (depthB > depthA) {
                b >>= 1;
                depthB--;
            }
            // Ascend together until LCA found
            while (a != b) {
                a >>= 1;
                b >>= 1;
                depthA--;
                depthB--;
            }
            int lcaDepth = depthA; // same as depthB now
            int distance = origDepthA + origDepthB - 2 * lcaDepth;
            ans[i] = distance + 1;
        }
        return ans;
    }

    private int depth(int x) {
        // depth from root (node 1) where root has depth 0
        return 31 - Integer.numberOfLeadingZeros(x);
    }
}
```

## Python

```python
class Solution(object):
    def cycleLengthQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for a, b in queries:
            da = a.bit_length() - 1
            db = b.bit_length() - 1
            steps = 0
            # Bring to same depth
            while da > db:
                a //= 2
                da -= 1
                steps += 1
            while db > da:
                b //= 2
                db -= 1
                steps += 1
            # Ascend together until meet
            while a != b:
                a //= 2
                b //= 2
                steps += 2
            res.append(steps + 1)  # cycle length = distance + 1
        return res
```

## Python3

```python
class Solution:
    def cycleLengthQueries(self, n: int, queries):
        ans = []
        for a, b in queries:
            steps = 0
            while a != b:
                if a > b:
                    a >>= 1
                else:
                    b >>= 1
                steps += 1
            ans.append(steps + 1)
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* cycleLengthQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)n; // n is not needed for computation
    int *ans = (int*)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;
    
    for (int i = 0; i < queriesSize; ++i) {
        int a = queries[i][0];
        int b = queries[i][1];
        int da = 31 - __builtin_clz(a);
        int db = 31 - __builtin_clz(b);
        int dist = 0;
        
        while (da > db) {
            a >>= 1;
            da--;
            dist++;
        }
        while (db > da) {
            b >>= 1;
            db--;
            dist++;
        }
        while (a != b) {
            a >>= 1;
            b >>= 1;
            dist += 2;
        }
        ans[i] = dist + 1; // cycle length equals distance + 1
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] CycleLengthQueries(int n, int[][] queries) {
        int m = queries.Length;
        int[] answer = new int[m];
        for (int i = 0; i < m; i++) {
            int a = queries[i][0];
            int b = queries[i][1];

            int depthA = GetDepth(a);
            int depthB = GetDepth(b);

            int u = a, v = b;
            int da = depthA, db = depthB;

            // Bring both nodes to the same depth
            while (da > db) {
                u >>= 1;
                da--;
            }
            while (db > da) {
                v >>= 1;
                db--;
            }

            // Ascend together until they meet
            while (u != v) {
                u >>= 1;
                v >>= 1;
                da--; // depth decreases equally for both
            }

            int lcaDepth = da; // depth of LCA
            int distance = depthA + depthB - 2 * lcaDepth;
            answer[i] = distance + 1; // cycle length includes the added edge
        }
        return answer;
    }

    private int GetDepth(int x) {
        int d = 0;
        while (x > 1) {
            x >>= 1;
            d++;
        }
        return d;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var cycleLengthQueries = function(n, queries) {
    const res = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        let a = queries[i][0];
        let b = queries[i][1];
        let dist = 0;
        while (a !== b) {
            if (a > b) {
                a >>= 1;
            } else {
                b >>= 1;
            }
            ++dist;
        }
        res[i] = dist + 1; // cycle nodes = path edges + 1
    }
    return res;
};
```

## Typescript

```typescript
function cycleLengthQueries(n: number, queries: number[][]): number[] {
    const ans: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        let a = queries[i][0];
        let b = queries[i][1];
        let dist = 0;
        while (a !== b) {
            if (a > b) {
                a >>= 1;
            } else {
                b >>= 1;
            }
            dist++;
        }
        ans[i] = dist + 1;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function cycleLengthQueries($n, $queries) {
        $ans = [];
        foreach ($queries as $q) {
            [$a, $b] = $q;
            $da = $this->depth($a);
            $db = $this->depth($b);
            $origDa = $da;
            $origDb = $db;

            // lift deeper node
            while ($da > $db) {
                $a >>= 1;
                $da--;
            }
            while ($db > $da) {
                $b >>= 1;
                $db--;
            }

            // lift both until meet
            while ($a !== $b) {
                $a >>= 1;
                $b >>= 1;
                $da--; // depth of LCA will be this after loop
            }
            $depthLca = $da; // same as $db now

            $dist = $origDa + $origDb - 2 * $depthLca;
            $ans[] = $dist + 1; // number of nodes in the cycle
        }
        return $ans;
    }

    private function depth($x) {
        $d = 0;
        while ($x > 1) {
            $x >>= 1;
            $d++;
        }
        return $d;
    }
}
```

## Swift

```swift
class Solution {
    func cycleLengthQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let a0 = q[0]
            let b0 = q[1]
            let depthA = nodeDepth(a0)
            let depthB = nodeDepth(b0)
            var a = a0
            var b = b0
            var da = depthA
            var db = depthB
            
            while da > db {
                a >>= 1
                da -= 1
            }
            while db > da {
                b >>= 1
                db -= 1
            }
            while a != b {
                a >>= 1
                b >>= 1
                da -= 1
            }
            let lcaDepth = da
            let distance = depthA + depthB - 2 * lcaDepth
            result.append(distance + 1)
        }
        return result
    }
    
    private func nodeDepth(_ x: Int) -> Int {
        var v = x
        var d = 0
        while v > 1 {
            v >>= 1
            d += 1
        }
        return d
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun cycleLengthQueries(n: Int, queries: Array<IntArray>): IntArray {
        val m = queries.size
        val ans = IntArray(m)
        for (i in 0 until m) {
            var a = queries[i][0]
            var b = queries[i][1]
            var dist = 0
            var da = depth(a)
            var db = depth(b)
            while (da > db) {
                a = a / 2
                da--
                dist++
            }
            while (db > da) {
                b = b / 2
                db--
                dist++
            }
            while (a != b) {
                a = a / 2
                b = b / 2
                dist += 2
            }
            ans[i] = dist + 1
        }
        return ans
    }

    private fun depth(x: Int): Int {
        // depth of node x in a binary heap (root at 1) is floor(log2(x))
        return 31 - Integer.numberOfLeadingZeros(x)
    }
}
```

## Dart

```dart
class Solution {
  List<int> cycleLengthQueries(int n, List<List<int>> queries) {
    int m = queries.length;
    List<int> ans = List.filled(m, 0);
    for (int i = 0; i < m; i++) {
      int a = queries[i][0];
      int b = queries[i][1];

      int depthA = a.bitLength - 1;
      int depthB = b.bitLength - 1;

      int aa = a, bb = b;
      int da = depthA, db = depthB;

      while (aa != bb) {
        if (da > db) {
          aa >>= 1;
          da--;
        } else if (db > da) {
          bb >>= 1;
          db--;
        } else {
          aa >>= 1;
          bb >>= 1;
          da--;
          db--;
        }
      }

      int depthLCA = da; // same as db now
      int distance = depthA + depthB - 2 * depthLCA;
      ans[i] = distance + 1;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "math/bits"

func cycleLengthQueries(n int, queries [][]int) []int {
	ans := make([]int, len(queries))
	for i, q := range queries {
		a, b := q[0], q[1]
		da, db := depth(a), depth(b)
		aa, bb := a, b
		for da > db {
			aa >>= 1
			da--
		}
		for db > da {
			bb >>= 1
			db--
		}
		for aa != bb {
			aa >>= 1
			bb >>= 1
		}
		lcaDepth := depth(aa)
		dist := depth(a) + depth(b) - 2*lcaDepth
		ans[i] = dist + 1
	}
	return ans
}

func depth(x int) int {
	return bits.Len(uint(x)) - 1
}
```

## Ruby

```ruby
def cycle_length_queries(n, queries)
  result = []
  queries.each do |a, b|
    # depth of a
    da = 0
    x = a
    while x > 0
      da += 1
      x >>= 1
    end
    da -= 1

    # depth of b
    db = 0
    x = b
    while x > 0
      db += 1
      x >>= 1
    end
    db -= 1

    aa = a
    bb = b
    # find LCA by climbing the larger node
    while aa != bb
      if aa > bb
        aa >>= 1
      else
        bb >>= 1
      end
    end

    # depth of LCA
    dl = 0
    x = aa
    while x > 0
      dl += 1
      x >>= 1
    end
    dl -= 1

    dist = da + db - 2 * dl
    result << (dist + 1)
  end
  result
end
```

## Scala

```scala
object Solution {
    def cycleLengthQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
        val m = queries.length
        val res = new Array[Int](m)
        for (i <- 0 until m) {
            val aOrig = queries(i)(0)
            val bOrig = queries(i)(1)

            var a = aOrig
            var b = bOrig
            var da = depth(a)
            var db = depth(b)

            // lift deeper node
            while (da > db) { a >>= 1; da -= 1 }
            while (db > da) { b >>= 1; db -= 1 }

            // lift both until meet
            while (a != b) {
                a >>= 1
                b >>= 1
                da -= 1   // depth decreases together
            }
            val lcaDepth = da

            val dist = depth(aOrig) + depth(bOrig) - 2 * lcaDepth
            res(i) = dist + 1
        }
        res
    }

    private def depth(x: Int): Int = {
        31 - Integer.numberOfLeadingZeros(x)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn cycle_length_queries(_n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        fn depth(mut x: i32) -> i32 {
            let mut d = 0;
            while x > 1 {
                x >>= 1;
                d += 1;
            }
            d
        }

        let mut res = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let mut a = q[0];
            let mut b = q[1];

            // compute depths
            let da = depth(a);
            let db = depth(b);

            // find LCA by climbing the larger node
            let (mut x, mut y) = (a, b);
            while x != y {
                if x > y {
                    x >>= 1;
                } else {
                    y >>= 1;
                }
            }
            let dlca = depth(x);

            let distance = da + db - 2 * dlca;
            res.push(distance + 1);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (cycle-length-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (letrec
      ((depth
        (lambda (x)
          (- (integer-length x) 1)))
       (distance
        (lambda (a b)
          (let loop ((a a) (b b) (da (depth a)) (db (depth b)) (dist 0))
            (cond
              [(> da db) (loop (quotient a 2) b (- da 1) db (+ dist 1))]
              [(< da db) (loop a (quotient b 2) da (- db 1) (+ dist 1))]
              [else (if (= a b)
                        dist
                        (loop (quotient a 2) (quotient b 2) (- da 1) (- db 1) (+ dist 2)))])))))
    (map (lambda (pair)
           (let* ((a (first pair))
                  (b (second pair))
                  (dist (distance a b)))
             (+ dist 1)))
         queries)))
```

## Erlang

```erlang
-module(solution).
-export([cycle_length_queries/2]).

-spec cycle_length_queries(N :: integer(), Queries :: [[integer()]]) -> [integer()].
cycle_length_queries(_N, Queries) ->
    lists:map(fun([A,B]) -> distance(A,B) + 1 end, Queries).

depth(Val) -> depth(Val,0).
depth(1, Acc) -> Acc;
depth(V, Acc) -> depth(V div 2, Acc+1).

distance(A,B) ->
    Da = depth(A),
    Db = depth(B),
    distance(A,B,Da,Db,0).

distance(A,B,Da,Db,Dist) when Da > Db ->
    distance(A div 2, B, Da-1, Db, Dist+1);
distance(A,B,Da,Db,Dist) when Db > Da ->
    distance(A, B div 2, Da, Db-1, Dist+1);
distance(A,B,_Da,_Db,Dist) when A =:= B ->
    Dist;
distance(A,B,Da,Db,Dist) ->
    distance(A div 2, B div 2, Da-1, Db-1, Dist+2).
```

## Elixir

```elixir
defmodule Solution do
  @spec cycle_length_queries(n :: integer, queries :: [[integer]]) :: [integer]
  def cycle_length_queries(_n, queries) do
    Enum.map(queries, fn [a, b] ->
      da = depth(a)
      db = depth(b)
      lca = find_lca(a, b)
      dl = depth(lca)
      (da + db - 2 * dl) + 1
    end)
  end

  defp depth(x), do: Integer.bit_size(x) - 1

  defp find_lca(a, b) when a == b, do: a
  defp find_lca(a, b) do
    if a > b do
      find_lca(div(a, 2), b)
    else
      find_lca(a, div(b, 2))
    end
  end
end
```
