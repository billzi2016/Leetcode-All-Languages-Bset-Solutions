# 2946. Matrix Similarity After Cyclic Shifts

## Cpp

```cpp
class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        int shift = k % n;
        for (int i = 0; i < m; ++i) {
            int leftShift = (i % 2 == 0) ? shift : (n - shift) % n;
            if (leftShift == 0) continue;
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] != mat[i][(j + leftShift) % n])
                    return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        int m = mat.length;
        int n = mat[0].length;
        int shift = k % n;
        if (shift == 0) return true;
        for (int i = 0; i < m; i++) {
            if ((i & 1) == 0) { // even row: left shift
                for (int j = 0; j < n; j++) {
                    if (mat[i][j] != mat[i][(j + shift) % n]) return false;
                }
            } else { // odd row: right shift
                for (int j = 0; j < n; j++) {
                    int idx = j - shift;
                    if (idx < 0) idx += n;
                    if (mat[i][j] != mat[i][idx]) return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])
        k_mod = k % n
        for i in range(m):
            shift = k_mod if i % 2 == 0 else (n - k_mod) % n
            if shift == 0:
                continue
            row = mat[i]
            for j in range(n):
                if row[j] != row[(j + shift) % n]:
                    return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        if not mat:
            return True
        n = len(mat[0])
        shift = k % n
        if shift == 0:
            return True
        for i, row in enumerate(mat):
            if i % 2 == 0:  # left shift
                rotated = row[shift:] + row[:shift]
            else:           # right shift
                rotated = row[-shift:] + row[:-shift]
            if rotated != row:
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool areSimilar(int** mat, int matSize, int* matColSize, int k) {
    for (int i = 0; i < matSize; ++i) {
        int n = matColSize[i];
        if (n == 0) continue;
        int shift = k % n;
        if (shift == 0) continue;

        if ((i & 1) == 0) { // even row: left shift
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] != mat[i][(j + shift) % n])
                    return false;
            }
        } else { // odd row: right shift -> equivalent left shift by n - shift
            int leftShift = (n - shift) % n;
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] != mat[i][(j + leftShift) % n])
                    return false;
            }
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool AreSimilar(int[][] mat, int k) {
        int m = mat.Length;
        if (m == 0) return true;
        int n = mat[0].Length;
        int shift = k % n;
        if (shift == 0) return true;

        for (int i = 0; i < m; i++) {
            if ((i & 1) == 0) { // even row: left shift
                for (int j = 0; j < n; j++) {
                    if (mat[i][j] != mat[i][(j + shift) % n])
                        return false;
                }
            } else { // odd row: right shift
                for (int j = 0; j < n; j++) {
                    int idx = j - shift;
                    if (idx < 0) idx += n;
                    if (mat[i][j] != mat[i][idx])
                        return false;
                }
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {boolean}
 */
var areSimilar = function(mat, k) {
    const m = mat.length;
    const n = mat[0].length;
    const s = k % n;
    if (s === 0) return true; // full cycles bring rows back to original
    
    for (let i = 0; i < m; ++i) {
        // effective left shift amount for this row
        const shift = (i % 2 === 0) ? s : (n - s);
        for (let j = 0; j < n; ++j) {
            if (mat[i][j] !== mat[i][(j + shift) % n]) return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function areSimilar(mat: number[][], k: number): boolean {
    const m = mat.length;
    const n = mat[0].length;
    const shift = k % n;
    if (shift === 0) return true;

    for (let i = 0; i < m; i++) {
        const row = mat[i];
        const offset = (i % 2 === 0) ? shift : (n - shift);
        for (let j = 0; j < n; j++) {
            if (row[j] !== row[(j + offset) % n]) return false;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Boolean
     */
    function areSimilar($mat, $k) {
        $m = count($mat);
        if ($m == 0) return true;
        $n = count($mat[0]);
        $shift = $k % $n;
        $original = $mat;

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i % 2 == 0) { // even row: left shift
                    $origIdx = ($j + $shift) % $n;
                } else { // odd row: right shift
                    $origIdx = ($j + $n - $shift) % $n;
                }
                if ($mat[$i][$j] !== $original[$i][$origIdx]) {
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
    func areSimilar(_ mat: [[Int]], _ k: Int) -> Bool {
        let m = mat.count
        guard let n = mat.first?.count else { return true }
        if n == 1 { return true }
        let shiftMod = k % n
        for i in 0..<m {
            var shift = 0
            if i % 2 == 0 {
                shift = shiftMod
            } else {
                shift = (n - shiftMod) % n
            }
            if shift == 0 { continue }
            let row = mat[i]
            for j in 0..<n {
                if row[j] != row[(j + shift) % n] {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun areSimilar(mat: Array<IntArray>, k: Int): Boolean {
        val m = mat.size
        val n = mat[0].size
        if (n == 1) return true
        val shift = k % n
        for (i in 0 until m) {
            val leftShift = if (i % 2 == 0) shift else (n - shift) % n
            if (leftShift == 0) continue
            val row = mat[i]
            for (j in 0 until n) {
                if (row[j] != row[(j + leftShift) % n]) return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool areSimilar(List<List<int>> mat, int k) {
    int m = mat.length;
    int n = mat[0].length;
    int shift = k % n;
    if (shift == 0) return true;

    for (int i = 0; i < m; i++) {
      int offset = (i % 2 == 0) ? shift : (n - shift);
      // Normalize offset in case n - shift == n
      offset %= n;
      List<int> row = mat[i];
      for (int j = 0; j < n; j++) {
        if (row[j] != row[(j + offset) % n]) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func areSimilar(mat [][]int, k int) bool {
    if len(mat) == 0 {
        return true
    }
    n := len(mat[0])
    shift := k % n
    if shift == 0 {
        return true
    }
    for i, row := range mat {
        if i%2 == 0 { // even rows: left shift
            for j := 0; j < n; j++ {
                if row[j] != row[(j+shift)%n] {
                    return false
                }
            }
        } else { // odd rows: right shift
            for j := 0; j < n; j++ {
                if row[j] != row[(j-shift+n)%n] {
                    return false
                }
            }
        }
    }
    return true
}
```

## Ruby

```ruby
def are_similar(mat, k)
  n = mat[0].length
  shift = k % n
  return true if shift == 0
  mat.each_with_index do |row, i|
    shifted = i.even? ? row.rotate(shift) : row.rotate(-shift)
    return false unless shifted == row
  end
  true
end
```

## Scala

```scala
object Solution {
    def areSimilar(mat: Array[Array[Int]], k: Int): Boolean = {
        val m = mat.length
        if (m == 0) return true
        val n = mat(0).length
        val shift = k % n
        for (i <- 0 until m) {
            val targetShift = if (i % 2 == 0) shift else (n - shift) % n
            if (targetShift != 0) {
                val row = mat(i)
                for (j <- 0 until n) {
                    if (row(j) != row((j + targetShift) % n)) return false
                }
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn are_similar(mat: Vec<Vec<i32>>, k: i32) -> bool {
        let n = mat[0].len();
        let shift = (k as usize) % n;
        if shift == 0 {
            return true;
        }
        for row in &mat {
            for j in 0..n {
                if row[j] != row[(j + shift) % n] {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (are-similar mat k)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  (let* ((n (length (first mat)))
         (kmod (remainder k n))
         (rotate-left
          (lambda (lst s)
            (let ((len (length lst))
                  (s (modulo s len)))
              (append (drop lst s) (take lst s))))))
    (let loop ((i 0) (rows mat))
      (cond [(null? rows) #t]
            [else
             (define row (first rows))
             (define shift (if (even? i) kmod (- kmod)))
             (define shifted (rotate-left row shift))
             (if (equal? shifted row)
                 (loop (+ i 1) (rest rows))
                 #f)]))))
```

## Erlang

```erlang
-spec are_similar(Mat :: [[integer()]], K :: integer()) -> boolean().
are_similar(Mat, K) ->
    case Mat of
        [] -> true;
        [FirstRow | _] ->
            N = length(FirstRow),
            ShiftK = K rem N,
            check_rows(Mat, ShiftK, N, 0)
    end.

check_rows([], _, _, _) -> true;
check_rows([Row | Rest], ShiftK, N, Index) ->
    Shift = case Index rem 2 of
                0 -> ShiftK;
                1 -> (N - ShiftK) rem N
            end,
    case shift_equal(Row, Shift) of
        true -> check_rows(Rest, ShiftK, N, Index + 1);
        false -> false
    end.

shift_equal(_, 0) -> true;
shift_equal(Row, Shift) ->
    {Left, Right} = lists:split(Shift, Row),
    Rotated = Right ++ Left,
    Row == Rotated.
```

## Elixir

```elixir
defmodule Solution do
  @spec are_similar(mat :: [[integer]], k :: integer) :: boolean
  def are_similar(mat, k) do
    n = length(List.first(mat))
    shift = rem(k, n)

    Enum.with_index(mat)
    |> Enum.all?(fn {row, idx} ->
      left_shift =
        if rem(idx, 2) == 0 do
          shift
        else
          rem(n - shift, n)
        end

      rotate_left(row, left_shift) == row
    end)
  end

  defp rotate_left(list, 0), do: list
  defp rotate_left(list, l) do
    {a, b} = Enum.split(list, l)
    b ++ a
  end
end
```
