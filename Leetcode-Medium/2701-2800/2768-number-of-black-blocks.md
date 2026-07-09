# 2768. Number of Black Blocks

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<long long> countBlackBlocks(int m, int n, vector<vector<int>>& coordinates) {
        unordered_map<long long, int> blockCnt;
        blockCnt.reserve(coordinates.size() * 4 * 2);
        for (const auto& cell : coordinates) {
            int x = cell[0], y = cell[1];
            for (int dx = -1; dx <= 0; ++dx) {
                for (int dy = -1; dy <= 0; ++dy) {
                    int tx = x + dx;
                    int ty = y + dy;
                    if (tx >= 0 && tx < m - 1 && ty >= 0 && ty < n - 1) {
                        long long key = ((long long)tx << 32) | (unsigned int)ty;
                        ++blockCnt[key];
                    }
                }
            }
        }

        vector<long long> ans(5, 0);
        long long totalBlocks = (long long)(m - 1) * (n - 1);

        for (const auto& kv : blockCnt) {
            int c = kv.second; // 1..4
            if (c >= 0 && c <= 4) ans[c]++;
        }

        long long counted = 0;
        for (int i = 1; i <= 4; ++i) counted += ans[i];
        ans[0] = totalBlocks - counted;

        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] countBlackBlocks(int m, int n, int[][] coordinates) {
        java.util.HashMap<Long, Integer> blockCount = new java.util.HashMap<>();
        for (int[] cell : coordinates) {
            int x = cell[0];
            int y = cell[1];
            for (int dx = -1; dx <= 0; dx++) {
                int tx = x + dx;
                if (tx < 0 || tx >= m - 1) continue;
                for (int dy = -1; dy <= 0; dy++) {
                    int ty = y + dy;
                    if (ty < 0 || ty >= n - 1) continue;
                    long key = ((long) tx << 32) | (ty & 0xffffffffL);
                    blockCount.put(key, blockCount.getOrDefault(key, 0) + 1);
                }
            }
        }

        long[] ans = new long[5];
        for (int cnt : blockCount.values()) {
            if (cnt >= 1 && cnt <= 4) {
                ans[cnt]++;
            }
        }

        long totalBlocks = (long) (m - 1) * (n - 1);
        long nonZero = ans[1] + ans[2] + ans[3] + ans[4];
        ans[0] = totalBlocks - nonZero;
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        """
        :type m: int
        :type n: int
        :type coordinates: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict

        block_counts = defaultdict(int)

        for x, y in coordinates:
            # each black cell can belong to up to 4 blocks whose top-left corners are (x-1,y-1), (x-1,y), (x,y-1), (x,y)
            for dx in (-1, 0):
                for dy in (-1, 0):
                    tlx = x + dx
                    tly = y + dy
                    if 0 <= tlx < m - 1 and 0 <= tly < n - 1:
                        block_counts[(tlx, tly)] += 1

        total_blocks = (m - 1) * (n - 1)
        ans = [0] * 5
        ans[0] = total_blocks - len(block_counts)

        for cnt in block_counts.values():
            if 1 <= cnt <= 4:
                ans[cnt] += 1

        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_counts = defaultdict(int)
        for x, y in coordinates:
            for dx in (-1, 0):
                for dy in (-1, 0):
                    tx = x + dx
                    ty = y + dy
                    if 0 <= tx < m - 1 and 0 <= ty < n - 1:
                        block_counts[(tx, ty)] += 1

        total_blocks = (m - 1) * (n - 1)
        ans = [0] * 5
        ans[0] = total_blocks - len(block_counts)

        for cnt in block_counts.values():
            if 1 <= cnt <= 4:
                ans[cnt] += 1

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->x != pb->x) return pa->x - pb->x;
    return pa->y - pb->y;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countBlackBlocks(int m, int n, int** coordinates, int coordinatesSize, int* coordinatesColSize, int* returnSize) {
    // Maximum possible entries: 4 per black cell
    int maxEntries = coordinatesSize * 4;
    Pair *blocks = (Pair *)malloc(sizeof(Pair) * maxEntries);
    int blkCnt = 0;

    for (int i = 0; i < coordinatesSize; ++i) {
        int x = coordinates[i][0];
        int y = coordinates[i][1];

        // top-left corners that include (x, y)
        for (int dx = -1; dx <= 0; ++dx) {
            int nx = x + dx;
            if (nx < 0 || nx >= m - 1) continue;
            for (int dy = -1; dy <= 0; ++dy) {
                int ny = y + dy;
                if (ny < 0 || ny >= n - 1) continue;
                blocks[blkCnt].x = nx;
                blocks[blkCnt].y = ny;
                ++blkCnt;
            }
        }
    }

    // Sort to group identical blocks
    qsort(blocks, blkCnt, sizeof(Pair), cmpPair);

    long long ans[5] = {0};
    int i = 0;
    while (i < blkCnt) {
        int j = i + 1;
        while (j < blkCnt && blocks[j].x == blocks[i].x && blocks[j].y == blocks[i].y) {
            ++j;
        }
        int cntBlack = j - i; // number of black cells in this block
        if (cntBlack >= 1 && cntBlack <= 4) {
            ans[cntBlack] += 1;
        }
        i = j;
    }

    long long totalBlocks = (long long)(m - 1) * (n - 1);
    long long sumNonZero = ans[1] + ans[2] + ans[3] + ans[4];
    ans[0] = totalBlocks - sumNonZero;

    free(blocks);

    long long *ret = (long long *)malloc(5 * sizeof(long long));
    for (int k = 0; k < 5; ++k) ret[k] = ans[k];
    *returnSize = 5;
    return ret;
}
```

## Csharp

```csharp
public class Solution
{
    public long[] CountBlackBlocks(int m, int n, int[][] coordinates)
    {
        var blockCounts = new Dictionary<(int, int), int>();
        foreach (var cell in coordinates)
        {
            int x = cell[0];
            int y = cell[1];
            for (int dx = -1; dx <= 0; ++dx)
            {
                int bx = x + dx;
                if (bx < 0 || bx >= m - 1) continue;
                for (int dy = -1; dy <= 0; ++dy)
                {
                    int by = y + dy;
                    if (by < 0 || by >= n - 1) continue;
                    var key = (bx, by);
                    if (blockCounts.TryGetValue(key, out int cur))
                        blockCounts[key] = cur + 1;
                    else
                        blockCounts[key] = 1;
                }
            }
        }

        long[] ans = new long[5];
        foreach (var kvp in blockCounts)
        {
            ans[kvp.Value]++;
        }

        long totalBlocks = (long)(m - 1) * (n - 1);
        ans[0] = totalBlocks - (ans[1] + ans[2] + ans[3] + ans[4]);
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} coordinates
 * @return {number[]}
 */
var countBlackBlocks = function(m, n, coordinates) {
    const maxX = m - 1; // number of possible top-left rows
    const maxY = n - 1; // number of possible top-left cols
    const blockCounts = new Map(); // key -> black cells in that block

    for (const [x, y] of coordinates) {
        for (let dx = -1; dx <= 0; ++dx) {
            const bx = x + dx;
            if (bx < 0 || bx >= maxX) continue;
            for (let dy = -1; dy <= 0; ++dy) {
                const by = y + dy;
                if (by < 0 || by >= maxY) continue;
                const key = bx * maxY + by; // unique encoding
                blockCounts.set(key, (blockCounts.get(key) || 0) + 1);
            }
        }
    }

    const ans = [0, 0, 0, 0, 0];
    for (const cnt of blockCounts.values()) {
        ans[cnt]++; // cnt is between 1 and 4
    }

    const totalBlocks = maxX * maxY;
    const counted = ans[1] + ans[2] + ans[3] + ans[4];
    ans[0] = totalBlocks - counted;

    return ans;
};
```

## Typescript

```typescript
function countBlackBlocks(m: number, n: number, coordinates: number[][]): number[] {
    const blockCounts = new Map<number, number>();
    const maxX = m - 1;
    const maxY = n - 1; // number of possible top‑left rows/cols

    for (const [x, y] of coordinates) {
        for (let dx = -1; dx <= 0; ++dx) {
            const bx = x + dx;
            if (bx < 0 || bx >= maxX) continue;
            for (let dy = -1; dy <= 0; ++dy) {
                const by = y + dy;
                if (by < 0 || by >= maxY) continue;
                const key = bx * maxY + by;
                blockCounts.set(key, (blockCounts.get(key) ?? 0) + 1);
            }
        }
    }

    const ans = [0, 0, 0, 0, 0];
    for (const cnt of blockCounts.values()) {
        if (cnt >= 1 && cnt <= 4) ans[cnt]++;
    }

    const totalBlocks = (m - 1) * (n - 1);
    const nonZero = ans[1] + ans[2] + ans[3] + ans[4];
    ans[0] = totalBlocks - nonZero;

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $coordinates
     * @return Integer[]
     */
    function countBlackBlocks($m, $n, $coordinates) {
        $blockCounts = [];

        foreach ($coordinates as $coord) {
            $x = $coord[0];
            $y = $coord[1];

            for ($dx = -1; $dx <= 0; $dx++) {
                $tx = $x + $dx;
                if ($tx < 0 || $tx >= $m - 1) continue;

                for ($dy = -1; $dy <= 0; $dy++) {
                    $ty = $y + $dy;
                    if ($ty < 0 || $ty >= $n - 1) continue;

                    $key = $tx . ':' . $ty;
                    if (!isset($blockCounts[$key])) {
                        $blockCounts[$key] = 1;
                    } else {
                        $blockCounts[$key]++;
                    }
                }
            }
        }

        $totalBlocks = ($m - 1) * ($n - 1);
        $result = array_fill(0, 5, 0);
        $result[0] = $totalBlocks - count($blockCounts);

        foreach ($blockCounts as $cnt) {
            // $cnt is between 1 and 4
            $result[$cnt]++;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countBlackBlocks(_ m: Int, _ n: Int, _ coordinates: [[Int]]) -> [Int] {
        let rows = m - 1
        let cols = n - 1
        var blockMap = [Int64: Int]()
        let offsets = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
        
        for coord in coordinates {
            let x = coord[0]
            let y = coord[1]
            for (dx, dy) in offsets {
                let tx = x + dx
                let ty = y + dy
                if tx >= 0 && tx < rows && ty >= 0 && ty < cols {
                    let key = Int64(tx) * Int64(cols) + Int64(ty)
                    blockMap[key, default: 0] += 1
                }
            }
        }
        
        var result = [Int](repeating: 0, count: 5)
        let totalBlocks = Int64(rows) * Int64(cols)
        var blocksWithBlack: Int64 = 0
        
        for cnt in blockMap.values {
            if cnt >= 1 && cnt <= 4 {
                result[cnt] += 1
            }
            blocksWithBlack += 1
        }
        
        result[0] = Int(totalBlocks - blocksWithBlack)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countBlackBlocks(m: Int, n: Int, coordinates: Array<IntArray>): LongArray {
        val blockMap = HashMap<Long, Int>()
        for (coord in coordinates) {
            val x = coord[0]
            val y = coord[1]
            for (dx in -1..0) {
                val nx = x + dx
                if (nx < 0 || nx >= m - 1) continue
                for (dy in -1..0) {
                    val ny = y + dy
                    if (ny < 0 || ny >= n - 1) continue
                    val key = nx.toLong() * n + ny
                    blockMap[key] = (blockMap[key] ?: 0) + 1
                }
            }
        }

        val ans = LongArray(5)
        for (cnt in blockMap.values) {
            if (cnt in 1..4) ans[cnt]++
        }

        val totalBlocks = (m - 1).toLong() * (n - 1).toLong()
        var nonZero = 0L
        for (i in 1..4) nonZero += ans[i]
        ans[0] = totalBlocks - nonZero

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countBlackBlocks(int m, int n, List<List<int>> coordinates) {
    final Map<int, int> blockCount = {};
    final int maxX = m - 1;
    final int maxY = n - 1;

    for (final coord in coordinates) {
      final int x = coord[0];
      final int y = coord[1];
      for (int dx = -1; dx <= 0; ++dx) {
        final int nx = x + dx;
        if (nx < 0 || nx >= maxX) continue;
        for (int dy = -1; dy <= 0; ++dy) {
          final int ny = y + dy;
          if (ny < 0 || ny >= maxY) continue;
          final int key = nx * maxY + ny;
          blockCount[key] = (blockCount[key] ?? 0) + 1;
        }
      }
    }

    final List<int> ans = List.filled(5, 0);
    for (final cnt in blockCount.values) {
      if (cnt >= 1 && cnt <= 4) ans[cnt]++;
    }

    int totalBlocks = maxX * maxY;
    int nonZero = 0;
    for (int i = 1; i <= 4; ++i) nonZero += ans[i];
    ans[0] = totalBlocks - nonZero;

    return ans;
  }
}
```

## Golang

```go
func countBlackBlocks(m int, n int, coordinates [][]int) []int64 {
    blockCount := make(map[int64]int)

    for _, p := range coordinates {
        x, y := p[0], p[1]
        for dx := -1; dx <= 0; dx++ {
            for dy := -1; dy <= 0; dy++ {
                tlx := x + dx
                tly := y + dy
                if tlx >= 0 && tlx < m-1 && tly >= 0 && tyl < n-1 {
                    key := (int64(tlx) << 32) | int64(tly)
                    blockCount[key]++
                }
            }
        }
    }

    res := make([]int64, 5)
    for _, cnt := range blockCount {
        if cnt >= 1 && cnt <= 4 {
            res[cnt]++
        }
    }

    totalBlocks := int64(m-1) * int64(n-1)
    sumNonZero := res[1] + res[2] + res[3] + res[4]
    res[0] = totalBlocks - sumNonZero
    return res
}
```

## Ruby

```ruby
def count_black_blocks(m, n, coordinates)
  block_counts = Hash.new(0)

  coordinates.each do |x, y|
    (-1..0).each do |dx|
      tl_x = x + dx
      next if tl_x < 0 || tl_x >= m - 1
      (-1..0).each do |dy|
        tl_y = y + dy
        next if tl_y < 0 || tl_y >= n - 1
        block_counts[[tl_x, tl_y]] += 1
      end
    end
  end

  ans = Array.new(5, 0)
  block_counts.each_value { |cnt| ans[cnt] += 1 }

  total_blocks = (m - 1) * (n - 1)
  counted = ans[1..4].reduce(0, :+)
  ans[0] = total_blocks - counted
  ans
end
```

## Scala

```scala
object Solution {
    def countBlackBlocks(m: Int, n: Int, coordinates: Array[Array[Int]]): Array[Long] = {
        import scala.collection.mutable

        val blockCounts = mutable.Map[Long, Int]()
        def encode(x: Int, y: Int): Long = (x.toLong << 32) | (y & 0xffffffffL)

        for (c <- coordinates) {
            val x = c(0)
            val y = c(1)
            for (dx <- -1 to 0) {
                val bx = x + dx
                if (bx >= 0 && bx < m - 1) {
                    for (dy <- -1 to 0) {
                        val by = y + dy
                        if (by >= 0 && by < n - 1) {
                            val key = encode(bx, by)
                            blockCounts.update(key, blockCounts.getOrElse(key, 0) + 1)
                        }
                    }
                }
            }
        }

        val res = Array.ofDim[Long](5)
        var countedBlocks: Long = 0L
        for ((_, cnt) <- blockCounts) {
            if (cnt >= 1 && cnt <= 4) {
                res(cnt) += 1
                countedBlocks += 1
            }
        }

        val totalBlocks = (m - 1).toLong * (n - 1)
        res(0) = totalBlocks - countedBlocks
        res
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_black_blocks(m: i32, n: i32, coordinates: Vec<Vec<i32>>) -> Vec<i64> {
        let mut block_counts: HashMap<(i32, i32), u8> = HashMap::new();
        let max_x = m - 1;
        let max_y = n - 1;

        for coord in &coordinates {
            let x = coord[0];
            let y = coord[1];
            for dx in -1..=0 {
                for dy in -1..=0 {
                    let tx = x + dx;
                    let ty = y + dy;
                    if tx >= 0 && tx < max_x && ty >= 0 && ty < max_y {
                        *block_counts.entry((tx, ty)).or_insert(0) += 1;
                    }
                }
            }
        }

        let mut ans = vec![0i64; 5];
        for &cnt in block_counts.values() {
            ans[cnt as usize] += 1;
        }

        let total_blocks: i64 = (max_x as i64) * (max_y as i64);
        let non_zero: i64 = ans.iter().skip(1).sum();
        ans[0] = total_blocks - non_zero;

        ans
    }
}
```

## Racket

```racket
(define/contract (count-black-blocks m n coordinates)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([block-count (make-hash)]
         [add-to-block
          (lambda (bx by)
            (when (and (>= bx 0) (< bx (- m 1))
                       (>= by 0) (< by (- n 1)))
              (define key (cons bx by))
              (hash-set! block-count key (add1 (hash-ref block-count key 0))))))])
    (for ([coord coordinates])
      (let* ([x (first coord)]
             [y (second coord)])
        (add-to-block x y)
        (add-to-block (- x 1) y)
        (add-to-block x (- y 1))
        (add-to-block (- x 1) (- y 1))))
    (define total (* (- m 1) (- n 1)))
    (define result (make-vector 5 0))
    (for ([kv (in-hash block-count)])
      (let* ([cnt (cdr kv)]) ; number of black cells in this block
        (vector-set! result cnt (add1 (vector-ref result cnt)))))
    (vector-set! result 0 (- total (hash-count block-count)))
    (vector->list result)))
```

## Erlang

```erlang
-spec count_black_blocks(M :: integer(), N :: integer(), Coordinates :: [[integer()]]) -> [integer()].
count_black_blocks(M, N, Coordinates) ->
    TotalBlocks = (M - 1) * (N - 1),
    Offsets = [{-1, -1}, {-1, 0}, {0, -1}, {0, 0}],
    BlockMap = lists:foldl(
        fun([X, Y], AccMap) ->
            lists:foldl(
                fun({DX, DY}, MapAcc) ->
                    TLX = X + DX,
                    TLY = Y + DY,
                    if
                        TLX >= 0, TLX < M - 1,
                        TLY >= 0, TLY < N - 1 ->
                            Count = maps:get({TLX, TLY}, MapAcc, 0),
                            maps:put({TLX, TLY}, Count + 1, MapAcc);
                        true ->
                            MapAcc
                    end
                end,
                AccMap,
                Offsets
            )
        end,
        #{},
        Coordinates
    ),
    ResultTuple1 = maps:fold(
        fun(_Key, Cnt, Tuple) ->
            Old = element(Cnt + 1, Tuple),
            setelement(Cnt + 1, Tuple, Old + 1)
        end,
        {0, 0, 0, 0, 0},
        BlockMap
    ),
    ZeroCount = TotalBlocks - maps:size(BlockMap),
    ResultTuple = setelement(1, ResultTuple1, ZeroCount),
    tuple_to_list(ResultTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_black_blocks(m :: integer, n :: integer, coordinates :: [[integer]]) :: [integer]
  def count_black_blocks(m, n, coordinates) do
    block_counts =
      Enum.reduce(coordinates, %{}, fn [x, y], acc ->
        Enum.reduce([-1, 0], acc, fn dx, acc2 ->
          Enum.reduce([-1, 0], acc2, fn dy, acc3 ->
            i = x + dx
            j = y + dy

            if i >= 0 and i < m - 1 and j >= 0 and j < n - 1 do
              Map.update(acc3, {i, j}, 1, &(&1 + 1))
            else
              acc3
            end
          end)
        end)
      end)

    freq =
      Enum.reduce(block_counts, [0, 0, 0, 0, 0], fn {_k, c}, arr ->
        List.update_at(arr, c, &(&1 + 1))
      end)

    total_blocks = (m - 1) * (n - 1)
    non_zero_blocks = map_size(block_counts)
    zero_blocks = total_blocks - non_zero_blocks

    [zero_blocks, Enum.at(freq, 1), Enum.at(freq, 2), Enum.at(freq, 3), Enum.at(freq, 4)]
  end
end
```
