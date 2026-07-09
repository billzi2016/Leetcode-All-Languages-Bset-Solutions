# 0090. Subsets II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> current;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(current);
            for (int i = start; i < (int)nums.size(); ++i) {
                if (i > start && nums[i] == nums[i - 1]) continue;
                current.push_back(nums[i]);
                backtrack(i + 1);
                current.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        backtrack(0, nums, new ArrayList<>(), res);
        return res;
    }
    
    private void backtrack(int start, int[] nums, List<Integer> path, List<List<Integer>> res) {
        res.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;
            path.add(nums[i]);
            backtrack(i + 1, nums, path, res);
            path.remove(path.size() - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        path = []

        def dfs(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []

        def backtrack(start: int, path: List[int]) -> None:
            res.append(path.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

static void dfs(int *nums, int n, int start, int depth, int *path,
                int **res, int *colSizes, int *cnt) {
    int *subset = NULL;
    if (depth > 0) {
        subset = (int *)malloc(depth * sizeof(int));
        memcpy(subset, path, depth * sizeof(int));
    }
    res[*cnt] = subset;
    colSizes[*cnt] = depth;
    (*cnt)++;

    for (int i = start; i < n; ++i) {
        if (i > start && nums[i] == nums[i - 1]) continue;
        path[depth] = nums[i];
        dfs(nums, n, i + 1, depth + 1, path, res, colSizes, cnt);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** subsetsWithDup(int* nums, int numsSize, int* returnSize, int*** returnColumnSizes) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int maxSubset = 1 << numsSize;               // maximum possible subsets
    int **res = (int **)malloc(maxSubset * sizeof(int *));
    int *colSizes = (int *)malloc(maxSubset * sizeof(int));
    int cnt = 0;
    int path[10];                                // numsSize <= 10

    dfs(nums, numsSize, 0, 0, path, res, colSizes, &cnt);

    *returnSize = cnt;
    *returnColumnSizes = colSizes;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        Array.Sort(nums);
        var result = new List<IList<int>>();
        var subset = new List<int>();
        Backtrack(0);
        return result;

        void Backtrack(int start) {
            result.Add(new List<int>(subset));
            for (int i = start; i < nums.Length; i++) {
                if (i > start && nums[i] == nums[i - 1]) continue;
                subset.Add(nums[i]);
                Backtrack(i + 1);
                subset.RemoveAt(subset.Count - 1);
            }
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
var subsetsWithDup = function(nums) {
    const res = [];
    nums.sort((a, b) => a - b);
    const backtrack = (start, path) => {
        res.push([...path]);
        for (let i = start; i < nums.length; i++) {
            if (i > start && nums[i] === nums[i - 1]) continue;
            path.push(nums[i]);
            backtrack(i + 1, path);
            path.pop();
        }
    };
    backtrack(0, []);
    return res;
};
```

## Typescript

```typescript
function subsetsWithDup(nums: number[]): number[][] {
    const result: number[][] = [];
    nums.sort((a, b) => a - b);
    const path: number[] = [];

    const backtrack = (start: number): void => {
        result.push([...path]);
        for (let i = start; i < nums.length; i++) {
            if (i > start && nums[i] === nums[i - 1]) continue;
            path.push(nums[i]);
            backtrack(i + 1);
            path.pop();
        }
    };

    backtrack(0);
    return result;
};
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsetsWithDup($nums) {
        sort($nums);
        $result = [];
        $path = [];
        $this->backtrack($nums, 0, $path, $result);
        return $result;
    }

    private function backtrack($nums, $start, &$path, &$result) {
        $result[] = $path;
        $n = count($nums);
        for ($i = $start; $i < $n; $i++) {
            if ($i > $start && $nums[$i] == $nums[$i - 1]) {
                continue;
            }
            $path[] = $nums[$i];
            $this->backtrack($nums, $i + 1, $path, $result);
            array_pop($path);
        }
    }
}
```

## Swift

```swift
class Solution {
    func subsetsWithDup(_ nums: [Int]) -> [[Int]] {
        let sorted = nums.sorted()
        var result = [[Int]]()
        var current = [Int]()
        
        func backtrack(_ start: Int) {
            result.append(current)
            for i in start..<sorted.count {
                if i > start && sorted[i] == sorted[i - 1] { continue }
                current.append(sorted[i])
                backtrack(i + 1)
                current.removeLast()
            }
        }
        
        backtrack(0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subsetsWithDup(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        nums.sort()
        val path = mutableListOf<Int>()
        fun backtrack(start: Int) {
            result.add(ArrayList(path))
            for (i in start until nums.size) {
                if (i > start && nums[i] == nums[i - 1]) continue
                path.add(nums[i])
                backtrack(i + 1)
                path.removeAt(path.lastIndex)
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
  List<List<int>> subsetsWithDup(List<int> nums) {
    nums.sort();
    List<List<int>> result = [];
    List<int> path = [];

    void dfs(int start) {
      result.add(List.from(path));
      for (int i = start; i < nums.length; i++) {
        if (i > start && nums[i] == nums[i - 1]) continue;
        path.add(nums[i]);
        dfs(i + 1);
        path.removeLast();
      }
    }

    dfs(0);
    return result;
  }
}
```

## Golang

```go
package main

import "sort"

func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	var res [][]int
	var path []int

	var backtrack func(int)
	backtrack = func(start int) {
		tmp := make([]int, len(path))
		copy(tmp, path)
		res = append(res, tmp)

		for i := start; i < len(nums); i++ {
			if i > start && nums[i] == nums[i-1] {
				continue
			}
			path = append(path, nums[i])
			backtrack(i + 1)
			path = path[:len(path)-1]
		}
	}

	backtrack(0)
	return res
}
```

## Ruby

```ruby
def subsets_with_dup(nums)
  nums.sort!
  result = []
  dfs = nil
  dfs = lambda do |index, path|
    result << path.clone
    (index...nums.length).each do |i|
      next if i > index && nums[i] == nums[i - 1]
      path << nums[i]
      dfs.call(i + 1, path)
      path.pop
    end
  end
  dfs.call(0, [])
  result
end
```

## Scala

```scala
object Solution {
    def subsetsWithDup(nums: Array[Int]): List[List[Int]] = {
        val sorted = nums.sorted
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val path = scala.collection.mutable.ArrayBuffer[Int]()

        def backtrack(start: Int): Unit = {
            result += path.toList
            var i = start
            while (i < sorted.length) {
                if (i > start && sorted(i) == sorted(i - 1)) {
                    // skip duplicates
                } else {
                    path.append(sorted(i))
                    backtrack(i + 1)
                    path.remove(path.size - 1)
                }
                i += 1
            }
        }

        backtrack(0)
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subsets_with_dup(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut res = Vec::new();
        let mut path = Vec::new();
        Self::backtrack(0, &nums, &mut path, &mut res);
        res
    }

    fn backtrack(start: usize, nums: &Vec<i32>, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        res.push(path.clone());
        for i in start..nums.len() {
            if i > start && nums[i] == nums[i - 1] {
                continue;
            }
            path.push(nums[i]);
            Self::backtrack(i + 1, nums, path, res);
            path.pop();
        }
    }
}
```

## Racket

```racket
(define/contract (subsets-with-dup nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ((sorted (sort nums <))
         (n (length sorted)))
    (let rec ((start 0) (curr '()) (res '()))
      (let ((new-res (cons (reverse curr) res)))
        (if (= start n)
            new-res
            (let loop ((i start) (acc new-res))
              (if (>= i n)
                  acc
                  (let* ((val (list-ref sorted i))
                         (with (rec (+ i 1) (cons val curr) acc))
                         (next-i (let skip ((j i))
                                   (if (and (< j n) (= (list-ref sorted j) val))
                                       (skip (+ j 1))
                                       j))))
                    (loop next-i with)))))))))
```

## Erlang

```erlang
-export([subsets_with_dup/1]).

-spec subsets_with_dup(Nums :: [integer()]) -> [[integer()]].
subsets_with_dup(Nums) ->
    Sorted = lists:sort(Nums),
    Res = dfs(0, Sorted, [], []),
    lists:reverse(Res).

dfs(Index, Sorted, Curr, Acc) ->
    Subset = lists:reverse(Curr),
    Acc1 = [Subset | Acc],
    Len = length(Sorted),
    loop(Index, Sorted, Len, Index, Curr, Acc1).

loop(I, Sorted, Len, Index, Curr, Acc) when I < Len ->
    Elem = lists:nth(I + 1, Sorted),
    Skip = (I > Index) andalso (Elem == lists:nth(I, Sorted)),
    if
        Skip ->
            loop(I + 1, Sorted, Len, Index, Curr, Acc);
        true ->
            NewCurr = [Elem | Curr],
            Acc1 = dfs(I + 1, Sorted, NewCurr, Acc),
            loop(I + 1, Sorted, Len, Index, Curr, Acc1)
    end;
loop(_, _, _, _, _, Acc) -> Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec subsets_with_dup(nums :: [integer]) :: [[integer]]
  def subsets_with_dup(nums) do
    sorted = Enum.sort(nums)
    dfs(sorted, 0, [], [])
    |> Enum.reverse()
  end

  defp dfs(nums, start, path, acc) do
    acc = [path | acc]

    len = length(nums)

    Enum.reduce(start..(len - 1), acc, fn i, acc2 ->
      if i > start && Enum.at(nums, i) == Enum.at(nums, i - 1) do
        acc2
      else
        new_path = path ++ [Enum.at(nums, i)]
        dfs(nums, i + 1, new_path, acc2)
      end
    end)
  end
end
```
