# 2215. Find the Difference of Two Arrays

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        
        vector<int> onlyInFirst;
        for (int x : set1) {
            if (!set2.count(x)) onlyInFirst.push_back(x);
        }
        
        vector<int> onlyInSecond;
        for (int x : set2) {
            if (!set1.count(x)) onlyInSecond.push_back(x);
        }
        
        return {onlyInFirst, onlyInSecond};
    }
};
```

## Java

```java
class Solution {
    public java.util.List<java.util.List<Integer>> findDifference(int[] nums1, int[] nums2) {
        java.util.Set<Integer> set2 = new java.util.HashSet<>();
        for (int num : nums2) {
            set2.add(num);
        }
        java.util.Set<Integer> onlyIn1 = new java.util.HashSet<>();
        for (int num : nums1) {
            if (!set2.contains(num)) {
                onlyIn1.add(num);
            }
        }

        java.util.Set<Integer> set1 = new java.util.HashSet<>();
        for (int num : nums1) {
            set1.add(num);
        }
        java.util.Set<Integer> onlyIn2 = new java.util.HashSet<>();
        for (int num : nums2) {
            if (!set1.contains(num)) {
                onlyIn2.add(num);
            }
        }

        java.util.List<Integer> list1 = new java.util.ArrayList<>(onlyIn1);
        java.util.List<Integer> list2 = new java.util.ArrayList<>(onlyIn2);

        java.util.List<java.util.List<Integer>> result = new java.util.ArrayList<>();
        result.add(list1);
        result.add(list2);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
```

## Python3

```python
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
```

## C

```c
#include <stdlib.h>
#include <string.h>

int** findDifference(int* nums1, int nums1Size, int* nums2, int nums2Size,
                     int* returnSize, int*** returnColumnSizes) {
    const int OFFSET = 1000;
    const int RANGE = 2001; // -1000 .. 1000

    char present1[RANGE];
    char present2[RANGE];
    memset(present1, 0, sizeof(present1));
    memset(present2, 0, sizeof(present2));

    for (int i = 0; i < nums1Size; ++i) {
        present1[nums1[i] + OFFSET] = 1;
    }
    for (int i = 0; i < nums2Size; ++i) {
        present2[nums2[i] + OFFSET] = 1;
    }

    char onlyIn1[RANGE];
    char onlyIn2[RANGE];
    memset(onlyIn1, 0, sizeof(onlyIn1));
    memset(onlyIn2, 0, sizeof(onlyIn2));

    for (int i = 0; i < nums1Size; ++i) {
        int idx = nums1[i] + OFFSET;
        if (!present2[idx]) onlyIn1[idx] = 1;
    }
    for (int i = 0; i < nums2Size; ++i) {
        int idx = nums2[i] + OFFSET;
        if (!present1[idx]) onlyIn2[idx] = 1;
    }

    int size1 = 0, size2 = 0;
    for (int i = 0; i < RANGE; ++i) {
        if (onlyIn1[i]) ++size1;
        if (onlyIn2[i]) ++size2;
    }

    int* arr1 = size1 ? (int*)malloc(size1 * sizeof(int)) : NULL;
    int* arr2 = size2 ? (int*)malloc(size2 * sizeof(int)) : NULL;

    int pos = 0;
    for (int i = 0; i < RANGE; ++i) {
        if (onlyIn1[i]) {
            arr1[pos++] = i - OFFSET;
        }
    }

    pos = 0;
    for (int i = 0; i < RANGE; ++i) {
        if (onlyIn2[i]) {
            arr2[pos++] = i - OFFSET;
        }
    }

    int** result = (int**)malloc(2 * sizeof(int*));
    result[0] = arr1;
    result[1] = arr2;

    int* colSizes = (int*)malloc(2 * sizeof(int));
    colSizes[0] = size1;
    colSizes[1] = size2;

    *returnSize = 2;
    *returnColumnSizes = &colSizes; // adjust to expected signature

    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
        var set2 = new HashSet<int>(nums2);
        var onlyInNums1 = new HashSet<int>();
        foreach (var num in nums1) {
            if (!set2.Contains(num)) {
                onlyInNums1.Add(num);
            }
        }

        var set1 = new HashSet<int>(nums1);
        var onlyInNums2 = new HashSet<int>();
        foreach (var num in nums2) {
            if (!set1.Contains(num)) {
                onlyInNums2.Add(num);
            }
        }

        return new List<IList<int>> { onlyInNums1.ToList(), onlyInNums2.ToList() };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    
    const onlyIn1 = [];
    for (const x of set1) {
        if (!set2.has(x)) onlyIn1.push(x);
    }
    
    const onlyIn2 = [];
    for (const x of set2) {
        if (!set1.has(x)) onlyIn2.push(x);
    }
    
    return [onlyIn1, onlyIn2];
};
```

## Typescript

```typescript
function findDifference(nums1: number[], nums2: number[]): number[][] {
    const set2 = new Set<number>(nums2);
    const onlyInFirst = new Set<number>();
    for (const num of nums1) {
        if (!set2.has(num)) onlyInFirst.add(num);
    }

    const set1 = new Set<number>(nums1);
    const onlyInSecond = new Set<number>();
    for (const num of nums2) {
        if (!set1.has(num)) onlyInSecond.add(num);
    }

    return [Array.from(onlyInFirst), Array.from(onlyInSecond)];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[][]
     */
    function findDifference($nums1, $nums2) {
        // Build set for nums2
        $set2 = [];
        foreach ($nums2 as $v) {
            $set2[$v] = true;
        }
        // Elements only in nums1
        $only1Set = [];
        foreach ($nums1 as $v) {
            if (!isset($set2[$v])) {
                $only1Set[$v] = true;
            }
        }

        // Build set for nums1
        $set1 = [];
        foreach ($nums1 as $v) {
            $set1[$v] = true;
        }
        // Elements only in nums2
        $only2Set = [];
        foreach ($nums2 as $v) {
            if (!isset($set1[$v])) {
                $only2Set[$v] = true;
            }
        }

        $only1 = array_map('intval', array_keys($only1Set));
        $only2 = array_map('intval', array_keys($only2Set));

        return [$only1, $only2];
    }
}
```

## Swift

```swift
class Solution {
    func findDifference(_ nums1: [Int], _ nums2: [Int]) -> [[Int]] {
        let set1 = Set(nums1)
        let set2 = Set(nums2)
        let diff1 = Array(set1.subtracting(set2))
        let diff2 = Array(set2.subtracting(set1))
        return [diff1, diff2]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDifference(nums1: IntArray, nums2: IntArray): List<List<Int>> {
        val set1 = nums1.toHashSet()
        val set2 = nums2.toHashSet()

        val onlyIn1 = mutableListOf<Int>()
        for (num in set1) {
            if (!set2.contains(num)) {
                onlyIn1.add(num)
            }
        }

        val onlyIn2 = mutableListOf<Int>()
        for (num in set2) {
            if (!set1.contains(num)) {
                onlyIn2.add(num)
            }
        }

        return listOf(onlyIn1, onlyIn2)
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> findDifference(List<int> nums1, List<int> nums2) {
    final set1 = nums1.toSet();
    final set2 = nums2.toSet();

    final onlyInNums1 = set1.difference(set2).toList();
    final onlyInNums2 = set2.difference(set1).toList();

    return [onlyInNums1, onlyInNums2];
  }
}
```

## Golang

```go
func findDifference(nums1 []int, nums2 []int) [][]int {
	// Build set for nums2
	set2 := make(map[int]struct{}, len(nums2))
	for _, v := range nums2 {
		set2[v] = struct{}{}
	}
	// Elements only in nums1
	only1Set := make(map[int]struct{})
	for _, v := range nums1 {
		if _, exists := set2[v]; !exists {
			only1Set[v] = struct{}{}
		}
	}
	// Build set for nums1
	set1 := make(map[int]struct{}, len(nums1))
	for _, v := range nums1 {
		set1[v] = struct{}{}
	}
	// Elements only in nums2
	only2Set := make(map[int]struct{})
	for _, v := range nums2 {
		if _, exists := set1[v]; !exists {
			only2Set[v] = struct{}{}
		}
	}
	// Convert sets to slices
	only1 := make([]int, 0, len(only1Set))
	for v := range only1Set {
		only1 = append(only1, v)
	}
	only2 := make([]int, 0, len(only2Set))
	for v := range only2Set {
		only2 = append(only2, v)
	}
	return [][]int{only1, only2}
}
```

## Ruby

```ruby
require 'set'

def find_difference(nums1, nums2)
  set1 = nums1.to_set
  set2 = nums2.to_set
  [(set1 - set2).to_a, (set2 - set1).to_a]
end
```

## Scala

```scala
object Solution {
    def findDifference(nums1: Array[Int], nums2: Array[Int]): List[List[Int]] = {
        val set1 = nums1.toSet
        val set2 = nums2.toSet
        val onlyIn1 = (set1 diff set2).toList
        val onlyIn2 = (set2 diff set1).toList
        List(onlyIn1, onlyIn2)
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let set2: HashSet<i32> = nums2.iter().cloned().collect();
        let mut only1 = HashSet::new();
        for &x in &nums1 {
            if !set2.contains(&x) {
                only1.insert(x);
            }
        }

        let set1: HashSet<i32> = nums1.iter().cloned().collect();
        let mut only2 = HashSet::new();
        for &x in &nums2 {
            if !set1.contains(&x) {
                only2.insert(x);
            }
        }

        vec![
            only1.into_iter().collect(),
            only2.into_iter().collect(),
        ]
    }
}
```

## Racket

```racket
(define/contract (find-difference nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ([set2 (make-hash)]
         [_   (for-each (lambda (x) (hash-set! set2 x #t)) nums2)]
         [seen1 (make-hash)]
         [unique1 '()])
    ;; elements only in nums1
    (for-each
     (lambda (x)
       (when (and (not (hash-has-key? set2 x))
                  (not (hash-has-key? seen1 x)))
         (set! unique1 (cons x unique1))
         (hash-set! seen1 x #t)))
     nums1)
    (let* ([set1 (make-hash)]
           [_   (for-each (lambda (x) (hash-set! set1 x #t)) nums1)]
           [seen2 (make-hash)]
           [unique2 '()])
      ;; elements only in nums2
      (for-each
       (lambda (x)
         (when (and (not (hash-has-key? set1 x))
                    (not (hash-has-key? seen2 x)))
           (set! unique2 (cons x unique2))
           (hash-set! seen2 x #t)))
       nums2)
      (list (reverse unique1) (reverse unique2)))))
```

## Erlang

```erlang
-spec find_difference(Nums1 :: [integer()], Nums2 :: [integer()]) -> [[integer()]].
find_difference(Nums1, Nums2) ->
    Set2 = lists:foldl(fun(X, Acc) -> sets:add_element(X, Acc) end,
                       sets:new(),
                       Nums2),
    Only1Set = lists:foldl(
        fun(X, Acc) ->
            case sets:is_element(X, Set2) of
                true -> Acc;
                false -> sets:add_element(X, Acc)
            end
        end,
        sets:new(),
        Nums1),
    Set1 = lists:foldl(fun(X, Acc) -> sets:add_element(X, Acc) end,
                       sets:new(),
                       Nums1),
    Only2Set = lists:foldl(
        fun(X, Acc) ->
            case sets:is_element(X, Set1) of
                true -> Acc;
                false -> sets:add_element(X, Acc)
            end
        end,
        sets:new(),
        Nums2),
    [sets:to_list(Only1Set), sets:to_list(Only2Set)].
```

## Elixir

```elixir
defmodule Solution do
  @spec find_difference(nums1 :: [integer], nums2 :: [integer]) :: [[integer]]
  def find_difference(nums1, nums2) do
    set1 = MapSet.new(nums1)
    set2 = MapSet.new(nums2)

    only_in_nums1 = MapSet.difference(set1, set2) |> Enum.to_list()
    only_in_nums2 = MapSet.difference(set2, set1) |> Enum.to_list()

    [only_in_nums1, only_in_nums2]
  end
end
```
