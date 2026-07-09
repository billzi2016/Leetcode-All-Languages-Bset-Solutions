# 0046. Permutations

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        vector<bool> used(nums.size(), false);
        backtrack(nums, used, path, result);
        return result;
    }
private:
    void backtrack(const vector<int>& nums, vector<bool>& used,
                   vector<int>& path, vector<vector<int>>& result) {
        if (path.size() == nums.size()) {
            result.push_back(path);
            return;
        }
        for (size_t i = 0; i < nums.size(); ++i) {
            if (!used[i]) {
                used[i] = true;
                path.push_back(nums[i]);
                backtrack(nums, used, path, result);
                path.pop_back();
                used[i] = false;
            }
        }
    }
};
```

## Java

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                used[i] = true;
                path.add(nums[i]);
                backtrack(nums, used, path, result);
                path.remove(path.size() - 1);
                used[i] = false;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False

        backtrack()
        return res
```

## Python3

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(nums)
        used = [False] * n
        path: List[int] = []

        def backtrack() -> None:
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False

        backtrack()
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/* Helper function for backtracking */
static void backtrack(int idx, int n, int *arr,
                      int **res, int *col, int *pos) {
    if (idx == n) {
        int *perm = (int *)malloc(n * sizeof(int));
        memcpy(perm, arr, n * sizeof(int));
        res[*pos] = perm;
        col[*pos] = n;
        (*pos)++;
        return;
    }
    for (int i = idx; i < n; ++i) {
        int tmp = arr[idx];
        arr[idx] = arr[i];
        arr[i] = tmp;

        backtrack(idx + 1, n, arr, res, col, pos);

        /* swap back */
        tmp = arr[idx];
        arr[idx] = arr[i];
        arr[i] = tmp;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** permute(int* nums, int numsSize, int* returnSize, int*** returnColumnSizes) {
    (void)returnColumnSizes; // suppress unused warning if not needed
    int total = 1;
    for (int i = 2; i <= numsSize; ++i) total *= i;

    int **result = (int **)malloc(total * sizeof(int *));
    int *colSizes = (int *)malloc(total * sizeof(int));

    int *arrCopy = (int *)malloc(numsSize * sizeof(int));
    memcpy(arrCopy, nums, numsSize * sizeof(int));

    int pos = 0;
    backtrack(0, numsSize, arrCopy, result, colSizes, &pos);

    free(arrCopy);
    *returnSize = total;
    *returnColumnSizes = &colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<IList<int>> Permute(int[] nums)
    {
        var result = new List<IList<int>>();
        var path = new List<int>();
        var used = new bool[nums.Length];
        Backtrack(nums, used, path, result);
        return result;
    }

    private void Backtrack(int[] nums, bool[] used, List<int> path, IList<IList<int>> result)
    {
        if (path.Count == nums.Length)
        {
            result.Add(new List<int>(path));
            return;
        }

        for (int i = 0; i < nums.Length; i++)
        {
            if (used[i]) continue;

            used[i] = true;
            path.Add(nums[i]);

            Backtrack(nums, used, path, result);

            path.RemoveAt(path.Count - 1);
            used[i] = false;
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
var permute = function(nums) {
    const result = [];
    const path = [];
    const used = new Array(nums.length).fill(false);
    
    function backtrack() {
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.push(nums[i]);
            backtrack();
            path.pop();
            used[i] = false;
        }
    }
    
    backtrack();
    return result;
};
```

## Typescript

```typescript
function permute(nums: number[]): number[][] {
    const res: number[][] = [];
    const n = nums.length;
    const used = new Array(n).fill(false);
    const path: number[] = [];

    function backtrack() {
        if (path.length === n) {
            res.push([...path]);
            return;
        }
        for (let i = 0; i < n; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.push(nums[i]);
            backtrack();
            path.pop();
            used[i] = false;
        }
    }

    backtrack();
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function permute($nums) {
        $result = [];
        $n = count($nums);
        if ($n === 0) return $result;
        $used = array_fill(0, $n, false);
        $path = [];

        $dfs = function($depth) use (&$nums, &$used, &$path, &$result, $n, &$dfs) {
            if ($depth === $n) {
                $result[] = $path;
                return;
            }
            for ($i = 0; $i < $n; $i++) {
                if ($used[$i]) continue;
                $used[$i] = true;
                $path[] = $nums[$i];
                $dfs($depth + 1);
                array_pop($path);
                $used[$i] = false;
            }
        };

        $dfs(0);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func permute(_ nums: [Int]) -> [[Int]] {
        var result = [[Int]]()
        var current = [Int]()
        var used = Array(repeating: false, count: nums.count)
        
        func backtrack() {
            if current.count == nums.count {
                result.append(current)
                return
            }
            for i in 0..<nums.count {
                if used[i] { continue }
                used[i] = true
                current.append(nums[i])
                backtrack()
                current.removeLast()
                used[i] = false
            }
        }
        
        backtrack()
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun permute(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        fun backtrack(start: Int) {
            if (start == nums.size) {
                result.add(nums.toList())
                return
            }
            for (i in start until nums.size) {
                // swap nums[start] and nums[i]
                val tmp = nums[start]
                nums[start] = nums[i]
                nums[i] = tmp

                backtrack(start + 1)

                // revert swap
                val tmp2 = nums[start]
                nums[start] = nums[i]
                nums[i] = tmp2
            }
        }
        backtrack(0)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> permute(List<int> nums) {
    List<List<int>> result = [];

    void backtrack(int start) {
      if (start == nums.length) {
        result.add(List.from(nums));
        return;
      }
      for (int i = start; i < nums.length; i++) {
        // swap
        int tmp = nums[start];
        nums[start] = nums[i];
        nums[i] = tmp;

        backtrack(start + 1);

        // revert swap
        tmp = nums[start];
        nums[start] = nums[i];
        nums[i] = tmp;
      }
    }

    backtrack(0);
    return result;
  }
}
```

## Golang

```go
func permute(nums []int) [][]int {
    var res [][]int
    n := len(nums)

    var backtrack func(int)
    backtrack = func(first int) {
        if first == n {
            tmp := make([]int, n)
            copy(tmp, nums)
            res = append(res, tmp)
            return
        }
        for i := first; i < n; i++ {
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
        }
    }

    backtrack(0)
    return res
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def permute(nums)
  res = []
  n = nums.size
  used = Array.new(n, false)

  backtrack = lambda do |path|
    if path.size == n
      res << path.clone
      return
    end

    nums.each_with_index do |num, i|
      next if used[i]
      used[i] = true
      path << num
      backtrack.call(path)
      path.pop
      used[i] = false
    end
  end

  backtrack.call([])
  res
end
```

## Scala

```scala
object Solution {
    def permute(nums: Array[Int]): List[List[Int]] = {
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val used = Array.fill(nums.length)(false)
        val path = scala.collection.mutable.ArrayBuffer[Int]()

        def backtrack(): Unit = {
            if (path.size == nums.length) {
                result += path.toList
                return
            }
            for (i <- nums.indices) {
                if (!used(i)) {
                    used(i) = true
                    path.append(nums(i))
                    backtrack()
                    path.remove(path.size - 1)
                    used(i) = false
                }
            }
        }

        backtrack()
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn permute(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        fn backtrack(start: usize, nums: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
            if start == nums.len() {
                result.push(nums.clone());
                return;
            }
            for i in start..nums.len() {
                nums.swap(start, i);
                backtrack(start + 1, nums, result);
                nums.swap(start, i);
            }
        }
        backtrack(0, &mut nums, &mut result);
        result
    }
}
```

## Racket

```racket
(define/contract (permute nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (letrec ((remove-first
            (lambda (e l)
              (cond [(null? l) '()]
                    [(equal? (car l) e) (cdr l)]
                    [else (cons (car l) (remove-first e (cdr l)))])))
           (permute-helper
            (lambda (lst)
              (if (null? lst)
                  (list '())
                  (apply append
                         (map (lambda (x)
                                (let ((rest (remove-first x lst)))
                                  (map (lambda (p) (cons x p))
                                       (permute-helper rest))))
                              lst))))))
    (permute-helper nums)))
```

## Erlang

```erlang
-spec permute(Nums :: [integer()]) -> [[integer()]].
permute([]) ->
    [[]];
permute(L) ->
    [ [H|Tail] || H <- L,
                 Tail <- permute(lists:delete(H, L)) ].
```

## Elixir

```elixir
defmodule Solution do
  @spec permute(nums :: [integer]) :: [[integer]]
  def permute(nums) do
    permute_helper(nums)
  end

  defp permute_helper([]), do: [[]]

  defp permute_helper(nums) do
    Enum.with_index(nums)
    |> Enum.flat_map(fn {num, idx} ->
      rest = List.delete_at(nums, idx)

      for tail <- permute_helper(rest), do: [num | tail]
    end)
  end
end
```
