# 1331. Rank Transform of an Array

## Cpp

```cpp
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        if (arr.empty()) return {};
        vector<int> sorted = arr;
        sort(sorted.begin(), sorted.end());
        unordered_map<int, int> rank;
        int r = 1;
        for (int i = 0; i < (int)sorted.size(); ++i) {
            if (i == 0 || sorted[i] != sorted[i - 1]) {
                rank[sorted[i]] = r++;
            }
        }
        vector<int> result(arr.size());
        for (int i = 0; i < (int)arr.size(); ++i) {
            result[i] = rank[arr[i]];
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        if (arr == null || arr.length == 0) {
            return new int[0];
        }
        int n = arr.length;
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int val : sorted) {
            if (!rankMap.containsKey(val)) {
                rankMap.put(val, rankMap.size() + 1);
            }
        }
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = rankMap.get(arr[i]);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        # Get sorted unique values and assign ranks starting from 1
        rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        # Transform original array using the rank mapping
        return [rank[x] for x in arr]
```

## Python3

```python
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        sorted_unique = sorted(set(arr))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        return [rank[x] for x in arr]
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/* binary search for value in sorted unique array */
static int find_rank(int *uniq, int uniqSize, int target) {
    int left = 0, right = uniqSize - 1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (uniq[mid] == target) return mid + 1;          // rank is index+1
        else if (uniq[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1; // should never happen
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* arrayRankTransform(int* arr, int arrSize, int* returnSize) {
    if (arrSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    int *copy = (int *)malloc(arrSize * sizeof(int));
    memcpy(copy, arr, arrSize * sizeof(int));

    qsort(copy, arrSize, sizeof(int), cmp_int);

    // build unique sorted values
    int *uniq = (int *)malloc(arrSize * sizeof(int));
    int uniqCount = 0;
    for (int i = 0; i < arrSize; ++i) {
        if (i == 0 || copy[i] != copy[i - 1]) {
            uniq[uniqCount++] = copy[i];
        }
    }

    int *result = (int *)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; ++i) {
        result[i] = find_rank(uniq, uniqCount, arr[i]);
    }

    free(copy);
    free(uniq);

    *returnSize = arrSize;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] ArrayRankTransform(int[] arr) {
        int n = arr.Length;
        if (n == 0) return new int[0];

        int[] sorted = (int[])arr.Clone();
        Array.Sort(sorted);

        var rankMap = new Dictionary<int, int>();
        int rank = 1;
        foreach (int val in sorted) {
            if (!rankMap.ContainsKey(val)) {
                rankMap[val] = rank++;
            }
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = rankMap[arr[i]];
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    if (arr.length === 0) return [];
    const uniqueSorted = Array.from(new Set(arr)).sort((a, b) => a - b);
    const rankMap = new Map();
    for (let i = 0; i < uniqueSorted.length; i++) {
        rankMap.set(uniqueSorted[i], i + 1);
    }
    return arr.map(val => rankMap.get(val));
};
```

## Typescript

```typescript
function arrayRankTransform(arr: number[]): number[] {
    const uniqueSorted = Array.from(new Set(arr)).sort((a, b) => a - b);
    const rankMap = new Map<number, number>();
    for (let i = 0; i < uniqueSorted.length; i++) {
        rankMap.set(uniqueSorted[i], i + 1);
    }
    return arr.map(v => rankMap.get(v)!);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function arrayRankTransform($arr) {
        $n = count($arr);
        if ($n === 0) {
            return [];
        }
        $sorted = $arr;
        sort($sorted, SORT_NUMERIC);
        $rankMap = [];
        $rank = 1;
        foreach ($sorted as $val) {
            if (!array_key_exists($val, $rankMap)) {
                $rankMap[$val] = $rank++;
            }
        }
        $result = [];
        foreach ($arr as $val) {
            $result[] = $rankMap[$val];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func arrayRankTransform(_ arr: [Int]) -> [Int] {
        if arr.isEmpty { return [] }
        var unique = Array(Set(arr))
        unique.sort()
        var rankMap = [Int:Int]()
        for (i, val) in unique.enumerated() {
            rankMap[val] = i + 1
        }
        return arr.map { rankMap[$0]! }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        if (arr.isEmpty()) return intArrayOf()
        val sorted = arr.clone()
        java.util.Arrays.sort(sorted)
        val rankMap = HashMap<Int, Int>()
        var rank = 1
        for (v in sorted) {
            if (!rankMap.containsKey(v)) {
                rankMap[v] = rank++
            }
        }
        val result = IntArray(arr.size)
        for (i in arr.indices) {
            result[i] = rankMap[arr[i]]!!
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> arrayRankTransform(List<int> arr) {
    if (arr.isEmpty) return [];
    List<int> sorted = List.from(arr);
    sorted.sort();
    Map<int, int> rankMap = {};
    int rank = 1;
    for (int num in sorted) {
      if (!rankMap.containsKey(num)) {
        rankMap[num] = rank++;
      }
    }
    return arr.map((num) => rankMap[num]!).toList();
  }
}
```

## Golang

```go
import "sort"

func arrayRankTransform(arr []int) []int {
	n := len(arr)
	if n == 0 {
		return []int{}
	}
	sorted := make([]int, n)
	copy(sorted, arr)
	sort.Ints(sorted)

	rankMap := make(map[int]int, n)
	rank := 1
	for i, v := range sorted {
		if i == 0 || v != sorted[i-1] {
			rankMap[v] = rank
			rank++
		}
	}

	res := make([]int, n)
	for i, v := range arr {
		res[i] = rankMap[v]
	}
	return res
}
```

## Ruby

```ruby
def array_rank_transform(arr)
  ranks = {}
  arr.uniq.sort.each_with_index { |v, i| ranks[v] = i + 1 }
  arr.map { |v| ranks[v] }
end
```

## Scala

```scala
object Solution {
    def arrayRankTransform(arr: Array[Int]): Array[Int] = {
        if (arr.isEmpty) return arr
        val sortedDistinct = arr.distinct.sorted
        val rankMap = scala.collection.mutable.HashMap[Int, Int]()
        var rank = 1
        for (v <- sortedDistinct) {
            rankMap(v) = rank
            rank += 1
        }
        arr.map(rankMap)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        if arr.is_empty() {
            return vec![];
        }
        let mut sorted = arr.clone();
        sorted.sort_unstable();
        sorted.dedup();

        use std::collections::HashMap;
        let mut rank_map: HashMap<i32, i32> = HashMap::with_capacity(sorted.len());
        for (i, &v) in sorted.iter().enumerate() {
            rank_map.insert(v, (i as i32) + 1);
        }

        arr.iter()
            .map(|&v| *rank_map.get(&v).unwrap())
            .collect()
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (array-rank-transform arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([unique-sorted (sort (remove-duplicates arr) <)]
         [rank-hash (make-hash)])
    (for ([val unique-sorted] [i (in-naturals 1)])
      (hash-set! rank-hash val i))
    (map (lambda (x) (hash-ref rank-hash x)) arr)))
```

## Erlang

```erlang
-spec array_rank_transform([integer()]) -> [integer()].
array_rank_transform(Arr) ->
    Sorted = lists:sort(Arr),
    Map = build_map(Sorted, #{}, undefined, 0),
    [maps:get(X, Map) || X <- Arr].

build_map([], AccMap, _Prev, _Rank) ->
    AccMap;
build_map([H|T], AccMap, Prev, Rank) ->
    NewRank = case Prev of
        undefined -> Rank + 1;
        _ when H =/= Prev -> Rank + 1;
        _ -> Rank
    end,
    NewAccMap = maps:put(H, NewRank, AccMap),
    build_map(T, NewAccMap, H, NewRank).
```

## Elixir

```elixir
defmodule Solution do
  @spec array_rank_transform(arr :: [integer]) :: [integer]
  def array_rank_transform(arr) do
    ranks =
      arr
      |> Enum.uniq()
      |> Enum.sort()
      |> Enum.with_index(1)
      |> Map.new(fn {value, rank} -> {value, rank} end)

    Enum.map(arr, fn v -> Map.fetch!(ranks, v) end)
  end
end
```
