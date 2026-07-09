# 3467. Transform Array by Parity

## Cpp

```cpp
class Solution {
public:
    vector<int> transformArray(vector<int>& nums) {
        int evenCount = 0;
        for (int v : nums) {
            if (v % 2 == 0) ++evenCount;
        }
        int oddCount = nums.size() - evenCount;
        vector<int> result;
        result.reserve(nums.size());
        result.insert(result.end(), evenCount, 0);
        result.insert(result.end(), oddCount, 1);
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] transformArray(int[] nums) {
        int evens = 0;
        for (int v : nums) {
            if ((v & 1) == 0) {
                evens++;
            }
        }
        int n = nums.length;
        int[] res = new int[n];
        for (int i = evens; i < n; i++) {
            res[i] = 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = sum(1 for v in nums if v % 2 == 0)
        odds = len(nums) - evens
        return [0] * evens + [1] * odds
```

## Python3

```python
from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        evens = sum(1 for v in nums if v % 2 == 0)
        odds = len(nums) - evens
        return [0] * evens + [1] * odds
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* transformArray(int* nums, int numsSize, int* returnSize) {
    int evenCount = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] % 2 == 0) {
            ++evenCount;
        }
    }
    int oddCount = numsSize - evenCount;

    int* result = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < evenCount; ++i) {
        result[i] = 0;
    }
    for (int i = 0; i < oddCount; ++i) {
        result[evenCount + i] = 1;
    }

    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] TransformArray(int[] nums) {
        int evenCount = 0;
        foreach (int num in nums) {
            if ((num & 1) == 0) evenCount++;
        }
        int total = nums.Length;
        int[] result = new int[total];
        for (int i = evenCount; i < total; i++) {
            result[i] = 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var transformArray = function(nums) {
    let evenCount = 0, oddCount = 0;
    for (const num of nums) {
        if (num % 2 === 0) evenCount++;
        else oddCount++;
    }
    const result = new Array(evenCount).fill(0);
    result.push(...new Array(oddCount).fill(1));
    return result;
};
```

## Typescript

```typescript
function transformArray(nums: number[]): number[] {
    let evenCount = 0;
    for (const num of nums) {
        if (num % 2 === 0) evenCount++;
    }
    const oddCount = nums.length - evenCount;
    return new Array(evenCount).fill(0).concat(new Array(oddCount).fill(1));
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function transformArray($nums) {
        $evenCount = 0;
        foreach ($nums as $num) {
            if ($num % 2 == 0) {
                $evenCount++;
            }
        }
        $oddCount = count($nums) - $evenCount;
        $result = array_fill(0, $evenCount, 0);
        if ($oddCount > 0) {
            $result = array_merge($result, array_fill(0, $oddCount, 1));
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func transformArray(_ nums: [Int]) -> [Int] {
        var evenCount = 0
        for num in nums {
            if num % 2 == 0 { evenCount += 1 }
        }
        let oddCount = nums.count - evenCount
        var result = [Int]()
        result.reserveCapacity(nums.count)
        result.append(contentsOf: Array(repeating: 0, count: evenCount))
        result.append(contentsOf: Array(repeating: 1, count: oddCount))
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun transformArray(nums: IntArray): IntArray {
        var evenCount = 0
        for (num in nums) {
            if (num % 2 == 0) evenCount++
        }
        return IntArray(nums.size) { index -> if (index < evenCount) 0 else 1 }
    }
}
```

## Dart

```dart
class Solution {
  List<int> transformArray(List<int> nums) {
    int evenCount = 0;
    for (int num in nums) {
      if (num % 2 == 0) evenCount++;
    }
    int oddCount = nums.length - evenCount;

    List<int> result = [];
    result.addAll(List.filled(evenCount, 0));
    result.addAll(List.filled(oddCount, 1));
    return result;
  }
}
```

## Golang

```go
func transformArray(nums []int) []int {
    evenCount := 0
    for _, v := range nums {
        if v%2 == 0 {
            evenCount++
        }
    }
    result := make([]int, len(nums))
    for i := evenCount; i < len(nums); i++ {
        result[i] = 1
    }
    return result
}
```

## Ruby

```ruby
def transform_array(nums)
  even_count = nums.count { |v| v.even? }
  odd_count = nums.size - even_count
  [0] * even_count + [1] * odd_count
end
```

## Scala

```scala
object Solution {
    def transformArray(nums: Array[Int]): Array[Int] = {
        val evenCount = nums.count(_ % 2 == 0)
        val oddCount = nums.length - evenCount
        Array.fill(evenCount)(0) ++ Array.fill(oddCount)(1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn transform_array(nums: Vec<i32>) -> Vec<i32> {
        let mut even_cnt = 0usize;
        for &v in &nums {
            if v % 2 == 0 {
                even_cnt += 1;
            }
        }
        let odd_cnt = nums.len() - even_cnt;
        let mut result = Vec::with_capacity(nums.len());
        result.extend(std::iter::repeat(0).take(even_cnt));
        result.extend(std::iter::repeat(1).take(odd_cnt));
        result
    }
}
```

## Racket

```racket
(define/contract (transform-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((x (length (filter even? nums)))
         (y (length (filter odd? nums))))
    (append (make-list x 0) (make-list y 1))))
```

## Erlang

```erlang
-module(solution).
-export([transform_array/1]).

-spec transform_array(Nums :: [integer()]) -> [integer()].
transform_array(Nums) ->
    {EvenCount, OddCount} = count_parity(Nums, 0, 0),
    lists:duplicate(EvenCount, 0) ++ lists:duplicate(OddCount, 1).

count_parity([], E, O) -> {E, O};
count_parity([H|T], E, O) ->
    case H rem 2 of
        0 -> count_parity(T, E + 1, O);
        _ -> count_parity(T, E, O + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec transform_array(nums :: [integer]) :: [integer]
  def transform_array(nums) do
    {evens, odds} =
      Enum.reduce(nums, {0, 0}, fn n, {e, o} ->
        if rem(n, 2) == 0, do: {e + 1, o}, else: {e, o + 1}
      end)

    List.duplicate(0, evens) ++ List.duplicate(1, odds)
  end
end
```
