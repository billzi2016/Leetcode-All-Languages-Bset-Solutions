# 1337. The K Weakest Rows in a Matrix

## Cpp

```cpp
class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        vector<pair<int,int>> rows; // {soldierCount, index}
        rows.reserve(m);
        for (int i = 0; i < m; ++i) {
            int lo = 0, hi = n;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (mat[i][mid] == 1)
                    lo = mid + 1;
                else
                    hi = mid;
            }
            rows.emplace_back(lo, i);
        }
        sort(rows.begin(), rows.end());
        vector<int> ans;
        ans.reserve(k);
        for (int i = 0; i < k; ++i) {
            ans.push_back(rows[i].second);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        int m = mat.length;
        int n = mat[0].length;
        int[] soldiers = new int[m];
        for (int i = 0; i < m; i++) {
            int lo = 0, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (mat[i][mid] == 1) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            soldiers[i] = lo; // number of 1's
        }

        Integer[] idx = new Integer[m];
        for (int i = 0; i < m; i++) idx[i] = i;

        Arrays.sort(idx, (a, b) -> {
            if (soldiers[a] != soldiers[b]) return soldiers[a] - soldiers[b];
            return a - b;
        });

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = idx[i];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def count_soldiers(row):
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi) // 2
                if row[mid] == 1:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        counts = [(count_soldiers(row), i) for i, row in enumerate(mat)]
        counts.sort()
        return [i for _, i in counts[:k]]
```

## Python3

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = [(sum(row), i) for i, row in enumerate(mat)]
        rows.sort()
        return [i for _, i in rows[:k]]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int cnt;
    int idx;
} Row;

static int cmpRows(const void *a, const void *b) {
    const Row *ra = (const Row *)a;
    const Row *rb = (const Row *)b;
    if (ra->cnt != rb->cnt)
        return ra->cnt - rb->cnt;          // fewer soldiers first
    return ra->idx - rb->idx;              // lower index first
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* kWeakestRows(int** mat, int matSize, int* matColSize, int k, int* returnSize) {
    int n = matColSize[0];
    Row *rows = (Row *)malloc(matSize * sizeof(Row));
    for (int i = 0; i < matSize; ++i) {
        int cnt = 0;
        for (int j = 0; j < n && mat[i][j] == 1; ++j)
            ++cnt;
        rows[i].cnt = cnt;
        rows[i].idx = i;
    }
    
    qsort(rows, matSize, sizeof(Row), cmpRows);
    
    int *res = (int *)malloc(k * sizeof(int));
    for (int i = 0; i < k; ++i)
        res[i] = rows[i].idx;
    
    free(rows);
    *returnSize = k;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] KWeakestRows(int[][] mat, int k) {
        int m = mat.Length;
        var rows = new (int soldiers, int index)[m];
        for (int i = 0; i < m; i++) {
            int n = mat[i].Length;
            int left = 0, right = n;
            while (left < right) {
                int mid = (left + right) / 2;
                if (mat[i][mid] == 1)
                    left = mid + 1;
                else
                    right = mid;
            }
            rows[i] = (left, i);
        }
        Array.Sort(rows, (a, b) => {
            int cmp = a.soldiers.CompareTo(b.soldiers);
            return cmp != 0 ? cmp : a.index.CompareTo(b.index);
        });
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = rows[i].index;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function(mat, k) {
    const m = mat.length;
    const info = [];
    for (let i = 0; i < m; ++i) {
        const row = mat[i];
        let lo = 0, hi = row.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (row[mid] === 1) lo = mid + 1;
            else hi = mid;
        }
        info.push([lo, i]); // [soldierCount, index]
    }
    info.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    const res = [];
    for (let i = 0; i < k; ++i) {
        res.push(info[i][1]);
    }
    return res;
};
```

## Typescript

```typescript
function kWeakestRows(mat: number[][], k: number): number[] {
    const m = mat.length;
    const rows: [number, number][] = new Array(m);
    for (let i = 0; i < m; i++) {
        let left = 0, right = mat[i].length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (mat[i][mid] === 1) left = mid + 1;
            else right = mid;
        }
        rows[i] = [left, i];
    }
    rows.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    const ans: number[] = [];
    for (let i = 0; i < k; i++) ans.push(rows[i][1]);
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Integer[]
     */
    function kWeakestRows($mat, $k) {
        $rows = [];
        foreach ($mat as $i => $row) {
            $cnt = 0;
            foreach ($row as $val) {
                if ($val == 1) {
                    $cnt++;
                } else {
                    break; // soldiers are contiguous at the start
                }
            }
            $rows[] = [$cnt, $i];
        }

        usort($rows, function($a, $b) {
            if ($a[0] === $b[0]) {
                return $a[1] <=> $b[1];
            }
            return $a[0] <=> $b[0];
        });

        $result = [];
        for ($i = 0; $i < $k; $i++) {
            $result[] = $rows[$i][1];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func kWeakestRows(_ mat: [[Int]], _ k: Int) -> [Int] {
        var rowsInfo: [(soldiers: Int, index: Int)] = []
        
        for (i, row) in mat.enumerated() {
            var low = 0
            var high = row.count
            while low < high {
                let mid = (low + high) / 2
                if row[mid] == 1 {
                    low = mid + 1
                } else {
                    high = mid
                }
            }
            rowsInfo.append((soldiers: low, index: i))
        }
        
        rowsInfo.sort { a, b in
            if a.soldiers == b.soldiers {
                return a.index < b.index
            }
            return a.soldiers < b.soldiers
        }
        
        var result: [Int] = []
        for i in 0..<k {
            result.append(rowsInfo[i].index)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kWeakestRows(mat: Array<IntArray>, k: Int): IntArray {
        val rows = mutableListOf<Pair<Int, Int>>()
        for (i in mat.indices) {
            rows.add(Pair(countOnes(mat[i]), i))
        }
        rows.sortWith(compareBy({ it.first }, { it.second }))
        return IntArray(k) { rows[it].second }
    }

    private fun countOnes(row: IntArray): Int {
        var left = 0
        var right = row.size
        while (left < right) {
            val mid = (left + right) ushr 1
            if (row[mid] == 1) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  List<int> kWeakestRows(List<List<int>> mat, int k) {
    final rows = <MapEntry<int, int>>[];
    for (int i = 0; i < mat.length; i++) {
      int count = 0;
      for (final val in mat[i]) {
        if (val == 1) {
          count++;
        } else {
          break;
        }
      }
      rows.add(MapEntry(count, i));
    }
    rows.sort((a, b) {
      if (a.key != b.key) return a.key - b.key;
      return a.value - b.value;
    });
    final result = <int>[];
    for (int i = 0; i < k; i++) {
      result.add(rows[i].value);
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func kWeakestRows(mat [][]int, k int) []int {
	type pair struct {
		cnt int
		idx int
	}
	m := len(mat)
	pairs := make([]pair, m)
	for i := 0; i < m; i++ {
		row := mat[i]
		lo, hi := 0, len(row)
		for lo < hi {
			mid := (lo + hi) / 2
			if row[mid] == 1 {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		pairs[i] = pair{cnt: lo, idx: i}
	}
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].cnt == pairs[j].cnt {
			return pairs[i].idx < pairs[j].idx
		}
		return pairs[i].cnt < pairs[j].cnt
	})
	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[i] = pairs[i].idx
	}
	return res
}
```

## Ruby

```ruby
def k_weakest_rows(mat, k)
  counts = mat.each_with_index.map { |row, i| [row.sum, i] }
  counts.sort_by! { |cnt, idx| [cnt, idx] }
  counts.first(k).map { |_, idx| idx }
end
```

## Scala

```scala
object Solution {
    def kWeakestRows(mat: Array[Array[Int]], k: Int): Array[Int] = {
        def countOnes(row: Array[Int]): Int = {
            var lo = 0
            var hi = row.length
            while (lo < hi) {
                val mid = (lo + hi) >>> 1
                if (row(mid) == 1) lo = mid + 1 else hi = mid
            }
            lo
        }

        val indexedCounts = mat.indices.map(i => (countOnes(mat(i)), i))
        indexedCounts.sortBy { case (cnt, idx) => (cnt, idx) }.take(k).map(_._2).toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut rows: Vec<(i32, usize)> = mat
            .iter()
            .enumerate()
            .map(|(idx, row)| (Self::soldier_count(row), idx))
            .collect();
        rows.sort_by_key(|&(cnt, idx)| (cnt, idx));
        rows.into_iter()
            .take(k as usize)
            .map(|(_, idx)| idx as i32)
            .collect()
    }

    fn soldier_count(row: &Vec<i32>) -> i32 {
        let mut lo = 0usize;
        let mut hi = row.len();
        while lo < hi {
            let mid = (lo + hi) / 2;
            if row[mid] == 1 {
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
(require racket/list)

(define/contract (k-weakest-rows mat k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  (let* ([pairs
          (map-indexed (lambda (i row)
                         (list (count (lambda (x) (= x 1)) row) i))
                       mat)]
         [sorted
          (sort pairs
                (lambda (a b)
                  (or (< (first a) (first b))
                      (and (= (first a) (first b))
                           (< (second a) (second b))))))])
    (map second (take sorted k))))
```

## Erlang

```erlang
-module(solution).
-export([k_weakest_rows/2]).

-spec k_weakest_rows(Mat :: [[integer()]], K :: integer()) -> [integer()].
k_weakest_rows(Mat, K) ->
    Counts = counts_with_index(Mat, 0, []),
    Sorted = lists:sort(Counts),
    take_k(Sorted, K).

counts_with_index([], _Idx, Acc) -> Acc;
counts_with_index([Row|Rest], Idx, Acc) ->
    Count = count_soldiers(Row),
    counts_with_index(Rest, Idx + 1, [{Count, Idx} | Acc]).

count_soldiers([]) -> 0;
count_soldiers([1|Tail]) -> 1 + count_soldiers(Tail);
count_soldiers([0|_]) -> 0.

take_k(Sorted, K) -> take_k(Sorted, K, []).

take_k(_, 0, Acc) -> lists:reverse(Acc);
take_k([], _K, Acc) -> lists:reverse(Acc);
take_k([{_Count, Index}|Rest], K, Acc) ->
    take_k(Rest, K - 1, [Index | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec k_weakest_rows(mat :: [[integer]], k :: integer) :: [integer]
  def k_weakest_rows(mat, k) do
    mat
    |> Enum.with_index()
    |> Enum.map(fn {row, idx} -> {count_soldiers(row), idx} end)
    |> Enum.sort_by(fn {cnt, idx} -> {cnt, idx} end)
    |> Enum.take(k)
    |> Enum.map(fn {_cnt, idx} -> idx end)
  end

  defp count_soldiers(row) do
    binary_search(row, 0, length(row))
  end

  defp binary_search(_row, low, high) when low >= high, do: low

  defp binary_search(row, low, high) do
    mid = div(low + high, 2)

    if Enum.at(row, mid) == 1 do
      binary_search(row, mid + 1, high)
    else
      binary_search(row, low, mid)
    end
  end
end
```
