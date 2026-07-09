# 1572. Matrix Diagonal Sum

## Cpp

```cpp
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += mat[i][i];
            ans += mat[n - 1 - i][i];
        }
        if (n % 2 == 1) {
            ans -= mat[n / 2][n / 2];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int diagonalSum(int[][] mat) {
        int n = mat.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += mat[i][i];                 // primary diagonal
            sum += mat[n - 1 - i][i];         // secondary diagonal
        }
        if ((n & 1) == 1) { // odd size, subtract the middle element counted twice
            sum -= mat[n / 2][n / 2];
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]               # primary diagonal
            total += mat[n - 1 - i][i]       # secondary diagonal
        if n % 2 == 1:
            mid = n // 2
            total -= mat[mid][mid]           # subtract the overlapping center element
        return total
```

## Python3

```python
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[n - 1 - i][i]
        if n % 2 == 1:
            mid = n // 2
            total -= mat[mid][mid]
        return total
```

## C

```c
int diagonalSum(int** mat, int matSize, int* matColSize) {
    int n = matSize;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += mat[i][i];
        sum += mat[i][n - 1 - i];
    }
    if (n % 2 == 1) {
        int mid = n / 2;
        sum -= mat[mid][mid];
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int DiagonalSum(int[][] mat) {
        int n = mat.Length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += mat[i][i];
            sum += mat[n - 1 - i][i];
        }
        if ((n & 1) == 1) {
            sum -= mat[n / 2][n / 2];
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    const n = mat.length;
    let sum = 0;
    for (let i = 0; i < n; ++i) {
        sum += mat[i][i];
        sum += mat[n - 1 - i][i];
    }
    if (n % 2 === 1) {
        const mid = Math.floor(n / 2);
        sum -= mat[mid][mid];
    }
    return sum;
};
```

## Typescript

```typescript
function diagonalSum(mat: number[][]): number {
    const n = mat.length;
    let sum = 0;
    for (let i = 0; i < n; ++i) {
        sum += mat[i][i];
        sum += mat[n - 1 - i][i];
    }
    if (n % 2 === 1) {
        const mid = Math.floor(n / 2);
        sum -= mat[mid][mid];
    }
    return sum;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function diagonalSum($mat) {
        $n = count($mat);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += $mat[$i][$i];
            $ans += $mat[$n - 1 - $i][$i];
        }
        if ($n % 2 == 1) {
            $mid = intdiv($n, 2);
            $ans -= $mat[$mid][$mid];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func diagonalSum(_ mat: [[Int]]) -> Int {
        let n = mat.count
        var sum = 0
        for i in 0..<n {
            sum += mat[i][i]
            sum += mat[n - 1 - i][i]
        }
        if n % 2 == 1 {
            sum -= mat[n / 2][n / 2]
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun diagonalSum(mat: Array<IntArray>): Int {
        val n = mat.size
        var sum = 0
        for (i in 0 until n) {
            sum += mat[i][i]
            sum += mat[n - 1 - i][i]
        }
        if (n % 2 == 1) {
            sum -= mat[n / 2][n / 2]
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int diagonalSum(List<List<int>> mat) {
    int n = mat.length;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      ans += mat[i][i];
      ans += mat[n - 1 - i][i];
    }
    if (n % 2 == 1) {
      ans -= mat[n ~/ 2][n ~/ 2];
    }
    return ans;
  }
}
```

## Golang

```go
func diagonalSum(mat [][]int) int {
    n := len(mat)
    sum := 0
    for i := 0; i < n; i++ {
        sum += mat[i][i]
        sum += mat[n-1-i][i]
    }
    if n%2 == 1 {
        mid := n / 2
        sum -= mat[mid][mid]
    }
    return sum
}
```

## Ruby

```ruby
def diagonal_sum(mat)
  n = mat.length
  ans = 0
  (0...n).each do |i|
    ans += mat[i][i]
    ans += mat[n - 1 - i][i]
  end
  ans -= mat[n / 2][n / 2] if n.odd?
  ans
end
```

## Scala

```scala
object Solution {
    def diagonalSum(mat: Array[Array[Int]]): Int = {
        val n = mat.length
        var sum = 0
        for (i <- 0 until n) {
            sum += mat(i)(i)
            sum += mat(n - 1 - i)(i)
        }
        if (n % 2 == 1) {
            sum -= mat(n / 2)(n / 2)
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let n = mat.len();
        let mut ans: i32 = 0;
        for i in 0..n {
            ans += mat[i][i];
            ans += mat[n - 1 - i][i];
        }
        if n % 2 == 1 {
            let mid = n / 2;
            ans -= mat[mid][mid];
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (diagonal-sum mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length mat))
         (total
          (for/fold ([s 0]) ([i (in-range n)])
            (+ s
               (list-ref (list-ref mat i) i)
               (list-ref (list-ref mat (- n 1 i)) i)))))
    (if (odd? n)
        (- total (list-ref (list-ref mat (quotient n 2))
                           (quotient n 2)))
        total)))
```

## Erlang

```erlang
-spec diagonal_sum(Mat :: [[integer()]]) -> integer().
diagonal_sum(Mat) ->
    N = length(Mat),
    Sum = diag_sum(Mat, N, 0, 0),
    case N rem 2 of
        1 ->
            MidIdx = N div 2,
            MidVal = lists:nth(MidIdx + 1, lists:nth(MidIdx + 1, Mat)),
            Sum - MidVal;
        _ -> Sum
    end.

diag_sum(_Mat, N, I, Acc) when I >= N ->
    Acc;
diag_sum(Mat, N, I, Acc) ->
    RowPrimary = lists:nth(I + 1, Mat),
    Primary = lists:nth(I + 1, RowPrimary),

    RowSecIdx = N - I,
    RowSecondary = lists:nth(RowSecIdx, Mat),
    Secondary = lists:nth(I + 1, RowSecondary),

    diag_sum(Mat, N, I + 1, Acc + Primary + Secondary).
```

## Elixir

```elixir
defmodule Solution do
  @spec diagonal_sum(mat :: [[integer]]) :: integer
  def diagonal_sum(mat) do
    n = length(mat)

    sum =
      0..(n - 1)
      |> Enum.reduce(0, fn i, acc ->
        primary = mat |> Enum.at(i) |> Enum.at(i)
        secondary = mat |> Enum.at(n - 1 - i) |> Enum.at(i)
        acc + primary + secondary
      end)

    if rem(n, 2) == 1 do
      mid = div(n, 2)
      sum - (mat |> Enum.at(mid) |> Enum.at(mid))
    else
      sum
    end
  end
end
```
