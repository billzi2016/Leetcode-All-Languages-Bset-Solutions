# 1389. Create Target Array in the Given Order

## Cpp

```cpp
class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> target;
        int n = nums.size();
        target.reserve(n);
        for (int i = 0; i < n; ++i) {
            target.insert(target.begin() + index[i], nums[i]);
        }
        return target;
    }
};
```

## Java

```java
class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        java.util.List<Integer> target = new java.util.ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            target.add(index[i], nums[i]);
        }
        int[] result = new int[target.size()];
        for (int i = 0; i < target.size(); i++) {
            result[i] = target.get(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target
```

## Python3

```python
from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize) {
    int *target = (int *)malloc(numsSize * sizeof(int));
    int len = 0;
    for (int i = 0; i < numsSize; ++i) {
        int pos = index[i];
        // shift elements to the right
        for (int j = len - 1; j >= pos; --j) {
            target[j + 1] = target[j];
        }
        target[pos] = nums[i];
        ++len;
    }
    *returnSize = numsSize;
    return target;
}
```

## Csharp

```csharp
public class Solution {
    public int[] CreateTargetArray(int[] nums, int[] index) {
        var target = new System.Collections.Generic.List<int>();
        for (int i = 0; i < nums.Length; i++) {
            target.Insert(index[i], nums[i]);
        }
        return target.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function(nums, index) {
    const target = [];
    for (let i = 0; i < nums.length; i++) {
        target.splice(index[i], 0, nums[i]);
    }
    return target;
};
```

## Typescript

```typescript
function createTargetArray(nums: number[], index: number[]): number[] {
    const target: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        target.splice(index[i], 0, nums[i]);
    }
    return target;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $index
     * @return Integer[]
     */
    function createTargetArray($nums, $index) {
        $target = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $pos = $index[$i];
            array_splice($target, $pos, 0, [$nums[$i]]);
        }
        return $target;
    }
}
```

## Swift

```swift
class Solution {
    func createTargetArray(_ nums: [Int], _ index: [Int]) -> [Int] {
        var target = [Int]()
        for i in 0..<nums.count {
            target.insert(nums[i], at: index[i])
        }
        return target
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun createTargetArray(nums: IntArray, index: IntArray): IntArray {
        val target = mutableListOf<Int>()
        for (i in nums.indices) {
            target.add(index[i], nums[i])
        }
        return target.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> createTargetArray(List<int> nums, List<int> index) {
    List<int> target = [];
    for (int i = 0; i < nums.length; i++) {
      target.insert(index[i], nums[i]);
    }
    return target;
  }
}
```

## Golang

```go
func createTargetArray(nums []int, index []int) []int {
    target := make([]int, 0, len(nums))
    for i, v := range nums {
        pos := index[i]
        if pos == len(target) {
            target = append(target, v)
        } else {
            oldLen := len(target)
            target = append(target, 0)
            copy(target[pos+1:], target[pos:oldLen])
            target[pos] = v
        }
    }
    return target
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} index
# @return {Integer[]}
def create_target_array(nums, index)
  target = []
  nums.each_with_index do |num, i|
    target.insert(index[i], num)
  end
  target
end
```

## Scala

```scala
object Solution {
    def createTargetArray(nums: Array[Int], index: Array[Int]): Array[Int] = {
        val target = scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- nums.indices) {
            target.insert(index(i), nums(i))
        }
        target.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn create_target_array(nums: Vec<i32>, index: Vec<i32>) -> Vec<i32> {
        let mut target = Vec::with_capacity(nums.len());
        for (num, &idx) in nums.iter().zip(index.iter()) {
            target.insert(idx as usize, *num);
        }
        target
    }
}
```

## Racket

```racket
(define/contract (create-target-array nums index)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (letrec ((insert-at
            (lambda (lst pos val)
              (if (= pos 0)
                  (cons val lst)
                  (cons (car lst) (insert-at (cdr lst) (- pos 1) val)))))
           (build
            (lambda (ns is target)
              (if (null? ns)
                  target
                  (build (cdr ns) (cdr is) (insert-at target (car is) (car ns)))))))
    (build nums index '())))
```

## Erlang

```erlang
-module(solution).
-export([create_target_array/2]).

-spec create_target_array(Nums :: [integer()], Index :: [integer()]) -> [integer()].
create_target_array(Nums, Index) ->
    lists:foldl(
        fun({Num, Idx}, Acc) ->
            insert_at(Idx, Num, Acc)
        end,
        [],
        lists:zip(Nums, Index)
    ).

insert_at(0, Elem, List) ->
    [Elem | List];
insert_at(N, Elem, [H|T]) when N > 0 ->
    [H | insert_at(N-1, Elem, T)];
insert_at(_, Elem, []) ->
    [Elem].
```

## Elixir

```elixir
defmodule Solution do
  @spec create_target_array(nums :: [integer], index :: [integer]) :: [integer]
  def create_target_array(nums, index) do
    Enum.zip(nums, index)
    |> Enum.reduce([], fn {num, idx}, acc ->
      List.insert_at(acc, idx, num)
    end)
  end
end
```
