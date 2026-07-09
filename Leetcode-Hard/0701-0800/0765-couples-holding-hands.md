# 0765. Couples Holding Hands

## Cpp

```cpp
class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int m = row.size();
        vector<int> pos(2 * (m / 2));
        for (int i = 0; i < m; ++i) pos[row[i]] = i;
        int swaps = 0;
        for (int i = 0; i < m; i += 2) {
            int first = row[i];
            int partner = (first % 2 == 0) ? first + 1 : first - 1;
            if (row[i + 1] == partner) continue;
            int idxPartner = pos[partner];
            // swap row[i+1] with row[idxPartner]
            int other = row[i + 1];
            row[i + 1] = partner;
            row[idxPartner] = other;
            pos[other] = idxPartner;
            ++swaps;
        }
        return swaps;
    }
};
```

## Java

```java
class Solution {
    public int minSwapsCouples(int[] row) {
        int n = row.length;
        // position of each person
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) {
            pos[row[i]] = i;
        }
        int swaps = 0;
        for (int i = 0; i < n; i += 2) {
            int first = row[i];
            int partner = first ^ 1; // the correct partner
            if (row[i + 1] == partner) continue; // already a couple
            // index where the partner currently sits
            int partnerIdx = pos[partner];
            // swap row[i+1] with row[partnerIdx]
            int second = row[i + 1];
            row[i + 1] = partner;
            row[partnerIdx] = second;
            // update positions in map
            pos[second] = partnerIdx;
            pos[partner] = i + 1;
            swaps++;
        }
        return swaps;
    }
}
```

## Python

```python
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        n = len(row)
        for i in range(0, n, 2):
            first = row[i]
            partner = first ^ 1
            if row[i + 1] != partner:
                j = pos[partner]
                # swap the person at i+1 with partner at j
                other = row[i + 1]
                row[i + 1], row[j] = row[j], row[i + 1]
                # update positions in map
                pos[other] = j
                pos[partner] = i + 1
                swaps += 1
        return swaps
```

## Python3

```python
from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        n = len(row)
        for i in range(0, n, 2):
            a = row[i]
            b = row[i + 1]
            if a // 2 == b // 2:
                continue
            partner = a ^ 1
            idx = pos[partner]
            # swap b with partner
            row[i + 1], row[idx] = row[idx], row[i + 1]
            # update positions
            pos[row[idx]] = idx
            pos[row[i + 1]] = i + 1
            swaps += 1
        return swaps
```

## C

```c
static int find(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unite(int *parent, int *rank, int a, int b) {
    int ra = find(parent, a);
    int rb = find(parent, b);
    if (ra == rb) return;
    if (rank[ra] < rank[rb]) {
        parent[ra] = rb;
    } else if (rank[ra] > rank[rb]) {
        parent[rb] = ra;
    } else {
        parent[rb] = ra;
        rank[ra]++;
    }
}

int minSwapsCouples(int* row, int rowSize) {
    int n = rowSize / 2; // number of couples / couches
    int *parent = (int *)malloc(n * sizeof(int));
    int *rank = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    for (int i = 0; i < rowSize; i += 2) {
        int a = row[i];
        int b = row[i + 1];
        unite(parent, rank, a / 2, b / 2);
    }

    int components = 0;
    for (int i = 0; i < n; ++i) {
        if (parent[i] == i) components++;
    }

    free(parent);
    free(rank);
    return n - components;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSwapsCouples(int[] row) {
        int m = row.Length;
        int[] pos = new int[m];
        for (int i = 0; i < m; i++) {
            pos[row[i]] = i;
        }
        int swaps = 0;
        for (int i = 0; i < m; i += 2) {
            int first = row[i];
            int partner = first ^ 1; // partner ID
            if (row[i + 1] == partner) continue;
            int partnerIdx = pos[partner];

            // swap row[i+1] with row[partnerIdx]
            int second = row[i + 1];
            row[i + 1] = partner;
            row[partnerIdx] = second;

            // update positions
            pos[second] = partnerIdx;
            pos[partner] = i + 1;

            swaps++;
        }
        return swaps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} row
 * @return {number}
 */
var minSwapsCouples = function(row) {
    const pos = new Array(row.length);
    for (let i = 0; i < row.length; ++i) {
        pos[row[i]] = i;
    }
    let swaps = 0;
    for (let i = 0; i < row.length; i += 2) {
        const first = row[i];
        const partner = first ^ 1; // partner ID
        if (row[i + 1] !== partner) {
            const partnerIdx = pos[partner];
            
            // swap row[i+1] with row[partnerIdx]
            const second = row[i + 1];
            row[i + 1] = partner;
            row[partnerIdx] = second;
            
            // update positions
            pos[second] = partnerIdx;
            pos[partner] = i + 1;
            
            swaps++;
        }
    }
    return swaps;
};
```

## Typescript

```typescript
function minSwapsCouples(row: number[]): number {
    const n = row.length >> 1; // number of couples / seats pairs
    class DSU {
        parent: number[];
        rank: number[];
        constructor(size: number) {
            this.parent = new Array(size);
            this.rank = new Array(size).fill(0);
            for (let i = 0; i < size; i++) this.parent[i] = i;
        }
        find(x: number): number {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }
        union(a: number, b: number): void {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return;
            if (this.rank[ra] < this.rank[rb]) {
                this.parent[ra] = rb;
            } else if (this.rank[ra] > this.rank[rb]) {
                this.parent[rb] = ra;
            } else {
                this.parent[rb] = ra;
                this.rank[ra]++;
            }
        }
    }

    const dsu = new DSU(n);
    for (let i = 0; i < row.length; i += 2) {
        const a = Math.floor(row[i] / 2);
        const b = Math.floor(row[i + 1] / 2);
        dsu.union(a, b);
    }

    const seen = new Set<number>();
    for (let i = 0; i < n; ++i) {
        seen.add(dsu.find(i));
    }
    return n - seen.size;
}
```

## Php

```php
class UnionFind {
    public array $parent;
    public function __construct(int $size) {
        $this->parent = range(0, $size - 1);
    }
    public function find(int $x): int {
        if ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }
    public function union(int $x, int $y): bool {
        $rx = $this->find($x);
        $ry = $this->find($y);
        if ($rx === $ry) {
            return false;
        }
        $this->parent[$rx] = $ry;
        return true;
    }
}

class Solution {

    /**
     * @param Integer[] $row
     * @return Integer
     */
    function minSwapsCouples($row) {
        $n = intdiv(count($row), 2);
        $uf = new UnionFind($n);
        for ($i = 0; $i < count($row); $i += 2) {
            $a = $row[$i];
            $b = $row[$i + 1];
            $ca = intdiv($a, 2);
            $cb = intdiv($b, 2);
            $uf->union($ca, $cb);
        }
        $roots = [];
        for ($i = 0; $i < $n; ++$i) {
            $root = $uf->find($i);
            $roots[$root] = true;
        }
        $components = count($roots);
        return $n - $components;
    }
}
```

## Swift

```swift
class Solution {
    func minSwapsCouples(_ row: [Int]) -> Int {
        var arr = row
        var position = [Int: Int]()
        for (idx, person) in arr.enumerated() {
            position[person] = idx
        }
        
        var swaps = 0
        let total = arr.count
        var i = 0
        while i < total {
            let first = arr[i]
            let second = arr[i + 1]
            let partnerFirst = first ^ 1   // partner of first person
            
            if second != partnerFirst {
                // index where the partner of 'first' is sitting
                if let partnerIdx = position[partnerFirst] {
                    // swap second with partnerFirst
                    let currentSecondPerson = arr[i + 1]
                    
                    // update positions in the map
                    position[currentSecondPerson] = partnerIdx
                    position[partnerFirst] = i + 1
                    
                    arr.swapAt(i + 1, partnerIdx)
                    swaps += 1
                }
            }
            i += 2
        }
        return swaps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwapsCouples(row: IntArray): Int {
        val n = row.size
        val pos = IntArray(n)
        for (i in 0 until n) {
            pos[row[i]] = i
        }
        var swaps = 0
        var i = 0
        while (i < n) {
            val a = row[i]
            val b = row[i + 1]
            val partner = a xor 1
            if (b != partner) {
                swaps++
                val idx = pos[partner]

                // swap b with partner
                row[i + 1] = partner
                row[idx] = b

                // update positions
                pos[b] = idx
                pos[partner] = i + 1
            }
            i += 2
        }
        return swaps
    }
}
```

## Dart

```dart
class Solution {
  int minSwapsCouples(List<int> row) {
    int length = row.length;
    List<int> pos = List.filled(length, 0);
    for (int i = 0; i < length; i++) {
      pos[row[i]] = i;
    }

    int swaps = 0;
    for (int i = 0; i < length; i += 2) {
      int a = row[i];
      int b = row[i + 1];
      int partner = a ^ 1;
      if (b == partner) continue;

      int partnerPos = pos[partner];

      // Update positions in the map
      pos[b] = partnerPos;
      pos[partner] = i + 1;

      // Perform swap in the row
      row[i + 1] = partner;
      row[partnerPos] = b;

      swaps++;
    }
    return swaps;
  }
}
```

## Golang

```go
func minSwapsCouples(row []int) int {
	n := len(row)
	pos := make([]int, n)
	for i, v := range row {
		pos[v] = i
	}
	swaps := 0
	for i := 0; i < n; i += 2 {
		a := row[i]
		b := row[i+1]
		partner := a ^ 1
		if b == partner {
			continue
		}
		j := pos[partner] // index of a's partner
		row[i+1], row[j] = row[j], row[i+1]
		pos[b] = j
		pos[partner] = i + 1
		swaps++
	}
	return swaps
}
```

## Ruby

```ruby
def min_swaps_couples(row)
  n = row.length
  pos = Array.new(n)
  row.each_with_index { |person, idx| pos[person] = idx }

  swaps = 0
  i = 0
  while i < n
    a = row[i]
    b = row[i + 1]
    partner = a ^ 1
    if b != partner
      swaps += 1
      j = pos[partner]

      # swap person at i+1 (b) with partner at position j
      row[j] = b
      pos[b] = j

      row[i + 1] = partner
      pos[partner] = i + 1
    end
    i += 2
  end

  swaps
end
```

## Scala

```scala
object Solution {
    def minSwapsCouples(row: Array[Int]): Int = {
        val m = row.length
        val pos = new Array[Int](m)
        for (i <- 0 until m) {
            pos(row(i)) = i
        }
        var swaps = 0
        var i = 0
        while (i < m) {
            val x = row(i)
            val y = row(i + 1)
            val partner = x ^ 1
            if (y != partner) {
                swaps += 1
                val idx = pos(partner)

                // swap y and partner
                row(i + 1) = partner
                row(idx) = y

                // update positions
                pos(y) = idx
                pos(partner) = i + 1
            }
            i += 2
        }
        swaps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swaps_couples(row: Vec<i32>) -> i32 {
        let n = row.len();
        let mut seats = row.clone();
        let mut pos = vec![0usize; n];
        for (i, &person) in seats.iter().enumerate() {
            pos[person as usize] = i;
        }
        let mut swaps = 0;
        let mut i = 0;
        while i < n {
            let first = seats[i];
            let partner = if first % 2 == 0 { first + 1 } else { first - 1 };
            if seats[i + 1] != partner {
                let partner_idx = pos[partner as usize];
                // swap seats[i+1] and seats[partner_idx]
                let other = seats[i + 1];
                seats[i + 1] = partner;
                seats[partner_idx] = other;
                // update positions
                pos[other as usize] = partner_idx;
                pos[partner as usize] = i + 1;
                swaps += 1;
            }
            i += 2;
        }
        swaps as i32
    }
}
```

## Racket

```racket
(define/contract (min-swaps-couples row)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((row-vec (list->vector row))
         (len (vector-length row-vec))
         (n (/ len 2))
         (parent (make-vector n))
         (rank (make-vector n 0)))
    ;; initialize union‑find
    (for ([i (in-range n)])
      (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x)
              x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    (define (union a b)
      (let ((ra (find a))
            (rb (find b)))
        (when (not (= ra rb))
          (let ((rank-a (vector-ref rank ra))
                (rank-b (vector-ref rank rb)))
            (cond
              [(< rank-a rank-b) (vector-set! parent ra rb)]
              [(> rank-a rank-b) (vector-set! parent rb ra)]
              [else
               (vector-set! parent rb ra)
               (vector-set! rank ra (+ rank-a 1))])))))
    ;; union couples that share a couch
    (for ([i (in-range 0 len 2)])
      (let* ((p1 (vector-ref row-vec i))
             (p2 (vector-ref row-vec (+ i 1)))
             (c1 (quotient p1 2))
             (c2 (quotient p2 2)))
        (union c1 c2)))
    ;; count distinct components
    (let ((seen (make-hash)))
      (for ([i (in-range n)])
        (hash-set! seen (find i) #t))
      (- n (hash-count seen)))))
```

## Erlang

```erlang
-module(solution).
-export([min_swaps_couples/1]).

-spec min_swaps_couples(Row :: [integer()]) -> integer().
min_swaps_couples(Row) ->
    N = length(Row) div 2,
    Parents0 = maps:from_list([{I, I} || I <- lists:seq(0, N - 1)]),
    {_Parents, Swaps} = process(Row, Parents0, 0),
    Swaps.

process([], Parents, Swaps) ->
    {Parents, Swaps};
process([A, B | Rest], Parents, Swaps) ->
    PartnerA = A bxor 1,
    case B == PartnerA of
        true ->
            process(Rest, Parents, Swaps);
        false ->
            Ca = A div 2,
            Cb = B div 2,
            Ra = find(Ca, Parents),
            Rb = find(Cb, Parents),
            if
                Ra == Rb ->
                    process(Rest, Parents, Swaps);
                true ->
                    NewParents = maps:put(Ra, Rb, Parents),
                    process(Rest, NewParents, Swaps + 1)
            end
    end.

find(X, Parents) ->
    case maps:get(X, Parents) of
        X -> X;
        P -> find(P, Parents)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swaps_couples(row :: [integer]) :: integer
  def min_swaps_couples(row) do
    len = length(row)
    n = div(len, 2)

    parent0 =
      Enum.into(0..(n - 1), %{}, fn i -> {i, i} end)

    parent_final =
      Enum.reduce(0..(len - 1), parent0, fn idx, acc ->
        if rem(idx, 2) == 0 do
          a = Enum.at(row, idx)
          b = Enum.at(row, idx + 1)
          ca = div(a, 2)
          cb = div(b, 2)

          {ra, p1} = find(acc, ca)
          {rb, p2} = find(p1, cb)

          if ra != rb do
            Map.put(p2, ra, rb)
          else
            p2
          end
        else
          acc
        end
      end)

    components =
      Enum.reduce(0..(n - 1), MapSet.new(), fn i, set ->
        {root, _} = find(parent_final, i)
        MapSet.put(set, root)
      end)
      |> MapSet.size()

    n - components
  end

  defp find(parent, x) do
    case Map.get(parent, x) do
      ^x -> {x, parent}
      p ->
        {root, updated_parent} = find(parent, p)
        {root, Map.put(updated_parent, x, root)}
    end
  end
end
```
