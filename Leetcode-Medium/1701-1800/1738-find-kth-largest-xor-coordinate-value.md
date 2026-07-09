# 1738. Find Kth Largest XOR Coordinate Value

## Cpp

```cpp
class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> vals;
        vals.reserve(m * n);
        vector<vector<int>> pref(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int x = matrix[i][j];
                if (i > 0) x ^= pref[i - 1][j];
                if (j > 0) x ^= pref[i][j - 1];
                if (i > 0 && j > 0) x ^= pref[i - 1][j - 1];
                pref[i][j] = x;
                vals.push_back(x);
            }
        }
        nth_element(vals.begin(), vals.begin() + k - 1, vals.end(), greater<int>());
        return vals[k - 1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int kthLargestValue(int[][] matrix, int k) {
        int m = matrix.length;
        int n = matrix[0].length;
        int total = m * n;
        int[] vals = new int[total];
        int[][] pref = new int[m][n];
        int idx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int xor = matrix[i][j];
                if (i > 0) xor ^= pref[i - 1][j];
                if (j > 0) xor ^= pref[i][j - 1];
                if (i > 0 && j > 0) xor ^= pref[i - 1][j - 1];
                pref[i][j] = xor;
                vals[idx++] = xor;
            }
        }
        Arrays.sort(vals);
        return vals[total - k];
    }
}
```

## Python

```python
class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        m, n = len(matrix), len(matrix[0])
        pref = [[0] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                if i:
                    val ^= pref[i - 1][j]
                if j:
                    val ^= pref[i][j - 1]
                if i and j:
                    val ^= pref[i - 1][j - 1]
                pref[i][j] = val
                if len(heap) < k:
                    heapq.heappush(heap, val)
                else:
                    if val > heap[0]:
                        heapq.heapreplace(heap, val)
        return heap[0]
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pref = [[0] * n for _ in range(m)]
        vals = []
        for i in range(m):
            for j in range(n):
                x = matrix[i][j]
                if i > 0:
                    x ^= pref[i - 1][j]
                if j > 0:
                    x ^= pref[i][j - 1]
                if i > 0 and j > 0:
                    x ^= pref[i - 1][j - 1]
                pref[i][j] = x
                vals.append(x)
        return heapq.nlargest(k, vals)[-1]
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return bi - ai;  // descending order
}

int kthLargestValue(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int m = matrixSize;
    if (m == 0) return 0;
    int n = matrixColSize[0];
    int total = m * n;

    int *vals = (int *)malloc(total * sizeof(int));
    if (!vals) return 0; // allocation failure guard

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int cur = matrix[i][j];
            if (i > 0) cur ^= vals[(i - 1) * n + j];
            if (j > 0) cur ^= vals[i * n + (j - 1)];
            if (i > 0 && j > 0) cur ^= vals[(i - 1) * n + (j - 1)];
            vals[i * n + j] = cur;
        }
    }

    qsort(vals, total, sizeof(int), cmp_desc);
    int ans = vals[k - 1];
    free(vals);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int KthLargestValue(int[][] matrix, int k) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[,] pref = new int[m, n];
        int total = m * n;
        int[] vals = new int[total];
        int idx = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int cur = matrix[i][j];
                if (i > 0) cur ^= pref[i - 1, j];
                if (j > 0) cur ^= pref[i, j - 1];
                if (i > 0 && j > 0) cur ^= pref[i - 1, j - 1];
                pref[i, j] = cur;
                vals[idx++] = cur;
            }
        }

        Array.Sort(vals); // ascending
        return vals[total - k]; // kth largest
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthLargestValue = function(matrix, k) {
    const m = matrix.length;
    const n = matrix[0].length;
    const pref = Array.from({ length: m }, () => new Uint32Array(n));
    const total = m * n;
    const vals = new Uint32Array(total);
    let idx = 0;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const up = i > 0 ? pref[i - 1][j] : 0;
            const left = j > 0 ? pref[i][j - 1] : 0;
            const diag = (i > 0 && j > 0) ? pref[i - 1][j - 1] : 0;
            const cur = up ^ left ^ diag ^ matrix[i][j];
            pref[i][j] = cur;
            vals[idx++] = cur;
        }
    }

    // Convert Uint32Array to regular array for sorting with comparator
    const arr = Array.from(vals);
    arr.sort((a, b) => b - a);
    return arr[k - 1];
};
```

## Typescript

```typescript
function kthLargestValue(matrix: number[][], k: number): number {
    const m = matrix.length;
    const n = matrix[0].length;
    const pref: Uint32Array[] = new Array(m);
    for (let i = 0; i < m; i++) pref[i] = new Uint32Array(n);
    const total = m * n;
    const vals = new Array<number>(total);
    let idx = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let v = matrix[i][j];
            if (i > 0) v ^= pref[i - 1][j];
            if (j > 0) v ^= pref[i][j - 1];
            if (i > 0 && j > 0) v ^= pref[i - 1][j - 1];
            pref[i][j] = v;
            vals[idx++] = v;
        }
    }

    const target = k - 1; // index in descending order

    function swap(arr: number[], i: number, j: number): void {
        const tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    function partition(arr: number[], left: number, right: number, pivotIdx: number): number {
        const pivotVal = arr[pivotIdx];
        swap(arr, pivotIdx, right);
        let store = left;
        for (let i = left; i < right; i++) {
            if (arr[i] > pivotVal) { // larger values to the left
                swap(arr, store, i);
                store++;
            }
        }
        swap(arr, store, right);
        return store;
    }

    function quickSelect(arr: number[], left: number, right: number, kIdx: number): number {
        while (true) {
            if (left === right) return arr[left];
            let pivotIdx = Math.floor((left + right) / 2);
            pivotIdx = partition(arr, left, right, pivotIdx);
            if (kIdx === pivotIdx) return arr[kIdx];
            else if (kIdx < pivotIdx) right = pivotIdx - 1;
            else left = pivotIdx + 1;
        }
    }

    return quickSelect(vals, 0, total - 1, target);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function kthLargestValue($matrix, $k) {
        $m = count($matrix);
        $n = count($matrix[0]);
        // Initialize prefix xor matrix
        $pref = array_fill(0, $m, array_fill(0, $n, 0));
        $vals = [];

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $xor = $matrix[$i][$j];
                if ($i > 0) {
                    $xor ^= $pref[$i - 1][$j];
                }
                if ($j > 0) {
                    $xor ^= $pref[$i][$j - 1];
                }
                if ($i > 0 && $j > 0) {
                    $xor ^= $pref[$i - 1][$j - 1];
                }
                $pref[$i][$j] = $xor;
                $vals[] = $xor;
            }
        }

        rsort($vals);
        return $vals[$k - 1];
    }
}
```

## Swift

```swift
class Solution {
    func kthLargestValue(_ matrix: [[Int]], _ k: Int) -> Int {
        let m = matrix.count
        guard m > 0 else { return 0 }
        let n = matrix[0].count
        
        var pref = Array(repeating: Array(repeating: 0, count: n), count: m)
        var values = [Int]()
        values.reserveCapacity(m * n)
        
        for i in 0..<m {
            for j in 0..<n {
                var x = matrix[i][j]
                if i > 0 { x ^= pref[i - 1][j] }
                if j > 0 { x ^= pref[i][j - 1] }
                if i > 0 && j > 0 { x ^= pref[i - 1][j - 1] }
                pref[i][j] = x
                values.append(x)
            }
        }
        
        values.sort(by: >)
        return values[k - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthLargestValue(matrix: Array<IntArray>, k: Int): Int {
        val m = matrix.size
        val n = matrix[0].size
        val pref = Array(m) { IntArray(n) }
        val total = m * n
        val vals = IntArray(total)
        var idx = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                var cur = matrix[i][j]
                if (i > 0) cur = cur xor pref[i - 1][j]
                if (j > 0) cur = cur xor pref[i][j - 1]
                if (i > 0 && j > 0) cur = cur xor pref[i - 1][j - 1]
                pref[i][j] = cur
                vals[idx++] = cur
            }
        }
        java.util.Arrays.sort(vals)
        return vals[total - k]
    }
}
```

## Dart

```dart
class Solution {
  int kthLargestValue(List<List<int>> matrix, int k) {
    int m = matrix.length;
    int n = matrix[0].length;
    List<int> vals = List.filled(m * n, 0);
    int idx = 0;

    List<List<int>> pref = List.generate(m, (_) => List.filled(n, 0));

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int v = matrix[i][j];
        if (i > 0) v ^= pref[i - 1][j];
        if (j > 0) v ^= pref[i][j - 1];
        if (i > 0 && j > 0) v ^= pref[i - 1][j - 1];
        pref[i][j] = v;
        vals[idx++] = v;
      }
    }

    vals.sort((a, b) => b.compareTo(a));
    return vals[k - 1];
  }
}
```

## Golang

```go
func kthLargestValue(matrix [][]int, k int) int {
    m := len(matrix)
    n := len(matrix[0])
    pref := make([][]int, m)
    for i := 0; i < m; i++ {
        pref[i] = make([]int, n)
    }
    vals := make([]int, 0, m*n)

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            cur := matrix[i][j]
            if i > 0 {
                cur ^= pref[i-1][j]
            }
            if j > 0 {
                cur ^= pref[i][j-1]
            }
            if i > 0 && j > 0 {
                cur ^= pref[i-1][j-1]
            }
            pref[i][j] = cur
            vals = append(vals, cur)
        }
    }

    sort.Slice(vals, func(a, b int) bool { return vals[a] > vals[b] })
    return vals[k-1]
}
```

## Ruby

```ruby
def kth_largest_value(matrix, k)
  m = matrix.length
  n = matrix[0].length
  pref = Array.new(m) { Array.new(n, 0) }
  values = []

  (0...m).each do |i|
    row = matrix[i]
    (0...n).each do |j|
      val = row[j]
      val ^= pref[i - 1][j] if i > 0
      val ^= pref[i][j - 1] if j > 0
      val ^= pref[i - 1][j - 1] if i > 0 && j > 0
      pref[i][j] = val
      values << val
    end
  end

  values.sort!
  values[-k]
end
```

## Scala

```scala
object Solution {
    def kthLargestValue(matrix: Array[Array[Int]], k: Int): Int = {
        val m = matrix.length
        val n = matrix(0).length
        val pref = Array.ofDim[Int](m, n)
        val total = m * n
        val vals = new Array[Int](total)
        var idx = 0
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                var cur = matrix(i)(j)
                if (i > 0) cur ^= pref(i - 1)(j)
                if (j > 0) cur ^= pref(i)(j - 1)
                if (i > 0 && j > 0) cur ^= pref(i - 1)(j - 1)
                pref(i)(j) = cur
                vals(idx) = cur
                idx += 1
            }
        }
        java.util.Arrays.sort(vals)
        vals(total - k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_largest_value(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut pref = vec![vec![0i32; n]; m];
        let mut vals = Vec::with_capacity(m * n);
        for i in 0..m {
            for j in 0..n {
                let mut x = matrix[i][j];
                if i > 0 { x ^= pref[i - 1][j]; }
                if j > 0 { x ^= pref[i][j - 1]; }
                if i > 0 && j > 0 { x ^= pref[i - 1][j - 1]; }
                pref[i][j] = x;
                vals.push(x);
            }
        }
        vals.sort_unstable_by(|a, b| b.cmp(a));
        vals[(k as usize) - 1]
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/vector)
(require racket/bitwise)

(define/contract (kth-largest-value matrix k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((m (length matrix))
         (n (if (null? matrix) 0 (length (car matrix))))
         (pref (make-vector m)))
    ;; initialize prefix vectors
    (for ([i (in-range m)])
      (vector-set! pref i (make-vector n 0)))
    (define vals (make-vector (* m n) 0))
    (define idx 0)
    ;; compute prefix xor and collect values
    (for ([i (in-range m)])
      (let ((row (list->vector (list-ref matrix i))))
        (for ([j (in-range n)])
          (define cur (vector-ref row j))
          (define up (if (> i 0) (vector-ref (vector-ref pref (- i 1)) j) 0))
          (define left (if (> j 0) (vector-ref (vector-ref pref i) (- j 1)) 0))
          (define upleft (if (and (> i 0) (> j 0))
                             (vector-ref (vector-ref pref (- i 1)) (- j 1))
                             0))
          (define val (bitwise-xor cur (bitwise-xor up (bitwise-xor left upleft))))
          (vector-set! (vector-ref pref i) j val)
          (vector-set! vals idx val)
          (set! idx (+ idx 1)))))
    ;; sort descending and pick kth largest
    (let ((sorted (sort (vector->list vals) >)))
      (list-ref sorted (- k 1)))))
```

## Erlang

```erlang
-module(solution).
-export([kth_largest_value/2]).

-spec kth_largest_value(Matrix :: [[integer()]], K :: integer()) -> integer().
kth_largest_value(Matrix, K) ->
    case Matrix of
        [] -> 0;
        [FirstRow | _] ->
            N = length(FirstRow),
            InitPrev = list_to_tuple(lists:duplicate(N, 0)),
            Values = process_rows(Matrix, InitPrev, []),
            SortedDesc = lists:reverse(lists:sort(Values)),
            lists:nth(K, SortedDesc)
    end.

%% Process all rows, accumulating prefix XOR values.
-spec process_rows([[integer()]], tuple(), [integer()]) -> [integer()].
process_rows([], _PrevTuple, Acc) ->
    Acc;
process_rows([Row | RestRows], PrevTuple, Acc) ->
    {NewPrev, NewAcc} = process_row(Row, PrevTuple, 0, 0, [], Acc),
    process_rows(RestRows, NewPrev, NewAcc).

%% Process a single row.
-spec process_row([integer()], tuple(), non_neg_integer(),
                  integer(), [integer()], [integer()]) ->
                 {tuple(), [integer()]}.
process_row([], _PrevTuple, _Idx, _LeftPrev, CurrValsRev, OutAcc) ->
    PrevList = lists:reverse(CurrValsRev),
    {list_to_tuple(PrevList), OutAcc};
process_row([Val | Rest], PrevTuple, Idx, LeftPrev, CurrValsRev, OutAcc) ->
    Up = element(Idx + 1, PrevTuple),
    Diag = case Idx of
               0 -> 0;
               _ -> element(Idx, PrevTuple)
           end,
    Curr = Val bxor Up bxor LeftPrev bxor Diag,
    NewOutAcc = [Curr | OutAcc],
    process_row(Rest, PrevTuple, Idx + 1, Curr, [Curr | CurrValsRev], NewOutAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_largest_value(matrix :: [[integer]], k :: integer) :: integer
  def kth_largest_value(matrix, k) do
    require Bitwise

    n = length(List.first(matrix))
    zero_row = List.duplicate(0, n)

    {_, values_rev} =
      Enum.reduce(matrix, {zero_row, []}, fn row_vals, {prev_row, acc_vals} ->
        {cur_row, new_acc} = process(row_vals, prev_row, 0, 0, acc_vals)
        {cur_row, new_acc}
      end)

    vals = Enum.reverse(values_rev)
    sorted = Enum.sort(vals, &>=/1)
    Enum.at(sorted, k - 1)
  end

  defp process([], [], _left, _prev_up, acc), do: {[], acc}

  defp process([val | rest_vals], [up | rest_up], left, prev_up, acc) do
    cur = Bitwise.bxor(val, up) |> Bitwise.bxor(left) |> Bitwise.bxor(prev_up)
    {rest_row, new_acc} = process(rest_vals, rest_up, cur, up, [cur | acc])
    {[cur | rest_row], new_acc}
  end
end
```
