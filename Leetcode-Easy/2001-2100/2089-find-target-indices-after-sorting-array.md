# 2089. Find Target Indices After Sorting Array

## Cpp

```cpp
class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<int> res;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == target) {
                res.push_back(i);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> targetIndices(int[] nums, int target) {
        java.util.Arrays.sort(nums);
        java.util.List<Integer> res = new java.util.ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                res.add(i);
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result = []
        for i, val in enumerate(nums):
            if val == target:
                result.append(i)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, v in enumerate(nums) if v == target]
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    
    int *result = (int *)malloc(numsSize * sizeof(int));
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == target) {
            result[count++] = i;
        }
    }
    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> TargetIndices(int[] nums, int target) {
        Array.Sort(nums);
        List<int> result = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == target) {
                result.Add(i);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    nums.sort((a, b) => a - b);
    const result = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            result.push(i);
        }
    }
    return result;
};
```

## Typescript

```typescript
function targetIndices(nums: number[], target: number): number[] {
    nums.sort((a, b) => a - b);
    const result: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            result.push(i);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function targetIndices($nums, $target) {
        sort($nums);
        $result = [];
        foreach ($nums as $i => $val) {
            if ($val === $target) {
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
    func targetIndices(_ nums: [Int], _ target: Int) -> [Int] {
        let sorted = nums.sorted()
        var result = [Int]()
        for (i, v) in sorted.enumerated() where v == target {
            result.append(i)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun targetIndices(nums: IntArray, target: Int): List<Int> {
        val sorted = nums.sorted()
        val res = mutableListOf<Int>()
        for (i in sorted.indices) {
            if (sorted[i] == target) {
                res.add(i)
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> targetIndices(List<int> nums, int target) {
    var sorted = List<int>.from(nums);
    sorted.sort();
    List<int> result = [];
    for (int i = 0; i < sorted.length; i++) {
      if (sorted[i] == target) {
        result.add(i);
      }
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func targetIndices(nums []int, target int) []int {
	sort.Ints(nums)
	var result []int
	for i, v := range nums {
		if v == target {
			result = append(result, i)
		}
	}
	return result
}
```

## Ruby

```ruby
def target_indices(nums, target)
  sorted = nums.sort
  result = []
  sorted.each_with_index do |value, index|
    result << index if value == target
  end
  result
end
```

## Scala

```scala
object Solution {
    def targetIndices(nums: Array[Int], target: Int): List[Int] = {
        val sorted = nums.sorted
        sorted.zipWithIndex.collect { case (`target`, idx) => idx }.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut sorted = nums;
        sorted.sort();
        let mut result = Vec::new();
        for (i, &v) in sorted.iter().enumerate() {
            if v == target {
                result.push(i as i32);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (target-indices nums target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ((sorted (sort nums <)))
    (for/list ([i (in-range (length sorted))]
               #:when (= (list-ref sorted i) target))
      i)))
```

## Erlang

```erlang
-module(solution).
-export([target_indices/2]).

-spec target_indices(Nums :: [integer()], Target :: integer()) -> [integer()].
target_indices(Nums, Target) ->
    Sorted = lists:sort(Nums),
    collect(Sorted, Target, 0, []).

collect([], _Target, _Idx, Acc) ->
    lists:reverse(Acc);
collect([H|T], Target, Idx, Acc) ->
    case H of
        Target -> collect(T, Target, Idx + 1, [Idx | Acc]);
        _      -> collect(T, Target, Idx + 1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec target_indices(nums :: [integer], target :: integer) :: [integer]
  def target_indices(nums, target) do
    nums
    |> Enum.sort()
    |> Enum.with_index()
    |> Enum.filter(fn {v, _i} -> v == target end)
    |> Enum.map(fn {_v, i} -> i end)
  end
end
```
