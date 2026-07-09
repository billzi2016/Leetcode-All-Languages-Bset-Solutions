# 1886. Determine Whether Matrix Can Be Obtained By Rotation

## Cpp

```cpp
class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        int n = mat.size();
        auto equal = [&](const vector<vector<int>>& a, const vector<vector<int>>& b)->bool{
            for(int i=0;i<n;++i)
                for(int j=0;j<n;++j)
                    if(a[i][j]!=b[i][j]) return false;
            return true;
        };
        for(int rot=0; rot<4; ++rot){
            if(equal(mat, target)) return true;
            vector<vector<int>> rotated(n, vector<int>(n));
            for(int i=0;i<n;++i)
                for(int j=0;j<n;++j)
                    rotated[i][j] = mat[n-1-j][i];
            mat.swap(rotated);
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        int n = mat.length;
        for (int k = 0; k < 4; k++) {
            if (isEqual(mat, target)) return true;
            mat = rotate90(mat, n);
        }
        return false;
    }

    private boolean isEqual(int[][] a, int[][] b) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] != b[i][j]) return false;
            }
        }
        return true;
    }

    private int[][] rotate90(int[][] m, int n) {
        int[][] res = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[j][n - 1 - i] = m[i][j];
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for _ in range(4):
            if mat == target:
                return True
            # rotate 90 degrees clockwise
            n = len(mat)
            rotated = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[j][n - 1 - i] = mat[i][j]
            mat = rotated
        return False
```

## Python3

```python
from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if mat == target:
                return True
            # rotate 90 degrees clockwise
            rotated = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[i][j] = mat[n - 1 - j][i]
            mat = rotated
        return False
```

## C

```c
#include <stdbool.h>

bool findRotation(int** mat, int matSize, int* matColSize, int** target, int targetSize, int* targetColSize) {
    int n = matSize;
    for (int rot = 0; rot < 4; ++rot) {
        bool ok = true;
        for (int i = 0; i < n && ok; ++i) {
            for (int j = 0; j < n; ++j) {
                int v;
                if (rot == 0) v = mat[i][j];
                else if (rot == 1) v = mat[n - 1 - j][i];
                else if (rot == 2) v = mat[n - 1 - i][n - 1 - j];
                else v = mat[j][n - 1 - i];
                if (v != target[i][j]) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool FindRotation(int[][] mat, int[][] target) {
        int n = mat.Length;
        for (int rot = 0; rot < 4; rot++) {
            if (IsEqual(mat, target)) return true;
            mat = Rotate90(mat, n);
        }
        return false;
    }

    private bool IsEqual(int[][] a, int[][] b) {
        int n = a.Length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] != b[i][j]) return false;
            }
        }
        return true;
    }

    private int[][] Rotate90(int[][] m, int n) {
        int[][] res = new int[n][];
        for (int i = 0; i < n; i++) {
            res[i] = new int[n];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = m[n - 1 - j][i];
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @param {number[][]} target
 * @return {boolean}
 */
var findRotation = function(mat, target) {
    const n = mat.length;
    
    const isEqual = (a, b) => {
        for (let i = 0; i < n; ++i) {
            for (let j = 0; j < n; ++j) {
                if (a[i][j] !== b[i][j]) return false;
            }
        }
        return true;
    };
    
    const rotate90 = (m) => {
        const res = Array.from({ length: n }, () => Array(n));
        for (let i = 0; i < n; ++i) {
            for (let j = 0; j < n; ++j) {
                res[j][n - 1 - i] = m[i][j];
            }
        }
        return res;
    };
    
    let cur = mat;
    for (let k = 0; k < 4; ++k) {
        if (isEqual(cur, target)) return true;
        cur = rotate90(cur);
    }
    return false;
};
```

## Typescript

```typescript
function findRotation(mat: number[][], target: number[][]): boolean {
    const n = mat.length;
    
    const isEqual = (a: number[][], b: number[][]): boolean => {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (a[i][j] !== b[i][j]) return false;
            }
        }
        return true;
    };
    
    const rotate = (m: number[][]): number[][] => {
        const res: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                res[i][j] = m[n - 1 - j][i];
            }
        }
        return res;
    };
    
    let cur = mat;
    for (let k = 0; k < 4; k++) {
        if (isEqual(cur, target)) return true;
        cur = rotate(cur);
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer[][] $target
     * @return Boolean
     */
    function findRotation($mat, $target) {
        for ($k = 0; $k < 4; $k++) {
            if ($this->isEqual($mat, $target)) {
                return true;
            }
            $mat = $this->rotate($mat);
        }
        return false;
    }

    private function rotate($mat) {
        $n = count($mat);
        $new = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $new[$i][$j] = $mat[$n - 1 - $j][$i];
            }
        }
        return $new;
    }

    private function isEqual($a, $b) {
        $n = count($a);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($a[$i][$j] !== $b[$i][$j]) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func findRotation(_ mat: [[Int]], _ target: [[Int]]) -> Bool {
        var current = mat
        for _ in 0..<4 {
            if current == target { return true }
            current = rotate(current)
        }
        return false
    }
    
    private func rotate(_ matrix: [[Int]]) -> [[Int]] {
        let n = matrix.count
        var rotated = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n {
                rotated[i][j] = matrix[n - 1 - j][i]
            }
        }
        return rotated
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRotation(mat: Array<IntArray>, target: Array<IntArray>): Boolean {
        var cur = mat
        repeat(4) {
            if (equals(cur, target)) return true
            cur = rotate90(cur)
        }
        return false
    }

    private fun equals(a: Array<IntArray>, b: Array<IntArray>): Boolean {
        val n = a.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (a[i][j] != b[i][j]) return false
            }
        }
        return true
    }

    private fun rotate90(m: Array<IntArray>): Array<IntArray> {
        val n = m.size
        val res = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                res[i][j] = m[n - 1 - j][i]
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  bool findRotation(List<List<int>> mat, List<List<int>> target) {
    for (int r = 0; r < 4; ++r) {
      if (_isEqual(mat, target)) return true;
      mat = _rotate(mat);
    }
    return false;
  }

  bool _isEqual(List<List<int>> a, List<List<int>> b) {
    int n = a.length;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (a[i][j] != b[i][j]) return false;
      }
    }
    return true;
  }

  List<List<int>> _rotate(List<List<int>> m) {
    int n = m.length;
    List<List<int>> res = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        res[i][j] = m[n - 1 - j][i];
      }
    }
    return res;
  }
}
```

## Golang

```go
func findRotation(mat [][]int, target [][]int) bool {
	n := len(mat)
	// helper to compare two matrices
	equal := func(a, b [][]int) bool {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if a[i][j] != b[i][j] {
					return false
				}
			}
		}
		return true
	}
	// helper to rotate matrix clockwise by 90 degrees
	rotate := func(m [][]int) [][]int {
		res := make([][]int, n)
		for i := 0; i < n; i++ {
			res[i] = make([]int, n)
			for j := 0; j < n; j++ {
				res[i][j] = m[n-1-j][i]
			}
		}
		return res
	}

	for k := 0; k < 4; k++ {
		if equal(mat, target) {
			return true
		}
		mat = rotate(mat)
	}
	return false
}
```

## Ruby

```ruby
def find_rotation(mat, target)
  4.times do
    return true if mat == target
    n = mat.length
    rotated = Array.new(n) { Array.new(n) }
    n.times do |i|
      n.times do |j|
        rotated[i][j] = mat[n - 1 - j][i]
      end
    end
    mat = rotated
  end
  false
end
```

## Scala

```scala
object Solution {
    def findRotation(mat: Array[Array[Int]], target: Array[Array[Int]]): Boolean = {
        val n = mat.length
        var cur = mat.map(_.clone())
        for (_ <- 0 until 4) {
            if (equalsMatrix(cur, target)) return true
            cur = rotate90(cur)
        }
        false
    }

    private def rotate90(m: Array[Array[Int]]): Array[Array[Int]] = {
        val n = m.length
        val res = Array.ofDim[Int](n, n)
        for (i <- 0 until n; j <- 0 until n) {
            res(j)(n - 1 - i) = m(i)(j)
        }
        res
    }

    private def equalsMatrix(a: Array[Array[Int]], b: Array[Array[Int]]): Boolean = {
        val n = a.length
        for (i <- 0 until n; j <- 0 until n) {
            if (a(i)(j) != b(i)(j)) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_rotation(mut mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        for _ in 0..4 {
            if mat == target {
                return true;
            }
            let n = mat.len();
            let mut rotated = vec![vec![0; n]; n];
            for i in 0..n {
                for j in 0..n {
                    rotated[i][j] = mat[n - 1 - j][i];
                }
            }
            mat = rotated;
        }
        false
    }
}
```

## Racket

```racket
(define/contract (find-rotation mat target)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      boolean?)
  (letrec ((rotate
            (lambda (m)
              (let ((n (length m)))
                (build-list n
                  (lambda (i)
                    (build-list n
                      (lambda (j)
                        (list-ref (list-ref m (- n 1 j)) i)))))))))
    (let loop ((cur mat) (cnt 0))
      (cond
        [(equal? cur target) #t]
        [(= cnt 3) #f]
        [else (loop (rotate cur) (+ cnt 1))]))))
```

## Erlang

```erlang
-spec find_rotation(Mat :: [[integer()]], Target :: [[integer()]]) -> boolean().
find_rotation(Mat, Target) ->
    find_rotation_helper(Mat, Target, 0).

find_rotation_helper(_, _, 4) -> false;
find_rotation_helper(Mat, Target, Count) ->
    case Mat =:= Target of
        true -> true;
        false -> find_rotation_helper(rotate(Mat), Target, Count + 1)
    end.

rotate(Mat) ->
    N = length(Mat),
    [ [ get_elem(Mat, N - 1 - J, I) || J <- lists:seq(0, N-1) ] || I <- lists:seq(0, N-1) ].

get_elem(Mat, RowIdx, ColIdx) ->
    Row = lists:nth(RowIdx + 1, Mat),
    lists:nth(ColIdx + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_rotation(mat :: [[integer]], target :: [[integer]]) :: boolean
  def find_rotation(mat, target) do
    check(mat, target, 4)
  end

  defp check(_mat, _target, 0), do: false
  defp check(mat, target, rotations) do
    if mat == target do
      true
    else
      check(rotate(mat), target, rotations - 1)
    end
  end

  defp rotate(matrix) do
    n = length(matrix)

    for i <- 0..(n - 1) do
      for j <- 0..(n - 1) do
        matrix
        |> Enum.at(n - 1 - j)
        |> Enum.at(i)
      end
    end
  end
end
```
