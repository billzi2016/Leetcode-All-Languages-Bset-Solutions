# 2732. Find a Good Subset of the Matrix

## Cpp

```cpp
class Solution {
public:
    vector<int> goodSubsetofBinaryMatrix(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int maxMask = 1 << n;
        vector<int> firstIdx(maxMask, -1);
        for (int i = 0; i < m; ++i) {
            int mask = 0;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) mask |= (1 << j);
            }
            if (mask == 0) return {i};
            // try to find a previous row with disjoint bits
            for (int prevMask = 0; prevMask < maxMask; ++prevMask) {
                if (firstIdx[prevMask] != -1 && (mask & prevMask) == 0) {
                    int a = firstIdx[prevMask];
                    int b = i;
                    if (a > b) swap(a, b);
                    return {a, b};
                }
            }
            // store this mask if not seen before
            if (firstIdx[mask] == -1) firstIdx[mask] = i;
        }
        return {};
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> goodSubsetofBinaryMatrix(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int maxMask = 1 << n;
        int[] firstIdx = new int[maxMask];
        java.util.Arrays.fill(firstIdx, -1);
        
        for (int i = 0; i < m; i++) {
            int mask = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    mask |= 1 << j;
                }
            }
            // subset of size 1: need all zeros
            if (mask == 0) {
                java.util.List<Integer> res = new java.util.ArrayList<>();
                res.add(i);
                return res;
            }
            if (firstIdx[mask] == -1) {
                firstIdx[mask] = i;
            }
        }
        
        for (int a = 0; a < maxMask; a++) {
            if (firstIdx[a] == -1) continue;
            for (int b = a + 1; b < maxMask; b++) {
                if (firstIdx[b] == -1) continue;
                if ((a & b) == 0) {
                    java.util.List<Integer> res = new java.util.ArrayList<>();
                    int idxA = firstIdx[a];
                    int idxB = firstIdx[b];
                    if (idxA < idxB) {
                        res.add(idxA);
                        res.add(idxB);
                    } else {
                        res.add(idxB);
                        res.add(idxA);
                    }
                    return res;
                }
            }
        }
        return new java.util.ArrayList<>();
    }
}
```

## Python

```python
class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        mask_to_idx = {}
        masks_present = []
        for i in range(m):
            mask = 0
            row = grid[i]
            for j in range(n):
                if row[j]:
                    mask |= (1 << j)
            if mask == 0:
                return [i]  # single zero row is a good subset
            if mask not in mask_to_idx:
                mask_to_idx[mask] = i
                masks_present.append(mask)

        # try to find two rows whose bitwise AND is zero
        for i in range(len(masks_present)):
            m1 = masks_present[i]
            idx1 = mask_to_idx[m1]
            for j in range(i + 1, len(masks_present)):
                m2 = masks_present[j]
                if (m1 & m2) == 0:
                    idx2 = mask_to_idx[m2]
                    return [idx1, idx2] if idx1 < idx2 else [idx2, idx1]

        return []
```

## Python3

```python
from typing import List

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        mask_to_idxs = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, val in enumerate(row):
                if val:
                    mask |= 1 << j
            if mask == 0:
                return [i]
            if mask not in mask_to_idxs:
                mask_to_idxs[mask] = []
            if len(mask_to_idxs[mask]) < 2:  # keep at most two indices
                mask_to_idxs[mask].append(i)

        masks = list(mask_to_idxs.keys())
        for i, m1 in enumerate(masks):
            for m2 in masks[i:]:
                if (m1 & m2) == 0:
                    if m1 != m2:
                        return sorted([mask_to_idxs[m1][0], mask_to_idxs[m2][0]])
                    else:
                        if len(mask_to_idxs[m1]) >= 2:
                            return sorted([mask_to_idxs[m1][0], mask_to_idxs[m1][1]])
        return []
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodSubsetofBinaryMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize){
    int n = gridColSize[0];
    int maxMask = 1 << n;
    int *firstIdx = (int*)malloc(maxMask * sizeof(int));
    for (int i = 0; i < maxMask; ++i) firstIdx[i] = -1;

    for (int i = 0; i < gridSize; ++i) {
        int mask = 0;
        for (int j = 0; j < n; ++j) {
            if (grid[i][j]) mask |= (1 << j);
        }
        if (mask == 0) { // single zero row works
            int *res = (int*)malloc(sizeof(int));
            res[0] = i;
            *returnSize = 1;
            free(firstIdx);
            return res;
        }
        if (firstIdx[mask] == -1) firstIdx[mask] = i; // store first occurrence
    }

    for (int a = 1; a < maxMask; ++a) {
        if (firstIdx[a] == -1) continue;
        for (int b = a + 1; b < maxMask; ++b) {
            if (firstIdx[b] == -1) continue;
            if ((a & b) == 0) { // disjoint masks
                int *res = (int*)malloc(2 * sizeof(int));
                res[0] = firstIdx[a];
                res[1] = firstIdx[b];
                *returnSize = 2;
                free(firstIdx);
                return res;
            }
        }
    }

    *returnSize = 0;
    free(firstIdx);
    return NULL;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> GoodSubsetofBinaryMatrix(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int maxMask = 1 << n;
        int[] firstIdx = new int[maxMask];
        for (int i = 0; i < maxMask; i++) firstIdx[i] = -1;

        // Scan rows, compute masks, look for all-zero row
        for (int i = 0; i < m; i++) {
            int mask = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) mask |= 1 << j;
            }
            if (mask == 0) {
                return new List<int> { i };
            }
            if (firstIdx[mask] == -1) {
                firstIdx[mask] = i;
            }
        }

        // Look for two rows with disjoint masks
        for (int a = 0; a < maxMask; a++) {
            if (firstIdx[a] == -1) continue;
            for (int b = a + 1; b < maxMask; b++) {
                if (firstIdx[b] == -1) continue;
                if ((a & b) == 0) {
                    var res = new List<int> { firstIdx[a], firstIdx[b] };
                    res.Sort();
                    return res;
                }
            }
        }

        // No good subset found
        return new List<int>();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var goodSubsetofBinaryMatrix = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const maxMask = 1 << n;
    const firstIdx = new Array(maxMask).fill(-1);
    
    for (let i = 0; i < m; ++i) {
        let mask = 0;
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) mask |= (1 << j);
        }
        if (mask === 0) return [i]; // single all-zero row
        if (firstIdx[mask] === -1) firstIdx[mask] = i;
    }
    
    for (let a = 0; a < maxMask; ++a) {
        if (firstIdx[a] === -1) continue;
        for (let b = a + 1; b < maxMask; ++b) {
            if (firstIdx[b] === -1) continue;
            if ((a & b) === 0) {
                const res = [firstIdx[a], firstIdx[b]];
                res.sort((x, y) => x - y);
                return res;
            }
        }
    }
    
    return [];
};
```

## Typescript

```typescript
function goodSubsetofBinaryMatrix(grid: number[][]): number[] {
    const m = grid.length;
    const n = grid[0].length;
    const maskToIdx = new Map<number, number>();

    for (let i = 0; i < m; i++) {
        let mask = 0;
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                mask |= (1 << j);
            }
        }
        if (mask === 0) return [i];
        if (!maskToIdx.has(mask)) {
            maskToIdx.set(mask, i);
        }
    }

    const masks = Array.from(maskToIdx.keys());
    for (let a = 0; a < masks.length; a++) {
        for (let b = a + 1; b < masks.length; b++) {
            const m1 = masks[a];
            const m2 = masks[b];
            if ((m1 & m2) === 0) {
                const i1 = maskToIdx.get(m1)!;
                const i2 = maskToIdx.get(m2)!;
                return i1 < i2 ? [i1, i2] : [i2, i1];
            }
        }
    }

    return [];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function goodSubsetofBinaryMatrix($grid) {
        $m = count($grid);
        if ($m == 0) return [];
        $n = count($grid[0]);
        $maskToIdx = [];

        // Check for a single all-zero row
        for ($i = 0; $i < $m; $i++) {
            $mask = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1) {
                    $mask |= (1 << $j);
                }
            }
            if ($mask === 0) {
                return [$i];
            }
            // store first occurrence of each mask
            if (!isset($maskToIdx[$mask])) {
                $maskToIdx[$mask] = $i;
            }
        }

        $masks = array_keys($maskToIdx);
        $cnt = count($masks);

        for ($a = 0; $a < $cnt; $a++) {
            for ($b = $a + 1; $b < $cnt; $b++) {
                $maskA = $masks[$a];
                $maskB = $masks[$b];
                if ( ($maskA & $maskB) === 0 ) {
                    $idx1 = $maskToIdx[$maskA];
                    $idx2 = $maskToIdx[$maskB];
                    if ($idx1 > $idx2) {
                        $tmp = $idx1;
                        $idx1 = $idx2;
                        $idx2 = $tmp;
                    }
                    return [$idx1, $idx2];
                }
            }
        }

        return [];
    }
}
```

## Swift

```swift
class Solution {
    func goodSubsetofBinaryMatrix(_ grid: [[Int]]) -> [Int] {
        let m = grid.count
        guard m > 0 else { return [] }
        let n = grid[0].count
        let maxMask = 1 << n
        var firstIdx = Array(repeating: -1, count: maxMask)
        
        for i in 0..<m {
            var mask = 0
            for j in 0..<n {
                if grid[i][j] == 1 {
                    mask |= (1 << j)
                }
            }
            // size 1 subset possible only with all-zero row
            if mask == 0 {
                return [i]
            }
            if firstIdx[mask] == -1 {
                firstIdx[mask] = i
            }
        }
        
        for a in 0..<maxMask {
            let idxA = firstIdx[a]
            if idxA == -1 { continue }
            for b in a..<maxMask {
                let idxB = firstIdx[b]
                if idxB == -1 { continue }
                if (a & b) != 0 { continue } // overlapping ones, not good
                if a == b { continue } // same non-zero mask can't satisfy condition
                var result = [idxA, idxB]
                if result[0] > result[1] {
                    result.swapAt(0, 1)
                }
                return result
            }
        }
        
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun goodSubsetofBinaryMatrix(grid: Array<IntArray>): List<Int> {
        val m = grid.size
        val n = grid[0].size
        val maskToIdx = HashMap<Int, Int>()
        for (i in 0 until m) {
            var mask = 0
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    mask = mask or (1 shl j)
                }
            }
            if (mask == 0) {
                return listOf(i)
            }
            if (!maskToIdx.containsKey(mask)) {
                maskToIdx[mask] = i
            }
        }

        val masks = maskToIdx.keys.toIntArray()
        for (a in masks) {
            for (b in masks) {
                if ((a and b) == 0) {
                    val idx1 = maskToIdx[a]!!
                    val idx2 = maskToIdx[b]!!
                    return if (idx1 < idx2) listOf(idx1, idx2) else listOf(idx2, idx1)
                }
            }
        }

        return emptyList()
    }
}
```

## Dart

```dart
class Solution {
  List<int> goodSubsetofBinaryMatrix(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int maxMask = 1 << n;

    // Store the first occurrence index of each mask
    List<int?> firstIdx = List.filled(maxMask, null);

    for (int i = 0; i < m; i++) {
      int mask = 0;
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) mask |= 1 << j;
      }
      // Subset of size 1: all-zero row
      if (mask == 0) return [i];
      if (firstIdx[mask] == null) firstIdx[mask] = i;
    }

    // Collect masks that appear in the matrix
    List<int> presentMasks = [];
    for (int mask = 0; mask < maxMask; mask++) {
      if (firstIdx[mask] != null) presentMasks.add(mask);
    }

    // Check pairs of distinct masks where bitwise AND is zero
    for (int a in presentMasks) {
      for (int b in presentMasks) {
        if (a >= b) continue; // ensure distinct and avoid duplicates
        if ((a & b) == 0) {
          int idxA = firstIdx[a]!;
          int idxB = firstIdx[b]!;
          return idxA < idxB ? [idxA, idxB] : [idxB, idxA];
        }
      }
    }

    // No good subset found
    return [];
  }
}
```

## Golang

```go
func goodSubsetofBinaryMatrix(grid [][]int) []int {
	m := len(grid)
	if m == 0 {
		return []int{}
	}
	n := len(grid[0])
	const maxMasks = 1 << 5 // n <= 5
	firstIdx := make([]int, maxMasks)
	for i := range firstIdx {
		firstIdx[i] = -1
	}

	for i, row := range grid {
		mask := 0
		for j, v := range row {
			if v == 1 {
				mask |= 1 << j
			}
		}
		if mask == 0 {
			return []int{i}
		}
		if firstIdx[mask] == -1 {
			firstIdx[mask] = i
		}
	}

	limit := 1 << n
	for a := 0; a < limit; a++ {
		idxA := firstIdx[a]
		if idxA == -1 {
			continue
		}
		for b := a + 1; b < limit; b++ {
			idxB := firstIdx[b]
			if idxB == -1 {
				continue
			}
			if (a & b) == 0 {
				if idxA > idxB {
					idxA, idxB = idxB, idxA
				}
				return []int{idxA, idxB}
			}
		}
	}
	return []int{}
}
```

## Ruby

```ruby
def good_subsetof_binary_matrix(grid)
  n = grid[0].length
  max_mask = 1 << n
  first_idx = Array.new(max_mask, -1)

  grid.each_with_index do |row, i|
    mask = 0
    row.each_with_index { |val, j| mask |= (1 << j) if val == 1 }
    return [i] if mask == 0
    first_idx[mask] = i if first_idx[mask] == -1
  end

  (0...max_mask).each do |m1|
    next if first_idx[m1] == -1
    ((m1 + 1)...max_mask).each do |m2|
      next if first_idx[m2] == -1
      if (m1 & m2) == 0
        i = first_idx[m1]
        j = first_idx[m2]
        return [i, j].sort
      end
    end
  end

  []
end
```

## Scala

```scala
object Solution {
    def goodSubsetofBinaryMatrix(grid: Array[Array[Int]]): List[Int] = {
        val m = grid.length
        val n = grid(0).length
        val seen = scala.collection.mutable.Map[Int, Int]() // mask -> first index

        for (i <- 0 until m) {
            var mask = 0
            var j = 0
            while (j < n) {
                if (grid(i)(j) == 1) mask |= (1 << j)
                j += 1
            }

            if (mask == 0) return List(i)

            // check for a previously seen row with non‑overlapping bits
            val it = seen.iterator
            while (it.hasNext) {
                val (otherMask, otherIdx) = it.next()
                if ((mask & otherMask) == 0) {
                    return List(otherIdx, i).sorted
                }
            }

            // store first occurrence of this mask
            if (!seen.contains(mask)) seen(mask) = i
        }

        List.empty[Int]
    }
}
```

## Rust

```rust
impl Solution {
    pub fn good_subsetof_binary_matrix(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        if m == 0 {
            return vec![];
        }
        let n = grid[0].len();
        let limit = 1usize << n;
        // store first occurrence index for each mask
        let mut first: Vec<Option<usize>> = vec![None; limit];
        for (i, row) in grid.iter().enumerate() {
            let mut mask: usize = 0;
            for (j, &v) in row.iter().enumerate() {
                if v == 1 {
                    mask |= 1 << j;
                }
            }
            // size 1 good subset: all zeros
            if mask == 0 {
                return vec![i as i32];
            }
            if first[mask].is_none() {
                first[mask] = Some(i);
            }
        }

        for a in 0..limit {
            if let Some(idx_a) = first[a] {
                // try all b > a
                for b in (a + 1)..limit {
                    if let Some(idx_b) = first[b] {
                        if (a & b) == 0 {
                            let mut res = vec![idx_a as i32, idx_b as i32];
                            if res[0] > res[1] {
                                res.swap(0, 1);
                            }
                            return res;
                        }
                    }
                }
            }
        }

        vec![]
    }
}
```

## Racket

```racket
#lang racket

(define (row->mask row)
  (let loop ((lst row) (pos 0) (m 0))
    (if (null? lst)
        m
        (loop (cdr lst)
              (+ pos 1)
              (if (= (car lst) 1)
                  (bitwise-ior m (arithmetic-shift 1 pos))
                  m)))))

(define/contract (good-subsetof-binary-matrix grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (call/cc
    (lambda (return)
      (let* ((n (length (first grid)))
             (max-mask (arithmetic-shift 1 n))
             (idx (make-vector max-mask -1)))
        ;; First pass: look for all‑zero row and store first index per mask
        (for ([row grid] [i (in-naturals)])
          (define mask (row->mask row))
          (when (= mask 0)
            (return (list i)))
          (when (= (vector-ref idx mask) -1)
            (vector-set! idx mask i)))
        ;; Second pass: find two rows whose masks have no overlapping 1s
        (for ([a (in-range max-mask)] #:when (not (= (vector-ref idx a) -1)))
          (for ([b (in-range max-mask)]
                #:when (and (not (= (vector-ref idx b) -1))
                            (= (bitwise-and a b) 0)
                            (not (= a b))))
            (define i (vector-ref idx a))
            (define j (vector-ref idx b))
            (if (< i j)
                (return (list i j))
                (return (list j i)))))
        ;; No good subset found
        (return '())))))
```

## Erlang

```erlang
-spec good_subsetof_binary_matrix(Grid :: [[integer()]]) -> [integer()].
good_subsetof_binary_matrix(Grid) ->
    N = length(hd(Grid)),
    build_map(Grid, 0, #{}, N).

build_map([], _Idx, Map, _N) ->
    find_pair_from_map(Map);
build_map([Row|Rest], Idx, Map, N) ->
    Mask = row_to_mask(Row, N),
    case Mask of
        0 -> [Idx];
        _ ->
            NewMap = case maps:is_key(Mask, Map) of
                        true -> Map;
                        false -> maps:put(Mask, Idx, Map)
                     end,
            build_map(Rest, Idx + 1, NewMap, N)
    end.

row_to_mask(Row, N) ->
    row_to_mask(Row, 0, 0, N).

row_to_mask([], _Pos, Acc, _N) -> Acc;
row_to_mask([Bit|Rest], Pos, Acc, N) ->
    NewAcc = case Bit of
                1 -> Acc bor (1 bsl Pos);
                _ -> Acc
             end,
    row_to_mask(Rest, Pos + 1, NewAcc, N).

find_pair_from_map(Map) ->
    Keys = maps:keys(Map),
    case find_pair(Keys, Map) of
        {ok, I1, I2} -> lists:sort([I1, I2]);
        not_found -> []
    end.

find_pair([], _Map) -> not_found;
find_pair([M|Rest], Map) ->
    I1 = maps:get(M, Map),
    case find_match(M, Rest, Map) of
        {ok, I2} -> {ok, I1, I2};
        not_found -> find_pair(Rest, Map)
    end.

find_match(_M, [], _Map) -> not_found;
find_match(M, [M2|Rest], Map) ->
    case (M band M2) of
        0 ->
            I2 = maps:get(M2, Map),
            {ok, I2};
        _ ->
            find_match(M, Rest, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec good_subsetof_binary_matrix(grid :: [[integer]]) :: [integer]
  def good_subsetof_binary_matrix(grid) do
    require Bitwise

    # First pass: look for a zero row and build mask -> index map
    {zero_idx, mask_map} =
      Enum.reduce(Enum.with_index(grid), {nil, %{}}, fn {row, idx}, {found_zero, map} ->
        if found_zero != nil do
          {found_zero, map}
        else
          mask = Enum.reduce(row, 0, fn bit, acc -> Bitwise.<<<(acc, 1) ||| bit end)

          cond do
            mask == 0 ->
              {idx, map}

            true ->
              new_map = Map.put_new(map, mask, idx)
              {nil, new_map}
          end
        end
      end)

    # If a zero row exists, return it as the good subset of size 1
    case zero_idx do
      nil ->
        masks = Map.to_list(mask_map)  # [{mask, index}]

        pair =
          for {m1, i1} <- masks,
              {m2, i2} <- masks,
              i1 < i2,
              Bitwise.band(m1, m2) == 0 do
            [i1, i2] |> Enum.sort()
          end
          |> List.first()

        pair || []

      idx ->
        [idx]
    end
  end
end
```
