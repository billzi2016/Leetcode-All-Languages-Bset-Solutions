# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

## Cpp

```cpp
class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int m = mat.size();
        int n = mat[0].size();
        vector<vector<int>> pref(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                pref[i][j] = mat[i - 1][j - 1] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
            }
        }
        auto can = [&](int k) -> bool {
            if (k == 0) return true;
            for (int i = 0; i + k <= m; ++i) {
                for (int j = 0; j + k <= n; ++j) {
                    int sum = pref[i + k][j + k] - pref[i][j + k] - pref[i + k][j] + pref[i][j];
                    if (sum <= threshold) return true;
                }
            }
            return false;
        };
        int lo = 0, hi = min(m, n);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length;
        int n = mat[0].length;
        long[][] pre = new long[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            long rowSum = 0;
            for (int j = 1; j <= n; j++) {
                rowSum += mat[i - 1][j - 1];
                pre[i][j] = pre[i - 1][j] + rowSum;
            }
        }

        int low = 0, high = Math.min(m, n);
        while (low < high) {
            int mid = (low + high + 1) / 2;
            if (hasValidSquare(pre, m, n, mid, threshold)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private boolean hasValidSquare(long[][] pre, int m, int n, int len, int threshold) {
        for (int i = len; i <= m; i++) {
            for (int j = len; j <= n; j++) {
                long sum = pre[i][j] - pre[i - len][j] - pre[i][j - len] + pre[i - len][j - len];
                if (sum <= threshold) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        # prefix sum with extra row and column
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                pref[i + 1][j + 1] = pref[i][j + 1] + row_sum

        def can(k):
            if k == 0:
                return True
            for i in range(k, m + 1):
                pi = i - k
                for j in range(k, n + 1):
                    pj = j - k
                    total = pref[i][j] - pref[pi][j] - pref[i][pj] + pref[pi][pj]
                    if total <= threshold:
                        return True
            return False

        low, high = 0, min(m, n)
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## Python3

```python
class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # prefix sum matrix
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum

        def can(k: int) -> bool:
            if k == 0:
                return True
            for i in range(m - k + 1):
                ii = i + k
                for j in range(n - k + 1):
                    jj = j + k
                    total = ps[ii][jj] - ps[i][jj] - ps[ii][j] + ps[i][j]
                    if total <= threshold:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stdlib.h>

int maxSideLength(int** mat, int matSize, int* matColSize, int threshold) {
    int m = matSize;
    int n = matColSize[0];
    
    // Prefix sum matrix with extra row and column (size (m+1) x (n+1))
    int **pre = (int **)malloc((m + 1) * sizeof(int *));
    for (int i = 0; i <= m; ++i) {
        pre[i] = (int *)calloc(n + 1, sizeof(int));
    }
    
    // Build prefix sums
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            pre[i][j] = mat[i - 1][j - 1] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1];
        }
    }
    
    // Helper to check if a square of side k exists with sum <= threshold
    int can(int k) {
        for (int i = k; i <= m; ++i) {
            for (int j = k; j <= n; ++j) {
                int sum = pre[i][j] - pre[i - k][j] - pre[i][j - k] + pre[i - k][j - k];
                if (sum <= threshold) return 1;
            }
        }
        return 0;
    }
    
    // Binary search on side length
    int lo = 0, hi = m < n ? m : n;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (can(mid))
            lo = mid;
        else
            hi = mid - 1;
    }
    
    // Free prefix sum matrix
    for (int i = 0; i <= m; ++i) {
        free(pre[i]);
    }
    free(pre);
    
    return lo;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxSideLength(int[][] mat, int threshold)
    {
        int m = mat.Length;
        int n = mat[0].Length;
        long[,] prefix = new long[m + 1, n + 1];

        for (int i = 1; i <= m; i++)
        {
            long rowSum = 0;
            for (int j = 1; j <= n; j++)
            {
                rowSum += mat[i - 1][j - 1];
                prefix[i, j] = prefix[i - 1, j] + rowSum;
            }
        }

        bool CanFind(int k)
        {
            if (k == 0) return true;
            for (int i = k; i <= m; i++)
            {
                for (int j = k; j <= n; j++)
                {
                    long total = prefix[i, j] - prefix[i - k, j] - prefix[i, j - k] + prefix[i - k, j - k];
                    if (total <= threshold) return true;
                }
            }
            return false;
        }

        int low = 0, high = Math.Min(m, n);
        while (low < high)
        {
            int mid = (low + high + 1) / 2;
            if (CanFind(mid))
                low = mid;
            else
                high = mid - 1;
        }
        return low;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} threshold
 * @return {number}
 */
var maxSideLength = function(mat, threshold) {
    const m = mat.length;
    const n = mat[0].length;
    
    // build prefix sum matrix (m+1) x (n+1)
    const pre = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; ++i) {
        let rowSum = 0;
        for (let j = 1; j <= n; ++j) {
            rowSum += mat[i - 1][j - 1];
            pre[i][j] = pre[i - 1][j] + rowSum;
        }
    }
    
    const canFind = (k) => {
        if (k === 0) return true;
        for (let i = k; i <= m; ++i) {
            for (let j = k; j <= n; ++j) {
                const total = pre[i][j] - pre[i - k][j] - pre[i][j - k] + pre[i - k][j - k];
                if (total <= threshold) return true;
            }
        }
        return false;
    };
    
    let low = 0, high = Math.min(m, n);
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canFind(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maxSideLength(mat: number[][], threshold: number): number {
    const m = mat.length;
    const n = mat[0].length;

    // Build prefix sum matrix (m+1) x (n+1)
    const ps: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= m; ++i) {
        let rowSum = 0;
        for (let j = 1; j <= n; ++j) {
            rowSum += mat[i - 1][j - 1];
            ps[i][j] = ps[i - 1][j] + rowSum;
        }
    }

    const canFind = (k: number): boolean => {
        if (k === 0) return true;
        for (let i = k; i <= m; ++i) {
            for (let j = k; j <= n; ++j) {
                const total = ps[i][j] - ps[i - k][j] - ps[i][j - k] + ps[i - k][j - k];
                if (total <= threshold) return true;
            }
        }
        return false;
    };

    let low = 0, high = Math.min(m, n);
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canFind(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $threshold
     * @return Integer
     */
    function maxSideLength($mat, $threshold) {
        $m = count($mat);
        $n = count($mat[0]);
        // build prefix sum matrix (size (m+1) x (n+1))
        $ps = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 1; $i <= $m; ++$i) {
            for ($j = 1; $j <= $n; ++$j) {
                $ps[$i][$j] = $mat[$i - 1][$j - 1]
                    + $ps[$i - 1][$j]
                    + $ps[$i][$j - 1]
                    - $ps[$i - 1][$j - 1];
            }
        }

        // helper to check if any square of side $len has sum <= threshold
        $canFind = function($len) use ($m, $n, $ps, $threshold) {
            if ($len == 0) return true;
            for ($i = 0; $i + $len <= $m; ++$i) {
                $i2 = $i + $len;
                for ($j = 0; $j + $len <= $n; ++$j) {
                    $j2 = $j + $len;
                    $sum = $ps[$i2][$j2] - $ps[$i][$j2] - $ps[$i2][$j] + $ps[$i][$j];
                    if ($sum <= $threshold) {
                        return true;
                    }
                }
            }
            return false;
        };

        $low = 0;
        $high = min($m, $n);
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($canFind($mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func maxSideLength(_ mat: [[Int]], _ threshold: Int) -> Int {
        let m = mat.count
        let n = mat[0].count
        var prefix = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for i in 0..<m {
            var rowSum = 0
            for j in 0..<n {
                rowSum += mat[i][j]
                prefix[i + 1][j + 1] = prefix[i][j + 1] + rowSum
            }
        }
        
        func can(_ k: Int) -> Bool {
            if k == 0 { return true }
            for i in 0...m - k {
                let i2 = i + k
                for j in 0...n - k {
                    let j2 = j + k
                    let total = prefix[i2][j2] - prefix[i][j2] - prefix[i2][j] + prefix[i][j]
                    if total <= threshold { return true }
                }
            }
            return false
        }
        
        var low = 0
        var high = min(m, n)
        while low < high {
            let mid = (low + high + 1) / 2
            if can(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSideLength(mat: Array<IntArray>, threshold: Int): Int {
        val m = mat.size
        val n = mat[0].size
        val pref = Array(m + 1) { LongArray(n + 1) }
        for (i in 0 until m) {
            var rowSum = 0L
            for (j in 0 until n) {
                rowSum += mat[i][j].toLong()
                pref[i + 1][j + 1] = pref[i][j + 1] + rowSum
            }
        }

        fun canFit(k: Int): Boolean {
            if (k == 0) return true
            for (i in 0..m - k) {
                val i2 = i + k
                for (j in 0..n - k) {
                    val j2 = j + k
                    val sum = pref[i2][j2] - pref[i][j2] - pref[i2][j] + pref[i][j]
                    if (sum <= threshold.toLong()) return true
                }
            }
            return false
        }

        var low = 0
        var high = minOf(m, n)
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (canFit(mid)) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
```

## Dart

```dart
class Solution {
  int maxSideLength(List<List<int>> mat, int threshold) {
    int m = mat.length;
    int n = mat[0].length;
    List<List<int>> ps = List.generate(m + 1, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        ps[i + 1][j + 1] = mat[i][j] +
            ps[i][j + 1] +
            ps[i + 1][j] -
            ps[i][j];
      }
    }

    bool can(int k) {
      if (k == 0) return true;
      for (int i = 0; i <= m - k; ++i) {
        for (int j = 0; j <= n - k; ++j) {
          int total = ps[i + k][j + k] -
              ps[i][j + k] -
              ps[i + k][j] +
              ps[i][j];
          if (total <= threshold) return true;
        }
      }
      return false;
    }

    int low = 0, high = m < n ? m : n;
    while (low < high) {
      int mid = ((low + high + 1) >> 1);
      if (can(mid)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func maxSideLength(mat [][]int, threshold int) int {
	m, n := len(mat), len(mat[0])
	// prefix sum matrix with extra row and column
	ps := make([][]int, m+1)
	for i := range ps {
		ps[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		rowSum := 0
		for j := 0; j < n; j++ {
			rowSum += mat[i][j]
			ps[i+1][j+1] = ps[i][j+1] + rowSum
		}
	}

	can := func(k int) bool {
		if k == 0 {
			return true
		}
		for i := 0; i <= m-k; i++ {
			for j := 0; j <= n-k; j++ {
				sum := ps[i+k][j+k] - ps[i][j+k] - ps[i+k][j] + ps[i][j]
				if sum <= threshold {
					return true
				}
			}
		}
		return false
	}

	low, high := 0, m
	if n < high {
		high = n
	}
	for low < high {
		mid := (low + high + 1) / 2
		if can(mid) {
			low = mid
		} else {
			high = mid - 1
		}
	}
	return low
}
```

## Ruby

```ruby
def max_side_length(mat, threshold)
  m = mat.length
  n = mat[0].length
  ps = Array.new(m + 1) { Array.new(n + 1, 0) }
  (0...m).each do |i|
    row_sum = 0
    (0...n).each do |j|
      row_sum += mat[i][j]
      ps[i + 1][j + 1] = ps[i][j + 1] + row_sum
    end
  end

  can_fit = lambda do |k|
    return true if k == 0
    (0..m - k).each do |i|
      (0..n - k).each do |j|
        total = ps[i + k][j + k] - ps[i][j + k] - ps[i + k][j] + ps[i][j]
        return true if total <= threshold
      end
    end
    false
  end

  low = 0
  high = [m, n].min
  while low < high
    mid = (low + high + 1) / 2
    if can_fit.call(mid)
      low = mid
    else
      high = mid - 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
    def maxSideLength(mat: Array[Array[Int]], threshold: Int): Int = {
        val m = mat.length
        val n = mat(0).length
        // prefix sum matrix (m+1) x (n+1)
        val ps = Array.ofDim[Int](m + 1, n + 1)
        for (i <- 0 until m) {
            var rowSum = 0
            for (j <- 0 until n) {
                rowSum += mat(i)(j)
                ps(i + 1)(j + 1) = ps(i)(j + 1) + rowSum
            }
        }

        def can(k: Int): Boolean = {
            if (k == 0) return true
            var i = 0
            while (i <= m - k) {
                var j = 0
                while (j <= n - k) {
                    val sum = ps(i + k)(j + k) - ps(i)(j + k) - ps(i + k)(j) + ps(i)(j)
                    if (sum <= threshold) return true
                    j += 1
                }
                i += 1
            }
            false
        }

        var low = 0
        var high = Math.min(m, n)
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (can(mid)) low = mid else high = mid - 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold: i32) -> i32 {
        let m = mat.len();
        if m == 0 {
            return 0;
        }
        let n = mat[0].len();

        // Prefix sum matrix (m+1) x (n+1)
        let mut ps = vec![vec![0i64; n + 1]; m + 1];
        for i in 0..m {
            for j in 0..n {
                ps[i + 1][j + 1] =
                    mat[i][j] as i64 + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];
            }
        }

        let mut low = 0i32;
        let mut high = std::cmp::min(m, n) as i32;
        let thr = threshold as i64;

        while low < high {
            let mid = (low + high + 1) / 2;
            if Self::can(&ps, m, n, mid as usize, thr) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }

        low
    }

    fn can(ps: &Vec<Vec<i64>>, m: usize, n: usize, len: usize, thr: i64) -> bool {
        if len == 0 {
            return true;
        }
        for i in 0..=m - len {
            let i2 = i + len;
            for j in 0..=n - len {
                let j2 = j + len;
                let sum = ps[i2][j2] - ps[i][j2] - ps[i2][j] + ps[i][j];
                if sum <= thr {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (max-side-length mat threshold)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([m (length mat)]
         [n (if (zero? m) 0 (length (first mat)))]
         [rows-vec (list->vector (map list->vector mat))]
         [ps (make-vector (+ m 1) #f)])
    ;; initialize prefix sum matrix with zeros
    (for ([i (in-range (add1 m))])
      (vector-set! ps i (make-vector (+ n 1) 0)))
    ;; compute prefix sums
    (for ([i (in-range 1 (add1 m))])
      (for ([j (in-range 1 (add1 n))])
        (let* ([val (vector-ref (vector-ref rows-vec (- i 1)) (- j 1))]
               [a   (vector-ref (vector-ref ps (- i 1)) j)]
               [b   (vector-ref (vector-ref ps i)       (- j 1))]
               [c   (vector-ref (vector-ref ps (- i 1)) (- j 1))]
               [sum (+ val a b (- c))])
          (vector-set! (vector-ref ps i) j sum))))
    ;; helper to test if a square of side k fits the threshold
    (define (exists-square k)
      (call/cc
        (lambda (return)
          (for ([i (in-range k (add1 m))])
            (for ([j (in-range k (add1 n))])
              (let* ([a (vector-ref (vector-ref ps i) j)]
                     [b (vector-ref (vector-ref ps (- i k)) j)]
                     [c (vector-ref (vector-ref ps i)       (- j k))]
                     [d (vector-ref (vector-ref ps (- i k)) (- j k))]
                     [total (+ a d (- b c))])
                (when (<= total threshold)
                  (return #t)))))
          #f)))
    ;; binary search for maximum side length
    (let loop ((low 0) (high (min m n)))
      (if (= low high)
          low
          (let* ([mid (quotient (+ low high 1) 2)])
            (if (exists-square mid)
                (loop mid high)
                (loop low (- mid 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_side_length/2]).

-spec max_side_length(Mat :: [[integer()]], Threshold :: integer()) -> integer().
max_side_length(Mat, Threshold) ->
    M = length(Mat),
    [FirstRow|_] = Mat,
    N = length(FirstRow),
    ZeroRow = lists:duplicate(N + 1, 0),
    PS = build_prefix_rows(Mat, ZeroRow, [ZeroRow], N),
    MaxSide = binary_search(1, min(M, N), 0, PS, Threshold),
    MaxSide.

%% Binary search for the largest side length
binary_search(Low, High, Best, _PS, _Threshold) when Low > High ->
    Best;
binary_search(Low, High, Best, PS, Threshold) ->
    Mid = (Low + High) div 2,
    case exists_square_of_size(Mid, PS, Threshold) of
        true -> binary_search(Mid + 1, High, Mid, PS, Threshold);
        false -> binary_search(Low, Mid - 1, Best, PS, Threshold)
    end.

%% Check if any square of side K satisfies the threshold
exists_square_of_size(0, _PS, _Threshold) ->
    true;
exists_square_of_size(K, PS, Threshold) ->
    M = length(PS) - 1,
    N = length(hd(PS)) - 1,
    MaxI = M - K + 1,
    MaxJ = N - K + 1,
    exists_in_grid(1, MaxI, 1, MaxJ, K, PS, Threshold).

exists_in_grid(IStart, IEnd, _JStart, _JEnd, _K, _PS, _Threshold) when IStart > IEnd ->
    false;
exists_in_grid(I, IEnd, JStart, JEnd, K, PS, Threshold) ->
    case exists_in_row(I, JStart, JEnd, K, PS, Threshold) of
        true -> true;
        false -> exists_in_grid(I + 1, IEnd, JStart, JEnd, K, PS, Threshold)
    end.

exists_in_row(_I, JStart, _JEnd, _K, _PS, _Threshold) when JStart > _JEnd ->
    false;
exists_in_row(I, J, JEnd, K, PS, Threshold) ->
    Sum = square_sum(I, J, K, PS),
    if
        Sum =< Threshold -> true;
        true -> exists_in_row(I, J + 1, JEnd, K, PS, Threshold)
    end.

%% Compute sum of KxK square with top-left corner (I,J) using prefix sums
square_sum(I, J, K, PS) ->
    I2 = I + K - 1,
    J2 = J + K - 1,
    A = get_ps(PS, I2, J2),
    B = get_ps(PS, I - 1, J2),
    C = get_ps(PS, I2, J - 1),
    D = get_ps(PS, I - 1, J - 1),
    A - B - C + D.

%% Retrieve prefix sum value at (I,J) where indices start from 0
get_ps(PS, I, J) ->
    Row = lists:nth(I + 1, PS),
    lists:nth(J + 1, Row).

%% Build full prefix sum matrix with an extra leading zero row and column
build_prefix_rows([], _PrevRow, AccRows, _N) ->
    lists:reverse(AccRows);
build_prefix_rows([MatRow|Rest], PrevRow, AccRows, N) ->
    NewRow = build_prefix_row(MatRow, PrevRow),
    build_prefix_rows(Rest, NewRow, [NewRow|AccRows], N).

%% Build a single prefix sum row given the original matrix row and previous prefix row
build_prefix_row(MatVals, PrevRow) ->
    Rev = build_prefix_row_helper(MatVals, PrevRow, 1, []),
    [0 | lists:reverse(Rev)].

build_prefix_row_helper([], _PrevRow, _Idx, AccRev) ->
    AccRev;
build_prefix_row_helper([Val|Rest], PrevRow, Idx, AccRev) ->
    Up = lists:nth(Idx + 1, PrevRow),          % prefix sum from previous row at column Idx
    UpLeft = lists:nth(Idx, PrevRow),         % prefix sum from previous row at column Idx-1
    Left = case AccRev of [] -> 0; [L|_] -> L end,
    Cur = Val + Up + Left - UpLeft,
    build_prefix_row_helper(Rest, PrevRow, Idx + 1, [Cur|AccRev]).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_side_length(mat :: [[integer]], threshold :: integer) :: integer
  def max_side_length(mat, threshold) do
    m = length(mat)
    n = length(List.first(mat))

    # Build prefix sum matrix ps of size (m+1) x (n+1)
    empty_row = List.duplicate(0, n + 1)
    initial_ps = for _ <- 0..m, do: empty_row

    ps =
      Enum.reduce(1..m, initial_ps, fn i, acc ->
        mat_row = Enum.at(mat, i - 1)
        prev_ps_row = Enum.at(acc, i - 1)

        # compute current prefix sum row
        cur_rev =
          Enum.reduce(1..n, [], fn j, rev_acc ->
            val = Enum.at(mat_row, j - 1)
            top = Enum.at(prev_ps_row, j)
            left = if rev_acc == [], do: 0, else: hd(rev_acc)
            top_left = Enum.at(prev_ps_row, j - 1)

            cur = val + top + left - top_left
            [cur | rev_acc]
          end)

        cur_row = [0 | Enum.reverse(cur_rev)]
        List.replace_at(acc, i, cur_row)
      end)

    max_len = min(m, n)

    binary_search(0, max_len, m, n, ps, threshold)
  end

  defp get(ps, i, j), do: ps |> Enum.at(i) |> Enum.at(j)

  defp check(k, m, n, ps, threshold) when k == 0, do: true
  defp check(k, m, n, ps, threshold) do
    max_i = m - k
    max_j = n - k

    Enum.any?(0..max_i, fn i ->
      Enum.any?(0..max_j, fn j ->
        sum =
          get(ps, i + k, j + k)
          - get(ps, i, j + k)
          - get(ps, i + k, j)
          + get(ps, i, j)

        sum <= threshold
      end)
    end)
  end

  defp binary_search(low, high, m, n, ps, threshold) when low < high do
    mid = div(low + high + 1, 2)

    if check(mid, m, n, ps, threshold) do
      binary_search(mid, high, m, n, ps, threshold)
    else
      binary_search(low, mid - 1, m, n, ps, threshold)
    end
  end

  defp binary_search(low, _high, _m, _n, _ps, _threshold), do: low
end
```
