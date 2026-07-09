# 2295. Replace Elements in an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> arrayChange(vector<int>& nums, vector<vector<int>>& operations) {
        unordered_map<int,int> pos;
        pos.reserve(nums.size()*2);
        for (int i = 0; i < (int)nums.size(); ++i) {
            pos[nums[i]] = i;
        }
        for (const auto& op : operations) {
            int oldVal = op[0];
            int newVal = op[1];
            int idx = pos[oldVal];
            nums[idx] = newVal;
            pos.erase(oldVal);
            pos[newVal] = idx;
        }
        return nums;
    }
};
```

## Java

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] arrayChange(int[] nums, int[][] operations) {
        Map<Integer, Integer> pos = new HashMap<>(nums.length * 2);
        for (int i = 0; i < nums.length; i++) {
            pos.put(nums[i], i);
        }
        for (int[] op : operations) {
            int oldVal = op[0];
            int newVal = op[1];
            int idx = pos.get(oldVal);
            nums[idx] = newVal;
            pos.remove(oldVal);
            pos.put(newVal, idx);
        }
        return nums;
    }
}
```

## Python

```python
class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        pos = {v: i for i, v in enumerate(nums)}
        for old, new in operations:
            idx = pos.pop(old)
            nums[idx] = new
            pos[new] = idx
        return nums
```

## Python3

```python
from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {num: i for i, num in enumerate(nums)}
        for old, new in operations:
            idx = pos.pop(old)
            nums[idx] = new
            pos[new] = idx
        return nums
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* arrayChange(int* nums, int numsSize, int** operations, int operationsSize, int* operationsColSize, int* returnSize){
    const int MAX_VAL = 1000000;
    int *pos = (int*)malloc((MAX_VAL + 1) * sizeof(int));
    for (int i = 0; i <= MAX_VAL; ++i) pos[i] = -1;
    
    for (int i = 0; i < numsSize; ++i){
        pos[nums[i]] = i;
    }
    
    for (int i = 0; i < operationsSize; ++i){
        int oldVal = operations[i][0];
        int newVal = operations[i][1];
        int idx = pos[oldVal];
        nums[idx] = newVal;
        pos[newVal] = idx;
        pos[oldVal] = -1;
    }
    
    free(pos);
    *returnSize = numsSize;
    return nums;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] ArrayChange(int[] nums, int[][] operations) {
        var pos = new Dictionary<int, int>(nums.Length);
        for (int i = 0; i < nums.Length; i++) {
            pos[nums[i]] = i;
        }

        foreach (var op in operations) {
            int oldVal = op[0];
            int newVal = op[1];
            int idx = pos[oldVal];
            nums[idx] = newVal;
            pos.Remove(oldVal);
            pos[newVal] = idx;
        }

        return nums;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} operations
 * @return {number[]}
 */
var arrayChange = function(nums, operations) {
    const indexMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        indexMap.set(nums[i], i);
    }
    for (const [oldVal, newVal] of operations) {
        const idx = indexMap.get(oldVal);
        nums[idx] = newVal;
        indexMap.delete(oldVal);
        indexMap.set(newVal, idx);
    }
    return nums;
};
```

## Typescript

```typescript
function arrayChange(nums: number[], operations: number[][]): number[] {
    const indexMap = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        indexMap.set(nums[i], i);
    }
    for (const [oldVal, newVal] of operations) {
        const idx = indexMap.get(oldVal)!;
        nums[idx] = newVal;
        indexMap.delete(oldVal);
        indexMap.set(newVal, idx);
    }
    return nums;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $operations
     * @return Integer[]
     */
    function arrayChange($nums, $operations) {
        // map value => index
        $pos = [];
        foreach ($nums as $i => $v) {
            $pos[$v] = $i;
        }

        foreach ($operations as $op) {
            $old = $op[0];
            $new = $op[1];
            $idx = $pos[$old];
            // replace in nums
            $nums[$idx] = $new;
            // update map
            unset($pos[$old]);
            $pos[$new] = $idx;
        }

        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func arrayChange(_ nums: [Int], _ operations: [[Int]]) -> [Int] {
        var result = nums
        var indexMap = [Int: Int]()
        for (i, v) in nums.enumerated() {
            indexMap[v] = i
        }
        for op in operations {
            let oldVal = op[0]
            let newVal = op[1]
            if let idx = indexMap[oldVal] {
                result[idx] = newVal
                indexMap.removeValue(forKey: oldVal)
                indexMap[newVal] = idx
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arrayChange(nums: IntArray, operations: Array<IntArray>): IntArray {
        val indexMap = HashMap<Int, Int>(nums.size * 2)
        for (i in nums.indices) {
            indexMap[nums[i]] = i
        }
        for (op in operations) {
            val oldVal = op[0]
            val newVal = op[1]
            val idx = indexMap[oldVal]!!
            nums[idx] = newVal
            indexMap.remove(oldVal)
            indexMap[newVal] = idx
        }
        return nums
    }
}
```

## Dart

```dart
class Solution {
  List<int> arrayChange(List<int> nums, List<List<int>> operations) {
    final Map<int, int> indexMap = {};
    for (int i = 0; i < nums.length; i++) {
      indexMap[nums[i]] = i;
    }
    for (final op in operations) {
      int oldVal = op[0];
      int newVal = op[1];
      int idx = indexMap[oldVal]!;
      nums[idx] = newVal;
      indexMap.remove(oldVal);
      indexMap[newVal] = idx;
    }
    return nums;
  }
}
```

## Golang

```go
func arrayChange(nums []int, operations [][]int) []int {
    // map from value to its index in nums
    pos := make(map[int]int, len(nums))
    for i, v := range nums {
        pos[v] = i
    }
    for _, op := range operations {
        oldVal, newVal := op[0], op[1]
        idx := pos[oldVal]
        nums[idx] = newVal
        delete(pos, oldVal)
        pos[newVal] = idx
    }
    return nums
}
```

## Ruby

```ruby
def array_change(nums, operations)
  pos = {}
  nums.each_with_index { |v, i| pos[v] = i }
  operations.each do |old, new_val|
    idx = pos[old]
    nums[idx] = new_val
    pos.delete(old)
    pos[new_val] = idx
  end
  nums
end
```

## Scala

```scala
object Solution {
    def arrayChange(nums: Array[Int], operations: Array[Array[Int]]): Array[Int] = {
        import scala.collection.mutable
        val pos = mutable.HashMap[Int, Int]()
        for (i <- nums.indices) {
            pos(nums(i)) = i
        }
        for (op <- operations) {
            val oldVal = op(0)
            val newVal = op(1)
            val idx = pos(oldVal)
            nums(idx) = newVal
            pos -= oldVal
            pos(newVal) = idx
        }
        nums
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn array_change(nums: Vec<i32>, operations: Vec<Vec<i32>>) -> Vec<i32> {
        let mut arr = nums;
        let mut pos: HashMap<i32, usize> = HashMap::with_capacity(arr.len() * 2);
        for (i, &v) in arr.iter().enumerate() {
            pos.insert(v, i);
        }
        for op in operations {
            let old = op[0];
            let new = op[1];
            if let Some(&idx) = pos.get(&old) {
                arr[idx] = new;
                pos.remove(&old);
                pos.insert(new, idx);
            }
        }
        arr
    }
}
```

## Racket

```racket
(define/contract (array-change nums operations)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([v (list->vector nums)]
         [pos (make-hash)])
    ;; map each value to its index
    (for ([i (in-range (vector-length v))])
      (hash-set! pos (vector-ref v i) i))
    ;; apply operations
    (for ([op operations])
      (define old (first op))
      (define new (second op))
      (define idx (hash-ref pos old))
      (vector-set! v idx new)
      (hash-remove! pos old)
      (hash-set! pos new idx))
    (vector->list v)))
```

## Erlang

```erlang
-spec array_change(Nums :: [integer()], Operations :: [[integer()]]) -> [integer()].
array_change(Nums, Operations) ->
    Map0 = build_map(Nums, 0, #{}),
    Array0 = array:from_list(Nums),
    {ArrayFinal,_} = lists:foldl(
        fun([Old, New], {Arr, Mp}) ->
            Idx = maps:get(Old, Mp),
            Arr1 = array:set(Idx, New, Arr),
            Mp1 = maps:remove(Old, Mp),
            Mp2 = maps:put(New, Idx, Mp1),
            {Arr1, Mp2}
        end,
        {Array0, Map0},
        Operations
    ),
    array:to_list(ArrayFinal).

build_map([], _Idx, Map) -> Map;
build_map([H|T], Idx, Map) ->
    NewMap = maps:put(H, Idx, Map),
    build_map(T, Idx + 1, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec array_change(nums :: [integer], operations :: [[integer]]) :: [integer]
  def array_change(nums, operations) do
    # value -> index map
    pos =
      Enum.with_index(nums)
      |> Enum.reduce(%{}, fn {v, i}, acc -> Map.put(acc, v, i) end)

    # index -> value map
    idx_val =
      Enum.with_index(nums)
      |> Enum.reduce(%{}, fn {v, i}, acc -> Map.put(acc, i, v) end)

    {_final_pos, final_idx_val} =
      Enum.reduce(operations, {pos, idx_val}, fn [old, new], {p, iv} ->
        idx = Map.fetch!(p, old)
        iv2 = Map.put(iv, idx, new)
        p2 = p |> Map.delete(old) |> Map.put(new, idx)
        {p2, iv2}
      end)

    len = length(nums)

    0..(len - 1)
    |> Enum.map(fn i -> Map.fetch!(final_idx_val, i) end)
  end
end
```
