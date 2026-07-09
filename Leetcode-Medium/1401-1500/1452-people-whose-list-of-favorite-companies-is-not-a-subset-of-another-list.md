# 1452. People Whose List of Favorite Companies Is Not a Subset of Another List

## Cpp

```cpp
class Solution {
public:
    vector<int> peopleIndexes(vector<vector<string>>& favoriteCompanies) {
        int n = favoriteCompanies.size();
        vector<unordered_set<string>> sets(n);
        for (int i = 0; i < n; ++i) {
            sets[i] = unordered_set<string>(favoriteCompanies[i].begin(), favoriteCompanies[i].end());
        }
        vector<int> ans;
        for (int i = 0; i < n; ++i) {
            bool isSubset = false;
            for (int j = 0; j < n && !isSubset; ++j) {
                if (i == j) continue;
                if (favoriteCompanies[i].size() > favoriteCompanies[j].size()) continue;
                const auto& setJ = sets[j];
                bool allPresent = true;
                for (const string& comp : favoriteCompanies[i]) {
                    if (setJ.find(comp) == setJ.end()) {
                        allPresent = false;
                        break;
                    }
                }
                if (allPresent) isSubset = true;
            }
            if (!isSubset) ans.push_back(i);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        int n = favoriteCompanies.size();
        List<Set<String>> sets = new ArrayList<>(n);
        for (List<String> list : favoriteCompanies) {
            sets.add(new HashSet<>(list));
        }
        boolean[] isSubset = new boolean[n];
        for (int i = 0; i < n; i++) {
            Set<String> setI = sets.get(i);
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                Set<String> setJ = sets.get(j);
                if (setI.size() > setJ.size()) continue;
                if (setJ.containsAll(setI)) {
                    isSubset[i] = true;
                    break;
                }
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!isSubset[i]) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        n = len(favoriteCompanies)
        sets = [set(comp) for comp in favoriteCompanies]
        # indices sorted by descending size
        order = sorted(range(n), key=lambda i: -len(sets[i]))
        is_subset = [False] * n

        for pos_i, i in enumerate(order):
            if is_subset[i]:
                continue
            # compare only with larger (or equal) sets that appear earlier in order
            for pos_j in range(pos_i):
                j = order[pos_j]
                if sets[i].issubset(sets[j]):
                    is_subset[i] = True
                    break

        return [i for i in range(n) if not is_subset[i]]
```

## Python3

```python
from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        sets = [set(comp) for comp in favoriteCompanies]
        lengths = [len(s) for s in sets]

        result = []
        for i in range(n):
            subset = False
            for j in range(n):
                if i == j or lengths[j] < lengths[i]:
                    continue
                if sets[i].issubset(sets[j]):
                    subset = True
                    break
            if not subset:
                result.append(i)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int cmpStr(const void *a, const void *b) {
    const char *const *pa = (const char *const *)a;
    const char *const *pb = (const char *const *)b;
    return strcmp(*pa, *pb);
}

struct List {
    int idx;
    int size;
    char **arr;
};

static bool isSubset(const struct List *small, const struct List *big) {
    if (small->size > big->size) return false;
    int i = 0, j = 0;
    while (i < small->size && j < big->size) {
        int cmp = strcmp(small->arr[i], big->arr[j]);
        if (cmp == 0) {
            ++i; ++j;
        } else if (cmp > 0) {
            ++j;
        } else {
            return false;
        }
    }
    return i == small->size;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* peopleIndexes(char*** favoriteCompanies, int favoriteCompaniesSize, int* favoriteCompaniesColSize, int* returnSize) {
    struct List *lists = (struct List *)malloc(favoriteCompaniesSize * sizeof(struct List));
    for (int i = 0; i < favoriteCompaniesSize; ++i) {
        int sz = favoriteCompaniesColSize[i];
        char **arr = (char **)malloc(sz * sizeof(char *));
        for (int j = 0; j < sz; ++j) {
            arr[j] = favoriteCompanies[i][j];
        }
        qsort(arr, sz, sizeof(char *), cmpStr);
        lists[i].idx = i;
        lists[i].size = sz;
        lists[i].arr = arr;
    }

    bool *subsetFlag = (bool *)calloc(favoriteCompaniesSize, sizeof(bool));

    for (int i = 0; i < favoriteCompaniesSize; ++i) {
        for (int j = 0; j < favoriteCompaniesSize; ++j) {
            if (i == j) continue;
            if (lists[i].size > lists[j].size) continue;
            if (isSubset(&lists[i], &lists[j])) {
                subsetFlag[i] = true;
                break;
            }
        }
    }

    int *result = (int *)malloc(favoriteCompaniesSize * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < favoriteCompaniesSize; ++i) {
        if (!subsetFlag[i]) {
            result[cnt++] = i;
        }
    }

    *returnSize = cnt;

    for (int i = 0; i < favoriteCompaniesSize; ++i) {
        free(lists[i].arr);
    }
    free(lists);
    free(subsetFlag);

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> PeopleIndexes(IList<IList<string>> favoriteCompanies) {
        int n = favoriteCompanies.Count;
        var sets = new List<HashSet<string>>(n);
        for (int i = 0; i < n; i++) {
            sets.Add(new HashSet<string>(favoriteCompanies[i]));
        }

        var result = new List<int>();
        for (int i = 0; i < n; i++) {
            bool isSubset = false;
            for (int j = 0; j < n && !isSubset; j++) {
                if (i == j) continue;
                if (sets[j].Count < sets[i].Count) continue;

                bool allContain = true;
                foreach (var comp in sets[i]) {
                    if (!sets[j].Contains(comp)) {
                        allContain = false;
                        break;
                    }
                }
                if (allContain) isSubset = true;
            }
            if (!isSubset) result.Add(i);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} favoriteCompanies
 * @return {number[]}
 */
var peopleIndexes = function(favoriteCompanies) {
    const n = favoriteCompanies.length;
    const sets = favoriteCompanies.map(arr => new Set(arr));
    const result = [];
    
    for (let i = 0; i < n; i++) {
        let isSubset = false;
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            if (favoriteCompanies[i].length > favoriteCompanies[j].length) continue;
            
            const setJ = sets[j];
            let allPresent = true;
            for (const comp of favoriteCompanies[i]) {
                if (!setJ.has(comp)) {
                    allPresent = false;
                    break;
                }
            }
            if (allPresent) {
                isSubset = true;
                break;
            }
        }
        if (!isSubset) result.push(i);
    }
    
    return result;
};
```

## Typescript

```typescript
function peopleIndexes(favoriteCompanies: string[][]): number[] {
    const n = favoriteCompanies.length;
    const sets: Set<string>[] = favoriteCompanies.map(arr => new Set(arr));
    const isSubset = new Array(n).fill(false);

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            if (sets[i].size > sets[j].size) continue;

            let subset = true;
            for (const comp of sets[i]) {
                if (!sets[j].has(comp)) {
                    subset = false;
                    break;
                }
            }

            if (subset) {
                isSubset[i] = true;
                break;
            }
        }
    }

    const result: number[] = [];
    for (let i = 0; i < n; i++) {
        if (!isSubset[i]) result.push(i);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $favoriteCompanies
     * @return Integer[]
     */
    function peopleIndexes($favoriteCompanies) {
        $n = count($favoriteCompanies);
        // Build hash sets for fast lookup
        $sets = [];
        foreach ($favoriteCompanies as $list) {
            $set = [];
            foreach ($list as $c) {
                $set[$c] = true;
            }
            $sets[] = $set;
        }

        $result = [];
        for ($i = 0; $i < $n; $i++) {
            $isSubset = false;
            $sizeI = count($favoriteCompanies[$i]);
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                $sizeJ = count($favoriteCompanies[$j]);
                if ($sizeI > $sizeJ) continue; // cannot be subset
                $subset = true;
                foreach ($favoriteCompanies[$i] as $c) {
                    if (!isset($sets[$j][$c])) {
                        $subset = false;
                        break;
                    }
                }
                if ($subset) {
                    $isSubset = true;
                    break;
                }
            }
            if (!$isSubset) {
                $result[] = $i;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func peopleIndexes(_ favoriteCompanies: [[String]]) -> [Int] {
        let n = favoriteCompanies.count
        var sets = [Set<String>]()
        for list in favoriteCompanies {
            sets.append(Set(list))
        }
        var result = [Int]()
        for i in 0..<n {
            var isSubset = false
            for j in 0..<n where i != j {
                if sets[i].isSubset(of: sets[j]) {
                    isSubset = true
                    break
                }
            }
            if !isSubset {
                result.append(i)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun peopleIndexes(favoriteCompanies: List<List<String>>): List<Int> {
        val n = favoriteCompanies.size
        val sets = Array(n) { idx -> favoriteCompanies[idx].toHashSet() }
        val result = mutableListOf<Int>()
        for (i in 0 until n) {
            var isSubset = false
            for (j in 0 until n) {
                if (i == j) continue
                if (sets[i].size > sets[j].size) continue
                var allContain = true
                for (c in sets[i]) {
                    if (!sets[j].contains(c)) {
                        allContain = false
                        break
                    }
                }
                if (allContain) {
                    isSubset = true
                    break
                }
            }
            if (!isSubset) result.add(i)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> peopleIndexes(List<List<String>> favoriteCompanies) {
    int n = favoriteCompanies.length;
    List<Set<String>> sets = [];
    for (var list in favoriteCompanies) {
      sets.add(list.toSet());
    }

    List<bool> isSubset = List.filled(n, false);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (i == j) continue;
        if (sets[i].length > sets[j].length) continue;
        if (sets[j].containsAll(sets[i])) {
          isSubset[i] = true;
          break;
        }
      }
    }

    List<int> result = [];
    for (int i = 0; i < n; i++) {
      if (!isSubset[i]) result.add(i);
    }
    return result;
  }
}
```

## Golang

```go
func peopleIndexes(favoriteCompanies [][]string) []int {
    n := len(favoriteCompanies)
    // Build a map (set) for each person's favorite companies
    sets := make([]map[string]struct{}, n)
    for i, list := range favoriteCompanies {
        m := make(map[string]struct{}, len(list))
        for _, c := range list {
            m[c] = struct{}{}
        }
        sets[i] = m
    }

    result := []int{}
    for i := 0; i < n; i++ {
        isSubset := false
        for j := 0; j < n && !isSubset; j++ {
            if i == j {
                continue
            }
            // A subset must have size <= the superset's size
            if len(favoriteCompanies[i]) > len(favoriteCompanies[j]) {
                continue
            }
            allPresent := true
            for _, c := range favoriteCompanies[i] {
                if _, ok := sets[j][c]; !ok {
                    allPresent = false
                    break
                }
            }
            if allPresent {
                isSubset = true
            }
        }
        if !isSubset {
            result = append(result, i)
        }
    }
    return result
}
```

## Ruby

```ruby
require 'set'

def people_indexes(favorite_companies)
  sets = favorite_companies.map { |arr| arr.to_set }
  result = []
  sets.each_with_index do |s_i, i|
    is_subset = false
    sets.each_with_index do |s_j, j|
      next if i == j
      next if s_i.size > s_j.size
      if s_i.subset?(s_j)
        is_subset = true
        break
      end
    end
    result << i unless is_subset
  end
  result
end
```

## Scala

```scala
object Solution {
    def peopleIndexes(favoriteCompanies: List[List[String]]): List[Int] = {
        val n = favoriteCompanies.length
        val sets = favoriteCompanies.map(_.toSet)
        val sizes = favoriteCompanies.map(_.size)

        val res = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 0 until n) {
            var subset = false
            for (j <- 0 until n if i != j && !subset) {
                if (sizes(i) <= sizes(j) && sets(i).subsetOf(sets(j))) {
                    subset = true
                }
            }
            if (!subset) res += i
        }
        res.toList
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn people_indexes(favorite_companies: Vec<Vec<String>>) -> Vec<i32> {
        let n = favorite_companies.len();
        // Convert each list to a HashSet for O(1) lookups
        let sets: Vec<HashSet<String>> = favorite_companies
            .iter()
            .map(|list| list.iter().cloned().collect())
            .collect();

        let mut result = Vec::new();

        for i in 0..n {
            let mut is_subset = false;
            for j in 0..n {
                if i == j {
                    continue;
                }
                // If i's set is larger, it cannot be a subset of j
                if sets[i].len() > sets[j].len() {
                    continue;
                }
                // Check whether all elements of i are contained in j
                if sets[i].iter().all(|c| sets[j].contains(c)) {
                    is_subset = true;
                    break;
                }
            }
            if !is_subset {
                result.push(i as i32);
            }
        }

        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/set)

(define/contract (people-indexes favoriteCompanies)
  (-> (listof (listof string?)) (listof exact-integer?))
  (let* ([sets (map list->set favoriteCompanies)]
         [n (length sets)])
    (for/list ([i (in-range n)]
               #:when (not
                       (let ([si (list-ref sets i)])
                         (for/or ([j (in-range n)]
                                  #:when (not (= i j)))
                           (let ([sj (list-ref sets j)])
                             (and (<= (set-count si) (set-count sj))
                                  (set-subset? si sj)))))))
      i)))
```

## Erlang

```erlang
-spec people_indexes(FavoriteCompanies :: [[unicode:unicode_binary()]]) -> [integer()].
people_indexes(FavoriteCompanies) ->
    Indexed = lists:zip(lists:seq(0, length(FavoriteCompanies) - 1), FavoriteCompanies),
    SortedLists = [{Idx, lists:sort(List)} || {Idx, List} <- Indexed],
    SubsetFlags = [is_subset_of_any(Idx, List, SortedLists) ||
        {Idx, List} <- SortedLists],
    Result = [Idx ||
        {Idx, IsSubset} <- lists:zip(lists:seq(0, length(FavoriteCompanies) - 1), SubsetFlags),
        not IsSubset],
    Result.

is_subset_of_any(Idx, List, SortedLists) ->
    lists:any(
        fun({Jdx, L2}) ->
            Jdx =/= Idx andalso is_subset(List, L2)
        end,
        SortedLists).

is_subset([], _) -> true;
is_subset(_, []) -> false;
is_subset([H|T1] = A, [H2|T2] = B) ->
    case H =< H2 of
        true when H == H2 -> is_subset(T1, T2);
        true -> false;
        false -> is_subset(A, T2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec people_indexes(favorite_companies :: [[String.t]]) :: [integer]
  def people_indexes(favorite_companies) do
    indexed_sets =
      favorite_companies
      |> Enum.with_index()
      |> Enum.map(fn {list, idx} -> {idx, MapSet.new(list)} end)

    for {i, set_i} <- indexed_sets,
        not Enum.any?(indexed_sets, fn {j, set_j} ->
          i != j and MapSet.subset?(set_i, set_j)
        end),
        do: i
  end
end
```
