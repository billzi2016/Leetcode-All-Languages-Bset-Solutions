# 1282. Group the People Given the Group Size They Belong To

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        unordered_map<int, vector<int>> cur;
        vector<vector<int>> ans;
        for (int i = 0; i < (int)groupSizes.size(); ++i) {
            int sz = groupSizes[i];
            auto &vec = cur[sz];
            vec.push_back(i);
            if ((int)vec.size() == sz) {
                ans.push_back(vec);
                vec.clear();
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> ans = new ArrayList<>();
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < groupSizes.length; i++) {
            int sz = groupSizes[i];
            List<Integer> cur = map.computeIfAbsent(sz, k -> new ArrayList<>());
            cur.add(i);
            if (cur.size() == sz) {
                ans.add(new ArrayList<>(cur));
                cur.clear();
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        buckets = defaultdict(list)
        ans = []
        for i, sz in enumerate(groupSizes):
            buckets[sz].append(i)
            if len(buckets[sz]) == sz:
                ans.append(buckets[sz])
                buckets[sz] = []
        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        temp = defaultdict(list)
        ans = []
        for i, sz in enumerate(groupSizes):
            temp[sz].append(i)
            if len(temp[sz]) == sz:
                ans.append(temp[sz][:])
                temp[sz].clear()
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *arr;
    int len;
} Bucket;

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** groupThePeople(int* groupSizes, int groupSizesSize, int* returnSize, int*** returnColumnSizes) {
    // Allocate buckets for each possible size (1..groupSizesSize)
    Bucket *buckets = (Bucket *)malloc((groupSizesSize + 1) * sizeof(Bucket));
    for (int s = 1; s <= groupSizesSize; ++s) {
        buckets[s].arr = (int *)malloc(s * sizeof(int));
        buckets[s].len = 0;
    }

    // Result containers
    int **groups = (int **)malloc(groupSizesSize * sizeof(int *));
    int *colSizes = (int *)malloc(groupSizesSize * sizeof(int));
    int resCount = 0;

    for (int i = 0; i < groupSizesSize; ++i) {
        int sz = groupSizes[i];
        Bucket *b = &buckets[sz];
        b->arr[b->len++] = i;
        if (b->len == sz) {
            groups[resCount] = (int *)malloc(sz * sizeof(int));
            memcpy(groups[resCount], b->arr, sz * sizeof(int));
            colSizes[resCount] = sz;
            ++resCount;
            b->len = 0; // reset for next group of this size
        }
    }

    // Clean up bucket memory (optional)
    for (int s = 1; s <= groupSizesSize; ++s) {
        free(buckets[s].arr);
    }
    free(buckets);

    *returnSize = resCount;
    *returnColumnSizes = colSizes;
    return groups;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> GroupThePeople(int[] groupSizes) {
        var result = new List<IList<int>>();
        var map = new Dictionary<int, List<int>>();
        
        for (int i = 0; i < groupSizes.Length; i++) {
            int size = groupSizes[i];
            if (!map.TryGetValue(size, out var list)) {
                list = new List<int>();
                map[size] = list;
            }
            list.Add(i);
            if (list.Count == size) {
                result.Add(new List<int>(list));
                list.Clear();
            }
        }
        
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
var groupThePeople = function(groupSizes) {
    const map = new Map(); // size -> current members list
    const result = [];
    
    for (let i = 0; i < groupSizes.length; i++) {
        const sz = groupSizes[i];
        if (!map.has(sz)) {
            map.set(sz, []);
        }
        const bucket = map.get(sz);
        bucket.push(i);
        if (bucket.length === sz) {
            result.push(bucket.slice()); // add a copy as a completed group
            map.set(sz, []); // reset for next group of same size
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function groupThePeople(groupSizes: number[]): number[][] {
    const groupsMap = new Map<number, number[]>();
    const result: number[][] = [];

    for (let i = 0; i < groupSizes.length; i++) {
        const size = groupSizes[i];
        const curGroup = groupsMap.get(size) ?? [];
        curGroup.push(i);
        if (curGroup.length === size) {
            result.push(curGroup);
            groupsMap.delete(size);
        } else {
            groupsMap.set(size, curGroup);
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $groupSizes
     * @return Integer[][]
     */
    function groupThePeople($groupSizes) {
        $buckets = [];
        $result = [];

        foreach ($groupSizes as $i => $size) {
            if (!isset($buckets[$size])) {
                $buckets[$size] = [];
            }
            $buckets[$size][] = $i;
            if (count($buckets[$size]) === $size) {
                $result[] = $buckets[$size];
                $buckets[$size] = [];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func groupThePeople(_ groupSizes: [Int]) -> [[Int]] {
        var result = [[Int]]()
        var buckets = [Int: [Int]]()
        
        for (person, size) in groupSizes.enumerated() {
            var current = buckets[size] ?? []
            current.append(person)
            if current.count == size {
                result.append(current)
                buckets[size] = []
            } else {
                buckets[size] = current
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun groupThePeople(groupSizes: IntArray): List<List<Int>> {
        val map = HashMap<Int, MutableList<Int>>()
        val result = mutableListOf<List<Int>>()
        for (i in groupSizes.indices) {
            val size = groupSizes[i]
            val cur = map.getOrPut(size) { mutableListOf() }
            cur.add(i)
            if (cur.size == size) {
                result.add(ArrayList(cur))
                cur.clear()
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> groupThePeople(List<int> groupSizes) {
    final Map<int, List<int>> buckets = {};
    final List<List<int>> result = [];

    for (int i = 0; i < groupSizes.length; i++) {
      int size = groupSizes[i];
      List<int> bucket = buckets.putIfAbsent(size, () => []);
      bucket.add(i);
      if (bucket.length == size) {
        result.add(List<int>.from(bucket));
        bucket.clear();
      }
    }

    return result;
  }
}
```

## Golang

```go
func groupThePeople(groupSizes []int) [][]int {
    groups := make([][]int, 0)
    bucketMap := make(map[int][]int)

    for i, sz := range groupSizes {
        bucketMap[sz] = append(bucketMap[sz], i)
        if len(bucketMap[sz]) == sz {
            groups = append(groups, bucketMap[sz])
            bucketMap[sz] = nil
        }
    }

    return groups
}
```

## Ruby

```ruby
# @param {Integer[]} group_sizes
# @return {Integer[][]}
def group_the_people(group_sizes)
  groups_by_size = Hash.new { |h, k| h[k] = [] }
  result = []

  group_sizes.each_with_index do |size, idx|
    bucket = groups_by_size[size]
    bucket << idx
    if bucket.size == size
      result << bucket.clone
      bucket.clear
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  def groupThePeople(groupSizes: Array[Int]): List[List[Int]] = {
    import scala.collection.mutable

    val pending = mutable.Map.empty[Int, mutable.ListBuffer[Int]]
    val result = mutable.ListBuffer.empty[List[Int]]

    for (i <- groupSizes.indices) {
      val sz = groupSizes(i)
      val buf = pending.getOrElseUpdate(sz, mutable.ListBuffer.empty[Int])
      buf += i
      if (buf.size == sz) {
        result += buf.toList
        buf.clear()
      }
    }

    result.toList
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut buckets: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut result: Vec<Vec<i32>> = Vec::new();

        for (i, &size) in group_sizes.iter().enumerate() {
            let entry = buckets.entry(size).or_insert_with(Vec::new);
            entry.push(i as i32);
            if entry.len() == size as usize {
                result.push(entry.clone());
                entry.clear();
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (group-the-people groupSizes)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let ((h (make-hash))
        (ans '()))
    (for ([i (in-range (length groupSizes))])
      (let* ((size (list-ref groupSizes i))
             (cur (hash-ref h size '())))
        (define new-list (cons i cur))
        (if (= (length new-list) size)
            (begin
              (set! ans (cons (reverse new-list) ans))
              (hash-set! h size '()))
            (hash-set! h size new-list))))
    (reverse ans)))
```

## Erlang

```erlang
-module(solution).
-export([group_the_people/1]).

-spec group_the_people(GroupSizes :: [integer()]) -> [[integer()]].
group_the_people(GroupSizes) ->
    {_, GroupsRev} = lists:foldl(
        fun({Size, Idx}, {Map, Acc}) ->
            Cur = maps:get(Size, Map, []),
            NewCur = [Idx | Cur],
            case length(NewCur) of
                Size ->
                    Group = lists:reverse(NewCur),
                    {maps:remove(Size, Map), [Group | Acc]};
                _ ->
                    {maps:put(Size, NewCur, Map), Acc}
            end
        end,
        {#{}, []},
        lists:zip(GroupSizes, lists:seq(0, length(GroupSizes) - 1))
    ),
    lists:reverse(GroupsRev).
```

## Elixir

```elixir
defmodule Solution do
  @spec group_the_people(group_sizes :: [integer]) :: [[integer]]
  def group_the_people(group_sizes) do
    {groups_rev, _} =
      Enum.reduce(Enum.with_index(group_sizes), {[], %{}}, fn {size, idx},
                                                             {acc, map} ->
        cur = Map.get(map, size, [])
        new_cur = [idx | cur]

        if length(new_cur) == size do
          group = Enum.reverse(new_cur)
          {[group | acc], Map.delete(map, size)}
        else
          {acc, Map.put(map, size, new_cur)}
        end
      end)

    Enum.reverse(groups_rev)
  end
end
```
