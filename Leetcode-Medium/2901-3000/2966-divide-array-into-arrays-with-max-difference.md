# 2966. Divide Array Into Arrays With Max Difference

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (size_t i = 0; i < nums.size(); i += 3) {
            if (nums[i + 2] - nums[i] > k) {
                return {};
            }
            ans.push_back({nums[i], nums[i + 1], nums[i + 2]});
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int groups = n / 3;
        int[][] result = new int[groups][3];
        for (int i = 0, g = 0; i < n; i += 3, g++) {
            if (nums[i + 2] - nums[i] > k) {
                return new int[0][];
            }
            result[g][0] = nums[i];
            result[g][1] = nums[i + 1];
            result[g][2] = nums[i + 2];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans
```

## C

```c
#include <stdlib.h>

/* Comparator function for qsort */
static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** divideArray(int* nums, int numsSize, int k, int* returnSize, int*** returnColumnSizes) {
    /* Sort the input array */
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    
    int groups = numsSize / 3;
    for (int i = 0; i < numsSize; i += 3) {
        if (nums[i + 2] - nums[i] > k) {
            *returnSize = 0;
            *returnColumnSizes = NULL;
            return NULL;
        }
    }
    
    int **ans = (int **)malloc(groups * sizeof(int *));
    int *colSizes = (int *)malloc(groups * sizeof(int));
    
    for (int g = 0; g < groups; ++g) {
        ans[g] = (int *)malloc(3 * sizeof(int));
        ans[g][0] = nums[3 * g];
        ans[g][1] = nums[3 * g + 1];
        ans[g][2] = nums[3 * g + 2];
        colSizes[g] = 3;
    }
    
    *returnSize = groups;
    *returnColumnSizes = &colSizes;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] DivideArray(int[] nums, int k)
    {
        Array.Sort(nums);
        var groups = new List<int[]>();
        for (int i = 0; i < nums.Length; i += 3)
        {
            if (nums[i + 2] - nums[i] > k)
                return new int[0][];
            groups.Add(new int[] { nums[i], nums[i + 1], nums[i + 2] });
        }
        return groups.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[][]}
 */
var divideArray = function(nums, k) {
    nums.sort((a, b) => a - b);
    const res = [];
    for (let i = 0; i < nums.length; i += 3) {
        if (nums[i + 2] - nums[i] > k) {
            return [];
        }
        res.push([nums[i], nums[i + 1], nums[i + 2]]);
    }
    return res;
};
```

## Typescript

```typescript
function divideArray(nums: number[], k: number): number[][] {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const result: number[][] = [];
    for (let i = 0; i < n; i += 3) {
        if (i + 2 >= n) return [];
        if (nums[i + 2] - nums[i] > k) return [];
        result.push([nums[i], nums[i + 1], nums[i + 2]]);
    }
    return result;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[][]
     */
    function divideArray($nums, $k) {
        sort($nums);
        $n = count($nums);
        $result = [];
        for ($i = 0; $i < $n; $i += 3) {
            if ($nums[$i + 2] - $nums[$i] > $k) {
                return [];
            }
            $result[] = [$nums[$i], $nums[$i + 1], $nums[$i + 2]];
        }
        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    func divideArray(_ nums: [Int], _ k: Int) -> [[Int]] {
        let sorted = nums.sorted()
        var result = [[Int]]()
        var i = 0
        while i < sorted.count {
            if sorted[i + 2] - sorted[i] > k {
                return []
            }
            result.append([sorted[i], sorted[i + 1], sorted[i + 2]])
            i += 3
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun divideArray(nums: IntArray, k: Int): Array<IntArray> {
        val n = nums.size
        val arr = nums.clone()
        java.util.Arrays.sort(arr)
        val result = mutableListOf<IntArray>()
        var i = 0
        while (i < n) {
            if (arr[i + 2] - arr[i] > k) {
                return arrayOf()
            }
            result.add(intArrayOf(arr[i], arr[i + 1], arr[i + 2]))
            i += 3
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> divideArray(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    List<List<int>> result = [];
    for (int i = 0; i < n; i += 3) {
      if (i + 2 >= n) return [];
      if (nums[i + 2] - nums[i] > k) return [];
      result.add([nums[i], nums[i + 1], nums[i + 2]]);
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func divideArray(nums []int, k int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	res := make([][]int, 0, n/3)
	for i := 0; i < n; i += 3 {
		if nums[i+2]-nums[i] > k {
			return [][]int{}
		}
		res = append(res, []int{nums[i], nums[i+1], nums[i+2]})
	}
	return res
}
```

## Ruby

```ruby
def divide_array(nums, k)
  n = nums.length
  nums.sort!
  result = []
  i = 0
  while i < n
    return [] if nums[i + 2] - nums[i] > k
    result << [nums[i], nums[i + 1], nums[i + 2]]
    i += 3
  end
  result
end
```

## Scala

```scala
object Solution {
    def divideArray(nums: Array[Int], k: Int): Array[Array[Int]] = {
        val sorted = nums.sorted
        val n = sorted.length
        val groups = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
        var i = 0
        while (i < n) {
            if (sorted(i + 2) - sorted(i) > k) return Array.empty[Array[Int]]
            groups += Array(sorted(i), sorted(i + 1), sorted(i + 2))
            i += 3
        }
        groups.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut sorted = nums;
        sorted.sort();
        let n = sorted.len();
        let mut result: Vec<Vec<i32>> = Vec::with_capacity(n / 3);
        for i in (0..n).step_by(3) {
            if sorted[i + 2] - sorted[i] > k {
                return Vec::new();
            }
            result.push(vec![sorted[i], sorted[i + 1], sorted[i + 2]]);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (divide-array nums k)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))
  (let* ((sorted (sort nums <))
         (process
          (lambda (lst)
            (if (null? lst)
                '()
                (let* ((a (car lst))
                       (b (cadr lst))
                       (c (caddr lst))
                       (rest (cdddr lst)))
                  (if (> (- c a) k)
                      #f
                      (let ((sub (list a b c))
                            (next (process rest)))
                        (if (eq? next #f)
                            #f
                            (cons sub next)))))))))
    (let ((res (process sorted)))
      (if (eq? res #f) '() res))))
```

## Erlang

```erlang
-module(solution).
-export([divide_array/2]).

-spec divide_array(Nums :: [integer()], K :: integer()) -> [[integer()]].
divide_array(Nums, K) ->
    Sorted = lists:sort(Nums),
    case build(Sorted, K) of
        {ok, Res} -> Res;
        error -> []
    end.

build([], _K) -> {ok, []};
build([A, B, C | Rest], K) ->
    if
        C - A =< K ->
            case build(Rest, K) of
                {ok, Tail} -> {ok, [[A, B, C] | Tail]};
                error -> error
            end;
        true -> error
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec divide_array(nums :: [integer], k :: integer) :: [[integer]]
  def divide_array(nums, k) do
    sorted = Enum.sort(nums)

    case build(sorted, [], k) do
      :error -> []
      result -> result
    end
  end

  defp build([], acc, _k), do: Enum.reverse(acc)

  defp build([a, b, c | rest], acc, k) do
    if c - a <= k do
      build(rest, [[a, b, c] | acc], k)
    else
      :error
    end
  end
end
```
