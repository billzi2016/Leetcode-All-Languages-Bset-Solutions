# 0047. Permutations II

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> path;
        vector<bool> used(nums.size(), false);
        function<void()> dfs = [&]() {
            if (path.size() == nums.size()) {
                res.push_back(path);
                return;
            }
            for (int i = 0; i < (int)nums.size(); ++i) {
                if (used[i]) continue;
                if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
                used[i] = true;
                path.push_back(nums[i]);
                dfs();
                path.pop_back();
                used[i] = false;
            }
        };
        dfs();
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        Arrays.sort(nums);
        boolean[] used = new boolean[nums.length];
        Deque<Integer> path = new ArrayDeque<>();
        backtrack(nums, used, path, res);
        return res;
    }

    private void backtrack(int[] nums, boolean[] used, Deque<Integer> path, List<List<Integer>> res) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            // skip duplicates: only use the first occurrence of a number at this depth
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.addLast(nums[i]);
            backtrack(nums, used, path, res);
            path.removeLast();
            used[i] = false;
        }
    }
}
```

## Python

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        used = [False] * n
        res = []
        path = []

        def backtrack():
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
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
class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        n = len(nums)
        used = [False] * n
        path = []
        res = []

        def backtrack():
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
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

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

static void backtrack(int *nums, int n, int *used, int *path, int depth,
                      int **res, int *colSizes, int *cnt) {
    if (depth == n) {
        int *perm = (int *)malloc(n * sizeof(int));
        memcpy(perm, path, n * sizeof(int));
        res[*cnt] = perm;
        colSizes[*cnt] = n;
        (*cnt)++;
        return;
    }
    for (int i = 0; i < n; ++i) {
        if (used[i]) continue;
        if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
        used[i] = 1;
        path[depth] = nums[i];
        backtrack(nums, n, used, path, depth + 1, res, colSizes, cnt);
        used[i] = 0;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** permuteUnique(int* nums, int numsSize, int* returnSize, int*** returnColumnSizes) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);

    int capacity = 1;
    for (int i = 2; i <= numsSize; ++i) capacity *= i;

    int **res = (int **)malloc(capacity * sizeof(int *));
    int *colSizes = (int *)malloc(capacity * sizeof(int));

    int *used = (int *)calloc(numsSize, sizeof(int));
    int *path = (int *)malloc(numsSize * sizeof(int));
    int cnt = 0;

    backtrack(nums, numsSize, used, path, 0, res, colSizes, &cnt);

    free(used);
    free(path);

    *returnSize = cnt;
    *returnColumnSizes = &colSizes;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var num in nums) {
            if (!freq.ContainsKey(num)) freq[num] = 0;
            freq[num]++;
        }

        var uniqueVals = freq.Keys.ToList();
        var counts = uniqueVals.Select(v => freq[v]).ToArray();
        var result = new List<IList<int>>();
        var path = new int[nums.Length];

        void Backtrack(int depth) {
            if (depth == nums.Length) {
                result.Add(new List<int>(path));
                return;
            }
            for (int i = 0; i < uniqueVals.Count; i++) {
                if (counts[i] == 0) continue;
                path[depth] = uniqueVals[i];
                counts[i]--;
                Backtrack(depth + 1);
                counts[i]++;
            }
        }

        Backtrack(0);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    const results = [];
    nums.sort((a, b) => a - b);
    const used = new Array(nums.length).fill(false);
    
    const backtrack = (path) => {
        if (path.length === nums.length) {
            results.push([...path]);
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.push(nums[i]);
            backtrack(path);
            path.pop();
            used[i] = false;
        }
    };
    
    backtrack([]);
    return results;
};
```

## Typescript

```typescript
function permuteUnique(nums: number[]): number[][] {
    const result: number[][] = [];
    nums.sort((a, b) => a - b);
    const used = new Array(nums.length).fill(false);
    const path: number[] = [];

    function backtrack() {
        if (path.length === nums.length) {
            result.push([...path]);
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.push(nums[i]);
            backtrack();
            path.pop();
            used[i] = false;
        }
    }

    backtrack();
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
    function permuteUnique($nums) {
        sort($nums);
        $n = count($nums);
        $res = [];
        $path = [];
        $used = array_fill(0, $n, false);

        $dfs = function() use (&$dfs, &$res, &$path, &$used, $nums, $n) {
            if (count($path) === $n) {
                $res[] = $path;
                return;
            }
            for ($i = 0; $i < $n; $i++) {
                if ($used[$i]) {
                    continue;
                }
                if ($i > 0 && $nums[$i] == $nums[$i - 1] && !$used[$i - 1]) {
                    continue;
                }
                $used[$i] = true;
                $path[] = $nums[$i];
                $dfs();
                array_pop($path);
                $used[$i] = false;
            }
        };

        $dfs();

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        var results = [[Int]]()
        let sortedNums = nums.sorted()
        var used = Array(repeating: false, count: sortedNums.count)
        var path = [Int]()
        
        func backtrack() {
            if path.count == sortedNums.count {
                results.append(path)
                return
            }
            for i in 0..<sortedNums.count {
                if used[i] { continue }
                if i > 0 && sortedNums[i] == sortedNums[i - 1] && !used[i - 1] {
                    continue
                }
                used[i] = true
                path.append(sortedNums[i])
                backtrack()
                path.removeLast()
                used[i] = false
            }
        }
        
        backtrack()
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun permuteUnique(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        if (nums.isEmpty()) return result
        nums.sort()
        val used = BooleanArray(nums.size)
        val path = mutableListOf<Int>()
        fun backtrack() {
            if (path.size == nums.size) {
                result.add(ArrayList(path))
                return
            }
            for (i in nums.indices) {
                if (used[i]) continue
                if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue
                used[i] = true
                path.add(nums[i])
                backtrack()
                path.removeAt(path.size - 1)
                used[i] = false
            }
        }
        backtrack()
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> permuteUnique(List<int> nums) {
    nums.sort();
    int n = nums.length;
    List<bool> used = List.filled(n, false);
    List<int> path = [];
    List<List<int>> result = [];

    void backtrack() {
      if (path.length == n) {
        result.add(List.from(path));
        return;
      }
      for (int i = 0; i < n; i++) {
        if (used[i]) continue;
        if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
        used[i] = true;
        path.add(nums[i]);
        backtrack();
        path.removeLast();
        used[i] = false;
      }
    }

    backtrack();
    return result;
  }
}
```

## Golang

```go
import "sort"

func permuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	used := make([]bool, n)
	var path []int
	var res [][]int

	var backtrack func()
	backtrack = func() {
		if len(path) == n {
			tmp := make([]int, n)
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		for i := 0; i < n; i++ {
			if used[i] {
				continue
			}
			if i > 0 && nums[i] == nums[i-1] && !used[i-1] {
				continue
			}
			used[i] = true
			path = append(path, nums[i])
			backtrack()
			path = path[:len(path)-1]
			used[i] = false
		}
	}

	backtrack()
	return res
}
```

## Ruby

```ruby
def permute_unique(nums)
  nums.sort!
  n = nums.length
  used = Array.new(n, false)
  result = []

  backtrack = lambda do |path|
    if path.size == n
      result << path.clone
      next
    end

    (0...n).each do |i|
      next if used[i]
      if i > 0 && nums[i] == nums[i - 1] && !used[i - 1]
        next
      end

      used[i] = true
      path << nums[i]
      backtrack.call(path)
      path.pop
      used[i] = false
    end
  end

  backtrack.call([])
  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, ListBuffer}
  
  def permuteUnique(nums: Array[Int]): List[List[Int]] = {
    val n = nums.length
    if (n == 0) return Nil
    java.util.Arrays.sort(nums)
    val visited = new Array[Boolean](n)
    val path = new ArrayBuffer[Int](n)
    val res = new ListBuffer[List[Int]]()
    
    def backtrack(): Unit = {
      if (path.size == n) {
        res += path.toList
        return
      }
      var i = 0
      while (i < n) {
        if (!visited(i)) {
          if (i > 0 && nums(i) == nums(i - 1) && !visited(i - 1)) {
            // skip duplicate
          } else {
            visited(i) = true
            path += nums(i)
            backtrack()
            path.remove(path.size - 1)
            visited(i) = false
          }
        }
        i += 1
      }
    }
    
    backtrack()
    res.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let mut used = vec![false; n];
        let mut path = Vec::with_capacity(n);
        let mut res = Vec::new();

        fn backtrack(
            nums: &Vec<i32>,
            used: &mut Vec<bool>,
            path: &mut Vec<i32>,
            res: &mut Vec<Vec<i32>>,
        ) {
            if path.len() == nums.len() {
                res.push(path.clone());
                return;
            }
            for i in 0..nums.len() {
                if used[i] {
                    continue;
                }
                if i > 0 && nums[i] == nums[i - 1] && !used[i - 1] {
                    continue;
                }
                used[i] = true;
                path.push(nums[i]);
                backtrack(nums, used, path, res);
                path.pop();
                used[i] = false;
            }
        }

        backtrack(&nums, &mut used, &mut path, &mut res);
        res
    }
}
```

## Racket

```racket
(define/contract (permute-unique nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ((sorted (list->vector (sort nums <)))      ; sorted numbers
         (n (vector-length sorted))
         (used (make-vector n #f))                ; marks if an index is used
         (path (make-vector n))                   ; current permutation being built
         (result '()))                            ; accumulator for permutations

    ;; depth = how many positions have been filled in `path`
    (define (backtrack depth)
      (if (= depth n)
          (set! result (cons (vector->list (vector-copy path)) result))
          (let loop ((i 0))
            (when (< i n)
              (cond
                ;; already used this element, skip
                [(vector-ref used i) (loop (+ i 1))]
                ;; duplicate element: skip if the previous identical element hasn't been used
                [(and (> i 0)
                      (= (vector-ref sorted i) (vector-ref sorted (- i 1)))
                      (not (vector-ref used (- i 1))))
                 (loop (+ i 1))]
                [else
                 (vector-set! used i #t)
                 (vector-set! path depth (vector-ref sorted i))
                 (backtrack (+ depth 1))
                 (vector-set! used i #f)
                 (loop (+ i 1))]))))))

    (backtrack 0)
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([permute_unique/1]).

-spec permute_unique(Nums :: [integer()]) -> [[integer()]].
permute_unique(Nums) ->
    Len = length(Nums),
    Counter = build_counter(Nums, #{}),
    backtrack(Counter, [], Len).

build_counter([], Map) -> Map;
build_counter([H|T], Map) ->
    Count = maps:get(H, Map, 0) + 1,
    NewMap = maps:put(H, Count, Map),
    build_counter(T, NewMap).

backtrack(Counter, Path, Len) when length(Path) == Len ->
    [lists:reverse(Path)];
backtrack(Counter, Path, Len) ->
    Keys = maps:keys(Counter),
    lists:foldl(fun(Key, Acc) ->
        Count = maps:get(Key, Counter),
        if Count > 0 ->
                NewCounter = maps:update_with(Key,
                                              fun(C) -> C - 1 end,
                                              Counter),
                SubRes = backtrack(NewCounter, [Key|Path], Len),
                Acc ++ SubRes;
           true -> Acc
        end
    end, [], Keys).
```

## Elixir

```elixir
defmodule Solution do
  @spec permute_unique(nums :: [integer]) :: [[integer]]
  def permute_unique(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    used = List.duplicate(false, n)
    dfs(sorted, used, [])
  end

  defp dfs(sorted, _used, path) when length(path) == length(sorted) do
    [Enum.reverse(path)]
  end

  defp dfs(sorted, used, path) do
    len = length(sorted)

    Enum.reduce(0..len - 1, [], fn i, acc ->
      cond do
        Enum.at(used, i) ->
          acc

        i > 0 and Enum.at(sorted, i) == Enum.at(sorted, i - 1) and not Enum.at(used, i - 1) ->
          acc

        true ->
          new_used = List.replace_at(used, i, true)
          perms = dfs(sorted, new_used, [Enum.at(sorted, i) | path])
          perms ++ acc
      end
    end)
  end
end
```
