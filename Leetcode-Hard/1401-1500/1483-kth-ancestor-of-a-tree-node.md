# 1483. Kth Ancestor of a Tree Node

## Cpp

```cpp
class TreeAncestor {
public:
    vector<vector<int>> up;
    int LOG;
    
    TreeAncestor(int n, vector<int>& parent) {
        LOG = 1;
        while ((1 << LOG) <= n) ++LOG;
        up.assign(LOG, vector<int>(n, -1));
        for (int i = 0; i < n; ++i) {
            up[0][i] = parent[i];
        }
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < n; ++i) {
                int prev = up[j-1][i];
                up[j][i] = (prev == -1 ? -1 : up[j-1][prev]);
            }
        }
    }
    
    int getKthAncestor(int node, int k) {
        for (int i = 0; i < LOG && node != -1; ++i) {
            if (k & (1 << i)) {
                node = up[i][node];
            }
        }
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */
```

## Java

```java
class TreeAncestor {
    private final int[][] up;
    private final int LOG;

    public TreeAncestor(int n, int[] parent) {
        int log = 0;
        while ((1 << log) <= n) {
            log++;
        }
        LOG = log;
        up = new int[LOG][n];
        // level 0 (2^0 = 1)
        for (int i = 0; i < n; i++) {
            up[0][i] = parent[i];
        }
        // higher levels
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                int prev = up[j - 1][i];
                up[j][i] = (prev == -1) ? -1 : up[j - 1][prev];
            }
        }
    }

    public int getKthAncestor(int node, int k) {
        for (int j = 0; j < LOG && node != -1; j++) {
            if ((k & (1 << j)) != 0) {
                node = up[j][node];
            }
        }
        return node;
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = new TreeAncestor(n, parent);
 * int param_1 = obj.getKthAncestor(node,k);
 */
```

## Python

```python
class TreeAncestor(object):
    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        self.LOG = (n).bit_length()
        self.up = [[-1] * self.LOG for _ in range(n)]
        for i in range(n):
            self.up[i][0] = parent[i]
        for j in range(1, self.LOG):
            for i in range(n):
                prev = self.up[i][j - 1]
                if prev != -1:
                    self.up[i][j] = self.up[prev][j - 1]

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        i = 0
        while k and node != -1:
            if k & 1:
                node = self.up[node][i]
            k >>= 1
            i += 1
        return node
```

## Python3

```python
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.LOG = 1
        while (1 << self.LOG) <= n:
            self.LOG += 1
        # up[j][i] is the 2^j-th ancestor of node i
        self.up = [[-1] * n for _ in range(self.LOG)]
        self.up[0] = parent[:]
        for j in range(1, self.LOG):
            prev = self.up[j - 1]
            cur = self.up[j]
            for i in range(n):
                anc = prev[i]
                cur[i] = -1 if anc == -1 else prev[anc]

    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0
        while k and node != -1:
            if k & 1:
                node = self.up[bit][node]
            k >>= 1
            bit += 1
        return node if node != -1 else -1
```

## C

```c
#include <stdlib.h>

typedef struct {
    int n;
    int maxLog;
    int **up;
} TreeAncestor;

TreeAncestor* treeAncestorCreate(int n, int* parent, int parentSize) {
    (void)parentSize; // unused
    TreeAncestor *obj = (TreeAncestor*)malloc(sizeof(TreeAncestor));
    obj->n = n;
    int maxLog = 0;
    while ((1 << maxLog) <= n) ++maxLog;
    obj->maxLog = maxLog;

    obj->up = (int**)malloc(maxLog * sizeof(int*));
    for (int i = 0; i < maxLog; ++i) {
        obj->up[i] = (int*)malloc(n * sizeof(int));
    }

    // level 0 (2^0 = 1)
    for (int v = 0; v < n; ++v) {
        obj->up[0][v] = parent[v];
    }
    // higher levels
    for (int j = 1; j < maxLog; ++j) {
        for (int v = 0; v < n; ++v) {
            int mid = obj->up[j - 1][v];
            obj->up[j][v] = (mid == -1) ? -1 : obj->up[j - 1][mid];
        }
    }

    return obj;
}

int treeAncestorGetKthAncestor(TreeAncestor* obj, int node, int k) {
    if (node < 0 || node >= obj->n) return -1;
    for (int j = 0; j < obj->maxLog && node != -1; ++j) {
        if (k & (1 << j)) {
            node = obj->up[j][node];
        }
    }
    return node;
}

void treeAncestorFree(TreeAncestor* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->maxLog; ++i) {
        free(obj->up[i]);
    }
    free(obj->up);
    free(obj);
}

/**
 * Your TreeAncestor struct will be instantiated and called as such:
 * TreeAncestor* obj = treeAncestorCreate(n, parent, parentSize);
 * int param_1 = treeAncestorGetKthAncestor(obj, node, k);
 * 
 * treeAncestorFree(obj);
 */
```

## Csharp

```csharp
public class TreeAncestor
{
    private readonly int[,] up;
    private readonly int LOG;

    public TreeAncestor(int n, int[] parent)
    {
        LOG = 0;
        while ((1 << LOG) <= n) LOG++;
        up = new int[LOG, n];
        for (int v = 0; v < n; v++)
            up[0, v] = parent[v];

        for (int j = 1; j < LOG; j++)
        {
            for (int v = 0; v < n; v++)
            {
                int prev = up[j - 1, v];
                up[j, v] = prev == -1 ? -1 : up[j - 1, prev];
            }
        }
    }

    public int GetKthAncestor(int node, int k)
    {
        for (int i = 0; i < LOG && node != -1; i++)
        {
            if ((k & (1 << i)) != 0)
                node = up[i, node];
        }
        return node;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} parent
 */
var TreeAncestor = function(n, parent) {
    this.LOG = Math.ceil(Math.log2(n + 1));
    this.up = Array.from({ length: this.LOG }, () => new Int32Array(n));
    // 2^0 ancestors (direct parents)
    for (let i = 0; i < n; i++) {
        this.up[0][i] = parent[i];
    }
    // Build binary lifting table
    for (let j = 1; j < this.LOG; j++) {
        const prev = this.up[j - 1];
        const cur = this.up[j];
        for (let i = 0; i < n; i++) {
            const mid = prev[i];
            cur[i] = mid === -1 ? -1 : prev[mid];
        }
    }
};

/**
 * @param {number} node
 * @param {number} k
 * @return {number}
 */
TreeAncestor.prototype.getKthAncestor = function(node, k) {
    let cur = node;
    for (let j = 0; j < this.LOG && cur !== -1; j++) {
        if ((k >> j) & 1) {
            cur = this.up[j][cur];
        }
    }
    return cur === undefined ? -1 : cur;
};
```

## Typescript

```typescript
class TreeAncestor {
    private up: Int32Array[];
    private LOG: number;

    constructor(n: number, parent: number[]) {
        this.LOG = 0;
        while ((1 << this.LOG) <= n) this.LOG++;
        this.up = new Array(this.LOG);
        // level 0 ancestors (direct parents)
        this.up[0] = new Int32Array(parent);
        for (let i = 1; i < this.LOG; i++) {
            const curArr = new Int32Array(n);
            const prevArr = this.up[i - 1];
            for (let v = 0; v < n; v++) {
                const mid = prevArr[v];
                curArr[v] = mid === -1 ? -1 : prevArr[mid];
            }
            this.up[i] = curArr;
        }
    }

    getKthAncestor(node: number, k: number): number {
        let cur = node;
        for (let i = 0; i < this.LOG && cur !== -1; i++) {
            if ((k & (1 << i)) !== 0) {
                cur = this.up[i][cur];
            }
        }
        return cur;
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * var obj = new TreeAncestor(n, parent)
 * var param_1 = obj.getKthAncestor(node,k)
 */
```

## Php

```php
class TreeAncestor {
    private $up;
    private $maxLog;

    /**
     * @param Integer $n
     * @param Integer[] $parent
     */
    function __construct($n, $parent) {
        $this->maxLog = 0;
        while ((1 << $this->maxLog) <= $n) {
            $this->maxLog++;
        }
        // initialize up table with -1
        $this->up = array_fill(0, $n, array_fill(0, $this->maxLog, -1));
        for ($i = 0; $i < $n; $i++) {
            $this->up[$i][0] = $parent[$i];
        }
        for ($j = 1; $j < $this->maxLog; $j++) {
            for ($i = 0; $i < $n; $i++) {
                $prev = $this->up[$i][$j - 1];
                if ($prev != -1) {
                    $this->up[$i][$j] = $this->up[$prev][$j - 1];
                } else {
                    $this->up[$i][$j] = -1;
                }
            }
        }
    }

    /**
     * @param Integer $node
     * @param Integer $k
     * @return Integer
     */
    function getKthAncestor($node, $k) {
        for ($j = 0; $j < $this->maxLog && $node != -1; $j++) {
            if ($k & (1 << $j)) {
                $node = $this->up[$node][$j];
            }
        }
        return $node;
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * $obj = new TreeAncestor($n, $parent);
 * $ret_1 = $obj->getKthAncestor($node, $k);
 */
```

## Swift

```swift
class TreeAncestor {
    private var up: [[Int]]
    private let maxLog: Int

    init(_ n: Int, _ parent: [Int]) {
        var log = 0
        while (1 << log) <= n { log += 1 }
        self.maxLog = log
        self.up = Array(repeating: Array(repeating: -1, count: maxLog), count: n)
        for i in 0..<n {
            up[i][0] = parent[i]
        }
        if maxLog > 1 {
            for j in 1..<maxLog {
                for i in 0..<n {
                    let prev = up[i][j - 1]
                    up[i][j] = (prev != -1) ? up[prev][j - 1] : -1
                }
            }
        }
    }

    func getKthAncestor(_ node: Int, _ k: Int) -> Int {
        var current = node
        var kk = k
        var i = 0
        while kk > 0 && current != -1 {
            if (kk & 1) == 1 {
                current = up[current][i]
            }
            kk >>= 1
            i += 1
        }
        return current
    }
}
```

## Kotlin

```kotlin
class TreeAncestor(n: Int, parent: IntArray) {
    private val LOG: Int
    private val up: Array<IntArray>

    init {
        var log = 0
        while ((1 shl log) <= n) {
            log++
        }
        LOG = log
        up = Array(LOG) { IntArray(n) }
        for (i in 0 until n) {
            up[0][i] = parent[i]
        }
        for (j in 1 until LOG) {
            for (i in 0 until n) {
                val prev = up[j - 1][i]
                up[j][i] = if (prev == -1) -1 else up[j - 1][prev]
            }
        }
    }

    fun getKthAncestor(node: Int, k: Int): Int {
        var cur = node
        var kk = k
        var bit = 0
        while (kk > 0 && cur != -1) {
            if ((kk and 1) == 1) {
                cur = up[bit][cur]
            }
            kk = kk shr 1
            bit++
        }
        return cur
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * var obj = TreeAncestor(n, parent)
 * var param_1 = obj.getKthAncestor(node,k)
 */
```

## Dart

```dart
class TreeAncestor {
  late final List<List<int>> _up;
  final int _log;

  TreeAncestor(int n, List<int> parent) :
        _log = (() {
          int lg = 0;
          while ((1 << lg) <= n) lg++;
          return lg;
        }()) {
    _up = List.generate(_log, (_) => List.filled(n, -1));
    // 2^0 ancestors (direct parents)
    for (int i = 0; i < n; i++) {
      _up[0][i] = parent[i];
    }
    // Build binary lifting table
    for (int j = 1; j < _log; j++) {
      for (int i = 0; i < n; i++) {
        int prev = _up[j - 1][i];
        _up[j][i] = (prev != -1) ? _up[j - 1][prev] : -1;
      }
    }
  }

  int getKthAncestor(int node, int k) {
    for (int j = 0; j < _log && node != -1; j++) {
      if ((k & (1 << j)) != 0) {
        node = _up[j][node];
      }
    }
    return node;
  }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = TreeAncestor(n, parent);
 * int param1 = obj.getKthAncestor(node,k);
 */
```

## Golang

```go
type TreeAncestor struct {
	up [][]int
}

func Constructor(n int, parent []int) TreeAncestor {
	LOG := 0
	for (1 << LOG) <= n {
		LOG++
	}
	up := make([][]int, LOG)
	up[0] = make([]int, n)
	copy(up[0], parent)
	for i := 1; i < LOG; i++ {
		up[i] = make([]int, n)
		for v := 0; v < n; v++ {
			prev := up[i-1][v]
			if prev != -1 {
				up[i][v] = up[i-1][prev]
			} else {
				up[i][v] = -1
			}
		}
	}
	return TreeAncestor{up: up}
}

func (this *TreeAncestor) GetKthAncestor(node int, k int) int {
	for i := 0; i < len(this.up) && node != -1; i++ {
		if k&(1<<i) != 0 {
			node = this.up[i][node]
		}
	}
	return node
}
```

## Ruby

```ruby
class TreeAncestor
  def initialize(n, parent)
    @max_log = 0
    while (1 << @max_log) <= n
      @max_log += 1
    end
    @up = Array.new(@max_log) { Array.new(n, -1) }
    (0...n).each do |i|
      @up[0][i] = parent[i]
    end
    (1...@max_log).each do |j|
      (0...n).each do |i|
        prev = @up[j - 1][i]
        @up[j][i] = prev == -1 ? -1 : @up[j - 1][prev]
      end
    end
  end

  def get_kth_ancestor(node, k)
    cur = node
    bit = 0
    while k > 0 && cur != -1
      if (k & 1) == 1
        cur = @up[bit][cur]
      end
      k >>= 1
      bit += 1
    end
    cur
  end
end
```

## Scala

```scala
class TreeAncestor(_n: Int, _parent: Array[Int]) {
    private val maxLog: Int = (Math.log(_n) / Math.log(2)).toInt + 1
    private val up: Array[Array[Int]] = Array.ofDim[Int](_n, maxLog)

    // initialize the first ancestor (direct parent)
    for (i <- 0 until _n) {
        up(i)(0) = _parent(i)
    }
    // binary lifting table
    for (j <- 1 until maxLog) {
        for (i <- 0 until _n) {
            val prev = up(i)(j - 1)
            up(i)(j) = if (prev != -1) up(prev)(j - 1) else -1
        }
    }

    def getKthAncestor(node: Int, k: Int): Int = {
        var cur = node
        var kk = k
        var j = 0
        while (kk > 0 && cur != -1) {
            if ((kk & 1) == 1) {
                cur = up(cur)(j)
            }
            kk >>= 1
            j += 1
        }
        cur
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * val obj = new TreeAncestor(n, parent)
 * val param_1 = obj.getKthAncestor(node,k)
 */
```

## Rust

```rust
struct TreeAncestor {
    up: Vec<Vec<i32>>,
}

impl TreeAncestor {
    fn new(n: i32, parent: Vec<i32>) -> Self {
        let n_usize = n as usize;
        // find smallest power of two greater than n
        let mut max_log = 1usize;
        while (1usize << max_log) <= n_usize {
            max_log += 1;
        }
        let mut up = vec![vec![-1; max_log]; n_usize];
        for i in 0..n_usize {
            up[i][0] = parent[i];
        }
        for j in 1..max_log {
            for i in 0..n_usize {
                let prev = up[i][j - 1];
                if prev != -1 {
                    up[i][j] = up[prev as usize][j - 1];
                } else {
                    up[i][j] = -1;
                }
            }
        }
        TreeAncestor { up }
    }

    fn get_kth_ancestor(&self, node: i32, k: i32) -> i32 {
        let mut cur = node;
        if cur == -1 {
            return -1;
        }
        let mut kk = k as u32;
        let max_log = self.up[0].len();
        let mut i = 0usize;
        while kk > 0 && cur != -1 && i < max_log {
            if (kk & 1) == 1 {
                cur = self.up[cur as usize][i];
            }
            kk >>= 1;
            i += 1;
        }
        cur
    }
}
```

## Racket

```racket
(define tree-ancestor%
  (class object%
    (super-new)
    (init-field n parent)

    ;; convert parent list to a vector for O(1) access
    (define parent-vec (list->vector parent))

    ;; number of levels needed so that 2^LOG > n
    (define LOG
      (let loop ((cnt 0))
        (if (> (arithmetic-shift 1 cnt) n)
            cnt
            (loop (+ cnt 1)))))

    ;; up[j][i] = 2^j-th ancestor of node i, -1 if none
    (define up
      (let ([tbl (make-vector LOG)])
        ;; allocate each level vector
        (for ([j (in-range LOG)])
          (vector-set! tbl j (make-vector n -1)))
        ;; level 0: direct parent
        (let ([level0 (vector-ref tbl 0)])
          (for ([i (in-range n)])
            (vector-set! level0 i (vector-ref parent-vec i))))
        ;; higher levels
        (for ([j (in-range 1 LOG)])
          (let* ([prev (vector-ref tbl (- j 1))]
                 [curr (vector-ref tbl j)])
            (for ([i (in-range n)])
              (define mid (vector-ref prev i))
              (if (and (>= mid 0) (< mid n))
                  (vector-set! curr i (vector-ref prev mid))
                  (vector-set! curr i -1)))))
        tbl))

    ;; public method
    (define/public (get-kth-ancestor node k)
      (let loop ((cur node) (rem k) (j 0))
        (cond [(or (= cur -1) (= rem 0)) cur]
              [(>= j LOG) cur] ; no higher jumps available
              [(zero? (bitwise-and rem 1))
               (loop cur (arithmetic-shift rem -1) (+ j 1))]
              [else
               (let ([next (vector-ref (vector-ref up j) cur)])
                 (loop next (arithmetic-shift rem -1) (+ j 1)))])))
    ))
```

## Erlang

```erlang
-spec tree_ancestor_init_(N :: integer(), Parent :: [integer()]) -> any().
tree_ancestor_init_(N, Parent) ->
    % convert parent list to tuple for O(1) access (0‑based index)
    ParentTuple = list_to_tuple(Parent),
    % number of levels needed (including level 0)
    Log = trunc(math:log2(N)) + 1,
    UpList = build_up(Log, N, ParentTuple, []),
    put(tree_ancestor_up, UpList),
    ok.

-spec tree_ancestor_get_kth_ancestor(Node :: integer(), K :: integer()) -> integer().
tree_ancestor_get_kth_ancestor(Node, K) ->
    UpList = get(tree_ancestor_up),
    get_kth(Node, K, UpList).

%% ------------------------------------------------------------------
%% Build binary‑lifting table.
%% UpList is a list where the i‑th element (0‑based) is a tuple
%% representing 2^i ancestors for all nodes.
%% ------------------------------------------------------------------
build_up(0, _N, Prev, Acc) ->
    lists:reverse([Prev | Acc]);
build_up(Levels, N, Prev, Acc) when Levels > 0 ->
    Next = compute_next(Prev, N),
    build_up(Levels - 1, N, Next, [Prev | Acc]).

%% For each node i, up[i][node] = up[i‑1][ up[i‑1][node] ].
compute_next(Prev, N) ->
    List = [
        case element(I + 1, Prev) of
            -1 -> -1;
            Anc ->
                case element(Anc + 1, Prev) of
                    -1 -> -1;
                    A2 -> A2
                end
        end
        || I <- lists:seq(0, N - 1)
    ],
    list_to_tuple(List).

%% ------------------------------------------------------------------
%% Answer a query using the binary‑lifting table.
%% ------------------------------------------------------------------
get_kth(Node, 0, _UpList) ->
    Node;
get_kth(_Node, _K, []) ->
    -1;                     % ran out of levels
get_kth(Node, K, [Level | Rest]) ->
    case K band 1 of
        1 ->
            NewNode = element(Node + 1, Level),
            if
                NewNode == -1 -> -1;
                true -> get_kth(NewNode, K bsr 1, Rest)
            end;
        0 ->
            get_kth(Node, K bsr 1, Rest)
    end.
```

## Elixir

```elixir
defmodule TreeAncestor do
  use Bitwise

  @spec init_(n :: integer, parent :: [integer]) :: any
  def init_(n, parent) do
    max_log = (:math.log2(n) |> Float.floor() |> trunc()) + 1

    case :ets.whereis(:tree_up) do
      :undefined -> :ok
      tid -> :ets.delete(tid)
    end

    :ets.new(:tree_up, [:named_table, :public, read_concurrency: true])
    Process.put(:tree_max_log, max_log)

    # level 0 ancestors (direct parents)
    Enum.each(0..(n - 1), fn i ->
      :ets.insert(:tree_up, {{i, 0}, Enum.at(parent, i)})
    end)

    # binary lifting table
    for j <- 1..(max_log - 1) do
      Enum.each(0..(n - 1), fn i ->
        case :ets.lookup(:tree_up, {i, j - 1}) do
          [{{_, _}, anc}] when anc != -1 ->
            case :ets.lookup(:tree_up, {anc, j - 1}) do
              [{{_, _}, anc2}] -> :ets.insert(:tree_up, {{i, j}, anc2})
              [] -> :ets.insert(:tree_up, {{i, j}, -1})
            end

          _ ->
            :ets.insert(:tree_up, {{i, j}, -1})
        end
      end)
    end
  end

  @spec get_kth_ancestor(node :: integer, k :: integer) :: integer
  def get_kth_ancestor(node, k) do
    max_log = Process.get(:tree_max_log, 0)
    climb(node, k, 0, max_log)
  end

  defp climb(cur, _k, j, max_log) when cur == -1 or j >= max_log, do: cur

  defp climb(cur, k, j, max_log) do
    if (k &&& (1 <<< j)) != 0 do
      case :ets.lookup(:tree_up, {cur, j}) do
        [{{_, _}, anc}] -> climb(anc, k, j + 1, max_log)
        [] -> -1
      end
    else
      climb(cur, k, j + 1, max_log)
    end
  end
end
```
