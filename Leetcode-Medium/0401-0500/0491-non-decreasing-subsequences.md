# 0491. Non-decreasing Subsequences

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        function<void(int)> dfs = [&](int start) {
            unordered_set<int> used;
            for (int i = start; i < (int)nums.size(); ++i) {
                if (!path.empty() && nums[i] < path.back()) continue;
                if (used.count(nums[i])) continue;
                used.insert(nums[i]);
                path.push_back(nums[i]);
                if (path.size() >= 2) res.push_back(path);
                dfs(i + 1);
                path.pop_back();
            }
        };
        dfs(0);
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void dfs(int[] nums, int start, List<Integer> path, List<List<Integer>> result) {
        if (path.size() >= 2) {
            result.add(new ArrayList<>(path));
        }
        Set<Integer> used = new HashSet<>();
        for (int i = start; i < nums.length; i++) {
            if ((path.isEmpty() || nums[i] >= path.get(path.size() - 1)) && !used.contains(nums[i])) {
                used.add(nums[i]);
                path.add(nums[i]);
                dfs(nums, i + 1, path, result);
                path.remove(path.size() - 1);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def dfs(start, path):
            if len(path) >= 2:
                res.append(path[:])
            used = set()
            for i in range(start, n):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(nums)

        def dfs(start: int, path: List[int]) -> None:
            if len(path) >= 2:
                res.append(path.copy())
            used = set()
            for i in range(start, n):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return res
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int **g_res;
static int *g_colSizes;
static int g_cnt = 0;
static int g_cap = 0;

static void addResult(int *seq, int len) {
    if (g_cnt == g_cap) {
        g_cap = g_cap ? g_cap * 2 : 128;
        g_res = realloc(g_res, g_cap * sizeof(int *));
        g_colSizes = realloc(g_colSizes, g_cap * sizeof(int));
    }
    int *copy = malloc(len * sizeof(int));
    memcpy(copy, seq, len * sizeof(int));
    g_res[g_cnt] = copy;
    g_colSizes[g_cnt] = len;
    g_cnt++;
}

static void backtrack(int *nums, int numsSize, int start, int *temp, int len) {
    if (len >= 2) {
        addResult(temp, len);
    }
    bool visited[201] = {false}; // values range -100..100
    for (int i = start; i < numsSize; ++i) {
        if ((len == 0 || nums[i] >= temp[len - 1]) && !visited[nums[i] + 100]) {
            visited[nums[i] + 100] = true;
            temp[len] = nums[i];
            backtrack(nums, numsSize, i + 1, temp, len + 1);
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findSubsequences(int* nums, int numsSize, int* returnSize, int*** returnColumnSizes) {
    g_res = NULL;
    g_colSizes = NULL;
    g_cnt = 0;
    g_cap = 0;

    int *temp = malloc(numsSize * sizeof(int));
    backtrack(nums, numsSize, 0, temp, 0);
    free(temp);

    *returnSize = g_cnt;
    *returnColumnSizes = &g_colSizes;
    return g_res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindSubsequences(int[] nums) {
        var result = new List<IList<int>>();
        Backtrack(0, new List<int>(), nums, result);
        return result;
    }

    private void Backtrack(int start, List<int> path, int[] nums, List<IList<int>> result) {
        if (path.Count >= 2) {
            result.Add(new List<int>(path));
        }
        var used = new HashSet<int>();
        for (int i = start; i < nums.Length; i++) {
            if ((path.Count == 0 || nums[i] >= path[path.Count - 1]) && !used.Contains(nums[i])) {
                used.Add(nums[i]);
                path.Add(nums[i]);
                Backtrack(i + 1, path, nums, result);
                path.RemoveAt(path.Count - 1);
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
var findSubsequences = function(nums) {
    const result = [];
    const seen = new Set();

    const dfs = (start, path) => {
        if (path.length >= 2) {
            const key = path.join(',');
            if (!seen.has(key)) {
                seen.add(key);
                result.push([...path]);
            }
        }

        const usedAtLevel = new Set();
        for (let i = start; i < nums.length; i++) {
            if ((path.length === 0 || nums[i] >= path[path.length - 1]) && !usedAtLevel.has(nums[i])) {
                usedAtLevel.add(nums[i]);
                path.push(nums[i]);
                dfs(i + 1, path);
                path.pop();
            }
        }
    };

    dfs(0, []);
    return result;
};
```

## Typescript

```typescript
function findSubsequences(nums: number[]): number[][] {
    const result = new Set<string>();
    
    function backtrack(start: number, path: number[]) {
        if (path.length >= 2) {
            result.add(path.join(','));
        }
        const used = new Set<number>();
        for (let i = start; i < nums.length; i++) {
            if ((path.length === 0 || nums[i] >= path[path.length - 1]) && !used.has(nums[i])) {
                used.add(nums[i]);
                path.push(nums[i]);
                backtrack(i + 1, path);
                path.pop();
            }
        }
    }
    
    backtrack(0, []);
    return Array.from(result).map(s => s.split(',').map(Number));
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function findSubsequences($nums) {
        $res = [];
        $set = [];
        $n = count($nums);
        $path = [];

        $dfs = function($index) use (&$dfs, &$nums, $n, &$path, &$res, &$set) {
            if (count($path) >= 2) {
                $key = implode(',', $path);
                if (!isset($set[$key])) {
                    $set[$key] = true;
                    $res[] = $path;
                }
            }

            for ($i = $index; $i < $n; $i++) {
                if (empty($path) || $nums[$i] >= end($path)) {
                    $path[] = $nums[$i];
                    $dfs($i + 1);
                    array_pop($path);
                }
            }
        };

        $dfs(0);
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func findSubsequences(_ nums: [Int]) -> [[Int]] {
        var result = Set<[Int]>()
        let n = nums.count
        
        func dfs(_ index: Int, _ path: [Int]) {
            if path.count >= 2 {
                result.insert(path)
            }
            var used = Set<Int>()
            var i = index
            while i < n {
                let val = nums[i]
                if (path.isEmpty || val >= path.last!) && !used.contains(val) {
                    used.insert(val)
                    dfs(i + 1, path + [val])
                }
                i += 1
            }
        }
        
        dfs(0, [])
        return Array(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSubsequences(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        fun backtrack(start: Int, path: MutableList<Int>) {
            if (path.size >= 2) {
                result.add(ArrayList(path))
            }
            val used = HashSet<Int>()
            for (i in start until nums.size) {
                if ((path.isEmpty() || nums[i] >= path.last()) && used.add(nums[i])) {
                    path.add(nums[i])
                    backtrack(i + 1, path)
                    path.removeAt(path.size - 1)
                }
            }
        }
        backtrack(0, mutableListOf())
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> findSubsequences(List<int> nums) {
    List<List<int>> result = [];
    Set<String> seen = {};
    List<int> path = [];

    void backtrack(int start) {
      if (path.length >= 2) {
        String key = path.join(',');
        if (!seen.contains(key)) {
          seen.add(key);
          result.add(List.from(path));
        }
      }

      Set<int> usedAtLevel = {};
      for (int i = start; i < nums.length; i++) {
        int cur = nums[i];
        if ((path.isEmpty || cur >= path.last) && !usedAtLevel.contains(cur)) {
          usedAtLevel.add(cur);
          path.add(cur);
          backtrack(i + 1);
          path.removeLast();
        }
      }
    }

    backtrack(0);
    return result;
  }
}
```

## Golang

```go
func findSubsequences(nums []int) [][]int {
	var res [][]int
	var path []int

	var dfs func(int)
	dfs = func(start int) {
		if len(path) >= 2 {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
		}
		used := make(map[int]bool)
		for i := start; i < len(nums); i++ {
			if used[nums[i]] {
				continue
			}
			if len(path) == 0 || nums[i] >= path[len(path)-1] {
				used[nums[i]] = true
				path = append(path, nums[i])
				dfs(i + 1)
				path = path[:len(path)-1]
			}
		}
	}

	dfs(0)
	return res
}
```

## Ruby

```ruby
def find_subsequences(nums)
  require 'set'
  result = Set.new

  dfs = nil
  dfs = lambda do |start_idx, path|
    result << path.clone if path.size >= 2

    used = {}
    (start_idx...nums.length).each do |i|
      next if !path.empty? && nums[i] < path[-1]
      next if used[nums[i]]
      used[nums[i]] = true
      path << nums[i]
      dfs.call(i + 1, path)
      path.pop
    end
  end

  dfs.call(0, [])
  result.to_a
end
```

## Scala

```scala
object Solution {
    def findSubsequences(nums: Array[Int]): List[List[Int]] = {
        val n = nums.length
        val result = scala.collection.mutable.HashSet[List[Int]]()
        val path = scala.collection.mutable.ListBuffer[Int]()

        def backtrack(start: Int): Unit = {
            if (path.size >= 2) result += path.toList

            val used = scala.collection.mutable.HashSet[Int]()
            var i = start
            while (i < n) {
                val cur = nums(i)
                if ((path.isEmpty || cur >= path.last) && !used.contains(cur)) {
                    used.add(cur)
                    path.append(cur)
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
use std::collections::HashSet;

impl Solution {
    pub fn find_subsequences(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut set: HashSet<Vec<i32>> = HashSet::new();
        let mut path: Vec<i32> = Vec::new();

        fn dfs(start: usize, nums: &Vec<i32>, path: &mut Vec<i32>, set: &mut HashSet<Vec<i32>>) {
            if path.len() >= 2 {
                set.insert(path.clone());
            }
            for i in start..nums.len() {
                if path.is_empty() || nums[i] >= *path.last().unwrap() {
                    path.push(nums[i]);
                    dfs(i + 1, nums, path, set);
                    path.pop();
                }
            }
        }

        dfs(0, &nums, &mut path, &mut set);
        set.into_iter().collect()
    }
}
```

## Racket

```racket
(require racket/base)

(define/contract (find-subsequences nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (result (make-hash))) ; seq -> #t
    (define (add-seq seq)
      (when (>= (length seq) 2)
        (hash-set! result seq #t)))
    (define (backtrack start seq)
      (add-seq seq)
      (let ((used (make-hash))) ; values used at this recursion depth
        (let loop ((i start))
          (when (< i n)
            (let* ((val (vector-ref v i))
                   (last-val (if (null? seq) #f (car (reverse seq)))))
              (when (or (null? seq) (<= last-val val))
                (unless (hash-has-key? used val)
                  (hash-set! used val #t)
                  (backtrack (+ i 1) (append seq (list val))))))
            (loop (+ i 1))))))
    (backtrack 0 '())
    (hash-keys result)))
```

## Erlang

```erlang
-spec find_subsequences([integer()]) -> [[integer()]].
find_subsequences(Nums) ->
    Set = dfs(Nums, [], #{}),
    maps:keys(Set).

dfs([], Curr, Set) ->
    case length(Curr) >= 2 of
        true -> maps:put(Curr, true, Set);
        false -> Set
    end;
dfs([H|T], Curr, Set) ->
    SetSkip = dfs(T, Curr, Set),
    case (Curr == [] orelse lists:last(Curr) =< H) of
        true ->
            NewCurr = Curr ++ [H],
            dfs(T, NewCurr, SetSkip);
        false -> SetSkip
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_subsequences(nums :: [integer]) :: [[integer]]
  def find_subsequences(nums) do
    set = dfs(0, [], nums, MapSet.new())
    MapSet.to_list(set)
  end

  defp dfs(idx, path, nums, set) when idx >= length(nums), do: set

  defp dfs(idx, path, nums, set) do
    Enum.reduce(idx..(length(nums) - 1), set, fn i, acc_set ->
      val = Enum.at(nums, i)

      if path == [] or val >= List.last(path) do
        new_path = path ++ [val]
        acc2 =
          if length(new_path) >= 2,
            do: MapSet.put(acc_set, new_path),
            else: acc_set

        dfs(i + 1, new_path, nums, acc2)
      else
        acc_set
      end
    end)
  end
end
```
