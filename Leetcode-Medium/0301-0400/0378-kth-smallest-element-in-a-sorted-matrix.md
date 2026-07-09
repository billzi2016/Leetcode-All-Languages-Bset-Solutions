# 0378. Kth Smallest Element in a Sorted Matrix

## Cpp

```cpp
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int lo = matrix[0][0];
        int hi = matrix[n - 1][n - 1];
        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            int cnt = 0;
            int col = n - 1;
            for (int row = 0; row < n; ++row) {
                while (col >= 0 && matrix[row][col] > mid) --col;
                cnt += col + 1;
            }
            if (cnt >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int lo = matrix[0][0];
        int hi = matrix[n - 1][n - 1];
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int count = 0;
            int col = n - 1;
            for (int row = 0; row < n; row++) {
                while (col >= 0 && matrix[row][col] > mid) {
                    col--;
                }
                count += (col + 1);
            }
            if (count < k) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        
        while lo < hi:
            mid = (lo + hi) // 2
            # count how many numbers are <= mid
            cnt = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    cnt += row + 1
                    col += 1
                else:
                    row -= 1
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)

        cnt = 0
        while True:
            val, r, c = heapq.heappop(heap)
            cnt += 1
            if cnt == k:
                return val
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int row;
    int col;
} Node;

static void heapSwap(Node *a, Node *b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(Node *heap, int *size, Node node) {
    int i = (*size)++;
    heap[i] = node;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].val <= heap[i].val) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static Node heapPop(Node *heap, int *size) {
    Node top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1;
        int r = l + 1;
        int smallest = i;
        if (l < *size && heap[l].val < heap[smallest].val) smallest = l;
        if (r < *size && heap[r].val < heap[smallest].val) smallest = r;
        if (smallest == i) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int n = matrixSize;
    int limit = k < n ? k : n;               // we never need more than k rows
    Node *heap = (Node *)malloc(sizeof(Node) * limit);
    int heapSize = 0;

    for (int i = 0; i < limit; ++i) {
        Node node = {matrix[i][0], i, 0};
        heapPush(heap, &heapSize, node);
    }

    Node cur;
    for (int cnt = 0; cnt < k; ++cnt) {
        cur = heapPop(heap, &heapSize);
        int r = cur.row, c = cur.col;
        if (c + 1 < n) {
            Node nxt = {matrix[r][c + 1], r, c + 1};
            heapPush(heap, &heapSize, nxt);
        }
    }

    free(heap);
    return cur.val;
}
```

## Csharp

```csharp
public class Solution {
    public int KthSmallest(int[][] matrix, int k) {
        int n = matrix.Length;
        long lo = matrix[0][0];
        long hi = matrix[n - 1][n - 1];

        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            int count = 0;
            int i = n - 1, j = 0;

            while (i >= 0 && j < n) {
                if ((long)matrix[i][j] <= mid) {
                    count += i + 1;
                    j++;
                } else {
                    i--;
                }
            }

            if (count >= k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        return (int)lo;
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
var kthSmallest = function(matrix, k) {
    const n = matrix.length;
    let lo = matrix[0][0];
    let hi = matrix[n - 1][n - 1];
    
    while (lo < hi) {
        const mid = Math.floor(lo + (hi - lo) / 2);
        // count how many numbers are <= mid
        let cnt = 0;
        let i = n - 1; // start from bottom-left corner
        let j = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] <= mid) {
                cnt += i + 1;
                j++;
            } else {
                i--;
            }
        }
        if (cnt < k) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    
    return lo;
};
```

## Typescript

```typescript
function kthSmallest(matrix: number[][], k: number): number {
    const n = matrix.length;
    type Node = { val: number; r: number; c: number };
    const heap: Node[] = [];

    const swap = (i: number, j: number) => {
        const t = heap[i];
        heap[i] = heap[j];
        heap[j] = t;
    };

    const less = (a: Node, b: Node) => a.val < b.val;

    const push = (node: Node) => {
        heap.push(node);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (!less(heap[i], heap[p])) break;
            swap(i, p);
            i = p;
        }
    };

    const pop = (): Node | undefined => {
        if (heap.length === 0) return undefined;
        const top = heap[0];
        const last = heap.pop()!;
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1,
                    r = i * 2 + 2,
                    smallest = i;
                if (l < heap.length && less(heap[l], heap[smallest])) smallest = l;
                if (r < heap.length && less(heap[r], heap[smallest])) smallest = r;
                if (smallest === i) break;
                swap(i, smallest);
                i = smallest;
            }
        }
        return top;
    };

    // Initialize heap with the first element of each row (up to k rows)
    for (let r = 0; r < Math.min(n, k); ++r) {
        push({ val: matrix[r][0], r, c: 0 });
    }

    let answer = 0;
    for (let i = 0; i < k; ++i) {
        const node = pop()!;
        answer = node.val;
        if (node.c + 1 < n) {
            push({ val: matrix[node.r][node.c + 1], r: node.r, c: node.c + 1 });
        }
    }

    return answer;
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
    function kthSmallest($matrix, $k) {
        $n = count($matrix);
        $pq = new SplPriorityQueue();
        // we want the smallest value to have highest priority (max-heap), so use negative priority
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        for ($i = 0; $i < $n; $i++) {
            $value = $matrix[$i][0];
            $pq->insert([$value, $i, 0], -$value);
        }

        $count = 0;
        while (!$pq->isEmpty()) {
            [$val, $row, $col] = $pq->extract();
            $count++;
            if ($count == $k) {
                return $val;
            }
            if ($col + 1 < $n) {
                $nextVal = $matrix[$row][$col + 1];
                $pq->insert([$nextVal, $row, $col + 1], -$nextVal);
            }
        }

        // Should never reach here because k is always valid
        return null;
    }
}
```

## Swift

```swift
class Solution {
    func kthSmallest(_ matrix: [[Int]], _ k: Int) -> Int {
        let n = matrix.count
        var low = matrix[0][0]
        var high = matrix[n - 1][n - 1]
        
        func countLessEqual(_ target: Int) -> Int {
            var cnt = 0
            for row in matrix {
                var l = 0, r = row.count
                while l < r {
                    let m = (l + r) >> 1
                    if row[m] <= target {
                        l = m + 1
                    } else {
                        r = m
                    }
                }
                cnt += l
            }
            return cnt
        }
        
        while low < high {
            let mid = low + (high - low) / 2
            let cnt = countLessEqual(mid)
            if cnt < k {
                low = mid + 1
            } else {
                high = mid
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthSmallest(matrix: Array<IntArray>, k: Int): Int {
        val n = matrix.size
        var lo = matrix[0][0].toLong()
        var hi = matrix[n - 1][n - 1].toLong()
        while (lo < hi) {
            val mid = lo + (hi - lo) / 2
            var count = 0
            var col = n - 1
            for (row in 0 until n) {
                while (col >= 0 && matrix[row][col].toLong() > mid) {
                    col--
                }
                count += col + 1
            }
            if (count < k) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int kthSmallest(List<List<int>> matrix, int k) {
    int n = matrix.length;
    int low = matrix[0][0];
    int high = matrix[n - 1][n - 1];
    while (low < high) {
      int mid = low + ((high - low) >> 1);
      int cnt = _countLessEqual(matrix, mid);
      if (cnt < k) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }
    return low;
  }

  int _countLessEqual(List<List<int>> matrix, int target) {
    int n = matrix.length;
    int count = 0;
    int i = n - 1;
    int j = 0;
    while (i >= 0 && j < n) {
      if (matrix[i][j] <= target) {
        count += i + 1;
        j++;
      } else {
        i--;
      }
    }
    return count;
  }
}
```

## Golang

```go
func kthSmallest(matrix [][]int, k int) int {
    n := len(matrix)
    low, high := matrix[0][0], matrix[n-1][n-1]
    for low < high {
        mid := low + (high-low)/2
        // count elements <= mid
        cnt := 0
        row, col := n-1, 0
        for row >= 0 && col < n {
            if matrix[row][col] <= mid {
                cnt += row + 1
                col++
            } else {
                row--
            }
        }
        if cnt < k {
            low = mid + 1
        } else {
            high = mid
        }
    }
    return low
}
```

## Ruby

```ruby
def kth_smallest(matrix, k)
  n = matrix.size
  left = matrix[0][0]
  right = matrix[n - 1][n - 1]

  while left < right
    mid = (left + right) / 2
    count = 0
    i = n - 1
    j = 0
    while i >= 0 && j < n
      if matrix[i][j] <= mid
        count += i + 1
        j += 1
      else
        i -= 1
      end
    end

    if count < k
      left = mid + 1
    else
      right = mid
    end
  end

  left
end
```

## Scala

```scala
object Solution {
    def kthSmallest(matrix: Array[Array[Int]], k: Int): Int = {
        val n = matrix.length
        var low = matrix(0)(0).toLong
        var high = matrix(n - 1)(n - 1).toLong

        while (low < high) {
            val mid = low + (high - low) / 2
            var count = 0
            var i = n - 1
            var j = 0
            while (i >= 0 && j < n) {
                if (matrix(i)(j).toLong <= mid) {
                    count += i + 1
                    j += 1
                } else {
                    i -= 1
                }
            }
            if (count < k) low = mid + 1
            else high = mid
        }
        low.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_smallest(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = matrix.len();
        let mut lo = matrix[0][0] as i64;
        let mut hi = matrix[n - 1][n - 1] as i64;

        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            let mut cnt: usize = 0;
            for row in &matrix {
                // upper bound: first element > mid
                let mut l = 0usize;
                let mut r = row.len();
                while l < r {
                    let m = (l + r) / 2;
                    if row[m] as i64 <= mid {
                        l = m + 1;
                    } else {
                        r = m;
                    }
                }
                cnt += l;
            }

            if cnt < k as usize {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        lo as i32
    }
}
```

## Racket

```racket
(define/contract (kth-smallest matrix k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (length matrix))
         (low (list-ref (first matrix) 0))
         (high (list-ref (list-ref matrix (- n 1)) (- n 1))))
    (let loop ((lo low) (hi high))
      (if (= lo hi)
          lo
          (let* ((mid (quotient (+ lo hi) 2))
                 (cnt (let count ((row (- n 1)) (col 0) (c 0))
                        (cond [(or (< row 0) (>= col n)) c]
                              [(<= (list-ref (list-ref matrix row) col) mid)
                               (count row (+ col 1) (+ c (+ row 1)))]
                              [else
                               (count (- row 1) col c)]))))
            (if (>= cnt k)
                (loop lo mid)
                (loop (+ mid 1) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([kth_smallest/2]).

-spec kth_smallest(Matrix :: [[integer()]], K :: integer()) -> integer().
kth_smallest(Matrix, K) ->
    Rows = [list_to_tuple(Row) || Row <- Matrix],
    RowsT = list_to_tuple(Rows),
    N = tuple_size(RowsT),
    FirstRow = element(1, RowsT),
    Low0 = element(1, FirstRow),
    LastRow = element(N, RowsT),
    High0 = element(N, LastRow),
    binary_search(RowsT, N, K, Low0, High0).

binary_search(_RowsT, _N, _K, Low, High) when Low >= High ->
    Low;
binary_search(RowsT, N, K, Low, High) ->
    Mid = (Low + High) div 2,
    Count = count_leq(RowsT, N, Mid),
    if
        Count < K ->
            binary_search(RowsT, N, K, Mid + 1, High);
        true ->
            binary_search(RowsT, N, K, Low, Mid)
    end.

count_leq(RowsT, N, Mid) ->
    count_leq_loop(RowsT, N, N - 1, 0, Mid, 0).

count_leq_loop(_RowsT, _N, I, J, _Mid, Acc) when I < 0; J >= _N ->
    Acc;
count_leq_loop(RowsT, N, I, J, Mid, Acc) ->
    Row = element(I + 1, RowsT),
    Val = element(J + 1, Row),
    if
        Val =< Mid ->
            count_leq_loop(RowsT, N, I, J + 1, Mid, Acc + I + 1);
        true ->
            count_leq_loop(RowsT, N, I - 1, J, Mid, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_smallest(matrix :: [[integer]], k :: integer) :: integer
  def kth_smallest(matrix, k) do
    rows = Enum.map(matrix, &List.to_tuple/1)
    n = length(rows)

    low = elem(hd(rows), 0)
    high = elem(List.last(rows), n - 1)

    find_kth(low, high, rows, k)
  end

  defp find_kth(low, high, _rows, _k) when low == high, do: low
  defp find_kth(low, high, rows, k) do
    mid = div(low + high, 2)
    cnt = count_less_equal(rows, mid)

    if cnt < k do
      find_kth(mid + 1, high, rows, k)
    else
      find_kth(low, mid, rows, k)
    end
  end

  defp count_less_equal(rows, target) do
    n = length(rows)
    do_count(rows, target, n - 1, 0, 0)
  end

  defp do_count(_rows, _target, row, col, acc) when row < 0 or col >= length(_rows), do: acc

  defp do_count(rows, target, row, col, acc) do
    val = elem(Enum.at(rows, row), col)

    if val <= target do
      do_count(rows, target, row, col + 1, acc + row + 1)
    else
      do_count(rows, target, row - 1, col, acc)
    end
  end
end
```
