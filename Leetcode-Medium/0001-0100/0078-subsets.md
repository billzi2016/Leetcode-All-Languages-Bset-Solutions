# 0078. Subsets

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result = {{}};
        for (int num : nums) {
            int sz = result.size();
            for (int i = 0; i < sz; ++i) {
                vector<int> subset = result[i];
                subset.push_back(num);
                result.push_back(std::move(subset));
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        for (int num : nums) {
            int size = result.size();
            for (int i = 0; i < size; i++) {
                List<Integer> subset = new ArrayList<>(result.get(i));
                subset.add(num);
                result.add(subset);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            # extend current subsets with the new number
            res += [curr + [num] for curr in res]
        return res
```

## Python3

```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []
        n = len(nums)

        def backtrack(start: int) -> None:
            result.append(path.copy())
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int total = 1 << numsSize;               // total number of subsets
    *returnSize = total;

    int* colSizes = (int*)malloc(total * sizeof(int));
    int** result   = (int**)malloc(total * sizeof(int*));

    for (int mask = 0; mask < total; ++mask) {
        // count bits to know subset size
        int cnt = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (mask & (1 << i)) cnt++;
        }
        colSizes[mask] = cnt;

        int* subset = (int*)malloc(cnt * sizeof(int));
        int idx = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (mask & (1 << i)) {
                subset[idx++] = nums[i];
            }
        }
        result[mask] = subset;
    }

    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<IList<int>> Subsets(int[] nums)
    {
        var result = new List<IList<int>>();
        Array.Sort(nums);
        Backtrack(0, new List<int>(), nums, result);
        return result;
    }

    private void Backtrack(int start, List<int> current, int[] nums, List<IList<int>> result)
    {
        result.Add(new List<int>(current));
        for (int i = start; i < nums.Length; i++)
        {
            current.Add(nums[i]);
            Backtrack(i + 1, current, nums, result);
            current.RemoveAt(current.Count - 1);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const result = [[]];
    for (const num of nums) {
        const size = result.length;
        for (let i = 0; i < size; i++) {
            result.push(result[i].concat(num));
        }
    }
    return result;
};
```

## Typescript

```typescript
function subsets(nums: number[]): number[][] {
    const result: number[][] = [[]];
    for (const num of nums) {
        const size = result.length;
        for (let i = 0; i < size; i++) {
            result.push([...result[i], num]);
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
     * @return Integer[][]
     */
    function subsets($nums) {
        $result = [[]];
        foreach ($nums as $num) {
            $newSubsets = [];
            foreach ($result as $subset) {
                $temp = $subset;
                $temp[] = $num;
                $newSubsets[] = $temp;
            }
            $result = array_merge($result, $newSubsets);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        var result = [[Int]]()
        let n = nums.count
        let total = 1 << n
        for mask in 0..<total {
            var subset = [Int]()
            for i in 0..<n {
                if (mask & (1 << i)) != 0 {
                    subset.append(nums[i])
                }
            }
            result.append(subset)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>(emptyList())
        for (num in nums) {
            val currentSize = result.size
            for (i in 0 until currentSize) {
                val newSubset = ArrayList(result[i])
                newSubset.add(num)
                result.add(newSubset)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> subsets(List<int> nums) {
    List<List<int>> result = [[]];
    for (int num in nums) {
      int currentSize = result.length;
      for (int i = 0; i < currentSize; i++) {
        List<int> newSubset = List.from(result[i]);
        newSubset.add(num);
        result.add(newSubset);
      }
    }
    return result;
  }
}
```

## Golang

```go
func subsets(nums []int) [][]int {
    res := make([][]int, 0, 1<<uint(len(nums)))
    res = append(res, []int{})
    for _, num := range nums {
        n := len(res)
        for i := 0; i < n; i++ {
            subset := make([]int, len(res[i])+1)
            copy(subset, res[i])
            subset[len(res[i])] = num
            res = append(res, subset)
        }
    }
    return res
}
```

## Ruby

```ruby
def subsets(nums)
  result = [[]]
  nums.each do |num|
    result += result.map { |subset| subset + [num] }
  end
  result
end
```

## Scala

```scala
object Solution {
    def subsets(nums: Array[Int]): List[List[Int]] = {
        var result: List[List[Int]] = List(Nil)
        for (num <- nums) {
            val added = result.map(_ :+ num)
            result = result ++ added
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        let total = 1usize << n;
        let mut res = Vec::with_capacity(total);
        for mask in 0..total {
            let mut subset = Vec::new();
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    subset.push(nums[i]);
                }
            }
            res.push(subset);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (subsets nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let recur ((lst nums))
    (if (null? lst)
        (list '())
        (let* ((first (car lst))
               (rest-subsets (recur (cdr lst))))
          (append rest-subsets
                  (map (lambda (s) (cons first s)) rest-subsets))))))
```

## Erlang

```erlang
-spec subsets(Nums :: [integer()]) -> [[integer()]].
subsets(Nums) ->
    lists:foldl(
        fun(Num, Acc) ->
            Acc ++ [[Num | Sub] || Sub <- Acc]
        end,
        [[]],
        Nums
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec subsets(nums :: [integer]) :: [[integer]]
  def subsets(nums) do
    Enum.reduce(nums, [[]], fn num, acc ->
      acc ++ Enum.map(acc, fn subset -> [num | subset] end)
    end)
    |> Enum.map(&Enum.reverse/1)
  end
end
```
