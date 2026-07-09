# 2326. Spiral Matrix IV

## Cpp

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> res(m, vector<int>(n, -1));
        const int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
        int dir = 0;
        int i = 0, j = 0;
        while (head) {
            res[i][j] = head->val;
            head = head->next;
            if (!head) break; // finished filling
            int ni = i + dirs[dir][0];
            int nj = j + dirs[dir][1];
            if (ni < 0 || ni >= m || nj < 0 || nj >= n || res[ni][nj] != -1) {
                dir = (dir + 1) % 4;
                ni = i + dirs[dir][0];
                nj = j + dirs[dir][1];
            }
            i = ni;
            j = nj;
        }
        return res;
    }
};
```

## Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] res = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(res[i], -1);
        }
        // direction vectors: right, down, left, up
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        int r = 0, c = 0, d = 0;
        while (head != null) {
            res[r][c] = head.val;
            head = head.next;
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || res[nr][nc] != -1) {
                d = (d + 1) % 4;
                nr = r + dr[d];
                nc = c + dc[d];
            }
            r = nr;
            c = nc;
        }
        return res;
    }
}
```

## Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # Initialize matrix with -1
        res = [[-1] * n for _ in range(m)]
        # Directions: right, down, left, up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        i = j = 0

        while head:
            res[i][j] = head.val
            head = head.next

            ni = i + dirs[dir_idx][0]
            nj = j + dirs[dir_idx][1]

            # Change direction if next cell is out of bounds or already filled
            if not (0 <= ni < m and 0 <= nj < n) or res[ni][nj] != -1:
                dir_idx = (dir_idx + 1) % 4
                ni = i + dirs[dir_idx][0]
                nj = j + dirs[dir_idx][1]

            i, j = ni, nj

        return res
```

## Python3

```python
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional['ListNode']) -> List[List[int]]:
        # Initialize matrix with -1
        res = [[-1] * n for _ in range(m)]
        # Directions: right, down, left, up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = j = d = 0

        while head:
            res[i][j] = head.val
            head = head.next

            ni, nj = i + dirs[d][0], j + dirs[d][1]
            if not (0 <= ni < m and 0 <= nj < n) or res[ni][nj] != -1:
                d = (d + 1) % 4
                ni, nj = i + dirs[d][0], j + dirs[d][1]

            i, j = ni, nj

        return res
```

## C

```c
#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** spiralMatrix(int m, int n, struct ListNode* head, int* returnSize, int*** returnColumnSizes) {
    // Allocate result matrix
    int **res = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        res[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) {
            res[i][j] = -1;
        }
    }

    // Direction vectors: right, down, left, up
    int dr[4] = {0, 1, 0, -1};
    int dc[4] = {1, 0, -1, 0};

    int r = 0, c = 0, d = 0;
    while (head) {
        res[r][c] = head->val;

        // Compute next position
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n || res[nr][nc] != -1) {
            d = (d + 1) % 4;
            nr = r + dr[d];
            nc = c + dc[d];
        }
        r = nr;
        c = nc;

        head = head->next;
    }

    // Set return sizes
    *returnSize = m;
    int **colSizesPtr = (int **)malloc(sizeof(int *));
    int *colSizes = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) colSizes[i] = n;
    *colSizesPtr = colSizes;
    *returnColumnSizes = colSizesPtr;

    return res;
}
```

## Csharp

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public int[][] SpiralMatrix(int m, int n, ListNode head) {
        int[][] matrix = new int[m][];
        for (int i = 0; i < m; i++) {
            matrix[i] = new int[n];
            for (int j = 0; j < n; j++) {
                matrix[i][j] = -1;
            }
        }

        int[] dr = { 0, 1, 0, -1 };
        int[] dc = { 1, 0, -1, 0 };
        int dir = 0, r = 0, c = 0;

        while (head != null) {
            matrix[r][c] = head.val;
            head = head.next;

            int nr = r + dr[dir];
            int nc = c + dc[dir];

            if (nr < 0 || nr >= m || nc < 0 || nc >= n || matrix[nr][nc] != -1) {
                dir = (dir + 1) % 4;
                nr = r + dr[dir];
                nc = c + dc[dir];
            }

            r = nr;
            c = nc;
        }

        return matrix;
    }
}
```

## Javascript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
var spiralMatrix = function(m, n, head) {
    const res = Array.from({ length: m }, () => Array(n).fill(-1));
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let dirIdx = 0;
    let i = 0, j = 0;

    while (head) {
        res[i][j] = head.val;
        head = head.next;

        let nextI = i + dirs[dirIdx][0];
        let nextJ = j + dirs[dirIdx][1];

        if (
            nextI < 0 || nextI >= m ||
            nextJ < 0 || nextJ >= n ||
            res[nextI][nextJ] !== -1
        ) {
            dirIdx = (dirIdx + 1) % 4;
            nextI = i + dirs[dirIdx][0];
            nextJ = j + dirs[dirIdx][1];
        }

        i = nextI;
        j = nextJ;
    }

    return res;
};
```

## Typescript

```typescript
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function spiralMatrix(m: number, n: number, head: ListNode | null): number[][] {
    const res: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
    const dirs: [number, number][] = [
        [0, 1],   // right
        [1, 0],   // down
        [0, -1],  // left
        [-1, 0]   // up
    ];
    let i = 0, j = 0, d = 0;
    while (head) {
        res[i][j] = head.val;
        head = head.next;
        if (!head) break; // finished filling
        const ni = i + dirs[d][0];
        const nj = j + dirs[d][1];
        if (ni < 0 || ni >= m || nj < 0 || nj >= n || res[ni][nj] !== -1) {
            d = (d + 1) % 4;
        }
        i += dirs[d][0];
        j += dirs[d][1];
    }
    return res;
}
```

## Php

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param ListNode $head
     * @return Integer[][]
     */
    function spiralMatrix($m, $n, $head) {
        // Initialize matrix with -1
        $res = array_fill(0, $m, array_fill(0, $n, -1));
        
        // Direction vectors: right, down, left, up
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $dirIdx = 0;
        $i = 0;
        $j = 0;
        
        while ($head !== null) {
            $res[$i][$j] = $head->val;
            
            // Compute next position
            $ni = $i + $dirs[$dirIdx][0];
            $nj = $j + $dirs[$dirIdx][1];
            
            // If out of bounds or already filled, turn clockwise
            if ($ni < 0 || $ni >= $m || $nj < 0 || $nj >= $n || $res[$ni][$nj] != -1) {
                $dirIdx = ($dirIdx + 1) % 4;
                $ni = $i + $dirs[$dirIdx][0];
                $nj = $j + $dirs[$dirIdx][1];
            }
            
            $i = $ni;
            $j = $nj;
            $head = $head->next;
        }
        
        return $res;
    }
}
```

## Swift

```swift
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func spiralMatrix(_ m: Int, _ n: Int, _ head: ListNode?) -> [[Int]] {
        var matrix = Array(repeating: Array(repeating: -1, count: n), count: m)
        let dr = [0, 1, 0, -1]
        let dc = [1, 0, -1, 0]
        var dir = 0
        var r = 0, c = 0
        var node = head
        
        while let cur = node {
            matrix[r][c] = cur.val
            
            var nr = r + dr[dir]
            var nc = c + dc[dir]
            
            if nr < 0 || nr >= m || nc < 0 || nc >= n || matrix[nr][nc] != -1 {
                dir = (dir + 1) % 4
                nr = r + dr[dir]
                nc = c + dc[dir]
            }
            
            r = nr
            c = nc
            node = cur.next
        }
        
        return matrix
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun spiralMatrix(m: Int, n: Int, head: ListNode?): Array<IntArray> {
        val res = Array(m) { IntArray(n) { -1 } }
        val dirs = arrayOf(
            intArrayOf(0, 1),   // right
            intArrayOf(1, 0),   // down
            intArrayOf(0, -1),  // left
            intArrayOf(-1, 0)   // up
        )
        var dir = 0
        var i = 0
        var j = 0
        var cur = head
        while (cur != null) {
            res[i][j] = cur.`val`
            var ni = i + dirs[dir][0]
            var nj = j + dirs[dir][1]
            if (ni !in 0 until m || nj !in 0 until n || res[ni][nj] != -1) {
                dir = (dir + 1) % 4
                ni = i + dirs[dir][0]
                nj = j + dirs[dir][1]
            }
            i = ni
            j = nj
            cur = cur.next
        }
        return res
    }
}
```

## Dart

```dart
/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  List<List<int>> spiralMatrix(int m, int n, ListNode? head) {
    // Initialize matrix with -1
    List<List<int>> res = List.generate(m, (_) => List.filled(n, -1));

    // Direction vectors: right, down, left, up
    const List<int> dr = [0, 1, 0, -1];
    const List<int> dc = [1, 0, -1, 0];

    int dir = 0; // current direction index
    int i = 0, j = 0;

    while (head != null) {
      res[i][j] = head.val;
      head = head.next;
      if (head == null) break; // no more nodes to place

      int ni = i + dr[dir];
      int nj = j + dc[dir];

      // Change direction if next cell is out of bounds or already filled
      if (ni < 0 || ni >= m || nj < 0 || nj >= n || res[ni][nj] != -1) {
        dir = (dir + 1) % 4;
        ni = i + dr[dir];
        nj = j + dc[dir];
      }

      i = ni;
      j = nj;
    }

    return res;
  }
}
```

## Golang

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func spiralMatrix(m int, n int, head *ListNode) [][]int {
    // Initialize matrix with -1
    res := make([][]int, m)
    for i := 0; i < m; i++ {
        row := make([]int, n)
        for j := 0; j < n; j++ {
            row[j] = -1
        }
        res[i] = row
    }

    // Direction vectors: right, down, left, up
    dr := []int{0, 1, 0, -1}
    dc := []int{1, 0, -1, 0}

    r, c, dir := 0, 0, 0
    for cur := head; cur != nil; cur = cur.Next {
        res[r][c] = cur.Val

        nr := r + dr[dir]
        nc := c + dc[dir]

        // Change direction if next cell is out of bounds or already filled
        if nr < 0 || nr >= m || nc < 0 || nc >= n || res[nr][nc] != -1 {
            dir = (dir + 1) % 4
            nr = r + dr[dir]
            nc = c + dc[dir]
        }

        r, c = nr, nc
    }

    return res
}
```

## Ruby

```ruby
# Definition for singly-linked list.
# class ListNode
#   attr_accessor :val, :next
#   def initialize(val = 0, _next = nil)
#     @val = val
#     @next = _next
#   end
# end

def spiral_matrix(m, n, head)
  # Initialize matrix with -1
  res = Array.new(m) { Array.new(n, -1) }

  # Direction vectors: right, down, left, up
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  dir_idx = 0
  i = 0
  j = 0
  node = head

  while node
    res[i][j] = node.val

    # Compute next position
    ni = i + dirs[dir_idx][0]
    nj = j + dirs[dir_idx][1]

    # Change direction if out of bounds or cell already filled
    if ni < 0 || ni >= m || nj < 0 || nj >= n || res[ni][nj] != -1
      dir_idx = (dir_idx + 1) % 4
      ni = i + dirs[dir_idx][0]
      nj = j + dirs[dir_idx][1]
    end

    i, j = ni, nj
    node = node.next
  end

  res
end
```

## Scala

```scala
/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def spiralMatrix(m: Int, n: Int, head: ListNode): Array[Array[Int]] = {
        val res = Array.ofDim[Int](m, n)
        // fill with -1
        var r = 0
        while (r < m) {
            java.util.Arrays.fill(res(r), -1)
            r += 1
        }

        val dirs = Array((0, 1), (1, 0), (0, -1), (-1, 0))
        var i = 0
        var j = 0
        var d = 0
        var cur = head

        while (cur != null) {
            res(i)(j) = cur.x
            var ni = i + dirs(d)._1
            var nj = j + dirs(d)._2
            if (ni < 0 || ni >= m || nj < 0 || nj >= n || res(ni)(nj) != -1) {
                d = (d + 1) % 4
                ni = i + dirs(d)._1
                nj = j + dirs(d)._2
            }
            i = ni
            j = nj
            cur = cur.next
        }

        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn spiral_matrix(m: i32, n: i32, head: Option<Box<ListNode>>) -> Vec<Vec<i32>> {
        let rows = m as usize;
        let cols = n as usize;
        let mut matrix = vec![vec![-1i32; cols]; rows];
        let dirs: [(isize, isize); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let (mut i, mut j) = (0usize, 0usize);
        let mut dir_idx = 0usize;
        let mut cur = head;

        while let Some(mut node) = cur {
            matrix[i][j] = node.val;
            // determine next position
            let mut ni = i as isize + dirs[dir_idx].0;
            let mut nj = j as isize + dirs[dir_idx].1;
            if ni < 0
                || ni >= rows as isize
                || nj < 0
                || nj >= cols as isize
                || matrix[ni as usize][nj as usize] != -1
            {
                dir_idx = (dir_idx + 1) % 4;
                ni = i as isize + dirs[dir_idx].0;
                nj = j as isize + dirs[dir_idx].1;
            }
            i = ni as usize;
            j = nj as usize;
            cur = node.next.take();
        }

        matrix
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
(struct list-node
  (val next) #:mutable #:transparent)

(define/contract (spiral-matrix m n head)
  (-> exact-integer? exact-integer? (or/c list-node? #f) (listof (listof exact-integer?)))
  (let* ((res (make-vector m))
         (dr '#(0 1 0 -1))   ; row delta: right, down, left, up
         (dc '#(1 0 -1 0)))  ; col delta
    ;; initialize matrix with -1
    (for ([i (in-range m)])
      (vector-set! res i (make-vector n -1)))
    ;; recursive simulation
    (let loop ((i 0) (j 0) (dir 0) (node head))
      (if (not node)
          ;; conversion to list of lists
          (for/list ([r (in-range m)])
            (vector->list (vector-ref res r)))
          (begin
            (vector-set! (vector-ref res i) j (list-node-val node))
            (define nexti (+ i (vector-ref dr dir)))
            (define nextj (+ j (vector-ref dc dir)))
            (define need-turn?
              (or (< nexti 0) (>= nexti m)
                  (< nextj 0) (>= nextj n)
                  (not (= (vector-ref (vector-ref res nexti) nextj) -1))))
            (if need-turn?
                (let* ((new-dir (modulo (+ dir 1) 4))
                       (ni (+ i (vector-ref dr new-dir)))
                       (nj (+ j (vector-ref dc new-dir))))
                  (loop ni nj new-dir (list-node-next node)))
                (loop nexti nextj dir (list-node-next node))))))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec spiral_matrix(M :: integer(), N :: integer(), Head :: #list_node{} | null) -> [[integer()]].
spiral_matrix(M, N, Head) ->
    Size = M * N,
    Flat0 = array:new(Size, {default, -1}),
    FlatFilled = fill(M, N, Flat0, 0, 0, 0, Head),
    to_matrix(FlatFilled, M, N).

-spec fill(integer(), integer(),
          array:array(integer()),
          integer(), integer(), integer(),
          #list_node{} | null) -> array:array(integer()).
fill(_M, _N, Flat, _I, _J, _DirIdx, null) ->
    Flat;
fill(M, N, Flat, I, J, DirIdx,
     #list_node{val = Val, next = Next}) ->
    Index = I * N + J,
    Flat1 = array:set(Index, Val, Flat),
    {Dr, Dc} = direction(DirIdx),
    NI = I + Dr,
    NJ = J + Dc,
    case out_of_bounds(NI, NJ, M, N) of
        true ->
            NewDir = (DirIdx + 1) rem 4,
            {Dr2, Dc2} = direction(NewDir),
            fill(M, N, Flat1, I + Dr2, J + Dc2, NewDir, Next);
        false ->
            NextIdx = NI * N + NJ,
            case array:get(NextIdx, Flat1) of
                -1 ->
                    fill(M, N, Flat1, NI, NJ, DirIdx, Next);
                _ ->
                    NewDir = (DirIdx + 1) rem 4,
                    {Dr2, Dc2} = direction(NewDir),
                    fill(M, N, Flat1, I + Dr2, J + Dc2, NewDir, Next)
            end
    end.

-spec direction(integer()) -> {integer(), integer()}.
direction(0) -> {0, 1};
direction(1) -> {1, 0};
direction(2) -> {0, -1};
direction(3) -> {-1, 0}.

-spec out_of_bounds(integer(), integer(), integer(), integer()) -> boolean().
out_of_bounds(I, J, M, N) ->
    I < 0 orelse I >= M orelse J < 0 orelse J >= N.

-spec to_matrix(array:array(integer()), integer(), integer()) -> [[integer()]].
to_matrix(Flat, M, N) ->
    [ [ array:get(I * N + J, Flat) || J <- lists:seq(0, N - 1) ]
      || I <- lists:seq(0, M - 1) ].
```

## Elixir

```elixir
defmodule Solution do
  @dirs [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]

  @spec spiral_matrix(m :: integer, n :: integer, head :: ListNode.t() | nil) :: [[integer]]
  def spiral_matrix(m, n, head) do
    map = fill_spiral(m, n, 0, 0, 0, head, %{})
    for i <- 0..(m - 1) do
      for j <- 0..(n - 1), do: Map.get(map, {i, j}, -1)
    end
  end

  defp fill_spiral(_m, _n, _i, _j, _d, nil, acc), do: acc

  defp fill_spiral(m, n, i, j, d, %ListNode{val: v, next: nxt}, acc) do
    new_acc = Map.put(acc, {i, j}, v)
    {di, dj} = Enum.at(@dirs, d)
    ni = i + di
    nj = j + dj

    if out_of_bounds?(ni, nj, m, n) or Map.has_key?(new_acc, {ni, nj}) do
      nd = rem(d + 1, 4)
      {ndi, ndj} = Enum.at(@dirs, nd)
      fill_spiral(m, n, i + ndi, j + ndj, nd, nxt, new_acc)
    else
      fill_spiral(m, n, ni, nj, d, nxt, new_acc)
    end
  end

  defp out_of_bounds?(i, j, m, n) do
    i < 0 or i >= m or j < 0 or j >= n
  end
end
```
