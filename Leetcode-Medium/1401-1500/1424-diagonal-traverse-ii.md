# 1424. Diagonal Traverse II

## Cpp

```cpp
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        unordered_map<int, vector<int>> groups;
        int maxSum = 0;
        long long total = 0;
        for (int r = (int)nums.size() - 1; r >= 0; --r) {
            const auto& row = nums[r];
            for (int c = 0; c < (int)row.size(); ++c) {
                int d = r + c;
                groups[d].push_back(row[c]);
                if (d > maxSum) maxSum = d;
                ++total;
            }
        }
        vector<int> ans;
        ans.reserve(total);
        for (int i = 0; i <= maxSum; ++i) {
            auto it = groups.find(i);
            if (it != groups.end()) {
                ans.insert(ans.end(), it->second.begin(), it->second.end());
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] findDiagonalOrder(java.util.List<java.util.List<Integer>> nums) {
        int total = 0;
        for (java.util.List<Integer> row : nums) {
            total += row.size();
        }
        java.util.ArrayList<java.util.List<Integer>> groups = new java.util.ArrayList<>();
        int maxKey = 0;
        for (int i = 0; i < nums.size(); i++) {
            java.util.List<Integer> row = nums.get(i);
            for (int j = 0; j < row.size(); j++) {
                int key = i + j;
                while (groups.size() <= key) {
                    groups.add(new java.util.ArrayList<>());
                }
                groups.get(key).add(row.get(j));
                if (key > maxKey) {
                    maxKey = key;
                }
            }
        }
        int[] ans = new int[total];
        int idx = 0;
        for (int k = 0; k <= maxKey; k++) {
            java.util.List<Integer> list = groups.get(k);
            for (int p = list.size() - 1; p >= 0; p--) {
                ans[idx++] = list.get(p);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        groups = defaultdict(list)
        max_key = 0
        for i in range(len(nums) - 1, -1, -1):
            row = nums[i]
            for j, val in enumerate(row):
                d = i + j
                groups[d].append(val)
                if d > max_key:
                    max_key = d
        ans = []
        for k in range(max_key + 1):
            ans.extend(groups[k])
        return ans
```

## Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for r in range(len(nums) - 1, -1, -1):
            row = nums[r]
            for c, val in enumerate(row):
                groups[r + c].append(val)
        ans = []
        for d in range(max(groups.keys()) + 1):
            ans.extend(groups[d])
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDiagonalOrder(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    // Determine maximum diagonal index and total number of elements
    int maxDiag = 0;
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += numsColSize[i];
        for (int j = 0; j < numsColSize[i]; ++j) {
            int d = i + j;
            if (d > maxDiag) maxDiag = d;
        }
    }
    
    // Allocate structures for groups
    int **groupVals = (int **)malloc((maxDiag + 1) * sizeof(int *));
    int *groupSize = (int *)calloc(maxDiag + 1, sizeof(int));
    int *groupCap  = (int *)calloc(maxDiag + 1, sizeof(int));
    
    for (int d = 0; d <= maxDiag; ++d) {
        groupVals[d] = NULL;
        groupCap[d] = 0;
    }
    
    // Fill groups: iterate rows from bottom to top
    for (int i = numsSize - 1; i >= 0; --i) {
        int cols = numsColSize[i];
        for (int j = 0; j < cols; ++j) {
            int d = i + j;
            if (groupSize[d] == groupCap[d]) {
                // expand capacity
                int newCap = groupCap[d] == 0 ? 4 : groupCap[d] * 2;
                int *newArr = (int *)realloc(groupVals[d], newCap * sizeof(int));
                groupVals[d] = newArr;
                groupCap[d] = newCap;
            }
            groupVals[d][groupSize[d]++] = nums[i][j];
        }
    }
    
    // Build result array
    int *result = (int *)malloc(total * sizeof(int));
    int pos = 0;
    for (int d = 0; d <= maxDiag; ++d) {
        for (int k = 0; k < groupSize[d]; ++k) {
            result[pos++] = groupVals[d][k];
        }
        // free each group's memory
        if (groupVals[d]) free(groupVals[d]);
    }
    
    free(groupVals);
    free(groupSize);
    free(groupCap);
    
    *returnSize = total;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindDiagonalOrder(IList<IList<int>> nums) {
        var groups = new Dictionary<int, List<int>>();
        int maxKey = 0;
        for (int i = nums.Count - 1; i >= 0; i--) {
            var row = nums[i];
            for (int j = 0; j < row.Count; j++) {
                int key = i + j;
                if (!groups.TryGetValue(key, out var list)) {
                    list = new List<int>();
                    groups[key] = list;
                }
                list.Add(row[j]);
                if (key > maxKey) maxKey = key;
            }
        }

        int total = 0;
        foreach (var row in nums) total += row.Count;
        int[] result = new int[total];
        int idx = 0;
        for (int k = 0; k <= maxKey; k++) {
            if (groups.TryGetValue(k, out var list)) {
                foreach (int val in list) {
                    result[idx++] = val;
                }
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var findDiagonalOrder = function(nums) {
    const groups = new Map(); // sum -> array of values in correct order
    
    for (let r = nums.length - 1; r >= 0; --r) {
        const row = nums[r];
        for (let c = 0; c < row.length; ++c) {
            const d = r + c;
            if (!groups.has(d)) groups.set(d, []);
            groups.get(d).push(row[c]);
        }
    }
    
    const result = [];
    for (let d = 0; ; ++d) {
        const arr = groups.get(d);
        if (!arr) break;
        result.push(...arr);
    }
    return result;
};
```

## Typescript

```typescript
function findDiagonalOrder(nums: number[][]): number[] {
    const groups: number[][] = [];
    let maxDiag = 0;
    for (let r = nums.length - 1; r >= 0; --r) {
        const row = nums[r];
        for (let c = 0; c < row.length; ++c) {
            const d = r + c;
            if (!groups[d]) groups[d] = [];
            groups[d].push(row[c]);
            if (d > maxDiag) maxDiag = d;
        }
    }
    const ans: number[] = [];
    for (let d = 0; d <= maxDiag; ++d) {
        const arr = groups[d];
        if (arr) {
            for (const v of arr) ans.push(v);
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer[]
     */
    function findDiagonalOrder($nums) {
        $groups = [];
        $maxKey = 0;
        $rows = count($nums);
        for ($i = $rows - 1; $i >= 0; $i--) {
            $cols = count($nums[$i]);
            for ($j = 0; $j < $cols; $j++) {
                $key = $i + $j;
                if (!isset($groups[$key])) {
                    $groups[$key] = [];
                }
                $groups[$key][] = $nums[$i][$j];
                if ($key > $maxKey) {
                    $maxKey = $key;
                }
            }
        }

        $ans = [];
        for ($d = 0; $d <= $maxKey; $d++) {
            if (isset($groups[$d])) {
                foreach ($groups[$d] as $val) {
                    $ans[] = $val;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findDiagonalOrder(_ nums: [[Int]]) -> [Int] {
        var groups = [Int: [Int]]()
        var maxSum = 0
        let rowCount = nums.count
        
        for r in stride(from: rowCount - 1, through: 0, by: -1) {
            let row = nums[r]
            for c in 0..<row.count {
                let d = r + c
                groups[d, default: []].append(row[c])
                if d > maxSum { maxSum = d }
            }
        }
        
        var result = [Int]()
        result.reserveCapacity(groups.values.reduce(0) { $0 + $1.count })
        for d in 0...maxSum {
            if let arr = groups[d] {
                result.append(contentsOf: arr)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDiagonalOrder(nums: List<List<Int>>): IntArray {
        val groups = HashMap<Int, MutableList<Int>>()
        for (i in nums.indices.reversed()) {
            val row = nums[i]
            for (j in row.indices) {
                val d = i + j
                groups.computeIfAbsent(d) { mutableListOf() }.add(row[j])
            }
        }
        val total = nums.sumOf { it.size }
        val result = IntArray(total)
        var idx = 0
        var d = 0
        while (true) {
            val list = groups[d] ?: break
            for (v in list) {
                result[idx++] = v
            }
            d++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findDiagonalOrder(List<List<int>> nums) {
    final Map<int, List<int>> groups = {};
    for (int i = nums.length - 1; i >= 0; --i) {
      final row = nums[i];
      for (int j = 0; j < row.length; ++j) {
        int d = i + j;
        groups.putIfAbsent(d, () => []).add(row[j]);
      }
    }
    List<int> ans = [];
    var keys = groups.keys.toList()..sort();
    for (int k in keys) {
      ans.addAll(groups[k]!);
    }
    return ans;
  }
}
```

## Golang

```go
package main

func findDiagonalOrder(nums [][]int) []int {
	groups := make(map[int][]int)
	maxKey, total := 0, 0

	for r := len(nums) - 1; r >= 0; r-- {
		row := nums[r]
		for c, v := range row {
			key := r + c
			groups[key] = append(groups[key], v)
			if key > maxKey {
				maxKey = key
			}
			total++
		}
	}

	ans := make([]int, 0, total)
	for i := 0; i <= maxKey; i++ {
		if vals, ok := groups[i]; ok {
			ans = append(ans, vals...)
		}
	}
	return ans
}
```

## Ruby

```ruby
def find_diagonal_order(nums)
  groups = Hash.new { |h, k| h[k] = [] }
  (nums.length - 1).downto(0) do |i|
    nums[i].each_with_index do |val, j|
      groups[i + j] << val
    end
  end
  result = []
  max_key = groups.keys.max || -1
  (0..max_key).each do |k|
    result.concat(groups[k]) if groups.key?(k)
  end
  result
end
```

## Scala

```scala
object Solution {
  def findDiagonalOrder(nums: List[List[Int]]): Array[Int] = {
    val groups = scala.collection.mutable.Map[Int, scala.collection.mutable.ArrayBuffer[Int]]()
    for (i <- nums.indices.reverse) {
      val row = nums(i)
      var j = 0
      while (j < row.length) {
        val d = i + j
        groups.getOrElseUpdate(d, scala.collection.mutable.ArrayBuffer[Int]()) += row(j)
        j += 1
      }
    }
    val total = nums.foldLeft(0)(_ + _.size)
    val result = new Array[Int](total)
    var idx = 0
    val maxKey = if (groups.isEmpty) -1 else groups.keys.max
    for (d <- 0 to maxKey) {
      groups.get(d).foreach { buf =>
        var k = 0
        while (k < buf.length) {
          result(idx) = buf(k)
          idx += 1
          k += 1
        }
      }
    }
    result
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_diagonal_order(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let mut groups: Vec<Vec<i32>> = Vec::new();
        let mut total = 0usize;
        for (i, row) in nums.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                let d = i + j;
                if groups.len() <= d {
                    groups.resize(d + 1, Vec::new());
                }
                groups[d].push(val);
                total += 1;
            }
        }
        let mut ans = Vec::with_capacity(total);
        for vec in groups.into_iter() {
            for v in vec {
                ans.push(v);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-diagonal-order nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([row-vecs (list->vector (map list->vector nums))]
         [rows (vector-length row-vecs)]
         [ht (make-hash)])
    ;; populate hash table with reversed diagonal lists
    (for ([i (in-range (sub1 rows) -1 -1)]) ; i = rows-1 .. 0
      (let* ([row (vector-ref row-vecs i)]
             [cols (vector-length row)])
        (for ([j (in-range cols)])
          (let* ([val (vector-ref row j)]
                 [diag (+ i j)])
            (hash-set! ht diag (cons val (hash-ref ht diag '())))))))
    ;; collect result by traversing diagonals from largest to smallest
    (let loop ((keys (sort (hash-keys ht) >))
               (acc '()))
      (if (null? keys)
          acc
          (let* ([k (car keys)]
                 [lst (hash-ref ht k)])
            (loop (cdr keys)
                  (let inner ((elems lst) (a acc))
                    (if (null? elems)
                        a
                        (inner (cdr elems) (cons (car elems) a)))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_diagonal_order/1]).

-spec find_diagonal_order(Nums :: [[integer()]]) -> [integer()].
find_diagonal_order(Nums) ->
    Map = build_map(Nums, length(Nums) - 1, #{}),
    Keys = lists:sort(maps:keys(Map)),
    Acc = lists:foldl(fun(Key, A) -> maps:get(Key, Map) ++ A end, [], Keys),
    lists:reverse(Acc).

build_map(_Nums, -1, Acc) ->
    Acc;
build_map(Nums, RowIdx, Acc) ->
    Row = lists:nth(RowIdx + 1, Nums),
    NewAcc = add_row(Row, RowIdx, 0, Acc),
    build_map(Nums, RowIdx - 1, NewAcc).

add_row([], _RowIdx, _ColIdx, Acc) ->
    Acc;
add_row([Val | Rest], RowIdx, ColIdx, Acc) ->
    Diag = RowIdx + ColIdx,
    Prev = maps:get(Diag, Acc, []),
    Updated = maps:put(Diag, [Val | Prev], Acc),
    add_row(Rest, RowIdx, ColIdx + 1, Updated).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_diagonal_order(nums :: [[integer]]) :: [integer]
  def find_diagonal_order(nums) do
    groups =
      nums
      |> Enum.with_index()
      |> Enum.reverse()
      |> Enum.reduce(%{}, fn {row_vals, r}, acc ->
        row_vals
        |> Enum.with_index()
        |> Enum.reduce(acc, fn {val, c}, acc2 ->
          d = r + c
          Map.update(acc2, d, [val], fn list -> list ++ [val] end)
        end)
      end)

    groups
    |> Enum.sort_by(fn {k, _} -> k end)
    |> Enum.map(fn {_k, lst} -> lst end)
    |> List.flatten()
  end
end
```
