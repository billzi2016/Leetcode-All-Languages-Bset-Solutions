# 0040. Combination Sum II

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> path;
        dfs(0, target, candidates, path, result);
        return result;
    }
private:
    void dfs(int start, int target, const vector<int>& cand,
             vector<int>& path, vector<vector<int>>& res) {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < (int)cand.size(); ++i) {
            if (i > start && cand[i] == cand[i - 1]) continue; // skip duplicates
            if (cand[i] > target) break; // prune
            path.push_back(cand[i]);
            dfs(i + 1, target - cand[i], cand, path, res);
            path.pop_back();
        }
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> path,
                           int[] candidates, int remaining, int start) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < candidates.length && candidates[i] <= remaining; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue; // skip duplicates
            path.add(candidates[i]);
            backtrack(result, path, candidates, remaining - candidates[i], i + 1);
            path.remove(path.size() - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                cur = candidates[i]
                if cur > remaining:
                    break
                if i > start and cur == candidates[i - 1]:
                    continue
                path.append(cur)
                backtrack(i + 1, remaining - cur)
                path.pop()

        backtrack(0, target)
        return res
```

## Python3

```python
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(start, remain, path):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur = candidates[i]
                if cur > remain:
                    break
                path.append(cur)
                backtrack(i + 1, remain - cur, path)
                path.pop()

        backtrack(0, target, [])
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

typedef struct {
    int **results;
    int *colSizes;
    int count;
    int capacity;
    int *candidates;
    int candidatesSize;
    int *temp;
} Context;

static void backtrack(Context *ctx, int start, int remain, int depth) {
    if (remain == 0) {
        if (ctx->count == ctx->capacity) {
            ctx->capacity <<= 1;
            ctx->results = realloc(ctx->results, ctx->capacity * sizeof(int *));
            ctx->colSizes = realloc(ctx->colSizes, ctx->capacity * sizeof(int));
        }
        int *comb = malloc(depth * sizeof(int));
        memcpy(comb, ctx->temp, depth * sizeof(int));
        ctx->results[ctx->count] = comb;
        ctx->colSizes[ctx->count] = depth;
        ctx->count++;
        return;
    }

    for (int i = start; i < ctx->candidatesSize; ++i) {
        int val = ctx->candidates[i];
        if (val > remain) break;
        if (i > start && val == ctx->candidates[i - 1]) continue;
        ctx->temp[depth] = val;
        backtrack(ctx, i + 1, remain - val, depth + 1);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum2(int* candidates, int candidatesSize, int target,
                     int* returnSize, int*** returnColumnSizes) {
    qsort(candidates, (size_t)candidatesSize, sizeof(int), cmp_int);

    Context ctx;
    ctx.capacity = 128;
    ctx.results = malloc(ctx.capacity * sizeof(int *));
    ctx.colSizes = malloc(ctx.capacity * sizeof(int));
    ctx.count = 0;
    ctx.candidates = candidates;
    ctx.candidatesSize = candidatesSize;
    ctx.temp = malloc(candidatesSize * sizeof(int));

    backtrack(&ctx, 0, target, 0);

    free(ctx.temp);
    *returnSize = ctx.count;
    if (ctx.count == 0) {
        free(ctx.results);
        free(ctx.colSizes);
        *returnColumnSizes = NULL;
        return NULL;
    }
    *returnColumnSizes = ctx.colSizes;
    return ctx.results;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
        var results = new List<IList<int>>();
        if (candidates == null || candidates.Length == 0) return results;
        System.Array.Sort(candidates);
        Backtrack(0, target, new List<int>(), candidates, results);
        return results;
    }

    private void Backtrack(int start, int remaining, List<int> path, int[] nums, List<IList<int>> results) {
        if (remaining == 0) {
            results.Add(new List<int>(path));
            return;
        }
        for (int i = start; i < nums.Length; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue; // skip duplicates
            if (nums[i] > remaining) break; // prune
            path.Add(nums[i]);
            Backtrack(i + 1, remaining - nums[i], path, nums, results);
            path.RemoveAt(path.Count - 1);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    candidates.sort((a, b) => a - b);
    const result = [];
    const path = [];

    function backtrack(start, remaining) {
        if (remaining === 0) {
            result.push([...path]);
            return;
        }
        for (let i = start; i < candidates.length; i++) {
            const val = candidates[i];
            if (val > remaining) break; // prune since array is sorted
            if (i > start && val === candidates[i - 1]) continue; // skip duplicates
            path.push(val);
            backtrack(i + 1, remaining - val);
            path.pop();
        }
    }

    backtrack(0, target);
    return result;
};
```

## Typescript

```typescript
function combinationSum2(candidates: number[], target: number): number[][] {
    const results: number[][] = [];
    candidates.sort((a, b) => a - b);
    
    function backtrack(start: number, remaining: number, path: number[]): void {
        if (remaining === 0) {
            results.push([...path]);
            return;
        }
        for (let i = start; i < candidates.length; i++) {
            const cur = candidates[i];
            if (i > start && cur === candidates[i - 1]) continue; // skip duplicates
            if (cur > remaining) break; // prune
            path.push(cur);
            backtrack(i + 1, remaining - cur, path);
            path.pop();
        }
    }
    
    backtrack(0, target, []);
    return results;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */
    function combinationSum2($candidates, $target) {
        sort($candidates);
        $result = [];
        $temp = [];
        $len = count($candidates);

        $backtrack = function ($start, $remain) use (&$candidates, &$result, &$temp, $len, &$backtrack) {
            if ($remain == 0) {
                $result[] = $temp;
                return;
            }
            for ($i = $start; $i < $len; $i++) {
                if ($candidates[$i] > $remain) {
                    break;
                }
                if ($i > $start && $candidates[$i] == $candidates[$i - 1]) {
                    continue;
                }
                $temp[] = $candidates[$i];
                $backtrack($i + 1, $remain - $candidates[$i]);
                array_pop($temp);
            }
        };

        $backtrack(0, $target);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func combinationSum2(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var results = [[Int]]()
        let sorted = candidates.sorted()
        var current = [Int]()
        
        func backtrack(_ start: Int, _ remaining: Int) {
            if remaining == 0 {
                results.append(current)
                return
            }
            if remaining < 0 { return }
            
            for i in start..<sorted.count {
                if i > start && sorted[i] == sorted[i - 1] {
                    continue
                }
                let value = sorted[i]
                if value > remaining { break }
                current.append(value)
                backtrack(i + 1, remaining - value)
                current.removeLast()
            }
        }
        
        backtrack(0, target)
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun combinationSum2(candidates: IntArray, target: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        candidates.sort()
        val path = mutableListOf<Int>()
        fun backtrack(start: Int, remaining: Int) {
            if (remaining == 0) {
                result.add(ArrayList(path))
                return
            }
            var i = start
            while (i < candidates.size && candidates[i] <= remaining) {
                if (i > start && candidates[i] == candidates[i - 1]) {
                    i++
                    continue
                }
                path.add(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.removeAt(path.size - 1)
                i++
            }
        }
        backtrack(0, target)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> combinationSum2(List<int> candidates, int target) {
    candidates.sort();
    List<List<int>> res = [];
    List<int> path = [];

    void backtrack(int start, int remaining) {
      if (remaining == 0) {
        res.add(List.from(path));
        return;
      }
      for (int i = start; i < candidates.length; i++) {
        if (i > start && candidates[i] == candidates[i - 1]) continue;
        int cur = candidates[i];
        if (cur > remaining) break;
        path.add(cur);
        backtrack(i + 1, remaining - cur);
        path.removeLast();
      }
    }

    backtrack(0, target);
    return res;
  }
}
```

## Golang

```go
package main

import "sort"

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	var res [][]int
	var path []int

	var dfs func(start, remain int)
	dfs = func(start, remain int) {
		if remain == 0 {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		for i := start; i < len(candidates); i++ {
			if candidates[i] > remain {
				break
			}
			if i > start && candidates[i] == candidates[i-1] {
				continue
			}
			path = append(path, candidates[i])
			dfs(i+1, remain-candidates[i])
			path = path[:len(path)-1]
		}
	}

	dfs(0, target)
	return res
}
```

## Ruby

```ruby
def combination_sum2(candidates, target)
  candidates.sort!
  result = []
  dfs = nil
  dfs = lambda do |start_idx, remaining, path|
    if remaining == 0
      result << path.clone
      return
    end
    (start_idx...candidates.length).each do |i|
      val = candidates[i]
      break if val > remaining
      next if i > start_idx && val == candidates[i - 1]
      path << val
      dfs.call(i + 1, remaining - val, path)
      path.pop
    end
  end
  dfs.call(0, target, [])
  result
end
```

## Scala

```scala
object Solution {
    def combinationSum2(candidates: Array[Int], target: Int): List[List[Int]] = {
        val sorted = candidates.sorted
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val path = scala.collection.mutable.ArrayBuffer[Int]()

        def backtrack(start: Int, remaining: Int): Unit = {
            if (remaining == 0) {
                result += path.toList
                return
            }
            var i = start
            while (i < sorted.length && sorted(i) <= remaining) {
                if (i > start && sorted(i) == sorted(i - 1)) {
                    i += 1
                } else {
                    path.append(sorted(i))
                    backtrack(i + 1, remaining - sorted(i))
                    path.remove(path.length - 1)
                    i += 1
                }
            }
        }

        backtrack(0, target)
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut cand = candidates;
        cand.sort();
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut path: Vec<i32> = Vec::new();

        fn dfs(start: usize, target: i32, cand: &[i32], path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            if target == 0 {
                res.push(path.clone());
                return;
            }
            for i in start..cand.len() {
                let val = cand[i];
                if val > target {
                    break;
                }
                if i > start && cand[i] == cand[i - 1] {
                    continue;
                }
                path.push(val);
                dfs(i + 1, target - val, cand, path, res);
                path.pop();
            }
        }

        dfs(0, target, &cand, &mut path, &mut res);
        res
    }
}
```

## Racket

```racket
(define/contract (combination-sum2 candidates target)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))
  (let* ((sorted (sort candidates <))
         (n (length sorted)))
    (define (backtrack start rem cur acc)
      (cond
        [(= rem 0) (cons (reverse cur) acc)]
        [(or (< rem 0) (>= start n)) acc]
        [else
         (let loop ((i start) (acc2 acc))
           (if (>= i n)
               acc2
               (let ((val (list-ref sorted i)))
                 (if (> val rem)
                     acc2
                     (let ((new-acc (backtrack (+ i 1) (- rem val) (cons val cur) acc2)))
                       ;; skip duplicates of the current value at this recursion level
                       (let ((j (+ i 1)))
                         (let loop-skip ((k j))
                           (if (and (< k n) (= (list-ref sorted k) val))
                               (loop-skip (+ k 1))
                               (loop k new-acc))))))))))]))
    (reverse (backtrack 0 target '() '())))))
```

## Erlang

```erlang
-spec combination_sum2(Candidates :: [integer()], Target :: integer()) -> [[integer()]].
combination_sum2(Candidates, Target) ->
    Sorted = lists:sort(Candidates),
    go(Target, Sorted).

go(0, _) ->
    [[]];
go(_, []) ->
    [];
go(Target, _) when Target < 0 ->
    [];
go(Target, [H|T]) when H > Target ->
    [];
go(Target, [H|T]) ->
    Include = case go(Target - H, T) of
                  [] -> [];
                  SubCombos -> lists:map(fun(Sub) -> [H | Sub] end, SubCombos)
              end,
    NextCandidates = skip_same(H, T),
    Exclude = go(Target, NextCandidates),
    Include ++ Exclude.

skip_same(_, []) ->
    [];
skip_same(Val, [H|T]) when H =:= Val ->
    skip_same(Val, T);
skip_same(_, List) ->
    List.
```

## Elixir

```elixir
defmodule Solution do
  @spec combination_sum2(candidates :: [integer], target :: integer) :: [[integer]]
  def combination_sum2(candidates, target) do
    sorted = Enum.sort(candidates)
    dfs(sorted, target, 0, [])
  end

  defp dfs(_candidates, 0, _start, path) do
    [Enum.reverse(path)]
  end

  defp dfs(_candidates, target, _start, _path) when target < 0 do
    []
  end

  defp dfs(candidates, target, start, path) do
    len = length(candidates)

    Enum.reduce_while(start..(len - 1), [], fn i, acc ->
      if i > start && Enum.at(candidates, i) == Enum.at(candidates, i - 1) do
        {:cont, acc}
      else
        val = Enum.at(candidates, i)

        if val > target do
          {:halt, acc}
        else
          combos = dfs(candidates, target - val, i + 1, [val | path])
          {:cont, acc ++ combos}
        end
      end
    end)
  end
end
```
