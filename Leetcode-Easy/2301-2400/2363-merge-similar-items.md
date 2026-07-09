# 2363. Merge Similar Items

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        map<int, int> mp;
        for (const auto& it : items1) {
            mp[it[0]] += it[1];
        }
        for (const auto& it : items2) {
            mp[it[0]] += it[1];
        }
        vector<vector<int>> res;
        res.reserve(mp.size());
        for (const auto& p : mp) {
            res.push_back({p.first, p.second});
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        java.util.TreeMap<Integer, Integer> map = new java.util.TreeMap<>();
        for (int[] item : items1) {
            map.merge(item[0], item[1], Integer::sum);
        }
        for (int[] item : items2) {
            map.merge(item[0], item[1], Integer::sum);
        }
        List<List<Integer>> result = new java.util.ArrayList<>();
        for (java.util.Map.Entry<Integer, Integer> entry : map.entrySet()) {
            List<Integer> pair = new java.util.ArrayList<>(2);
            pair.add(entry.getKey());
            pair.add(entry.getValue());
            result.add(pair);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        weight_map = defaultdict(int)
        for v, w in items1:
            weight_map[v] += w
        for v, w in items2:
            weight_map[v] += w
        return [[v, weight_map[v]] for v in sorted(weight_map)]
```

## Python3

```python
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weight_map = {}
        for v, w in items1:
            weight_map[v] = weight_map.get(v, 0) + w
        for v, w in items2:
            weight_map[v] = weight_map.get(v, 0) + w
        return [[v, weight_map[v]] for v in sorted(weight_map)]
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** mergeSimilarItems(int** items1, int items1Size, int* items1ColSize,
                       int** items2, int items2Size, int* items2ColSize,
                       int* returnSize, int** returnColumnSizes) {
    const int MAX_VAL = 1000;
    int *sum = (int *)calloc(MAX_VAL + 1, sizeof(int));
    
    for (int i = 0; i < items1Size; ++i) {
        int v = items1[i][0];
        int w = items1[i][1];
        sum[v] += w;
    }
    for (int i = 0; i < items2Size; ++i) {
        int v = items2[i][0];
        int w = items2[i][1];
        sum[v] += w;
    }
    
    int cnt = 0;
    for (int v = 1; v <= MAX_VAL; ++v) {
        if (sum[v] > 0) cnt++;
    }
    
    *returnSize = cnt;
    int **res = (int **)malloc(cnt * sizeof(int *));
    *returnColumnSizes = (int *)malloc(cnt * sizeof(int));
    
    int idx = 0;
    for (int v = 1; v <= MAX_VAL; ++v) {
        if (sum[v] > 0) {
            res[idx] = (int *)malloc(2 * sizeof(int));
            res[idx][0] = v;
            res[idx][1] = sum[v];
            (*returnColumnSizes)[idx] = 2;
            idx++;
        }
    }
    
    free(sum);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> MergeSimilarItems(int[][] items1, int[][] items2) {
        var map = new SortedDictionary<int, int>();
        foreach (var item in items1) {
            int value = item[0];
            int weight = item[1];
            if (map.ContainsKey(value))
                map[value] += weight;
            else
                map[value] = weight;
        }
        foreach (var item in items2) {
            int value = item[0];
            int weight = item[1];
            if (map.ContainsKey(value))
                map[value] += weight;
            else
                map[value] = weight;
        }

        var result = new List<IList<int>>();
        foreach (var kvp in map) {
            result.Add(new List<int> { kvp.Key, kvp.Value });
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} items1
 * @param {number[][]} items2
 * @return {number[][]}
 */
var mergeSimilarItems = function(items1, items2) {
    const weightMap = new Map();
    
    const addItems = (items) => {
        for (const [value, weight] of items) {
            weightMap.set(value, (weightMap.get(value) || 0) + weight);
        }
    };
    
    addItems(items1);
    addItems(items2);
    
    const result = Array.from(weightMap.entries())
        .sort((a, b) => a[0] - b[0])
        .map(([value, weight]) => [value, weight]);
    
    return result;
};
```

## Typescript

```typescript
function mergeSimilarItems(items1: number[][], items2: number[][]): number[][] {
    const weightMap = new Map<number, number>();
    for (const [value, weight] of items1) {
        weightMap.set(value, (weightMap.get(value) ?? 0) + weight);
    }
    for (const [value, weight] of items2) {
        weightMap.set(value, (weightMap.get(value) ?? 0) + weight);
    }
    return Array.from(weightMap.entries())
        .sort((a, b) => a[0] - b[0])
        .map(([value, totalWeight]) => [value, totalWeight]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $items1
     * @param Integer[][] $items2
     * @return Integer[][]
     */
    function mergeSimilarItems($items1, $items2) {
        $map = [];

        foreach ($items1 as $item) {
            $value = $item[0];
            $weight = $item[1];
            if (!isset($map[$value])) {
                $map[$value] = 0;
            }
            $map[$value] += $weight;
        }

        foreach ($items2 as $item) {
            $value = $item[0];
            $weight = $item[1];
            if (!isset($map[$value])) {
                $map[$value] = 0;
            }
            $map[$value] += $weight;
        }

        ksort($map, SORT_NUMERIC);

        $result = [];
        foreach ($map as $value => $weight) {
            $result[] = [$value, $weight];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func mergeSimilarItems(_ items1: [[Int]], _ items2: [[Int]]) -> [[Int]] {
        var weightMap = [Int: Int]()
        
        for item in items1 {
            let value = item[0]
            let weight = item[1]
            weightMap[value, default: 0] += weight
        }
        
        for item in items2 {
            let value = item[0]
            let weight = item[1]
            weightMap[value, default: 0] += weight
        }
        
        let sortedValues = weightMap.keys.sorted()
        var result = [[Int]]()
        for v in sortedValues {
            if let w = weightMap[v] {
                result.append([v, w])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mergeSimilarItems(items1: Array<IntArray>, items2: Array<IntArray>): List<List<Int>> {
        val map = java.util.TreeMap<Int, Int>()
        for (item in items1) {
            val value = item[0]
            val weight = item[1]
            map[value] = (map[value] ?: 0) + weight
        }
        for (item in items2) {
            val value = item[0]
            val weight = item[1]
            map[value] = (map[value] ?: 0) + weight
        }
        val result = ArrayList<List<Int>>(map.size)
        for ((value, totalWeight) in map) {
            result.add(listOf(value, totalWeight))
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> mergeSimilarItems(List<List<int>> items1, List<List<int>> items2) {
    final Map<int, int> weightMap = {};
    for (var item in items1) {
      weightMap[item[0]] = (weightMap[item[0]] ?? 0) + item[1];
    }
    for (var item in items2) {
      weightMap[item[0]] = (weightMap[item[0]] ?? 0) + item[1];
    }
    final List<int> values = weightMap.keys.toList()..sort();
    return values.map((v) => [v, weightMap[v]!]).toList();
  }
}
```

## Golang

```go
package main

import "sort"

func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {
	m := make(map[int]int)
	for _, p := range items1 {
		m[p[0]] += p[1]
	}
	for _, p := range items2 {
		m[p[0]] += p[1]
	}
	keys := make([]int, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	res := make([][]int, len(keys))
	for i, v := range keys {
		res[i] = []int{v, m[v]}
	}
	return res
}
```

## Ruby

```ruby
def merge_similar_items(items1, items2)
  sums = Hash.new(0)
  items1.each { |value, weight| sums[value] += weight }
  items2.each { |value, weight| sums[value] += weight }
  sums.sort.map { |value, total_weight| [value, total_weight] }
end
```

## Scala

```scala
object Solution {
    def mergeSimilarItems(items1: Array[Array[Int]], items2: Array[Array[Int]]): List[List[Int]] = {
        val weightMap = scala.collection.mutable.Map[Int, Int]()
        for (item <- items1) {
            val v = item(0)
            val w = item(1)
            weightMap(v) = weightMap.getOrElse(v, 0) + w
        }
        for (item <- items2) {
            val v = item(0)
            val w = item(1)
            weightMap(v) = weightMap.getOrElse(v, 0) + w
        }
        weightMap.toSeq.sortBy(_._1).map { case (v, w) => List(v, w) }.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge_similar_items(items1: Vec<Vec<i32>>, items2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        use std::collections::BTreeMap;
        let mut map = BTreeMap::new();
        for item in items1.iter() {
            let v = item[0];
            let w = item[1];
            *map.entry(v).or_insert(0) += w;
        }
        for item in items2.iter() {
            let v = item[0];
            let w = item[1];
            *map.entry(v).or_insert(0) += w;
        }
        map.into_iter().map(|(v, w)| vec![v, w]).collect()
    }
}
```

## Racket

```racket
(define/contract (merge-similar-items items1 items2)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let ([ht (make-hash)])
    (for-each
     (lambda (pair)
       (define v (first pair))
       (define w (second pair))
       (hash-set! ht v (+ w (hash-ref ht v 0))))
     items1)
    (for-each
     (lambda (pair)
       (define v (first pair))
       (define w (second pair))
       (hash-set! ht v (+ w (hash-ref ht v 0))))
     items2)
    (let* ([sorted-keys (sort (hash-keys ht) <)])
      (map (lambda (k) (list k (hash-ref ht k))) sorted-keys))))
```

## Erlang

```erlang
-module(solution).
-export([merge_similar_items/2]).

-spec merge_similar_items(Items1 :: [[integer()]], Items2 :: [[integer()]]) -> [[integer()]].
merge_similar_items(Items1, Items2) ->
    Map = add_items(add_items(maps:new(), Items1), Items2),
    Sorted = lists:keysort(1, maps:to_list(Map)),
    [ [K, W] || {K, W} <- Sorted ].

add_items(Map, []) -> 
    Map;
add_items(Map, [[V, W] | Rest]) ->
    NewMap = maps:update_with(V,
                               fun(Prev) -> Prev + W end,
                               W,
                               Map),
    add_items(NewMap, Rest).
```

## Elixir

```elixir
defmodule Solution do
  @spec merge_similar_items(items1 :: [[integer]], items2 :: [[integer]]) :: [[integer]]
  def merge_similar_items(items1, items2) do
    items = items1 ++ items2

    aggregated =
      Enum.reduce(items, %{}, fn [value, weight], acc ->
        Map.update(acc, value, weight, &(&1 + weight))
      end)

    aggregated
    |> Enum.map(fn {value, total_weight} -> [value, total_weight] end)
    |> Enum.sort_by(fn [value, _] -> value end)
  end
end
```
